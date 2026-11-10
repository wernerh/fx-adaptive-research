"""E031 (backlog B26): USD depreciation after the Tokyo fix on gotobi dates, dev only.

Pre-registered 2026-11-10 R063, before any run. Every parameter below was fixed in the backlog (R060) or in the E031
methodology before any data were touched. Parent E011 (post-fix window, all dates); sibling E030 (B25, pre-fix, gotobi).

* Gotobi dates, universe, quote rule, exclusion order, statistic and bootstrap: exactly as E030 (`gotobi_fix`), reused here.
* Trade on a gotobi date: LONG EUR/USD from 09:55 to 10:55 Asia/Tokyo. Signed return = +(mid exit - mid entry) / PIP.
* Coverage: >= 55 of the 60 one-minute bars in [09:55, 10:55) Tokyo. Spread cap: ask-bid at 09:55 > 2.0 pips -> skipped.
* Decision (`decide_b26`): identical to `decide_b25` (SIGNAL if mean > 1.0 pip AND block-20 CI lower > 0 AND one-sided t p < 0.05;
  WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE; < 40 events -> NONE).
* Descriptive only: the pre-fix move (mid 09:55 - mid 08:55 Tokyo, raw, unsigned) to condition the post-fix return on its sign
  (exploratory), and the last half hour 10:25 -> 10:55 (`late_signed_pips`).
The gotobi flag is a pure calendar function and the pre-fix move ends at the entry quote, so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .data import PIP
from .gotobi_fix import (ALPHA, BOOT_BLOCK, BOOT_N, MAX_ENTRY_SPREAD_PIPS, MIN_MEAN_PIPS, MIN_WINDOW_BARS, TOKYO,
                         build_days, cost_summary, counts, decide_b25, evaluate, gotobi_info, local_quotes, universe,
                         window_bar_counts)

ENTRY_HM = (9, 55)
EXIT_HM = (10, 55)
LATE_HM = (10, 25)              # descriptive last half hour 10:25 -> 10:55
PRE_HM = (8, 55)                # descriptive pre-fix move 08:55 -> 09:55
SIDE = 1                        # long EUR/USD (USD sold back after the fix)

__all__ = ["ENTRY_HM", "EXIT_HM", "LATE_HM", "PRE_HM", "SIDE", "TOKYO", "ALPHA", "BOOT_BLOCK", "BOOT_N",
           "MAX_ENTRY_SPREAD_PIPS", "MIN_MEAN_PIPS", "MIN_WINDOW_BARS", "frame_from_bars", "evaluate", "decide_b26",
           "counts", "cost_summary", "gotobi_info"]


def frame_from_bars(bars: pd.DataFrame, side: int = SIDE) -> pd.DataFrame:
    df = build_days(universe(bars), local_quotes(bars, TOKYO, *ENTRY_HM), local_quotes(bars, TOKYO, *EXIT_HM),
                    local_quotes(bars, TOKYO, *LATE_HM), window_bar_counts(bars, TOKYO, ENTRY_HM, EXIT_HM), side=side)
    if df.empty:
        return df
    pre = local_quotes(bars, TOKYO, *PRE_HM)
    pre_mid = pd.Series((pre["bid_open"] + pre["ask_open"]) / 2, index=pre.index)
    df["pre_mid"] = [float(pre_mid.get(d, np.nan)) for d in df["date"]]
    df["pre_move_pips"] = (df["entry_mid"] - df["pre_mid"]) / PIP
    return df


def decide_b26(res: dict) -> str:
    """Pre-registered E031 rule (B26): identical to the E030 rule."""
    return decide_b25(res)
