from datetime import date

import pandas as pd
import pytest

from fxresearch.data import synthetic_bars
from fxresearch.fixes import E011_TESTS, TOKYO_FIX_WINDOWS, run_fix_tests, window_bidask_net
from fxresearch.outcomes import window_outcome


def test_e011_tests_are_two_fixed_directions():
    assert [(t.window, t.direction, t.month_end_only) for t in E011_TESTS] == [
        ("tky_fix_pre", -1, False), ("tky_fix_post", +1, False)]


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk(seed):
    bars = synthetic_bars("2024-01-01", "2024-12-31", seed=seed)
    feats = pd.concat([window_outcome(bars, tz, s, e, n) for n, (tz, s, e) in TOKYO_FIX_WINDOWS.items()], axis=1)
    split = pd.Series("dev", index=feats.index)
    res = run_fix_tests(feats, split, E011_TESTS, blocks=("dev",))
    assert len(res) == 2
    assert not (res["decision"] == "SIGNAL").any()


def test_tokyo_windows_cross_utc_midnight_within_one_trading_date():
    # 08:55-09:55 JST on 2024-03-06 = 2024-03-05 23:55 .. 2024-03-06 00:55 UTC; trading date 2024-03-06.
    bars = synthetic_bars("2024-03-01", "2024-03-10")
    pre = window_outcome(bars, "Asia/Tokyo", *TOKYO_FIX_WINDOWS["tky_fix_pre"][1:], "p")
    post = window_outcome(bars, "Asia/Tokyo", *TOKYO_FIX_WINDOWS["tky_fix_post"][1:], "q")
    assert pre.loc[date(2024, 3, 6), "y_p_bars"] == 60
    assert post.loc[date(2024, 3, 6), "y_q_bars"] == 60


def test_bidask_net_is_mid_minus_spread_on_constant_spread():
    bars = synthetic_bars("2024-03-01", "2024-03-10", spread_pips_=0.3)
    tz, s, e = TOKYO_FIX_WINDOWS["tky_fix_post"]
    mid_ret = window_outcome(bars, tz, s, e, "w")["y_w_ret_pips"]
    nb = window_bidask_net(bars, tz, s, e, +1, "w")
    diff = (mid_ret - nb["w_net_pips"]).dropna()
    assert len(diff) > 0
    assert diff.round(6).eq(0.3).all()
    nbs = window_bidask_net(bars, tz, s, e, -1, "w")
    assert ((-mid_ret - nbs["w_net_pips"]).dropna().round(6) == 0.3).all()
