from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.btc_lag import (
    END, EXCLUSION_ORDER, MAX_ABS_B, MIN_BOTH_VALID_SHARE, MIN_EVENTS, SIGN, START, btc_mids, build_daily, data_gate,
    decide_b64,
)
from fxresearch.data import PIP, synthetic_bars
from fxresearch.sessions import trading_date
from fxresearch.tsmom import daily_quotes, evaluate


def _q(mids, start=date(2018, 1, 1), spread=0.4):
    mids = np.asarray(mids, dtype=float)
    idx = pd.Index([start + timedelta(days=i) for i in range(len(mids))], name="trading_date")
    h = spread * PIP / 2
    return pd.DataFrame({"bid": mids - h, "ask": mids + h}, index=idx)


def test_constants_fixed():
    assert START == date(2017, 5, 9) and END == date(2020, 12, 31)
    assert MAX_ABS_B == 0.50 and MIN_BOTH_VALID_SHARE == 0.90 and MIN_EVENTS == 500 and SIGN == 1.0
    assert EXCLUSION_ORDER == ("no_next", "missing_now", "missing_next", "missing_btc", "zero_signal", "btc_jump")


def test_signal_sign_return_and_exclusions():
    q = _q([1.10, 1.11, 1.12, np.nan, 1.13, 1.14, 1.15, 1.16, 1.17])
    btc = np.array([100, 110, 99, 120, 130, 130, np.nan, 300, 310], dtype=float)
    df, sk = build_daily(q, btc, start=q.index[0], end=q.index[-1])
    # i=1: B=ln(110/100)>0 -> long, move 1.11->1.12 = +100 pips
    r1 = df[df["pos"] == 1].iloc[0]
    assert r1["signal"] == 1.0 and abs(r1["signed_pips"] - 100) < 1e-6
    assert abs(r1["b"] - np.log(1.1)) < 1e-12
    assert sk["missing_next"] == 1      # i=2 (next missing)
    assert sk["missing_now"] == 1       # i=3
    # i=4: B=ln(130/120)>0 long, 1.13->1.14
    assert df[df["pos"] == 4].iloc[0]["signed_pips"] > 0
    assert sk["zero_signal"] == 1       # i=5
    assert sk["missing_btc"] == 2       # i=6 (now NaN), i=7 (prev NaN)
    assert sk["no_next"] == 1           # i=8
    assert sk["btc_jump"] == 0
    assert len(df) == 2


def test_short_on_btc_down_and_jump_guard():
    q = _q([1.10, 1.11, 1.12, 1.13])
    btc = np.array([100, 90, 300, 290], dtype=float)
    df, sk = build_daily(q, btc, start=q.index[0], end=q.index[-1])
    r = df[df["pos"] == 1].iloc[0]
    assert r["signal"] == -1.0 and abs(r["signed_pips"] + 100) < 1e-6
    assert sk["btc_jump"] == 1          # i=2: ln(300/90) > 0.5


def test_date_window_respected():
    q = _q(np.linspace(1.1, 1.2, 10))
    btc = np.linspace(100, 200, 10)
    df, _ = build_daily(q, btc, start=q.index[3], end=q.index[5])
    assert list(df["pos"]) == [3, 4, 5]


def test_data_gate():
    q = _q(np.full(21, 1.1))
    btc = np.full(21, 100.0)
    btc[5] = np.nan      # breaks dates 5 and 6
    g = data_gate(q, btc, 10, start=q.index[1], end=q.index[-1])
    assert g["ok"] and g["dates_in_range"] == 20 and g["dates_both_valid"] == 18
    btc[10] = np.nan     # breaks 10 and 11 -> 16/20 = 0.8
    assert not data_gate(q, btc, 10, start=q.index[1], end=q.index[-1])["ok"]
    assert not data_gate(q, btc, 0, start=q.index[1], end=q.index[-1])["ok"]


def test_decide_min_events():
    assert decide_b64({"n": 499, "mean_pips": 5.0, "t_p_one_sided": 0.001, "mean_ci95_block_boot": (1.0, 9.0)}) == "NONE"
    assert decide_b64({"n": 600, "mean_pips": 5.0, "t_p_one_sided": 0.001, "mean_ci95_block_boot": (1.0, 9.0)}) == "SIGNAL"
    assert decide_b64({"n": 600, "mean_pips": 0.5, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (-1.0, 2.0)}) == "WEAK"
    assert decide_b64({"n": 600, "mean_pips": -0.5, "t_p_one_sided": 0.9, "mean_ci95_block_boot": (-2.0, 1.0)}) == "NONE"


def _bars_pair():
    fx = synthetic_bars("2024-01-01", "2024-03-01", seed=3)
    btc = synthetic_bars("2024-01-01", "2024-03-01", seed=11)
    for c in btc.columns:
        btc[c] = btc[c] * 40000.0
    return fx, btc


def test_btc_mids_ny_1600_open():
    fx, btc = _bars_pair()
    q = daily_quotes(fx)
    m = btc_mids(btc, q.index)
    d = q.index[5]
    ts = pd.Timestamp(f"{d} 16:00", tz="America/New_York").tz_convert("UTC")
    row = btc.loc[ts]
    assert abs(m[5] - (row["bid_open"] + row["ask_open"]) / 2) < 1e-6
    assert np.isnan(btc_mids(btc.iloc[:0], q.index)).all()


def test_no_look_ahead_truncation():
    fx, btc = _bars_pair()
    q_full = daily_quotes(fx)
    full, _ = build_daily(q_full, btc_mids(btc, q_full.index), start=q_full.index[0], end=q_full.index[-1])
    k = 20
    d = q_full.index[k]
    cut = pd.Timestamp(f"{d} 16:00", tz="America/New_York").tz_convert("UTC")
    btc_t = btc[btc.index <= cut]           # BTC through the 16:00 NY D bar open only
    fx_t = fx[fx.index <= cut]
    q_t = daily_quotes(fx_t)
    m_t = btc_mids(btc_t, q_t.index)
    b_full = full.set_index("pos").loc[k, "signal"]
    b_t = np.sign(np.log(m_t[k]) - np.log(m_t[k - 1]))
    assert b_full == SIGN * b_t
    # perturbing BTC after the cut leaves the signal at D unchanged
    btc2 = btc.copy()
    btc2.loc[btc2.index > cut, ["bid_open", "ask_open"]] *= 3.0
    alt, _ = build_daily(q_full, btc_mids(btc2, q_full.index), start=q_full.index[0], end=q_full.index[-1])
    assert alt.set_index("pos").loc[k, "signal"] == b_full


def test_random_walk_no_signal():
    rng = np.random.default_rng(0)
    n = 1200
    fx = 1.12 * np.exp(np.cumsum(rng.normal(0, 45 * PIP / 1.12, n)))
    btc = 10000 * np.exp(np.cumsum(rng.normal(0, 0.04, n)))
    q = _q(fx, start=date(2017, 1, 1))
    df, _ = build_daily(q, btc, start=q.index[0], end=q.index[-1])
    res = evaluate(df["signed_pips"])
    assert decide_b64(res) != "SIGNAL"


def test_synthetic_bars_end_to_end_trading_dates():
    fx, btc = _bars_pair()
    q = daily_quotes(fx)
    assert set(q.index) == set(trading_date(fx.index))
    df, sk = build_daily(q, btc_mids(btc, q.index), start=q.index[0], end=q.index[-1])
    assert len(df) + sum(sk.values()) == len(q) - 1
