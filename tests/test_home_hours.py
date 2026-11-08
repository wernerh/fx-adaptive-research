from datetime import date

import pandas as pd
import pytest

from fxresearch.data import PIP, synthetic_bars
from fxresearch.fixes import decide
from fxresearch.home_hours import E017_LEGS, cost_summary, daily_frame, leg_frame
from fxresearch.predictive import evaluate_predictor


def test_e017_legs_fixed():
    assert [(l.name, l.start_hour, l.end_hour, l.direction) for l in E017_LEGS] == [("eu", 3, 8, -1), ("us", 12, 17, 1)]
    assert [l.min_bars for l in E017_LEGS] == [275, 275]


def test_leg_windows_on_ny_clock_and_same_trading_date():
    bars = synthetic_bars("2024-03-04", "2024-03-16")  # spans the 2024-03-10 US DST change
    for leg in E017_LEGS:
        f = leg_frame(bars, leg)
        assert (f["bars"] == 300).all()
        assert date(2024, 3, 6) in f.index and date(2024, 3, 12) in f.index
    # eu leg first bar 03:00 NY: 08:00 UTC before DST (EST), 07:00 UTC after (EDT)
    d = daily_frame(bars)
    assert len(d) >= 9


def test_signed_return_is_short_eu_plus_long_us():
    bars = synthetic_bars("2024-03-04", "2024-03-09")
    d = daily_frame(bars)
    eu = leg_frame(bars, E017_LEGS[0])["ret_pips"]
    us = leg_frame(bars, E017_LEGS[1])["ret_pips"]
    for td in d.index:
        assert abs(d.loc[td, "signed_pips"] - (-eu.loc[td] + us.loc[td])) < 1e-9


def test_eu_leg_return_matches_manual_mid():
    bars = synthetic_bars("2024-03-04", "2024-03-06")
    td = date(2024, 3, 5)
    ny = bars.index.tz_convert("America/New_York")
    w = bars[(ny.date == td) & (ny.hour >= 3) & (ny.hour < 8)]
    manual = ((w["bid_close"].iloc[-1] + w["ask_close"].iloc[-1]) / 2 - (w["bid_open"].iloc[0] + w["ask_open"].iloc[0]) / 2) / PIP
    assert abs(leg_frame(bars, E017_LEGS[0]).loc[td, "ret_pips"] - manual) < 1e-9


def test_net_is_mid_minus_two_spreads_and_costs():
    bars = synthetic_bars("2024-03-04", "2024-03-16", spread_pips_=0.3)
    d = daily_frame(bars)
    assert ((d["signed_pips"] - d["net_bidask_pips"]).round(6) == 0.6).all()  # 0.3 spread per leg
    c = cost_summary(d)
    assert abs(c["mean_signed_mid_pips"] - c["mean_net_spec4_pips"] - 1.0) < 2e-3  # 0.6 + 2 x 0.2


def test_coverage_drops_leg_with_gap():
    bars = synthetic_bars("2024-03-04", "2024-03-09")
    ny = bars.index.tz_convert("America/New_York")
    gap = (ny.date == date(2024, 3, 6)) & (ny.hour == 13)  # remove 60 of 300 us-leg bars
    d = daily_frame(bars[~gap])
    assert date(2024, 3, 6) not in d.index
    assert date(2024, 3, 5) in d.index


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk(seed):
    bars = synthetic_bars("2021-01-01", "2023-06-30", seed=seed)
    d = daily_frame(bars)
    res = evaluate_predictor(pd.Series(1.0, index=d.index), d["signed_pips"])
    assert decide(res, n_trials=1) != "SIGNAL"
