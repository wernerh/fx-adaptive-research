"""E035 (backlog B32 + B33): overnight -> intraday reversal in EUR/USD, DEV ONLY, 2 trials in one experiment.

Definitions (fixed in the backlog, R074, and pre-registered 2026-11-10 R075, before any run):
* Trading date D (17:00 NY roll, SPEC 2, `sessions.trading_date`). Dates = sorted trading-date set of the (dev) bars.
* Quotes = bid/ask OPEN of the first 1-minute bar in [T, T+5 min) (E011 rule). Missing -> NaN, never filled.
  - open quote of D: first bar in [17:05, 17:10) America/New_York whose trading date is D (the evening that opens D; Sunday
    17:05 for Mondays) (`evening_quotes`);
  - 07:00 and 16:55 quotes: first bar in [07:00, 07:05) / [16:55, 17:00) NY on NY calendar date D (`vol_state_fix.ny_quotes`).
* r_on(D) = (mid 07:00 NY on D - mid 17:05 NY opening D) / PIP; r_id(D) = (mid 16:55 - mid 07:00 NY on D) / PIP.
* B32 position = -sign(r_on(D)) (fade the overnight move); signed return = position x r_id(D).
* B33 position = -sign(O20(D)), O20(D) = sum of r_on over the 20 previous dates (before D) that have a valid r_on (dates with a
  missing r_on are skipped and the window reaches further back; D's own r_on is excluded). The first 20 dates with a valid r_on
  have no O20 (burn-in, counted as `burn_in`).
* Exclusions per arm, counted, first reason in this order: `missing_signal` (B32: r_on NaN; B33: burn-in or no O20), `zero_signal`
  (signal == 0), `missing_entry` (07:00), `missing_exit` (16:55), `entry_skipped_spread` (ask-bid at 07:00 > 2.0 pips, SPEC 4).
  For B32 `missing_signal` covers a missing 17:05 or 07:00 quote; the 07:00 quote is also the entry, so a missing 07:00 is counted
  as `missing_signal` first.
* Statistic per arm: mean, median, SD, hit, one-sided t (H1 mean > 0), moving-block bootstrap 95% CI (block 20 dates, 2000 draws,
  seed 0) (`evaluate_b32`).
* Decision (`decide_b32`, same for B33): < 500 tested dates -> NONE (insufficient sample). SIGNAL if mean > 1.0 pip AND CI lower > 0
  AND one-sided t p < 0.025 (Bonferroni for 2 trials). WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE.
The side uses only quotes at or before 07:00 NY on D (B33: r_on of earlier dates only); the trade runs 07:00 -> 16:55 NY on D.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import trading_date
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, ny_quotes

NY = "America/New_York"
EDGE_MINUTES = 5
OPEN_HM = (17, 5)
ENTRY_HM = (7, 0)
EXIT_HM = (16, 55)
SMOOTH_N = 20
ALPHA = 0.025                    # Bonferroni for 2 trials
MIN_MEAN_PIPS = 1.0
MIN_EVENTS = 500
BOOT_BLOCK = 20
BOOT_N = 2000

EXCLUSION_ORDER = ("missing_signal", "zero_signal", "missing_entry", "missing_exit", "entry_skipped_spread")


def evening_quotes(bars: pd.DataFrame, hour: int = OPEN_HM[0], minute: int = OPEN_HM[1]) -> pd.DataFrame:
    """Per TRADING date: bid/ask open of the first bar in [hh:mm, hh:mm+5) NY (an evening time after the 17:00 roll)."""
    ny = bars.index.tz_convert(NY)
    mins = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    t0 = hour * 60 + minute
    sel = (mins >= t0) & (mins < t0 + EDGE_MINUTES)
    td = pd.Index(trading_date(bars.index[sel]))
    out = bars.loc[sel, ["bid_open", "ask_open"]].groupby(td).first()
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="trading_date")
    return out


def _mid(q):
    return sum(q) / 2 if q else np.nan


def smoothed_signal(r_on: pd.Series, n: int = SMOOTH_N) -> pd.Series:
    """O20: sum of the previous n VALID r_on values (strictly before each date); NaN during burn-in. Index-aligned to r_on."""
    out = pd.Series(np.nan, index=r_on.index)
    hist: list[float] = []
    for i, v in enumerate(r_on.to_numpy()):
        if len(hist) >= n:
            out.iloc[i] = float(np.sum(hist[-n:]))
        if not np.isnan(v):
            hist.append(float(v))
    return out


def build_days(dates, q_open: pd.DataFrame, q_in: pd.DataFrame, q_out: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for d in sorted(dates):
        o, i, x = _get(q_open, d), _get(q_in, d), _get(q_out, d)
        rows.append({"date": d, "open_mid": _mid(o), "entry_mid": _mid(i),
                     "entry_spread_pips": (i[1] - i[0]) / PIP if i else np.nan,
                     "exit_mid": _mid(x), "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["r_on_pips"] = (df["entry_mid"] - df["open_mid"]) / PIP
    df["r_id_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["o20_pips"] = smoothed_signal(df["r_on_pips"])
    df["burn_in"] = df["o20_pips"].isna()
    for arm, sig in (("b32", df["r_on_pips"]), ("b33", df["o20_pips"])):
        excl = []
        for s, r in zip(sig.to_numpy(), df.itertuples(index=False)):
            if np.isnan(s):
                excl.append("missing_signal")
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
        side = -np.sign(sig)
        df[f"{arm}_side"] = side
        df[f"{arm}_signed_pips"] = side * df["r_id_pips"]
    df["weekday"] = pd.to_datetime(df["date"]).dt.dayofweek
    return df


def frame_from_bars(bars: pd.DataFrame) -> pd.DataFrame:
    dates = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    return build_days(dates, evening_quotes(bars), ny_quotes(bars, *ENTRY_HM), ny_quotes(bars, *EXIT_HM))


def arm_events(df: pd.DataFrame, arm: str) -> pd.DataFrame:
    """Tested dates of one arm with generic column names (signed_pips, net columns) for cost_summary."""
    ev = df[df[f"{arm}_tested"]].copy()
    ev["signed_pips"] = ev[f"{arm}_signed_pips"]
    ev["side"] = ev[f"{arm}_side"]
    ev["net_bidask_pips"] = ev["signed_pips"] - (ev["entry_spread_pips"] + ev["exit_spread_pips"]) / 2
    ev["net_spec4_pips"] = ev["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    ev["net_x1_5_pips"] = ev["signed_pips"] - 1.5 * (ev["signed_pips"] - ev["net_spec4_pips"])
    return ev


def evaluate_b32(signed) -> dict:
    x = np.asarray(signed, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2 * BOOT_BLOCK:
        return {"n": n, "note": "insufficient sample"}
    t = stats.ttest_1samp(x, 0.0, alternative="greater")
    lo, hi = block_bootstrap_mean_ci(x, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    return {"n": n, "mean_pips": round(float(x.mean()), 3), "median_pips": round(float(np.median(x)), 3),
            "sd_pips": round(float(x.std(ddof=1)), 3), "hit_rate": round(float((x > 0).mean()), 4),
            "t_stat": round(float(t.statistic), 3), "t_p_one_sided": round(float(t.pvalue), 4),
            "mean_ci95_block_boot": (round(lo, 3), round(hi, 3))}


def decide_b32(res: dict) -> str:
    """Pre-registered E035 rule (B32 and B33): < 500 tested dates -> NONE. SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI
    lower > 0 AND one-sided t p < 0.025; WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE."""
    if "mean_pips" not in res or res.get("n", 0) < MIN_EVENTS:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_block_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


decide_b33 = decide_b32

# E036 (backlog B34, pre-registered 2026-11-10 R077): val confirmation of the B33 arm, 1 val trial. Identical rule except p < 0.05.
ALPHA_VAL = 0.05


def decide_b34(res: dict) -> str:
    """Pre-registered E036 rule (B33 arm on val): < 500 tested dates -> NONE. SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI
    lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE."""
    if "mean_pips" not in res or res.get("n", 0) < MIN_EVENTS:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_block_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA_VAL:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA_VAL):
        return "WEAK"
    return "NONE"


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"trading_dates": 0}
    n_valid = int(df["r_on_pips"].notna().sum())
    out = {"trading_dates": int(len(df)), "valid_r_on_dates": n_valid,
           "b33_burn_in_valid_dates": int(min(SMOOTH_N, n_valid))}
    for arm in ("b32", "b33"):
        vc = df[f"{arm}_excluded"].value_counts()
        out.update({f"{arm}_{k}": int(vc.get(k, 0)) for k in EXCLUSION_ORDER})
        out[f"{arm}_tested"] = int(df[f"{arm}_tested"].sum())
    return out


def slope(df: pd.DataFrame) -> dict:
    """Descriptive OLS slope of r_id on r_on over B32-tested dates (negative = reversal)."""
    t = df[df["b32_tested"]]
    if len(t) < 3:
        return {}
    r = stats.linregress(t["r_on_pips"], t["r_id_pips"])
    return {"n": int(len(t)), "slope": round(float(r.slope), 4), "t_stat": round(float(r.slope / r.stderr), 3),
            "p_two_sided": round(float(r.pvalue), 4)}
