"""E047 (B56) pivot R1/S1 first-touch continuation: day key, levels, touch definition, first-touch only, both-touch skip,
previous-date bar floor, no look-ahead, control shift, decision rule and no edge on random walks."""
import numpy as np
import pandas as pd

from fxresearch.data import synthetic_bars
from fxresearch.pivot_touch import (CONTROL_SHIFT, HORIZON_MIN, MIN_EVENTS, MIN_PREV_BARS, bracket_outcomes,
                                    daily_levels, day_key, decide_b56, detect_events, evaluate)
from fxresearch.round_numbers import build_trades

HALF = 0.00001


def _frame(idx, o, h, lo, c):
    df = pd.DataFrame(index=pd.DatetimeIndex(idx, name="ts"))
    for f, v in (("open", o), ("high", h), ("low", lo), ("close", c)):
        df[f"bid_{f}"] = np.asarray(v, float) - HALF
        df[f"ask_{f}"] = np.asarray(v, float) + HALF
    return df


def _two_days(today_closes, today_highs=None, today_lows=None, prev_n=1100, H=1.1050, L=1.0950, C=1.1000,
              day="2019-03-06"):
    """Previous UTC date (Tuesday) with prev_n bars, high H, low L, last close C; then bars on `day` from 08:00 UTC."""
    d = pd.Timestamp(day, tz="UTC")
    pidx = pd.date_range(d - pd.Timedelta(days=1), periods=prev_n, freq="1min")
    pc = np.full(prev_n, C)
    ph, pl = pc.copy(), pc.copy()
    ph[10], pl[20] = H, L
    prev = _frame(pidx, pc, ph, pl, pc)
    c = np.asarray(today_closes, float)
    o = np.concatenate([[C], c[:-1]])
    h = np.maximum(np.asarray(today_highs, float) if today_highs is not None else c, np.maximum(o, c))
    lo = np.minimum(np.asarray(today_lows, float) if today_lows is not None else c, np.minimum(o, c))
    tidx = pd.date_range(d + pd.Timedelta(hours=8), periods=len(c), freq="1min")
    return pd.concat([prev, _frame(tidx, o, h, lo, c)])


# P = (1.1050 + 1.0950 + 1.1000)/3 = 1.1000; R1 = 2P - L = 1.1050; S1 = 2P - H = 1.0950
R1, S1 = 1.1050, 1.0950


def test_constants():
    assert MIN_EVENTS == 300 and HORIZON_MIN == 120 and MIN_PREV_BARS == 1000 and CONTROL_SHIFT == 0.0023


def test_day_key_sunday_to_monday_and_saturday_dropped():
    idx = pd.DatetimeIndex(["2019-03-08 21:00", "2019-03-09 12:00", "2019-03-10 22:00", "2019-03-11 01:00"], tz="UTC")
    k = day_key(idx)
    assert pd.Timestamp(k[0]) == pd.Timestamp("2019-03-08")
    assert np.isnat(k[1])
    assert pd.Timestamp(k[2]) == pd.Timestamp("2019-03-11") == pd.Timestamp(k[3])


def test_levels_exact():
    b = _two_days([1.1000, 1.1001])
    lv = daily_levels(b).iloc[-1]
    assert lv["valid"]
    assert lv["r1_3"] / 3 == round(2 * R1 * 1e5) and lv["s1_3"] / 3 == round(2 * S1 * 1e5)


def test_r1_touch_long_and_s1_touch_short():
    b = _two_days([1.1040, 1.1045, 1.1048], today_highs=[1.1040, 1.1045, 1.1050])
    ev, _ = detect_events(b)
    assert len(ev) == 1 and ev.iloc[0].leg == "R1" and ev.iloc[0].direction == 1 and ev.iloc[0].ts == b.index[-1]
    assert abs(ev.iloc[0].level - R1) < 1e-9
    b = _two_days([1.0960, 1.0955, 1.0952], today_lows=[1.0960, 1.0955, 1.0950])
    ev, _ = detect_events(b)
    assert len(ev) == 1 and ev.iloc[0].leg == "S1" and ev.iloc[0].direction == -1


