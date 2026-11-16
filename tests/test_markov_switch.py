from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from fxresearch.data import PIP
from fxresearch.markov_switch import (
    HORIZON, REFIT_EVERY, build_daily, expected_return, fit_params, hamilton_filter, model_returns, stationary,
)
from fxresearch.tsmom import decide_b16, evaluate


def _q(mids, spread=0.4, start=date(2015, 1, 1)):
    mids = np.asarray(mids, dtype=float)
    idx = pd.Index([start + timedelta(days=i) for i in range(len(mids))], name="trading_date")
    h = spread * PIP / 2
    return pd.DataFrame({"bid": mids - h, "ask": mids + h}, index=idx)


def _rw(n, seed=0, sd=45):
    rng = np.random.default_rng(seed)
    return 1.12 * np.exp(np.cumsum(rng.normal(0, sd * PIP / 1.12, n)))


def test_constants_fixed():
    assert HORIZON == 8 and REFIT_EVERY == 21


def test_model_returns_drops_pairs_with_missing_quote():
    q = _q([1.10, 1.11, np.nan, 1.12, 1.13])
    r, dropped = model_returns(q)
    assert dropped == 2 and len(r) == 2
    assert abs(r.iloc[0] - 1e4 * np.log(1.11 / 1.10)) < 1e-9


def test_stationary_and_expected_return():
    P = np.array([[0.9, 0.1], [0.2, 0.8]])
    pi = stationary(P)
    assert np.allclose(pi @ P, pi)
    mu = np.array([1.0, -1.0])
    # from the stationary distribution the expected return per step is pi @ mu each step
    assert abs(expected_return(pi, P, mu, 8) - 8 * float(pi @ mu)) < 1e-12
    # certain in state 0 with P = I: H x mu0
    assert abs(expected_return(np.array([1.0, 0.0]), np.eye(2), mu, 8) - 8.0) < 1e-12


def test_hamilton_filter_uses_only_past():
    rng = np.random.default_rng(1)
    r = rng.normal(0, 1, 200)
    mu, sig, P = np.array([0.5, -0.5]), np.array([0.5, 2.0]), np.array([[0.95, 0.05], [0.1, 0.9]])
    a = hamilton_filter(r, mu, sig, P)
    r2 = r.copy()
    r2[120:] = 50.0
    b = hamilton_filter(r2, mu, sig, P)
    assert np.allclose(a[:120], b[:120])
    assert np.allclose(a.sum(axis=1), 1.0)


def test_filter_detects_obvious_regime():
    r = np.r_[np.full(50, 3.0), np.full(50, -3.0)]
    f = hamilton_filter(r, np.array([3.0, -3.0]), np.array([1.0, 1.0]), np.array([[0.95, 0.05], [0.05, 0.95]]))
    assert f[49, 0] > 0.99 and f[99, 1] > 0.99


def test_fit_params_recovers_two_states():
    rng = np.random.default_rng(2)
    states = np.repeat([0, 1, 0, 1], 150)
    r = np.where(states == 0, rng.normal(5, 1, len(states)), rng.normal(-5, 3, len(states)))
    p = fit_params(r)
    assert p is not None
    assert np.allclose(p["P"].sum(axis=1), 1.0)
    assert sorted(np.round(p["mu"]).tolist()) == [-5.0, 5.0]


def _fake_fitter(calls):
    def f(r):
        calls.append(len(r))
        return {"mu": np.array([1.0, -1.0]), "sigma": np.array([1.0, 1.0]), "P": np.array([[0.9, 0.1], [0.1, 0.9]])}
    return f


def test_refit_schedule_and_skips():
    m = _rw(100)
    q = _q(m)
    first_end = q.index[29]
    calls = []
    df, skips, info = build_daily(q, first_end, refit_every=21, fitter=_fake_fitter(calls))
    # walk has 70 dates (positions 30..99); refits at k = 21, 42, 63
    assert info["n_fits_attempted"] == 4 and len(calls) == 4
    assert calls[0] == 29  # returns dated <= position 29
    assert calls[1] == 29 + 22  # k=21 -> position 51 -> returns dated <= position 51
    assert skips["no_next"] == 1 and len(df) == 69


def test_first_fit_failure_blocks():
    q = _q(_rw(60))
    with pytest.raises(RuntimeError):
        build_daily(q, q.index[29], fitter=lambda r: None)


def test_failed_refit_keeps_params_and_counts():
    q = _q(_rw(80))
    n = {"c": 0}

    def f(r):
        n["c"] += 1
        if n["c"] == 1:
            return {"mu": np.array([1.0, -1.0]), "sigma": np.array([1.0, 1.0]), "P": np.eye(2) * 0.8 + 0.1}
        return None
    df, _, info = build_daily(q, q.index[29], refit_every=21, fitter=f)
    assert info["n_fit_failures"] == info["n_fits_attempted"] - 1 >= 1
    assert len(df) > 0


def test_no_look_ahead_real_fitter():
    m = _rw(330, seed=3)
    q = _q(m)
    first_end = q.index[259]
    a, _, _ = build_daily(q, first_end)
    m2 = m.copy()
    m2[300:] *= 1.05
    b, _, _ = build_daily(_q(m2), first_end)
    ka = a[a["pos"] + 1 < 300].reset_index(drop=True)
    kb = b[b["pos"] + 1 < 300].reset_index(drop=True)
    assert len(ka) > 20
    pd.testing.assert_frame_equal(ka, kb)


def test_random_walk_gives_no_signal():
    q = _q(_rw(600, seed=4))
    df, _, _ = build_daily(q, q.index[259])
    res = evaluate(df["signed_pips"])
    assert decide_b16(res) != "SIGNAL"
