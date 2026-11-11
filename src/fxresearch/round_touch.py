"""E045 (backlog B52): take-profit reversal at round numbers, rejected touches (Osler 2003), dev only.

Definitions (fixed in the backlog, R102, and pre-registered 2026-11-11 R103, before any run):
* Prices in exact 1e-5 units of 2 x mid (as E018 `round_numbers._to_units`): close c(t) = bid_close + ask_close,
  high h(t) = bid_high + ask_high, low l(t) = bid_low + ask_low. Levels L = k * 0.0050 (+ offset for control levels).
* Bars t-1 and t must be in the same FX trading date (`sessions.trading_date`, 17:00 NY roll).
* Up-touch of L at bar t: c(t-1) < L, h(t) >= L, c(t) < L. Down-touch: c(t-1) > L, l(t) <= L, c(t) > L.
  If one bar touches several levels (either side), the level nearest c(t) counts (exact tie: the up-touch level; fixed now).
* Only the FIRST touch event (either side) of each level per trading date counts, and a level already crossed by close
  (E018 crossing: c(t'-1) < L <= c(t') or c(t'-1) > L >= c(t'), any crossed level, same trading date) at an earlier bar
  t' < t of the same trading date is not eligible.
* Position s = -1 after an up-touch, +1 after a down-touch (fade back from the level).
* Trades: `round_numbers.build_trades` unchanged (E018 conventions: entry open of first bar >= t + 1 min (<= +5), exit open of
  first bar >= entry + 60 min (<= +5), >= 55/60 bars, roll [16:30, 18:30) NY at entry or exit, entry spread > 2.0 pips, overlap).
  Signed = s x (mid open exit - mid open entry), pips.
* Statistic and decision = E043: one-sided t-test, date-cluster bootstrap (trading dates, 2000 draws, seed 0);
  < 300 events NONE; SIGNAL mean > 1.0 AND CI lower > 0 AND p < 0.05; WEAK mean > 0 and (CI lower > 0 or p < 0.05); else NONE.

Nothing looks ahead: the event uses bars t-1 and t only, and the trade starts at t + 1 min or later.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .post_jump import decide_b48, evaluate
from .round_numbers import CONTROL_OFFSET, LEVEL_STEP, _SCALE, _to_units
from .sessions import trading_date

MIN_EVENTS = 300  # = post_jump.MIN_EVENTS (B52 rule)


def _units(bars: pd.DataFrame, field: str) -> np.ndarray:
    return np.rint((bars[f"bid_{field}"].to_numpy() + bars[f"ask_{field}"].to_numpy()) * _SCALE).astype(np.int64)


def detect_touches(bars: pd.DataFrame, offset: float = 0.0, step: float = LEVEL_STEP) -> pd.DataFrame:
    """Eligible first rejected touches. Columns: ts (bar t), direction (position s), level, trading_date, side (+1 up-touch)."""
    cols = ["ts", "direction", "level", "trading_date", "side"]
    c, h, low = _units(bars, "close"), _units(bars, "high"), _units(bars, "low")
    s, o = _to_units(step), _to_units(offset)
    c, h, low = c - o, h - o, low - o
    td = np.asarray(trading_date(bars.index))
    if len(c) < 2:
        return pd.DataFrame(columns=cols)
    prev, cur, hi, lo = c[:-1], c[1:], h[1:], low[1:]
    same = td[:-1] == td[1:]
    # up-touch: lowest level strictly above max(prev, cur) must be <= high
    up_k = np.floor_divide(np.maximum(prev, cur), s) + 1
    up = same & (up_k * s <= hi)
    # down-touch: highest level strictly below min(prev, cur) must be >= low
    dn_k = -np.floor_divide(-np.minimum(prev, cur), s) - 1
    dn = same & (dn_k * s >= lo)
    d_up = up_k * s - cur
    d_dn = cur - dn_k * s
    pick_up = up & (~dn | (d_up <= d_dn))
    pick_dn = dn & ~pick_up
    ev_i = np.nonzero(pick_up | pick_dn)[0]
    if len(ev_i) == 0:
        return pd.DataFrame(columns=cols)
    side = np.where(pick_up[ev_i], 1, -1)
    k = np.where(side > 0, up_k[ev_i], dn_k[ev_i])
    ev = pd.DataFrame({"pos": ev_i + 1, "side": side, "level_k": k, "trading_date": td[ev_i + 1]})
    ev = ev.drop_duplicates(subset=["trading_date", "level_k"], keep="first")
    # first close-crossing position of each (trading date, level), all crossed levels counted
    fl_p, fl_c = np.floor_divide(prev, s), np.floor_divide(cur, s)
    ce_p, ce_c = -np.floor_divide(-prev, s), -np.floor_divide(-cur, s)
    moved = same & ((fl_c > fl_p) | (ce_c < ce_p))
    first_cross: dict = {}
    for j in np.nonzero(moved)[0]:
        if cur[j] > prev[j]:
            ks = range(int(np.floor_divide(prev[j], s)) + 1, int(np.floor_divide(cur[j], s)) + 1)   # prev < L <= cur
        else:
            ks = range(int(-np.floor_divide(-cur[j], s)), int(-np.floor_divide(-prev[j], s)))       # cur <= L < prev
        for kk in ks:
            key = (td[j + 1], kk)
            if key not in first_cross:
                first_cross[key] = j + 1
    fc = np.array([first_cross.get((d, int(kk)), np.iinfo(np.int64).max)
                   for d, kk in zip(ev["trading_date"], ev["level_k"])], dtype=np.int64)
    ev = ev[ev["pos"].to_numpy() <= fc - 1].copy()   # crossing must not be at an EARLIER bar (strictly before t)
    ev = ev.sort_values("pos").reset_index(drop=True)
    out = pd.DataFrame({
        "ts": bars.index[ev["pos"].to_numpy()],
        "direction": -ev["side"].to_numpy(),
        "level": np.round((ev["level_k"].to_numpy() * s + o) / (2 * _SCALE), 5),
        "trading_date": ev["trading_date"].to_numpy(),
        "side": ev["side"].to_numpy(),
    })
    return out[cols]


def crossed_within_hold(bars: pd.DataFrame, trades: pd.DataFrame) -> np.ndarray:
    """Descriptive: True if the touched level is crossed by mid close on a bar in [entry, exit)."""
    if len(trades) == 0:
        return np.array([], dtype=bool)
    idx = bars.index
    cm = (bars["bid_close"].to_numpy() + bars["ask_close"].to_numpy()) / 2
    out = []
    for tr in trades.itertuples(index=False):
        i0, i1 = int(idx.searchsorted(tr.entry_ts)), int(idx.searchsorted(tr.exit_ts))
        seg = cm[i0:i1]
        lvl = float(tr.level)
        if len(seg) == 0:
            out.append(False)
        elif tr.direction < 0:   # up-touch, level above
            out.append(bool(seg.max() >= lvl - 1e-9))
        else:
            out.append(bool(seg.min() <= lvl + 1e-9))
    return np.array(out, dtype=bool)


def decide_b52(res: dict) -> str:
    """Pre-registered B52 rule (identical thresholds to E043 decide_b48: 300 events, 1.0 pip, CI lower > 0, p < 0.05)."""
    return decide_b48(res)


__all__ = ["CONTROL_OFFSET", "MIN_EVENTS", "crossed_within_hold", "decide_b52", "detect_touches", "evaluate"]
