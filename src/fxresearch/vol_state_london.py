"""E024 (backlog B20): post-London-fix EUR appreciation on high-volatility dates, dev only.

Pre-registered 2026-11-09 R046, before any run. Identical vol-state definition to E022 (`vol_state_fix`: previous trading
date's mid range strictly above the rolling 67th percentile of the 60 valid dates before it, 90% coverage, past only,
60-date burn-in). The one variable changed relative to the unconditional relatives E007 / E017 is this conditioning.

* Trade for a high-vol D: LONG EUR/USD from 11:05 NY to 16:00 NY on NY calendar date D (after the 5-minute WM/R London 4pm
  fix window at 11:00 NY; exit before 16:30 NY per the R030 lesson). Quote = bid/ask open of the first bar in [hh:mm, hh:mm+5)
  NY. Exclusions as E022: missing_entry, missing_exit, entry_skipped_spread (> 2.0 pips at 11:05).
* Signed return = +(mid exit - mid entry) / PIP.
* Decision rule: identical to E022 (`decide_b20` = `decide_b19`).
Descriptive only: FOMC statement days (14:00 NY statement inside the hold) share and the result excluding them.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from .vol_state_fix import decide_b19, frame_from_bars as _frame

ENTRY_HM = (11, 5)
EXIT_HM = (16, 0)
SIDE = 1                          # long EUR/USD (USD depreciates after the London fix)


def frame_from_bars(bars: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    return _frame(bars, entry_hm=ENTRY_HM, exit_hm=EXIT_HM, side=SIDE)


def decide_b20(res: dict) -> str:
    """Pre-registered E024 rule, identical to E022: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided
    t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE."""
    return decide_b19(res)


def fomc_statement_dates(path: Path) -> set[date]:
    """Scheduled, non-cancelled FOMC statement dates from data/calendars/fomc_dates.csv."""
    cal = pd.read_csv(path)
    cal = cal[cal["scheduled"].astype(str).str.lower().eq("true") & ~cal["cancelled"].astype(str).str.lower().eq("true")]
    return {pd.Timestamp(x).date() for x in cal["statement_date"]}


def flag_fomc(df: pd.DataFrame, dates: set[date]) -> pd.DataFrame:
    df = df.copy()
    df["fomc_day"] = [d in dates for d in df["date"]] if len(df) else []
    return df
