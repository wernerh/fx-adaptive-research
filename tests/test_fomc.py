from datetime import date

import numpy as np
import pandas as pd
import pytest

from fxresearch.data import synthetic_bars
from fxresearch.fomc import (
    decide_b11, evaluate_long, parse_calendars_page, parse_heading, parse_historical_page, prev_business_day,
    validate_year, window_frame,
)

# Synthetic HTML fixtures shaped like the Fed pages. Dates here are invented test inputs, not FOMC dates.
HIST = """
<div class="panel panel-default"><div class="panel-heading"><h5>January 10-11 Meeting - 2099</h5></div></div>
<h5>February 3 Conference Call - 2099</h5>
<h5>March 14-15 Meeting - 2099</h5>
<h5>March 20 Meeting (unscheduled) - 2099</h5>
<h5>April 29-May 1 Meeting - 2099</h5>
<h5>June 16-17 Meeting - 2099</h5>
<h5>July 28-29 Meeting - 2098</h5>
<h5>July 28-29 Meeting - 2099</h5>
<h5>September 15&ndash;16 Meeting - 2099</h5>
<h5>October 27-28 Meeting - 2099</h5>
<h5>December 15-16 Meeting - 2099</h5>
"""

CAL = """
<h4><a>2098 FOMC Meetings</a></h4>
<div class="row fomc-meeting"><div class="fomc-meeting__month col-xs-5"><strong>January</strong></div>
<div class="fomc-meeting__date col-xs-4">27-28</div></div>
<h4><a>2097 FOMC Meetings</a></h4>
<div class="row fomc-meeting"><div class="fomc-meeting__month col-xs-5"><strong>Jan</strong></div>
<div class="fomc-meeting__date col-xs-4">26-27</div></div>
<div class="row fomc-meeting"><div class="fomc-meeting__month col-xs-5"><strong>March</strong></div>
<div class="fomc-meeting__date col-xs-4">16 (unscheduled)</div></div>
<div class="row fomc-meeting"><div class="fomc-meeting__month col-xs-5"><strong>Apr/May</strong></div>
<div class="fomc-meeting__date col-xs-4">30-1*</div></div>
"""


def test_parse_heading_variants():
    m = parse_heading("April 29-May 1 Meeting", 2099)
    assert m.start == date(2099, 4, 29) and m.statement_date == date(2099, 5, 1) and m.scheduled
    assert not parse_heading("March 20 Meeting (unscheduled)", 2099).scheduled
    assert not parse_heading("February 3 Conference Call", 2099).scheduled
    assert parse_heading("Minutes released January 5", 2099) is None


def test_historical_page_eight_scheduled():
    ms = parse_historical_page(HIST, 2099)
    sched = [m for m in ms if m.scheduled]
    assert len(sched) == 8
    assert sched[0].statement_date == date(2099, 1, 11)
    assert date(2099, 9, 16) in [m.statement_date for m in sched]  # en dash handled
    assert all(m.year == 2099 for m in ms)  # 2098 heading ignored
    ok, note = validate_year(ms)
    # 2099-01-11 etc. are arbitrary dates; only the count/structure is checked here
    assert ok or "weekend" in note


def test_validate_year_rejects_wrong_count():
    ms = parse_historical_page(HIST, 2099)[:5]
    ok, note = validate_year(ms)
    assert not ok and "scheduled meetings" in note


def test_calendars_page():
    cal = parse_calendars_page(CAL)
    assert set(cal) == {2097, 2098}
    m97 = cal[2097]
    assert [m.scheduled for m in m97] == [True, False, True]
    assert m97[2].start == date(2097, 4, 30) and m97[2].statement_date == date(2097, 5, 1)


def test_prev_business_day():
    assert prev_business_day(date(2024, 3, 13)) == date(2024, 3, 12)  # Wed -> Tue
    assert prev_business_day(date(2024, 3, 11)) == date(2024, 3, 8)   # Mon -> Fri


def test_window_uses_16ny_edges_dst_aware():
    bars = synthetic_bars("2024-03-01", "2024-03-20", spread_pips_=0.3)
    # 2024-03-13 is after US DST start (Mar 10): 16:00 NY = 20:00 UTC.
    f = window_frame(bars, [date(2024, 3, 13)])
    e = bars.loc[pd.Timestamp("2024-03-12 20:00", tz="UTC")]
    x = bars.loc[pd.Timestamp("2024-03-13 19:59", tz="UTC")]
    expected = ((x["bid_close"] + x["ask_close"]) / 2 - (e["bid_open"] + e["ask_open"]) / 2) / 1e-4
    assert abs(f.loc[date(2024, 3, 13), "ret_pips"] - expected) < 1e-9
    assert abs(f.loc[date(2024, 3, 13), "ret_pips"] - f.loc[date(2024, 3, 13), "net_bidask_pips"] - 0.3) < 1e-6
    # Before DST (2024-03-06): 16:00 NY = 21:00 UTC.
    g = window_frame(bars, [date(2024, 3, 6)])
    e2 = bars.loc[pd.Timestamp("2024-03-05 21:00", tz="UTC")]
    x2 = bars.loc[pd.Timestamp("2024-03-06 20:59", tz="UTC")]
    exp2 = ((x2["bid_close"] + x2["ask_close"]) / 2 - (e2["bid_open"] + e2["ask_open"]) / 2) / 1e-4
    assert abs(g.loc[date(2024, 3, 6), "ret_pips"] - exp2) < 1e-9


