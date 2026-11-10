"""E037 (backlog B35 + B36): relative equity performance -> next-day EUR/USD (Hau & Rey 2006, lagged extension), DEV ONLY,
2 trials in one experiment.

Definitions (fixed in the backlog, R079, and pre-registered 2026-11-10 R080, before any run):
* Dates = sorted EUR/USD trading dates (17:00 NY roll, SPEC 2) of the (dev) bars that fall on Monday-Friday. "Previous valid
  trading date" of D = the date before D in this list; "next" = the date after D. Weekend trading-date artefacts (if any) are
  dropped and counted (`weekend_trading_dates_dropped`).
* Quotes = bid/ask OPEN of the first 1-minute bar in [T, T+5 min) Europe/London on London calendar date D (E011 rule,
  `month_end_hedging.london_quotes`). 16:00 London always falls inside trading date D (it is 10:00-12:00 NY).
* Index mids (EU Stocks 50 CFD `eusidxeur`, US 500 CFD `usa500idxusd`): mid at 16:00 London on D. **No holiday fallback**: a missing
  index quote at either end skips the date (`missing_index_quote`).
* S1(D) = [ln EU(D) - ln EU(prev)] - [ln US(D) - ln US(prev)]. Position B35 = -sign(S1): US outperformed -> long EUR/USD.
* S20(D) = same with the date 20 places before D in the list instead of prev. Position B36 = -sign(S20).
  Burn-in: the first date has no prev (B35), the first 20 dates have no D-20 (B36): counted `burn_in`.
* Trade (both arms): EUR/USD from the 16:05 London quote on D to the 16:00 London quote on the next date (weekends held).
  Signed return = position x (mid exit - mid entry) / PIP.
* Exclusions per arm, counted, first reason in this order: `burn_in`, `missing_index_quote`, `zero_signal`, `missing_entry`,
  `missing_exit` (incl. no next date), `entry_skipped_spread` (ask-bid at entry > 2.0 pips, SPEC 4).
* Statistic per arm: `overnight_reversal.evaluate_b32` (mean, median, SD, hit, one-sided t, moving-block bootstrap 95% CI, block 20
  dates, 2000 draws, seed 0). Decision: `decide_b35` (= `overnight_reversal.decide_b32`): < 500 tested dates -> NONE; SIGNAL if
  mean > 1.0 pip AND CI lower > 0 AND one-sided t p < 0.025 (Bonferroni, 2 trials); WEAK if mean > 0 and (CI lower > 0 or
  p < 0.025); else NONE.
* Data gate (first): either index series empty, or no 16:00 London index quote (either index) on > 10% of dev dates -> BLOCKED,
  0 trials used.
The signal uses index quotes at or before 16:00 London on D; the trade enters at 16:05 London on D, so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .data import PIP
from .fixes import month_end_flag
from .month_end_hedging import EU_INDEX, US_INDEX, london_quotes  # noqa: F401  (re-exported for the run script)
from .overnight_reversal import decide_b32, evaluate_b32
from .sessions import trading_date
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS

SIGNAL_HM = (16, 0)
ENTRY_HM = (16, 5)
EXIT_HM = (16, 0)
SMOOTH_N = 20
MAX_MISSING_INDEX_SHARE = 0.10
ALPHA = 0.025
MIN_MEAN_PIPS = 1.0
MIN_EVENTS = 500
BOOT_BLOCK = 20
EXCLUSION_ORDER = ("burn_in", "missing_index_quote", "zero_signal", "missing_entry", "missing_exit", "entry_skipped_spread")
ARMS = {"b35": 1, "b36": SMOOTH_N}

decide_b35 = decide_b32
decide_b36 = decide_b32
evaluate = evaluate_b32


def _mid(q: pd.DataFrame, d):
    if d is None or d not in q.index:
        return np.nan
    b, a = q.loc[d, "bid_open"], q.loc[d, "ask_open"]
    if pd.isna(b) or pd.isna(a) or b <= 0 or a <= 0:
        return np.nan
    return (float(b) + float(a)) / 2


def _spread(q: pd.DataFrame, d):
    if d is None or d not in q.index:
        return np.nan
    b, a = q.loc[d, "bid_open"], q.loc[d, "ask_open"]
    return (float(a) - float(b)) / PIP if not (pd.isna(b) or pd.isna(a)) else np.nan


def fx_dates(bars: pd.DataFrame) -> tuple[list, int]:
    """Sorted Mon-Fri trading dates of the bars, and the number of weekend trading dates dropped."""
    all_d = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    wk = [d for d in all_d if d.weekday() < 5]
    return wk, len(all_d) - len(wk)


def build_days(dates, eu_q: pd.DataFrame, us_q: pd.DataFrame, fx_fix: pd.DataFrame, fx_in: pd.DataFrame) -> pd.DataFrame:
    """One row per date D: index mids, S1/S20, both arms' side, trade, exclusions, costs, contemporaneous move."""
    dates = sorted(dates)
    eu = np.array([_mid(eu_q, d) for d in dates])
    us = np.array([_mid(us_q, d) for d in dates])
    rows = []
    for i, d in enumerate(dates):
        nxt = dates[i + 1] if i + 1 < len(dates) else None
        prev = dates[i - 1] if i >= 1 else None
        row = {"date": d, "prev_date": prev, "next_date": nxt, "eu_mid": eu[i], "us_mid": us[i],
               "entry_mid": _mid(fx_in, d), "entry_spread_pips": _spread(fx_in, d),
               "exit_mid": _mid(fx_fix, nxt), "exit_spread_pips": _spread(fx_fix, nxt),
               "fix_mid": _mid(fx_fix, d), "prev_fix_mid": _mid(fx_fix, prev)}
        for arm, lag in ARMS.items():
            if i >= lag:
                j = i - lag
                s_eu = np.log(eu[i] / eu[j]) if eu[i] > 0 and eu[j] > 0 else np.nan
                s_us = np.log(us[i] / us[j]) if us[i] > 0 and us[j] > 0 else np.nan
                row[f"{arm}_burn_in"] = False
            else:
                s_eu = s_us = np.nan
                row[f"{arm}_burn_in"] = True
            row[f"{arm}_s_eu"], row[f"{arm}_s_us"] = s_eu, s_us
            row[f"{arm}_s"] = s_eu - s_us
        rows.append(row)
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["move_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["contemp_move_pips"] = (df["fix_mid"] - df["prev_fix_mid"]) / PIP   # 16:00 prev -> 16:00 D (descriptive)
    for arm in ARMS:
        excl = []
        for r in df.itertuples(index=False):
            s = getattr(r, f"{arm}_s")
            if getattr(r, f"{arm}_burn_in"):
                excl.append("burn_in")
            elif np.isnan(s):
                excl.append("missing_index_quote")
            elif s == 0:
                excl.append("zero_signal")
            elif np.isnan(r.entry_mid):
                excl.append("missing_entry")
            elif np.isnan(r.exit_mid):
                excl.append("missing_exit")
            elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
                excl.append("entry_skipped_spread")
            else:
                excl.append(None)
        df[f"{arm}_excluded"] = excl
        df[f"{arm}_tested"] = df[f"{arm}_excluded"].isna()
        df[f"{arm}_side"] = -np.sign(df[f"{arm}_s"])
        df[f"{arm}_signed_pips"] = df[f"{arm}_side"] * df["move_pips"]
    df["weekday"] = pd.to_datetime(df["date"]).dt.dayofweek
    df["month_end"] = month_end_flag(pd.Index(df["date"])).to_numpy()
    df["next_is_month_end"] = df["month_end"].shift(-1, fill_value=False).astype(bool)
    return df


def frame_from_bars(fx_bars: pd.DataFrame, eu_bars: pd.DataFrame, us_bars: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    dates, dropped = fx_dates(fx_bars)
    df = build_days(dates, london_quotes(eu_bars, *SIGNAL_HM), london_quotes(us_bars, *SIGNAL_HM),
                    london_quotes(fx_bars, *EXIT_HM), london_quotes(fx_bars, *ENTRY_HM))
    return df, dropped


def data_gate(df: pd.DataFrame, eu_bars: pd.DataFrame, us_bars: pd.DataFrame) -> dict:
    """Pre-registered gate: BLOCKED if an index series is empty or no 16:00 London index quote on > 10% of dates."""
    out = {"eu_bars": int(len(eu_bars)), "us_bars": int(len(us_bars))}
    if len(eu_bars) == 0 or len(us_bars) == 0 or df.empty:
        return {**out, "ok": False, "reason": "index data missing"}
    miss = int((df["eu_mid"].isna() | df["us_mid"].isna()).sum())
    share = miss / len(df)
    ok = share <= MAX_MISSING_INDEX_SHARE
    return {**out, "ok": bool(ok), "dates": int(len(df)), "dates_missing_index_quote": miss,
            "missing_share": round(float(share), 4),
            "reason": None if ok else "missing 16:00 London index quote on > 10% of dates"}


def arm_events(df: pd.DataFrame, arm: str) -> pd.DataFrame:
    ev = df[df[f"{arm}_tested"]].copy()
    ev["signed_pips"] = ev[f"{arm}_signed_pips"]
    ev["side"] = ev[f"{arm}_side"]
    ev["net_bidask_pips"] = ev["signed_pips"] - (ev["entry_spread_pips"] + ev["exit_spread_pips"]) / 2
    ev["net_spec4_pips"] = ev["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    ev["net_x1_5_pips"] = ev["signed_pips"] - 1.5 * (ev["signed_pips"] - ev["net_spec4_pips"])
    return ev


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"dates": 0}
    out = {"dates": int(len(df))}
    for arm in ARMS:
        vc = df[f"{arm}_excluded"].value_counts()
        out.update({f"{arm}_{k}": int(vc.get(k, 0)) for k in EXCLUSION_ORDER})
        out[f"{arm}_tested"] = int(df[f"{arm}_tested"].sum())
    return out
