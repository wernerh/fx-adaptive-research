"""E016 (B13): settlement-window parser, CT edges, no look-ahead, decision rule, random walk."""
import json
from datetime import date, time

import numpy as np
import pandas as pd
import pytest

from fxresearch.cme_settle import (
    CT, cost_summary, decide_b13, evaluate, find_fx_windows, load_settlement, momentum_frame, reversal_flag,
    validate_settlement,
)
from fxresearch.data import synthetic_bars

# Invented test text (shape only); not the real CME values.
TXT = """Product  Settlement window  Updates
Equity: 08:10:00-08:11:00 CT 08:20
FX: 09:29:30-09:30:00 CT 09:47, 10:00
Interest Rates 10:00-10:01 CT
"""


def test_find_fx_windows_only_fx_row():
    w = find_fx_windows(TXT)
    assert len(w) == 1
    assert w[0]["start"] == "09:29:30" and w[0]["end"] == "09:30:00" and w[0]["tz"] == "CT"


def test_find_fx_windows_variants():
    assert find_fx_windows("Euro FX settles 09:29 to 09:30 Central")[0]["end"] == "09:30"
    assert find_fx_windows("nothing here 09:29-09:30 CT") == []


def test_validate_settlement():
    ok, note, s = validate_settlement(find_fx_windows(TXT))
    assert ok and s == "09:30"
    assert validate_settlement([])[0] is False
    conflict = find_fx_windows(TXT + "\nFX: 10:59:30-11:00:00 CT")
    ok2, note2, _ = validate_settlement(conflict)
    assert not ok2 and "conflicting" in note2
    ok3, note3, _ = validate_settlement(find_fx_windows("FX: 02:00-03:00 CT"))
    assert not ok3 and "implausible" in note3


def test_load_settlement_requires_review(tmp_path):
    p = tmp_path / "s.json"
    p.write_text(json.dumps({"settle_time_ct": "09:30", "source_url": "x", "reviewed": False}))
    with pytest.raises(ValueError):
        load_settlement(p)
    p.write_text(json.dumps({"settle_time_ct": "09:30", "source_url": "x", "reviewed": True}))
    assert load_settlement(p) == time(9, 30)


def _flat_bars(start="2024-01-08", end="2024-01-13"):
    idx = pd.date_range(start, end, freq="1min", tz="UTC", inclusive="left")
    b = pd.DataFrame(index=idx)
    for f in ("open", "high", "low", "close"):
        b[f"bid_{f}"] = 1.1000
        b[f"ask_{f}"] = 1.1002
    b["volume"] = 1
    return b


def _set(b, mask, price):
    for f in ("open", "high", "low", "close"):
        b.loc[mask, f"bid_{f}"] = price
        b.loc[mask, f"ask_{f}"] = price + 0.0002


S = time(9, 30)  # invented settlement time for tests


def test_edges_in_central_time_and_sign():
    b = _flat_bars()
    ct = b.index.tz_convert(CT)
    day = ct.date == date(2024, 1, 10)
    m = ct.hour * 60 + ct.minute
    # r1 up 10 pips by S-30 (08:55 CT close quote at 08:59), r2 +5 pips over the last 30 min
    _set(b, day & (m >= 8 * 60) & (m < 9 * 60 + 25), 1.1010)
    _set(b, day & (m >= 9 * 60 + 25) & (m < 9 * 60 + 30), 1.1015)
    f = momentum_frame(b, S)
    r = f.loc[date(2024, 1, 10)]
    assert r["r1_pips"] == pytest.approx(10.0)
    assert r["r2_pips"] == pytest.approx(5.0)
    assert r["direction"] == 1 and r["signed_pips"] == pytest.approx(5.0)
    assert r["entry_spread_pips"] == pytest.approx(2.0)
    assert r["net_bidask_pips"] == pytest.approx(3.0)


def test_no_lookahead_r1_ignores_target_window():
    b = _flat_bars()
    ct = b.index.tz_convert(CT)
    day = ct.date == date(2024, 1, 10)
    m = ct.hour * 60 + ct.minute
    f0 = momentum_frame(b, S).loc[date(2024, 1, 10)]
    _set(b, day & (m >= 9 * 60) & (m < 9 * 60 + 30), 1.1050)  # change only bars inside [S-30, S)
    f1 = momentum_frame(b, S).loc[date(2024, 1, 10)]
    assert f1["r1_pips"] == pytest.approx(f0["r1_pips"])
    assert f1["direction"] == f0["direction"]


def test_small_r1_is_no_trade_kept_in_n_and_missing_dropped():
    b = _flat_bars()
    ct = b.index.tz_convert(CT)
    m = ct.hour * 60 + ct.minute
    hole = (ct.date == date(2024, 1, 11)) & (m >= 9 * 60 + 25) & (m < 9 * 60 + 30)
    b = b[~hole]
    f = momentum_frame(b, S)
    assert np.isnan(f.loc[date(2024, 1, 11), "signed_pips"])
    flat = f.loc[date(2024, 1, 9)]
    assert flat["direction"] == 0 and flat["signed_pips"] == 0.0
    res = evaluate(f)
    assert res["n"] == int(f["signed_pips"].notna().sum()) and res["n_traded"] == 0


def test_decision_rule():
    base = {"mean_signed_pips": 1.5, "mean_signed_ci95_block_boot": (0.2, 2.5), "binom_p": 0.01}
    assert decide_b13(base) == "SIGNAL"
    assert decide_b13({**base, "mean_signed_pips": 0.8}) == "WEAK"
    assert decide_b13({**base, "mean_signed_ci95_block_boot": (-0.1, 2.5), "binom_p": 0.2}) == "NONE"
    assert decide_b13({}) == "NONE"
    assert reversal_flag({"mean_signed_pips": -1.0, "mean_signed_ci95_block_boot": (-2.0, -0.1)})


def test_random_walk_no_signal():
    b = synthetic_bars()
    f = momentum_frame(b, S)
    res = evaluate(f)
    assert res["n"] > 40
    assert decide_b13(res) != "SIGNAL"
    c = cost_summary(f)
    assert c["mean_net_spec4_pips"] < c["mean_gross_traded_pips"]