def test_near_miss_is_not_a_touch():
    b = _two_days([1.1040, 1.1045, 1.1048], today_highs=[1.1040, 1.1045, 1.10499])
    assert len(detect_events(b)[0]) == 0


def test_close_already_above_level_is_not_a_touch():
    # c(t-1) >= R1: no touch until the close falls back below
    b = _two_days([1.1040, 1.1050, 1.1055, 1.1049, 1.1052])
    ev, _ = detect_events(b)
    assert len(ev) == 1 and ev.iloc[0].ts == b.index[-1 - 3]   # bar with close 1.1050 (c(t-1)=1.1040 < R1 <= h)


def test_first_touch_only_per_level_and_date():
    b = _two_days([1.1040, 1.1050, 1.1040, 1.1051])
    ev, _ = detect_events(b)
    assert len(ev) == 1 and ev.iloc[0].ts == b.index[-3]


def test_both_touch_bar_is_skipped():
    b = _two_days([1.1000, 1.1001], today_highs=[1.1000, 1.1060], today_lows=[1.1000, 1.0940])
    ev, cnt = detect_events(b)
    assert len(ev) == 0 and cnt["both_touch"] == 2


def test_prev_date_bar_floor():
    b = _two_days([1.1040, 1.1050], prev_n=999)
    ev, cnt = detect_events(b)
    assert len(ev) == 0 and cnt["dates_excluded_prev_bars"] >= 1


def test_no_lookahead_future_bars_do_not_change_levels_or_events():
    b = _two_days(list(np.linspace(1.1040, 1.1052, 30)))
    ev1, _ = detect_events(b)
    ext = b.copy()
    ext.iloc[-5:, :] = ext.iloc[-5:, :] + 0.01   # perturb later bars of the same date
    ev2, _ = detect_events(ext)
    assert ev1.iloc[0].ts == ev2.iloc[0].ts and ev1.iloc[0].level == ev2.iloc[0].level


def test_control_shift_moves_level():
    b = _two_days([1.1060, 1.1070, 1.1075], today_highs=[1.1060, 1.1070, 1.1073])
    ev, _ = detect_events(b, shift=CONTROL_SHIFT)
    assert len(ev) == 1 and abs(ev.iloc[0].level - (R1 + CONTROL_SHIFT)) < 1e-9


def test_trade_sign_and_bracket():
    closes = [1.1040, 1.1050] + [1.1050 + 0.00002 * i for i in range(1, 200)]
    b = _two_days(closes)
    ev, _ = detect_events(b)
    tr, skips = build_trades(b, ev, horizon=HORIZON_MIN, descriptive_horizons=(60, 180))
    assert len(tr) == 1 and tr.iloc[0].signed_pips > 0 and tr.iloc[0].direction == 1
    assert (tr.iloc[0].entry_ts - ev.iloc[0].ts) >= pd.Timedelta(minutes=1)
    out = bracket_outcomes(b, tr, ev)
    assert out.iloc[0] in ("win", "unresolved")


def test_decision_rule():
    base = {"n": 400, "mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_date_cluster_boot": (0.2, 2.8)}
    assert decide_b56(base) == "SIGNAL"
    assert decide_b56({**base, "n": 299}) == "NONE"
    assert decide_b56({**base, "mean_pips": 0.8}) == "WEAK"
    assert decide_b56({**base, "mean_pips": -0.1}) == "NONE"
    assert decide_b56({**base, "mean_ci95_date_cluster_boot": (-0.1, 2.8), "t_p_one_sided": 0.2}) == "NONE"


def test_no_edge_on_random_walk():
    frames = []
    for seed in (1, 2):
        b = synthetic_bars("2024-01-01", "2024-12-31", vol_pips_per_min=1.5, seed=seed)
        ev, _ = detect_events(b)
        tr, _ = build_trades(b, ev, horizon=HORIZON_MIN, descriptive_horizons=())
        frames.append(tr)
    tr = pd.concat(frames, ignore_index=True)
    assert len(tr) > MIN_EVENTS
    res = evaluate(tr)
    assert decide_b56(res) != "SIGNAL"
    assert abs(res["mean_pips"]) < 3.0
