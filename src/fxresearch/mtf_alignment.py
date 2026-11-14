"""E049 (backlog B59): multi-timeframe trend alignment (1h + 30m + 15m agree), 5-minute EMA20-cross trigger, 60-minute hold,
dev only.

Definitions (fixed in the backlog, R153, and pre-registered 2026-11-14 R156, before any run). Prices are mid closes in exact
integer units of 2 x mid x 1e5 (close = bid_close + ask_close, as E018/E045/E047/E048). 1 pip = 20 units.

* Bars of length m minutes (m in 60, 30, 15, 5, 10) are UTC-aligned buckets [start, start + m) of the 1-minute bars; a bar
  exists when the bucket holds >= 1 minute bar (empty buckets do not exist); close = close of its last 1-minute bar.
  The bar is complete at end = start + m.
* EMA20 per timeframe: pandas ewm(span=20, adjust=False) over the existing bars of that timeframe in time order, NaN for the
  first 19 bars (min_periods=20).
* Trend sign of a timeframe at time T: the last COMPLETED bar is the bucket ending exactly at floor(T, m) (i.e. start =
  floor(T, m) - m). If that bucket does not exist the sign is 0 (`htf_missing`). sign = +1 if close > EMA20, -1 if close <
  EMA20, 0 if equal or EMA undefined. State at T = +1 (BULL) if all three of 1h/30m/15m are +1, -1 (BEAR) if all -1, else 0.
* Trigger: trigger-timeframe bar j (5m for the rule; 10m descriptive) with close time T = start + m in [07:00 Europe/London,
  12:00 America/New_York) (local wall clock of T, as E048). Bar j-1 must be the immediately preceding bucket (start - m),
  else no cross. Up-cross: close(j-1) <= EMA(j-1) and close(j) > EMA(j); down-cross mirror (close(j-1) >= EMA(j-1) and
  close(j) < EMA(j)). Signal = up-cross with state BULL at T (long) or down-cross with state BEAR at T (short).
* The signal is stamped start + m - 1 min (open time of the bucket's last nominal minute) so that `round_numbers.build_trades`
  fills at the first 1-minute bar at or after T (SPEC 4 bar-close rule). Trading date = `sessions.trading_date(T - 1 min)`.
* Trades: `round_numbers.build_trades` (E018/E045/E047/E048 fills, exclusions, non-overlap: signals during an open trade are
  skipped and counted `overlap`) with a 60-minute hold. Decision = `post_jump.decide_b48` (E045/E047/E048 thresholds).

Nothing looks ahead: every bar used at T ends at or before T; entry is at or after T.
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
EMA_SPAN = 20
TREND_TFS = (60, 30, 15)
TRIGGER_TF = 5
ALT_TRIGGER_TF = 10
LONDON_START_MIN = 7 * 60        # 07:00 Europe/London (T)
NY_END_MIN = 12 * 60             # 12:00 America/New_York (T, exclusive)

_EVENT_COLS = ["ts", "direction", "level", "trading_date"]


def tf_bars(bars: pd.DataFrame, minutes: int) -> pd.DataFrame:
    """Existing UTC-aligned bars of `minutes`: index = start, columns close (units), n, ema, end."""
    idx = bars.index.tz_convert("UTC")
    c = np.rint((bars["bid_close"].to_numpy() + bars["ask_close"].to_numpy()) * _SCALE).astype(np.int64)
    df = pd.DataFrame({"c": c}, index=idx.floor(f"{minutes}min"))
    g = df.groupby(level=0, sort=True).agg(close=("c", "last"), n=("c", "size"))
    g["ema"] = g["close"].astype(float).ewm(span=EMA_SPAN, adjust=False, min_periods=EMA_SPAN).mean()
    g["end"] = g.index + pd.Timedelta(minutes=minutes)
    return g


def _sign(g: pd.DataFrame) -> pd.Series:
    """Trend sign per bar, indexed by bar END time."""
    s = np.sign(g["close"].to_numpy(float) - g["ema"].to_numpy(float))
    s = np.where(np.isnan(s), 0, s).astype(int)
    return pd.Series(s, index=pd.DatetimeIndex(g["end"]))


def trend_state(bars: pd.DataFrame, times: pd.DatetimeIndex) -> tuple[np.ndarray, np.ndarray]:
    """(state, htf_missing) at each time T: state in {-1, 0, +1}; htf_missing True if any timeframe's last bucket is absent."""
    times = pd.DatetimeIndex(times)
    signs, missing = [], np.zeros(len(times), bool)
    for m in TREND_TFS:
        s = _sign(tf_bars(bars, m))
        key = times.floor(f"{m}min")
        v = s.reindex(key)
        missing |= v.isna().to_numpy()
        signs.append(v.fillna(0).to_numpy(int))
    S = np.vstack(signs) if signs else np.zeros((0, len(times)), int)
    state = np.where((S == 1).all(axis=0), 1, np.where((S == -1).all(axis=0), -1, 0))
    return state, missing


