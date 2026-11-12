"""E046 (B54) FOMC-cycle even/odd weeks tests: cycle counting, weeks, positions, trade timing, exclusions, decision, RW."""
from datetime import date

import numpy as np
import pandas as pd

from fxresearch.data import OHLC, PIP, synthetic_bars
from fxresearch.fomc_cycle import (
    ALPHA, BOOT_BLOCK, EXCLUSION_ORDER, LONG_WEEKS, MIN_EVENTS, MIN_MEAN_PIPS, SHORT_WEEKS, counts, cycle_k, cycle_week,
    decide_b54, evaluate, frame_from_bars, position, prev_weekday, statement_dates,
)
from fxresearch.sessions import NY, trading_date

S1, S2 = date(2024, 1, 31), date(2024, 3, 20)   # Wednesdays, 35 weekdays apart
STMTS = [S1, S2]


def _dates(bars):
    return sorted({d for d in trading_date(bars.index) if d.weekday() < 5})


def test_constants_preregistered():
    assert MIN_EVENTS == 500 and MIN_MEAN_PIPS == 1.0 and ALPHA == 0.05 and BOOT_BLOCK == 20
    assert LONG_WEEKS == (2, 4, 6) and SHORT_WEEKS == (-1, 1, 3, 5)
    assert EXCLUSION_ORDER == ("pre_cycle", "unassigned", "week0_excluded", "missing_entry", "missing_exit",
                               "entry_skipped_spread")


def test_statement_dates_filters_unscheduled_and_cancelled():
    cal = pd.DataFrame({"statement_date": ["2020-01-29", "2020-03-03", "2020-03-18", "2020-04-29"],
                        "scheduled": [True, False, True, True], "cancelled": [False, False, True, False]})
    assert statement_dates(cal) == [date(2020, 1, 29), date(2020, 4, 29)]


def test_cycle_k_counting():
    assert cycle_k(S1, STMTS) == 0
    assert cycle_k(date(2024, 1, 30), STMTS) == -1           # Tue before
    assert cycle_k(date(2024, 1, 29), STMTS) == -2           # Mon before
    assert cycle_k(date(2024, 1, 26), STMTS) == -3           # Fri before (weekend skipped)
    assert cycle_k(date(2024, 1, 23), STMTS) == -6
    assert np.isnan(cycle_k(date(2024, 1, 22), STMTS))       # -7, no previous meeting -> pre_cycle
    assert cycle_k(date(2024, 2, 1), STMTS) == 1
    assert cycle_k(date(2024, 2, 5), STMTS) == 3             # Mon after weekend
    assert cycle_k(date(2024, 2, 6), STMTS) == 4
    # S2 is 35 weekdays after S1: S2-7 weekdays is k = 28 after S1; S2-6 is -6
    assert cycle_k(date(2024, 3, 11), STMTS) == 28
    assert cycle_k(date(2024, 3, 12), STMTS) == -6


def test_cycle_weeks_and_positions():
    exp = {-6: -1, -2: -1, -1: 0, 3: 0, 4: 1, 8: 1, 9: 2, 13: 2, 14: 3, 19: 4, 24: 5, 29: 6, 33: 6}
    for k, w in exp.items():
        assert cycle_week(float(k)) == w
    assert np.isnan(cycle_week(34.0)) and np.isnan(cycle_week(float("nan")))
    assert [position(w) for w in (2, 4, 6)] == [1, 1, 1]
    assert [position(w) for w in (-1, 1, 3, 5)] == [-1, -1, -1, -1]
    assert position(0) == 0 and position(float("nan")) == 0


def test_unassigned_after_long_gap():
    stm = [date(2024, 1, 3), date(2024, 3, 27)]   # 60 weekdays apart
    assert cycle_k(date(2024, 2, 22), stm) == 36
    assert np.isnan(cycle_week(cycle_k(date(2024, 2, 22), stm)))


def test_prev_weekday():
    assert prev_weekday(date(2024, 2, 5)) == date(2024, 2, 2)
    assert prev_weekday(date(2024, 2, 6)) == date(2024, 2, 5)


