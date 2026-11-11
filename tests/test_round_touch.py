"""E045 (B52) take-profit reversal at round numbers: touch definition, eligibility, nearest level, trade sign, no look-ahead,
crossed-within-hold, decision rule and no edge on random walks."""
import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.round_numbers import build_trades
from fxresearch.round_touch import (CONTROL_OFFSET, MIN_EVENTS, crossed_within_hold, decide_b52, detect_touches,
                                    evaluate)

HALF = 0.00001  # half-spread 0.1 pip -> bid + ask = 2 x mid exactly


def _bars(closes, highs=None, lows=None, start="2019-03-05 12:00", opens=None):
    """1-minute bars from mid closes (UTC 12:00 = 07:00/08:00 NY, one trading date). High/low default to max/min(open, close)."""
    c = np.asarray(closes, float)
    o = np.asarray(opens, float) if opens is not None else np.concatenate([[c[0]], c[:-1]])
    h = np.asarray(highs, float) if highs is not None else np.maximum(o, c)
    lo = np.asarray(lows, float) if lows is not None else np.minimum(o, c)
    h, lo = np.maximum(h, np.maximum(o, c)), np.minimum(lo, np.minimum(o, c))
    idx = pd.date_range(start, periods=len(c), freq="1min", tz="UTC", name="ts")
    df = pd.DataFrame(index=idx)
    for f, v in (("open", o), ("high", h), ("low", lo), ("close", c)):
        df[f"bid_{f}"] = v - HALF
        df[f"ask_{f}"] = v + HALF
    return df


def test_constants():
    assert MIN_EVENTS == 300
    assert CONTROL_OFFSET == 0.0023


def test_up_touch_detected_and_fade_sign():
    b = _bars([1.0990, 1.0995, 1.0992], highs=[1.0990, 1.0995, 1.1000])
    ev = detect_touches(b)
    assert len(ev) == 1
    r = ev.iloc[0]
    assert r.ts == b.index[2] and r.level == 1.1 and r.side == 1 and r.direction == -1


def test_down_touch_detected():
    b = _bars([1.1010, 1.1005, 1.1003], lows=[1.1010, 1.1005, 1.1000])
    ev = detect_touches(b)
    assert len(ev) == 1 and ev.iloc[0].direction == 1 and ev.iloc[0].level == 1.1


def test_near_miss_and_close_on_level_are_not_touches():
    assert len(detect_touches(_bars([1.0990, 1.0995, 1.0992], highs=[1.0990, 1.0995, 1.09999]))) == 0
    # close exactly at the level is an E018 crossing, not a rejected touch
    assert len(detect_touches(_bars([1.0990, 1.0995, 1.1000]))) == 0


def test_first_touch_only_per_level_and_date():
    b = _bars([1.0990, 1.0995, 1.0992, 1.0994, 1.0993], highs=[1.0990, 1.0995, 1.1000, 1.0994, 1.1001])
    ev = detect_touches(b)
    assert len(ev) == 1 and ev.iloc[0].ts == b.index[2]


def test_level_crossed_earlier_is_ineligible_but_earlier_touch_counts():
    # cross up through 1.1000 at bar 2, then a touch from above at bar 4 -> no event
    b = _bars([1.0995, 1.0998, 1.1004, 1.1006, 1.1003], lows=[1.0995, 1.0998, 1.0998, 1.1006, 1.1000])
    assert len(detect_touches(b)) == 0
    # touch first (bar 2), crossing later (bar 4) -> the touch counts
    b2 = _bars([1.0990, 1.0995, 1.0992, 1.0996, 1.1004], highs=[1.0990, 1.0995, 1.1000, 1.0996, 1.1004])
    ev = detect_touches(b2)
    assert len(ev) == 1 and ev.iloc[0].ts == b2.index[2]


