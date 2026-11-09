"""E028 (backlog B23): intraday continuation on overreaction days, dev only.

Definitions (fixed in the backlog, R055, and pre-registered 2026-11-09 R056, before any run):
* Trading date D starts 17:00 NY on the previous NY calendar date (SPEC 2, `sessions.trading_date`).
* Open quote of D = bid/ask OPEN of the first 1-minute bar in [17:00, 17:05) NY whose trading date is D (`open_quotes`).
  Other quotes at hh:mm NY on D = first bar in [hh:mm, hh:mm+5) NY on NY calendar date D (`vol_state_fix.ny_quotes`;
  for 12:00 and 16:30 NY the NY calendar date equals the trading date). Missing -> NaN, never filled.
* r(D) = (mid 12:00 NY on D - mid at the open of D) / PIP. D is VALID if both quotes exist; otherwise
  `invalid_missing_signal_quote`, counted, never an event, not in the history.
* m(D), s(D) = mean and sample SD (ddof=1) of r over the 60 valid dates before D (past only). First 60 valid dates are burn-in.
* Event: valid D past burn-in with r(D) > m + 2s or r(D) < m - 2s (strict).
* Trade: position sign(r(D) - m(D)) from 12:00 NY (the same quote that ends the signal) to 16:30 NY on D. Exclusions, counted, first
  reason in this order: `missing_exit`, `entry_skipped_spread` (ask-bid at 12:00 > 2.0 pips, SPEC 4).
* Signed return = sign x (mid 16:30 - mid 12:00) / PIP.
* Decision rule: thresholds identical to E022/E024 (`decide_b23` = `vol_state_fix.decide_b19`) with the pre-registered block-5
  moving-block bootstrap (2000 draws, seed 0) in `evaluate_b23`.
Only quotes at or before 12:00 NY on D (and past dates) enter the event decision, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import NY, trading_date
from .vol_state_fix import (COMMISSION_RT_PIPS, EDGE_MINUTES, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, decide_b19,
                            ny_quotes)

WINDOW = 60
K = 2.0
ALT_KS = (1.5, 2.5)              # descriptive only
OPEN_HM = (17, 0)
ENTRY_HM = (12, 0)               # also the end of the signal window
EXIT_HM = (16, 30)
BOOT_BLOCK = 5
BOOT_N = 2000


def open_quotes(bars: pd.DataFrame, hour: int = OPEN_HM[0], minute: int = OPEN_HM[1]) -> pd.DataFrame:
    """Per TRADING date: bid/ask open of the first bar in [17:00, 17:05) NY that belongs to that trading date."""
    ny = bars.index.tz_convert(NY)
    mins = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    t0 = hour * 60 + minute
    sel = (mins >= t0) & (mins < t0 + EDGE_MINUTES)
    td = pd.Index(trading_date(bars.index))[sel]
    out = bars.loc[sel, ["bid_open", "ask_open"]].groupby(td).first()
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="trading_date")
    return out


def _first_friday(d: date) -> bool:
    return d.weekday() == 4 and d.day <= 7


def add_bands(df: pd.DataFrame, window: int = WINDOW) -> pd.DataFrame:
    """Past-only rolling mean and sample SD of r over the previous `window` valid dates; NaN on invalid and burn-in dates."""
    df = df.copy()
    v = df[df["valid"]]
    a = v["r_pips"].to_numpy()
    m = np.full(len(v), np.nan)
    s = np.full(len(v), np.nan)
    for i in range(window, len(v)):
        h = a[i - window:i]
        m[i] = h.mean()
        s[i] = h.std(ddof=1)
    df["hist_mean_pips"] = np.nan
    df["hist_sd_pips"] = np.nan
    df.loc[v.index, "hist_mean_pips"] = m
    df.loc[v.index, "hist_sd_pips"] = s
    return df


def _event(df: pd.DataFrame, k: float) -> pd.Series:
    has = df["valid"] & df["hist_sd_pips"].notna()
    up = df["r_pips"] > df["hist_mean_pips"] + k * df["hist_sd_pips"]
    dn = df["r_pips"] < df["hist_mean_pips"] - k * df["hist_sd_pips"]
    return has & (up | dn)


def build_days(dates, q_open: pd.DataFrame, q_entry: pd.DataFrame, q_exit: pd.DataFrame, window: int = WINDOW,
               k: float = K) -> pd.DataFrame:
    """One row per trading date in `dates` (sorted): r, validity, past-only bands, event flag, trade, exclusions, returns."""
    rows = []
    for d in sorted(dates):
        o, e, x = _get(q_open, d), _get(q_entry, d), _get(q_exit, d)
        rows.append({"date": d,
                     "open_mid": sum(o) / 2 if o else np.nan,
                     "entry_mid": sum(e) / 2 if e else np.nan,
                     "entry_spread_pips": (e[1] - e[0]) / PIP if e else np.nan,
                     "exit_mid": sum(x) / 2 if x else np.nan,
                     "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["r_pips"] = (df["entry_mid"] - df["open_mid"]) / PIP
    df["valid"] = df["r_pips"].notna()
    df = add_bands(df, window)
    df["is_event"] = _event(df, k)
    for ka in ALT_KS:
        df[f"is_event_k{ka}"] = _event(df, ka)
    excl = []
    for r in df.itertuples(index=False):
        if not r.valid:
            excl.append("invalid_missing_signal_quote")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tradable"] = df["excluded"].isna()
    df["tested"] = df["is_event"] & df["tradable"]
    sign = np.sign(df["r_pips"] - df["hist_mean_pips"])
    df["side"] = sign
    df["signed_pips"] = sign * (df["exit_mid"] - df["entry_mid"]) / PIP
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    df["first_friday"] = [_first_friday(d) for d in df["date"]]
    return df


def frame_from_bars(bars: pd.DataFrame, window: int = WINDOW, k: float = K) -> pd.DataFrame:
    dates = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    return build_days(dates, open_quotes(bars), ny_quotes(bars, *ENTRY_HM), ny_quotes(bars, *EXIT_HM), window, k)


def evaluate_b23(signed) -> dict:
    """As vol_state_fix.evaluate but with the pre-registered block-5 moving-block bootstrap."""
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


def decide_b23(res: dict) -> str:
    """Pre-registered E028 rule (thresholds identical to E022/E024): SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0
    AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE."""
    return decide_b19(res)


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
        "missing_exit": int(vc.get("missing_exit", 0)),
        "entry_skipped_spread": int(vc.get("entry_skipped_spread", 0)),
        "events_tested": int(df["tested"].sum()),
    }
