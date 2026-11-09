from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.london_momentum import (
    ALT_SIGNAL_END_HM, BOOT_BLOCK, ENTRY_HM, EXIT_HM, SIGNAL_END_HM, SIGNAL_START_HM, build_days, counts, decide_b22,
    evaluate_b22, frame_from_bars, london_quotes, slope,
)


def _q(dates, mids, spread=0.00002):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates, name="ldn_date"))


def _synthetic(r1, last, start=date(2015, 1, 5)):
    ds = [start + timedelta(days=i) for i in range(len(r1))]
    s = [1.1] * len(ds)
    e = [1.1 + r * PIP for r in r1]
    i = [1.2] * len(ds)
    o = [1.2 + x * PIP for x in last]
    return ds, _q(ds, s), _q(ds, e), _q(ds, i), _q(ds, o)


def test_constants_fixed():
    assert SIGNAL_START_HM == (8, 0) and SIGNAL_END_HM == (8, 30)
    assert ENTRY_HM == (15, 25) and EXIT_HM == (15, 55) and ALT_SIGNAL_END_HM == (9, 0)
    assert BOOT_BLOCK == 20


def test_sign_and_return():
    df = build_days(*_synthetic([5.0, -3.0], [2.0, 4.0]))
    assert abs(df["signed_pips"].iloc[0] - 2.0) < 1e-6
    assert abs(df["signed_pips"].iloc[1] + 4.0) < 1e-6
    assert df["tested"].all()


def test_exclusions_in_order():
    ds, s, e, i, o = _synthetic([5.0, 0.0, 5.0, 5.0, 5.0, 5.0], [1.0] * 6)
    s = s.drop(ds[0])
    i = i.drop(ds[2])
    o = o.drop(ds[3])
    i.loc[ds[4], "ask_open"] += 3 * PIP
    o = o.drop(ds[1])  # zero signal takes precedence over missing exit
    df = build_days(ds, s, e, i, o)
    assert list(df["excluded"].iloc[:5]) == ["invalid_missing_signal_quote", "zero_signal", "missing_entry", "missing_exit",
                                             "entry_skipped_spread"]
    assert pd.isna(df["excluded"].iloc[5])
    c = counts(df)
    assert c["events_tested"] == 1 and c["zero_signal"] == 1 and c["entry_skipped_spread"] == 1


def test_no_look_ahead_side():
    r = np.random.default_rng(1)
    r1 = list(r.normal(0, 8, 100))
    a = build_days(*_synthetic(r1, list(r.normal(0, 7, 100))))
    b = build_days(*_synthetic(r1, list(r.normal(0, 7, 100) + 50)))
    assert list(a["side"]) == list(b["side"])


def test_quotes_from_bars_london_time():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df = frame_from_bars(bars)
    d = date(2024, 3, 5)
    row = df[df["date"] == d].iloc[0]

    def mid(hm):
        t = pd.Timestamp(f"2024-03-05 {hm}", tz="Europe/London").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2
    assert abs(row["s_mid"] - mid("08:00")) < 1e-12
    assert abs(row["e_mid"] - mid("08:30")) < 1e-12
    assert abs(row["entry_mid"] - mid("15:25")) < 1e-12
    assert abs(row["exit_mid"] - mid("15:55")) < 1e-12
    assert abs(row["signed_pips"] - np.sign(row["r1_pips"]) * (mid("15:55") - mid("15:25")) / PIP) < 1e-6


def test_dst_mismatch_flag():
    # 2024-03-12: US on EDT, UK still GMT -> London 4 h ahead; 2024-03-05: 5 h
    df = build_days(*_synthetic([1.0] * 10, [0.0] * 10, start=date(2024, 3, 4)))
    f = dict(zip(df["date"], df["dst_mismatch"]))
    assert f[date(2024, 3, 12)] and not f[date(2024, 3, 5)]
    q = london_quotes(synthetic_bars("2024-03-01", "2024-03-20"), 15, 25)
    assert date(2024, 3, 12) in q.index


def test_random_walk_no_signal():
    sig = 0
    for seed in range(40):
        r = np.random.default_rng(300 + seed)
        n = 1500
        df = build_days(*_synthetic(list(r.normal(0, 8, n)), list(r.normal(0, 7, n))))
        sig += decide_b22(evaluate_b22(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    assert sig / 40 <= 0.10


def test_strong_momentum_gives_signal_and_sub_pip_is_not_signal():
    r = np.random.default_rng(3)
    n = 1500
    r1 = r.normal(0, 8, n)
    df = build_days(*_synthetic(list(r1), list(np.sign(r1) * 2.0 + r.normal(0, 7, n))))
    assert decide_b22(evaluate_b22(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    df2 = build_days(*_synthetic(list(r1), list(np.sign(r1) * 0.6 + r.normal(0, 3, n))))
    assert decide_b22(evaluate_b22(df2[df2["tested"]]["signed_pips"])) == "WEAK"


def test_month_end_and_slope():
    df = build_days(*_synthetic([1.0, -2.0, 3.0, 4.0], [1.5, -2.0, 3.0, 4.2], start=date(2015, 1, 29)))
    me = dict(zip(df["date"], df["month_end"]))
    assert me[date(2015, 1, 31)] and not me[date(2015, 1, 30)] and me[date(2015, 2, 1)]
    assert slope(df)["n"] == 4 and slope(df)["slope"] > 0.9
