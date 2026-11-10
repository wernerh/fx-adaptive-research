"""E032 (backlog B27): post-Tokyo-fix EUR appreciation in the Krohn-Mueller-Whelan window, VAL ONLY.

Pre-registered 2026-11-10 R066, before any run. Every parameter below was fixed in the backlog (R065) or in the E032
methodology before any data were touched.

* Window (paper's, verbatim, New York clock): 20:55 -> 02:00 America/New_York. Both ends belong to the same FX trading date D
  (17:00 NY roll): entry 20:55 NY on NY calendar date D - 1, exit 02:00 NY on NY calendar date D.
* Universe: trading dates present in the bars that are Mon-Fri (Monday = Sunday-evening entry; no Friday-evening entries exist).
* Quote at hh:mm = bid/ask OPEN of the first bar in [hh:mm, hh:mm+5) NY whose trading date is D; missing -> NaN (E011 rule).
* Trade: LONG EUR/USD. Signed return = +(mid exit - mid entry) / PIP.
* Exclusions, counted, first reason in this order: `missing_entry`, `missing_exit`, `low_coverage` (< 280 of the 305 one-minute
  bars in [20:55, 02:00) NY), `entry_skipped_spread` (ask-bid at 20:55 NY > 2.0 pips, SPEC 4).
* Statistic: mean, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI (block 20 dates, 2000 draws, seed 0).
  Fewer than 200 valid dates -> "insufficient sample" -> NONE.
* Decision (`decide_b27`): SIGNAL if mean > 1.0 pip AND CI lower > 0 AND t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or
  p < 0.05); else NONE.
* Descriptive only: first hour 20:55 -> 21:55 NY (`first_hour_pips`) and rest 21:55 -> 02:00 (`rest_pips`); EDT/EST flag at entry.
Both quotes and the window are keyed by the trading date that contains them, so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .data import PIP
from .gotobi_fix import (ALPHA, BOOT_BLOCK, BOOT_N, COMMISSION_RT_PIPS, EDGE_MINUTES, MAX_ENTRY_SPREAD_PIPS, MIN_MEAN_PIPS,
                         SLIPPAGE_ENTRY_PIPS, cost_summary)
from .gotobi_fix import evaluate as _evaluate
from .sessions import trading_date

NY = "America/New_York"
ENTRY_HM = (20, 55)
EXIT_HM = (2, 0)
MID_HM = (21, 55)               # descriptive first-hour split
SIDE = 1                        # long EUR/USD (USD depreciation post-fix)
WINDOW_BARS = 305
MIN_WINDOW_BARS = 280
MIN_DATES = 200

__all__ = ["NY", "ENTRY_HM", "EXIT_HM", "MID_HM", "SIDE", "WINDOW_BARS", "MIN_WINDOW_BARS", "MIN_DATES", "ALPHA",
           "BOOT_BLOCK", "BOOT_N", "MAX_ENTRY_SPREAD_PIPS", "MIN_MEAN_PIPS", "td_quotes", "window_bar_counts",
           "frame_from_bars", "evaluate", "decide_b27", "counts", "cost_summary"]


def _ny_minutes(index: pd.DatetimeIndex) -> np.ndarray:
    loc = index.tz_convert(NY)
    return np.asarray(loc.hour) * 60 + np.asarray(loc.minute)


def td_quotes(bars: pd.DataFrame, hour: int, minute: int) -> pd.DataFrame:
    """Per trading date: bid/ask open of the first bar in [hh:mm, hh:mm+5) NY belonging to that trading date."""
    mins = _ny_minutes(bars.index)
    t0 = hour * 60 + minute
    sel = (mins >= t0) & (mins < t0 + EDGE_MINUTES)
    td = pd.Index(trading_date(bars.index))[sel]
    out = bars.loc[sel, ["bid_open", "ask_open"]].groupby(td).first()
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="trading_date")
    return out


def in_window(index: pd.DatetimeIndex) -> np.ndarray:
    mins = _ny_minutes(index)
    return (mins >= ENTRY_HM[0] * 60 + ENTRY_HM[1]) | (mins < EXIT_HM[0] * 60 + EXIT_HM[1])


def window_bar_counts(bars: pd.DataFrame) -> pd.Series:
    """Number of 1-minute bars in [20:55, 02:00) NY per trading date (both sides of NY midnight are in the same trading date)."""
    sel = in_window(bars.index)
    td = pd.Index(trading_date(bars.index))[sel]
    s = pd.Series(1, index=td).groupby(level=0).size()
    s.index = pd.Index([pd.Timestamp(x).date() for x in s.index])
    return s


def _get(qt: pd.DataFrame, d):
    if d in qt.index:
        b, a = qt.loc[d, "bid_open"], qt.loc[d, "ask_open"]
        if not (np.isnan(b) or np.isnan(a)):
            return float(b), float(a)
    return None


def _entry_is_edt(d) -> bool:
    """DST flag at 20:55 NY on NY calendar date d - 1 (wall clock; offset -4h = EDT)."""
    t = pd.Timestamp(d) - pd.Timedelta(days=1) + pd.Timedelta(hours=20, minutes=55)
    return t.tz_localize(NY).utcoffset() == pd.Timedelta(hours=-4)


def frame_from_bars(bars: pd.DataFrame, side: int = SIDE) -> pd.DataFrame:
    dates = sorted({pd.Timestamp(x).date() for x in trading_date(bars.index)})
    dates = [d for d in dates if d.weekday() < 5]
    eq, xq, mq = td_quotes(bars, *ENTRY_HM), td_quotes(bars, *EXIT_HM), td_quotes(bars, *MID_HM)
    nb = window_bar_counts(bars)
    rows = []
    for d in dates:
        e, x, m = _get(eq, d), _get(xq, d), _get(mq, d)
        rows.append({"date": d, "weekday": d.weekday(), "edt": _entry_is_edt(d), "window_bars": int(nb.get(d, 0)),
                     "entry_mid": sum(e) / 2 if e else np.nan,
                     "entry_spread_pips": (e[1] - e[0]) / PIP if e else np.nan,
                     "exit_mid": sum(x) / 2 if x else np.nan,
                     "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan,
                     "mid_mid": sum(m) / 2 if m else np.nan})
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
    df["tested"] = df["excluded"].isna()
    df["signed_pips"] = side * (df["exit_mid"] - df["entry_mid"]) / PIP
    df["first_hour_pips"] = side * (df["mid_mid"] - df["entry_mid"]) / PIP
    df["rest_pips"] = side * (df["exit_mid"] - df["mid_mid"]) / PIP
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    return df


def evaluate(signed, min_n: int = MIN_DATES) -> dict:
    x = np.asarray(signed, dtype=float)
    x = x[~np.isnan(x)]
    if len(x) < min_n:
        return {"n": int(len(x)), "note": "insufficient sample"}
    return _evaluate(x, block=BOOT_BLOCK)


def evaluate_desc(signed) -> dict:
    """Descriptive subsets: same statistics, only the 2 x block floor (no 200-date floor)."""
    return _evaluate(signed, block=BOOT_BLOCK)


def decide_b27(res: dict) -> str:
    """Pre-registered E032 rule (B27); thresholds identical to B25/B26."""
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
    vc = df["excluded"].value_counts() if len(df) else pd.Series(dtype=int)
    return {"weekday_trading_dates": int(len(df)),
            **{k: int(vc.get(k, 0)) for k in ("missing_entry", "missing_exit", "low_coverage", "entry_skipped_spread")},
            "dates_tested": int(df["tested"].sum()) if len(df) else 0}
