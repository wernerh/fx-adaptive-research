"""E047 (backlog B56): pivot-point R1/S1 first touch, continuation ("inverse pivot", Johnsson & Frykmer 2019), dev only.

Definitions (fixed in the backlog, R124, and pre-registered 2026-11-12 R125, before any run):
* Day = UTC calendar date; bars on a Sunday (UTC) belong to the following Monday's date; Saturday bars are dropped.
* Levels of date d from the previous date d-1 that has bars (Monday's previous date = Friday), mid in exact 1e-5 units of
  2 x mid (as E018/E045): H = max(bid_high + ask_high), L = min(bid_low + ask_low), C = bid_close + ask_close of the last bar.
  P = (H + L + C)/3, R1 = 2P - L, S1 = 2P - H. Held exactly as 3 x R1 = 2H - L + 2C and 3 x S1 = 2L - H + 2C.
  d-1 needs >= 1,000 bars, else date d is excluded (counted).
* R1 touch at bar t (bars t-1 and t on the same date d): c(t-1) < R1 <= h(t) -> s = +1 (long, continuation).
  S1 touch: c(t-1) > S1 >= l(t) -> s = -1 (short). Only the FIRST touch of each level per date. If that first-touch bar also
  satisfies the other level's touch condition, the event is skipped (counted, `both_touch`).
* Trades: `round_numbers.build_trades` (E018/E045 fills, exclusions and order) with a 120-minute hold (coverage >= 110/120).
  Signed = s x (mid open exit - mid open entry), pips. The date-cluster bootstrap resamples UTC dates (column `trading_date`
  carries the UTC day key here).
* Decision = E045 rule (`post_jump.decide_b48`): < 300 events NONE; SIGNAL mean > 1.0 AND CI lower > 0 AND p < 0.05;
  WEAK mean > 0 and (CI lower > 0 or p < 0.05); else NONE.

Nothing looks ahead: levels use only the previous date; the event uses bars t-1 and t; the trade starts at t + 1 min or later.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .post_jump import decide_b48, evaluate
from .round_numbers import _SCALE, _to_units

MIN_EVENTS = 300
HORIZON_MIN = 120
DESCRIPTIVE_HORIZONS = (60, 180)
MIN_PREV_BARS = 1000
CONTROL_SHIFT = 0.0023
BRACKET_FRAC = 0.0015            # thesis multiple 0.15% of P (descriptive only)
BRACKET_MAX_MIN = 1440           # descriptive bracket resolved within 24 h, else unresolved


def day_key(index: pd.DatetimeIndex) -> np.ndarray:
    """UTC date; Sunday -> Monday; Saturday -> NaT (dropped)."""
    idx = index.tz_convert("UTC")
    d = idx.normalize().tz_localize(None)
    wd = idx.weekday
    d = d + pd.to_timedelta(np.where(wd == 6, 1, 0), unit="D")
    d = pd.DatetimeIndex(d).where(wd != 5)
    return np.asarray(d, dtype="datetime64[ns]")


def _units(bars: pd.DataFrame, field: str) -> np.ndarray:
    return np.rint((bars[f"bid_{field}"].to_numpy() + bars[f"ask_{field}"].to_numpy()) * _SCALE).astype(np.int64)


def daily_levels(bars: pd.DataFrame) -> pd.DataFrame:
    """Per date d: n_prev (bars of d-1), r1_3, s1_3, p_3 (3 x level in 2*mid 1e-5 units), valid (n_prev >= 1000)."""
    dk = day_key(bars.index)
    keep = ~np.isnat(dk)
    df = pd.DataFrame({"d": dk[keep], "h": _units(bars, "high")[keep], "l": _units(bars, "low")[keep],
                       "c": _units(bars, "close")[keep]})
    g = df.groupby("d", sort=True).agg(H=("h", "max"), L=("l", "min"), C=("c", "last"), n=("c", "size"))
    prev = g.shift(1)
    out = pd.DataFrame(index=g.index)
    out["n_prev"] = prev["n"].fillna(0).astype(int)
    H, L, C = prev["H"], prev["L"], prev["C"]
    out["p_3"] = H + L + C
    out["r1_3"] = 2 * H - L + 2 * C
    out["s1_3"] = 2 * L - H + 2 * C
    out["valid"] = out["n_prev"] >= MIN_PREV_BARS
    return out


def detect_events(bars: pd.DataFrame, shift: float = 0.0) -> tuple[pd.DataFrame, dict]:
    """First R1 / S1 touches per date (levels shifted by `shift` for the control). Returns (events, counts)."""
    cols = ["ts", "direction", "level", "trading_date", "leg", "pivot"]
    counts = {"dates": 0, "dates_excluded_prev_bars": 0, "both_touch": 0}
    if len(bars) < 2:
        return pd.DataFrame(columns=cols), counts
    lv = daily_levels(bars)
    counts["dates"] = int(len(lv))
    counts["dates_excluded_prev_bars"] = int((~lv["valid"]).sum())
    sh3 = 3 * _to_units(shift)
    dk = day_key(bars.index)
    c3, h3, l3 = 3 * _units(bars, "close"), 3 * _units(bars, "high"), 3 * _units(bars, "low")
    m = lv.reindex(pd.DatetimeIndex(dk))
    valid = m["valid"].fillna(False).to_numpy(bool)
    r1 = m["r1_3"].to_numpy(float) + sh3
    s1 = m["s1_3"].to_numpy(float) + sh3
    same = np.zeros(len(dk), bool)
    same[1:] = (dk[1:] == dk[:-1]) & ~np.isnat(dk[1:])
    ok = same & valid
    prev_c = np.empty_like(c3)
    prev_c[0] = c3[0]
    prev_c[1:] = c3[:-1]
    r_t = ok & (prev_c < r1) & (r1 <= h3)
    s_t = ok & (prev_c > s1) & (s1 >= l3)
    rows = []
    for flag, other, d, leg, lvl in ((r_t, s_t, 1, "R1", r1), (s_t, r_t, -1, "S1", s1)):
        pos = np.nonzero(flag)[0]
        if len(pos) == 0:
            continue
        first = pd.Series(pos).groupby(dk[pos]).min().to_numpy()
        for i in first:
            if other[i]:
                counts["both_touch"] += 1
                continue
            rows.append({"ts": bars.index[i], "direction": d, "level": round(lvl[i] / (6 * _SCALE), 6),
                         "trading_date": pd.Timestamp(dk[i]).date(), "leg": leg,
                         "pivot": round(m["p_3"].to_numpy(float)[i] / (6 * _SCALE), 6)})
    if not rows:
        return pd.DataFrame(columns=cols), counts
    ev = pd.DataFrame(rows).sort_values("ts", kind="mergesort").reset_index(drop=True)
    return ev[cols], counts


def bracket_outcomes(bars: pd.DataFrame, trades: pd.DataFrame, events: pd.DataFrame) -> pd.Series:
    """Descriptive thesis bracket: target/stop = entry mid +- 0.15% x P in the trade direction, first hit from the entry bar.
    Returns 'win' / 'loss' / 'both_same_bar' / 'unresolved' per trade."""
    if len(trades) == 0:
        return pd.Series([], dtype=object)
    idx = bars.index
    mh = (bars["bid_high"].to_numpy() + bars["ask_high"].to_numpy()) / 2
    ml = (bars["bid_low"].to_numpy() + bars["ask_low"].to_numpy()) / 2
    mo = (bars["bid_open"].to_numpy() + bars["ask_open"].to_numpy()) / 2
    piv = dict(zip(events["ts"], events["pivot"]))
    out = []
    for tr in trades.itertuples(index=False):
        i0 = int(idx.searchsorted(tr.entry_ts))
        i1 = int(idx.searchsorted(tr.entry_ts + pd.Timedelta(minutes=BRACKET_MAX_MIN)))
        w = BRACKET_FRAC * float(piv[tr.event_ts])
        e = mo[i0]
        up_hit = mh[i0:i1] >= e + w
        dn_hit = ml[i0:i1] <= e - w
        any_hit = np.nonzero(up_hit | dn_hit)[0]
        if len(any_hit) == 0:
            out.append("unresolved")
            continue
        j = any_hit[0]
        if up_hit[j] and dn_hit[j]:
            out.append("both_same_bar")
        elif (up_hit[j] and tr.direction > 0) or (dn_hit[j] and tr.direction < 0):
            out.append("win")
        else:
            out.append("loss")
    return pd.Series(out, index=trades.index)


def decide_b56(res: dict) -> str:
    """Pre-registered B56 rule (= E045 decide_b52 = E043 decide_b48 thresholds)."""
    return decide_b48(res)


__all__ = ["BRACKET_FRAC", "CONTROL_SHIFT", "DESCRIPTIVE_HORIZONS", "HORIZON_MIN", "MIN_EVENTS", "MIN_PREV_BARS",
           "bracket_outcomes", "daily_levels", "day_key", "decide_b56", "detect_events", "evaluate"]
