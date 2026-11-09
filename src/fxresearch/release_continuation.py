"""E026 (backlog B21): post-08:30 NY release-window continuation, calendar-free, dev only.

Definitions (fixed in the backlog, R050, and pre-registered 2026-11-09 R051, before any run):
* Quote at hh:mm NY on NY calendar date d = bid/ask OPEN of the first 1-minute bar in [hh:mm, hh:mm+5) America/New_York
  (`vol_state_fix.ny_quotes`). Missing -> NaN, never filled.
* Jump J(D) = (mid 08:45 NY - mid 08:30 NY) / PIP on date D (only dates in the trading-date set of the bars).
  D is VALID if both quotes exist; otherwise `invalid_missing_jump_quote`, counted, never an event, not in the history.
* Threshold: thr(D) = np.percentile(|J| of the 60 valid dates before D, 90) (numpy default linear interpolation; past only).
  The first 60 valid dates are burn-in.
* Event: valid D past burn-in with |J(D)| > thr(D) (strictly greater).
* Trade: position sign(J(D)) from 08:45 NY (the same 08:45 quote) to 10:45 NY on D. Exclusions, counted, first reason in this
  order: `missing_exit`, `entry_skipped_spread` (ask-bid at 08:45 > 2.0 pips, SPEC 4).
* Signed return = sign(J) x (mid 10:45 - mid 08:45) / PIP.
* Decision rule: identical thresholds to E022/E024 (`decide_b21` = `vol_state_fix.decide_b19`; block 10, 2000 draws, seed 0).
Only quotes at or before 08:45 on D (and past dates) enter the event decision, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from .data import PIP
from .sessions import trading_date
from .vol_state_fix import (COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, decide_b19,
                            ny_quotes)

WINDOW = 60
PCTL = 90
JUMP_START_HM = (8, 30)
JUMP_END_HM = (8, 45)            # also the entry
EXIT_HM = (10, 45)
ALT_EXITS_HM = {"exit_0930": (9, 30), "exit_1200": (12, 0)}   # descriptive horizons only
ALT_PCTLS = (80, 95)                                            # descriptive thresholds only


def _first_friday(d: date) -> bool:
    return d.weekday() == 4 and d.day <= 7


def build_days(dates, q_start: pd.DataFrame, q_end: pd.DataFrame, q_exit: pd.DataFrame,
               alt_exits: dict[str, pd.DataFrame] | None = None, window: int = WINDOW, pctl: float = PCTL) -> pd.DataFrame:
    """One row per date in `dates` (sorted): jump, validity, past-only threshold, event flag, trade, exclusions, returns."""
    alt_exits = alt_exits or {}
    rows = []
    for d in sorted(dates):
        s, e, x = _get(q_start, d), _get(q_end, d), _get(q_exit, d)
        row = {"date": d,
               "start_mid": sum(s) / 2 if s else np.nan,
               "entry_mid": sum(e) / 2 if e else np.nan,
               "entry_spread_pips": (e[1] - e[0]) / PIP if e else np.nan,
               "exit_mid": sum(x) / 2 if x else np.nan,
               "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan}
        for k, q in alt_exits.items():
            a = _get(q, d)
            row[k + "_mid"] = sum(a) / 2 if a else np.nan
        rows.append(row)
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["jump_pips"] = (df["entry_mid"] - df["start_mid"]) / PIP
    df["valid"] = df["jump_pips"].notna()
    df = add_threshold(df, window, pctl)
    df["is_event"] = df["valid"] & df["threshold_pips"].notna() & (df["jump_pips"].abs() > df["threshold_pips"])
    excl = []
    for r in df.itertuples(index=False):
        if not r.valid:
            excl.append("invalid_missing_jump_quote")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tradable"] = df["excluded"].isna()
    df["tested"] = df["is_event"] & df["tradable"]
    sign = np.sign(df["jump_pips"])
    df["side"] = sign
    df["signed_pips"] = sign * (df["exit_mid"] - df["entry_mid"]) / PIP
    for k in alt_exits:
        df["signed_" + k + "_pips"] = sign * (df[k + "_mid"] - df["entry_mid"]) / PIP
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    df["first_friday"] = [_first_friday(d) for d in df["date"]]
    return df


def add_threshold(df: pd.DataFrame, window: int = WINDOW, pctl: float = PCTL, col: str = "threshold_pips") -> pd.DataFrame:
    """Past-only rolling percentile of |J| over the previous `window` valid dates; NaN on invalid and burn-in dates."""
    df = df.copy()
    v = df[df["valid"]]
    a = v["jump_pips"].abs().to_numpy()
    thr = np.full(len(v), np.nan)
    for i in range(window, len(v)):
        thr[i] = np.percentile(a[i - window:i], pctl)
    df[col] = np.nan
    df.loc[v.index, col] = thr
    return df


def frame_from_bars(bars: pd.DataFrame, window: int = WINDOW, pctl: float = PCTL) -> pd.DataFrame:
    dates = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    alts = {k: ny_quotes(bars, *hm) for k, hm in ALT_EXITS_HM.items()}
    return build_days(dates, ny_quotes(bars, *JUMP_START_HM), ny_quotes(bars, *JUMP_END_HM), ny_quotes(bars, *EXIT_HM),
                      alts, window, pctl)


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"trading_dates": 0, "events_tested": 0}
    ev = df[df["is_event"]]
    vc = ev["excluded"].value_counts()
    valid = df[df["valid"]]
    return {
        "trading_dates": int(len(df)),
        "valid_dates": int(df["valid"].sum()),
        "invalid_missing_jump_quote": int((~df["valid"]).sum()),
        "burn_in": int(min(WINDOW, len(valid))),
        "post_burn_in_valid": int(valid["threshold_pips"].notna().sum()),
        "events": int(df["is_event"].sum()),
        "missing_exit": int(vc.get("missing_exit", 0)),
        "entry_skipped_spread": int(vc.get("entry_skipped_spread", 0)),
        "events_tested": int(df["tested"].sum()),
    }


def decide_b21(res: dict) -> str:
    """Pre-registered E026 rule (thresholds identical to E022/E024): SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0
    AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE."""
    return decide_b19(res)
