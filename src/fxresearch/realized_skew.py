"""E044 (backlog B50): daily realized skewness -> next-day EUR/USD (Jiang, Han & Yin 2019 sign, single-pair time-series
extension), DEV ONLY, 1 trial.

Definitions (fixed in the backlog, R099, and pre-registered 2026-11-11 R100, before any run):
* Grid and quotes: `post_jump.slot_grid` (5-minute NY-clock slots over trading time; quote at slot T = bid/ask OPEN of the first
  1-minute bar in [T, T+5 min); missing -> NaN, never filled).
* r_T = ln mid(T+5) - ln mid(T) (T+5 in clock time, both quotes present, else missing).
* Trading date D (17:00 NY roll, `sessions.trading_date` of slot T). Signal window of D: slots T with trading date D whose NY
  time is NOT in [16:55, 18:00), i.e. T = 18:00 NY (start of D) .. 16:50 NY on D -> 275 returns, the last one ending at 16:55.
* Valid D: >= 90% of the 275 returns present (>= 248) and sum r^2 > 0.
* RS(D) = sqrt(N) x sum r^3 / (sum r^2)^(3/2), N = number of valid returns of D.
* Position s = sign(RS(D)) (positive skew -> long EUR/USD on D+1; sign from the paper, stated before data).
* Trade: entry at 20:00 NY on NY calendar date D (start of trading date D+1, after the roll), exit at 16:55 NY on NY calendar
  date D+1 (E033 convention, `vol_state_fix.ny_quotes`). Signed return = s x (mid exit - mid entry) / PIP.
* Exclusions, counted, first reason in this order: `invalid_signal` (coverage < 90% or zero variance), `friday_excluded` (D is a
  Friday; weekend), `zero_signal` (RS == 0), `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at entry > 2.0
  pips, SPEC 4).
* Statistic: `overnight_reversal.evaluate_b32` (mean, median, SD, hit, one-sided t, moving-block bootstrap 95% CI, block 20
  dates, 2000 draws, seed 0). Decision `decide_b50` (= `overnight_reversal.decide_b34`): < 500 tested dates -> NONE; SIGNAL if
  mean > 1.0 pip AND CI lower > 0 AND one-sided t p < 0.05 (1 trial); WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
The signal uses quotes up to 16:55 NY on D; the trade enters at 20:00 NY on D, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd

from .data import PIP
from .overnight_reversal import decide_b34, evaluate_b32
from .post_jump import SLOT, slot_grid
from .sessions import NY, trading_date
from .vol_state_fix import (COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, ny_quotes)

EXPECTED_RETURNS = 275
MIN_VALID_SHARE = 0.90
MIN_VALID_RETURNS = int(np.ceil(MIN_VALID_SHARE * EXPECTED_RETURNS))   # 248
GAP_START_MIN = 16 * 60 + 55     # signal slots exclude NY [16:55, 18:00)
GAP_END_MIN = 18 * 60
START_HM = (18, 0)
CLOSE_HM = (16, 55)
ENTRY_HM = (20, 0)
EXIT_HM = (16, 55)
FRIDAY = 4
MIN_EVENTS = 500
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 20
EXCLUSION_ORDER = ("invalid_signal", "friday_excluded", "zero_signal", "missing_entry", "missing_exit",
                   "entry_skipped_spread")

decide_b50 = decide_b34
evaluate = evaluate_b32


def realized_skew(r) -> float:
    """sqrt(N) sum r^3 / (sum r^2)^1.5 over the non-NaN returns; NaN if no variance."""
    x = np.asarray(r, dtype=float)
    x = x[~np.isnan(x)]
    s2 = float(np.sum(x ** 2))
    if len(x) == 0 or s2 <= 0:
        return float("nan")
    return float(np.sqrt(len(x)) * np.sum(x ** 3) / s2 ** 1.5)


def slot_returns(grid: pd.DataFrame) -> pd.DataFrame:
    """Adds r (ln mid(T+5) - ln mid(T), contiguous slots only), trading_date and the signal-window flag."""
    g = grid.copy()
    idx = g.index
    mid = g["mid"].to_numpy()
    nxt = np.r_[mid[1:], np.nan]
    contiguous = np.r_[(idx[1:] - idx[:-1]) == SLOT, False]
    nxt = np.where(contiguous, nxt, np.nan)
    g["r"] = np.log(nxt) - np.log(mid)
    ny = idx.tz_convert(NY)
    mins = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    g["trading_date"] = trading_date(idx)
    g["in_window"] = ~((mins >= GAP_START_MIN) & (mins < GAP_END_MIN))
    return g


def daily_signal(g: pd.DataFrame) -> pd.DataFrame:
    """One row per trading date: n_valid returns, RS, valid flag, R(D) (mid 16:55 - mid 18:00 of D, pips)."""
    w = g[g["in_window"]]
    rows = []
    for d, grp in w.groupby("trading_date", sort=True):
        r = grp["r"].to_numpy(float)
        n = int((~np.isnan(r)).sum())
        rs = realized_skew(r)
        valid = n >= MIN_VALID_RETURNS and not np.isnan(rs)
        first_mid = grp["mid"].iloc[0] if len(grp) else np.nan
        ny0 = grp.index[0].tz_convert(NY)
        open_mid = first_mid if (ny0.hour, ny0.minute) == START_HM else np.nan
        rows.append({"date": d, "n_returns": n, "rs": rs if valid else np.nan, "rs_raw": rs, "valid": valid,
                     "open_mid": open_mid})
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=["date", "n_returns", "rs", "rs_raw", "valid", "open_mid"])
    return out


def build_days(sig: pd.DataFrame, q_close: pd.DataFrame, q_entry: pd.DataFrame, q_exit: pd.DataFrame) -> pd.DataFrame:
    """sig from daily_signal; q_close and q_entry keyed by NY calendar date D, q_exit keyed by NY calendar date D + 1."""
    df = sig.copy().reset_index(drop=True)
    rows = []
    for d in df["date"]:
        c, e, x = _get(q_close, d), _get(q_entry, d), _get(q_exit, d + timedelta(days=1))
        rows.append({"close_mid": sum(c) / 2 if c else np.nan,
                     "entry_mid": sum(e) / 2 if e else np.nan,
                     "entry_spread_pips": (e[1] - e[0]) / PIP if e else np.nan,
                     "exit_mid": sum(x) / 2 if x else np.nan,
                     "exit_spread_pips": (x[1] - x[0]) / PIP if x else np.nan})
    df = pd.concat([df, pd.DataFrame(rows, index=df.index)], axis=1)
    df["r_day_pips"] = (df["close_mid"] - df["open_mid"]) / PIP
    df["side"] = np.sign(df["rs"])
    excl = []
    for r in df.itertuples(index=False):
        if not r.valid:
            excl.append("invalid_signal")
        elif r.date.weekday() == FRIDAY:
            excl.append("friday_excluded")
        elif r.rs == 0:
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
    df["long_pips"] = (df["exit_mid"] - df["entry_mid"]) / PIP
    df["signed_pips"] = df["side"] * df["long_pips"]
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    return df


def frame_from_bars(bars: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    g = slot_returns(slot_grid(bars))
    sig = daily_signal(g)
    return g, build_days(sig, ny_quotes(bars, *CLOSE_HM), ny_quotes(bars, *ENTRY_HM), ny_quotes(bars, *EXIT_HM))


def minute_skew(bars: pd.DataFrame) -> pd.Series:
    """Robustness only: RS from 1-minute mid-open returns (consecutive minutes, both bars present) in the same window."""
    mid = (bars["bid_open"] + bars["ask_open"]) / 2
    idx = bars.index
    nxt = mid.shift(-1)
    contiguous = pd.Series(np.r_[(idx[1:] - idx[:-1]) == pd.Timedelta(minutes=1), False], index=idx)
    r = np.log(nxt / mid).where(contiguous)
    ny = idx.tz_convert(NY)
    mins = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    # return starts 18:00 .. 16:54 NY (last one ends at 16:55), same window as the 5-minute signal
    keep = ~((mins >= GAP_START_MIN) & (mins < GAP_END_MIN))
    r = r[keep]
    td = pd.Index(trading_date(r.index))
    return r.groupby(td).apply(realized_skew)


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"trading_dates": 0}
    vc = df["excluded"].value_counts()
    out = {"trading_dates": int(len(df)), "valid_signal_dates": int(df["valid"].sum())}
    for k in EXCLUSION_ORDER:
        out[k] = int(vc.get(k, 0))
    out["tested"] = int(df["tested"].sum())
    return out


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
