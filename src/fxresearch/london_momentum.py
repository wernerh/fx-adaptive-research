"""E027 (backlog B22): London-open intraday momentum into the pre-London-fix half hour, dev only.

Definitions (fixed in the backlog, R050, and pre-registered 2026-11-09 R053, before any run):
* Times are Europe/London local, so US/UK DST mismatches do not shift the windows.
* Quote at hh:mm London on London calendar date d = bid/ask OPEN of the first 1-minute bar in [hh:mm, hh:mm+5) Europe/London
  (`london_quotes`). Missing -> NaN, never filled. Dates = trading-date set of the bars (08:00-16:00 London lies inside one trading
  date, 17:00 NY roll).
* Signal r1(D) = (mid 08:30 - mid 08:00 London) / PIP. Every valid date is an event (no threshold).
* Trade: position sign(r1(D)) from 15:25 London to 15:55 London on D (last half hour before the 16:00 London fix, exit before the
  fix window). Signed return = sign(r1) x (mid 15:55 - mid 15:25) / PIP.
* Exclusions, counted, first reason in this order: `invalid_missing_signal_quote` (08:00 or 08:30 missing), `zero_signal`
  (r1 == 0, no trade), `missing_entry` (15:25), `missing_exit` (15:55), `entry_skipped_spread` (ask-bid at 15:25 > 2.0 pips, SPEC 4).
* Statistic: mean, median, SD, hit, one-sided t (H1 mean > 0), moving-block bootstrap 95% CI (block 20 events, 2000 draws, seed 0).
* Decision rule `decide_b22`: thresholds identical to E022/E024/E026 (SIGNAL: mean > 1.0 AND CI lower > 0 AND p < 0.05; WEAK:
  mean > 0 and (CI lower > 0 or p < 0.05); else NONE). Only the bootstrap block length differs (20, fixed in the backlog draft).
Only quotes at or before 08:30 London on D decide the side; the entry is at 15:25, so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .fixes import month_end_flag
from .metrics import block_bootstrap_mean_ci
from .sessions import trading_date
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, decide_b19

LDN = "Europe/London"
NY = "America/New_York"
EDGE_MINUTES = 5
SIGNAL_START_HM = (8, 0)
SIGNAL_END_HM = (8, 30)
ENTRY_HM = (15, 25)
EXIT_HM = (15, 55)
ALT_SIGNAL_END_HM = (9, 0)       # descriptive first-hour signal only
BOOT_BLOCK = 20
BOOT_N = 2000

EXCLUSION_ORDER = ("invalid_missing_signal_quote", "zero_signal", "missing_entry", "missing_exit", "entry_skipped_spread")


def london_quotes(bars: pd.DataFrame, hour: int, minute: int = 0) -> pd.DataFrame:
    """Per London calendar date: bid/ask open of the first bar in [hh:mm, hh:mm+5) Europe/London."""
    ld = bars.index.tz_convert(LDN)
    mins = np.asarray(ld.hour) * 60 + np.asarray(ld.minute)
    t0 = hour * 60 + minute
    sel = (mins >= t0) & (mins < t0 + EDGE_MINUTES)
    ldd = pd.Index(ld.date)[sel]
    out = bars.loc[sel, ["bid_open", "ask_open"]].groupby(ldd).first()
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="ldn_date")
    return out


def _mid(q):
    return sum(q) / 2 if q else np.nan


def _ny_offset_hours(d) -> float:
    """London minus New York UTC-offset in hours at 15:25 London on date d (5 normally, 4 in DST-mismatch weeks)."""
    t = pd.Timestamp(f"{d} 15:25", tz=LDN)
    return (t.utcoffset() - t.tz_convert(NY).utcoffset()).total_seconds() / 3600


def build_days(dates, q_s: pd.DataFrame, q_e: pd.DataFrame, q_in: pd.DataFrame, q_out: pd.DataFrame,
               q_alt: pd.DataFrame | None = None) -> pd.DataFrame:
    rows = []
    for d in sorted(dates):
        s, e, i, o = _get(q_s, d), _get(q_e, d), _get(q_in, d), _get(q_out, d)
        a = _get(q_alt, d) if q_alt is not None else None
        rows.append({"date": d, "s_mid": _mid(s), "e_mid": _mid(e), "alt_mid": _mid(a),
                     "entry_mid": _mid(i), "entry_spread_pips": (i[1] - i[0]) / PIP if i else np.nan,
                     "exit_mid": _mid(o), "exit_spread_pips": (o[1] - o[0]) / PIP if o else np.nan})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["r1_pips"] = (df["e_mid"] - df["s_mid"]) / PIP
    df["r1_hour_pips"] = (df["alt_mid"] - df["s_mid"]) / PIP
    df["valid"] = df["r1_pips"].notna()
    excl = []
    for r in df.itertuples(index=False):
        if not r.valid:
            excl.append("invalid_missing_signal_quote")
        elif r.r1_pips == 0:
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
    sign = np.sign(df["r1_pips"])
    df["side"] = sign
    df["last_half_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["signed_pips"] = sign * df["last_half_pips"]
    df["signed_hour_signal_pips"] = np.sign(df["r1_hour_pips"]) * df["last_half_pips"]
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    df["month_end"] = month_end_flag(pd.Index(pd.to_datetime(df["date"]))).to_numpy()
    df["dst_mismatch"] = [_ny_offset_hours(d) != 5.0 for d in df["date"]]
    return df


def frame_from_bars(bars: pd.DataFrame) -> pd.DataFrame:
    dates = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    return build_days(dates, london_quotes(bars, *SIGNAL_START_HM), london_quotes(bars, *SIGNAL_END_HM),
                      london_quotes(bars, *ENTRY_HM), london_quotes(bars, *EXIT_HM), london_quotes(bars, *ALT_SIGNAL_END_HM))


def evaluate_b22(signed) -> dict:
    """As vol_state_fix.evaluate but with the pre-registered block-20 moving-block bootstrap."""
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


def decide_b22(res: dict) -> str:
    """Pre-registered E027 rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05;
    WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE (thresholds identical to E022/E024/E026)."""
    return decide_b19(res)


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"trading_dates": 0, "events_tested": 0}
    vc = df["excluded"].value_counts()
    out = {"trading_dates": int(len(df)), "valid_dates": int(df["valid"].sum())}
    out.update({k: int(vc.get(k, 0)) for k in EXCLUSION_ORDER})
    out["events_tested"] = int(df["tested"].sum())
    out["dst_mismatch_dates_tested"] = int(df.loc[df["tested"], "dst_mismatch"].sum())
    return out


def slope(df: pd.DataFrame) -> dict:
    """Descriptive OLS slope of the (unsigned) 15:25-15:55 return on r1, tested dates."""
    t = df[df["tested"]]
    if len(t) < 3:
        return {}
    r = stats.linregress(t["r1_pips"], t["last_half_pips"])
    return {"n": int(len(t)), "slope": round(float(r.slope), 4), "t_stat": round(float(r.slope / r.stderr), 3),
            "p_two_sided": round(float(r.pvalue), 4)}
