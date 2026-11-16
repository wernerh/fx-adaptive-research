"""E050 (backlog B60): 2-state Markov switching expected-return rule, daily EUR/USD, 16:00 NY hold, dev only.

Definitions (fixed in pre-registration, R209, before any run):
* Daily quotes: `tsmom.daily_quotes` (16:00 NY bid/ask open per trading date; NaN where missing), mid = (bid + ask) / 2.
* Model return r(D) = 1e4 x ln(mid16(D) / mid16(D-1)) for consecutive trading dates D-1, D in the list where both quotes
  exist (pairs with a missing quote are dropped from the model series and counted). Scale is cosmetic (~pips).
* Model: statsmodels `MarkovRegression(r, k_regimes=2, trend="c", switching_variance=True)`, Gaussian, constant transition
  matrix, default (steady-state) initial probabilities. Labels are not used.
* Fits: first fit on all model returns dated <= FIRST_FIT_END (2015-12-31). Then the trading dates from the first trading date
  after FIRST_FIT_END are walked in order; at positions k = 21, 42, ... (k counted from 0 over ALL these trading dates, test date
  kept or not) the model is refitted on all model returns dated <= D before the signal of D is formed. A fit that raises or
  does not report convergence keeps the previous parameters and is counted. If the first fit fails the run is BLOCKED.
* Filtered probabilities: Hamilton filter with the parameters in force at D, run over all model returns dated <= D (this
  module's own filter, `hamilton_filter`, started from the stationary distribution of the transition matrix).
* E8(D) = sum_{h=1..8} p(D)' P^h mu with p(D) the filtered state probabilities after the last model return dated <= D,
  P[i, j] = Pr(s_t+1 = j | s_t = i), mu the state means. s(D) = sign(E8(D)); E8 == 0 exactly -> s = 0, date excluded (`flat`).
* Test dates: trading dates after FIRST_FIT_END with a next trading date. Excluded and counted in this order: `missing_now`
  (no 16:00 quote on D), `missing_next` (none on D+1), `flat`. The last date is `no_next`.
* Signed return = s(D) x (mid16(D+1) - mid16(D)) in pips.
Nothing dated after D enters s(D) (fit data, filter data and the parameters all stop at D).
"""
from __future__ import annotations

import bisect
import warnings

import numpy as np
import pandas as pd

from .data import PIP

HORIZON = 8
REFIT_EVERY = 21
SCALE = 1e4


def model_returns(q: pd.DataFrame) -> tuple[pd.Series, int]:
    """Model return series indexed by trading date D (return from D-1 to D). Returns (series, dropped pair count)."""
    mid = ((q["bid"] + q["ask"]) / 2).to_numpy(dtype=float)
    dates = list(q.index)
    vals, idx, dropped = [], [], 0
    for i in range(1, len(dates)):
        if np.isnan(mid[i]) or np.isnan(mid[i - 1]):
            dropped += 1
            continue
        vals.append(SCALE * np.log(mid[i] / mid[i - 1]))
        idx.append(dates[i])
    return pd.Series(vals, index=pd.Index(idx, name="trading_date"), dtype=float), dropped


def fit_params(r: np.ndarray) -> dict | None:
    """Fit the fixed 2-state model. Returns {"mu", "sigma", "P", "converged"} or None if the fit raises / does not converge.
    P is row-stochastic: P[i, j] = Pr(next = j | now = i)."""
    import statsmodels.api as sm

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            mod = sm.tsa.MarkovRegression(np.asarray(r, dtype=float), k_regimes=2, trend="c", switching_variance=True)
            res = mod.fit(disp=False)
    except Exception:  # noqa: BLE001 - any failure counts as a failed fit
        return None
    conv = bool(res.mle_retvals.get("converged", False)) if isinstance(res.mle_retvals, dict) else False
    if not conv:
        return None
    p = res.params
    names = list(mod.param_names)
    mu = np.array([p[names.index("const[0]")], p[names.index("const[1]")]], dtype=float)
    sigma = np.sqrt(np.array([p[names.index("sigma2[0]")], p[names.index("sigma2[1]")]], dtype=float))
    # statsmodels regime_transition[i, j, 0] = Pr(s_t = i | s_t-1 = j)  (columns sum to 1)
    T = np.asarray(mod.regime_transition_matrix(p))[:, :, 0]
    P = T.T
    if not (np.all(np.isfinite(mu)) and np.all(np.isfinite(sigma)) and np.all(sigma > 0) and np.all(np.isfinite(P))):
        return None
    return {"mu": mu, "sigma": sigma, "P": P}


