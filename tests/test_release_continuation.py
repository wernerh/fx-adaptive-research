from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.release_continuation import (
    ALT_EXITS_HM, EXIT_HM, JUMP_END_HM, JUMP_START_HM, PCTL, WINDOW, build_days, counts, decide_b21, frame_from_bars,
)
from fxresearch.vol_state_fix import evaluate


def _q(dates, mids, spread=0.00002):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates, name="ny_date"))


def _synthetic(jumps, rets, start=date(2015, 1, 5)):
    """Dates with 08:30 mid 1.1, 08:45 mid 1.1 + J pips, 10:45 mid = 08:45 + R pips."""
    ds = [start + timedelta(days=i) for i in range(len(jumps))]
    s = [1.1] * len(ds)
    e = [1.1 + j * PIP for j in jumps]
    x = [ei + r * PIP for ei, r in zip(e, rets)]
    return ds, _q(ds, s), _q(ds, e), _q(ds, x)


def test_constants_fixed():
    assert WINDOW == 60 and PCTL == 90
    assert JUMP_START_HM == (8, 30) and JUMP_END_HM == (8, 45) and EXIT_HM == (10, 45)
    assert ALT_EXITS_HM == {"exit_0930": (9, 30), "exit_1200": (12, 0)}


def test_event_threshold_and_sign():
    jumps = [float(i % 10 + 1) for i in range(60)] + [-50.0, 3.0]
    rets = [0.0] * 60 + [-8.0, 5.0]
    df = build_days(*_synthetic(jumps, rets))
    assert df["threshold_pips"].iloc[:60].isna().all()
    assert bool(df["is_event"].iloc[60]) and not bool(df["is_event"].iloc[61])
    # negative jump -> short; price falls 8 pips -> +8 signed
    assert abs(df["signed_pips"].iloc[60] - 8.0) < 1e-6
    assert abs(df["threshold_pips"].iloc[60] - np.percentile([float(i % 10 + 1) for i in range(60)], 90)) < 1e-9


def test_invalid_dates_excluded_from_history():
    ds, s, e, x = _synthetic([float(i % 10 + 1) for i in range(70)], [0.0] * 70)
    s = s.drop(ds[10])
    df = build_days(ds, s, e, x)
    assert not bool(df["valid"].iloc[10]) and df["excluded"].iloc[10] == "invalid_missing_jump_quote"
    # 60 valid dates needed: the first threshold appears at position 61
    assert df["threshold_pips"].iloc[:61].isna().all() and not np.isnan(df["threshold_pips"].iloc[61])
    assert counts(df)["invalid_missing_jump_quote"] == 1


def test_spread_and_missing_exit_exclusions():
    ds, s, e, x = _synthetic([1.0] * 60 + [40.0, 40.0], [0.0] * 62)
    e.loc[ds[60], "ask_open"] += 3 * PIP
    x = x.drop(ds[61])
    df = build_days(ds, s, e, x)
    assert df["excluded"].iloc[60] == "entry_skipped_spread" and df["excluded"].iloc[61] == "missing_exit"
    assert int(df["tested"].sum()) == 0


def test_no_look_ahead():
    r = np.random.default_rng(5)
    j = list(r.normal(0, 5, 200))
    rt = list(r.normal(0, 20, 200))
    a = build_days(*_synthetic(j, rt))
    b = build_days(*_synthetic(j[:120] + [v * 10 for v in j[120:]], rt[:120] + [v + 500 for v in rt[120:]]))
    assert list(a["is_event"].iloc[:120]) == list(b["is_event"].iloc[:120])
    assert np.allclose(a["threshold_pips"].iloc[:121].fillna(-1), b["threshold_pips"].iloc[:121].fillna(-1))


def test_quotes_from_bars():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df = frame_from_bars(bars)
    d = date(2024, 3, 5)
    row = df[df["date"] == d].iloc[0]

    def mid(hm):
        t = pd.Timestamp(f"2024-03-05 {hm}", tz="America/New_York").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2
    assert abs(row["start_mid"] - mid("08:30")) < 1e-12
    assert abs(row["entry_mid"] - mid("08:45")) < 1e-12
    assert abs(row["exit_mid"] - mid("10:45")) < 1e-12
    assert abs(row["jump_pips"] - (mid("08:45") - mid("08:30")) / PIP) < 1e-6
    assert abs(row["signed_pips"] - np.sign(row["jump_pips"]) * (mid("10:45") - mid("08:45")) / PIP) < 1e-6


def test_random_walk_no_signal():
    sig = 0
    for seed in range(40):
        r = np.random.default_rng(200 + seed)
        n = 1500
        df = build_days(*_synthetic(list(r.normal(0, 5, n)), list(r.normal(0, 20, n))))
        sig += decide_b21(evaluate(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    assert sig / 40 <= 0.10


def test_strong_continuation_gives_signal():
    r = np.random.default_rng(3)
    n = 1500
    j = r.normal(0, 5, n)
    rt = np.sign(j) * np.where(np.abs(j) > 8, 8.0, 0.0) + r.normal(0, 20, n)
    df = build_days(*_synthetic(list(j), list(rt)))
    assert decide_b21(evaluate(df[df["tested"]]["signed_pips"])) == "SIGNAL"


def test_first_friday_flag():
    df = build_days(*_synthetic([1.0] * 10, [0.0] * 10, start=date(2015, 1, 1)))
    ff = dict(zip(df["date"], df["first_friday"]))
    assert ff[date(2015, 1, 2)] and not ff[date(2015, 1, 9)]
