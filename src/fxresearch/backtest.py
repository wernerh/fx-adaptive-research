"""Bar-based trade simulator on 1-minute bid/ask data.

Fill rules (conservative by design; see docs/SPEC.md section 4):

* A signal stamped at time t is filled at the OPEN of the first bar with ts >= t.
  Longs buy at ask, shorts sell at bid, plus `slippage_pips` against the trader.
* Long exits are evaluated on BID prices, short exits on ASK prices.
* Stop and target are checked from the bar AFTER the entry bar's open, using the
  entry bar's own high/low as well (price can move after the open).
* If stop and target are both touched inside one bar, the STOP is assumed first.
* Stops fill at the stop price minus slippage (gaps fill at the bar open if worse).
* If neither is hit by `max_hold_minutes`, exit at the open of the bar at the time
  limit (time stop). A hard session cut-off may also be supplied.
* Commission is charged per round trip in pips.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np
import pandas as pd

from .data import PIP


@dataclass(frozen=True)
class Signal:
    time: pd.Timestamp          # earliest time the order may be filled (UTC)
    side: int                   # +1 long, -1 short
    stop_pips: float            # distance from fill price
    target_pips: float | None   # None = no target, exit by time
    max_hold_minutes: int
    strategy: str
    cutoff: pd.Timestamp | None = None  # force exit at/after this time
    tag: str = ""


@dataclass(frozen=True)
class CostModel:
    slippage_pips: float = 0.1       # per side, applied to entry and stop exits
    commission_pips: float = 0.1     # per round trip (approx. $5 per $1m per side, ECN)
    max_spread_pips: float = 2.0     # skip entries if spread at entry is wider


@dataclass
class Trade:
    strategy: str
    tag: str
    side: int
    signal_time: pd.Timestamp
    entry_time: pd.Timestamp
    entry_price: float
    exit_time: pd.Timestamp
    exit_price: float
    exit_reason: str
    stop_pips: float
    target_pips: float | None
    spread_at_entry_pips: float
    gross_pips: float
    net_pips: float
    r_multiple: float
    hold_minutes: float
    mae_pips: float
    mfe_pips: float


def _arrays(bars: pd.DataFrame):
    return {c: bars[c].to_numpy() for c in bars.columns if c.startswith(("bid_", "ask_"))}


def simulate(bars: pd.DataFrame, signals: list[Signal], costs: CostModel = CostModel()) -> pd.DataFrame:
    """Simulate signals one at a time. Overlapping positions are NOT allowed:
    a signal whose fill time falls inside an open trade is skipped."""
    a = _arrays(bars)
    idx = bars.index
    trades: list[Trade] = []
    busy_until = None
    for sig in sorted(signals, key=lambda s: s.time):
        i = idx.searchsorted(sig.time, side="left")
        if i >= len(idx):
            continue
        if busy_until is not None and idx[i] < busy_until:
            continue
        spread = (a["ask_open"][i] - a["bid_open"][i]) / PIP
        if spread > costs.max_spread_pips:
            continue
        t = _run_trade(sig, i, idx, a, costs, spread)
        if t is not None:
            trades.append(t)
            busy_until = t.exit_time
    df = pd.DataFrame([asdict(t) for t in trades])
    return df


def _run_trade(sig, i, idx, a, costs, spread):
    slip = costs.slippage_pips * PIP
    side = sig.side
    if side == 1:
        entry = a["ask_open"][i] + slip
        ex_hi, ex_lo, ex_open = a["bid_high"], a["bid_low"], a["bid_open"]
    else:
        entry = a["bid_open"][i] - slip
        ex_hi, ex_lo, ex_open = a["ask_high"], a["ask_low"], a["ask_open"]
    stop = entry - side * sig.stop_pips * PIP
    target = None if sig.target_pips is None else entry + side * sig.target_pips * PIP
    limit_time = idx[i] + pd.Timedelta(minutes=sig.max_hold_minutes)
    if sig.cutoff is not None:
        limit_time = min(limit_time, sig.cutoff)

    mae = mfe = 0.0
    exit_price = exit_time = reason = None
    j = i
    while j < len(idx):
        if idx[j] >= limit_time and j > i:
            exit_price, exit_time, reason = ex_open[j], idx[j], "time"
            break
        hi, lo, op = ex_hi[j], ex_lo[j], ex_open[j]
        fav = (hi - entry) if side == 1 else (entry - lo)
        adv = (entry - lo) if side == 1 else (hi - entry)
        mfe, mae = max(mfe, fav / PIP), max(mae, adv / PIP)
        stop_hit = (lo <= stop) if side == 1 else (hi >= stop)
        tgt_hit = target is not None and ((hi >= target) if side == 1 else (lo <= target))
        if stop_hit:  # stop takes precedence when both are touched in one bar
            gap_worse = (op < stop) if side == 1 else (op > stop)
            base = op if (gap_worse and j > i) else stop
            exit_price, exit_time, reason = base - side * slip, idx[j], "stop"
            break
        if tgt_hit:
            exit_price, exit_time, reason = target, idx[j], "target"
            break
        j += 1
    if exit_price is None:
        return None  # ran out of data; trade discarded and should be reported

    gross = side * (exit_price - entry) / PIP
    net = gross - costs.commission_pips
    hold = (exit_time - idx[i]).total_seconds() / 60 + (1 if reason != "time" else 0)
    return Trade(
        strategy=sig.strategy, tag=sig.tag, side=side, signal_time=sig.time,
        entry_time=idx[i], entry_price=entry, exit_time=exit_time, exit_price=exit_price,
        exit_reason=reason, stop_pips=sig.stop_pips, target_pips=sig.target_pips,
        spread_at_entry_pips=spread, gross_pips=gross, net_pips=net,
        r_multiple=net / sig.stop_pips, hold_minutes=hold, mae_pips=mae, mfe_pips=mfe,
    )
