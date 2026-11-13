"""E048 (B58) 1h swing-level breakout + 5m break-and-retest: hourly levels, lookback floor, time window, retest / failed break /
no retest, short mirror, first setup per date, signal stamp and fill, no look-ahead, decision rule, no edge on random walks."""
import numpy as np
import pandas as pd

from fxresearch.breakout_retest import (HORIZON_MIN, MIN_EVENTS, breakout_close_events, decide_b58, detect_events,
                                        evaluate, find_breakouts, hourly_levels)
from fxresearch.data import synthetic_bars
from fxresearch.round_numbers import build_trades

HALF = 0.00001
BASE = 1.1000
DAY = pd.Timestamp("2019-03-06", tz="UTC")   # Wednesday; London = UTC, NY = UTC-5 (before US DST 2019-03-10)


def _frame(idx, c, h=None, lo=None):
    c = np.asarray(c, float)
    o = np.concatenate([[c[0]], c[:-1]])
    hh = np.maximum(np.maximum(o, c), np.asarray(h, float) if h is not None else c)
    ll = np.minimum(np.minimum(o, c), np.asarray(lo, float) if lo is not None else c)
    df = pd.DataFrame(index=pd.DatetimeIndex(idx, name="ts"))
    for f, v in (("open", o), ("high", hh), ("low", ll), ("close", c)):
        df[f"bid_{f}"] = v - HALF
        df[f"ask_{f}"] = v + HALF
    return df


def _scenario(after, start_hour=9, rng_hi=1.1010, rng_lo=1.0990):
    """Flat 1.1000 from DAY-1 00:00 to DAY start_hour:00 (range rng_hi/rng_lo touched once), then the 1-minute closes `after`
    starting at DAY start_hour:00 (the breakout hour is the first 60 of them), then flat at the last price for 4 hours."""
    t0 = DAY - pd.Timedelta(days=1)
    n_pre = int((DAY + pd.Timedelta(hours=start_hour) - t0) / pd.Timedelta(minutes=1))
    pre = np.full(n_pre, BASE)
    h, lo = pre.copy(), pre.copy()
    h[-300], lo[-200] = rng_hi, rng_lo
    after = np.asarray(after, float)
    tail = np.full(240, after[-1])
    c = np.concatenate([pre, after, tail])
    hh = np.concatenate([h, after, tail])
    ll = np.concatenate([lo, after, tail])
    idx = pd.date_range(t0, periods=len(c), freq="1min")
    return _frame(idx, c, hh, ll)


def _breakout_hour(close=1.1020):
    return np.linspace(BASE, close, 60)


def test_constants():
    assert MIN_EVENTS == 300 and HORIZON_MIN == 60


def test_hourly_levels():
    b = _scenario(np.concatenate([_breakout_hour(), np.full(60, 1.1020)]))
    g = hourly_levels(b)
    k = g.loc[DAY + pd.Timedelta(hours=9)]
    assert k["valid"] and k["n_valid_lb"] == 24
    assert k["R"] == round(2 * 1.1010 * 1e5) and k["S"] == round(2 * 1.0990 * 1e5)
    assert k["close"] == round(2 * 1.1020 * 1e5)


def test_long_retest_signal_stamp_and_fill():
    # after the breakout hour: 10 min at 1.1020, then dip to 1.10105 (within 1 pip of L = 1.1010) and close 1.1015
    post = np.concatenate([np.full(10, 1.1020), [1.10105, 1.1015, 1.1015, 1.1015, 1.1015], np.full(60, 1.1030)])
    b = _scenario(np.concatenate([_breakout_hour(), post]))
    ev, res, cnt = detect_events(b)
    assert cnt["setups"] == 1 and cnt["retest"] == 1
    assert len(ev) == 1 and ev.loc[0, "direction"] == 1 and abs(ev.loc[0, "level"] - 1.1010) < 1e-9
    # retest bucket = 10:10-10:15; stamp 10:14, fill at 10:15
    assert ev.loc[0, "ts"] == DAY + pd.Timedelta(hours=10, minutes=14)
    tr, _ = build_trades(b, ev, horizon=HORIZON_MIN, descriptive_horizons=())
    assert tr.loc[0, "entry_ts"] == DAY + pd.Timedelta(hours=10, minutes=15)
    assert tr.loc[0, "signed_pips"] > 0


def test_retest_too_far_is_not_a_retest_and_close_below_cancels():
    # dip to 1.10115 (1.5 pips above L): not a retest; later a 5m bar closes at 1.1008 <= L -> failed break
    post = np.concatenate([np.full(10, 1.1020), [1.10115, 1.1015, 1.1015, 1.1015, 1.1015], np.full(10, 1.1020),
                           np.full(5, 1.1008), np.full(30, 1.1015)])
    b = _scenario(np.concatenate([_breakout_hour(), post]))
    ev, res, cnt = detect_events(b)
    assert len(ev) == 0 and cnt["failed_break"] == 1 and cnt["retest"] == 0


def test_no_retest_when_price_runs_away():
    b = _scenario(np.concatenate([_breakout_hour(), np.linspace(1.1020, 1.1060, 150)]))
    ev, res, cnt = detect_events(b)
    assert len(ev) == 0 and cnt["no_retest"] == 1


