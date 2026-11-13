"""E048 (backlog B58): 1-hour swing-level breakout, 5-minute break-and-retest entry, 60-minute hold, dev only.

Definitions (fixed in the backlog, R153, and pre-registered 2026-11-13 R154, before any run). Prices are mid in exact integer
units of 2 x mid x 1e5 (as E018/E045/E047): high = bid_high + ask_high, low = bid_low + ask_low, close = bid_close + ask_close.
1 pip = 20 units.

* 1h bars = UTC clock hours [H, H + 60 min) of the 1-minute bars; valid with >= 50 minute bars. close = close of its last
  1-minute bar; high/low = max/min over its minute bars.
* At the close of 1h bar k (time t_c = H + 60 min): R = max high and S = min low over the VALID bars among the 24 clock hours
  k-24 .. k-1; needs >= 20 valid bars there, and bar k itself valid, else no setup (counted `lookback_short`).
* Breakout: close(k) > R -> long setup, level L = R; close(k) < S -> short setup, L = S. Only bars whose t_c is at/after 07:00
  Europe/London and before 12:00 America/New_York (local wall clock of t_c). At most the FIRST long and the FIRST short setup per
  FX trading date (17:00 NY roll, `sessions.trading_date` of the bar's last minute, t_c - 1 min).
* Retest: UTC-aligned 5-minute bars built from the 1-minute bars with open time in [t_c, t_c + 120 min), in order (empty buckets
  do not exist). Long: first 5m bar with low <= L + 1 pip AND close > L -> retest (signal); a 5m bar with close <= L before that
  -> setup cancelled (`failed_break`). Short mirror: high >= L - 1 pip AND close < L -> retest; close >= L -> cancelled. Nothing
  within 120 min -> `no_retest`. The retest 5m bar closes at bucket start + 5 min; its signal is stamped bucket start + 4 min
  (= open time of the bucket's last nominal minute) so that `round_numbers.build_trades` fills at the first 1-minute bar at or
  after bucket start + 5 min (SPEC 4: a bar-close signal is stamped open + 1 min).
* Trades: `round_numbers.build_trades` (E018/E045/E047 fills, exclusions, order and non-overlap) with a 60-minute hold
  (coverage >= 55/60). Signed = direction x (mid open exit - mid open entry), pips. Cluster = FX trading date.
* Decision = E045/E047 rule (`post_jump.decide_b48`): < 300 trades NONE; SIGNAL mean > 1.0 AND CI lower > 0 AND p < 0.05;
  WEAK mean > 0 and (CI lower > 0 or p < 0.05); else NONE.

Nothing looks ahead: R/S use bars before k; the breakout uses bar k's close; the retest uses completed 5m bars after t_c; entry is
at or after the retest bar's close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .post_jump import decide_b48, evaluate
from .round_numbers import _SCALE
from .sessions import trading_date

MIN_EVENTS = 300
HORIZON_MIN = 60
DESCRIPTIVE_HORIZONS = (30, 120)
LOOKBACK_H = 24
MIN_VALID_LOOKBACK = 20
MIN_MINUTES_PER_HOUR = 50
RETEST_WINDOW_MIN = 120
RETEST_TOL_UNITS = 20            # 1.0 pip in 2 x mid units
LONDON_START_MIN = 7 * 60        # 07:00 Europe/London (t_c)
NY_END_MIN = 12 * 60             # 12:00 America/New_York (t_c, exclusive)

_SETUP_COLS = ["tc", "direction", "level_u", "trading_date", "outcome", "signal_ts"]
_EVENT_COLS = ["ts", "direction", "level", "trading_date"]


def _units(bars: pd.DataFrame, field: str) -> np.ndarray:
    return np.rint((bars[f"bid_{field}"].to_numpy() + bars[f"ask_{field}"].to_numpy()) * _SCALE).astype(np.int64)


def hourly_levels(bars: pd.DataFrame) -> pd.DataFrame:
    """One row per UTC clock hour (full range, empty hours included): n, high, low, close, valid, R, S, n_valid_lb, tc."""
    idx = bars.index.tz_convert("UTC")
    df = pd.DataFrame({"h": _units(bars, "high"), "l": _units(bars, "low"), "c": _units(bars, "close")},
                      index=idx.floor("60min"))
    g = df.groupby(level=0, sort=True).agg(high=("h", "max"), low=("l", "min"), close=("c", "last"), n=("c", "size"))
    full = pd.date_range(g.index.min(), g.index.max(), freq="60min")
    g = g.reindex(full)
    g["n"] = g["n"].fillna(0).astype(int)
    g["valid"] = g["n"] >= MIN_MINUTES_PER_HOUR
    hv = g["high"].where(g["valid"])
    lv = g["low"].where(g["valid"])
    g["R"] = hv.shift(1).rolling(LOOKBACK_H, min_periods=1).max()
    g["S"] = lv.shift(1).rolling(LOOKBACK_H, min_periods=1).min()
    g["n_valid_lb"] = g["valid"].astype(int).shift(1).rolling(LOOKBACK_H, min_periods=1).sum().fillna(0).astype(int)
    g["tc"] = g.index + pd.Timedelta(minutes=60)
    return g


def _in_window(tc: pd.DatetimeIndex) -> np.ndarray:
    ld = tc.tz_convert("Europe/London")
    ny = tc.tz_convert("America/New_York")
    ldm = np.asarray(ld.hour * 60 + ld.minute)
    nym = np.asarray(ny.hour * 60 + ny.minute)
    return (ldm >= LONDON_START_MIN) & (nym < NY_END_MIN)


def find_breakouts(bars: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """First long and first short 1h breakout per trading date inside the time window.
    Returns (frame tc, direction, level_u, trading_date), counts."""
    g = hourly_levels(bars)
    counts = {"hours": int(len(g)), "hours_valid": int(g["valid"].sum()), "breakouts_in_window": 0,
              "breakouts_lookback_short": 0, "setups": 0}
    if len(g) == 0:
        return pd.DataFrame(columns=["tc", "direction", "level_u", "trading_date"]), counts
    win = _in_window(pd.DatetimeIndex(g["tc"]))
    close = g["close"].to_numpy(float)
    R, S = g["R"].to_numpy(float), g["S"].to_numpy(float)
    valid = g["valid"].to_numpy(bool)
    enough = g["n_valid_lb"].to_numpy() >= MIN_VALID_LOOKBACK
    with np.errstate(invalid="ignore"):
        up = valid & win & (close > R)
        dn = valid & win & (close < S)
    counts["breakouts_lookback_short"] = int(((up | dn) & ~enough).sum())
    up &= enough
    dn &= enough
    counts["breakouts_in_window"] = int((up | dn).sum())
    tc = pd.DatetimeIndex(g["tc"])
    td = np.asarray(trading_date(tc - pd.Timedelta(minutes=1)))
    rows = []
    for flag, d, lvl in ((up, 1, R), (dn, -1, S)):
        pos = np.nonzero(flag)[0]
        if len(pos) == 0:
            continue
        first = pd.Series(pos).groupby(td[pos]).min().to_numpy()
        for i in first:
            rows.append({"tc": tc[i], "direction": d, "level_u": int(lvl[i]), "trading_date": td[i]})
    if not rows:
        return pd.DataFrame(columns=["tc", "direction", "level_u", "trading_date"]), counts
    out = pd.DataFrame(rows).sort_values(["tc", "direction"], kind="mergesort").reset_index(drop=True)
    counts["setups"] = int(len(out))
    return out, counts


def resolve_retests(bars: pd.DataFrame, setups: pd.DataFrame) -> pd.DataFrame:
    """Per setup: outcome 'retest' / 'failed_break' / 'no_retest' and signal_ts (stamp for build_trades) if retest."""
    idx = bars.index.tz_convert("UTC")
    h, l, c = _units(bars, "high"), _units(bars, "low"), _units(bars, "close")
    out = []
    for s in setups.itertuples(index=False):
        i0 = int(idx.searchsorted(s.tc, side="left"))
        i1 = int(idx.searchsorted(s.tc + pd.Timedelta(minutes=RETEST_WINDOW_MIN), side="left"))
        outcome, sig = "no_retest", pd.NaT
        if i1 > i0:
            b = idx[i0:i1].floor("5min")
            _, first = np.unique(np.asarray(b.asi8), return_index=True)
            starts = b[first]
            bounds = list(first) + [i1 - i0]
            for j in range(len(starts)):
                a, e = i0 + bounds[j], i0 + bounds[j + 1]
                close = c[e - 1]
                if s.direction > 0:
                    lo = l[a:e].min()
                    if lo <= s.level_u + RETEST_TOL_UNITS and close > s.level_u:
                        outcome = "retest"
                    elif close <= s.level_u:
                        outcome = "failed_break"
                else:
                    hi = h[a:e].max()
                    if hi >= s.level_u - RETEST_TOL_UNITS and close < s.level_u:
                        outcome = "retest"
                    elif close >= s.level_u:
                        outcome = "failed_break"
                if outcome != "no_retest":
                    if outcome == "retest":
                        sig = starts[j] + pd.Timedelta(minutes=4)
                    break
        out.append({"tc": s.tc, "direction": int(s.direction), "level_u": int(s.level_u),
                    "trading_date": s.trading_date, "outcome": outcome, "signal_ts": sig})
    if not out:
        return pd.DataFrame(columns=_SETUP_COLS)
    return pd.DataFrame(out, columns=_SETUP_COLS)


def detect_events(bars: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Retest events (ts, direction, level, trading_date) sorted by ts, the resolved setups, counts."""
    setups, counts = find_breakouts(bars)
    res = resolve_retests(bars, setups)
    vc = res["outcome"].value_counts() if len(res) else pd.Series(dtype=int)
    for k in ("retest", "failed_break", "no_retest"):
        counts[k] = int(vc.get(k, 0))
    r = res[res["outcome"] == "retest"]
    if len(r) == 0:
        return pd.DataFrame(columns=_EVENT_COLS), res, counts
    ev = pd.DataFrame({"ts": pd.DatetimeIndex(r["signal_ts"]), "direction": r["direction"].to_numpy(),
                       "level": r["level_u"].to_numpy() / (2 * _SCALE), "trading_date": r["trading_date"].to_numpy()})
    ev = ev.sort_values("ts", kind="mergesort").reset_index(drop=True)
    return ev[_EVENT_COLS], res, counts


