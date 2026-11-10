"""E030 (backlog B25): USD appreciation into the Tokyo fix on gotobi dates, dev only.

Pre-registered 2026-11-10 R061, before any run. Every parameter below was fixed in the backlog (R060) or in the E030
methodology before any data were touched.

* Gotobi (Tokyo calendar date G, Mon-Fri): G is gotobi if its day of month is 5, 10, 15, 20, 25 or 30, or it is the last
  calendar day of its month (NOMINAL). A nominal day falling on Saturday or Sunday moves to the preceding Friday; that Friday is
  gotobi (flagged `weekend_shifted` only if it is not itself nominal). Japanese public holidays are NOT in the repo and are not
  shifted (limitation). Practitioner convention, UNVERIFIED as Ito & Yamada's (2017) definition.
* Universe: trading dates (17:00 NY roll) present in the bars that are Mon-Fri. For 08:55-10:55 Asia/Tokyo the trading date
  equals the Tokyo calendar date (window = 23:55-01:55 UTC, after the 17:00 NY roll), so the Tokyo date is the trading date.
* Quote at hh:mm = bid/ask OPEN of the first bar in [hh:mm, hh:mm+5) Asia/Tokyo on that Tokyo date; missing -> NaN.
* Trade on a gotobi date: SHORT EUR/USD from 08:55 to 09:55 Tokyo. Signed return = -(mid exit - mid entry) / PIP.
* Exclusions, counted, first reason in this order: `missing_entry`, `missing_exit`, `low_coverage` (< 55 of the 60 one-minute
  bars in [08:55, 09:55) Tokyo, as E011), `entry_skipped_spread` (ask-bid at 08:55 > 2.0 pips, SPEC 4).
* Statistic: mean, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI (block 20 events, 2000 draws, seed 0).
  Fewer than 40 tested events (2 x block) -> "insufficient sample" -> NONE.
* Decision (`decide_b25`): SIGNAL if mean > 1.0 pip AND CI lower > 0 AND t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or
  p < 0.05); else NONE.
The gotobi flag is a pure calendar function, so nothing looks ahead.
"""
from __future__ import annotations

import calendar
from datetime import date, timedelta

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import trading_date

TOKYO = "Asia/Tokyo"
GOTOBI_DAYS = (5, 10, 15, 20, 25, 30)
ENTRY_HM = (8, 55)
EXIT_HM = (9, 55)
LATE_HM = (9, 25)               # descriptive last half hour 09:25 -> 09:55
SIDE = -1                       # short EUR/USD (USD bought into the fix)
EDGE_MINUTES = 5
WINDOW_BARS = 60
MIN_WINDOW_BARS = 55
MAX_ENTRY_SPREAD_PIPS = 2.0
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 20
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1       # SPEC 4
COMMISSION_RT_PIPS = 0.1        # SPEC 4


def _last_day(d: date) -> int:
    return calendar.monthrange(d.year, d.month)[1]


def is_nominal_gotobi(d: date) -> bool:
    return d.day in GOTOBI_DAYS or d.day == _last_day(d)


def gotobi_info(d: date) -> dict:
    """For a calendar date d: gotobi (bool), weekend_shifted (bool), month_end (bool: a source day is the month's last day).

    Weekend dates are never gotobi (their nominal status is moved to the preceding Friday)."""
    if d.weekday() >= 5:
        return {"gotobi": False, "weekend_shifted": False, "month_end": False}
    sources = [d] if is_nominal_gotobi(d) else []
    shifted = []
    if d.weekday() == 4:
        for k in (1, 2):
            s = d + timedelta(days=k)
            if is_nominal_gotobi(s):
                shifted.append(s)
    allsrc = sources + shifted
    return {"gotobi": bool(allsrc),
            "weekend_shifted": bool(shifted) and not sources,
            "month_end": any(s.day == _last_day(s) for s in allsrc)}


def local_quotes(bars: pd.DataFrame, tz: str, hour: int, minute: int) -> pd.DataFrame:
    """Per local calendar date in `tz`: bid/ask open of the first bar in [hh:mm, hh:mm+5)."""
    loc = bars.index.tz_convert(tz)
    mins = np.asarray(loc.hour) * 60 + np.asarray(loc.minute)
    t0 = hour * 60 + minute
    sel = (mins >= t0) & (mins < t0 + EDGE_MINUTES)
    ld = pd.Index(loc.date)[sel]
    out = bars.loc[sel, ["bid_open", "ask_open"]].groupby(ld).first()
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="local_date")
    return out


