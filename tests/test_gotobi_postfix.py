from datetime import date

import numpy as np
import pandas as pd
import pytest

from fxresearch import gotobi_postfix as gp
from fxresearch.data import PIP, synthetic_bars


def test_constants_fixed_by_preregistration():
    assert (gp.ENTRY_HM, gp.EXIT_HM, gp.LATE_HM, gp.PRE_HM, gp.SIDE) == ((9, 55), (10, 55), (10, 25), (8, 55), 1)
    assert (gp.MIN_WINDOW_BARS, gp.MAX_ENTRY_SPREAD_PIPS, gp.MIN_MEAN_PIPS, gp.ALPHA) == (55, 2.0, 1.0, 0.05)
    assert (gp.BOOT_BLOCK, gp.BOOT_N) == (20, 2000)
    assert gp.TOKYO == "Asia/Tokyo"


def test_quotes_tokyo_keyed_long_sign_and_pre_move():
    bars = synthetic_bars("2024-03-01", "2024-03-12")
    df = gp.frame_from_bars(bars).set_index("date")
    d = date(2024, 3, 5)
    assert df.loc[d, "gotobi"]
    # 08:55 / 09:55 / 10:55 Tokyo on 2024-03-05 = 23:55 (Mar 4) / 00:55 / 01:55 UTC
    q = lambda ts: (lambda r: (r["bid_open"] + r["ask_open"]) / 2)(bars.loc[pd.Timestamp(ts, tz="UTC")])  # noqa: E731
    pm, em, xm = q("2024-03-04 23:55"), q("2024-03-05 00:55"), q("2024-03-05 01:55")
    assert df.loc[d, "signed_pips"] == pytest.approx((xm - em) / PIP)
    assert df.loc[d, "pre_move_pips"] == pytest.approx((em - pm) / PIP)
    assert df.loc[d, "window_bars"] == 60 and df.loc[d, "tested"]
    assert df.loc[d, "net_spec4_pips"] == pytest.approx(df.loc[d, "signed_pips"] - 0.5)
    assert df.loc[d, "net_x1_5_pips"] == pytest.approx(df.loc[d, "signed_pips"] - 0.75)
    assert not df.loc[date(2024, 3, 6), "tested"]


def test_exclusions_use_post_fix_window():
    bars = synthetic_bars("2024-03-01", "2024-03-12").copy()
    t = pd.Timestamp("2024-03-05 00:55", tz="UTC")          # 09:55 Tokyo entry on 2024-03-05
    bars.loc[t, "ask_open"] = bars.loc[t, "bid_open"] + 2.5 * PIP
    bars = bars.drop(pd.date_range("2024-03-08 00:56", periods=10, freq="1min", tz="UTC"))  # 09:56.. Tokyo on 03-08
    df = gp.frame_from_bars(bars).set_index("date")
    assert df.loc[date(2024, 3, 5), "excluded"] == "entry_skipped_spread"
    assert df.loc[date(2024, 3, 8), "excluded"] == "low_coverage"
    # a wide spread at 08:55 (pre-fix, descriptive only) does not exclude
    b2 = synthetic_bars("2024-03-01", "2024-03-12").copy()
    t2 = pd.Timestamp("2024-03-04 23:55", tz="UTC")
    b2.loc[t2, "ask_open"] = b2.loc[t2, "bid_open"] + 3 * PIP
    assert gp.frame_from_bars(b2).set_index("date").loc[date(2024, 3, 5), "tested"]
    b3 = synthetic_bars("2024-03-01", "2024-03-12").drop(pd.date_range("2024-03-06 01:55", periods=5, freq="1min", tz="UTC"))
    assert gp.frame_from_bars(b3).set_index("date").loc[date(2024, 3, 6), "excluded"] == "missing_exit"


def test_no_look_ahead():
    bars = synthetic_bars("2024-03-01", "2024-03-20", seed=3)
    a = gp.frame_from_bars(bars).set_index("date")
    b = gp.frame_from_bars(bars[bars.index < pd.Timestamp("2024-03-12", tz="UTC")]).set_index("date")
    common = b.index[b["tested"]]
    assert len(common) > 0
    pd.testing.assert_series_equal(a.loc[common, "signed_pips"], b.loc[common, "signed_pips"])


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk_pipeline(seed):
    df = gp.frame_from_bars(synthetic_bars("2024-01-01", "2024-12-31", seed=seed))
    ev = df[df["tested"]]
    assert 60 < len(ev) < 90
    assert gp.decide_b26(gp.evaluate(ev["signed_pips"])) != "SIGNAL"


def test_rule_behaviour():
    rng = np.random.default_rng(2)
    assert gp.decide_b26(gp.evaluate(3.0 + rng.normal(0, 8, 460))) == "SIGNAL"
    assert sum(gp.decide_b26(gp.evaluate(rng.standard_t(4, 460) * 6)) == "SIGNAL" for _ in range(200)) / 200 <= 0.05
    assert gp.decide_b26(gp.evaluate(np.ones(39))) == "NONE"