def stationary(P: np.ndarray) -> np.ndarray:
    """Stationary distribution of a 2-state row-stochastic matrix."""
    a, b = 1 - P[0, 0], 1 - P[1, 1]
    if a + b <= 0:
        return np.array([0.5, 0.5])
    return np.array([b / (a + b), a / (a + b)])


def hamilton_filter(r: np.ndarray, mu: np.ndarray, sigma: np.ndarray, P: np.ndarray) -> np.ndarray:
    """Filtered probabilities Pr(s_t | r_1..r_t), shape (len(r), 2). Row t uses r[:t+1] only."""
    r = np.asarray(r, dtype=float)
    out = np.empty((len(r), 2))
    prev = stationary(P)
    for t, x in enumerate(r):
        pred = prev @ P
        dens = np.exp(-0.5 * ((x - mu) / sigma) ** 2) / sigma
        post = pred * dens
        s = post.sum()
        post = pred if (not np.isfinite(s) or s <= 0) else post / s
        out[t] = post
        prev = post
    return out


def expected_return(p: np.ndarray, P: np.ndarray, mu: np.ndarray, horizon: int = HORIZON) -> float:
    """E_H = sum_{h=1..H} p' P^h mu."""
    total, v = 0.0, np.asarray(p, dtype=float)
    for _ in range(horizon):
        v = v @ P
        total += float(v @ mu)
    return total


def build_daily(q: pd.DataFrame, first_fit_end, refit_every: int = REFIT_EVERY, horizon: int = HORIZON,
                fitter=fit_params) -> tuple[pd.DataFrame, dict, dict]:
    """Walk-forward signals and signed returns. Returns (frame, skips, fit_info). Raises RuntimeError if the first fit fails."""
    bid, ask = q["bid"].to_numpy(dtype=float), q["ask"].to_numpy(dtype=float)
    mid = (bid + ask) / 2
    dates = list(q.index)
    rser, dropped = model_returns(q)
    rdates = list(rser.index)
    rv = rser.to_numpy()

    def upto(d):  # number of model returns dated <= d
        return bisect.bisect_right(rdates, d)

    first = fitter(rv[:upto(first_fit_end)])
    if first is None:
        raise RuntimeError("first fit failed: experiment BLOCKED")
    params = first
    info = {"dropped_model_pairs": dropped, "n_fits_attempted": 1, "n_fit_failures": 0,
            "first_fit_n": upto(first_fit_end), "fits": [_summ(first, str(first_fit_end), upto(first_fit_end))]}
    skips = {"missing_now": 0, "missing_next": 0, "flat": 0, "no_next": 0}
    rows = []
    walk = [i for i, d in enumerate(dates) if d > first_fit_end]
    for k, i in enumerate(walk):
        d = dates[i]
        if k > 0 and k % refit_every == 0:
            info["n_fits_attempted"] += 1
            n = upto(d)
            new = fitter(rv[:n])
            if new is None:
                info["n_fit_failures"] += 1
            else:
                params = new
                info["fits"].append(_summ(new, str(d), n))
        if i + 1 >= len(dates):
            skips["no_next"] += 1
            continue
        if np.isnan(mid[i]):
            skips["missing_now"] += 1
            continue
        if np.isnan(mid[i + 1]):
            skips["missing_next"] += 1
            continue
        n = upto(d)
        filt = hamilton_filter(rv[:n], params["mu"], params["sigma"], params["P"])
        e8 = expected_return(filt[-1], params["P"], params["mu"], horizon)
        s = float(np.sign(e8))
        if s == 0:
            skips["flat"] += 1
            continue
        ret = (mid[i + 1] - mid[i]) / PIP
        rows.append({
            "pos": i, "date": d, "next_date": dates[i + 1], "e8": e8, "signal": s, "ret_pips": ret,
            "signed_pips": s * ret, "entry_spread_pips": (ask[i] - bid[i]) / PIP,
            "exit_spread_pips": (ask[i + 1] - bid[i + 1]) / PIP,
            "mean_state_sd": float(params["sigma"].mean()),
        })
    cols = ["pos", "date", "next_date", "e8", "signal", "ret_pips", "signed_pips", "entry_spread_pips",
            "exit_spread_pips", "mean_state_sd"]
    return pd.DataFrame(rows, columns=cols), skips, info


def _summ(p: dict, d: str, n: int) -> dict:
    return {"fit_date": d, "n_obs": n, "mu": [round(float(x), 4) for x in p["mu"]],
            "sigma": [round(float(x), 4) for x in p["sigma"]],
            "p_stay": [round(float(p["P"][0, 0]), 4), round(float(p["P"][1, 1]), 4)]}
