"""E021 (backlog B18): next-session reversal after a large daily move, dev only.

Definitions (fixed in pre-registration, R039, before any run):
* Quote at hh:mm NY on NY calendar date d: bid/ask OPEN of the first bar in [hh:mm, hh:mm+5) America/New_York.
  Missing -> NaN, never filled.
* Trading dates: the sorted set of `sessions.trading_date` values present in the bars (17:00 NY roll). For hour 16:00 NY the
  NY calendar date equals the trading date.
* Daily move R(D) = (mid 16:00 NY on D - mid 16:00 NY on P) / PIP, where P is the trading date immediately before D in that
  set. D is "valid" if both quotes exist (otherwise excluded and counted: `missing_16_D`, then `missing_16_prev`; the first
  trading date has no P and is `no_prev`).
* Threshold: a valid D is LARGE if |R(D)| > np.percentile(|R| of the previous 60 valid dates, 80) (numpy default linear
  interpolation; strictly greater; past only). The first 60 valid dates are burn-in. Every valid date, Fridays included,
  enters the rolling |R| history (mids only).
* Trade for a large D: position -sign(R(D)) from 20:00 NY on calendar date D to 10:45 NY on calendar date N, where N is the
  trading date after D. Exclusions, counted, in this order: D is a Friday (`friday`); N missing from the bars or N != D + 1
  calendar day (`next_not_adjacent`); missing 20:00 quote on D (`missing_entry`); missing 10:45 quote on N (`missing_exit`);
  ask-bid spread at entry > 2.0 pips (`entry_skipped_spread`, SPEC 4).
* Signed return = -sign(R(D)) x (mid exit - mid entry) / PIP. R(D) = 0 cannot be large.
Nothing after 16:00 NY on D enters the event decision, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import NY, trading_date

WINDOW = 60
PCTL = 80
MAX_ENTRY_SPREAD_PIPS = 2.0
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 10
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1       # SPEC 4
COMMISSION_RT_PIPS = 0.1        # SPEC 4
CLOSE_HM = (16, 0)
ENTRY_HM = (20, 0)
EXIT_HM = (10, 45)
EDGE_MINUTES = 5


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


def daily_frame(bars: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """One row per trading date. Columns: date, prev, valid, missing, move_pips, close_mid, plus the trade legs for the
    next trading date (entry/exit mids and spreads, 16:00->20:00 move; NaN where unavailable). Returns (frame, counts)."""
    tds = sorted(set(trading_date(bars.index)))
    q16 = ny_quotes(bars, *CLOSE_HM)
    q20 = ny_quotes(bars, *ENTRY_HM)
    q1045 = ny_quotes(bars, *EXIT_HM)
    counts = {"no_prev": 0, "missing_16_D": 0, "missing_16_prev": 0}
    rows = []
    for i, d in enumerate(tds):
        p = tds[i - 1] if i > 0 else None
        n = tds[i + 1] if i + 1 < len(tds) else None
        row = {"date": d, "prev": p, "next": n, "valid": False, "missing": None, "move_pips": np.nan}
        c = _get(q16, d)
        cp = _get(q16, p) if p is not None else None
        if p is None:
            row["missing"] = "no_prev"
        elif c is None:
            row["missing"] = "missing_16_D"
        elif cp is None:
            row["missing"] = "missing_16_prev"
        if row["missing"]:
            counts[row["missing"]] += 1
        else:
            row["valid"] = True
            row["move_pips"] = (sum(c) / 2 - sum(cp) / 2) / PIP
            row["close_mid"] = sum(c) / 2
        e = _get(q20, d)
        x = _get(q1045, n) if n is not None else None
        row["entry_mid"] = sum(e) / 2 if e else np.nan
        row["entry_spread_pips"] = (e[1] - e[0]) / PIP if e else np.nan
        row["exit_mid"] = sum(x) / 2 if x else np.nan
        row["exit_spread_pips"] = (x[1] - x[0]) / PIP if x else np.nan
        rows.append(row)
    return pd.DataFrame(rows), counts


def mark_events(df: pd.DataFrame, window: int = WINDOW, pctl: float = PCTL) -> pd.DataFrame:
    """On VALID dates: rolling past-only threshold, is_large, exclusion reason, signed returns and costs."""
    v = df[df["valid"]].copy().reset_index(drop=True)
    absr = v["move_pips"].abs().to_numpy()
    thr = np.full(len(v), np.nan)
    for i in range(window, len(v)):
        thr[i] = np.percentile(absr[i - window:i], pctl)
    v["threshold_pips"] = thr
    v["is_large"] = ~np.isnan(thr) & (absr > np.nan_to_num(thr, nan=np.inf))
    excl = []
    for r in v.itertuples(index=False):
        if not r.is_large:
            excl.append(None)
        elif pd.Timestamp(r.date).weekday() == 4:
            excl.append("friday")
        elif r.next is None or (isinstance(r.next, float) and np.isnan(r.next)) or r.next != r.date + timedelta(days=1):
            excl.append("next_not_adjacent")
        elif np.isnan(r.entry_mid):
            excl.append("missing_entry")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    v["excluded"] = excl
    v["tested"] = v["is_large"] & v["excluded"].isna()
    sgn = -np.sign(v["move_pips"])
    v["signed_pips"] = sgn * (v["exit_mid"] - v["entry_mid"]) / PIP
    v["signed_16_20_pips"] = sgn * (v["entry_mid"] - v["close_mid"]) / PIP
    v["net_bidask_pips"] = v["signed_pips"] - (v["entry_spread_pips"] + v["exit_spread_pips"]) / 2
    v["net_spec4_pips"] = v["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    v["net_x1_5_pips"] = v["signed_pips"] - 1.5 * (v["signed_pips"] - v["net_spec4_pips"])
    return v


def tradable_events(v: pd.DataFrame) -> pd.DataFrame:
    return v[v["tested"]]


def exclusion_counts(v: pd.DataFrame) -> dict:
    keys = ["friday", "next_not_adjacent", "missing_entry", "missing_exit", "entry_skipped_spread"]
    vc = v.loc[v["is_large"], "excluded"].value_counts()
    return {k: int(vc.get(k, 0)) for k in keys}


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


def decide_b18(res: dict) -> str:
    """Pre-registered E021 rule. SIGNAL: mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
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


def fomc_overlap(ev: pd.DataFrame, statement_dates: set[date]) -> dict:
    """Descriptive: events whose move day D or exit day N is a scheduled FOMC statement date."""
    if len(ev) == 0:
        return {"n": 0}
    d_is = ev["date"].isin(statement_dates)
    n_is = ev["next"].isin(statement_dates)
    return {"n": int(len(ev)), "move_day_is_fomc": int(d_is.sum()), "exit_day_is_fomc": int(n_is.sum()),
            "share_either": round(float((d_is | n_is).mean()), 4)}
