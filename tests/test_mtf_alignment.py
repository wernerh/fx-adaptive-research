"""E049 (B59) multi-timeframe alignment + 5m EMA20-cross trigger: bars and EMA, last-completed-bucket state, cross detection,
contiguity, time window, signal stamp and fill, control variant, no look-ahead, decision rule, no edge on random walks."""
import numpy as np
import pandas as pd

from fxresearch.data import synthetic_bars
from fxresearch.mtf_alignment import (HORIZON_MIN, MIN_EVENTS, crosses, decide_b59, detect_events, evaluate, tf_bars,
                                      trend_state)
from fxresearch.round_numbers import build_trades

HALF = 0.00001
PIP = 0.0001
DAY = pd.Timestamp("2019-03-06", tz="UTC")   # Wednesday; London = UTC, NY = UTC-5


def _frame(idx, c):
    c = np.asarray(c, float)
    o = np.concatenate([[c[0]], c[:-1]])
    df = pd.DataFrame(index=pd.DatetimeIndex(idx, name="ts"))
    for f, v in (("open", o), ("high", np.maximum(o, c)), ("low", np.minimum(o, c)), ("close", c)):
        df[f"bid_{f}"] = v - HALF
        df[f"ask_{f}"] = v + HALF
    return df


def _trend_with_dip(sign=1, dip_at_h=10, slope=0.5, dip=30.0, dip_len=10):
    """Steady trend (slope pips/min, direction sign) from DAY-1 00:00 for 2 days; at DAY dip_at_h:00 a counter-move of `dip`
    pips over `dip_len` minutes, then the trend resumes."""
    n = 2 * 24 * 60
    steps = np.full(n, slope * sign)
    i0 = (24 + dip_at_h) * 60
    steps[i0:i0 + dip_len] = -sign * dip / dip_len
    c = 1.1000 + np.cumsum(steps) * PIP
    idx = pd.date_range(DAY - pd.Timedelta(days=1), periods=n, freq="1min")
    return _frame(idx, c)


def test_constants():
    assert MIN_EVENTS == 300 and HORIZON_MIN == 60


def test_tf_bars_and_ema():
    b = _trend_with_dip()
    g = tf_bars(b, 15)
    assert g.index[0] == DAY - pd.Timedelta(days=1) and g["n"].iloc[0] == 15
    assert g["end"].iloc[0] == g.index[0] + pd.Timedelta(minutes=15)
    assert g["close"].iloc[0] == round((b["bid_close"].iloc[14] + b["ask_close"].iloc[14]) * 1e5)
    assert g["ema"].iloc[:19].isna().all() and not np.isnan(g["ema"].iloc[19])
    ref = g["close"].astype(float).ewm(span=20, adjust=False).mean()
    assert np.allclose(g["ema"].iloc[19:], ref.iloc[19:])


def test_long_signal_on_dip_in_uptrend():
    b = _trend_with_dip(sign=1)
    ev, cnt = detect_events(b)
    day = ev[(ev["ts"] >= DAY + pd.Timedelta(hours=10)) & (ev["ts"] < DAY + pd.Timedelta(hours=11))]
    assert len(day) == 1 and day["direction"].iloc[0] == 1
    assert (ev["direction"] == 1).all()
    ts = day["ts"].iloc[0]
    assert (ts + pd.Timedelta(minutes=1)).minute % 5 == 0          # stamped T - 1 min, T on the 5m grid
    tr, _ = build_trades(b, day, horizon=HORIZON_MIN, descriptive_horizons=())
    assert tr["entry_ts"].iloc[0] == ts + pd.Timedelta(minutes=1)   # fill at the open of the bar at T
    assert tr["signed_pips"].iloc[0] > 0


def test_short_mirror():
    b = _trend_with_dip(sign=-1)
    ev, _ = detect_events(b)
    day = ev[(ev["ts"] >= DAY + pd.Timedelta(hours=10)) & (ev["ts"] < DAY + pd.Timedelta(hours=11))]
    assert len(day) == 1 and day["direction"].iloc[0] == -1
    assert (ev["direction"] == -1).all()


def test_no_signal_against_state_but_control_has_it():
    # downtrend with a 5m up-cross: the aligned rule takes only the short re-cross, the control also takes the long up-cross
    b = _trend_with_dip(sign=-1)
    cx = crosses(b)
    w = cx[(cx["T"] > DAY + pd.Timedelta(hours=10)) & (cx["T"] <= DAY + pd.Timedelta(hours=11))]
    assert set(w["cross"]) == {1, -1}
    ev, _ = detect_events(b)
    ctl, _ = detect_events(b, aligned=False)
    assert (ev["direction"] == -1).all() and (ctl["direction"] == 1).any()


