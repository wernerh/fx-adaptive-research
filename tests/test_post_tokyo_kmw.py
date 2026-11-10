from datetime import date

import numpy as np
import pandas as pd
import pytest

from fxresearch import post_tokyo_kmw as pk
from fxresearch.data import PIP, synthetic_bars


def test_constants_fixed_by_preregistration():
    assert (pk.ENTRY_HM, pk.EXIT_HM, pk.MID_HM, pk.SIDE, pk.NY) == ((20, 55), (2, 0), (21, 55), 1, "America/New_York")
    assert (pk.WINDOW_BARS, pk.MIN_WINDOW_BARS, pk.MIN_DATES) == (305, 280, 200)
    assert (pk.MAX_ENTRY_SPREAD_PIPS, pk.MIN_MEAN_PIPS, pk.ALPHA, pk.BOOT_BLOCK, pk.BOOT_N) == (2.0, 1.0, 0.05, 20, 2000)


def _mid(bars, ts):
    r = bars.loc[pd.Timestamp(ts, tz="UTC")]
    return (r["bid_open"] + r["ask_open"]) / 2


def test_window_spans_ny_midnight_same_trading_date_edt_and_est():
    bars = synthetic_bars("2024-03-01", "2024-03-20")
    df = pk.frame_from_bars(bars).set_index("date")
    # EST: trading date Thu 2024-03-07 -> entry 20:55 NY Wed 03-06 = 01:55 UTC 03-07; exit 02:00 NY 03-07 = 07:00 UTC
    d = date(2024, 3, 7)
    assert not df.loc[d, "edt"]
    e, x, m = _mid(bars, "2024-03-07 01:55"), _mid(bars, "2024-03-07 07:00"), _mid(bars, "2024-03-07 02:55")
    assert df.loc[d, "signed_pips"] == pytest.approx((x - e) / PIP)
    assert df.loc[d, "first_hour_pips"] + df.loc[d, "rest_pips"] == pytest.approx(df.loc[d, "signed_pips"])
    assert df.loc[d, "first_hour_pips"] == pytest.approx((m - e) / PIP)
    assert df.loc[d, "window_bars"] == 305 and df.loc[d, "tested"]
    # EDT (after 2024-03-10): trading date Wed 2024-03-13 -> entry 00:55 UTC, exit 06:00 UTC
    d2 = date(2024, 3, 13)
    assert df.loc[d2, "edt"]
    e2, x2 = _mid(bars, "2024-03-13 00:55"), _mid(bars, "2024-03-13 06:00")
    assert df.loc[d2, "signed_pips"] == pytest.approx((x2 - e2) / PIP)
    assert df.loc[d2, "net_spec4_pips"] == pytest.approx(df.loc[d2, "signed_pips"] - 0.5)
    assert df.loc[d2, "net_x1_5_pips"] == pytest.approx(df.loc[d2, "signed_pips"] - 0.75)


def test_monday_uses_sunday_evening_and_no_weekend_dates():
    bars = synthetic_bars("2024-03-01", "2024-03-20")
    df = pk.frame_from_bars(bars).set_index("date")
    assert all(d.weekday() < 5 for d in df.index)
    # Monday 2024-03-04: entry Sunday 03-03 20:55 EST = 01:55 UTC 03-04 (Sunday evening, market open after 17:00 NY)
    d = date(2024, 3, 4)
    assert df.loc[d, "tested"]
    assert df.loc[d, "entry_mid"] == pytest.approx(_mid(bars, "2024-03-04 01:55"))


def test_exclusions_order_and_coverage():
    bars = synthetic_bars("2024-03-01", "2024-03-20").copy()
    t = pd.Timestamp("2024-03-07 01:55", tz="UTC")
    bars.loc[t, "ask_open"] = bars.loc[t, "bid_open"] + 2.5 * PIP
    bars = bars.drop(pd.date_range("2024-03-08 03:00", periods=26, freq="1min", tz="UTC"))   # 279 bars left
    bars = bars.drop(pd.date_range("2024-03-12 06:00", periods=5, freq="1min", tz="UTC"))    # exit missing (EDT 02:00)
    df = pk.frame_from_bars(bars).set_index("date")
    assert df.loc[date(2024, 3, 7), "excluded"] == "entry_skipped_spread"
    assert df.loc[date(2024, 3, 8), "excluded"] == "low_coverage" and df.loc[date(2024, 3, 8), "window_bars"] == 279
    assert df.loc[date(2024, 3, 12), "excluded"] == "missing_exit"
    b2 = synthetic_bars("2024-03-01", "2024-03-20").drop(pd.date_range("2024-03-08 03:00", periods=25, freq="1min", tz="UTC"))
    assert pk.frame_from_bars(b2).set_index("date").loc[date(2024, 3, 8), "tested"]
    c = pk.counts(df)
    assert c["entry_skipped_spread"] == 1 and c["low_coverage"] == 1 and c["missing_exit"] == 1


def test_no_look_ahead():
    bars = synthetic_bars("2024-03-01", "2024-03-25", seed=3)
    a = pk.frame_from_bars(bars).set_index("date")
    b = pk.frame_from_bars(bars[bars.index < pd.Timestamp("2024-03-15", tz="UTC")]).set_index("date")
    common = b.index[b["tested"]]
    assert len(common) > 5
    pd.testing.assert_series_equal(a.loc[common, "signed_pips"], b.loc[common, "signed_pips"])


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk_pipeline(seed):
    df = pk.frame_from_bars(synthetic_bars("2023-01-01", "2024-06-30", seed=seed))
    ev = df[df["tested"]]
    assert 360 < len(ev) < 400
    assert pk.decide_b27(pk.evaluate(ev["signed_pips"])) != "SIGNAL"


def test_rule_behaviour():
    rng = np.random.default_rng(2)
    assert pk.decide_b27(pk.evaluate(3.0 + rng.normal(0, 17, 600))) == "SIGNAL"
    assert sum(pk.decide_b27(pk.evaluate(rng.standard_t(4, 600) * 12)) == "SIGNAL" for _ in range(200)) / 200 <= 0.05
    r = pk.evaluate(np.ones(199))
    assert r["note"] == "insufficient sample" and pk.decide_b27(r) == "NONE"
