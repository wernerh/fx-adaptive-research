"""E033 (backlog B28 + B29): next-day reversal after a low-unexpected-volume day (B28) and next-day continuation after a
high-unexpected-volume day (B29), DEV ONLY, 2 trials in one experiment.

Definitions (fixed in the backlog, R068, and pre-registered 2026-11-10 R069, before any run):
* Volume gate (checked first): the bars must have a `volume` column and zero/NaN volume on <= 1% of the (dev) bars; otherwise the
  experiment is BLOCKED with 0 trials used and nothing else is computed (`volume_gate`).
* Trading date D (17:00 NY roll, SPEC 2, `sessions.trading_date`) is VALID if >= 1,300 of its 1,440 one-minute bars exist.
* V(D) = sum of `volume` over D's bars. UV(D) = V(D) / mean(V over the previous 21 VALID trading dates) - 1 (past only).
* LOW (B28): UV(D) < np.percentile(UV of the previous 60 valid dates that have a UV, 33) (strict, numpy linear interpolation).
  HIGH (B29): UV(D) > np.percentile(same history, 67) (strict). Burn-in: 21 valid dates for UV, then 60 UV values for the band.
* R(D) = (mid at 16:55 NY on D - mid at the open of D) / PIP. Open of D = bid/ask OPEN of the first bar in [17:00, 17:05) NY whose
  trading date is D (`overreaction_day.open_quotes`); 16:55 = first bar in [16:55, 17:00) NY on NY calendar date D
  (`vol_state_fix.ny_quotes`). Missing -> NaN (`missing_signal_quote`), never an event.
* Trade: B28 position -sign(R(D)), B29 position +sign(R(D)), from 20:00 NY on NY calendar date D (start of trading date D+1, after
  the roll) to 16:55 NY on NY calendar date D+1. Exclusions, counted, first reason in this order: `friday_excluded` (D is a Friday;
  weekend gap belongs to B17), `zero_move` (R(D) = 0), `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at
  20:00 NY > 2.0 pips, SPEC 4).
* Signed return = position x (mid exit - mid entry) / PIP.
* Statistic per trial: `vol_state_fix.evaluate` (mean, one-sided t, moving-block bootstrap block 10 events, 2000 draws, seed 0).
* Decision (`decide_b28`, same for B29): < 150 tested events -> NONE (insufficient sample). SIGNAL if mean > 1.0 pip AND CI lower
  > 0 AND one-sided t p < 0.025 (Bonferroni for 2 trials). WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE.
Only bars of D and earlier dates enter the event decision (volume of D ends at 16:59 NY, R at 16:55 NY); the trade starts at 20:00 NY,
so nothing looks ahead.
"""
from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd

from .data import PIP
from .overreaction_day import open_quotes
from .sessions import trading_date
from .vol_state_fix import (COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, MIN_MEAN_PIPS, SLIPPAGE_ENTRY_PIPS, _get, evaluate,
                            ny_quotes)

MIN_BARS = 1300
UV_WINDOW = 21
BAND_WINDOW = 60
LOW_PCTL = 33
HIGH_PCTL = 67
ALPHA = 0.025                    # Bonferroni for 2 trials
MIN_EVENTS = 150
MAX_BAD_VOLUME_SHARE = 0.01
OPEN_HM = (17, 0)
CLOSE_HM = (16, 55)
ENTRY_HM = (20, 0)
EXIT_HM = (16, 55)
FRIDAY = 4
BOOT_BLOCK = 10                  # used by vol_state_fix.evaluate


def volume_gate(bars: pd.DataFrame) -> dict:
    """Pre-registered gate: BLOCKED if no `volume` column or zero/NaN volume on > 1% of bars."""
    if "volume" not in bars.columns:
        return {"ok": False, "reason": "no volume column", "n_bars": int(len(bars))}
    v = pd.to_numeric(bars["volume"], errors="coerce")
    bad = int((v.isna() | (v <= 0)).sum())
    share = bad / len(v) if len(v) else 1.0
    return {"ok": bool(len(v) > 0 and share <= MAX_BAD_VOLUME_SHARE), "n_bars": int(len(v)), "zero_or_nan_bars": bad,
            "zero_or_nan_share": round(float(share), 6),
            "reason": None if len(v) and share <= MAX_BAD_VOLUME_SHARE else "zero/NaN volume share above 1%"}


