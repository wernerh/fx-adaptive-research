from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.roll_momentum import (
    ALPHA, BOOT_BLOCK, ENTRY_HM, EXIT_HM, MIN_EVENTS, MIN_MEAN_PIPS, START_HM, build_days, counts, decide_b38, evaluate,
    events, frame_from_bars, reversal_flag, weekday_dates,
)
from fxresearch.vol_state_fix import cost_summary


def _q(dates, mids, spread=0.00002):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates))


def _synthetic(r1, r2, start=date(2015, 1, 5)):
    ds = [start + timedelta(days=i) for i in range(len(r1))]
    s = [1.1] * len(ds)
    e = [1.1 + a * PIP for a in r1]
    x = [1.1 + (a + b) * PIP for a, b in zip(r1, r2)]
    return ds, _q(ds, s), _q(ds, e), _q(ds, x)


def test_constants_fixed():
    assert START_HM == (17, 0) and ENTRY_HM == (16, 25) and EXIT_HM == (16, 55)
    assert BOOT_BLOCK == 20 and ALPHA == 0.05 and MIN_EVENTS == 500 and MIN_MEAN_PIPS == 1.0


def test_follows_sign_of_r1():
    df = build_days(*_synthetic([5.0, -3.0], [2.0, 4.0]))
    assert list(df["side"]) == [1.0, -1.0]
    assert np.allclose(df["signed_pips"], [2.0, -4.0])
    assert np.allclose(df["r1_pips"], [5.0, -3.0]) and np.allclose(df["r2_pips"], [2.0, 4.0])


def test_exclusions_in_order():
    ds, s, e, x = _synthetic([5.0, 5.0, 0.0, 5.0, 5.0, 5.0], [1.0] * 6)
    s = s.drop(ds[0])
    e = e.drop(ds[1])
    x = x.drop([ds[2], ds[3]])          # ds[2]: zero signal takes precedence over missing exit
    e.loc[ds[4], "ask_open"] += 3 * PIP
    df = build_days(ds, s, e, x)
    assert list(df["excluded"].iloc[:5]) == ["missing_start", "missing_entry", "zero_signal", "missing_exit",
                                             "entry_skipped_spread"]
    assert pd.isna(df["excluded"].iloc[5])
    c = counts(df, 2)
    assert c["tested"] == 1 and c["weekend_trading_dates_dropped"] == 2 and c["missing_exit"] == 1


def test_no_look_ahead_side():
    r = np.random.default_rng(1)
    r1 = list(r.normal(0, 25, 100))
    a = build_days(*_synthetic(r1, list(r.normal(0, 6, 100))))
    b = build_days(*_synthetic(r1, list(r.normal(0, 6, 100) + 50)))
    assert list(a["side"]) == list(b["side"])


def test_quotes_from_bars_ny_time_and_next_date_reading():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df, _ = frame_from_bars(bars)
    assert all(d.weekday() < 5 for d in df["date"])

    def mid(ts):
        t = pd.Timestamp(ts, tz="America/New_York").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2
    row = df[df["date"] == date(2024, 3, 5)].iloc[0]          # Tuesday: starts Monday 17:00 NY
    assert abs(row["start_mid"] - mid("2024-03-04 17:00")) < 1e-12
    assert abs(row["entry_mid"] - mid("2024-03-05 16:25")) < 1e-12
    assert abs(row["exit_mid"] - mid("2024-03-05 16:55")) < 1e-12
    assert abs(row["next_open_mid"] - mid("2024-03-05 17:05")) < 1e-12
    assert abs(row["next_entry_mid"] - mid("2024-03-06 16:25")) < 1e-12


def test_weekday_dates_drop_weekends():
    bars = synthetic_bars("2024-01-01", "2024-01-31")
    ds, n_we = weekday_dates(bars)
    assert all(d.weekday() < 5 for d in ds) and n_we >= 0


def test_random_walk_no_signal():
    sig = 0
    for seed in range(60):
        r = np.random.default_rng(700 + seed)
        n = 1500
        df = build_days(*_synthetic(list(r.normal(0, 25, n)), list(r.normal(0, 6, n))))
        sig += decide_b38(evaluate(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    assert sig / 60 <= 0.05


def test_strong_momentum_signal_small_sample_none_and_rules():
    r = np.random.default_rng(3)
    n = 1500
    r1 = r.normal(0, 25, n)
    df = build_days(*_synthetic(list(r1), list(np.sign(r1) * 1.6 + r.normal(0, 6, n))))
    assert decide_b38(evaluate(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    assert decide_b38(evaluate(df[df["tested"]]["signed_pips"].iloc[:400])) == "NONE"
    base = {"n": 600, "mean_pips": 1.2, "binom_p_one_sided": 0.04, "mean_ci95_block_boot": (0.1, 2.0)}
    assert decide_b38(base) == "SIGNAL"
    assert decide_b38({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b38({**base, "binom_p_one_sided": 0.2}) == "WEAK"   # CI lower > 0 alone -> WEAK
    assert decide_b38({**base, "binom_p_one_sided": 0.2, "mean_ci95_block_boot": (-0.1, 2.0)}) == "NONE"
    assert decide_b38({"n": 0, "note": "no events"}) == "NONE"
    assert reversal_flag({"mean_pips": -1.0, "mean_ci95_block_boot": (-2.0, -0.1)})


def test_events_costs():
    df = build_days(*_synthetic([5.0, -3.0], [2.0, -4.0]))
    c = cost_summary(events(df))
    assert c["n"] == 2 and c["mean_net_spec4_pips"] < c["mean_signed_mid_pips"]
    assert c["mean_net_costs_x1_5_pips"] < c["mean_net_spec4_pips"]
