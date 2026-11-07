"""S001 Asian range breakout (status: research candidate).

Hypothesis: the first decisive London break of the Asian range reflects informed
European order flow and continues for a short period.

Entry : first 1-minute mid close outside the Asian range during London, entered at
        the next bar open in the break direction.
Filters: Asian range between min_range_atr and max_range_atr of prior ATR.
Stop  : opposite side of the Asian range, capped at max_stop_pips; or stop_atr * ATR.
Target: target_r * stop distance.
Time  : max_hold_minutes, and never beyond the London session end.
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from ..backtest import Signal
from ..data import PIP, mid
from ..sessions import LONDON, label_sessions


@dataclass(frozen=True)
class Params:
    min_range_atr: float = 0.15
    max_range_atr: float = 0.60
    stop_mode: str = "range"        # "range" or "atr"
    stop_atr: float = 0.25
    max_stop_pips: float = 25.0
    target_r: float = 1.0
    max_hold_minutes: int = 60


def generate_signals(bars: pd.DataFrame, feats: pd.DataFrame, p: Params = Params()) -> list[Signal]:
    m = mid(bars)
    lab = label_sessions(bars.index)
    out: list[Signal] = []
    lon = m[lab["london"].to_numpy()]
    lon_dates = lab.loc[lab["london"], "trading_date"].to_numpy()
    for d, day_bars in lon.groupby(lon_dates):
        if d not in feats.index:
            continue
        f = feats.loc[d]
        if pd.isna(f.get("asia_range_atr")) or not (p.min_range_atr <= f["asia_range_atr"] <= p.max_range_atr):
            continue
        ah, al = f["asia_high"], f["asia_low"]
        up = day_bars.index[day_bars["close"] > ah]
        dn = day_bars.index[day_bars["close"] < al]
        first = min([x for x in (up[0] if len(up) else None, dn[0] if len(dn) else None) if x is not None],
                    default=None)
        if first is None:
            continue
        side = 1 if (len(up) and first == up[0]) else -1
        if p.stop_mode == "range":
            stop = (ah - al) / PIP
        else:
            stop = p.stop_atr * f["atr_pips_prior"]
        stop = min(stop, p.max_stop_pips)
        _, lon_end = LONDON.window_utc(d)
        out.append(Signal(
            time=first + pd.Timedelta(minutes=1),   # bar `first` closes 1 minute after its open
            side=side, stop_pips=float(stop), target_pips=float(stop * p.target_r),
            max_hold_minutes=p.max_hold_minutes, strategy="asian_range_breakout",
            cutoff=lon_end, tag=str(d),
        ))
    return out