def breakout_close_events(setups: pd.DataFrame) -> pd.DataFrame:
    """Descriptive 'no retest' variant: enter at the breakout 1h close (stamp tc - 1 min -> fill at/after tc)."""
    if len(setups) == 0:
        return pd.DataFrame(columns=_EVENT_COLS)
    ev = pd.DataFrame({"ts": pd.DatetimeIndex(setups["tc"]) - pd.Timedelta(minutes=1),
                       "direction": setups["direction"].to_numpy(),
                       "level": setups["level_u"].to_numpy() / (2 * _SCALE),
                       "trading_date": setups["trading_date"].to_numpy()})
    return ev.sort_values("ts", kind="mergesort").reset_index(drop=True)[_EVENT_COLS]


def decide_b58(res: dict) -> str:
    """Pre-registered B58 rule (= E045 decide_b52 = E047 decide_b56 = E043 decide_b48 thresholds)."""
    return decide_b48(res)


__all__ = ["DESCRIPTIVE_HORIZONS", "HORIZON_MIN", "LOOKBACK_H", "MIN_EVENTS", "MIN_MINUTES_PER_HOUR",
           "MIN_VALID_LOOKBACK", "RETEST_TOL_UNITS", "RETEST_WINDOW_MIN", "breakout_close_events", "decide_b58",
           "detect_events", "evaluate", "find_breakouts", "hourly_levels", "resolve_retests"]
