"""E038 (backlog B38): intraday momentum into the 17:00 NY spot roll, EUR/USD, DEV ONLY, 1 trial.

Pre-registered 2026-11-11 R083 in experiments/2026-11-11_E038_roll_momentum/ (anchor variant of E016/B13, Baltussen et al. 2021).
* Trading date D (17:00 NY roll, `sessions.trading_date`), Monday-Friday only.
* Quotes = bid/ask OPEN of the first 1-minute bar in [T, T+5 min) NY (E011 rule); missing -> NaN, never filled.
  - P0: first bar in [17:00, 17:05) NY whose trading date is D (`overnight_reversal.evening_quotes(bars, 17, 0)`);
  - E:  first bar in [16:25, 16:30) NY on NY calendar date D; X: first bar in [16:55, 17:00) NY on NY calendar date D.
* r1 = (mid E - mid P0) / pip, r2 = (mid X - mid E) / pip, signed = sign(r1) x r2.
* Exclusions, first reason in order: missing_start, missing_entry, zero_signal, missing_exit, entry_skipped_spread (> 2.0 pips at E).
* Decision (`decide_b38`, B13 rule): < 500 tested -> NONE; SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND
  one-sided binomial p < 0.05 on sign agreement; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
The side uses only quotes at or before 16:25 NY on D; the trade runs 16:25 -> 16:55 NY on D.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .overnight_reversal import evening_quotes
from .sessions import trading_date
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, ny_quotes

START_HM = (17, 0)
ENTRY_HM = (16, 25)
EXIT_HM = (16, 55)
NEXT_OPEN_HM = (17, 5)     # descriptive next-date reversal reading only
ALPHA = 0.05
MIN_MEAN_PIPS = 1.0
MIN_EVENTS = 500
BOOT_BLOCK = 20
BOOT_N = 2000

EXCLUSION_ORDER = ("missing_start", "missing_entry", "zero_signal", "missing_exit", "entry_skipped_spread")


def _mid(q):
    return sum(q) / 2 if q else np.nan


def _spr(q):
    return (q[1] - q[0]) / PIP if q else np.nan


def weekday_dates(bars: pd.DataFrame) -> tuple[list, int]:
    """Sorted Mon-Fri trading dates of `bars`, plus the number of weekend trading-date artefacts dropped."""
    all_d = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    keep = [d for d in all_d if d.weekday() < 5]
    return keep, len(all_d) - len(keep)


def build_days(dates, q_start: pd.DataFrame, q_entry: pd.DataFrame, q_exit: pd.DataFrame,
               q_next_open: pd.DataFrame | None = None) -> pd.DataFrame:
    dates = sorted(dates)
    rows = []
    for k, d in enumerate(dates):
        s, e, x = _get(q_start, d), _get(q_entry, d), _get(q_exit, d)
        r = {"date": d, "start_mid": _mid(s), "entry_mid": _mid(e), "exit_mid": _mid(x),
             "entry_spread_pips": _spr(e), "exit_spread_pips": _spr(x), "next_open_mid": np.nan, "next_entry_mid": np.nan}
        if q_next_open is not None and k + 1 < len(dates):
            nd = dates[k + 1]
            r["next_open_mid"] = _mid(_get(q_next_open, nd))
            r["next_entry_mid"] = _mid(_get(q_entry, nd))
        rows.append(r)
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["r1_pips"] = (df["entry_mid"] - df["start_mid"]) / PIP
    df["r2_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["next_day_pips"] = (df["next_entry_mid"] - df["next_open_mid"]) / PIP
    excl = []
    for r in df.itertuples(index=False):
        if np.isnan(r.start_mid):
            excl.append("missing_start")
        elif np.isnan(r.entry_mid):
            excl.append("missing_entry")
        elif r.r1_pips == 0:
            excl.append("zero_signal")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tested"] = df["excluded"].isna()
    df["side"] = np.sign(df["r1_pips"])
    df["signed_pips"] = df["side"] * df["r2_pips"]
    df["weekday"] = pd.to_datetime(df["date"]).dt.dayofweek
    return df


def frame_from_bars(bars: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    dates, n_weekend = weekday_dates(bars)
    df = build_days(dates, evening_quotes(bars, *START_HM), ny_quotes(bars, *ENTRY_HM), ny_quotes(bars, *EXIT_HM),
                    evening_quotes(bars, *NEXT_OPEN_HM))
    return df, n_weekend


def events(df: pd.DataFrame) -> pd.DataFrame:
    """Tested dates with net columns for vol_state_fix.cost_summary."""
    ev = df[df["tested"]].copy()
    ev["net_bidask_pips"] = ev["signed_pips"] - (ev["entry_spread_pips"] + ev["exit_spread_pips"]) / 2
    ev["net_spec4_pips"] = ev["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    ev["net_x1_5_pips"] = ev["signed_pips"] - 1.5 * (ev["signed_pips"] - ev["net_spec4_pips"])
    return ev


def evaluate(signed) -> dict:
    x = np.asarray(signed, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2 * BOOT_BLOCK:
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
            "mean_ci95_block_boot": (round(lo, 3), round(hi, 3))}


def decide_b38(res: dict) -> str:
    """Pre-registered E038 rule (B13 rule): < 500 tested dates -> NONE. SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI lower
    > 0 AND one-sided binomial p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE."""
    if "mean_pips" not in res or res.get("n", 0) < MIN_EVENTS:
        return "NONE"
    m, p = res["mean_pips"], res["binom_p_one_sided"]
    lo = res["mean_ci95_block_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


def reversal_flag(res: dict) -> bool:
    if "mean_pips" not in res:
        return False
    hi = res["mean_ci95_block_boot"][1]
    return res["mean_pips"] < 0 and hi is not None and not np.isnan(hi) and hi < 0


def counts(df: pd.DataFrame, n_weekend: int = 0) -> dict:
    if df.empty:
        return {"trading_dates": 0, "weekend_trading_dates_dropped": n_weekend}
    vc = df["excluded"].value_counts()
    out = {"trading_dates": int(len(df)), "weekend_trading_dates_dropped": n_weekend}
    out.update({k: int(vc.get(k, 0)) for k in EXCLUSION_ORDER})
    out["tested"] = int(df["tested"].sum())
    return out


def slope(ev: pd.DataFrame) -> dict:
    if len(ev) < 3:
        return {}
    r = stats.linregress(ev["r1_pips"], ev["r2_pips"])
    return {"n": int(len(ev)), "slope": round(float(r.slope), 5), "t_stat": round(float(r.slope / r.stderr), 3),
            "p_two_sided": round(float(r.pvalue), 4)}
