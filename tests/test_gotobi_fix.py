from datetime import date

import numpy as np
import pandas as pd
import pytest

from fxresearch import gotobi_fix as gf
from fxresearch.data import PIP, synthetic_bars


def test_constants_fixed_by_preregistration():
    assert gf.GOTOBI_DAYS == (5, 10, 15, 20, 25, 30)
    assert (gf.ENTRY_HM, gf.EXIT_HM, gf.LATE_HM, gf.SIDE) == ((8, 55), (9, 55), (9, 25), -1)
    assert (gf.MIN_WINDOW_BARS, gf.MAX_ENTRY_SPREAD_PIPS, gf.MIN_MEAN_PIPS, gf.ALPHA) == (55, 2.0, 1.0, 0.05)
    assert (gf.BOOT_BLOCK, gf.BOOT_N) == (20, 2000)
    assert gf.TOKYO == "Asia/Tokyo"


@pytest.mark.parametrize("d,exp", [
    (date(2024, 3, 5), (True, False, False)),     # Tue 5th
    (date(2024, 3, 6), (False, False, False)),
    (date(2024, 3, 29), (True, True, True)),      # Fri; 30 Sat and 31 Sun (month end) shift here
    (date(2024, 2, 29), (True, False, True)),     # leap-year last day
    (date(2023, 2, 28), (True, False, True)),     # non-leap last day
    (date(2024, 11, 29), (True, True, True)),     # Fri; Sat 30 = last day of Nov
    (date(2024, 8, 30), (True, False, True)),     # Fri 30 nominal, Sat 31 month end also maps here: not "shifted"
    (date(2024, 5, 10), (True, False, False)),    # Fri 10th, nothing on the weekend
    (date(2024, 1, 19), (True, True, False)),     # Fri; Sat 20th shifts here
    (date(2024, 1, 20), (False, False, False)),   # Saturday never gotobi
    (date(2024, 1, 31), (True, False, True)),     # 31st = last day
    (date(2024, 4, 30), (True, False, True)),     # 30th that is also the last day
])
def test_gotobi_calendar(d, exp):
    g = gf.gotobi_info(d)
    assert (g["gotobi"], g["weekend_shifted"], g["month_end"]) == exp


def test_gotobi_share_is_about_thirty_percent():
    days = pd.bdate_range("2015-01-01", "2020-12-31")
    share = np.mean([gf.gotobi_info(d.date())["gotobi"] for d in days])
    assert 0.27 < share < 0.33


def test_quotes_keyed_by_tokyo_date_equal_trading_date_and_signed_short():
    bars = synthetic_bars("2024-03-01", "2024-03-12")
    df = gf.frame_from_bars(bars).set_index("date")
    d = date(2024, 3, 5)
    assert d in df.index and df.loc[d, "gotobi"]
    # 08:55 Tokyo on 2024-03-05 = 2024-03-04 23:55 UTC; 09:55 Tokyo = 00:55 UTC.
    e = bars.loc[pd.Timestamp("2024-03-04 23:55", tz="UTC")]
    x = bars.loc[pd.Timestamp("2024-03-05 00:55", tz="UTC")]
    em, xm = (e["bid_open"] + e["ask_open"]) / 2, (x["bid_open"] + x["ask_open"]) / 2
    assert df.loc[d, "signed_pips"] == pytest.approx(-(xm - em) / PIP)
    assert df.loc[d, "window_bars"] == 60
    assert df.loc[d, "tested"]
    assert not df.loc[date(2024, 3, 6), "tested"]          # tradable but not gotobi
    # constant 0.3 spread -> bid/ask net = mid - 0.3; SPEC 4 a further 0.2
    assert df.loc[d, "net_bidask_pips"] == pytest.approx(df.loc[d, "signed_pips"] - 0.3)
    assert df.loc[d, "net_spec4_pips"] == pytest.approx(df.loc[d, "signed_pips"] - 0.5)
    assert df.loc[d, "net_x1_5_pips"] == pytest.approx(df.loc[d, "signed_pips"] - 0.75)


def test_exclusions_in_order():
    bars = synthetic_bars("2024-03-01", "2024-03-12").copy()
    # 2024-03-05: widen spread at entry bar -> entry_skipped_spread
    t = pd.Timestamp("2024-03-04 23:55", tz="UTC")
    bars.loc[t, "ask_open"] = bars.loc[t, "bid_open"] + 2.5 * PIP
    # 2024-03-08 (Fri; Sat 9 not nominal, Sun 10 nominal -> gotobi): drop 10 window bars -> low_coverage
    bars = bars.drop(pd.date_range("2024-03-07 23:56", periods=10, freq="1min", tz="UTC"))
    df = gf.frame_from_bars(bars).set_index("date")
    assert df.loc[date(2024, 3, 5), "excluded"] == "entry_skipped_spread"
    assert df.loc[date(2024, 3, 8), "gotobi"] and df.loc[date(2024, 3, 8), "weekend_shifted"]
    assert df.loc[date(2024, 3, 8), "excluded"] == "low_coverage"
    # missing exit: remove the whole 09:55-10:00 Tokyo block on 2024-03-06
    b2 = bars.drop(pd.date_range("2024-03-06 00:55", periods=5, freq="1min", tz="UTC"))
    assert gf.frame_from_bars(b2).set_index("date").loc[date(2024, 3, 6), "excluded"] == "missing_exit"
    b3 = bars.drop(pd.date_range("2024-03-06 23:55", periods=5, freq="1min", tz="UTC"))
    assert gf.frame_from_bars(b3).set_index("date").loc[date(2024, 3, 7), "excluded"] == "missing_entry"
    c = gf.counts(df)
    assert c["entry_skipped_spread"] == 1 and c["low_coverage"] == 1


def test_no_look_ahead_flag_is_calendar_only():
    bars = synthetic_bars("2024-03-01", "2024-03-20", seed=3)
    a = gf.frame_from_bars(bars).set_index("date")
    cut = bars[bars.index < pd.Timestamp("2024-03-12", tz="UTC")]
    b = gf.frame_from_bars(cut).set_index("date")
    common = b.index[b["tested"]]
    assert len(common) > 0
    pd.testing.assert_series_equal(a.loc[common, "signed_pips"], b.loc[common, "signed_pips"])


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk_pipeline(seed):
    bars = synthetic_bars("2024-01-01", "2024-12-31", seed=seed)
    df = gf.frame_from_bars(bars)
    ev = df[df["tested"]]
    assert 60 < len(ev) < 90
    assert gf.decide_b25(gf.evaluate(ev["signed_pips"])) != "SIGNAL"


def test_random_walk_signal_rate_low():
    rng = np.random.default_rng(0)
    sig = sum(gf.decide_b25(gf.evaluate(rng.standard_t(4, 460) * 6)) == "SIGNAL" for _ in range(200))
    assert sig / 200 <= 0.05


def test_strong_effect_gives_signal_and_insufficient_gives_none():
    rng = np.random.default_rng(1)
    assert gf.decide_b25(gf.evaluate(3.0 + rng.normal(0, 8, 460))) == "SIGNAL"
    assert gf.decide_b25(gf.evaluate(0.5 + rng.normal(0, 2, 460))) == "WEAK"
    assert gf.evaluate(np.ones(39))["note"] == "insufficient sample"
    assert gf.decide_b25(gf.evaluate(np.ones(39))) == "NONE"