def test_short_mirror():
    post = np.concatenate([np.full(10, 1.0980), [1.09895, 1.0985, 1.0985, 1.0985, 1.0985], np.full(60, 1.0970)])
    b = _scenario(np.concatenate([_breakout_hour(1.0980), post]))
    ev, res, cnt = detect_events(b)
    assert len(ev) == 1 and ev.loc[0, "direction"] == -1 and abs(ev.loc[0, "level"] - 1.0990) < 1e-9
    tr, _ = build_trades(b, ev, horizon=HORIZON_MIN, descriptive_horizons=())
    assert tr.loc[0, "signed_pips"] > 0


def test_time_window_excludes_early_breakout():
    # breakout hour 05:00-06:00 UTC closes 06:00 London (< 07:00): no setup
    # (price returns to 1.1000 afterwards, so no later bar breaks out either)
    b = _scenario(np.concatenate([_breakout_hour(), np.full(200, BASE)]), start_hour=5)
    setups, cnt = find_breakouts(b)
    assert len(setups) == 0


def test_time_window_ny_noon_end():
    # breakout hour 16:00-17:00 UTC closes 12:00 NY -> excluded; 15:00-16:00 closes 11:00 NY -> included
    b = _scenario(np.concatenate([_breakout_hour(), np.full(130, 1.1020)]), start_hour=16)
    assert len(find_breakouts(b)[0]) == 0
    b = _scenario(np.concatenate([_breakout_hour(), np.full(130, 1.1020)]), start_hour=15)
    assert len(find_breakouts(b)[0]) == 1


def test_first_long_setup_per_date_only():
    # a second, higher breakout two hours later is ignored
    after = np.concatenate([_breakout_hour(), np.full(60, 1.1020), np.linspace(1.1020, 1.1050, 60), np.full(60, 1.1050)])
    b = _scenario(after)
    setups, cnt = find_breakouts(b)
    assert cnt["breakouts_in_window"] >= 2 and len(setups) == 1
    assert setups.loc[0, "tc"] == DAY + pd.Timedelta(hours=10)


def test_lookback_needs_20_valid_hours():
    t0 = DAY + pd.Timedelta(hours=-10)       # only 19 hours of history before the 09:00 bar? use 10 + 9 = 19 hours
    n_pre = 19 * 60
    pre = np.full(n_pre, BASE)
    pre[50] = 1.1010
    c = np.concatenate([pre, _breakout_hour(), np.full(130, 1.1020)])
    idx = pd.date_range(t0, periods=len(c), freq="1min")
    b = _frame(idx, c)
    setups, cnt = find_breakouts(b)
    assert len(setups) == 0 and cnt["breakouts_lookback_short"] >= 1


def test_no_look_ahead_truncation():
    b = synthetic_bars("2024-01-01", "2024-02-29", vol_pips_per_min=1.5, seed=3)
    ev_full, _, _ = detect_events(b)
    cut = pd.Timestamp("2024-02-01", tz="UTC")
    ev_cut, _, _ = detect_events(b[b.index < cut])
    # events whose retest window closed before the cut are identical
    safe = ev_full[ev_full["ts"] < cut - pd.Timedelta(minutes=200)]
    got = ev_cut[ev_cut["ts"] < cut - pd.Timedelta(minutes=200)]
    assert len(safe) > 0
    pd.testing.assert_frame_equal(safe.reset_index(drop=True), got.reset_index(drop=True))


def test_breakout_close_variant_stamp():
    b = _scenario(np.concatenate([_breakout_hour(), np.full(130, 1.1020)]))
    setups, _ = find_breakouts(b)
    ev = breakout_close_events(setups)
    assert ev.loc[0, "ts"] == DAY + pd.Timedelta(hours=9, minutes=59)


def test_decision_rule():
    base = {"n": 400, "mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_date_cluster_boot": (0.2, 2.8)}
    assert decide_b58(base) == "SIGNAL"
    assert decide_b58({**base, "n": 299}) == "NONE"
    assert decide_b58({**base, "mean_pips": 0.8}) == "WEAK"
    assert decide_b58({**base, "t_p_one_sided": 0.2, "mean_ci95_date_cluster_boot": (-0.1, 2.0)}) == "NONE"
    assert decide_b58({**base, "mean_pips": -0.5, "mean_ci95_date_cluster_boot": (-1.0, 0.1)}) == "NONE"


def test_no_edge_on_random_walk():
    frames = []
    for seed in (1, 2, 3):
        b = synthetic_bars("2024-01-01", "2024-12-31", vol_pips_per_min=1.5, seed=seed)
        ev, _, _ = detect_events(b)
        tr, _ = build_trades(b, ev, horizon=HORIZON_MIN, descriptive_horizons=())
        frames.append(tr.assign(trading_date=tr["trading_date"].astype(str) + f"_{seed}"))
    tr = pd.concat(frames, ignore_index=True)
    assert len(tr) > 100
    res = evaluate(tr)
    assert decide_b58(res) != "SIGNAL"
    assert abs(res["mean_pips"]) < 3.0
