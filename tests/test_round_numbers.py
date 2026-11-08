import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.fixes import decide
from fxresearch.predictive import evaluate_predictor
from fxresearch.round_numbers import (
    CONTROL_OFFSET, HORIZON_MIN, LEVEL_STEP, build_trades, calendar_shares, cost_summary, detect_crossings,
)


def _bars_from_mid(mids, start="2024-03-05 13:00", spread=0.2):
    """Constant-spread bars whose close (and next open) follow `mids`."""
    idx = pd.date_range(start, periods=len(mids), freq="1min", tz="UTC")
    close = np.asarray(mids, dtype=float)
    open_ = np.concatenate([[close[0]], close[:-1]])
    half = spread * PIP / 2
    df = pd.DataFrame(index=pd.DatetimeIndex(idx, name="ts"))
    for f, v in (("open", open_), ("high", np.maximum(open_, close)), ("low", np.minimum(open_, close)), ("close", close)):
        df[f"bid_{f}"] = v - half
        df[f"ask_{f}"] = v + half
    df["volume"] = 100
    return df


def test_constants_fixed():
    assert LEVEL_STEP == 0.0050 and CONTROL_OFFSET == 0.0023 and HORIZON_MIN == 60


def test_up_and_down_crossing_definition():
    bars = _bars_from_mid([1.0998, 1.1000, 1.1003, 1.1001, 1.0999, 1.0997])
    ev = detect_crossings(bars)
    # 1.0998 -> 1.1000: up-crossing (p(t-1) < L <= p(t)); later down-crossing of the same level is not the first -> dropped
    assert len(ev) == 1
    assert ev.iloc[0]["direction"] == 1 and abs(ev.iloc[0]["level"] - 1.1000) < 1e-9
    assert ev.iloc[0]["ts"] == bars.index[1]


def test_down_crossing_touch_from_above_counts():
    bars = _bars_from_mid([1.1052, 1.1050, 1.1049])
    ev = detect_crossings(bars)
    assert len(ev) == 1 and ev.iloc[0]["direction"] == -1 and abs(ev.iloc[0]["level"] - 1.1050) < 1e-9


def test_no_event_without_crossing_and_on_level_start():
    assert len(detect_crossings(_bars_from_mid([1.1001, 1.1004, 1.1002, 1.1048]))) == 0
    # starting exactly on a level and moving up does not cross it
    assert len(detect_crossings(_bars_from_mid([1.1000, 1.1002, 1.1004]))) == 0


def test_multi_level_jump_uses_level_nearest_close():
    ev = detect_crossings(_bars_from_mid([1.0995, 1.1052]))
    assert len(ev) == 1 and abs(ev.iloc[0]["level"] - 1.1050) < 1e-9


def test_control_levels_end_in_23_and_73():
    ev = detect_crossings(_bars_from_mid([1.1020, 1.1024, 1.1074]), offset=CONTROL_OFFSET)
    assert sorted(np.round(ev["level"], 4)) == [1.1023, 1.1073]
    assert len(detect_crossings(_bars_from_mid([1.1020, 1.1024, 1.1074]))) == 1  # only 1.1050 is round


def test_first_crossing_resets_each_trading_date():
    # 16:58-17:01 NY crosses the 17:00 roll (EST on 2024-03-05: 21:58 UTC)
    mids = [1.0998, 1.1001, 1.0998, 1.1001]
    bars = _bars_from_mid(mids, start="2024-03-05 21:58")
    ev = detect_crossings(bars)
    # 21:58->21:59 up (td 03-05); 21:59->22:00 down crosses the roll boundary -> ignored; 22:00->22:01 up (td 03-06)
    assert list(ev["direction"]) == [1, 1]
    assert ev["trading_date"].nunique() == 2


def test_trade_entry_next_open_and_exit_60m_and_signed():
    mids = [1.0998, 1.1001] + list(np.linspace(1.1001, 1.1011, 70))
    bars = _bars_from_mid(mids)
    ev = detect_crossings(bars)
    tr, skips = build_trades(bars, ev)
    assert len(tr) == 1
    t = tr.iloc[0]
    assert t["entry_ts"] == ev.iloc[0]["ts"] + pd.Timedelta(minutes=1)
    assert t["exit_ts"] == t["entry_ts"] + pd.Timedelta(minutes=60)
    mo = (bars["bid_open"] + bars["ask_open"]) / 2
    assert abs(t["signed_pips"] - (mo[t["exit_ts"]] - mo[t["entry_ts"]]) / PIP) < 1e-9
    assert abs(t["net_bidask_pips"] - (t["signed_pips"] - 0.2)) < 1e-6  # one spread of 0.2 crossed in total


def test_roll_exclusion_and_spread_exclusion():
    # event at 16:00 NY (EST 21:00 UTC) -> exit 17:01 NY inside the roll window
    mids = [1.0998, 1.1001] + [1.1001] * 80
    bars = _bars_from_mid(mids, start="2024-03-05 20:59")
    tr, skips = build_trades(bars, detect_crossings(bars))
    assert len(tr) == 0 and skips["roll"] == 1
    wide = _bars_from_mid(mids, start="2024-03-05 14:00", spread=2.5)
    tr, skips = build_trades(wide, detect_crossings(wide))
    assert len(tr) == 0 and skips["spread"] == 1


def test_overlap_skipped_and_coverage():
    mids = [1.0998, 1.1001, 1.1048, 1.1051] + [1.1051] * 80  # 1.1000 at bar 1, 1.1050 crossed at bar 3 (inside trade)
    bars = _bars_from_mid(mids)
    ev = detect_crossings(bars)
    assert len(ev) == 2
    tr, skips = build_trades(bars, ev)
    assert len(tr) == 1 and skips["overlap"] == 1
    holed = bars.drop(bars.index[10:20])  # 10 missing bars inside the 60-minute window
    tr, skips = build_trades(holed, detect_crossings(holed))
    assert skips["coverage"] >= 1


def test_no_look_ahead_trade_uses_only_later_prices():
    mids = [1.0998, 1.1001] + [1.1001] * 70
    bars = _bars_from_mid(mids)
    tr, _ = build_trades(bars, detect_crossings(bars))
    assert (tr["entry_ts"] > tr["event_ts"]).all()
    # changing prices before the event bar does not change the trade return
    b2 = bars.copy()
    pc = [c for c in b2.columns if c != "volume"]
    b2.loc[b2.index[0], pc] = b2.loc[b2.index[0], pc] - 0.0001
    tr2, _ = build_trades(b2, detect_crossings(b2))
    assert np.allclose(tr["signed_pips"], tr2["signed_pips"])


def test_random_walk_no_signal_and_costs_negative():
    bars = synthetic_bars("2024-01-01", "2024-07-31", vol_pips_per_min=1.5, seed=11)
    ev = detect_crossings(bars)
    tr, _ = build_trades(bars, ev)
    assert len(tr) >= 100
    res = evaluate_predictor(tr["direction"].astype(float).set_axis(tr["entry_ts"]), tr["ret_pips"].set_axis(tr["entry_ts"]))
    assert decide(res, n_trials=1) != "SIGNAL"
    c = cost_summary(tr)
    assert c["mean_net_spec4_pips"] < c["mean_signed_mid_pips"]
    assert set(calendar_shares(tr)) == {"share_within_15m_ny_0830", "share_within_15m_ny_1000", "share_within_15m_ny_1100"}
