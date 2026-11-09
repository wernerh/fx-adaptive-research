from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.tsmom import (
    BOOT_BLOCK, LOOKBACK, MIN_MEAN_PIPS, build_daily, cost_summary, daily_quotes, decide_b16, evaluate,
    position_runs,
)


def _q(mids, spread=0.4, start=date(2015, 1, 1)):
    mids = np.asarray(mids, dtype=float)
    idx = pd.Index([start + timedelta(days=i) for i in range(len(mids))], name="trading_date")
    h = spread * PIP / 2
    return pd.DataFrame({"bid": mids - h, "ask": mids + h}, index=idx)


def test_constants_fixed():
    assert LOOKBACK == 252 and MIN_MEAN_PIPS == 1.0 and BOOT_BLOCK == 20


def test_signal_and_return_definition_small_lookback():
    q = _q([1.10, 1.11, 1.12, 1.11, 1.09])
    df, skips = build_daily(q, lookback=2)
    # i=2: sign(1.12-1.10)=+1, r = 1.11-1.12 = -100 pips; i=3: sign(1.11-1.11)=0; last date has no next
    assert list(df["pos"]) == [2, 3]
    assert df.loc[0, "signal"] == 1.0 and abs(df.loc[0, "ret_pips"] + 100) < 1e-6 and abs(df.loc[0, "signed_pips"] + 100) < 1e-6
    assert df.loc[1, "signal"] == 0.0 and df.loc[1, "signed_pips"] == 0.0
    assert skips["no_next"] == 1


def test_missing_quotes_excluded_in_order():
    m = [1.10, 1.11, 1.12, 1.13, 1.14, 1.15]
    q = _q(m)
    q.iloc[0] = np.nan   # past for i=2
    q.iloc[4] = np.nan   # now for i=4, next for i=3
    df, skips = build_daily(q, lookback=2)
    assert df.empty
    assert skips == {"missing_now": 1, "missing_past": 1, "missing_next": 1, "no_next": 1}


def test_no_look_ahead():
    rng = np.random.default_rng(0)
    m = 1.1 + np.cumsum(rng.normal(0, 40 * PIP, 400))
    a, _ = build_daily(_q(m))
    m2 = m.copy()
    m2[300:] += 0.05   # change prices from date 300 on
    b, _ = build_daily(_q(m2))
    keep = a["pos"] + 1 < 300
    pd.testing.assert_frame_equal(a[keep].reset_index(drop=True), b[b["pos"] + 1 < 300].reset_index(drop=True))


def test_daily_quotes_from_bars_uses_1600_ny_open():
    bars = synthetic_bars("2024-03-04", "2024-03-09")
    q = daily_quotes(bars)
    d = date(2024, 3, 5)
    ts = pd.Timestamp("2024-03-05 16:00", tz="America/New_York").tz_convert("UTC")
    assert abs(q.loc[d, "bid"] - bars.loc[ts, "bid_open"]) < 1e-12
    assert abs(q.loc[d, "ask"] - bars.loc[ts, "ask_open"]) < 1e-12


def test_runs_and_costs():
    # signals +1,+1,-1 on consecutive positions -> 2 round trips, 1 flip
    df = pd.DataFrame({"pos": [5, 6, 7], "date": [1, 2, 3], "next_date": [2, 3, 4], "signal": [1.0, 1.0, -1.0],
                       "ret_pips": [10.0, -4.0, 6.0], "signed_pips": [10.0, -4.0, -6.0],
                       "entry_spread_pips": [0.4, 0.6, 0.8], "exit_spread_pips": [0.6, 0.8, 1.0]})
    runs = position_runs(df)
    assert len(runs) == 2 and list(runs["n_days"]) == [2, 1]
    assert abs(runs.loc[0, "net_bidask_pips"] - (6.0 - (0.4 + 0.8) / 2)) < 1e-9
    c = cost_summary(df)
    assert c["n_round_trips"] == 2 and c["n_sign_flips"] == 1
    assert c["mean_net_spec4_pips_per_day"] < c["mean_net_bidask_pips_per_day"] < c["mean_signed_mid_pips_per_day"]
    assert c["mean_net_costs_x1_5_pips_per_day"] < c["mean_net_spec4_pips_per_day"]


def test_random_walk_no_signal():
    for seed in range(5):
        rng = np.random.default_rng(seed)
        m = 1.1 + np.cumsum(rng.normal(0, 45 * PIP, 1600))
        df, _ = build_daily(_q(m))
        res = evaluate(df["signed_pips"])
        assert res["n"] == 1600 - LOOKBACK - 1
        assert decide_b16(res) != "SIGNAL"


def test_strong_trend_gives_signal():
    rng = np.random.default_rng(1)
    m = 1.1 + np.cumsum(rng.normal(8 * PIP, 20 * PIP, 1600))
    df, _ = build_daily(_q(m))
    assert decide_b16(evaluate(df["signed_pips"])) == "SIGNAL"


def test_decide_rule_edges():
    base = {"mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.2, 2.8)}
    assert decide_b16(base) == "SIGNAL"
    assert decide_b16({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b16({**base, "mean_ci95_block_boot": (-0.1, 2.8), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b16({**base, "mean_pips": -0.5}) == "NONE"
    assert decide_b16({"n": 3, "note": "insufficient sample"}) == "NONE"
