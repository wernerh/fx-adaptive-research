from datetime import date, time

import numpy as np
import pandas as pd

from fxresearch import treasury_auction as ta
from fxresearch.data import PIP, synthetic_bars


def _rec(d, st="Note", ct="01:00 PM", term="10-Year", **kw):
    r = {"auction_date": d, "security_type": st, "security_term": term, "closing_time_comp": ct,
         "inflation_index_security": "No", "floating_rate": "No", "cusip": f"{d}{st}{term}"}
    r.update(kw)
    return r


def test_constants_fixed():
    assert ta.HOLDS == {"B40": 10, "B41": 1} and ta.WINDOW_MIN == 10 and ta.EXIT_HM == (16, 0)
    assert ta.ALPHA_T == 0.025 and ta.MIN_MEAN_PIPS == 1.0 and ta.MIN_EVENTS == 150 and ta.BOOT_BLOCK == 20
    assert (ta.GATE_MIN_PER_YEAR, ta.GATE_MAX_PER_YEAR, ta.GATE_MIN_PARSED) == (50, 110, 0.95)
    assert ta.MAX_ENTRY_SPREAD_PIPS == 2.0


def test_parse_close_time():
    assert ta.parse_close_time("01:00 PM") == time(13, 0)
    assert ta.parse_close_time("1:00 PM") == time(13, 0)
    assert ta.parse_close_time("11:30 AM") == time(11, 30)
    assert ta.parse_close_time("12:00 PM") == time(12, 0)
    assert ta.parse_close_time("13:00") == time(13, 0)
    assert ta.parse_close_time("01:00:00 PM") == time(13, 0)
    assert ta.parse_close_time("null") is None and ta.parse_close_time("") is None and ta.parse_close_time(np.nan) is None


def test_qualify_excludes_bills_tips_frns():
    assert ta.qualify(_rec("2016-01-05"))[0]
    assert ta.qualify(_rec("2016-01-05", st="Bond", term="30-Year"))[0]
    assert not ta.qualify(_rec("2016-01-05", st="Bill", term="13-Week"))[0]
    assert not ta.qualify(_rec("2016-01-05", st="CMB"))[0]
    assert not ta.qualify(_rec("2016-01-05", inflation_index_security="Yes"))[0]
    assert not ta.qualify(_rec("2016-01-05", term="2-Year", floating_rate="Yes"))[0]
    assert ta.tenor_bucket(_rec("x", term="9-Year 10-Month", original_security_term="10-Year")) == "long"
    assert ta.tenor_bucket(_rec("x", term="2-Year")) == "short"


def test_gate_counts_per_year_and_parse_share():
    recs = [_rec(f"{y}-{m:02d}-{d:02d}") for y in (2015, 2016) for m in range(1, 13) for d in (5, 10, 15, 20, 25)]
    cal = ta.calendar_from_records(recs)
    g = ta.calendar_gate(cal, years=[2015, 2016])
    assert g["qualifying_per_year"] == {2015: 60, 2016: 60} and g["pass"]
    assert not ta.calendar_gate(cal, years=[2015, 2016, 2017])["pass"]          # 2017 has 0
    bad = ta.calendar_from_records([_rec(r["auction_date"], ct="?") if i % 10 == 0 else r for i, r in enumerate(recs)])
    assert not ta.calendar_gate(bad, years=[2015, 2016])["pass"]                 # 90% parsed < 95%


def test_events_merge_same_time_keep_distinct_times():
    cal = ta.calendar_from_records([_rec("2016-01-05"), _rec("2016-01-05", term="3-Year"),
                                    _rec("2016-01-05", ct="11:30 AM"), _rec("2016-01-05", st="Bill", ct="11:30 AM")])
    ev = ta.auction_events(cal)
    assert len(ev) == 2
    assert ev.set_index("close_time").loc[time(13, 0), "n_auctions"] == 2
    assert ev.set_index("close_time").loc[time(11, 30), "n_auctions"] == 1


def _bars():
    return synthetic_bars(start="2024-01-01", end="2024-02-17")


