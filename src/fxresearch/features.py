"""Per-trading-day session features.

Look-ahead rule: every feature a strategy may use at time t is computed only from
bars with open time < t. Day-level ATR uses PRIOR trading days only (shift(1)).
Outcome columns (prefixed `y_`) describe the US session and must NEVER be used as
inputs to a signal. tests/test_features.py enforces both rules.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .data import PIP, mid
from .sessions import DEFAULT_SESSIONS, label_sessions

ATR_DAYS = 14


def _session_stats(m: pd.DataFrame, mask: pd.Series, dates: pd.Series, name: str) -> pd.DataFrame:
    sub = m[mask.to_numpy()]
    g = sub.groupby(dates[mask].to_numpy())
    stats = pd.DataFrame({
        f"{name}_open": g["open"].first(),
        f"{name}_high": g["high"].max(),
        f"{name}_low": g["low"].min(),
        f"{name}_close": g["close"].last(),
        f"{name}_bars": g["close"].size(),
    })
    stats[f"{name}_range_pips"] = (stats[f"{name}_high"] - stats[f"{name}_low"]) / PIP
    stats[f"{name}_ret_pips"] = (stats[f"{name}_close"] - stats[f"{name}_open"]) / PIP
    # Where the close sits within the range: 0 = at low, 1 = at high.
    rng = (stats[f"{name}_high"] - stats[f"{name}_low"]).replace(0, np.nan)
    stats[f"{name}_close_loc"] = (stats[f"{name}_close"] - stats[f"{name}_low"]) / rng
    return stats


def _london_breakout(m: pd.DataFrame, lab: pd.DataFrame, feats: pd.DataFrame) -> pd.DataFrame:
    """First side of the Asian range that London breaks, and whether London closes back inside."""
    rows = {}
    lon = m[lab["london"].to_numpy()]
    dates = lab.loc[lab["london"], "trading_date"]
    for d, bars in lon.groupby(dates.to_numpy()):
        if d not in feats.index or pd.isna(feats.at[d, "asia_high"]):
            continue
        ah, al = feats.at[d, "asia_high"], feats.at[d, "asia_low"]
        up = bars.index[bars["high"] > ah]
        dn = bars.index[bars["low"] < al]
        first_up = up[0] if len(up) else None
        first_dn = dn[0] if len(dn) else None
        if first_up is None and first_dn is None:
            side = 0
        elif first_dn is None or (first_up is not None and first_up <= first_dn):
            side = 1
        else:
            side = -1
        close = bars["close"].iloc[-1]
        inside = al <= close <= ah
        rows[d] = {
            "lon_break_side": side,               # +1 broke high first, -1 low first, 0 none
            "lon_broke_both": int(len(up) > 0 and len(dn) > 0),
            "lon_closed_inside_asia": int(side != 0 and inside),  # false-breakout proxy
            "lon_break_time": first_up if side == 1 else (first_dn if side == -1 else pd.NaT),
        }
    cols = ["lon_break_side", "lon_broke_both", "lon_closed_inside_asia", "lon_break_time"]
    if not rows:  # keep the schema stable even when no day qualifies
        return pd.DataFrame(columns=cols)
    return pd.DataFrame.from_dict(rows, orient="index")[cols]


def daily_features(bars: pd.DataFrame, sessions=DEFAULT_SESSIONS) -> pd.DataFrame:
    m = mid(bars)
    lab = label_sessions(bars.index, sessions)
    dates = lab["trading_date"]

    day = m.groupby(dates.to_numpy()).agg(
        day_high=("high", "max"), day_low=("low", "min"),
        day_open=("open", "first"), day_close=("close", "last"),
    )
    day["day_range_pips"] = (day["day_high"] - day["day_low"]) / PIP
    # ATR proxy from PRIOR days only. No look-ahead.
    day["atr_pips_prior"] = day["day_range_pips"].rolling(ATR_DAYS, min_periods=ATR_DAYS).mean().shift(1)
    day["prev_day_high"] = day["day_high"].shift(1)
    day["prev_day_low"] = day["day_low"].shift(1)

    feats = day
    for s in sessions:
        feats = feats.join(_session_stats(m, lab[s.name], dates, s.name), how="left")

    feats["asia_range_atr"] = feats["asia_range_pips"] / feats["atr_pips_prior"]
    feats["london_range_atr"] = feats["london_range_pips"] / feats["atr_pips_prior"]
    feats = feats.join(_london_breakout(m, lab, feats), how="left")

    # ---- Outcomes (US session). Never use as signal inputs. ----
    feats["y_us_ret_pips"] = feats.pop("us_ret_pips")
    feats["y_us_dir"] = np.sign(feats["y_us_ret_pips"])
    for c in ("us_open", "us_high", "us_low", "us_close", "us_range_pips", "us_close_loc", "us_bars"):
        feats[f"y_{c}"] = feats.pop(c)
    feats.index.name = "trading_date"
    return feats


SIGNAL_SAFE_PREFIXES = ("asia_", "london_", "lon_", "atr_", "prev_day_")


def signal_inputs(feats: pd.DataFrame) -> pd.DataFrame:
    """Columns a pre-US-session signal is allowed to use."""
    cols = [c for c in feats.columns if c.startswith(SIGNAL_SAFE_PREFIXES)]
    return feats[cols]
