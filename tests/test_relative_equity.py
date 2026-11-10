from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.overnight_reversal import decide_b32
from fxresearch.relative_equity import (
    ALPHA, BOOT_BLOCK, ENTRY_HM, EXIT_HM, MAX_MISSING_INDEX_SHARE, MIN_EVENTS, MIN_MEAN_PIPS, SIGNAL_HM, SMOOTH_N,
    arm_events, build_days, counts, data_gate, decide_b35, decide_b36, evaluate, frame_from_bars,
)


def _q(dates, mids, spread=0.0):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates))


def _weekdays(n, start=date(2015, 1, 5)):
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def _synthetic(eu_ret, us_ret, fx_moves, spread=0.00002):
    """eu_ret/us_ret: log returns from prev date to D (first ignored); fx_moves[i]: pips from 16:05 on D_i to 16:00 on D_i+1."""
    n = len(eu_ret)
    ds = _weekdays(n)
    eu = 3000 * np.exp(np.cumsum(eu_ret))
    us = 2500 * np.exp(np.cumsum(us_ret))
    entry = 1.1 + np.arange(n) * 0.0                      # 16:05 quote on D
    fix = np.r_[1.1, entry[:-1] + np.asarray(fx_moves[:-1]) * PIP]  # 16:00 quote on D = entry(D-1) + move(D-1)
    return ds, _q(ds, eu), _q(ds, us), _q(ds, fix, spread), _q(ds, entry, spread)


def test_constants_fixed():
    assert SIGNAL_HM == (16, 0) and ENTRY_HM == (16, 5) and EXIT_HM == (16, 0)
    assert SMOOTH_N == 20 and BOOT_BLOCK == 20 and ALPHA == 0.025 and MIN_EVENTS == 500 and MIN_MEAN_PIPS == 1.0
    assert MAX_MISSING_INDEX_SHARE == 0.10
    assert decide_b35 is decide_b32 and decide_b36 is decide_b32


def test_b35_sign_us_outperforms_long():
    # date 1: EU +1%, US +3% -> S1 < 0 -> long; date 2: EU +2%, US 0 -> S1 > 0 -> short
    df = build_days(*_synthetic([0, 0.01, 0.02, 0.0], [0, 0.03, 0.0, 0.0], [5.0, 7.0, -4.0, 0.0]))
    assert df.loc[1, "b35_side"] == 1.0 and df.loc[2, "b35_side"] == -1.0
    assert np.isclose(df.loc[1, "b35_signed_pips"], 7.0) and np.isclose(df.loc[2, "b35_signed_pips"], 4.0)
    assert df.loc[0, "b35_excluded"] == "burn_in"
    assert df.loc[3, "b35_excluded"] == "zero_signal"


def test_trade_runs_1605_to_next_1600():
    df = build_days(*_synthetic([0, 0.01, 0.02], [0, 0.0, 0.0], [5.0, 7.0, 0.0]))
    assert np.allclose(df["move_pips"].iloc[:2], [5.0, 7.0])
    assert df.loc[2, "b35_excluded"] == "missing_exit"          # last date has no next date


def test_b36_burn_in_and_window():
    n = 60
    r = np.random.default_rng(0)
    eu, us = r.normal(0, 0.01, n), r.normal(0, 0.01, n)
    df = build_days(*_synthetic(eu, us, list(r.normal(0, 40, n))))
    assert (df["b36_excluded"].iloc[:SMOOTH_N] == "burn_in").all()
    assert not df["b36_burn_in"].iloc[SMOOTH_N:].any()
    i = 30
    expect = (np.sum(eu[i - SMOOTH_N + 1:i + 1]) - np.sum(us[i - SMOOTH_N + 1:i + 1]))
    assert np.isclose(df.loc[i, "b36_s"], expect)


def test_missing_index_no_fallback():
    ds, eu_q, us_q, fx, fin = _synthetic([0, 0.01, 0.02, 0.01, 0.0], [0, 0.0, 0.0, 0.03, 0.0], [1.0, 2.0, 3.0, 4.0, 0.0])
    eu_q = eu_q.drop(ds[1])
    df = build_days(ds, eu_q, us_q, fx, fin)
    assert df.loc[1, "b35_excluded"] == "missing_index_quote"   # D itself missing
    assert df.loc[2, "b35_excluded"] == "missing_index_quote"   # prev missing, no fallback
    assert df.loc[3, "b35_tested"]


