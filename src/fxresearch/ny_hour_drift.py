"""E012 (backlog B9/B10): NY-clock hour drift on given trading-date weekdays, val confirmation of E009 candidates.

Per FX trading date (17:00 New York roll) and one America/New_York clock hour:
  ret_pips          mid close of last bar minus mid open of first bar (identical to E009 `hourly_returns`)
  net_bidask_pips   long trade: buy ask open of first bar, sell bid close of last bar
  entry_spread_pips ask_open - bid_open of first bar
Hours with fewer than 55 of 60 bars are dropped (E009 rule). Calendar-only, so nothing can look ahead.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .data import PIP
from .sessions import NY, trading_date

MIN_BARS = 55
# SPEC 4 defaults for a timed exit: 0.1 pip slippage on entry + 0.1 pip commission per round trip.
SLIPPAGE_ENTRY_PIPS = 0.1
COMMISSION_RT_PIPS = 0.1


@dataclass(frozen=True)
class HourTest:
    name: str
    weekday: int    # trading-date weekday, Mon=0
    ny_hour: int
    direction: int  # +1 long EUR/USD


E012_TESTS = (
    HourTest("wed_ny18_long", 2, 18, +1),
    HourTest("thu_ny18_long", 3, 18, +1),
)


def ny_hour_frame(bars: pd.DataFrame, ny_hour: int) -> pd.DataFrame:
    """One row per trading date for the given NY clock hour (only hours with >= MIN_BARS bars)."""
    idx = bars.index
    td = pd.Index(trading_date(idx))
    h = np.asarray(idx.tz_convert(NY).hour)
    sel = h == ny_hour
    b = bars[sel]
    g = b.groupby(td[sel])
    first, last = g.first(), g.last()
    n = g.size()
    mid_open = (first["bid_open"] + first["ask_open"]) / 2
    mid_close = (last["bid_close"] + last["ask_close"]) / 2
    out = pd.DataFrame({
        "ret_pips": (mid_close - mid_open) / PIP,
        "net_bidask_pips": (last["bid_close"] - first["ask_open"]) / PIP,
        "entry_spread_pips": (first["ask_open"] - first["bid_open"]) / PIP,
        "bars": n,
    })
    out.index.name = "trading_date"
    out = out[out["bars"] >= MIN_BARS]
    out["weekday"] = pd.to_datetime(pd.Index(out.index)).dayofweek
    return out


def cost_summary(df: pd.DataFrame, direction: int = +1) -> dict:
    """Descriptive cost check (long only implemented; E012 tests are long)."""
    assert direction == +1
    gross = df["ret_pips"]
    net_ba = df["net_bidask_pips"]
    net_spec = net_ba - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    cost = gross - net_spec
    return {
        "n": int(len(df)),
        "mean_signed_mid_pips": round(float(gross.mean()), 3),
        "median_entry_spread_pips": round(float(df["entry_spread_pips"].median()), 3),
        "mean_net_bidask_pips": round(float(net_ba.mean()), 3),
        "mean_net_spec4_pips": round(float(net_spec.mean()), 3),
        "mean_net_costs_x1_5_pips": round(float((gross - 1.5 * cost).mean()), 3),
        "net_spec4_hit_rate": round(float((net_spec > 0).mean()), 4) if len(df) else None,
    }
