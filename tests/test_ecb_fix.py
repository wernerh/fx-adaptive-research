from datetime import date

import pandas as pd
import pytest

from fxresearch.data import synthetic_bars
from fxresearch.fixes import E010_TESTS, ECB_FIX_WINDOWS, run_fix_tests
from fxresearch.outcomes import window_outcome


def test_e010_tests_are_two_fixed_directions():
    assert [(t.window, t.direction, t.month_end_only) for t in E010_TESTS] == [
        ("ecb_fix_pre", -1, False), ("ecb_fix_post", +1, False)]


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk(seed):
    bars = synthetic_bars("2024-01-01", "2024-12-31", seed=seed)
    feats = pd.concat([window_outcome(bars, tz, s, e, n) for n, (tz, s, e) in ECB_FIX_WINDOWS.items()], axis=1)
    split = pd.Series("dev", index=feats.index)
    res = run_fix_tests(feats, split, E010_TESTS, blocks=("dev",))
    assert len(res) == 2
    assert not (res["decision"] == "SIGNAL").any()


def test_ecb_windows_use_berlin_clock():
    # 2024-07-01 is CEST (UTC+2): 13:15-14:15 Berlin = 11:15-12:15 UTC -> 60 bars, first bar 11:15 UTC.
    # 2024-01-15 is CET (UTC+1): 14:15-15:15 Berlin = 13:15-14:15 UTC.
    bars = synthetic_bars("2024-01-10", "2024-07-03")
    pre = window_outcome(bars, "Europe/Berlin", *ECB_FIX_WINDOWS["ecb_fix_pre"][1:], "p")
    post = window_outcome(bars, "Europe/Berlin", *ECB_FIX_WINDOWS["ecb_fix_post"][1:], "q")
    assert pre.loc[date(2024, 7, 1), "y_p_bars"] == 60
    assert post.loc[date(2024, 1, 15), "y_q_bars"] == 60
    t = bars.index
    first = t[(t >= pd.Timestamp("2024-07-01 11:15", tz="UTC"))][0]
    assert first == pd.Timestamp("2024-07-01 11:15", tz="UTC")
