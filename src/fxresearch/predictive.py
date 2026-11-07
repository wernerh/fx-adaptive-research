"""Experiment E001: does pre-US session structure predict US-session direction?

This is a cost-free statistical test of the core hypothesis. If no conditional
signal exists here, there is little point backtesting strategies built on it.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .metrics import block_bootstrap_mean_ci, wilson_interval

# Candidate predictors: name -> function(feats) returning +1/-1/0 per day.
PREDICTORS = {
    # Unconditional benchmark. Breedon & Ranaldo (2013) document currencies depreciating in their
    # own trading hours, which implies a time-of-day drift in EUR/USD. Conditional predictors must
    # beat this, not just 50%.
    "unconditional_long": lambda f: pd.Series(1.0, index=f.index),
    "london_ret_sign": lambda f: np.sign(f["london_ret_pips"]),
    "asia_ret_sign": lambda f: np.sign(f["asia_ret_pips"]),
    "lon_break_side": lambda f: f["lon_break_side"].fillna(0),
    "lon_break_held": lambda f: f["lon_break_side"].fillna(0) * (1 - f["lon_closed_inside_asia"].fillna(0)),
    "lon_false_break_fade": lambda f: -f["lon_break_side"].fillna(0) * f["lon_closed_inside_asia"].fillna(0),
    "asia_london_agree": lambda f: np.where(
        np.sign(f["asia_ret_pips"]) == np.sign(f["london_ret_pips"]), np.sign(f["london_ret_pips"]), 0
    ),
}


def evaluate_predictor(signal: pd.Series, y_ret_pips: pd.Series) -> dict:
    df = pd.DataFrame({"s": signal, "y": y_ret_pips}).dropna()
    active = df[df["s"] != 0]
    n = len(active)
    if n < 30:
        return {"n_active": n, "note": "insufficient sample"}
    signed = active["s"] * active["y"]          # pips captured by trading the sign, before costs
    hits = int((signed > 0).sum())
    lo, hi = wilson_interval(hits, n)
    binom_p = stats.binomtest(hits, n, 0.5).pvalue
    if df["s"].nunique() > 1:
        rho, rho_p = stats.spearmanr(df["s"], df["y"])
    else:  # constant signal (e.g. unconditional benchmark): IC undefined
        rho, rho_p = float("nan"), float("nan")
    b_lo, b_hi = block_bootstrap_mean_ci(signed.to_numpy())
    return {
        "n_days": int(len(df)),
        "n_active": n,
        "coverage": round(n / len(df), 3),
        "hit_rate": round(hits / n, 4),
        "hit_rate_ci95": (round(lo, 4), round(hi, 4)),
        "binom_p": round(float(binom_p), 4),
        "mean_signed_pips": round(float(signed.mean()), 3),
        "mean_signed_ci95_block_boot": (round(b_lo, 3), round(b_hi, 3)),
        "spearman_ic": round(float(rho), 4),
        "spearman_p": round(float(rho_p), 4),
    }


def run_baseline(feats: pd.DataFrame, split: pd.Series, outcome: str = "y_us_ret_pips",
                 n_trials: int | None = None) -> pd.DataFrame:
    """Evaluate every predictor against `outcome` per block.

    `n_trials` is the Bonferroni multiplier; defaults to the number of predictors.
    Pass a larger number when several outcome windows are tested together.
    """
    rows = []
    for block in ("dev", "val", "oos"):
        f = feats[split.reindex(feats.index) == block]
        if f.empty:
            continue
        for name, fn in PREDICTORS.items():
            res = evaluate_predictor(pd.Series(fn(f), index=f.index), f[outcome])
            rows.append({"block": block, "outcome": outcome, "predictor": name, **res})
    out = pd.DataFrame(rows)
    if "binom_p" in out:
        out["binom_p_bonferroni"] = (out["binom_p"] * (n_trials or len(PREDICTORS))).clip(upper=1.0)
    return out
