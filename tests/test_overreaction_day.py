from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.overreaction_day import (
    ALT_KS, BOOT_BLOCK, ENTRY_HM, EXIT_HM, K, OPEN_HM, WINDOW, build_days, counts, decide_b23, evaluate_b23, frame_from_bars,
)


def _q(dates, mids, spread=0.00002):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates))


def _synthetic(rs, rets, start=date(2015, 1, 5)):
    """Dates with open mid 1.1, 12:00 mid 1.1 + r pips, 16:30 mid = 12:00 + R pips."""
    ds = [start + timedelta(days=i) for i in range(len(rs))]
    o = [1.1] * len(ds)
    e = [1.1 + r * PIP for r in rs]
    x = [ei + R * PIP for ei, R in zip(e, rets)]
    return ds, _q(ds, o), _q(ds, e), _q(ds, x)


def test_constants_fixed():
    assert WINDOW == 60 and K == 2.0 and ALT_KS == (1.5, 2.5) and BOOT_BLOCK == 5
    assert OPEN_HM == (17, 0) and ENTRY_HM == (12, 0) and EXIT_HM == (16, 30)


def test_bands_event_and_sign():
    hist = [float((i % 7) - 3) for i in range(60)]
    rs = hist + [-40.0, 40.0, 1.0]
    rets = [0.0] * 60 + [-6.0, -5.0, 9.0]
    df = build_days(*_synthetic(rs, rets))
    assert df["hist_mean_pips"].iloc[:60].isna().all()
    assert abs(df["hist_mean_pips"].iloc[60] - np.mean(hist)) < 1e-9
    assert abs(df["hist_sd_pips"].iloc[60] - np.std(hist, ddof=1)) < 1e-9
    assert list(df["is_event"].iloc[60:]) == [True, True, False]
    # negative overreaction -> short; price falls 6 -> +6. positive -> long; price falls 5 -> -5
    assert abs(df["signed_pips"].iloc[60] - 6.0) < 1e-6 and abs(df["signed_pips"].iloc[61] + 5.0) < 1e-6
    c = counts(df)
    assert c["events"] == 2 and c["events_positive"] == 1 and c["events_negative"] == 1


def test_strict_threshold():
    hist = [float((i % 2) * 2 - 1) for i in range(60)]   # mean 0, sd ~1.008
    sd = np.std(hist, ddof=1)
    below = build_days(*_synthetic(hist + [2 * sd - 1e-4], [0.0] * 61))
    above = build_days(*_synthetic(hist + [2 * sd + 1e-4], [0.0] * 61))
    assert not bool(below["is_event"].iloc[60]) and bool(above["is_event"].iloc[60])


def test_invalid_dates_excluded_from_history():
    ds, o, e, x = _synthetic([float(i % 5) for i in range(70)], [0.0] * 70)
    o = o.drop(ds[10])
    df = build_days(ds, o, e, x)
    assert not bool(df["valid"].iloc[10]) and df["excluded"].iloc[10] == "invalid_missing_signal_quote"
    assert df["hist_sd_pips"].iloc[:61].isna().all() and not np.isnan(df["hist_sd_pips"].iloc[61])
    assert counts(df)["invalid_missing_signal_quote"] == 1


def test_spread_and_missing_exit_exclusions():
    ds, o, e, x = _synthetic([float(i % 3) for i in range(60)] + [50.0, 50.0], [0.0] * 62)
    e.loc[ds[60], "ask_open"] += 3 * PIP
    x = x.drop(ds[61])
    df = build_days(ds, o, e, x)
    assert df["excluded"].iloc[60] == "entry_skipped_spread" and df["excluded"].iloc[61] == "missing_exit"
    assert int(df["tested"].sum()) == 0


def test_no_look_ahead():
    r = np.random.default_rng(5)
    a_r = list(r.normal(0, 30, 200))
    a_x = list(r.normal(0, 20, 200))
    a = build_days(*_synthetic(a_r, a_x))
    b = build_days(*_synthetic(a_r[:120] + [v * 10 for v in a_r[120:]], a_x[:120] + [v + 500 for v in a_x[120:]]))
    assert list(a["is_event"].iloc[:120]) == list(b["is_event"].iloc[:120])
    assert np.allclose(a["hist_sd_pips"].iloc[:121].fillna(-1), b["hist_sd_pips"].iloc[:121].fillna(-1))


def test_quotes_from_bars():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df = frame_from_bars(bars)
    d = date(2024, 3, 5)   # Tuesday: trading date starts Monday 17:00 NY
    row = df[df["date"] == d].iloc[0]

    def mid(ts):
        t = pd.Timestamp(ts, tz="America/New_York").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2
    assert abs(row["open_mid"] - mid("2024-03-04 17:00")) < 1e-12
    assert abs(row["entry_mid"] - mid("2024-03-05 12:00")) < 1e-12
    assert abs(row["exit_mid"] - mid("2024-03-05 16:30")) < 1e-12
    assert abs(row["r_pips"] - (mid("2024-03-05 12:00") - mid("2024-03-04 17:00")) / PIP) < 1e-6


def test_random_walk_no_signal():
    sig = 0
    for seed in range(40):
        r = np.random.default_rng(300 + seed)
        n = 1500
        df = build_days(*_synthetic(list(r.standard_t(4, n) * 25), list(r.normal(0, 20, n))))
        sig += decide_b23(evaluate_b23(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    assert sig / 40 <= 0.10


def test_strong_continuation_gives_signal():
    r = np.random.default_rng(3)
    n = 1500
    rs = r.normal(0, 25, n)
    rs[::20] *= 4                      # ~75 overreaction days
    rets = np.where(np.abs(rs) > 60, np.sign(rs) * 15.0, 0.0) + r.normal(0, 20, n)
    df = build_days(*_synthetic(list(rs), list(rets)))
    assert decide_b23(evaluate_b23(df[df["tested"]]["signed_pips"])) == "SIGNAL"


def test_insufficient_sample():
    assert evaluate_b23([1.0] * 9).get("note") == "insufficient sample"
    assert decide_b23(evaluate_b23([1.0] * 9)) == "NONE"
