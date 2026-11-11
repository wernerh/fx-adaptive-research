from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.fomc import prev_business_day
from fxresearch.post_fomc_reversal import (
    ALPHA, BOOT_BLOCK, ENTRY_HM, EXIT_HM, MIN_EVENTS, MIN_MEAN_PIPS, PRE_END_HM, PRE_START_HM, build_events, counts,
    decide_b43, evaluate, events, frame_from_bars,
)

WEDS = [date(2015, 1, 7) + timedelta(weeks=6 * i) for i in range(60)]


def _q(dates, mids, spread=0.00002):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates))


def _setup(p, r, dates=None):
    ds = dates or WEDS[:len(p)]
    n1 = [d + timedelta(days=1) for d in ds]
    qa = _q([prev_business_day(d) for d in ds], [1.1] * len(ds))
    qb = _q(ds, [1.1 + x * PIP for x in p])
    qs = _q(ds, [1.1] * len(ds))
    qe = _q(n1, [1.2] * len(ds))
    qx = _q(n1, [1.2 + x * PIP for x in r])
    return ds, qa, qb, qs, qe, qx, set(n1)


def test_constants_fixed():
    assert PRE_START_HM == (16, 0) and PRE_END_HM == (13, 55) and ENTRY_HM == (2, 0) and EXIT_HM == (14, 0)
    assert BOOT_BLOCK == 1 and ALPHA == 0.05 and MIN_EVENTS == 40 and MIN_MEAN_PIPS == 1.0


def test_reverses_sign_of_pre_drift():
    df = build_events(*_setup([10.0, -5.0], [-3.0, 4.0]))
    assert list(df["side"]) == [-1.0, 1.0]
    assert np.allclose(df["signed_pips"], [3.0, 4.0])
    assert np.allclose(df["p_pips"], [10.0, -5.0])


def test_exclusions_in_order():
    ds, qa, qb, qs, qe, qx, td = _setup([5.0] * 7, [1.0] * 7)
    td = td - {ds[0] + timedelta(days=1)}
    qb = qb.drop(ds[1])
    qb.loc[ds[2]] = [1.1 - 0.00001, 1.1 + 0.00001]       # P == 0
    qe = qe.drop(ds[3] + timedelta(days=1))
    qx = qx.drop(ds[4] + timedelta(days=1))
    qe.loc[ds[5] + timedelta(days=1), "ask_open"] += 3 * PIP
    df = build_events(ds, qa, qb, qs, qe, qx, td)
    assert list(df["excluded"].iloc[:6]) == ["not_trading_day", "missing_pre", "zero_signal", "missing_entry", "missing_exit",
                                             "entry_skipped_spread"]
    assert pd.isna(df["excluded"].iloc[6])
    assert counts(df)["tested"] == 1


def test_no_look_ahead_side():
    rng = np.random.default_rng(3)
    p = list(rng.normal(0, 20, 50))
    a = build_events(*_setup(p, list(rng.normal(0, 30, 50))))
    b = build_events(*_setup(p, list(rng.normal(0, 30, 50) + 80)))
    assert list(a["side"]) == list(b["side"])


def test_decision_rule():
    base = {"n": 48, "mean_pips": 5.0, "t_p_one_sided": 0.01, "mean_ci95_boot": (0.5, 9.0)}
    assert decide_b43(base) == "SIGNAL"
    assert decide_b43({**base, "n": 39}) == "NONE"
    assert decide_b43({**base, "mean_pips": 0.8}) == "WEAK"
    assert decide_b43({**base, "mean_ci95_boot": (-1.0, 9.0)}) == "WEAK"
    assert decide_b43({**base, "mean_ci95_boot": (-1.0, 9.0), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b43({**base, "mean_pips": -2.0}) == "NONE"


def test_no_edge_on_random_walk():
    rng = np.random.default_rng(0)
    p = list(rng.normal(0, 25, 300))
    r = list(rng.normal(0, 35, 300))
    dates = [date(2015, 1, 7) + timedelta(weeks=i) for i in range(300)]
    ev = events(build_events(*_setup(p, r, dates)))
    res = evaluate(ev["signed_pips"])
    assert res["n"] == 300 and decide_b43(res) == "NONE"


def test_frame_from_synthetic_bars_runs():
    bars = synthetic_bars()
    df = frame_from_bars(bars, [date(2024, 1, 17), date(2024, 2, 14)])
    assert len(df) == 2 and set(df.columns) >= {"signed_pips", "excluded", "tested"}
