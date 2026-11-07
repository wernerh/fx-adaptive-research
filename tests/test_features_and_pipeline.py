import numpy as np
import pandas as pd
import pytest

from fxresearch.backtest import CostModel, simulate
from fxresearch.data import synthetic_bars, quality_report
from fxresearch.features import daily_features, signal_inputs
from fxresearch.metrics import trade_metrics, wilson_interval
from fxresearch.predictive import run_baseline
from fxresearch.splits import SplitPlan
from fxresearch.strategies import REGISTRY
from datetime import date


@pytest.fixture(scope="module")
def bars():
    return synthetic_bars("2024-01-01", "2024-04-30")


@pytest.fixture(scope="module")
def feats(bars):
    return daily_features(bars)


def test_signal_inputs_exclude_outcomes(feats):
    cols = signal_inputs(feats).columns
    assert not any(c.startswith("y_") for c in cols)
    assert not any(c.startswith("day_") for c in cols)  # full-day stats include the US session


def test_atr_uses_prior_days_only(bars, feats):
    # Perturb the LAST day's prices; ATR for that day must not change.
    last = feats.index[-1]
    bumped = bars.copy()
    from fxresearch.sessions import trading_date
    mask = np.array(trading_date(bumped.index)) == last
    for c in [c for c in bumped.columns if c != "volume"]:
        bumped.loc[mask, c] = bumped.loc[mask, c] + np.linspace(0, 0.01, mask.sum())
    f2 = daily_features(bumped)
    assert f2.loc[last, "atr_pips_prior"] == pytest.approx(feats.loc[last, "atr_pips_prior"])
    assert f2.loc[last, "day_range_pips"] != pytest.approx(feats.loc[last, "day_range_pips"])


def test_london_features_unaffected_by_us_session(bars, feats):
    from fxresearch.sessions import label_sessions
    lab = label_sessions(bars.index)
    day = feats.index[-5]
    mask = (lab["us"] & (lab["trading_date"] == day)).to_numpy()
    assert mask.sum() > 0
    bumped = bars.copy()
    for c in [c for c in bumped.columns if c != "volume"]:
        bumped.loc[mask, c] += 0.005
    f2 = daily_features(bumped)
    # Every signal input for that day must be identical; the outcome must change.
    pd.testing.assert_series_equal(signal_inputs(f2).loc[day], signal_inputs(feats).loc[day])
    assert f2.loc[day, "y_us_high"] != pytest.approx(feats.loc[day, "y_us_high"])


def test_quality_report_runs(bars):
    q = quality_report(bars)
    assert q["crossed_quotes"] == 0 and q["missing_trading_minutes"] == 0


@pytest.mark.parametrize("name", sorted(REGISTRY))
def test_strategies_have_no_edge_on_random_walk(bars, feats, name):
    """A random walk has zero edge. After costs, expectancy should be <= ~0.
    A clearly positive result here means leakage or a simulator bug."""
    mod = REGISTRY[name]
    trades = simulate(bars, mod.generate_signals(bars, feats, mod.Params()), CostModel())
    assert len(trades) > 10
    m = trade_metrics(trades, trading_days=len(feats))
    assert m["t_stat"] is None or m["t_stat"] < 2.5


def test_signals_are_not_before_information_is_available(bars, feats):
    from fxresearch.sessions import US, LONDON
    mod = REGISTRY["london_us_continuation"]
    for s in mod.generate_signals(bars, feats, mod.Params()):
        d = pd.Timestamp(s.tag).date()
        assert s.time >= LONDON.window_utc(d)[1]


def test_baseline_runs_and_reports_blocks(feats):
    plan = SplitPlan(date(2024, 2, 15), date(2024, 3, 15), embargo_days=0)
    res = run_baseline(feats, plan.assign(feats.index))
    assert set(res["block"]) >= {"dev"}
    assert "binom_p_bonferroni" in res.columns


def test_wilson_interval():
    lo, hi = wilson_interval(50, 100)
    assert lo < 0.5 < hi and hi - lo == pytest.approx(0.19, abs=0.01)


def test_window_outcome_matches_manual(bars):
    from datetime import time
    from fxresearch.outcomes import window_outcome
    from fxresearch.data import mid, PIP
    w = window_outcome(bars, "America/New_York", time(8, 0), time(9, 0), "w")
    d = w.index[10]
    start = pd.Timestamp(f"{d} 08:00", tz="America/New_York").tz_convert("UTC")
    end = pd.Timestamp(f"{d} 09:00", tz="America/New_York").tz_convert("UTC")
    m = mid(bars)
    sub = m[(m.index >= start) & (m.index < end)]
    assert w.loc[d, "y_w_ret_pips"] == pytest.approx((sub["close"].iloc[-1] - sub["open"].iloc[0]) / PIP)
    assert w.loc[d, "y_w_bars"] == 60
