from datetime import date

import pandas as pd

from fxresearch.sessions import ASIA, LONDON, US, label_sessions, trading_date, is_weekend_bar


def ts(s):
    return pd.Timestamp(s, tz="UTC")


def test_trading_day_rolls_at_5pm_new_york_winter():
    # 22:00 UTC = 17:00 EST -> new trading day
    assert trading_date(ts("2024-01-16 21:59")) == date(2024, 1, 16)
    assert trading_date(ts("2024-01-16 22:00")) == date(2024, 1, 17)


def test_trading_day_rolls_at_5pm_new_york_summer():
    # 21:00 UTC = 17:00 EDT
    assert trading_date(ts("2024-07-16 20:59")) == date(2024, 7, 16)
    assert trading_date(ts("2024-07-16 21:00")) == date(2024, 7, 17)


def test_london_open_moves_with_uk_dst():
    assert LONDON.window_utc(date(2024, 1, 16))[0] == ts("2024-01-16 08:00")
    assert LONDON.window_utc(date(2024, 7, 16))[0] == ts("2024-07-16 07:00")


def test_tokyo_has_no_dst():
    assert ASIA.window_utc(date(2024, 1, 16)) == (ts("2024-01-16 00:00"), ts("2024-01-16 06:00"))
    assert ASIA.window_utc(date(2024, 7, 16)) == (ts("2024-07-16 00:00"), ts("2024-07-16 06:00"))


def test_us_eu_dst_mismatch_week():
    # 2024-03-12: US already on EDT (switched 10 Mar), UK still on GMT (switches 31 Mar).
    d = date(2024, 3, 12)
    us_start = US.window_utc(d)[0]
    lon_start = LONDON.window_utc(d)[0]
    assert us_start == ts("2024-03-12 12:00")
    assert (us_start - lon_start) == pd.Timedelta(hours=4)  # normally 5h
    # London session must still end no later than US start (no feature overlap).
    assert LONDON.window_utc(d)[1] <= us_start


def test_sessions_never_overlap_and_are_ordered_across_a_year():
    for d in pd.date_range("2024-01-01", "2024-12-31", freq="B").date:
        a, l, u = ASIA.window_utc(d), LONDON.window_utc(d), US.window_utc(d)
        assert a[1] <= l[0] and l[1] <= u[0], d


def test_label_sessions_assigns_trading_date_and_flags():
    idx = pd.DatetimeIndex([ts("2024-01-16 00:30"), ts("2024-01-16 09:00"), ts("2024-01-16 13:30"),
                            ts("2024-01-16 18:00")])
    lab = label_sessions(idx)
    assert list(lab["asia"]) == [True, False, False, False]
    assert list(lab["london"]) == [False, True, False, False]
    assert list(lab["us"]) == [False, False, True, False]
    assert set(lab["trading_date"]) == {date(2024, 1, 16)}


def test_weekend_detection():
    idx = pd.DatetimeIndex([ts("2024-01-19 21:59"), ts("2024-01-19 22:00"), ts("2024-01-21 21:59"),
                            ts("2024-01-21 22:00")])
    assert list(is_weekend_bar(idx)) == [False, True, True, False]