def test_missing_quotes_are_nan_not_filled():
    bars = synthetic_bars("2024-03-01", "2024-03-20")
    cut = bars[~((bars.index >= pd.Timestamp("2024-03-12 19:50", tz="UTC"))
                 & (bars.index < pd.Timestamp("2024-03-12 20:10", tz="UTC")))]
    f = window_frame(cut, [date(2024, 3, 13)])
    assert np.isnan(f.loc[date(2024, 3, 13), "ret_pips"])


def test_decide_rule():
    base = {"mean_pips": 12.0, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (1.0, 20.0)}
    assert decide_b11(base) == "SIGNAL"
    assert decide_b11({**base, "mean_pips": 8.0}) == "WEAK"
    assert decide_b11({**base, "mean_ci95_block_boot": (-1.0, 20.0), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b11({**base, "mean_pips": -3.0}) == "NONE"
    assert decide_b11({"n": 1}) == "NONE"


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk(seed):
    bars = synthetic_bars("2023-01-01", "2023-12-31", seed=seed)
    wednesdays = [d for d in pd.date_range("2023-01-04", "2023-12-27", freq="7D").date][::6]  # ~ every 6 weeks
    f = window_frame(bars, wednesdays)
    assert f["ret_pips"].notna().sum() >= 8
    assert decide_b11(evaluate_long(f["ret_pips"])) != "SIGNAL"


# --- R018: parser fix after the E013 phase-1 fetch (run 42458841737) failed validation for 2017-2019 ---------------
from pathlib import Path  # noqa: E402

RAW = Path(__file__).resolve().parents[1] / "backtests" / "calendars" / "raw_html"


def test_parse_heading_slash_cross_month():
    m = parse_heading("Jan/Feb 31-1 Meeting", 2099)
    assert m.start == date(2099, 1, 31) and m.statement_date == date(2099, 2, 1) and m.scheduled
    m = parse_heading("April/May 30-1 Meeting", 2099)
    assert m.start == date(2099, 4, 30) and m.statement_date == date(2099, 5, 1)
    m = parse_heading("Jul/Aug 31-1 Meeting", 2099)
    assert m.start == date(2099, 7, 31) and m.statement_date == date(2099, 8, 1)


def test_parse_heading_cancelled_counts_as_scheduled_slot_but_flagged():
    m = parse_heading("March 17-18 (cancelled) Meeting", 2099)
    assert m.scheduled and m.cancelled
    assert not parse_heading("March 14-15 Meeting", 2099).cancelled


@pytest.mark.parametrize("year", [2017, 2018, 2019])
def test_committed_raw_pages_now_parse_to_eight(year):
    p = RAW / f"fomchistorical{year}.html"
    if not p.exists():
        pytest.skip("raw page not committed")
    ms = parse_historical_page(p.read_text(), year)
    ok, note = validate_year(ms)
    assert ok, note


def test_promoted_fomc_date_file_is_valid():
    """R019: the reviewed date file used by E013 phase 2 (fetched on the runner, never hand-typed)."""
    from pathlib import Path

    import pandas as pd

    root = Path(__file__).resolve().parents[1]
    p = root / "data" / "calendars" / "fomc_dates.csv"
    cal = pd.read_csv(p, parse_dates=["meeting_start", "statement_date"])
    # identical to the runner output it was promoted from
    src = pd.read_csv(root / "backtests" / "calendars" / "fomc_dates.csv", parse_dates=["meeting_start", "statement_date"])
    pd.testing.assert_frame_equal(cal, src)
    s = cal[cal["scheduled"]]
    assert s.groupby("year").size().to_dict() == {y: 8 for y in range(2015, 2024)}
    assert (s["statement_date"].dt.weekday < 5).all()
    assert ((s["statement_date"] - s["meeting_start"]).dt.days <= 2).all()
    assert cal["source_url"].str.startswith("https://www.federalreserve.gov/monetarypolicy/").all()
    dev = s[(~s["cancelled"]) & (s["statement_date"] < "2021-01-01")]
    assert len(dev) == 47  # 48 scheduled 2015-2020 minus the cancelled 2020-03-18 slot


def test_calendar_block_dates_val_set_e014():
    """E014 (B11v): val statement days come from the validated date file; no dev or OOS date leaks in."""
    from pathlib import Path

    from fxresearch.fomc import calendar_block_dates
    from fxresearch.splits import DEFAULT_PLAN

    root = Path(__file__).resolve().parents[1]
    cal = pd.read_csv(root / "data" / "calendars" / "fomc_dates.csv")
    v = calendar_block_dates(cal, DEFAULT_PLAN, "val")
    assert len(v["scheduled"]) == 20
    assert v["cancelled"] == [] and v["unscheduled"] == []
    assert min(v["scheduled"]) == date(2021, 1, 27) and max(v["scheduled"]) == date(2023, 6, 14)
    assert all(date(2021, 1, 21) <= d <= date(2023, 6, 30) for d in v["scheduled"])
    d = calendar_block_dates(cal, DEFAULT_PLAN, "dev")
    assert len(d["scheduled"]) == 47 and d["cancelled"] == [date(2020, 3, 18)]
    with pytest.raises(ValueError):
        calendar_block_dates(cal, DEFAULT_PLAN, "oos")
