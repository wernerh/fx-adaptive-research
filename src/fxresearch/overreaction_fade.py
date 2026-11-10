"""E029 (backlog B24): next-morning fade after an overreaction day, VAL ONLY.

Definitions (fixed in the backlog, R055, and pre-registered 2026-11-10 R058, before any run):
* Trading date D starts 17:00 NY on the previous NY calendar date (SPEC 2, `sessions.trading_date`).
* Open quote of D = bid/ask OPEN of the first 1-minute bar in [17:00, 17:05) NY whose trading date is D
  (`overreaction_day.open_quotes`). Close quote of D = first bar in [16:55, 17:00) NY on NY calendar date D
  (`vol_state_fix.ny_quotes`). Missing -> NaN, never filled.
* R(D) = (mid close of D - mid open of D) / PIP. D is VALID if both quotes exist; otherwise `invalid_missing_signal_quote`, counted,
  never an event, not in the history. Valid Fridays stay in the history (only their trade is excluded).
* m(D), s(D) = mean and sample SD (ddof=1) of R over the 60 valid dates before D (past only). First 60 valid dates are burn-in.
* Event: valid D past burn-in with R(D) > m + 2s or R(D) < m - 2s (strict).
* Trade: position -sign(R(D) - m(D)) on the next trading date N = D + 1 calendar day. Entry = first bar in [17:05, 17:10) NY whose
  trading date is N (i.e. 17:05 NY on calendar date D, after the roll); exit = first bar in [02:00, 02:05) NY on NY calendar date N.
  Exclusions, counted, first reason in this order: `friday_excluded` (D is a Friday; the weekend gap belongs to B17),
  `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at 17:05 > 2.0 pips, SPEC 4).
* Signed return = -sign x (mid 02:00 - mid 17:05) / PIP.
* Decision rule: thresholds identical to E028 (`decide_b24` = `overreaction_day.decide_b23`) with the pre-registered block-5
  moving-block bootstrap (2000 draws, seed 0) in `overreaction_day.evaluate_b23`.
Only quotes at or before 16:55 NY on D (and past dates) enter the event decision; the trade starts after it, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from .data import PIP
from .overreaction_day import _event, _first_friday, add_bands, decide_b23, evaluate_b23, open_quotes
from .sessions import trading_date
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, ny_quotes

WINDOW = 60
K = 2.0
ALT_KS = (1.5, 2.5)              # descriptive only
OPEN_HM = (17, 0)
CLOSE_HM = (16, 55)
ENTRY_HM = (17, 5)               # start of the next trading date, after the roll
EXIT_HM = (2, 0)
ALT_EXIT_HM = (3, 0)             # descriptive only
BOOT_BLOCK = 5
FRIDAY = 4

evaluate_b24 = evaluate_b23


def decide_b24(res: dict) -> str:
    """Pre-registered E029 rule (thresholds identical to E028): SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND
    one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE."""
    return decide_b23(res)


def _mid(q):
    return sum(q) / 2 if q else np.nan


def _spread(q):
    return (q[1] - q[0]) / PIP if q else np.nan


def build_days(dates, q_open: pd.DataFrame, q_close: pd.DataFrame, q_entry: pd.DataFrame, q_exit: pd.DataFrame,
               q_exit_alt: pd.DataFrame | None = None, window: int = WINDOW, k: float = K) -> pd.DataFrame:
    """One row per trading date D in `dates` (sorted). q_open/q_entry keyed by trading date, q_close keyed by NY calendar date D,
    q_exit/q_exit_alt keyed by NY calendar date N = D + 1."""
    if q_exit_alt is None:
        q_exit_alt = pd.DataFrame(columns=["bid_open", "ask_open"])
    rows = []
    for d in sorted(dates):
        n = d + timedelta(days=1)
        o, c, e, x, x3 = _get(q_open, d), _get(q_close, d), _get(q_entry, n), _get(q_exit, n), _get(q_exit_alt, n)
        rows.append({"date": d, "next_date": n, "open_mid": _mid(o), "close_mid": _mid(c),
                     "entry_mid": _mid(e), "entry_spread_pips": _spread(e),
                     "exit_mid": _mid(x), "exit_spread_pips": _spread(x),
                     "exit_alt_mid": _mid(x3), "exit_alt_spread_pips": _spread(x3)})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["r_pips"] = (df["close_mid"] - df["open_mid"]) / PIP
    df["valid"] = df["r_pips"].notna()
    df = add_bands(df, window)
    df["is_event"] = _event(df, k)
    for ka in ALT_KS:
        df[f"is_event_k{ka}"] = _event(df, ka)
    excl = []
    for r in df.itertuples(index=False):
        if not r.valid:
            excl.append("invalid_missing_signal_quote")
        elif r.date.weekday() == FRIDAY:
            excl.append("friday_excluded")
        elif np.isnan(r.entry_mid):
            excl.append("missing_entry")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tradable"] = df["excluded"].isna()
    df["tested"] = df["is_event"] & df["tradable"]
    side = np.sign(df["r_pips"] - df["hist_mean_pips"])      # direction of the overreaction
    df["side"] = side
    df["signed_pips"] = -side * (df["exit_mid"] - df["entry_mid"]) / PIP
    df["signed_alt_exit_pips"] = -side * (df["exit_alt_mid"] - df["entry_mid"]) / PIP
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    df["first_friday"] = [_first_friday(d) for d in df["date"]]
    return df


def frame_from_bars(bars: pd.DataFrame, window: int = WINDOW, k: float = K) -> pd.DataFrame:
    dates = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    return build_days(dates, open_quotes(bars, *OPEN_HM), ny_quotes(bars, *CLOSE_HM), open_quotes(bars, *ENTRY_HM),
                      ny_quotes(bars, *EXIT_HM), ny_quotes(bars, *ALT_EXIT_HM), window, k)


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"trading_dates": 0, "events_tested": 0}
    ev = df[df["is_event"]]
    vc = ev["excluded"].value_counts()
    valid = df[df["valid"]]
    return {
        "trading_dates": int(len(df)),
        "valid_dates": int(df["valid"].sum()),
        "invalid_missing_signal_quote": int((~df["valid"]).sum()),
        "burn_in": int(min(WINDOW, len(valid))),
        "post_burn_in_valid": int(valid["hist_sd_pips"].notna().sum()),
        "events": int(df["is_event"].sum()),
        "events_positive": int((ev["side"] > 0).sum()),
        "events_negative": int((ev["side"] < 0).sum()),
        "friday_excluded": int(vc.get("friday_excluded", 0)),
        "missing_entry": int(vc.get("missing_entry", 0)),
        "missing_exit": int(vc.get("missing_exit", 0)),
        "entry_skipped_spread": int(vc.get("entry_skipped_spread", 0)),
        "events_tested": int(df["tested"].sum()),
    }
