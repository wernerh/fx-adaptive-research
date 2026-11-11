"""E040 (backlog B43): post-FOMC reversal of the pre-statement EUR/USD drift, 12-24 h after the statement. DEV ONLY, 1 trial.

Pre-registered 2026-11-11 R089 in experiments/2026-11-11_E040_post_fomc_reversal/ (Lee & Wang 2025, abstract only).
* Events: scheduled, not cancelled FOMC statement dates t (statement 14:00 America/New_York).
* Quotes = bid/ask OPEN of the first 1-minute bar in [T, T+5 min) NY (E011 rule, `vol_state_fix.ny_quotes`); missing -> excluded.
  A = 16:00 NY on prev business day of t; B = 13:55 NY on t; E = 02:00 NY on t+1; X = 14:00 NY on t+1 (t+1 = next calendar day).
* P = (mid B - mid A) / pip; side = -sign(P); r = (mid X - mid E) / pip; signed = side x r.
* Exclusions, first reason in order: not_trading_day, missing_pre, zero_signal, missing_entry, missing_exit, entry_skipped_spread.
* Decision (`decide_b43`): < 40 tested -> NONE; SIGNAL if mean > 1.0 pip AND i.i.d. bootstrap CI lower > 0 AND one-sided t p < 0.05;
  WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
"""
from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .fomc import prev_business_day
from .metrics import block_bootstrap_mean_ci
from .sessions import NY
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, ny_quotes

PRE_START_HM = (16, 0)     # previous business day
PRE_END_HM = (13, 55)      # statement day
STATEMENT_HM = (14, 0)     # descriptive 0-12 h window start
ENTRY_HM = (2, 0)          # t+1, 12 h after the statement
EXIT_HM = (14, 0)          # t+1, 24 h after the statement
ALPHA = 0.05
MIN_MEAN_PIPS = 1.0
MIN_EVENTS = 40
BOOT_BLOCK = 1             # i.i.d. bootstrap: events ~6 weeks apart
BOOT_N = 2000

EXCLUSION_ORDER = ("not_trading_day", "missing_pre", "zero_signal", "missing_entry", "missing_exit", "entry_skipped_spread")


def _mid(q):
    return sum(q) / 2 if q else np.nan


def _spr(q):
    return (q[1] - q[0]) / PIP if q else np.nan


def ny_dates_with_bars(bars: pd.DataFrame) -> set:
    return {pd.Timestamp(x).date() for x in pd.Index(bars.index.tz_convert(NY).date).unique()}


def build_events(dates, q_a: pd.DataFrame, q_b: pd.DataFrame, q_stmt: pd.DataFrame, q_e: pd.DataFrame, q_x: pd.DataFrame,
                 trading_days: set) -> pd.DataFrame:
    rows = []
    for t in sorted(dates):
        n1 = t + timedelta(days=1)
        a, b, s, e, x = _get(q_a, prev_business_day(t)), _get(q_b, t), _get(q_stmt, t), _get(q_e, n1), _get(q_x, n1)
        rows.append({"date": t, "next_date": n1, "a_mid": _mid(a), "b_mid": _mid(b), "stmt_mid": _mid(s), "entry_mid": _mid(e),
                     "exit_mid": _mid(x), "entry_spread_pips": _spr(e), "exit_spread_pips": _spr(x),
                     "next_is_trading_day": n1 in trading_days})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["p_pips"] = (df["b_mid"] - df["a_mid"]) / PIP
    df["r_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["r_0_12_pips"] = (df["entry_mid"] - df["stmt_mid"]) / PIP
    excl = []
    for r in df.itertuples(index=False):
        if not r.next_is_trading_day:
            excl.append("not_trading_day")
        elif np.isnan(r.a_mid) or np.isnan(r.b_mid):
            excl.append("missing_pre")
        elif r.p_pips == 0:
            excl.append("zero_signal")
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
    df["side"] = -np.sign(df["p_pips"])
    df["signed_pips"] = df["side"] * df["r_pips"]
    df["signed_0_12_pips"] = df["side"] * df["r_0_12_pips"]
    return df


def frame_from_bars(bars: pd.DataFrame, dates) -> pd.DataFrame:
    return build_events(dates, ny_quotes(bars, *PRE_START_HM), ny_quotes(bars, *PRE_END_HM), ny_quotes(bars, *STATEMENT_HM),
                        ny_quotes(bars, *ENTRY_HM), ny_quotes(bars, *EXIT_HM), ny_dates_with_bars(bars))


def events(df: pd.DataFrame) -> pd.DataFrame:
    """Tested events with net columns for vol_state_fix.cost_summary."""
    ev = df[df["tested"]].copy()
    ev["net_bidask_pips"] = ev["signed_pips"] - (ev["entry_spread_pips"] + ev["exit_spread_pips"]) / 2
    ev["net_spec4_pips"] = ev["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    ev["net_x1_5_pips"] = ev["signed_pips"] - 1.5 * (ev["signed_pips"] - ev["net_spec4_pips"])
    return ev


def evaluate(signed) -> dict:
    x = np.asarray(signed, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 3:
        return {"n": n, "note": "insufficient sample"}
    nz = x[x != 0]
    hits = int((nz > 0).sum())
    binom_p = float(stats.binomtest(hits, len(nz), 0.5, alternative="greater").pvalue) if len(nz) else 1.0
    t = stats.ttest_1samp(x, 0.0, alternative="greater")
    lo, hi = block_bootstrap_mean_ci(x, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    return {"n": n, "mean_pips": round(float(x.mean()), 3), "median_pips": round(float(np.median(x)), 3),
            "sd_pips": round(float(x.std(ddof=1)), 3), "n_nonzero": int(len(nz)), "hits": hits,
            "hit_rate": round(hits / len(nz), 4) if len(nz) else None, "binom_p_one_sided": round(binom_p, 5),
            "t_stat": round(float(t.statistic), 3), "t_p_one_sided": round(float(t.pvalue), 4),
            "mean_ci95_boot": (round(lo, 3), round(hi, 3))}


def decide_b43(res: dict) -> str:
    """Pre-registered E040 rule: < 40 tested events -> NONE. SIGNAL if mean > 1.0 pip AND i.i.d. bootstrap CI lower > 0 AND
    one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE."""
    if "mean_pips" not in res or res.get("n", 0) < MIN_EVENTS:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"events": 0}
    vc = df["excluded"].value_counts()
    out = {"events": int(len(df))}
    out.update({k: int(vc.get(k, 0)) for k in EXCLUSION_ORDER})
    out["tested"] = int(df["tested"].sum())
    return out


def slope(ev: pd.DataFrame) -> dict:
    if len(ev) < 3:
        return {}
    r = stats.linregress(ev["p_pips"], ev["r_pips"])
    return {"n": int(len(ev)), "slope": round(float(r.slope), 5), "t_stat": round(float(r.slope / r.stderr), 3),
            "p_two_sided": round(float(r.pvalue), 4)}