def daily_volume(bars: pd.DataFrame) -> pd.DataFrame:
    """One row per trading date: n_bars, volume (sum), range_pips (mid high - low, descriptive)."""
    td = pd.Index(trading_date(bars.index), name="date")
    hi = (bars["bid_high"] + bars["ask_high"]).to_numpy() / 2
    lo = (bars["bid_low"] + bars["ask_low"]).to_numpy() / 2
    g = pd.DataFrame({"v": pd.to_numeric(bars["volume"], errors="coerce").to_numpy(), "hi": hi, "lo": lo}, index=td).groupby(level=0)
    out = pd.DataFrame({"n_bars": g.size(), "volume": g["v"].sum(), "range_pips": (g["hi"].max() - g["lo"].min()) / PIP})
    out = out.reset_index()
    out["date"] = [pd.Timestamp(x).date() for x in out["date"]]
    return out.sort_values("date").reset_index(drop=True)


def add_uv(day: pd.DataFrame, uv_window: int = UV_WINDOW, band_window: int = BAND_WINDOW) -> pd.DataFrame:
    """Past-only UV and tercile bands on VALID dates (n_bars >= MIN_BARS); NaN elsewhere."""
    day = day.copy()
    day["valid"] = day["n_bars"] >= MIN_BARS
    v = day[day["valid"]]
    vol = v["volume"].to_numpy(dtype=float)
    uv = np.full(len(v), np.nan)
    for i in range(uv_window, len(v)):
        base = vol[i - uv_window:i].mean()
        if base > 0:
            uv[i] = vol[i] / base - 1
    lo = np.full(len(v), np.nan)
    hi = np.full(len(v), np.nan)
    hist_idx = np.where(~np.isnan(uv))[0]
    for j in range(band_window, len(hist_idx)):
        i = hist_idx[j]
        h = uv[hist_idx[j - band_window:j]]
        lo[i] = np.percentile(h, LOW_PCTL)
        hi[i] = np.percentile(h, HIGH_PCTL)
    for col, arr in (("uv", uv), ("uv_p33", lo), ("uv_p67", hi)):
        day[col] = np.nan
        day.loc[v.index, col] = arr
    has = day["uv_p33"].notna() & day["uv"].notna()
    day["is_low"] = has & (day["uv"] < day["uv_p33"])
    day["is_high"] = has & (day["uv"] > day["uv_p67"])
    day["is_mid"] = has & ~day["is_low"] & ~day["is_high"]
    return day


def _mid(q):
    return sum(q) / 2 if q else np.nan


def _spread(q):
    return (q[1] - q[0]) / PIP if q else np.nan