def test_time_window():
    # dip at 05:00 UTC (= 05:00 London, < 07:00): no in-window cross; dip at 17:00 UTC (= 12:00 NY): excluded
    for h in (5, 17):
        b = _trend_with_dip(dip_at_h=h)
        cx = crosses(b)
        w = cx[(cx["T"] > DAY + pd.Timedelta(hours=h)) & (cx["T"] <= DAY + pd.Timedelta(hours=h + 1))]
        assert len(w) == 0
    b = _trend_with_dip(dip_at_h=16)                 # 16:xx UTC = 11:xx NY: included
    cx = crosses(b)
    assert len(cx[(cx["T"] > DAY + pd.Timedelta(hours=16)) & (cx["T"] <= DAY + pd.Timedelta(hours=17))]) > 0


def test_state_uses_last_completed_bucket_only():
    b = _trend_with_dip(sign=1)
    T = pd.DatetimeIndex([DAY + pd.Timedelta(hours=12)])
    s_full, m_full = trend_state(b, T)
    # wreck everything at/after T: the state at T must not change
    b2 = b.copy()
    after = b2.index >= T[0]
    for col in b2.columns:
        b2.loc[after, col] = b2.loc[after, col] - 0.0500
    s_cut, m_cut = trend_state(b2, T)
    assert s_full[0] == 1 and s_cut[0] == s_full[0] and not m_full[0] and not m_cut[0]


def test_htf_missing_bucket():
    b = _trend_with_dip(sign=1)
    T = DAY + pd.Timedelta(hours=12)
    gap = (b.index >= T - pd.Timedelta(hours=1)) & (b.index < T)
    s, m = trend_state(b[~gap], pd.DatetimeIndex([T]))
    assert m[0] and s[0] == 0


def test_cross_needs_contiguous_previous_bucket():
    b = _trend_with_dip(sign=1)
    full = crosses(b)
    t = full[(full["T"] > DAY + pd.Timedelta(hours=10)) & (full["T"] <= DAY + pd.Timedelta(hours=11))]
    up = t[t["cross"] == 1].iloc[0]
    # drop the 5m bucket before the up-cross bar: no cross can be formed at that bar
    prev = (b.index >= up["start"] - pd.Timedelta(minutes=5)) & (b.index < up["start"])
    cx = crosses(b[~prev])
    assert not (cx["T"] == up["T"]).any()


def test_ten_minute_trigger_stamp():
    b = _trend_with_dip(sign=1)
    b = _trend_with_dip(sign=1, slope=0.3, dip=40.0)
    ev, _ = detect_events(b, trigger_minutes=10)
    assert len(ev) > 0 and ((ev["ts"] + pd.Timedelta(minutes=1)).dt.minute % 10 == 0).all()


def test_no_look_ahead_truncation():
    b = synthetic_bars("2024-01-01", "2024-02-29", vol_pips_per_min=1.5, seed=3)
    ev_full, _ = detect_events(b)
    cut = pd.Timestamp("2024-02-01", tz="UTC")
    ev_cut, _ = detect_events(b[b.index < cut])
    safe = ev_full[ev_full["ts"] < cut - pd.Timedelta(minutes=1)]
    assert len(safe) > 0
    pd.testing.assert_frame_equal(safe.reset_index(drop=True), ev_cut.reset_index(drop=True))


def test_decision_rule():
    base = {"n": 400, "mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_date_cluster_boot": (0.2, 2.8)}
    assert decide_b59(base) == "SIGNAL"
    assert decide_b59({**base, "n": 299}) == "NONE"
    assert decide_b59({**base, "mean_pips": 0.8}) == "WEAK"
    assert decide_b59({**base, "t_p_one_sided": 0.2, "mean_ci95_date_cluster_boot": (-0.1, 2.0)}) == "NONE"


def test_no_edge_on_random_walk():
    frames = []
    for seed in (1, 2):
        b = synthetic_bars("2024-01-01", "2024-06-30", vol_pips_per_min=1.5, seed=seed)
        ev, _ = detect_events(b)
        tr, _ = build_trades(b, ev, horizon=HORIZON_MIN, descriptive_horizons=())
        frames.append(tr)
    tr = pd.concat(frames, ignore_index=True)
    assert len(tr) > 100
    res = evaluate(tr, "signed_pips")
    assert decide_b59({**res, "n": max(res["n"], MIN_EVENTS)}) != "SIGNAL"
