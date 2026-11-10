from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.overreaction_fade import (
    ALT_EXIT_HM, ALT_KS, BOOT_BLOCK, CLOSE_HM, ENTRY_HM, EXIT_HM, K, OPEN_HM, WINDOW, build_days, counts, decide_b24,
    evaluate_b24, frame_from_bars,
)


def _q(dates, mids, spread=0.00002):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates))


def _weekdays(n, start=date(2021, 3, 1)):
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def _synthetic(rs, rets, ds=None, entry_spread=0.00002):
    """Trading dates ds; open mid 1.1, close mid 1.1 + R pips; entry (keyed D+1) 1.2, exit (keyed D+1) 1.2 + ret pips."""
    ds = ds or [start for start in _weekdays(len(rs))]
    nx = [d + timedelta(days=1) for d in ds]
    o = _q(ds, [1.1] * len(ds))
    c = _q(ds, [1.1 + r * PIP for r in rs])
    e = _q(nx, [1.2] * len(ds), entry_spread)
    x = _q(nx, [1.2 + v * PIP for v in rets])
    return ds, o, c, e, x


def test_constants_fixed():
    assert WINDOW == 60 and K == 2.0 and ALT_KS == (1.5, 2.5) and BOOT_BLOCK == 5
    assert OPEN_HM == (17, 0) and CLOSE_HM == (16, 55) and ENTRY_HM == (17, 5) and EXIT_HM == (2, 0) and ALT_EXIT_HM == (3, 0)


def _hist_then(extra_r, extra_ret):
    hist = [float((i % 7) - 3) for i in range(60)]
    ds = _weekdays(60 + len(extra_r))
    return hist, ds, build_days(*_synthetic(hist + extra_r, [0.0] * 60 + extra_ret, ds))


def test_bands_event_and_fade_sign():
    hist, ds, df = _hist_then([40.0, -40.0, 1.0], [5.0, 4.0, 9.0])
    assert df["hist_mean_pips"].iloc[:60].isna().all()
    assert abs(df["hist_mean_pips"].iloc[60] - np.mean(hist)) < 1e-9
    assert abs(df["hist_sd_pips"].iloc[60] - np.std(hist, ddof=1)) < 1e-9
    assert list(df["is_event"].iloc[60:]) == [True, True, False]
    # an up-day is faded (short): next-session rise of 5 -> -5; a down-day is bought: rise of 4 -> +4 (unless Friday-excluded)
    assert abs(df["signed_pips"].iloc[60] + 5.0) < 1e-6 and abs(df["signed_pips"].iloc[61] - 4.0) < 1e-6
    c = counts(df)
    assert c["events"] == 2 and c["events_positive"] == 1 and c["events_negative"] == 1


def test_friday_excluded_but_kept_in_history():
    ds = _weekdays(70)
    fri = next(i for i in range(60, 70) if ds[i].weekday() == 4)
    rs = [float((i % 7) - 3) for i in range(70)]
    rs[fri] = 50.0
    df = build_days(*_synthetic(rs, [3.0] * 70, ds))
    assert bool(df["is_event"].iloc[fri]) and df["excluded"].iloc[fri] == "friday_excluded"
    assert not bool(df["tested"].iloc[fri])
    # the Friday's R enters the next date's history window
    assert abs(df["hist_mean_pips"].iloc[fri + 1] - np.mean(rs[fri + 1 - 60:fri + 1])) < 1e-9
    assert counts(df)["friday_excluded"] == 1


def test_strict_threshold():
    hist = [float((i % 2) * 2 - 1) for i in range(60)]
    sd = np.std(hist, ddof=1)
    ds = _weekdays(61, start=date(2021, 3, 1))
    assert ds[60].weekday() != 4
    below = build_days(*_synthetic(hist + [2 * sd - 1e-4], [0.0] * 61, ds))
    above = build_days(*_synthetic(hist + [2 * sd + 1e-4], [0.0] * 61, ds))
    assert not bool(below["is_event"].iloc[60]) and bool(above["is_event"].iloc[60])


