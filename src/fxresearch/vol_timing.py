"""Volatility timing tests (E008): do pre-US session ranges predict the SIZE of the US move?

Not a direction test. The statistic is the PARTIAL Spearman correlation between a pre-US session
range (pips, known before 08:00 New York) and the absolute US-window return (pips), controlling for
the prior-day ATR (`atr_pips_prior`, prior days only). It asks whether today's *relative* activity
(the "range/ATR" idea) carries information beyond the volatility regime.

Why partial correlation and not range/ATR vs |move|/ATR: dividing both sides by the same noisy ATR
creates a spurious positive correlation (shared-denominator bias; about +0.02..+0.04 on a
constant-volatility random walk, found while building the tests, before any real data was used).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.stats import rankdata, spearmanr, t as t_dist


@dataclass(frozen=True)
class VolTest:
    name: str
    predictor: str   # signal-safe feature column
    outcome: str     # y_ column with signed window return in pips


E008_PREDICTORS = ("asia_range_pips", "london_range_pips")
CONTROL = "atr_pips_prior"
E008_OUTCOMES = {"us_session": "y_us_ret_pips", "us_0800_0900": "y_us_0800_0900_ret_pips"}
E008_TESTS = tuple(VolTest(f"{p}__{o}", p, col) for p in E008_PREDICTORS for o, col in E008_OUTCOMES.items())

MIN_IC = 0.10
ALPHA = 0.01


def partial_spearman(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> tuple[float, float]:
    """Spearman correlation of x and y controlling for z (Pearson on rank residuals). Returns (rho, p)."""
    rx, ry, rz = (rankdata(np.asarray(v, dtype=float)) for v in (x, y, z))
    Z = np.column_stack([np.ones_like(rz), rz])
    ex = rx - Z @ np.linalg.lstsq(Z, rx, rcond=None)[0]
    ey = ry - Z @ np.linalg.lstsq(Z, ry, rcond=None)[0]
    denom = np.sqrt((ex @ ex) * (ey @ ey))
    if denom == 0:
        return (float("nan"), float("nan"))
    r = float(ex @ ey / denom)
    df = len(rx) - 3
    tstat = r * np.sqrt(df / max(1e-12, 1 - r * r))
    return (r, float(2 * t_dist.sf(abs(tstat), df)))


def block_bootstrap_spearman_ci(x: np.ndarray, y: np.ndarray, z: np.ndarray | None = None, block: int = 20,
                                n_boot: int = 2000, seed: int = 0, alpha: float = 0.05) -> tuple[float, float]:
    """Moving-block bootstrap CI of (partial, if z given) Spearman's rho on time-ordered observations."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    if n < block * 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    k = int(np.ceil(n / block))
    starts = rng.integers(0, n - block + 1, size=(n_boot, k))
    offs = np.arange(block)
    rhos = np.empty(n_boot)
    for i, row in enumerate(starts):
        idx = (row[:, None] + offs[None, :]).ravel()[:n]
        rhos[i] = spearmanr(x[idx], y[idx]).statistic if z is None else partial_spearman(x[idx], y[idx], z[idx])[0]
    return (float(np.nanquantile(rhos, alpha / 2)), float(np.nanquantile(rhos, 1 - alpha / 2)))


def decide(res: dict, min_ic: float = MIN_IC, alpha: float = ALPHA) -> str:
    """USEFUL if IC > min_ic AND p < alpha AND block-bootstrap CI lower > 0; else NOT_USEFUL."""
    ic, p, ci = res.get("spearman_ic"), res.get("spearman_p"), res.get("ic_ci95_block_boot")
    if ic is None or p is None or ci is None or any(pd.isna(v) for v in (ic, p, ci[0])):
        return "NOT_USEFUL"
    return "USEFUL" if (ic > min_ic and p < alpha and ci[0] > 0) else "NOT_USEFUL"


def evaluate_vol_test(feats: pd.DataFrame, test: VolTest) -> dict:
    df = pd.DataFrame({"x": feats[test.predictor], "z": feats[CONTROL],
                       "y_pips": feats[test.outcome].abs()}).dropna().sort_index()
    df["y"] = df["y_pips"] / df["z"]
    out = {"test": test.name, "predictor": test.predictor, "outcome": test.outcome, "n": int(len(df))}
    if len(df) < 60:
        return {**out, "note": "insufficient sample", "decision": "NOT_USEFUL"}
    rho, p = partial_spearman(df["x"].to_numpy(), df["y_pips"].to_numpy(), df["z"].to_numpy())
    out["spearman_ic"] = round(rho, 4)   # partial Spearman | prior ATR (the decision statistic)
    out["spearman_p"] = p
    lo, hi = block_bootstrap_spearman_ci(df["x"].to_numpy(), df["y_pips"].to_numpy(), df["z"].to_numpy())
    out["ic_ci95_block_boot"] = (round(lo, 4), round(hi, 4))
    # Descriptive only (no decision): terciles of range/ATR, outcome means, and the plain raw-pips IC.
    terc = pd.qcut((df["x"] / df["z"]).rank(method="first"), 3, labels=["low", "mid", "high"])
    out["tercile_mean_abs_over_atr"] = {k: round(float(v), 4) for k, v in df.groupby(terc, observed=True)["y"].mean().items()}
    out["tercile_mean_abs_pips"] = {k: round(float(v), 2) for k, v in df.groupby(terc, observed=True)["y_pips"].mean().items()}
    out["spearman_ic_raw_pips_descriptive"] = round(float(spearmanr(df["x"], df["y_pips"]).statistic), 4)
    out["decision"] = decide(out)
    return out


def run_vol_tests(feats: pd.DataFrame, split: pd.Series, tests=E008_TESTS, blocks=("dev",)) -> pd.DataFrame:
    rows = []
    for b in blocks:
        sub = feats[(split == b).to_numpy()]
        for t in tests:
            rows.append({"block": b, **evaluate_vol_test(sub, t)})
    return pd.DataFrame(rows)
