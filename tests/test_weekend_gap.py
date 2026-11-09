from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.weekend_gap import (
    BOOT_BLOCK, MAX_ENTRY_SPREAD_PIPS, MIN_MEAN_PIPS, PCTL, WINDOW, cost_summary, decide_b17, evaluate, mark_events,
    tradable_events, weekend_frame,
)


def test_constants_fixed():
    assert WINDOW == 26 and PCTL == 67 and BOOT_BLOCK == 4 and MIN_MEAN_PIPS == 1.0 and MAX_ENTRY_SPREAD_PIPS == 2.0


def _wf(gaps, rets, m_spread=0.5, start=date(2015, 1, 5)):
    """Synthetic weekend frame: F=1.1, M=F+gap, X=M+ret (pips)."""
    rows = []
    for i, (g, r) in enumerate(zip(gaps, rets)):
        f = 1.1
        m = f + g * PIP
        x = m + r * PIP
        rows.append({"monday": start + timedelta(days=7 * i), "valid": True, "missing": None, "F_mid": f, "M_mid": m,
                     "X_mid": x, "gap_pips": g, "F_spread_pips": 0.3, "M_spread_pips": m_spread, "X_spread_pips": 0.3,
                     "tue_mid": x, "fri_mid": x, "sun17_mid": m})
    return pd.DataFrame(rows)


def test_threshold_is_past_only_and_strict():
    gaps = [float(i % 10 + 1) for i in range(26)] + [100.0, 1.0, -100.0]
    rets = [0.0] * 26 + [-30.0, 5.0, 40.0]
    v = mark_events(_wf(gaps, rets))
    assert not v["is_event"].iloc[:26].any()
    thr = np.percentile(np.abs(gaps[:26]), 67)
    assert abs(v["threshold_pips"].iloc[26] - thr) < 1e-9
    assert list(v["is_event"].iloc[26:]) == [True, False, True]
    # gap +100 then ret -30 -> reversal +30; gap -100 then ret +40 -> +40
    assert abs(v["signed_pips"].iloc[26] - 30) < 1e-6 and abs(v["signed_pips"].iloc[28] - 40) < 1e-6
    # gap equal to the threshold is not an event
    gaps2 = gaps[:26] + [thr]
    assert not mark_events(_wf(gaps2, rets[:27]))["is_event"].iloc[26]


def test_no_look_ahead_in_events():
    rng = np.random.default_rng(3)
    gaps = list(rng.normal(0, 15, 80))
    rets = list(rng.normal(0, 40, 80))
    a = mark_events(_wf(gaps, rets))
    gaps2 = gaps[:50] + [g * 10 for g in gaps[50:]]
    rets2 = rets[:50] + [r + 500 for r in rets[50:]]
    b = mark_events(_wf(gaps2, rets2))
    assert list(a["is_event"].iloc[:50]) == list(b["is_event"].iloc[:50])
    assert np.allclose(a["threshold_pips"].iloc[:51].fillna(-1), b["threshold_pips"].iloc[:51].fillna(-1))


def test_spread_skip():
    gaps = [float(i % 10 + 1) for i in range(26)] + [100.0]
    v = mark_events(_wf(gaps, [0.0] * 27, m_spread=2.5))
    assert v["is_event"].iloc[26] and v["entry_skipped"].iloc[26]
    assert tradable_events(v).empty


def test_costs_order():
    gaps = [float(i % 10 + 1) for i in range(26)] + [100.0, -100.0]
    v = mark_events(_wf(gaps, [0.0] * 26 + [-20.0, 10.0]))
    c = cost_summary(tradable_events(v))
    assert c["n"] == 2 and abs(c["mean_signed_mid_pips"] - 15) < 1e-6
    assert c["mean_net_costs_x1_5_pips"] < c["mean_net_spec4_pips"] < c["mean_net_bidask_pips"] < c["mean_signed_mid_pips"]


def test_weekend_frame_from_bars_uses_correct_quotes():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    wf, skips = weekend_frame(bars)
    assert wf["valid"].all() and sum(skips.values()) == 0
    r = wf[wf["monday"] == date(2024, 3, 4)].iloc[0]

    def mid(ts):
        t = pd.Timestamp(ts, tz="America/New_York").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2

    assert abs(r["F_mid"] - mid("2024-03-01 16:00")) < 1e-12
    assert abs(r["M_mid"] - mid("2024-03-03 20:00")) < 1e-12
    assert abs(r["X_mid"] - mid("2024-03-04 16:00")) < 1e-12
    assert abs(r["gap_pips"] - (r["M_mid"] - r["F_mid"]) / PIP) < 1e-9


def test_missing_bar_excluded_and_counted():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    t = pd.Timestamp("2024-03-03 20:00", tz="America/New_York").tz_convert("UTC")
    bars = bars[(bars.index < t) | (bars.index >= t + pd.Timedelta(minutes=5))]
    wf, skips = weekend_frame(bars)
    assert skips["missing_M"] == 1
    assert wf.loc[wf["monday"] == date(2024, 3, 4), "missing"].iloc[0] == "missing_M"


def test_random_walk_no_signal():
    for seed in range(5):
        rng = np.random.default_rng(seed)
        n = 320
        v = mark_events(_wf(list(rng.normal(0, 15, n)), list(rng.normal(0, 45, n))))
        res = evaluate(tradable_events(v)["signed_pips"])
        assert res["n"] > 60
        assert decide_b17(res) != "SIGNAL"


def test_strong_reversal_gives_signal():
    rng = np.random.default_rng(1)
    n = 320
    gaps = rng.normal(0, 15, n)
    rets = -0.8 * gaps + rng.normal(0, 10, n)
    v = mark_events(_wf(list(gaps), list(rets)))
    assert decide_b17(evaluate(tradable_events(v)["signed_pips"])) == "SIGNAL"


def test_decide_rule_edges():
    base = {"mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.2, 2.8)}
    assert decide_b17(base) == "SIGNAL"
    assert decide_b17({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b17({**base, "mean_ci95_block_boot": (-0.1, 2.8), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b17({**base, "mean_pips": -0.5}) == "NONE"
    assert decide_b17({"n": 3, "note": "insufficient sample"}) == "NONE"
