from datetime import date

import pandas as pd
import pytest

from fxresearch.data import synthetic_bars
from fxresearch.hourly_profile import N_CELLS, decide, hourly_returns, scan


def _all_dev(dates):
    return pd.Series("dev", index=dates)


def test_decide_rule():
    base = {"n": 1500, "mean_pips": 1.2, "ci_lo": 0.6, "ci_hi": 1.8, "t_p": 1e-5, "sign_p": 0.01}
    assert decide(base) == "CANDIDATE"
    assert decide({**base, "mean_pips": -1.2, "ci_lo": -1.8, "ci_hi": -0.6}) == "CANDIDATE"
    assert decide({**base, "t_p": 0.001}) == "NOTE"          # not < 0.05/192
    assert decide({**base, "mean_pips": 0.9}) == "NONE"       # below 1 pip
    assert decide({**base, "sign_p": 0.2}) == "NOTE"          # direction not consistent
    assert decide({**base, "ci_lo": -0.1}) == "NOTE"          # CI includes 0
    assert decide({**base, "n": 20}) == "NONE"


def test_hour_buckets_complete_and_ny_clock():
    bars = synthetic_bars("2024-07-01", "2024-07-06")
    hr = hourly_returns(bars)
    ny = hr[hr["clock"] == "ny"]
    assert (hr["bars"] == 60).all()
    # Trading date 2024-07-02 (17:00 NY roll) holds all 24 NY hours.
    assert sorted(ny.loc[ny["date"] == date(2024, 7, 2), "hour"]) == list(range(24))


@pytest.mark.parametrize("seed", [1, 2])
def test_no_candidates_on_random_walk(seed):
    bars = synthetic_bars("2023-01-01", "2024-12-31", seed=seed)
    res = scan(hourly_returns(bars), _all_dev)
    assert len(res) == N_CELLS
    assert not (res["decision"] == "CANDIDATE").any()
