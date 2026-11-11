"""E042 (B46) gold-lag tests; adapted from tests/test_oil_lag.py (E041)."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.gold_lag import (
    ALPHA, BOOT_BLOCK, ENTRY_HM, EXCLUSION_ORDER, EXIT_HM, GOLD, MAX_ABS_G, MIN_BOTH_VALID_SHARE, MIN_EVENTS,
    MIN_MEAN_PIPS, SIGN, SIGNAL_HM, build_days, counts, data_gate, decide_b46, evaluate, events, frame_from_bars,
)
from fxresearch.overnight_reversal import decide_b34


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


def _synthetic(oil_ret, fx_moves, spread=0.00002):
    """oil_ret[i]: log return prev -> D_i (first ignored); fx_moves[i]: pips 16:05 on D_i -> 16:00 on D_i+1."""
    n = len(oil_ret)
    ds = _weekdays(n)
    oil = 50 * np.exp(np.cumsum(oil_ret))
    entry = 1.1 + np.arange(n) * 0.0
    fix = np.r_[1.1, entry[:-1] + np.asarray(fx_moves[:-1]) * PIP]
    return ds, _q(ds, oil, 0.03), _q(ds, fix, spread), _q(ds, entry, spread)


def test_constants_fixed():
    assert GOLD == "xauusd" and SIGN == -1.0
    assert SIGNAL_HM == (16, 0) and ENTRY_HM == (16, 5) and EXIT_HM == (16, 0)
    assert MAX_ABS_G == 0.10 and MIN_BOTH_VALID_SHARE == 0.90
    assert ALPHA == 0.05 and MIN_EVENTS == 500 and MIN_MEAN_PIPS == 1.0 and BOOT_BLOCK == 20
    assert decide_b46 is decide_b34


def test_sign_gold_up_short_eurusd():
    df = build_days(*_synthetic([0, 0.02, -0.01, 0.0], [5.0, 7.0, -4.0, 0.0]))
    assert df.loc[1, "side"] == -1.0 and df.loc[2, "side"] == 1.0
    assert np.isclose(df.loc[1, "signed_pips"], -7.0) and np.isclose(df.loc[2, "signed_pips"], -4.0)
    assert df.loc[0, "excluded"] == "burn_in" and df.loc[3, "excluded"] == "zero_signal"
    assert np.isclose(df.loc[1, "g"], 0.02)
    assert set(df["excluded"].dropna()) <= set(EXCLUSION_ORDER)


def test_trade_runs_1605_to_next_1600_and_last_missing_exit():
    df = build_days(*_synthetic([0, 0.01, 0.02], [5.0, 7.0, 0.0]))
    assert np.allclose(df["move_pips"].iloc[:2], [5.0, 7.0])
    assert df.loc[2, "excluded"] == "missing_exit"


def test_gold_jump_and_missing_no_fallback():
    ds, oq, fx, fin = _synthetic([0, 0.01, 0.15, 0.01, -0.02, 0.01], [1.0] * 6)
    oq = oq.drop(ds[3])
    df = build_days(ds, oq, fx, fin)
    assert df.loc[2, "excluded"] == "gold_jump"
    assert df.loc[3, "excluded"] == "missing_gold_quote"       # D missing
    assert df.loc[4, "excluded"] == "missing_gold_quote"       # prev missing, no fallback
    oq2 = oq.copy()
    oq2.loc[ds[1], ["bid_open", "ask_open"]] = [-1.0, -0.9]   # non-positive quote is invalid
    df2 = build_days(ds, oq2, fx, fin)
    assert df2.loc[1, "excluded"] == "missing_gold_quote"


def test_exclusion_order_spread_and_entry():
    ds, oq, fx, fin = _synthetic([0, 0.01, 0.02, 0.01], [1.0, 2.0, 3.0, 0.0])
    fin.loc[ds[1], "ask_open"] += 3 * PIP
    fin = fin.drop(ds[2])
    df = build_days(ds, oq, fx, fin)
    assert df.loc[1, "excluded"] == "entry_skipped_spread"
    assert df.loc[2, "excluded"] == "missing_entry"
    c = counts(df)
    assert c["entry_skipped_spread"] == 1 and c["missing_entry"] == 1 and c["burn_in"] == 1 and c["tested"] == 0


def test_no_look_ahead_side():
    r = np.random.default_rng(1)
    n = 80
    o, mv = r.normal(0, 0.02, n), list(r.normal(0, 40, n))
    a = build_days(*_synthetic(o, mv))
    o2 = o.copy()
    o2[50:] = r.normal(0, 0.05, n - 50)
    mv2 = mv[:40] + list(r.normal(0, 40, n - 40))
    b = build_days(*_synthetic(o2, mv2))
    assert np.array_equal(a["side"].iloc[:50].fillna(9), b["side"].iloc[:50].fillna(9))


def test_random_walk_no_signal():
    sig = 0
    for seed in range(60):
        r = np.random.default_rng(900 + seed)
        n = 1400
        df = build_days(*_synthetic(r.normal(0, 0.02, n), list(r.normal(0, 50, n))))
        sig += decide_b46(evaluate(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    assert sig / 60 <= 0.07


def test_strong_effect_signal_and_small_sample_none():
    r = np.random.default_rng(3)
    n = 1400
    o = r.normal(0, 0.02, n)
    mv = list(-np.sign(o) * 8.0 + r.normal(0, 50, n))
    df = build_days(*_synthetic(o, mv))
    ev = df[df["tested"]]["signed_pips"]
    assert decide_b46(evaluate(ev)) == "SIGNAL"
    assert decide_b46(evaluate(ev.iloc[:400])) == "NONE"


def test_data_gate():
    ds, oq, fx, fin = _synthetic(np.zeros(41) + 0.001, [1.0] * 41)
    one = pd.DataFrame({"x": [1]})
    assert data_gate(build_days(ds, oq, fx, fin), one)["ok"]
    g = data_gate(build_days(ds, oq.drop(ds[10:14]), fx, fin), one)   # 4 missing -> D 10..14 lack both -> 35/40 < 90%
    assert not g["ok"] and g["dates_both_valid"] == 35 and g["dates_with_prev"] == 40
    g2 = data_gate(build_days(ds, oq.drop(ds[10:13]), fx, fin), one)  # 3 missing -> 36/40 = 90% (boundary passes)
    assert g2["ok"] and g2["dates_both_valid"] == 36
    assert not data_gate(build_days(ds, oq, fx, fin), pd.DataFrame())["ok"]


def test_events_costs():
    df = build_days(*_synthetic([0, 0.01, -0.02, 0.0], [5.0, 7.0, -4.0, 0.0], spread=1.0 * PIP))
    ev = events(df)
    assert len(ev) == 2
    assert np.allclose(ev["net_bidask_pips"], ev["signed_pips"] - 1.0)
    assert np.allclose(ev["net_spec4_pips"], ev["signed_pips"] - 1.2)
    assert np.allclose(ev["net_x1_5_pips"], ev["signed_pips"] - 1.8)


def test_quotes_from_bars_london_time():
    bars = synthetic_bars("2024-03-01", "2024-03-29", seed=5)
    gold = synthetic_bars("2024-03-01", "2024-03-29", seed=6)
    df, dropped = frame_from_bars(bars, gold)
    assert all(d.weekday() < 5 for d in df["date"])
    d = date(2024, 3, 12)
    t_in = pd.Timestamp("2024-03-12 16:05", tz="Europe/London").tz_convert("UTC")
    t_fix = pd.Timestamp("2024-03-12 16:00", tz="Europe/London").tz_convert("UTC")
    row = df[df["date"] == d].iloc[0]
    if t_in in bars.index:
        assert np.isclose(row["entry_mid"], (bars.loc[t_in, "bid_open"] + bars.loc[t_in, "ask_open"]) / 2)
    if t_fix in gold.index:
        assert np.isclose(row["gold_mid"], (gold.loc[t_fix, "bid_open"] + gold.loc[t_fix, "ask_open"]) / 2)


def test_continuation_effect_not_signal():
    """An effect in the opposite (continuation) direction must not pass the pre-registered reversal sign."""
    r = np.random.default_rng(4)
    n = 1400
    o = r.normal(0, 0.01, n)
    df = build_days(*_synthetic(o, list(np.sign(o) * 8.0 + r.normal(0, 50, n))))
    assert decide_b46(evaluate(df[df["tested"]]["signed_pips"])) == "NONE"