def _in_window(t: pd.DatetimeIndex) -> np.ndarray:
    ld = t.tz_convert("Europe/London")
    ny = t.tz_convert("America/New_York")
    ldm = np.asarray(ld.hour * 60 + ld.minute)
    nym = np.asarray(ny.hour * 60 + ny.minute)
    return (ldm >= LONDON_START_MIN) & (nym < NY_END_MIN)


def crosses(bars: pd.DataFrame, minutes: int = TRIGGER_TF) -> pd.DataFrame:
    """In-window EMA20 crosses of the trigger timeframe: columns start, T, cross (+1 up / -1 down), close_u."""
    g = tf_bars(bars, minutes)
    if len(g) < 2:
        return pd.DataFrame(columns=["start", "T", "cross", "close_u"])
    st = pd.DatetimeIndex(g.index)
    c, e = g["close"].to_numpy(float), g["ema"].to_numpy(float)
    contiguous = np.zeros(len(g), bool)
    contiguous[1:] = (st[1:] - st[:-1]) == pd.Timedelta(minutes=minutes)
    pc, pe = np.r_[np.nan, c[:-1]], np.r_[np.nan, e[:-1]]
    with np.errstate(invalid="ignore"):
        up = contiguous & (pc <= pe) & (c > e)
        dn = contiguous & (pc >= pe) & (c < e)
    T = pd.DatetimeIndex(g["end"])
    sel = (up | dn) & _in_window(T)
    out = pd.DataFrame({"start": st[sel], "T": T[sel], "cross": np.where(up[sel], 1, -1),
                        "close_u": c[sel].astype(np.int64)})
    return out.reset_index(drop=True)


def _events(cx: pd.DataFrame, direction: np.ndarray) -> pd.DataFrame:
    keep = direction != 0
    T = pd.DatetimeIndex(cx["T"])[keep]
    if len(T) == 0:
        return pd.DataFrame(columns=_EVENT_COLS)
    ev = pd.DataFrame({"ts": T - pd.Timedelta(minutes=1), "direction": direction[keep].astype(int),
                       "level": cx["close_u"].to_numpy()[keep] / (2 * _SCALE),
                       "trading_date": np.asarray(trading_date(T - pd.Timedelta(minutes=1)))})
    return ev.sort_values("ts", kind="mergesort").reset_index(drop=True)[_EVENT_COLS]


def detect_events(bars: pd.DataFrame, trigger_minutes: int = TRIGGER_TF, aligned: bool = True) -> tuple[pd.DataFrame, dict]:
    """Signal events (ts stamped T - 1 min, direction, level = trigger close, trading_date) and counts.
    aligned=False is the descriptive control: every in-window cross, direction = cross direction."""
    cx = crosses(bars, trigger_minutes)
    counts = {"crosses_in_window": int(len(cx)), "crosses_up": int((cx["cross"] == 1).sum()) if len(cx) else 0,
              "crosses_down": int((cx["cross"] == -1).sum()) if len(cx) else 0,
              "htf_missing": 0, "state_bull": 0, "state_bear": 0, "signals": 0}
    if len(cx) == 0:
        return pd.DataFrame(columns=_EVENT_COLS), counts
    cross = cx["cross"].to_numpy(int)
    if aligned:
        state, miss = trend_state(bars, pd.DatetimeIndex(cx["T"]))
        counts["htf_missing"] = int(miss.sum())
        counts["state_bull"] = int((state == 1).sum())
        counts["state_bear"] = int((state == -1).sum())
        direction = np.where(cross == state, cross, 0)
    else:
        direction = cross
    ev = _events(cx, direction)
    counts["signals"] = int(len(ev))
    return ev, counts


def decide_b59(res: dict) -> str:
    """Pre-registered B59 rule (= E048 decide_b58 = E045/E047 thresholds)."""
    return decide_b48(res)


__all__ = ["ALT_TRIGGER_TF", "DESCRIPTIVE_HORIZONS", "EMA_SPAN", "HORIZON_MIN", "MIN_EVENTS", "TREND_TFS", "TRIGGER_TF",
           "crosses", "decide_b59", "detect_events", "evaluate", "tf_bars", "trend_state"]
