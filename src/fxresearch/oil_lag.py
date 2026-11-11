"""E041 (backlog B45): lagged daily WTI oil return -> next-day EUR/USD (Ferraro, Rogoff & Rossi 2012/2015, EUR extension),
DEV ONLY, 1 trial.

Definitions (fixed in the backlog, R088, and pre-registered 2026-11-11 R091, before any run):
* Dates = sorted EUR/USD trading dates (17:00 NY roll, SPEC 2) of the (dev) bars that fall on Monday-Friday
  (`relative_equity.fx_dates`). "Previous" / "next" valid trading date = neighbour in this list (weekends and holidays held).
* Quotes = bid/ask OPEN of the first 1-minute bar in [T, T+5 min) Europe/London on London calendar date D (E011 rule,
  `month_end_hedging.london_quotes`, DST-aware). A quote with bid or ask <= 0 or missing is invalid (never filled, no fallback).
* WTI mid (Dukascopy CFD `lightcmdusd`) at 16:00 London on D. O(D) = ln WTI(D) - ln WTI(prev).
* Position = +sign(O): oil up -> USD weaker -> long EUR/USD (sign stated before data).
* Trade: EUR/USD from the 16:05 London quote on D to the 16:00 London quote on the next date (E037 convention).
  Signed return = position x (mid exit - mid entry) / PIP.
* Exclusions, counted, first reason in this order: `burn_in` (first date), `missing_oil_quote` (either end invalid),
  `zero_signal` (O == 0), `oil_jump` (|O| > 0.10: roll gap / April 2020 episode), `missing_entry`, `missing_exit`
  (incl. the last date), `entry_skipped_spread` (ask-bid at entry > 2.0 pips, SPEC 4).
* Statistic: `overnight_reversal.evaluate_b32` (mean, median, SD, hit, one-sided t, moving-block bootstrap 95% CI, block 20
  dates, 2000 draws, seed 0). Decision: `decide_b45` (= `overnight_reversal.decide_b34`): < 500 tested dates -> NONE; SIGNAL if
  mean > 1.0 pip AND CI lower > 0 AND one-sided t p < 0.05 (1 trial); WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
* Data gate (first): WTI series empty, or a valid WTI quote at BOTH 16:00 London points (D and prev) on < 90% of the dev dates
  that have a previous date -> BLOCKED, 0 trials used.
The signal uses WTI quotes at or before 16:00 London on D; the trade enters at 16:05 London on D, so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .data import PIP
from .month_end_hedging import london_quotes
from .overnight_reversal import decide_b34, evaluate_b32
from .relative_equity import _mid, _spread, fx_dates
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS

OIL = "lightcmdusd"
SIGNAL_HM = (16, 0)
ENTRY_HM = (16, 5)
EXIT_HM = (16, 0)
MAX_ABS_O = 0.10
MIN_BOTH_VALID_SHARE = 0.90
ALPHA = 0.05
MIN_MEAN_PIPS = 1.0
MIN_EVENTS = 500
BOOT_BLOCK = 20
EXCLUSION_ORDER = ("burn_in", "missing_oil_quote", "zero_signal", "oil_jump", "missing_entry", "missing_exit",
                   "entry_skipped_spread")

decide_b45 = decide_b34
evaluate = evaluate_b32


def build_days(dates, oil_q: pd.DataFrame, fx_fix: pd.DataFrame, fx_in: pd.DataFrame) -> pd.DataFrame:
    """One row per date D: WTI mids, O, side, trade, exclusion, costs inputs, contemporaneous move."""
    dates = sorted(dates)
    oil = np.array([_mid(oil_q, d) for d in dates], dtype=float)
    rows = []
    for i, d in enumerate(dates):
        nxt = dates[i + 1] if i + 1 < len(dates) else None
        prev = dates[i - 1] if i >= 1 else None
        o = np.log(oil[i] / oil[i - 1]) if i >= 1 and oil[i] > 0 and oil[i - 1] > 0 else np.nan
        rows.append({"date": d, "prev_date": prev, "next_date": nxt, "oil_mid": oil[i],
                     "prev_oil_mid": oil[i - 1] if i >= 1 else np.nan, "o": o, "burn_in": i == 0,
                     "entry_mid": _mid(fx_in, d), "entry_spread_pips": _spread(fx_in, d),
                     "exit_mid": _mid(fx_fix, nxt), "exit_spread_pips": _spread(fx_fix, nxt),
                     "fix_mid": _mid(fx_fix, d), "prev_fix_mid": _mid(fx_fix, prev)})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["move_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["contemp_move_pips"] = (df["fix_mid"] - df["prev_fix_mid"]) / PIP   # 16:00 prev -> 16:00 D (descriptive)
    excl = []
    for r in df.itertuples(index=False):
        if r.burn_in:
            excl.append("burn_in")
        elif np.isnan(r.o):
            excl.append("missing_oil_quote")
        elif r.o == 0:
            excl.append("zero_signal")
        elif abs(r.o) > MAX_ABS_O:
            excl.append("oil_jump")
        elif np.isnan(r.entry_mid):
            excl.append("missing_entry")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tested"] = df["excluded"].isna()
    df["side"] = np.sign(df["o"])
    df["signed_pips"] = df["side"] * df["move_pips"]
    df["weekday"] = pd.to_datetime(df["date"]).dt.dayofweek
    return df


def frame_from_bars(fx_bars: pd.DataFrame, oil_bars: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    dates, dropped = fx_dates(fx_bars)
    df = build_days(dates, london_quotes(oil_bars, *SIGNAL_HM), london_quotes(fx_bars, *EXIT_HM),
                    london_quotes(fx_bars, *ENTRY_HM))
    return df, dropped


def data_gate(df: pd.DataFrame, oil_bars: pd.DataFrame) -> dict:
    """Pre-registered gate: BLOCKED if WTI is empty or both 16:00 London quotes are valid on < 90% of dates with a prev date."""
    out = {"oil_bars": int(len(oil_bars))}
    if len(oil_bars) == 0 or df.empty or len(df) < 2:
        return {**out, "ok": False, "reason": "oil data missing"}
    sub = df[~df["burn_in"]]
    both = int((sub["oil_mid"].gt(0) & sub["prev_oil_mid"].gt(0)).sum())
    share = both / len(sub)
    ok = share >= MIN_BOTH_VALID_SHARE
    return {**out, "ok": bool(ok), "dates_with_prev": int(len(sub)), "dates_both_valid": both,
            "both_valid_share": round(float(share), 4),
            "reason": None if ok else "valid 16:00 London WTI quote at both points on < 90% of dates"}


def events(df: pd.DataFrame) -> pd.DataFrame:
    ev = df[df["tested"]].copy()
    ev["net_bidask_pips"] = ev["signed_pips"] - (ev["entry_spread_pips"] + ev["exit_spread_pips"]) / 2
    ev["net_spec4_pips"] = ev["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    ev["net_x1_5_pips"] = ev["signed_pips"] - 1.5 * (ev["signed_pips"] - ev["net_spec4_pips"])
    return ev


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"dates": 0}
    vc = df["excluded"].value_counts()
    return {"dates": int(len(df)), **{k: int(vc.get(k, 0)) for k in EXCLUSION_ORDER}, "tested": int(df["tested"].sum())}