def test_nearest_level_to_close_counts_when_bar_touches_two():
    # bar 1 wicks up to 1.1000 and down to 1.0950, closes 1.0990 -> 1.1000 (10 pips) nearer than 1.0950 (40 pips)
    b = _bars([1.0985, 1.0990], highs=[1.0985, 1.1000], lows=[1.0985, 1.0950])
    ev = detect_touches(b)
    assert len(ev) == 1 and ev.iloc[0].level == 1.1 and ev.iloc[0].direction == -1


def test_no_event_across_trading_date_boundary():
    # 21:59 -> 22:00 UTC in March 2019 before US DST (EST): 16:59 -> 17:00 NY roll
    b = _bars([1.0990, 1.0995], highs=[1.0990, 1.1000], start="2019-03-05 21:59")
    assert len(detect_touches(b)) == 0


def test_control_levels():
    b = _bars([1.0960, 1.0968, 1.0965], highs=[1.0960, 1.0968, 1.0973])
    assert len(detect_touches(b)) == 0
    ev = detect_touches(b, offset=CONTROL_OFFSET)
    assert len(ev) == 1 and abs(ev.iloc[0].level - 1.0973) < 1e-9


def test_trade_sign_and_no_look_ahead():
    n = 120
    closes = np.full(n, 1.0990)
    closes[:3] = [1.0990, 1.0995, 1.0992]
    closes[3:] = np.linspace(1.0992, 1.0972, n - 3)  # falls 20 pips after the up-touch
    highs = closes.copy()
    highs[2] = 1.1000
    b = _bars(closes, highs=highs)
    ev = detect_touches(b)
    assert len(ev) == 1
    tr, skips = build_trades(b, ev)
    assert len(tr) == 1 and tr.iloc[0].signed_pips > 8  # short after up-touch earns the fall (~10 pips in 60 min)
    assert tr.iloc[0].entry_ts == b.index[3]
    # truncating everything after bar t leaves the event unchanged
    ev_t = detect_touches(b.iloc[:3])
    assert ev_t.equals(ev)
    # changing later bars does not change the event at t
    b2 = b.copy()
    b2.iloc[3:, :] = b2.iloc[3:, :] + 0.0050
    assert detect_touches(b2).iloc[0].equals(ev.iloc[0])


def test_crossed_within_hold():
    n = 120
    closes = np.full(n, 1.0990)
    closes[:3] = [1.0990, 1.0995, 1.0992]
    closes[3:] = np.linspace(1.0992, 1.1010, n - 3)
    highs = closes.copy()
    highs[2] = 1.1000
    b = _bars(closes, highs=highs)
    tr, _ = build_trades(b, detect_touches(b))
    assert crossed_within_hold(b, tr).tolist() == [True]


def test_decision_rule():
    base = {"n": 400, "mean_pips": 1.2, "t_p_one_sided": 0.01, "mean_ci95_date_cluster_boot": (0.2, 2.0)}
    assert decide_b52(base) == "SIGNAL"
    assert decide_b52({**base, "n": 299}) == "NONE"
    assert decide_b52({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b52({**base, "mean_pips": 0.5, "t_p_one_sided": 0.2, "mean_ci95_date_cluster_boot": (-0.1, 1.0)}) == "NONE"
    assert decide_b52({**base, "mean_pips": -0.1}) == "NONE"


def test_no_edge_on_random_walk():
    """Pooled random-walk years (no edge by construction): no SIGNAL and |mean| small."""
    frames = []
    for seed in (1, 2, 3, 4):
        b = synthetic_bars("2024-01-01", "2024-12-31", vol_pips_per_min=1.5, seed=seed)
        tr, _ = build_trades(b, detect_touches(b))
        frames.append(tr)
    tr = pd.concat(frames, ignore_index=True)
    assert len(tr) > MIN_EVENTS
    res = evaluate(tr)
    assert abs(res["mean_pips"]) < 1.5
    assert decide_b52(res) != "SIGNAL"
