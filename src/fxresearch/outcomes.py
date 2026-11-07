"""Outcome windows other than the default US session (used by E006 and later).

An outcome window is any local-clock interval, e.g. 08:00-09:00 New York. The return is
mid close of the last bar before `end` minus mid open of the first bar at/after `start`,
in pips, per trading date. Outcomes are never signal inputs.
"""
from __future__ import annotations

from datetime import time

import pandas as pd

from .data import PIP, mid
from .sessions import Session, label_sessions


def window_outcome(bars: pd.DataFrame, tz: str, start: time, end: time, name: str) -> pd.DataFrame:
    s = Session(name, tz, start, end)
    lab = label_sessions(bars.index, (s,))
    m = mid(bars)[lab[name].to_numpy()]
    g = m.groupby(lab.loc[lab[name], "trading_date"].to_numpy())
    out = pd.DataFrame({
        f"y_{name}_ret_pips": (g["close"].last() - g["open"].first()) / PIP,
        f"y_{name}_bars": g["close"].size(),
    })
    out.index.name = "trading_date"
    return out