def window_bar_counts(bars: pd.DataFrame, tz: str, start_hm: tuple[int, int], end_hm: tuple[int, int]) -> pd.Series:
    """Number of 1-minute bars in [start, end) local time, per local calendar date."""
    loc = bars.index.tz_convert(tz)
    mins = np.asarray(loc.hour) * 60 + np.asarray(loc.minute)
    sel = (mins >= start_hm[0] * 60 + start_hm[1]) & (mins < end_hm[0] * 60 + end_hm[1])
    s = pd.Series(1, index=pd.Index(loc.date)[sel]).groupby(level=0).size()
    s.index = pd.Index([pd.Timestamp(x).date() for x in s.index])
    return s


def _get(qt: pd.DataFrame, d):
    if d in qt.index:
        b, a = qt.loc[d, "bid_open"], qt.loc[d, "ask_open"]
        if not (np.isnan(b) or np.isnan(a)):
            return float(b), float(a)
    return None


def universe(bars: pd.DataFrame) -> list[date]:
    """Sorted Mon-Fri trading dates present in the bars."""
    td = sorted({pd.Timestamp(x).date() for x in trading_date(bars.index)})
    return [d for d in td if d.weekday() < 5]


def build_days(dates: list[date], entry_q: pd.DataFrame, exit_q: pd.DataFrame, late_q: pd.DataFrame,
               nbars: pd.Series, side: int = SIDE) -> pd.DataFrame:
    rows = []
    for d in dates:
        g = gotobi_info(d)
        e, x, l_ = _get(entry_q, d), _get(exit_q, d), _get(late_q, d)
        rows.append({"date": d, "weekday": d.weekday(), **g, "window_bars": int(nbars.get(d, 0)),
                     "entry_mid": sum(e) / 2 if e else np.nan,
                     "entry_spread_pips": (e[1] - e[0]) / PIP if e else np.nan,
                     "exit_mid": sum(x) / 2 if x else np.nan,
                     "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan,
                     "late_mid": sum(l_) / 2 if l_ else np.nan})
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    excl = []
    for r in df.itertuples(index=False):
        if np.isnan(r.entry_mid):
            excl.append("missing_entry")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.window_bars < MIN_WINDOW_BARS:
            excl.append("low_coverage")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tradable"] = df["excluded"].isna()
    df["tested"] = df["gotobi"] & df["tradable"]
    df["signed_pips"] = side * (df["exit_mid"] - df["entry_mid"]) / PIP
    df["late_signed_pips"] = side * (df["exit_mid"] - df["late_mid"]) / PIP
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    return df


def frame_from_bars(bars: pd.DataFrame, side: int = SIDE) -> pd.DataFrame:
    return build_days(universe(bars), local_quotes(bars, TOKYO, *ENTRY_HM), local_quotes(bars, TOKYO, *EXIT_HM),
                      local_quotes(bars, TOKYO, *LATE_HM), window_bar_counts(bars, TOKYO, ENTRY_HM, EXIT_HM), side=side)


def evaluate(signed, block: int = BOOT_BLOCK) -> dict:
    x = np.asarray(signed, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2 * block:
        return {"n": n, "note": "insufficient sample"}
    t = stats.ttest_1samp(x, 0.0, alternative="greater")
    lo, hi = block_bootstrap_mean_ci(x, block=block, n_boot=BOOT_N, seed=0)
    return {"n": n, "mean_pips": round(float(x.mean()), 3), "median_pips": round(float(np.median(x)), 3),
            "sd_pips": round(float(x.std(ddof=1)), 3), "hit_rate": round(float((x > 0).mean()), 4),
            "t_stat": round(float(t.statistic), 3), "t_p_one_sided": round(float(t.pvalue), 4),
            "mean_ci95_block_boot": (round(lo, 3), round(hi, 3))}


def decide_b25(res: dict) -> str:
    """Pre-registered E030 rule (B25)."""
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


def counts(df: pd.DataFrame) -> dict:
    g = df[df["gotobi"]] if len(df) else df
    vc = g["excluded"].value_counts() if len(g) else pd.Series(dtype=int)
    return {"weekday_dates": int(len(df)), "gotobi_dates": int(len(g)),
            "gotobi_weekend_shifted": int(g["weekend_shifted"].sum()) if len(g) else 0,
            "gotobi_month_end": int(g["month_end"].sum()) if len(g) else 0,
            **{k: int(vc.get(k, 0)) for k in ("missing_entry", "missing_exit", "low_coverage", "entry_skipped_spread")},
            "events_tested": int(df["tested"].sum()) if len(df) else 0}


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