def build_days(day: pd.DataFrame, q_open: pd.DataFrame, q_close: pd.DataFrame, q_entry: pd.DataFrame,
               q_exit: pd.DataFrame) -> pd.DataFrame:
    """`day` from daily_volume (date, n_bars, volume, range_pips). q_open keyed by trading date; q_close, q_entry keyed by NY
    calendar date D; q_exit keyed by NY calendar date D + 1."""
    df = add_uv(day)
    rows = []
    for d in df["date"]:
        n = d + timedelta(days=1)
        o, c, e, x = _get(q_open, d), _get(q_close, d), _get(q_entry, d), _get(q_exit, n)
        rows.append({"open_mid": _mid(o), "close_mid": _mid(c), "entry_mid": _mid(e), "entry_spread_pips": _spread(e),
                     "exit_mid": _mid(x), "exit_spread_pips": _spread(x)})
    df = pd.concat([df.reset_index(drop=True), pd.DataFrame(rows)], axis=1)
    df["r_pips"] = (df["close_mid"] - df["open_mid"]) / PIP
    excl = []
    for r in df.itertuples(index=False):
        if np.isnan(r.r_pips):
            excl.append("missing_signal_quote")
        elif r.date.weekday() == FRIDAY:
            excl.append("friday_excluded")
        elif r.r_pips == 0:
            excl.append("zero_move")
        elif np.isnan(r.entry_mid):
            excl.append("missing_entry")
        elif np.isnan(r.exit_mid):
            excl.append("missing_exit")
        elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
            excl.append("entry_skipped_spread")
        else:
            excl.append(None)
    df["excluded"] = excl
    df["tradable"] = df["excluded"].isna()
    df["tested_low"] = df["is_low"] & df["tradable"]
    df["tested_high"] = df["is_high"] & df["tradable"]
    df["tested_mid"] = df["is_mid"] & df["tradable"]
    move = (df["exit_mid"] - df["entry_mid"]) / PIP
    sgn = np.sign(df["r_pips"])
    df["reversal_pips"] = -sgn * move          # B28 statistic
    df["continuation_pips"] = sgn * move       # B29 statistic
    for name, col in (("rev", "reversal_pips"), ("cont", "continuation_pips")):
        nb = df[col] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
        n4 = nb - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
        df[f"{name}_net_bidask_pips"] = nb
        df[f"{name}_net_spec4_pips"] = n4
        df[f"{name}_net_x1_5_pips"] = df[col] - 1.5 * (df[col] - n4)
    return df


def frame_from_bars(bars: pd.DataFrame) -> pd.DataFrame:
    return build_days(daily_volume(bars), open_quotes(bars, *OPEN_HM), ny_quotes(bars, *CLOSE_HM), ny_quotes(bars, *ENTRY_HM),
                      ny_quotes(bars, *EXIT_HM))


def evaluate_b28(signed) -> dict:
    res = evaluate(signed)
    if res.get("n", 0) < MIN_EVENTS and "mean_pips" in res:
        res["note"] = f"insufficient sample (< {MIN_EVENTS} events)"
    return res


def decide_b28(res: dict) -> str:
    """Pre-registered E033 rule (B28 and B29): < 150 events -> NONE. SIGNAL if mean > 1.0 pip AND block-10 bootstrap CI lower > 0
    AND one-sided t p < 0.025; WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE."""
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


decide_b29 = decide_b28


def cost_summary(ev: pd.DataFrame, name: str, col: str) -> dict:
    if len(ev) == 0:
        return {"n": 0}
    return {"n": int(len(ev)), "mean_signed_mid_pips": round(float(ev[col].mean()), 3),
            "mean_net_bidask_pips": round(float(ev[f"{name}_net_bidask_pips"].mean()), 3),
            "mean_net_spec4_pips": round(float(ev[f"{name}_net_spec4_pips"].mean()), 3),
            "mean_net_costs_x1_5_pips": round(float(ev[f"{name}_net_x1_5_pips"].mean()), 3),
            "median_spread_entry_pips": round(float(ev["entry_spread_pips"].median()), 3),
            "median_spread_exit_pips": round(float(ev["exit_spread_pips"].median()), 3)}


def counts(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"trading_dates": 0}
    out = {"trading_dates": int(len(df)), "valid_dates": int(df["valid"].sum()),
           "low_coverage_dates": int((~df["valid"]).sum()), "dates_with_band": int(df["uv_p33"].notna().sum())}
    for lab, flag in (("low", "is_low"), ("high", "is_high"), ("mid", "is_mid")):
        ev = df[df[flag]]
        vc = ev["excluded"].value_counts()
        out[f"{lab}_events"] = int(len(ev))
        for k in ("missing_signal_quote", "friday_excluded", "zero_move", "missing_entry", "missing_exit",
                  "entry_skipped_spread"):
            out[f"{lab}_{k}"] = int(vc.get(k, 0))
        out[f"{lab}_tested"] = int(df[f"tested_{lab}"].sum())
    return out