def test_trade_timing_sign_and_exclusions():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df = frame_from_bars(bars, STMTS, _dates(bars)).set_index("date")
    d = date(2024, 2, 14)          # k = 10 -> week 2 -> long
    assert df.loc[d, "week"] == 2 and df.loc[d, "side"] == 1
    ny = bars.index.tz_convert(NY)
    e = bars[(pd.Index(ny.date) == date(2024, 2, 13)) & (np.asarray(ny.hour) == 20) & (np.asarray(ny.minute) == 0)].iloc[0]
    x = bars[(pd.Index(ny.date) == d) & (np.asarray(ny.hour) == 16) & (np.asarray(ny.minute) == 55)].iloc[0]
    em, xm = (e["bid_open"] + e["ask_open"]) / 2, (x["bid_open"] + x["ask_open"]) / 2
    assert np.isclose(df.loc[d, "entry_mid"], em) and np.isclose(df.loc[d, "exit_mid"], xm)
    assert np.isclose(df.loc[d, "signed_pips"], (xm - em) / PIP)
    # Monday trading date: entry on Sunday 20:00 NY
    m = date(2024, 2, 19)          # k = 13 -> week 2
    assert df.loc[m, "week"] == 2
    s = bars[(pd.Index(ny.date) == date(2024, 2, 18)) & (np.asarray(ny.hour) == 20) & (np.asarray(ny.minute) == 0)]
    if len(s):
        assert np.isclose(df.loc[m, "entry_mid"], (s.iloc[0]["bid_open"] + s.iloc[0]["ask_open"]) / 2)
    # short week 1
    assert df.loc[date(2024, 2, 7), "side"] == -1 and df.loc[date(2024, 2, 7), "tested"]
    assert np.isclose(df.loc[date(2024, 2, 7), "signed_pips"], -df.loc[date(2024, 2, 7), "long_pips"])
    assert df.loc[S1, "excluded"] == "week0_excluded"
    assert df.loc[date(2024, 1, 10), "excluded"] == "pre_cycle"
    c = counts(df.reset_index())
    assert c["tested"] == int(df["tested"].sum()) and c["week0_excluded"] >= 10


def test_position_independent_of_prices():
    """The position depends only on the calendar: shifting prices changes returns, never sides."""
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    a = frame_from_bars(bars, STMTS, _dates(bars))
    b2 = bars.copy()
    for side in ("bid", "ask"):
        for f in OHLC:
            b2[f"{side}_{f}"] = b2[f"{side}_{f}"] + np.linspace(0, 0.05, len(b2))
    b = frame_from_bars(b2, STMTS, _dates(b2))
    assert (a["side"].to_numpy() == b["side"].to_numpy()).all()


def test_spread_exclusion():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    ny = bars.index.tz_convert(NY)
    sel = (pd.Index(ny.date) == date(2024, 2, 13)) & (np.asarray(ny.hour) == 20) & (np.asarray(ny.minute) < 5)
    b = bars.copy()
    for f in OHLC:
        b.loc[sel, f"ask_{f}"] = b.loc[sel, f"bid_{f}"] + 3 * PIP
    df = frame_from_bars(b, STMTS, _dates(b))
    assert df.set_index("date").loc[date(2024, 2, 14), "excluded"] == "entry_skipped_spread"


def test_decision_rule():
    base = {"n": 600, "mean_pips": 2.0, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.5, 3.5)}
    assert decide_b54(base) == "SIGNAL"
    assert decide_b54({**base, "n": 499}) == "NONE"
    assert decide_b54({**base, "mean_pips": 0.8}) == "WEAK"
    assert decide_b54({**base, "mean_ci95_block_boot": (-0.1, 3.0), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b54({**base, "mean_pips": -1.0}) == "NONE"


def test_no_edge_on_random_walk():
    """Pooled over 4 random-walk years with ~6-week placeholder Wednesdays: no SIGNAL, |mean| small."""
    stm = list(pd.date_range("2024-01-31", "2025-01-31", freq="6W-WED").date)
    parts = []
    for seed in (1, 2, 3, 4):
        bars = synthetic_bars("2024-01-01", "2024-12-31", seed=seed)
        df = frame_from_bars(bars, stm, _dates(bars))
        ev = df[df["tested"]]
        assert len(ev) > 120
        parts.append(ev["signed_pips"].to_numpy())
    res = evaluate(np.concatenate(parts))
    assert res["n"] >= MIN_EVENTS
    assert abs(res["mean_pips"]) < 2.0
    assert decide_b54(res) != "SIGNAL"
