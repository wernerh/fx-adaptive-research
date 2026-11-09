"""E022 (backlog B19): pre-ECB-fix USD appreciation on high-volatility dates, dev only.

Definitions (fixed in pre-registration, R042, before any run):
* Trading dates: the sorted set of `sessions.trading_date` values present in the bars (17:00 NY roll).
* Range RNG(P) = (max mid high - min mid low) / PIP over all 1-minute bars of trading date P (17:00 NY -> 17:00 NY), where
  mid high = (bid_high + ask_high) / 2 and mid low = (bid_low + ask_low) / 2. P is VALID if it has >= 90% of the 1,440
  expected 1-minute bars (>= 1,296 bars); otherwise invalid (`low_coverage`) and counted.
* Threshold: for a valid P, thr(P) = np.percentile(RNG of the 60 valid dates before P, 67) (numpy default linear
  interpolation; past only). The first 60 valid dates are burn-in.
* Event: trading date D is HIGH-VOL if its previous trading date P (the date immediately before D in the trading-date set) is
  valid, past burn-in, and RNG(P) > thr(P) (strictly greater). D with an invalid P is `prev_invalid`; with P in burn-in it is
  `burn_in`; both counted and never events.
* Trade for a high-vol D: short EUR/USD from 02:00 NY to 08:15 NY on NY calendar date D (the NY calendar date of these hours
  equals the trading date). Quote at hh:mm = bid/ask OPEN of the first bar in [hh:mm, hh:mm+5) America/New_York; missing -> NaN.
  Exclusions, counted, first reason in this order: `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at entry >
  2.0 pips, SPEC 4).
* Signed return = -(mid exit - mid entry) / PIP.
Only bars of P (which ends at 17:00 NY on the day before the 02:00 entry) enter the event decision, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import NY, trading_date

WINDOW = 60
PCTL = 67
EXPECTED_BARS = 1440
MIN_COVERAGE = 0.90
MAX_ENTRY_SPREAD_PIPS = 2.0
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 10
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1       # SPEC 4
COMMISSION_RT_PIPS = 0.1        # SPEC 4
ENTRY_HM = (2, 0)
EXIT_HM = (8, 15)
EDGE_MINUTES = 5
SIDE = -1                        # short EUR/USD (USD appreciates before the fix)


def ny_quotes(bars: pd.DataFrame, hour: int, minute: int = 0) -> pd.DataFrame:
    """Per NY calendar date: bid/ask open of the first bar in [hh:mm, hh:mm+5) America/New_York."""
    ny = bars.index.tz_convert(NY)
    mins = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    t0 = hour * 60 + minute
    sel = (mins >= t0) & (mins < t0 + EDGE_MINUTES)
    nyd = pd.Index(ny.date)[sel]
    out = bars.loc[sel, ["bid_open", "ask_open"]].groupby(nyd).first()
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="ny_date")
    return out


def _get(qt: pd.DataFrame, d):
    if d in qt.index:
        b, a = qt.loc[d, "bid_open"], qt.loc[d, "ask_open"]
        if not (np.isnan(b) or np.isnan(a)):
            return float(b), float(a)
    return None


def daily_ranges(bars: pd.DataFrame) -> pd.DataFrame:
    """One row per trading date: n_bars, range_pips (mid high-low), valid (coverage >= 90% of 1,440 bars)."""
    td = pd.Index(trading_date(bars.index), name="date")
    hi = (bars["bid_high"] + bars["ask_high"]).to_numpy() / 2
    lo = (bars["bid_low"] + bars["ask_low"]).to_numpy() / 2
    g = pd.DataFrame({"hi": hi, "lo": lo}, index=td).groupby(level=0)
    out = pd.DataFrame({"n_bars": g.size(), "range_pips": (g["hi"].max() - g["lo"].min()) / PIP})
    out["valid"] = out["n_bars"] >= MIN_COVERAGE * EXPECTED_BARS
    out = out.reset_index()
    out["date"] = [pd.Timestamp(x).date() if not isinstance(x, date) else x for x in out["date"]]
    return out.sort_values("date").reset_index(drop=True)


def add_threshold(rng: pd.DataFrame, window: int = WINDOW, pctl: float = PCTL) -> pd.DataFrame:
    """Rolling past-only threshold on VALID dates; NaN on invalid and burn-in dates. Adds is_high (range > thr)."""
    rng = rng.copy()
    v = rng[rng["valid"]]
    r = v["range_pips"].to_numpy()
    thr = np.full(len(v), np.nan)
    for i in range(window, len(v)):
        thr[i] = np.percentile(r[i - window:i], pctl)
    rng["threshold_pips"] = np.nan
    rng.loc[v.index, "threshold_pips"] = thr
    rng["is_high"] = rng["threshold_pips"].notna() & (rng["range_pips"] > rng["threshold_pips"].fillna(np.inf))
    return rng


def build_days(rng: pd.DataFrame, entry_q: pd.DataFrame, exit_q: pd.DataFrame) -> pd.DataFrame:
    """One row per trading date D (from the second on): prev P, state of P, event flag, trade legs, exclusion, returns."""
    rng = add_threshold(rng)
    rows = []
    for i in range(1, len(rng)):
        p, d = rng.iloc[i - 1], rng.iloc[i]
        if not p["valid"]:
            state = "prev_invalid"
        elif np.isnan(p["threshold_pips"]):
            state = "burn_in"
        else:
            state = "high" if p["is_high"] else "normal"
        e = _get(entry_q, d["date"])
        x = _get(exit_q, d["date"])
        rows.append({"date": d["date"], "prev": p["date"], "state": state, "prev_range_pips": p["range_pips"],
                     "threshold_pips": p["threshold_pips"],
                     "entry_mid": sum(e) / 2 if e else np.nan, "entry_spread_pips": (e[1] - e[0]) / PIP if e else np.nan,
                     "exit_mid": sum(x) / 2 if x else np.nan, "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    excl = []
    for r in df.itertuples(index=False):
        if np.isnan(r.entry_mid):
            excl.append("missing_entry")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tradable"] = df["excluded"].isna()
    df["is_event"] = df["state"] == "high"
    df["tested"] = df["is_event"] & df["tradable"]
    df["signed_pips"] = SIDE * (df["exit_mid"] - df["entry_mid"]) / PIP
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    return df


def frame_from_bars(bars: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = daily_ranges(bars)
    return rng, build_days(rng, ny_quotes(bars, *ENTRY_HM), ny_quotes(bars, *EXIT_HM))


def tradable_events(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["tested"]]


def counts(rng: pd.DataFrame, df: pd.DataFrame) -> dict:
    vc_state = df["state"].value_counts() if len(df) else pd.Series(dtype=int)
    ev = df[df["is_event"]] if len(df) else df
    vc_ex = ev["excluded"].value_counts() if len(ev) else pd.Series(dtype=int)
    return {
        "trading_dates": int(len(rng)), "valid_dates": int(rng["valid"].sum()),
        "low_coverage": int((~rng["valid"]).sum()),
        **{f"state_{k}": int(vc_state.get(k, 0)) for k in ("prev_invalid", "burn_in", "normal", "high")},
        **{k: int(vc_ex.get(k, 0)) for k in ("missing_entry", "missing_exit", "entry_skipped_spread")},
        "events_tested": int(df["tested"].sum()) if len(df) else 0,
    }


def evaluate(signed) -> dict:
    """Mean test: mean, median, sd, hit, one-sided t p (H1 mean > 0), block-10 moving-block bootstrap CI."""
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


def decide_b19(res: dict) -> str:
    """Pre-registered E022 rule. SIGNAL: mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
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
        "median_spread_entry_pips": round(float(ev["entry_spread_pips"].median()), 3),
        "median_spread_exit_pips": round(float(ev["exit_spread_pips"].median()), 3),
    }
