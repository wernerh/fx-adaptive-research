"""E052 (backlog B64): lagged daily Bitcoin return -> next-day EUR/USD, 16:00 NY daily hold, DEV ONLY, 1 trial.

Definitions (fixed in the backlog, R307, and pre-registered 2026-11-20 R308, before any run):
* EUR/USD dates and quotes: `tsmom.daily_quotes` (E019/E050/E051 code): bid/ask OPEN of the first 1-minute bar in
  [16:00, 16:05) America/New_York per FX trading date (17:00 NY roll; 16:00 NY is before the roll, so NY date = trading date).
* BTC quote on date D: bid/ask OPEN of the first BTC/USD bar in [16:00, 16:05) New York on NY calendar date D
  (`fomc.ny_edge_quotes`). Bid/ask <= 0 or missing -> invalid, never filled, no fallback.
* B(D) = ln(BTC mid 16:00 NY D) - ln(BTC mid 16:00 NY on the previous EUR/USD trading date in the grid, position i-1).
  Monday's B spans the weekend (BTC trades 24/7).
* s(D) = sign(B). Position long EUR/USD if B > 0 (BTC up -> USD weaker; Feng-Zhang 2023 EUR in-sample b1 > 0).
* Test dates: grid positions i >= 1 with START <= D <= END. Excluded and counted, first failing check in this order:
  `no_next` (last date), `missing_now` (EUR/USD 16:00 D), `missing_next` (EUR/USD 16:00 D+1), `missing_btc` (BTC at D or at
  the previous date), `zero_signal` (B == 0), `btc_jump` (|B| > 0.50, bad-print guard).
* Signed return = s(D) x (mid16(D+1) - mid16(D)) / PIP.
* Data gate first: a valid BTC quote at BOTH points on >= 90% of grid dates in [START, END] (with a previous date);
  otherwise BLOCKED (0 trials).
* Statistic and decision: `tsmom.evaluate` and `tsmom.decide_b16` (mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND
  one-sided t p < 0.05 -> SIGNAL; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE); fewer than 500 tested dates
  -> NONE.
s(D) uses BTC bar opens at 16:00 NY on D and earlier, the same instant as the EUR/USD entry open, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import date

import numpy as np
import pandas as pd

from .data import PIP
from .fomc import ny_edge_quotes
from .tsmom import HOLD_HOUR, decide_b16

BTC = "btcusd"
START = date(2017, 5, 9)
END = date(2020, 12, 31)
MAX_ABS_B = 0.50
MIN_BOTH_VALID_SHARE = 0.90
MIN_EVENTS = 500
SIGN = 1.0
EXCLUSION_ORDER = ("no_next", "missing_now", "missing_next", "missing_btc", "zero_signal", "btc_jump")
COLS = ["pos", "date", "next_date", "weekday", "btc_mid", "prev_btc_mid", "b", "signal", "ret_pips", "signed_pips",
        "entry_spread_pips", "exit_spread_pips"]


def btc_mids(btc_bars: pd.DataFrame, dates) -> np.ndarray:
    """BTC mid at 16:00 NY (open of first bar in [16:00, 16:05)) per date in `dates`; NaN if missing or non-positive."""
    if len(btc_bars) == 0:
        return np.full(len(dates), np.nan)
    q = ny_edge_quotes(btc_bars, HOLD_HOUR)[["bid_open", "ask_open"]].reindex(pd.Index(list(dates)))
    b, a = q["bid_open"].to_numpy(dtype=float), q["ask_open"].to_numpy(dtype=float)
    ok = np.isfinite(b) & np.isfinite(a) & (b > 0) & (a > 0)
    return np.where(ok, (b + a) / 2, np.nan)


def build_daily(q: pd.DataFrame, btc_mid: np.ndarray, start=START, end=END) -> tuple[pd.DataFrame, dict]:
    """Per test date D in [start, end]: BTC signal, EUR/USD 16:00 -> 16:00 next-date return. Returns (frame, exclusions)."""
    bid, ask = q["bid"].to_numpy(dtype=float), q["ask"].to_numpy(dtype=float)
    mid = (bid + ask) / 2
    dates = list(q.index)
    skips = {k: 0 for k in EXCLUSION_ORDER}
    rows = []
    for i in range(1, len(dates)):
        d = dates[i]
        if d < start or d > end:
            continue
        if i + 1 >= len(dates):
            skips["no_next"] += 1
            continue
        if np.isnan(mid[i]):
            skips["missing_now"] += 1
            continue
        if np.isnan(mid[i + 1]):
            skips["missing_next"] += 1
            continue
        if np.isnan(btc_mid[i]) or np.isnan(btc_mid[i - 1]):
            skips["missing_btc"] += 1
            continue
        b = float(np.log(btc_mid[i]) - np.log(btc_mid[i - 1]))
        if b == 0:
            skips["zero_signal"] += 1
            continue
        if abs(b) > MAX_ABS_B:
            skips["btc_jump"] += 1
            continue
        s = SIGN * float(np.sign(b))
        r = (mid[i + 1] - mid[i]) / PIP
        rows.append({
            "pos": i, "date": d, "next_date": dates[i + 1], "weekday": pd.Timestamp(d).weekday(),
            "btc_mid": btc_mid[i], "prev_btc_mid": btc_mid[i - 1], "b": b, "signal": s, "ret_pips": r,
            "signed_pips": s * r, "entry_spread_pips": (ask[i] - bid[i]) / PIP,
            "exit_spread_pips": (ask[i + 1] - bid[i + 1]) / PIP,
        })
    return pd.DataFrame(rows, columns=COLS), skips


def data_gate(q: pd.DataFrame, btc_mid: np.ndarray, n_btc_bars: int, start=START, end=END) -> dict:
    """BLOCKED if BTC is empty or both 16:00 NY BTC quotes are valid on < 90% of grid dates in [start, end]."""
    out = {"btc_bars": int(n_btc_bars)}
    dates = list(q.index)
    pos = [i for i in range(1, len(dates)) if start <= dates[i] <= end]
    if n_btc_bars == 0 or not pos:
        return {**out, "ok": False, "reason": "btc data missing"}
    both = int(sum(1 for i in pos if np.isfinite(btc_mid[i]) and np.isfinite(btc_mid[i - 1])))
    share = both / len(pos)
    ok = share >= MIN_BOTH_VALID_SHARE
    return {**out, "ok": bool(ok), "dates_in_range": len(pos), "dates_both_valid": both,
            "both_valid_share": round(float(share), 4),
            "reason": None if ok else "valid 16:00 NY BTC quote at both points on < 90% of dates"}


def decide_b64(res: dict) -> str:
    """B64 rule: < 500 tested dates -> NONE; else `tsmom.decide_b16`."""
    if res.get("n", 0) < MIN_EVENTS:
        return "NONE"
    return decide_b16(res)