def test_exclusion_order_spread_and_entry():
    ds, eu_q, us_q, fx, fin = _synthetic([0, 0.01, 0.02, 0.01], [0, 0.0, 0.0, 0.03], [1.0, 2.0, 3.0, 0.0])
    fin.loc[ds[1], "ask_open"] += 3 * PIP
    fin = fin.drop(ds[2])
    df = build_days(ds, eu_q, us_q, fx, fin)
    assert df.loc[1, "b35_excluded"] == "entry_skipped_spread"
    assert df.loc[2, "b35_excluded"] == "missing_entry"
    c = counts(df)
    assert c["b35_entry_skipped_spread"] == 1 and c["b35_missing_entry"] == 1 and c["b35_burn_in"] == 1


def test_no_look_ahead_side():
    r = np.random.default_rng(1)
    n = 80
    eu, us, mv = r.normal(0, 0.01, n), r.normal(0, 0.01, n), list(r.normal(0, 40, n))
    a = build_days(*_synthetic(eu, us, mv))
    eu2, us2 = eu.copy(), us.copy()
    eu2[50:] = r.normal(0, 0.05, n - 50)
    us2[50:] = r.normal(0, 0.05, n - 50)
    mv2 = mv[:40] + list(r.normal(0, 40, n - 40))
    b = build_days(*_synthetic(eu2, us2, mv2))
    for arm in ("b35", "b36"):
        assert np.array_equal(a[f"{arm}_side"].iloc[:50].fillna(9), b[f"{arm}_side"].iloc[:50].fillna(9))


def test_random_walk_no_signal():
    sig = 0
    for seed in range(40):
        r = np.random.default_rng(700 + seed)
        n = 1400
        df = build_days(*_synthetic(r.normal(0, 0.01, n), r.normal(0, 0.01, n), list(r.normal(0, 50, n))))
        for arm in ("b35", "b36"):
            sig += decide_b35(evaluate(df[df[f"{arm}_tested"]][f"{arm}_signed_pips"])) == "SIGNAL"
    assert sig / 80 <= 0.05


def test_strong_effect_signal_and_small_sample_none():
    r = np.random.default_rng(3)
    n = 1400
    eu, us = r.normal(0, 0.01, n), r.normal(0, 0.01, n)
    s1 = eu - us                                   # S1(D) for D >= 1
    # inject: move after D follows -sign(S1(D))
    mv = list(-np.sign(s1) * 8.0 + r.normal(0, 50, n))
    df = build_days(*_synthetic(eu, us, mv))
    ev = df[df["b35_tested"]]["b35_signed_pips"]
    assert decide_b35(evaluate(ev)) == "SIGNAL"
    assert decide_b35(evaluate(ev.iloc[:400])) == "NONE"


def test_data_gate():
    ds, eu_q, us_q, fx, fin = _synthetic(np.zeros(40), np.zeros(40) + 0.001, [1.0] * 40)
    df = build_days(ds, eu_q, us_q, fx, fin)
    one = pd.DataFrame({"x": [1]})
    assert data_gate(df, one, one)["ok"]
    df2 = build_days(ds, eu_q.drop(ds[:5]), us_q, fx, fin)
    g = data_gate(df2, one, one)
    assert not g["ok"] and g["dates_missing_index_quote"] == 5
    assert not data_gate(df, pd.DataFrame(), one)["ok"]


def test_arm_events_costs():
    df = build_days(*_synthetic([0, 0.01, 0.02, 0.0], [0, 0.03, 0.0, 0.0], [5.0, 7.0, -4.0, 0.0], spread=1.0 * PIP))
    ev = arm_events(df, "b35")
    assert np.allclose(ev["net_bidask_pips"], ev["signed_pips"] - 1.0)
    assert np.allclose(ev["net_spec4_pips"], ev["signed_pips"] - 1.2)
    assert np.allclose(ev["net_x1_5_pips"], ev["signed_pips"] - 1.8)


def test_quotes_from_bars_london_time():
    bars = synthetic_bars("2024-03-01", "2024-03-29", seed=5)
    eu = synthetic_bars("2024-03-01", "2024-03-29", seed=6)
    us = synthetic_bars("2024-03-01", "2024-03-29", seed=8)
    df, dropped = frame_from_bars(bars, eu, us)
    assert all(d.weekday() < 5 for d in df["date"])
    d = date(2024, 3, 12)
    t_in = pd.Timestamp("2024-03-12 16:05", tz="Europe/London").tz_convert("UTC")
    t_fix = pd.Timestamp("2024-03-12 16:00", tz="Europe/London").tz_convert("UTC")
    row = df[df["date"] == d].iloc[0]
    if t_in in bars.index:
        assert np.isclose(row["entry_mid"], (bars.loc[t_in, "bid_open"] + bars.loc[t_in, "ask_open"]) / 2)
    if t_fix in eu.index:
        assert np.isclose(row["eu_mid"], (eu.loc[t_fix, "bid_open"] + eu.loc[t_fix, "ask_open"]) / 2)
