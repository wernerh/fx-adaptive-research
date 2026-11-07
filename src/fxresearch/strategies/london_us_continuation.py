"""S003 London-to-US continuation (status: research candidate).

Hypothesis: when London trends strongly (large move, closes near its extreme),
the direction persists into the first part of the US session.

Entry : at US session open + entry_delay_minutes, in the London direction.
Filter: |London return| >= min_london_move_atr * ATR and close location >= min_close_loc
        (or <= 1 - min_close_loc for shorts). Optional: skip high-impact event days.
Stop  : stop_atr * ATR. Target: target_r * stop. Time stop: max_hold_minutes.

Note: the US session start (08:00 NY) is the point at which all London-session
features are known, so there is no look-ahead.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from ..backtest import Signal
from ..sessions import US


@dataclass(frozen=True)
class Params:
    min_london_move_atr: float = 0.25
    min_close_loc: float = 0.75
    entry_delay_minutes: int = 0
    stop_atr: float = 0.20
    target_r: float = 1.5
    max_hold_minutes: int = 30
    skip_dates: frozenset = field(default_factory=frozenset)  # high-impact event days


def generate_signals(bars: pd.DataFrame, feats: pd.DataFrame, p: Params = Params()) -> list[Signal]:
    out: list[Signal] = []
    for d, f in feats.iterrows():
        if d in p.skip_dates or pd.isna(f.get("atr_pips_prior")) or pd.isna(f.get("london_ret_pips")):
            continue
        atr = f["atr_pips_prior"]
        move = f["london_ret_pips"]
        if abs(move) < p.min_london_move_atr * atr:
            continue
        side = 1 if move > 0 else -1
        loc = f["london_close_loc"]
        if pd.isna(loc) or (side == 1 and loc < p.min_close_loc) or (side == -1 and loc > 1 - p.min_close_loc):
            continue
        us_start, us_end = US.window_utc(d)
        stop = p.stop_atr * atr
        out.append(Signal(
            time=us_start + pd.Timedelta(minutes=p.entry_delay_minutes), side=side,
            stop_pips=float(stop), target_pips=float(stop * p.target_r),
            max_hold_minutes=p.max_hold_minutes, strategy="london_us_continuation",
            cutoff=us_end, tag=str(d),
        ))
    return out
