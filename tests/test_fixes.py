from datetime import date

import pandas as pd
import pytest

from fxresearch.data import synthetic_bars
from fxresearch.fixes import E007_TESTS, LONDON_FIX_WINDOWS, decide, month_end_flag, run_fix_tests
from fxresearch.outcomes import window_outcome
from fxresearch.splits import SplitPlan


def test_month_end_flag_picks_last_trading_date():
    d = pd.Index([date(2024, 1, 30), date(2024, 1, 31), date(2024, 2, 1), date(2024, 2, 28), date(2024, 2, 29)])
    assert month_end_flag(d).tolist() == [False, True, False, False, True]


def test_decide_rule():
    base = {"mean_signed_pips": 1.5, "mean_signed_ci95_block_boot": (0.4, 2.6), "binom_p": 0.001}
    assert decide(base, 4) == "SIGNAL"
    assert decide({**base, "binom_p": 0.02}, 4) == "WEAK"            # p not < 0.05/4
    assert decide({**base, "mean_signed_pips": 0.8}, 4) == "WEAK"    # below 1 pip
    assert decide({**base, "mean_signed_pips": -1.5, "mean_signed_ci95_block_boot": (-2.6, -0.4)}, 4) == "NONE"
    assert decide({"n_active": 3, "note": "insufficient sample"}, 4) == "NONE"


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk(seed):
    bars = synthetic_bars("2024-01-01", "2024-12-31", seed=seed)
    feats = pd.concat([window_outcome(bars, tz, s, e, n) for n, (tz, s, e) in LONDON_FIX_WINDOWS.items()], axis=1)
    split = pd.Series("dev", index=feats.index)
    res = run_fix_tests(feats, split, E007_TESTS, blocks=("dev",))
    assert len(res) == 4
    assert not (res["decision"] == "SIGNAL").any()


def test_fix_windows_use_london_clock():
    # 2024-07-01 is BST: 15:00-16:00 London = 14:00-15:00 UTC -> 60 bars, first bar 14:00 UTC.
    bars = synthetic_bars("2024-06-28", "2024-07-03")
    w = window_outcome(bars, "Europe/London", *LONDON_FIX_WINDOWS["ldn_fix_pre"][1:], "p")
    assert w.loc[date(2024, 7, 1), "y_p_bars"] == 60
