from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from fxresearch.data import PIP
from fxresearch.rf_lags import (
    N_LAGS, N_TREES, RANDOM_STATE, REFIT_EVERY, build_daily, feature_matrix, fit_model, grid_returns, labels,
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
    assert N_LAGS == 10 and N_TREES == 51 and REFIT_EVERY == 21 and RANDOM_STATE == 0


def test_grid_returns_features_labels():
    q = _q([1.10, 1.11, np.nan, 1.12, 1.13, 1.12])
    r = grid_returns(q)
    assert np.isnan(r[0]) and np.isnan(r[2]) and np.isnan(r[3])
    assert abs(r[1] - 1e4 * np.log(1.11 / 1.10)) < 1e-9
    X = feature_matrix(r, 3)
    assert X[4, 0] == r[4] and np.isnan(X[4, 1]) and X[5, 1] == r[4]
    assert np.isnan(X[1]).any()
    y = labels(r)
    assert y[3] == 1.0 and y[4] == 0.0 and np.isnan(y[5]) and np.isnan(y[1])


def _const_fitter(calls, p=0.7):
    class M:
        classes_ = np.array([0, 1])

        def predict_proba(self, x):
            return np.array([[1 - p, p]])

    def f(X, y):
        calls.append(len(y))
        return M()
    return f


def test_refit_schedule_training_cutoff_and_skips():
    q = _q(_rw(100))
    first_end = q.index[39]
    calls = []
    df, skips, info = build_daily(q, first_end, refit_every=21, fitter=_const_fitter(calls))
    # usable rows j need lags j-9..j finite (j >= 10) and label date pos j+1 <= cutoff
    assert calls[0] == 39 - 10  # rows 10..38
    assert info["n_fits_attempted"] == 3 and len(calls) == 3  # walk 60 dates (40..99): refits at k=21,42
    assert calls[1] == 61 - 10  # refit at position 61: rows 10..60
    assert skips["no_next"] == 1 and len(df) == 59
    assert (df["signal"] == 1).all()


def test_flat_and_missing_lag_excluded():
    m = _rw(80)
    m[50] = np.nan
    q = _q(m)
    df, skips, _ = build_daily(q, q.index[39], fitter=_const_fitter([], p=0.5))
    assert len(df) == 0 and skips["flat"] > 0
    assert skips["missing_now"] == 1 and skips["missing_next"] == 1 and skips["missing_lag"] == 10  # positions 51..60 contain ret[51]


def test_first_fit_failure_blocks():
    q = _q(_rw(60))
    with pytest.raises(RuntimeError):
        build_daily(q, q.index[29], fitter=lambda X, y: None)


def test_fit_model_single_class_returns_none():
    assert fit_model(np.zeros((5, 10)), np.ones(5)) is None


def test_no_look_ahead_real_fitter():
    m = _rw(330, seed=3)
    first_end = _q(m).index[199]
    a, _, _ = build_daily(_q(m), first_end)
    m2 = m.copy()
    m2[280:] *= np.exp(np.random.default_rng(9).normal(0, 0.01, len(m2) - 280))
    b, _, _ = build_daily(_q(m2), first_end)
    # s(D) for D at position i uses quotes up to i only, so positions <= 279 must match
    ka = a[a["pos"] <= 279][["pos", "p_up", "signal"]].reset_index(drop=True)
    kb = b[b["pos"] <= 279][["pos", "p_up", "signal"]].reset_index(drop=True)
    assert len(ka) > 50
    pd.testing.assert_frame_equal(ka, kb)


def test_learns_obvious_nonlinear_pattern():
    # synthetic: next return sign = sign of current return (strong continuation); RF should pick it up
    rng = np.random.default_rng(5)
    r = np.empty(600)
    r[0] = 1
    for t in range(1, 600):
        r[t] = np.sign(r[t - 1]) * abs(rng.normal(0, 40)) * (1 if rng.random() < 0.9 else -1)
    m = 1.12 * np.exp(np.cumsum(r * PIP / 1.12))
    q = _q(m)
    df, _, _ = build_daily(q, q.index[299])
    assert (df["signed_pips"] > 0).mean() > 0.75


def test_random_walk_gives_no_signal():
    q = _q(_rw(700, seed=4))
    df, _, _ = build_daily(q, q.index[259])
    res = evaluate(df["signed_pips"])
    assert decide_b16(res) != "SIGNAL"
