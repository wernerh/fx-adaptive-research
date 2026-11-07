import numpy as np
import pandas as pd
import pytest

from fxresearch.backtest import CostModel, Signal, simulate
from fxresearch.data import PIP

NO_COST = CostModel(slippage_pips=0, commission_pips=0, max_spread_pips=5)


def make_bars(mids, spread_pips=0.2, highs=None, lows=None, start="2024-01-16 13:00"):
    idx = pd.date_range(start, periods=len(mids), freq="1min", tz="UTC")
    mids = np.asarray(mids, float)
    opens = np.concatenate([[mids[0]], mids[:-1]])
    hi = np.maximum(opens, mids) if highs is None else np.asarray(highs, float)
    lo = np.minimum(opens, mids) if lows is None else np.asarray(lows, float)
    h = spread_pips * PIP / 2
    df = pd.DataFrame(index=idx)
    for f, v in zip(("open", "high", "low", "close"), (opens, hi, lo, mids)):
        df[f"bid_{f}"] = v - h
        df[f"ask_{f}"] = v + h
    return df


def sig(bars, side=1, stop=5, target=5, hold=60, i=1):
    return Signal(time=bars.index[i], side=side, stop_pips=stop, target_pips=target,
                  max_hold_minutes=hold, strategy="t")


def test_long_target_hit_pays_the_spread():
    base = 1.1000
    bars = make_bars([base] * 2 + [base + 10 * PIP] * 3, spread_pips=0.2)
    t = simulate(bars, [sig(bars)], NO_COST)
    assert t.iloc[0]["exit_reason"] == "target"
    # entered at ask (base + 0.1 pip), exit target is +5 pips from entry
    assert t.iloc[0]["net_pips"] == pytest.approx(5.0)
    assert t.iloc[0]["entry_price"] == pytest.approx(base + 0.1 * PIP)


def test_long_exits_evaluated_on_bid_so_spread_alone_can_stop_you():
    base = 1.1000
    # Mid never moves but spread is 3 pips: bid sits 1.5 pips under mid, entry 1.5 above.
    bars = make_bars([base] * 6, spread_pips=3.0)
    t = simulate(bars, [sig(bars, stop=2.5, target=10, hold=3)], NO_COST)
    assert t.iloc[0]["exit_reason"] == "stop"
    assert t.iloc[0]["net_pips"] == pytest.approx(-2.5)


def test_stop_assumed_first_when_both_hit_in_one_bar():
    base = 1.1000
    mids = [base, base, base, base]
    highs = [base, base, base + 20 * PIP, base]
    lows = [base, base, base - 20 * PIP, base]
    bars = make_bars(mids, spread_pips=0.0, highs=highs, lows=lows)
    t = simulate(bars, [sig(bars, stop=5, target=5)], NO_COST)
    assert t.iloc[0]["exit_reason"] == "stop"


def test_short_symmetry():
    base = 1.1000
    bars = make_bars([base] * 2 + [base - 10 * PIP] * 3, spread_pips=0.2)
    t = simulate(bars, [sig(bars, side=-1)], NO_COST)
    assert t.iloc[0]["exit_reason"] == "target"
    assert t.iloc[0]["net_pips"] == pytest.approx(5.0)


def test_time_stop_and_hold_minutes():
    base = 1.1000
    bars = make_bars([base] * 30, spread_pips=0.0)
    t = simulate(bars, [sig(bars, stop=50, target=50, hold=10)], NO_COST)
    assert t.iloc[0]["exit_reason"] == "time"
    assert t.iloc[0]["hold_minutes"] == pytest.approx(10)


def test_gap_through_stop_fills_at_worse_open():
    base = 1.1000
    mids = [base, base, base, base - 20 * PIP, base - 20 * PIP]
    bars = make_bars(mids, spread_pips=0.0)
    # bar 3 opens at the previous close (base) in make_bars, so construct an explicit gap:
    bars.iloc[3, bars.columns.get_loc("bid_open")] = base - 15 * PIP
    bars.iloc[3, bars.columns.get_loc("ask_open")] = base - 15 * PIP
    t = simulate(bars, [sig(bars, stop=5, target=50)], NO_COST)
    assert t.iloc[0]["net_pips"] == pytest.approx(-15)


def test_costs_reduce_net():
    base = 1.1000
    bars = make_bars([base] * 2 + [base + 10 * PIP] * 3, spread_pips=0.2)
    t = simulate(bars, [sig(bars)], CostModel(slippage_pips=0.2, commission_pips=0.1))
    assert t.iloc[0]["net_pips"] == pytest.approx(5.0 - 0.1)  # target from slipped entry, minus commission
    assert t.iloc[0]["entry_price"] == pytest.approx(base + 0.1 * PIP + 0.2 * PIP)


def test_wide_spread_skips_entry():
    bars = make_bars([1.1] * 5, spread_pips=3.0)
    t = simulate(bars, [sig(bars)], CostModel(max_spread_pips=2.0))
    assert t.empty


def test_no_overlapping_positions():
    bars = make_bars([1.1] * 40, spread_pips=0.0)
    s1 = sig(bars, stop=50, target=50, hold=20, i=1)
    s2 = sig(bars, stop=50, target=50, hold=20, i=5)
    t = simulate(bars, [s1, s2], NO_COST)
    assert len(t) == 1
