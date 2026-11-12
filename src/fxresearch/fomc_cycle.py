"""E046 (backlog B54): even- vs odd-week FOMC cycle, EUR/USD daily hold, DEV ONLY, 1 trial.

Definitions (fixed in the backlog, R109, and pre-registered 2026-11-12 R110, before any run):
* Day 0 = `statement_date` of scheduled, non-cancelled meetings in the FOMC date file (unscheduled meetings ignored).
* Days are counted in Mon-Fri dates (pandas business days; US holidays NOT skipped - stated limitation).
* For trading date D: k_next = -(Mon-Fri dates from D to the next statement date S >= D) (D = S -> 0, D one weekday before S
  -> -1). If k_next >= -6 use it; else k = Mon-Fri dates since the previous statement date (D = S + 1 weekday -> 1).
  No previous statement and k_next < -6 -> `pre_cycle`.
* Cycle week: -1: k -6..-2; 0: -1..3; 1: 4..8; 2: 9..13; 3: 14..18; 4: 19..23; 5: 24..28; 6: 29..33; k > 33 -> unassigned.
* Position s = +1 in weeks 2, 4, 6; -1 in weeks -1, 1, 3, 5; week 0 excluded (statement-day effect tested in E013/E014).
* Trade (E044 convention): entry at the 20:00 NY quote on the NY calendar date before D (start of trading date D, after the
  17:00 roll), exit at the 16:55 NY quote on D (`vol_state_fix.ny_quotes`). Signed = s x (mid exit - mid entry) / PIP.
* Exclusions, counted, first reason in this order: `pre_cycle`, `unassigned`, `week0_excluded`, `missing_entry`,
  `missing_exit`, `entry_skipped_spread` (ask-bid at entry > 2.0 pips, SPEC 4).
* Statistic: `overnight_reversal.evaluate_b32` (block 20 dates, 2000 draws, seed 0). Decision `decide_b54`
  (= `overnight_reversal.decide_b34`): < 500 tested dates -> NONE; SIGNAL if mean > 1.0 pip AND CI lower > 0 AND one-sided
  t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
The position uses only the pre-announced FOMC calendar, so nothing can look ahead in prices.
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from .data import PIP
from .overnight_reversal import decide_b34, evaluate_b32
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, ny_quotes

ENTRY_HM = (20, 0)
EXIT_HM = (16, 55)
PRE_WINDOW = -6           # k_next >= -6 -> pre-meeting week -1 (or week 0 for -1)
MAX_K = 33
WEEK_BOUNDS = ((-1, -6, -2), (0, -1, 3), (1, 4, 8), (2, 9, 13), (3, 14, 18), (4, 19, 23), (5, 24, 28), (6, 29, 33))
LONG_WEEKS = (2, 4, 6)
SHORT_WEEKS = (-1, 1, 3, 5)
MIN_EVENTS = 500
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 20
EXCLUSION_ORDER = ("pre_cycle", "unassigned", "week0_excluded", "missing_entry", "missing_exit", "entry_skipped_spread")

decide_b54 = decide_b34
evaluate = evaluate_b32


def statement_dates(cal: pd.DataFrame) -> list[date]:
    """Scheduled, non-cancelled statement dates, sorted."""
    s = cal["scheduled"].astype(str).str.lower().eq("true")
    c = cal["cancelled"].astype(str).str.lower().eq("true") if "cancelled" in cal else pd.Series(False, index=cal.index)
    d = pd.to_datetime(cal.loc[s & ~c, "statement_date"]).dt.date
    return sorted(set(d))


def _bday_index(d: date) -> int:
    """Number of Mon-Fri dates from 1970-01-05 (a Monday) to d; consecutive weekdays differ by 1."""
    return int(np.busday_count(date(1970, 1, 5), d))


def cycle_k(d: date, stmts: list[date]) -> float:
    """Cycle day k of weekday d (NaN = pre_cycle)."""
    if d.weekday() >= 5:
        raise ValueError("cycle defined on Mon-Fri dates only")
    i = _bday_index(d)
    nxt = [s for s in stmts if s >= d]
    if nxt:
        k_next = -(_bday_index(nxt[0]) - i)
        if k_next >= PRE_WINDOW:
            return float(k_next)
    prev = [s for s in stmts if s < d]
    if not prev:
        return float("nan")
    return float(i - _bday_index(prev[-1]))


def cycle_week(k: float) -> float:
    """Cycle week from k; NaN if k is NaN or k > 33."""
    if np.isnan(k):
        return float("nan")
    for w, lo, hi in WEEK_BOUNDS:
        if lo <= k <= hi:
            return float(w)
    return float("nan")


def position(week: float) -> float:
    if week in LONG_WEEKS:
        return 1.0
    if week in SHORT_WEEKS:
        return -1.0
    return 0.0


def prev_weekday(d: date) -> date:
    x = d - timedelta(days=1)
    while x.weekday() >= 5:
        x -= timedelta(days=1)
    return x


def build_days(dates, stmts: list[date], q_entry: pd.DataFrame, q_exit: pd.DataFrame) -> pd.DataFrame:
    """dates: Mon-Fri trading dates. q_entry/q_exit keyed by NY calendar date (entry looked up on D - 1 calendar day)."""
    rows = []
    for d in sorted(dates):
        k = cycle_k(d, stmts)
        wk = cycle_week(k)
        k_lag = cycle_k(prev_weekday(d), stmts)
        e, x = _get(q_entry, d - timedelta(days=1)), _get(q_exit, d)
        rows.append({"date": d, "k": k, "week": wk, "week_lag1": cycle_week(k_lag),
                     "entry_mid": sum(e) / 2 if e else np.nan,
                     "entry_spread_pips": (e[1] - e[0]) / PIP if e else np.nan,
                     "exit_mid": sum(x) / 2 if x else np.nan,
                     "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan})
    df = pd.DataFrame(rows, columns=["date", "k", "week", "week_lag1", "entry_mid", "entry_spread_pips", "exit_mid",
                                     "exit_spread_pips"])
    df["side"] = [position(w) for w in df["week"]]
    df["side_lag1"] = [position(w) for w in df["week_lag1"]]
    excl = []
    for r in df.itertuples(index=False):
        if np.isnan(r.k):
            excl.append("pre_cycle")
        elif np.isnan(r.week):
            excl.append("unassigned")
        elif r.week == 0:
            excl.append("week0_excluded")
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
    df["long_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["signed_pips"] = df["side"] * df["long_pips"]
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    return df


def frame_from_bars(bars: pd.DataFrame, stmts: list[date], dates) -> pd.DataFrame:
    return build_days(dates, stmts, ny_quotes(bars, *ENTRY_HM), ny_quotes(bars, *EXIT_HM))


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"trading_dates": 0}
    vc = df["excluded"].value_counts()
    out = {"trading_dates": int(len(df))}
    for k in EXCLUSION_ORDER:
        out[k] = int(vc.get(k, 0))
    out["tested"] = int(df["tested"].sum())
    return out


def cost_summary(ev: pd.DataFrame) -> dict:
    if len(ev) == 0:
        return {"n": 0}
    return {"n": int(len(ev)),
            "mean_signed_mid_pips": round(float(ev["signed_pips"].mean()), 3),
            "mean_net_bidask_pips": round(float(ev["net_bidask_pips"].mean()), 3),
            "mean_net_spec4_pips": round(float(ev["net_spec4_pips"].mean()), 3),
            "mean_net_costs_x1_5_pips": round(float(ev["net_x1_5_pips"].mean()), 3),
            "median_spread_entry_pips": round(float(ev["entry_spread_pips"].median()), 3),
            "median_spread_exit_pips": round(float(ev["exit_spread_pips"].median()), 3)}
