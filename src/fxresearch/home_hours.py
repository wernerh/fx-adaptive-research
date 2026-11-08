"""E017 (backlog B14): home-hours depreciation (Breedon & Ranaldo 2013 mechanism), val only.

Per FX trading date (17:00 New York roll, `sessions.trading_date`), two fixed America/New_York clock windows:
  eu leg  03:00-08:00 NY (European-only hours): predicted EUR/USD down -> short
  us leg  12:00-17:00 NY (US-only hours):       predicted EUR/USD up   -> long
Daily signed return = -(eu mid return) + (us mid return), only on dates where BOTH legs pass coverage.
Window mid return = mid close of last bar minus mid open of first bar (pips). A leg needs >= 275 of 300 bars
(the E009/E012 55-of-60 share). Windows are calendar-only, so nothing can look ahead.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .data import PIP
from .sessions import NY, trading_date

# SPEC 4 defaults for a timed exit: 0.1 pip slippage on entry + 0.1 pip commission per round trip, per leg.
SLIPPAGE_ENTRY_PIPS = 0.1
COMMISSION_RT_PIPS = 0.1
MAX_ENTRY_SPREAD_PIPS = 2.0  # SPEC 4; reported descriptively only (share of entries wider)


@dataclass(frozen=True)
class Leg:
    name: str
    start_hour: int  # NY clock, inclusive
    end_hour: int    # NY clock, exclusive
    direction: int   # +1 long EUR/USD, -1 short

    @property
    def min_bars(self) -> int:
        return int(np.ceil((self.end_hour - self.start_hour) * 60 * 55 / 60))


E017_LEGS = (
    Leg("eu", 3, 8, -1),
    Leg("us", 12, 17, +1),
)


def leg_frame(bars: pd.DataFrame, leg: Leg) -> pd.DataFrame:
    """One row per trading date for one leg (only dates with >= leg.min_bars bars)."""
    idx = bars.index
    td = pd.Index(trading_date(idx))
    h = np.asarray(idx.tz_convert(NY).hour)
    sel = (h >= leg.start_hour) & (h < leg.end_hour)
    b = bars[sel]
    g = b.groupby(td[sel])
    first, last = g.first(), g.last()
    mid_open = (first["bid_open"] + first["ask_open"]) / 2
    mid_close = (last["bid_close"] + last["ask_close"]) / 2
    if leg.direction > 0:
        net_ba = last["bid_close"] - first["ask_open"]
    else:
        net_ba = first["bid_open"] - last["ask_close"]
    out = pd.DataFrame({
        "ret_pips": (mid_close - mid_open) / PIP,
        "signed_pips": leg.direction * (mid_close - mid_open) / PIP,
        "net_bidask_pips": net_ba / PIP,
        "entry_spread_pips": (first["ask_open"] - first["bid_open"]) / PIP,
        "exit_spread_pips": (last["ask_close"] - last["bid_close"]) / PIP,
        "bars": g.size(),
    })
    out.index.name = "trading_date"
    return out[out["bars"] >= leg.min_bars]


def daily_frame(bars: pd.DataFrame, legs=E017_LEGS) -> pd.DataFrame:
    """Join legs on trading date (inner join: both legs required). Adds `signed_pips` = sum of signed legs."""
    parts = {leg.name: leg_frame(bars, leg) for leg in legs}
    df = pd.concat({k: v for k, v in parts.items()}, axis=1, join="inner")
    df.columns = [f"{a}_{b}" for a, b in df.columns]
    df["signed_pips"] = sum(df[f"{leg.name}_signed_pips"] for leg in legs)
    df["net_bidask_pips"] = sum(df[f"{leg.name}_net_bidask_pips"] for leg in legs)
    df.index.name = "trading_date"
    return df


def cost_summary(df: pd.DataFrame, legs=E017_LEGS) -> dict:
    """Descriptive cost check of the two-leg daily trade (gates only the candidate label)."""
    gross = df["signed_pips"]
    net_ba = df["net_bidask_pips"]
    net_spec = net_ba - len(legs) * (SLIPPAGE_ENTRY_PIPS + COMMISSION_RT_PIPS)
    cost = gross - net_spec
    out = {
        "n": int(len(df)),
        "mean_signed_mid_pips": round(float(gross.mean()), 3),
        "mean_net_bidask_pips": round(float(net_ba.mean()), 3),
        "mean_net_spec4_pips": round(float(net_spec.mean()), 3),
        "mean_net_costs_x1_5_pips": round(float((gross - 1.5 * cost).mean()), 3),
        "net_spec4_hit_rate": round(float((net_spec > 0).mean()), 4) if len(df) else None,
    }
    for leg in legs:
        out[f"{leg.name}_mean_signed_mid_pips"] = round(float(df[f"{leg.name}_signed_pips"].mean()), 3)
        out[f"{leg.name}_median_entry_spread_pips"] = round(float(df[f"{leg.name}_entry_spread_pips"].median()), 3)
        out[f"{leg.name}_median_exit_spread_pips"] = round(float(df[f"{leg.name}_exit_spread_pips"].median()), 3)
        out[f"{leg.name}_share_entry_spread_gt_2"] = round(
            float((df[f"{leg.name}_entry_spread_pips"] > MAX_ENTRY_SPREAD_PIPS).mean()), 4)
    return out
