"""E019 (backlog B16): time-series momentum, 12-month (252 trading date) lookback, daily hold, dev only.

Definitions (fixed in pre-registration, R034, before any run):
* Trading dates: sorted unique `sessions.trading_date` of the (dev-only) bars. Lookback and hold are counted in this list.
* Quote at 16:00 NY on trading date D: bid/ask OPEN of the first bar in [16:00, 16:05) America/New_York on NY calendar
  date D (16:00 NY is before the 17:00 roll, so the NY date equals the trading date). Missing -> NaN.
* Signal s(D) = sign(mid16(D) - mid16(D252)), D252 = the trading date 252 positions earlier in the list.
  s = 0 (exactly equal mids) is a flat day: signed return 0, kept in n.
* Daily return r(D) = mid16(D+1) - mid16(D) in pips, D+1 = next trading date in the list.
  Signed return = s(D) x r(D).
* Test dates: positions i >= 252 that have a next date. Excluded and counted, first failing check in this order:
  `missing_now` (no 16:00 quote on D), `missing_past` (none on D252), `missing_next` (none on D+1).
  The last trading date (no D+1 inside the block) is reported as `no_next`.
Nothing at or after D+1 enters s(D), so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .fomc import ny_edge_quotes
from .metrics import block_bootstrap_mean_ci
from .sessions import trading_date

LOOKBACK = 252
HOLD_HOUR = 16                  # 16:00 NY entry and exit
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 20
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1       # SPEC 4
COMMISSION_RT_PIPS = 0.1        # SPEC 4


def daily_quotes(bars: pd.DataFrame) -> pd.DataFrame:
    """16:00 NY bid/ask per trading date of `bars` (NaN where the [16:00, 16:05) bar is missing)."""
    tds = sorted(set(trading_date(bars.index)))
    q = ny_edge_quotes(bars, HOLD_HOUR)[["bid_open", "ask_open"]]
    q = q.reindex(pd.Index(tds, name="trading_date"))
    return q.rename(columns={"bid_open": "bid", "ask_open": "ask"})


def build_daily(q: pd.DataFrame, lookback: int = LOOKBACK) -> tuple[pd.DataFrame, dict]:
    """Per test date: signal, mid return to next date, signed return, spreads. Returns (frame, exclusion counts)."""
    bid, ask = q["bid"].to_numpy(dtype=float), q["ask"].to_numpy(dtype=float)
    mid = (bid + ask) / 2
    dates = list(q.index)
    skips = {"missing_now": 0, "missing_past": 0, "missing_next": 0, "no_next": 0}
    rows = []
    for i in range(lookback, len(dates)):
        if i + 1 >= len(dates):
            skips["no_next"] += 1
            continue
        if np.isnan(mid[i]):
            skips["missing_now"] += 1
            continue
        if np.isnan(mid[i - lookback]):
            skips["missing_past"] += 1
            continue
        if np.isnan(mid[i + 1]):
            skips["missing_next"] += 1
            continue
        s = float(np.sign(mid[i] - mid[i - lookback]))
        r = (mid[i + 1] - mid[i]) / PIP
        rows.append({
            "pos": i, "date": dates[i], "next_date": dates[i + 1], "signal": s,
            "ret_pips": r, "signed_pips": s * r,
            "entry_spread_pips": (ask[i] - bid[i]) / PIP, "exit_spread_pips": (ask[i + 1] - bid[i + 1]) / PIP,
        })
    cols = ["pos", "date", "next_date", "signal", "ret_pips", "signed_pips", "entry_spread_pips", "exit_spread_pips"]
    return pd.DataFrame(rows, columns=cols), skips


def evaluate(signed: pd.Series) -> dict:
    """Mean test on daily signed returns: mean, sd, hit rate, one-sided t p (H1 mean > 0), block-20 bootstrap CI."""
    v = np.asarray(signed, dtype=float)
    v = v[~np.isnan(v)]
    n = len(v)
    if n < 2 * BOOT_BLOCK:
        return {"n": n, "note": "insufficient sample"}
    t = stats.ttest_1samp(v, 0.0, alternative="greater")
    lo, hi = block_bootstrap_mean_ci(v, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    return {
        "n": n,
        "mean_pips": round(float(v.mean()), 3),
        "median_pips": round(float(np.median(v)), 3),
        "sd_pips": round(float(v.std(ddof=1)), 3),
        "hit_rate": round(float((v > 0).mean()), 4),
        "t_stat": round(float(t.statistic), 3),
        "t_p_one_sided": round(float(t.pvalue), 4),
        "mean_ci95_block_boot": (round(lo, 3), round(hi, 3)),
    }


def decide_b16(res: dict) -> str:
    """Pre-registered E019 rule. SIGNAL: mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
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


def position_runs(df: pd.DataFrame) -> pd.DataFrame:
    """Round trips: maximal runs of the same non-zero signal on consecutive trading dates (pos i, i+1, ...).
    A flat day, a sign change or an excluded date ends a run. Entry at 16:00 NY on the first date, exit at 16:00 NY on
    the day after the last date."""
    rows = []
    cur = None
    for r in df.itertuples(index=False):
        if r.signal == 0:
            if cur:
                rows.append(cur)
            cur = None
            continue
        if cur and cur["signal"] == r.signal and r.pos == cur["last_pos"] + 1:
            cur["gross_pips"] += r.signed_pips
            cur["n_days"] += 1
            cur["last_pos"] = r.pos
            cur["exit_spread_pips"] = r.exit_spread_pips
        else:
            if cur:
                rows.append(cur)
            cur = {"signal": r.signal, "start": r.date, "last_pos": r.pos, "n_days": 1, "gross_pips": r.signed_pips,
                   "entry_spread_pips": r.entry_spread_pips, "exit_spread_pips": r.exit_spread_pips}
    if cur:
        rows.append(cur)
    out = pd.DataFrame(rows, columns=["signal", "start", "last_pos", "n_days", "gross_pips",
                                      "entry_spread_pips", "exit_spread_pips"])
    out["net_bidask_pips"] = out["gross_pips"] - (out["entry_spread_pips"] + out["exit_spread_pips"]) / 2
    out["net_spec4_pips"] = out["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    return out


def cost_summary(df: pd.DataFrame) -> dict:
    """Costs charged per round trip (run), reported per day and per run. Swap/carry is NOT in the data."""
    runs = position_runs(df)
    n_days = len(df)
    if n_days == 0:
        return {"n_days": 0}
    gross = float(df["signed_pips"].sum())
    cost_spec = float((runs["gross_pips"] - runs["net_spec4_pips"]).sum())
    sig = df["signal"].to_numpy()
    flips = int(((sig[1:] != sig[:-1]) & (sig[1:] != 0) & (sig[:-1] != 0)).sum())
    return {
        "n_days": n_days,
        "n_round_trips": int(len(runs)),
        "n_sign_flips": flips,
        "mean_days_per_round_trip": round(float(runs["n_days"].mean()), 2) if len(runs) else None,
        "mean_signed_mid_pips_per_day": round(gross / n_days, 3),
        "mean_net_bidask_pips_per_day": round(float(runs["net_bidask_pips"].sum()) / n_days, 3),
        "mean_net_spec4_pips_per_day": round((gross - cost_spec) / n_days, 3),
        "mean_net_costs_x1_5_pips_per_day": round((gross - 1.5 * cost_spec) / n_days, 3),
        "mean_net_spec4_pips_per_round_trip": round(float(runs["net_spec4_pips"].mean()), 3) if len(runs) else None,
        "median_entry_spread_pips": round(float(df["entry_spread_pips"].median()), 3),
    }
