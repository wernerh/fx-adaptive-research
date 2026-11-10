"""Tests for E034 (B30 month-end pre-fix equity-hedging flow), written before any run (R072)."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch import month_end_hedging as mh
from fxresearch.data import synthetic_bars


def test_constants_fixed():
    assert mh.FIX_HM == (16, 0) and mh.PRE_HM == (15, 0) and mh.POST_HM == (17, 0)
    assert mh.ALPHA == 0.025 and mh.MIN_EVENTS == 50 and mh.BOOT_BLOCK == 1 and mh.BOOT_N == 2000
    assert mh.MIN_MEAN_PIPS == 1.0 and mh.MAX_ENTRY_SPREAD_PIPS == 2.0
    assert mh.FALLBACK_DAYS == 5 and mh.MAX_MISSING_INDEX_SHARE == 0.05
    assert mh.EU_INDEX == "eusidxeur" and mh.US_INDEX == "usa500idxusd"


def _weekdays(start, end):
    d, out = start, []
    while d <= end:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def test_month_end_table():
    dates = _weekdays(date(2016, 1, 4), date(2016, 4, 29))
    tab = mh.month_end_table(dates)
    assert list(tab["date"]) == [date(2016, 1, 29), date(2016, 2, 29), date(2016, 3, 31), date(2016, 4, 29)]
    assert tab["anchor"].iloc[0] is None
    assert tab["anchor"].iloc[1] == date(2016, 1, 29) and tab["anchor"].iloc[3] == date(2016, 3, 31)
    assert tab["prev_date"].iloc[1] == date(2016, 2, 26)  # Monday Feb 29 -> previous trading date Friday Feb 26


def test_month_end_table_gap_month_has_no_anchor():
    dates = _weekdays(date(2016, 1, 4), date(2016, 1, 29)) + _weekdays(date(2016, 3, 1), date(2016, 3, 31))
    tab = mh.month_end_table(dates)
    assert tab["anchor"].iloc[1] is None


def _q(dates, mids):
    return pd.DataFrame({"bid_open": [m - 0.5 for m in mids], "ask_open": [m + 0.5 for m in mids]}, index=pd.Index(dates))


def test_index_quote_fallback_and_after():
    q = _q([date(2016, 12, 29), date(2016, 12, 30)], [100.0, 101.0])
    assert mh.index_mid_on_or_before(q, date(2016, 12, 30)) == (date(2016, 12, 30), 101.0)
    assert mh.index_mid_on_or_before(q, date(2017, 1, 2)) == (date(2016, 12, 30), 101.0)  # fallback
    assert mh.index_mid_on_or_before(q, date(2017, 1, 6)) is None                         # > 5 days back
    assert mh.index_mid_on_or_before(q, date(2016, 12, 30), after=date(2016, 12, 30)) is None
    assert mh.index_mid_on_or_before(q, date(2016, 12, 31), after=date(2016, 12, 29)) == (date(2016, 12, 30), 101.0)


def _index_bars(start, end, drift_per_day, base=100.0):
    """1-minute index bars only 15:55-16:10 London each weekday; price = base * exp(drift * day count)."""
    rows, idx = [], []
    for i, d in enumerate(_weekdays(start, end)):
        t0 = pd.Timestamp(d.isoformat() + " 15:55", tz="Europe/London").tz_convert("UTC")
        p = base * np.exp(drift_per_day * i)
        for k in range(15):
            idx.append(t0 + pd.Timedelta(minutes=k))
            rows.append({"bid_open": p - 0.01, "ask_open": p + 0.01})
    return pd.DataFrame(rows, index=pd.DatetimeIndex(idx, name="ts"))


FX = synthetic_bars("2024-01-01", "2024-06-29", seed=3)  # last trading date Fri 2024-06-28


def test_build_events_signal_direction_and_columns():
    eu = _index_bars(date(2024, 1, 1), date(2024, 6, 30), +0.002)   # EU equities rise
    us = _index_bars(date(2024, 1, 1), date(2024, 6, 30), 0.0)      # US flat
    df = mh.build_events(FX, eu, us)
    assert len(df) == 6
    assert df["day_excluded"].iloc[0] == "no_prev_month_end"
    ok = df[df["anchor"].notna()]
    assert (ok["s"] > 0).all() and (ok["position"] == -1).all()     # EU outperformed -> short EUR/USD
    assert ok["hour_tested"].all() and ok["day_tested"].all()
    # signed = position x move
    r = ok.iloc[0]
    assert np.isclose(r["hour_signed_pips"], -r["hour_move_pips"])
    us_up = _index_bars(date(2024, 1, 1), date(2024, 6, 30), +0.004)
    df2 = mh.build_events(FX, eu, us_up)
    assert (df2[df2["anchor"].notna()]["position"] == 1).all()       # US outperformed -> long EUR/USD


def test_signal_uses_only_past_quotes():
    eu = _index_bars(date(2024, 1, 1), date(2024, 6, 30), +0.001)
    us = _index_bars(date(2024, 1, 1), date(2024, 6, 30), -0.001)
    base = mh.build_events(FX, eu, us)
    # scramble all index prices after 16:05 London on each D-1: S must not change
    cut = {pd.Timestamp(d.isoformat() + " 16:05", tz="Europe/London") for d in base["prev_date"].dropna()}
    eu2, us2 = eu.copy(), us.copy()
    for frame in (eu2, us2):
        ldn = frame.index.tz_convert("Europe/London")
        later = np.zeros(len(frame), dtype=bool)
        for c in cut:
            later |= (ldn >= c) & (pd.Index(ldn.date) == c.date())
        frame.loc[later, ["bid_open", "ask_open"]] *= 1.5
    # also change FX bars on D after 16:05 London: hour/day results unchanged
    fx2 = FX.copy()
    ldn = fx2.index.tz_convert("Europe/London")
    mins = np.asarray(ldn.hour) * 60 + np.asarray(ldn.minute)
    me = set(base["date"])
    late = (mins >= 16 * 60 + 5) & pd.Index(ldn.date).isin(me)
    fx2.loc[late, [c for c in fx2.columns if c != "volume"]] *= 1.01
    alt = mh.build_events(fx2, eu2, us2)
    pd.testing.assert_series_equal(base["s"], alt["s"])
    pd.testing.assert_series_equal(base["hour_signed_pips"], alt["hour_signed_pips"])
    pd.testing.assert_series_equal(base["day_signed_pips"], alt["day_signed_pips"])


def test_holiday_fallback_flag():
    eu = _index_bars(date(2024, 1, 1), date(2024, 6, 30), +0.001)
    us = _index_bars(date(2024, 1, 1), date(2024, 6, 30), 0.0)
    base = mh.build_events(FX, eu, us)
    a = base["anchor"].dropna().iloc[0]
    ldn = eu.index.tz_convert("Europe/London")
    eu_h = eu[pd.Index(ldn.date) != a]                                # EU index closed on the anchor date
    df = mh.build_events(FX, eu_h, us)
    row = df[df["anchor"] == a].iloc[0]
    assert row["fallback_quote"] and row["eu_start_date"] < a and not np.isnan(row["s"])


def test_data_gate():
    eu = _index_bars(date(2024, 1, 1), date(2024, 6, 30), +0.001)
    us = _index_bars(date(2024, 1, 1), date(2024, 6, 30), 0.0)
    df = mh.build_events(FX, eu, us)
    assert mh.data_gate(df, eu, us)["ok"]
    empty = eu.iloc[:0]
    assert not mh.data_gate(mh.build_events(FX, empty, us), empty, us)["ok"]
    # remove EU quotes for a whole month around one D-1 -> 1 of 5 anchored month-ends missing (20% > 5%)
    d1 = df["prev_date"].dropna().iloc[2]
    ldn = eu.index.tz_convert("Europe/London")
    keep = ~((pd.Index(ldn.date) > d1 - timedelta(days=20)) & (pd.Index(ldn.date) <= d1))
    eu_m = eu[keep]
    g = mh.data_gate(mh.build_events(FX, eu_m, us), eu_m, us)
    assert not g["ok"] and g["missing_index_quote"] == 1


def test_decide_rule():
    assert mh.decide_b30({"n": 40, "mean_pips": 9.0, "t_p_one_sided": 0.001, "mean_ci95_boot": (2.0, 9.0)}) == "NONE"
    assert mh.decide_b30({"n": 70, "mean_pips": 6.0, "t_p_one_sided": 0.01, "mean_ci95_boot": (1.0, 9.0)}) == "SIGNAL"
    assert mh.decide_b30({"n": 70, "mean_pips": 6.0, "t_p_one_sided": 0.03, "mean_ci95_boot": (0.5, 9.0)}) == "WEAK"
    assert mh.decide_b30({"n": 70, "mean_pips": 0.8, "t_p_one_sided": 0.01, "mean_ci95_boot": (0.1, 2.0)}) == "WEAK"
    assert mh.decide_b30({"n": 70, "mean_pips": -1.0, "t_p_one_sided": 0.9, "mean_ci95_boot": (-3.0, 1.0)}) == "NONE"


def test_null_calibration_iid():
    rng = np.random.default_rng(0)
    hits = 0
    for _ in range(200):
        x = rng.standard_t(4, size=71) * 20
        hits += mh.decide_b30(mh.evaluate_b30(x)) == "SIGNAL"
    assert hits / 200 <= 0.05


def test_random_walk_never_signal():
    eu = _index_bars(date(2024, 1, 1), date(2024, 6, 30), +0.001)
    us = _index_bars(date(2024, 1, 1), date(2024, 6, 30), 0.0)
    df = mh.build_events(FX, eu, us)
    for win in ("hour", "day"):
        ev = df[df[f"{win}_tested"]]
        assert mh.decide_b30(mh.evaluate_b30(ev[f"{win}_signed_pips"])) == "NONE"  # < 50 events


def test_load_index_missing_dir(tmp_path):
    df = mh.load_index(tmp_path, mh.EU_INDEX)
    assert len(df) == 0 and "bid_open" in df.columns


def test_load_index_reads_files(tmp_path):
    ts = pd.date_range("2024-01-02 16:00", periods=3, freq="1min", tz="UTC")
    ms = (ts.asi8 // 10**6)
    for side, off in (("bid", -0.5), ("ask", 0.5)):
        pd.DataFrame({"timestamp": ms, "open": 100 + off, "high": 101 + off, "low": 99 + off, "close": 100 + off}).to_csv(
            tmp_path / f"{mh.EU_INDEX}-m1-{side}-2024.csv", index=False)
    df = mh.load_index(tmp_path, mh.EU_INDEX)
    assert len(df) == 3 and np.allclose(df["ask_open"] - df["bid_open"], 1.0)
