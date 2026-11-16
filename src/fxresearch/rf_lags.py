"""E051 (backlog B62): random-forest classifier on 10 lagged daily returns, next-day EUR/USD direction, 16:00 NY hold, dev only.

Definitions (fixed in pre-registration, R212, before any run):
* Daily quotes: `tsmom.daily_quotes` (16:00 NY bid/ask open per trading date; NaN where missing), mid = (bid + ask) / 2.
* Return on the trading-date grid: ret[i] = 1e4 x ln(mid16(dates[i]) / mid16(dates[i-1])) (NaN if either quote is missing;
  ret[0] = NaN). Scale is cosmetic (tree splits are scale-invariant).
* Features at position i (trading date D): ret[i], ret[i-1], ..., ret[i-9] (10 lags in trading-date positions); a row is usable
  only if all 10 are finite.
* Label of row i: 1 if ret[i+1] > 0, 0 if ret[i+1] < 0; row dropped from training if ret[i+1] is 0 or NaN. Label date = dates[i+1].
* Model: scikit-learn `RandomForestClassifier(n_estimators=51, random_state=0)`, all other arguments library defaults.
* Fits: first fit on all usable rows with label date <= FIRST_FIT_END. The trading dates after FIRST_FIT_END are walked in order;
  at k = 21, 42, ... (k counted from 0 over ALL walked dates) the model is refitted on all usable rows with label date <= D
  (i.e. rows j <= i - 1) before the signal of D is formed. A fit that raises or has fewer than 2 classes keeps the previous model
  and is counted. If the first fit fails the run is BLOCKED.
* Signal: p(D) = predicted probability of class 1 for the features at D; s = +1 if p > 0.5, -1 if p < 0.5.
* Test dates: walked dates. Excluded and counted, first failing check in this order: `no_next` (last date), `missing_now`,
  `missing_next`, `missing_lag` (any of the 10 features NaN), `flat` (p == 0.5 exactly).
* Signed return = s(D) x (mid16(D+1) - mid16(D)) in pips.
Nothing dated after D enters s(D): features stop at ret[i], training labels stop at label date D.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .data import PIP

N_LAGS = 10
N_TREES = 51
REFIT_EVERY = 21
RANDOM_STATE = 0
SCALE = 1e4


def grid_returns(q: pd.DataFrame) -> np.ndarray:
    """ret[i] = SCALE x ln(mid[i] / mid[i-1]) on the trading-date grid; NaN where a quote is missing; ret[0] = NaN."""
    mid = ((q["bid"] + q["ask"]) / 2).to_numpy(dtype=float)
    ret = np.full(len(mid), np.nan)
    if len(mid) > 1:
        ret[1:] = SCALE * np.log(mid[1:] / mid[:-1])
    return ret


def feature_matrix(ret: np.ndarray, n_lags: int = N_LAGS) -> np.ndarray:
    """X[i] = (ret[i], ret[i-1], ..., ret[i-n_lags+1]); rows with i < n_lags-1 are NaN."""
    n = len(ret)
    X = np.full((n, n_lags), np.nan)
    for j in range(n_lags):
        X[j:, j] = ret[: n - j]
    return X


def labels(ret: np.ndarray) -> np.ndarray:
    """y[i] = 1 if ret[i+1] > 0, 0 if < 0, NaN if 0, NaN or no next."""
    y = np.full(len(ret), np.nan)
    nxt = ret[1:]
    y[:-1] = np.where(nxt > 0, 1.0, np.where(nxt < 0, 0.0, np.nan))
    return y


def fit_model(X: np.ndarray, y: np.ndarray):
    """Fixed RF fit. Returns the fitted model or None if the fit raises or y has fewer than 2 classes."""
    from sklearn.ensemble import RandomForestClassifier

    if len(y) == 0 or len(np.unique(y)) < 2:
        return None
    try:
        m = RandomForestClassifier(n_estimators=N_TREES, random_state=RANDOM_STATE)
        m.fit(X, y.astype(int))
    except Exception:  # noqa: BLE001 - any failure counts as a failed fit
        return None
    return m


def prob_up(model, x: np.ndarray) -> float:
    proba = model.predict_proba(x.reshape(1, -1))[0]
    cls = list(model.classes_)
    return float(proba[cls.index(1)]) if 1 in cls else 0.0


def build_daily(q: pd.DataFrame, first_fit_end, refit_every: int = REFIT_EVERY, n_lags: int = N_LAGS,
                fitter=fit_model) -> tuple[pd.DataFrame, dict, dict]:
    """Walk-forward signals and signed returns. Returns (frame, skips, fit_info). Raises RuntimeError if the first fit fails."""
    bid, ask = q["bid"].to_numpy(dtype=float), q["ask"].to_numpy(dtype=float)
    mid = (bid + ask) / 2
    dates = list(q.index)
    ret = grid_returns(q)
    X = feature_matrix(ret, n_lags)
    y = labels(ret)
    usable = np.isfinite(X).all(axis=1) & np.isfinite(y)
    label_date_pos = np.arange(len(dates)) + 1  # label date of row j is dates[j+1]

    def train(max_label_pos: int):
        sel = usable & (label_date_pos <= max_label_pos)
        return X[sel], y[sel]

    first_end_pos = max((i for i, d in enumerate(dates) if d <= first_fit_end), default=-1)
    Xt, yt = train(first_end_pos)
    model = fitter(Xt, yt)
    if model is None:
        raise RuntimeError("first fit failed: experiment BLOCKED")
    info = {"n_fits_attempted": 1, "n_fit_failures": 0, "first_fit_n": int(len(yt)),
            "first_fit_up_share": round(float(yt.mean()), 4), "fits": [{"fit_date": str(first_fit_end), "n_rows": int(len(yt))}],
            "last_model": model}
    skips = {"no_next": 0, "missing_now": 0, "missing_next": 0, "missing_lag": 0, "flat": 0}
    rows = []
    walk = [i for i, d in enumerate(dates) if d > first_fit_end]
    for k, i in enumerate(walk):
        d = dates[i]
        if k > 0 and k % refit_every == 0:
            info["n_fits_attempted"] += 1
            Xt, yt = train(i)
            new = fitter(Xt, yt)
            if new is None:
                info["n_fit_failures"] += 1
            else:
                model = new
                info["last_model"] = new
                info["fits"].append({"fit_date": str(d), "n_rows": int(len(yt))})
        if i + 1 >= len(dates):
            skips["no_next"] += 1
            continue
        if np.isnan(mid[i]):
            skips["missing_now"] += 1
            continue
        if np.isnan(mid[i + 1]):
            skips["missing_next"] += 1
            continue
        if not np.isfinite(X[i]).all():
            skips["missing_lag"] += 1
            continue
        p = prob_up(model, X[i])
        if p == 0.5:
            skips["flat"] += 1
            continue
        s = 1.0 if p > 0.5 else -1.0
        r = (mid[i + 1] - mid[i]) / PIP
        rows.append({
            "pos": i, "date": d, "next_date": dates[i + 1], "p_up": p, "signal": s, "ret_pips": r,
            "signed_pips": s * r, "entry_spread_pips": (ask[i] - bid[i]) / PIP,
            "exit_spread_pips": (ask[i + 1] - bid[i + 1]) / PIP,
        })
    cols = ["pos", "date", "next_date", "p_up", "signal", "ret_pips", "signed_pips", "entry_spread_pips", "exit_spread_pips"]
    return pd.DataFrame(rows, columns=cols), skips, info
