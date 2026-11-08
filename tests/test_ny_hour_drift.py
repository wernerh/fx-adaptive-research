from datetime import date

import pandas as pd
import pytest

from fxresearch.data import synthetic_bars
from fxresearch.fixes import decide
from fxresearch.hourly_profile import hourly_returns
from fxresearch.ny_hour_drift import E012_TESTS, cost_summary, ny_hour_frame
from fxresearch.predictive import evaluate_predictor


def test_e012_tests_fixed():
    assert [(t.weekday, t.ny_hour, t.direction) for t in E012_TESTS] == [(2, 18, 1), (3, 18, 1)]


def test_ret_matches_e009_definition():
    bars = synthetic_bars("2024-03-01", "2024-03-20")
    f = ny_hour_frame(bars, 18)
    hr = hourly_returns(bars)
    e9 = hr[(hr["clock"] == "ny") & (hr["hour"] == 18)].set_index("date")["ret_pips"]
    common = f.index.intersection(e9.index)
    assert len(common) >= 10
    assert (f.loc[common, "ret_pips"] - e9.loc[common]).abs().max() < 1e-9


def test_trading_date_mapping_after_roll():
    # 18:00 NY on Tuesday 2024-03-05 (calendar) belongs to trading date Wednesday 2024-03-06.
    bars = synthetic_bars("2024-03-01", "2024-03-10")
    f = ny_hour_frame(bars, 18)
    assert date(2024, 3, 6) in f.index
    assert f.loc[date(2024, 3, 6), "weekday"] == 2
    assert f.loc[date(2024, 3, 6), "bars"] == 60


def test_net_is_mid_minus_spread_on_constant_spread():
    bars = synthetic_bars("2024-03-01", "2024-03-10", spread_pips_=0.3)
    f = ny_hour_frame(bars, 18)
    assert ((f["ret_pips"] - f["net_bidask_pips"]).round(6) == 0.3).all()
    c = cost_summary(f)
    assert abs(c["mean_signed_mid_pips"] - c["mean_net_spec4_pips"] - 0.5) < 2e-3  # 0.3 spread + 0.2 slip/comm


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk(seed):
    bars = synthetic_bars("2022-01-01", "2023-12-31", seed=seed)
    f = ny_hour_frame(bars, 18)
    for t in E012_TESTS:
        d = f[f["weekday"] == t.weekday]
        res = evaluate_predictor(pd.Series(float(t.direction), index=d.index), d["ret_pips"])
        assert decide(res, n_trials=1) != "SIGNAL"
