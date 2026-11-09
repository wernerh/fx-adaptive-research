"""E020 (backlog B17): weekend-gap reversal, dev only.

Definitions (fixed in pre-registration, R037, before any run):
* Quote at hh:00 NY on NY calendar date d: bid/ask OPEN of the first bar in [hh:00, hh:05) America/New_York
  (`fomc.ny_edge_quotes`). Missing -> NaN, never filled.
* Weekends are indexed by their Monday W (calendar Monday, NY date). Candidate Mondays: every calendar Monday W with
  W-3 (Friday) >= first trading date of the bars and W <= last trading date of the bars.
  F = mid at 16:00 NY on Friday W-3, M = mid at 20:00 NY on Sunday W-1, X = mid at 16:00 NY on Monday W.
  Gap G = (M - F) / PIP. Weekends with F, M or X missing are excluded and counted (first missing in order F, M, X).
  All others are "valid".
* Threshold: a valid weekend is an EVENT if |G| > np.percentile(|G| of the previous 26 valid weekends, 67) (numpy default
  linear interpolation; strictly greater; past only). The first 26 valid weekends are burn-in (no event).
* Entry skip: an event whose ask-bid spread at M is > 2.0 pips is skipped and counted (SPEC 4). It stays in the rolling
  |G| history (the history uses mids only).
* Signed return per event = -sign(G) x (X - M) / PIP, mid. G = 0 cannot be an event (|G| > percentile >= 0).
Nothing after M enters the event decision, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .fomc import ny_edge_quotes
from .metrics import block_bootstrap_mean_ci
from .sessions import trading_date

WINDOW = 26
PCTL = 67
MAX_ENTRY_SPREAD_PIPS = 2.0
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 4
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1       # SPEC 4
COMMISSION_RT_PIPS = 0.1        # SPEC 4
FRI_HOUR, SUN_HOUR, EXIT_HOUR = 16, 20, 16
SUNDAY_OPEN_HOUR = 17           # descriptive only: 17:00-20:00 NY Sunday move


def _quote_table(bars: pd.DataFrame) -> dict[int, pd.DataFrame]:
    return {h: ny_edge_quotes(bars, h)[["bid_open", "ask_open"]] for h in (16, 17, 20)}


def _get(qt: pd.DataFrame, d):
    if d in qt.index:
        b, a = qt.loc[d, "bid_open"], qt.loc[d, "ask_open"]
        if not (np.isnan(b) or np.isnan(a)):
            return float(b), float(a)
    return None


def weekend_frame(bars: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """One row per candidate Monday. Columns: monday, valid, missing, F/M/X bid+ask, gap_pips, spreads, X on Tue/Fri
    (descriptive), Sunday 17:00 mid (descriptive). Returns (frame, exclusion counts)."""
    tds = sorted(set(trading_date(bars.index)))
    qt = _quote_table(bars)
    first, last = tds[0], tds[-1]
    d = first + timedelta(days=(0 - first.weekday()) % 7)
    if d - timedelta(days=3) < first:
        d += timedelta(days=7)
    skips = {"missing_F": 0, "missing_M": 0, "missing_X": 0}
    rows = []
    while d <= last:
        f = _get(qt[FRI_HOUR], d - timedelta(days=3))
        m = _get(qt[SUN_HOUR], d - timedelta(days=1))
        x = _get(qt[EXIT_HOUR], d)
        miss = None
        if f is None:
            miss = "missing_F"
        elif m is None:
            miss = "missing_M"
        elif x is None:
            miss = "missing_X"
        row = {"monday": d, "valid": miss is None, "missing": miss}
        if miss:
            skips[miss] += 1
        else:
            fm, mm, xm = sum(f) / 2, sum(m) / 2, sum(x) / 2
            row.update({
                "F_mid": fm, "M_mid": mm, "X_mid": xm, "gap_pips": (mm - fm) / PIP,
                "F_spread_pips": (f[1] - f[0]) / PIP, "M_spread_pips": (m[1] - m[0]) / PIP,
                "X_spread_pips": (x[1] - x[0]) / PIP,
            })
            tue = _get(qt[EXIT_HOUR], d + timedelta(days=1))
            fri = _get(qt[EXIT_HOUR], d + timedelta(days=4)) if d + timedelta(days=4) <= last else None
            s17 = _get(qt[SUNDAY_OPEN_HOUR], d - timedelta(days=1))
            row["tue_mid"] = sum(tue) / 2 if tue else np.nan
            row["fri_mid"] = sum(fri) / 2 if fri else np.nan
            row["sun17_mid"] = sum(s17) / 2 if s17 else np.nan
        rows.append(row)
        d += timedelta(days=7)
    return pd.DataFrame(rows), skips


def mark_events(wf: pd.DataFrame, window: int = WINDOW, pctl: float = PCTL) -> pd.DataFrame:
    """Adds threshold, is_event, entry_skipped and signed returns to the VALID weekends (past-only rolling threshold)."""
    v = wf[wf["valid"]].copy().reset_index(drop=True)
    absg = v["gap_pips"].abs().to_numpy()
    thr = np.full(len(v), np.nan)
    for i in range(window, len(v)):
        thr[i] = np.percentile(absg[i - window:i], pctl)
    v["threshold_pips"] = thr
    v["is_event"] = ~np.isnan(thr) & (absg > np.nan_to_num(thr, nan=np.inf))
    v["entry_skipped"] = v["is_event"] & (v["M_spread_pips"] > MAX_ENTRY_SPREAD_PIPS)
    sgn = -np.sign(v["gap_pips"])
    v["signed_pips"] = sgn * (v["X_mid"] - v["M_mid"]) / PIP
    v["signed_tue_pips"] = sgn * (v["tue_mid"] - v["M_mid"]) / PIP
    v["signed_fri_pips"] = sgn * (v["fri_mid"] - v["M_mid"]) / PIP
    v["signed_sun17_20_pips"] = sgn * (v["M_mid"] - v["sun17_mid"]) / PIP
    v["net_bidask_pips"] = v["signed_pips"] - (v["M_spread_pips"] + v["X_spread_pips"]) / 2
    v["net_spec4_pips"] = v["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    v["net_x1_5_pips"] = v["signed_pips"] - 1.5 * (v["signed_pips"] - v["net_spec4_pips"])
    return v


def tradable_events(v: pd.DataFrame) -> pd.DataFrame:
    return v[v["is_event"] & ~v["entry_skipped"]]


def evaluate(signed) -> dict:
    """Mean test: mean, median, sd, hit, one-sided t p (H1 mean > 0), block-4 moving-block bootstrap CI."""
    x = np.asarray(signed, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2 * BOOT_BLOCK:
        return {"n": n, "note": "insufficient sample"}
    t = stats.ttest_1samp(x, 0.0, alternative="greater")
    lo, hi = block_bootstrap_mean_ci(x, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    return {
        "n": n,
        "mean_pips": round(float(x.mean()), 3),
        "median_pips": round(float(np.median(x)), 3),
        "sd_pips": round(float(x.std(ddof=1)), 3),
        "hit_rate": round(float((x > 0).mean()), 4),
        "t_stat": round(float(t.statistic), 3),
        "t_p_one_sided": round(float(t.pvalue), 4),
        "mean_ci95_block_boot": (round(lo, 3), round(hi, 3)),
    }


def decide_b17(res: dict) -> str:
    """Pre-registered E020 rule. SIGNAL: mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
    WEAK: mean > 0 and (CI lower > 0 or p < 0.05), not SIGNAL. NONE otherwise."""
    if "mean_pips" not in res:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_block_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


def cost_summary(ev: pd.DataFrame) -> dict:
    if len(ev) == 0:
        return {"n": 0}
    return {
        "n": int(len(ev)),
        "mean_signed_mid_pips": round(float(ev["signed_pips"].mean()), 3),
        "mean_net_bidask_pips": round(float(ev["net_bidask_pips"].mean()), 3),
        "mean_net_spec4_pips": round(float(ev["net_spec4_pips"].mean()), 3),
        "mean_net_costs_x1_5_pips": round(float(ev["net_x1_5_pips"].mean()), 3),
        "median_spread_F_pips": round(float(ev["F_spread_pips"].median()), 3),
        "median_spread_M_pips": round(float(ev["M_spread_pips"].median()), 3),
        "median_spread_X_pips": round(float(ev["X_spread_pips"].median()), 3),
    }