def test_build_events_signal_entry_exit_and_no_lookahead():
    bars = _bars()
    cal = ta.calendar_from_records([_rec("2024-01-10"), _rec("2024-01-17", ct="11:30 AM"), _rec("2024-02-14")])
    ev = ta.auction_events(cal)
    dates = ta.weekday_trading_dates(bars)
    df = ta.build_events(ev, bars, dates)
    r = df.iloc[0]
    pre = bars.loc[pd.Timestamp("2024-01-10 12:50", tz="America/New_York").tz_convert("UTC")]
    post = bars.loc[pd.Timestamp("2024-01-10 13:10", tz="America/New_York").tz_convert("UTC")]
    assert np.isclose(r["window_pips"], ((post.bid_open + post.ask_open) / 2 - (pre.bid_open + pre.ask_open) / 2) / PIP)
    k = dates.index(date(2024, 1, 10))
    assert r["B40_exit_date"] == dates[k + 10] and r["B41_exit_date"] == dates[k + 1]
    # the 2024-02-14 event cannot reach its 10th trading date inside the data -> exit_outside_dev for B40 only
    last = df.iloc[-1]
    assert last["B40_excluded"] == "exit_outside_dev" and last["B41_excluded"] is None
    # no look-ahead: perturbing every bar after T+10 min on 2024-01-10 leaves window and side unchanged
    t_cut = pd.Timestamp("2024-01-10 13:15", tz="America/New_York").tz_convert("UTC")
    b2 = bars.copy()
    later = b2.index >= t_cut
    for c in ("bid_open", "ask_open", "bid_high", "ask_high", "bid_low", "ask_low", "bid_close", "ask_close"):
        b2.loc[later, c] = b2.loc[later, c] + 0.05
    df2 = ta.build_events(ev, b2, dates)
    assert df2.iloc[0]["window_pips"] == r["window_pips"] and df2.iloc[0]["side"] == r["side"]
    assert df2.iloc[0]["B41_exit_date"] > date(2024, 1, 10)


def test_missing_window_and_not_trading_date_and_spread_skip():
    bars = _bars()
    ev = ta.auction_events(ta.calendar_from_records([_rec("2024-01-10"), _rec("2024-01-13"), _rec("2024-01-11")]))
    t_gap = pd.Timestamp("2024-01-10 13:10", tz="America/New_York").tz_convert("UTC")
    b = bars[(bars.index < t_gap) | (bars.index >= t_gap + pd.Timedelta(minutes=5))].copy()
    t_wide = pd.Timestamp("2024-01-11 13:10", tz="America/New_York").tz_convert("UTC")
    b.loc[t_wide, "ask_open"] = b.loc[t_wide, "bid_open"] + 3 * PIP
    df = ta.build_events(ev, b).set_index("date")
    assert df.loc[date(2024, 1, 10), "B41_excluded"] == "missing_window"
    assert df.loc[date(2024, 1, 13), "B41_excluded"] == "not_trading_date"        # Saturday
    assert df.loc[date(2024, 1, 11), "B41_excluded"] == "entry_skipped_spread"


def test_decide_rule():
    base = {"n": 200, "mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.2, 3.0)}
    assert ta.decide(base) == "SIGNAL"
    assert ta.decide({**base, "n": 149}) == "NONE"
    assert ta.decide({**base, "mean_pips": 0.8}) == "WEAK"
    assert ta.decide({**base, "t_p_one_sided": 0.03}) == "WEAK"
    assert ta.decide({**base, "mean_ci95_block_boot": (-0.1, 3.0), "t_p_one_sided": 0.03}) == "NONE"
    assert ta.decide({**base, "mean_pips": -1.0, "mean_ci95_block_boot": (-2.0, -0.1)}) == "NONE"


def test_control_events_skip_auction_dates():
    cal = ta.calendar_from_records([_rec("2024-01-10"), _rec("2024-01-17"), _rec("2024-01-25")])
    ctrl = ta.control_events(ta.auction_events(cal), cal)
    assert set(ctrl["date"]) == {date(2024, 1, 3), date(2024, 1, 18)}           # 01-17 - 7 = 01-10 is an auction date


def test_no_edge_on_random_walk():
    bars = synthetic_bars(start="2024-01-01", end="2024-03-31", seed=11)
    days = [d for d in pd.date_range("2024-01-02", "2024-03-10", freq="B")]
    cal = ta.calendar_from_records([_rec(d.date().isoformat()) for d in days])
    df = ta.build_events(ta.auction_events(cal), bars)
    res = ta.evaluate_arm(df, "B41")
    assert ta.decide(res) == "NONE"           # < 150 events and no edge by construction
    assert abs(res["mean_pips"]) < 3 * res["sd_pips"] / np.sqrt(res["n"]) + 1e-9