def test_invalid_dates_excluded_from_history():
    ds, o, c, e, x = _synthetic([float(i % 5) for i in range(70)], [0.0] * 70)
    c = c.drop(ds[10])
    df = build_days(ds, o, c, e, x)
    assert not bool(df["valid"].iloc[10]) and df["excluded"].iloc[10] == "invalid_missing_signal_quote"
    assert df["hist_sd_pips"].iloc[:61].isna().all() and not np.isnan(df["hist_sd_pips"].iloc[61])
    assert counts(df)["invalid_missing_signal_quote"] == 1


def test_missing_and_spread_exclusions():
    ds = [d for d in _weekdays(80) if d.weekday() != 4][:63]
    rs = [float(i % 3) for i in range(60)] + [50.0, 50.0, 50.0]
    _, o, c, e, x = _synthetic(rs, [0.0] * 63, ds)
    e = e.drop(ds[60] + timedelta(days=1))
    x = x.drop(ds[61] + timedelta(days=1))
    e.loc[ds[62] + timedelta(days=1), "ask_open"] += 3 * PIP
    df = build_days(ds, o, c, e, x)
    assert list(df["excluded"].iloc[60:]) == ["missing_entry", "missing_exit", "entry_skipped_spread"]
    assert int(df["tested"].sum()) == 0


def test_no_look_ahead():
    r = np.random.default_rng(5)
    a_r = list(r.normal(0, 30, 200))
    a_x = list(r.normal(0, 20, 200))
    ds = _weekdays(200)
    a = build_days(*_synthetic(a_r, a_x, ds))
    b = build_days(*_synthetic(a_r[:120] + [v * 10 for v in a_r[120:]], a_x[:120] + [v + 500 for v in a_x[120:]], ds))
    assert list(a["is_event"].iloc[:120]) == list(b["is_event"].iloc[:120])
    assert np.allclose(a["hist_sd_pips"].iloc[:121].fillna(-1), b["hist_sd_pips"].iloc[:121].fillna(-1))
    # the trade return of date D does not change the event flag of D
    c = build_days(*_synthetic(a_r, a_x[:100] + [v + 500 for v in a_x[100:]], ds))
    assert list(a["is_event"]) == list(c["is_event"])


def test_quotes_from_bars():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df = frame_from_bars(bars)
    d = date(2024, 3, 5)   # Tuesday: trading date starts Monday 17:00 NY, next trading date starts Tuesday 17:00 NY
    row = df[df["date"] == d].iloc[0]

    def mid(ts):
        t = pd.Timestamp(ts, tz="America/New_York").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2
    assert abs(row["open_mid"] - mid("2024-03-04 17:00")) < 1e-12
    assert abs(row["close_mid"] - mid("2024-03-05 16:55")) < 1e-12
    assert abs(row["entry_mid"] - mid("2024-03-05 17:05")) < 1e-12
    assert abs(row["exit_mid"] - mid("2024-03-06 02:00")) < 1e-12
    assert abs(row["exit_alt_mid"] - mid("2024-03-06 03:00")) < 1e-12
    assert abs(row["r_pips"] - (mid("2024-03-05 16:55") - mid("2024-03-04 17:00")) / PIP) < 1e-6


def test_random_walk_no_signal():
    # val-sized sample (~600 dates -> ~25 events). Small-n block bootstrap: measured null SIGNAL rate 0.043 over 300 seeds (R058).
    sig = 0
    ds = _weekdays(600)
    for seed in range(100):
        r = np.random.default_rng(10000 + seed)
        df = build_days(*_synthetic(list(r.standard_t(4, 600) * 40), list(r.normal(0, 15, 600)), ds))
        sig += decide_b24(evaluate_b24(df[df["tested"]]["signed_pips"])) == "SIGNAL"
    assert sig / 100 <= 0.08


def test_strong_fade_gives_signal():
    r = np.random.default_rng(3)
    n = 1500
    ds = _weekdays(n)
    rs = r.normal(0, 40, n)
    rs[::15] *= 4
    rets = np.where(np.abs(rs) > 100, -np.sign(rs) * 15.0, 0.0) + r.normal(0, 15, n)
    df = build_days(*_synthetic(list(rs), list(rets), ds))
    assert decide_b24(evaluate_b24(df[df["tested"]]["signed_pips"])) == "SIGNAL"


def test_insufficient_sample():
    assert evaluate_b24([1.0] * 9).get("note") == "insufficient sample"
    assert decide_b24(evaluate_b24([1.0] * 9)) == "NONE"
