"""E042 (backlog B46): lagged daily gold (XAU/USD) return -> next-day EUR/USD (Apergis 2014, AUD/USD only; EUR extension),
DEV ONLY, 1 trial.

Definitions (fixed in the backlog, R093, and pre-registered 2026-11-11 R094, before any run). Identical to E041
(`oil_lag`) except the source market (Dukascopy `xauusd` instead of the WTI CFD) and the sign, fixed from the paper's
printed negative short-run coefficients:
* Dates = sorted EUR/USD trading dates (17:00 NY roll, SPEC 2) on Monday-Friday (`relative_equity.fx_dates`).
* Quotes = bid/ask OPEN of the first 1-minute bar in [T, T+5 min) Europe/London on London date D. Bid/ask <= 0 or missing
  -> invalid, never filled, no fallback.
* G(D) = ln XAU/USD mid at 16:00 London D - ln same on the previous valid trading date.
* Position = -sign(G): gold up on D -> EUR/USD down over D -> next date.
* Trade: EUR/USD 16:05 London D -> 16:00 London on the next date. Signed return = position x (mid exit - mid entry) / PIP.
* Exclusions, counted, first reason in this order: `burn_in`, `missing_gold_quote`, `zero_signal`, `gold_jump`
  (|G| > 0.10, data-error guard), `missing_entry`, `missing_exit` (incl. last date), `entry_skipped_spread` (> 2.0 pips).
* Statistic and decision: as E041 (`evaluate_b32`, block-20 bootstrap, `decide_b34`: < 500 -> NONE; SIGNAL if mean > 1.0 pip
  AND CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE).
* Data gate first: gold empty, or valid 16:00 London gold quote at BOTH points on < 90% of dev dates with a previous date
  -> BLOCKED, 0 trials.
The signal uses quotes at or before 16:00 London on D; the trade enters at 16:05 London on D, so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import oil_lag as _ol
from .month_end_hedging import london_quotes
from .overnight_reversal import decide_b34, evaluate_b32
from .relative_equity import fx_dates

GOLD = "xauusd"
SIGNAL_HM = _ol.SIGNAL_HM
ENTRY_HM = _ol.ENTRY_HM
EXIT_HM = _ol.EXIT_HM
MAX_ABS_G = 0.10
MIN_BOTH_VALID_SHARE = 0.90
ALPHA = 0.05
MIN_MEAN_PIPS = 1.0
MIN_EVENTS = 500
BOOT_BLOCK = 20
SIGN = -1.0   # position = SIGN x sign(G): gold up -> short EUR/USD (Apergis 2014 short-run coefficients negative)
EXCLUSION_ORDER = ("burn_in", "missing_gold_quote", "zero_signal", "gold_jump", "missing_entry", "missing_exit",
                   "entry_skipped_spread")
_RENAME_COLS = {"oil_mid": "gold_mid", "prev_oil_mid": "prev_gold_mid", "o": "g"}
_RENAME_EXCL = {"missing_oil_quote": "missing_gold_quote", "oil_jump": "gold_jump"}

decide_b46 = decide_b34
evaluate = evaluate_b32


def build_days(dates, gold_q: pd.DataFrame, fx_fix: pd.DataFrame, fx_in: pd.DataFrame) -> pd.DataFrame:
    """One row per date D (E041 frame with gold columns and the reversed sign)."""
    assert _ol.MAX_ABS_O == MAX_ABS_G
    df = _ol.build_days(dates, gold_q, fx_fix, fx_in)
    if df.empty:
        return df
    df = df.rename(columns=_RENAME_COLS)
    df["excluded"] = df["excluded"].map(lambda x: _RENAME_EXCL.get(x, x) if isinstance(x, str) else None)
    df["tested"] = df["excluded"].isna()
    df["side"] = SIGN * np.sign(df["g"])
    df["signed_pips"] = df["side"] * df["move_pips"]
    return df


def frame_from_bars(fx_bars: pd.DataFrame, gold_bars: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    dates, dropped = fx_dates(fx_bars)
    df = build_days(dates, london_quotes(gold_bars, *SIGNAL_HM), london_quotes(fx_bars, *EXIT_HM),
                    london_quotes(fx_bars, *ENTRY_HM))
    return df, dropped


def data_gate(df: pd.DataFrame, gold_bars: pd.DataFrame) -> dict:
    """BLOCKED if gold is empty or both 16:00 London quotes are valid on < 90% of dates with a previous date."""
    out = {"gold_bars": int(len(gold_bars))}
    if len(gold_bars) == 0 or df.empty or len(df) < 2:
        return {**out, "ok": False, "reason": "gold data missing"}
    sub = df[~df["burn_in"]]
    both = int((sub["gold_mid"].gt(0) & sub["prev_gold_mid"].gt(0)).sum())
    share = both / len(sub)
    ok = share >= MIN_BOTH_VALID_SHARE
    return {**out, "ok": bool(ok), "dates_with_prev": int(len(sub)), "dates_both_valid": both,
            "both_valid_share": round(float(share), 4),
            "reason": None if ok else "valid 16:00 London gold quote at both points on < 90% of dates"}


events = _ol.events


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"dates": 0}
    vc = df["excluded"].value_counts()
    return {"dates": int(len(df)), **{k: int(vc.get(k, 0)) for k in EXCLUSION_ORDER}, "tested": int(df["tested"].sum())}
