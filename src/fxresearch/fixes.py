"""Fixing-window signal tests (E007 London 4pm WM/Reuters fix; reusable for ECB / Tokyo fixes).

Each test is a fixed direction held over a local-clock window around a fix:
  pre  window: short EUR/USD (USD bought into the fix)  -> signal -1
  post window: long EUR/USD (USD reverses after the fix) -> signal +1
Signals are constant (calendar-only), so they cannot look ahead.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import time

import pandas as pd

from .predictive import evaluate_predictor


@dataclass(frozen=True)
class FixTest:
    name: str
    window: str          # key into the windows dict
    direction: int       # +1 long EUR/USD, -1 short
    month_end_only: bool


def month_end_flag(dates: pd.Index) -> pd.Series:
    """True on the last trading date of each calendar month present in `dates`."""
    d = pd.to_datetime(pd.Index(dates))
    s = pd.Series(d, index=pd.Index(dates))
    last = s.groupby([d.year, d.month]).transform("max")
    return pd.Series((s == last).to_numpy(), index=pd.Index(dates))


LONDON_FIX_WINDOWS = {
    "ldn_fix_pre": ("Europe/London", time(15, 0), time(16, 0)),
    "ldn_fix_post": ("Europe/London", time(16, 0), time(17, 0)),
}

E007_TESTS = (
    FixTest("pre_all", "ldn_fix_pre", -1, False),
    FixTest("post_all", "ldn_fix_post", +1, False),
    FixTest("pre_month_end", "ldn_fix_pre", -1, True),
    FixTest("post_month_end", "ldn_fix_post", +1, True),
)


def decide(res: dict, n_trials: int, min_mean_pips: float = 1.0, alpha: float = 0.05) -> str:
    """Pre-registered E007 rule for one test: SIGNAL / WEAK / NONE.

    SIGNAL: mean signed pips > min_mean_pips AND block-bootstrap 95% CI lower bound > 0
            AND binomial p < alpha / n_trials.
    WEAK:   mean signed > 0 with CI lower bound > 0 or binom p < alpha, but not SIGNAL.
    NONE:   otherwise.
    """
    if "mean_signed_pips" not in res:
        return "NONE"
    m = res["mean_signed_pips"]
    lo = res["mean_signed_ci95_block_boot"][0]
    p = res["binom_p"]
    if m > min_mean_pips and lo > 0 and p < alpha / n_trials:
        return "SIGNAL"
    if m > 0 and (lo > 0 or p < alpha):
        return "WEAK"
    return "NONE"


def run_fix_tests(feats: pd.DataFrame, split: pd.Series, tests=E007_TESTS, blocks=("dev",)) -> pd.DataFrame:
    """`feats` must hold columns y_<window>_ret_pips, indexed by trading date."""
    me = month_end_flag(feats.index)
    rows = []
    for block in blocks:
        mask = (split.reindex(feats.index) == block).to_numpy()
        for t in tests:
            m = mask & (me.to_numpy() if t.month_end_only else True)
            f = feats[m]
            y = f[f"y_{t.window}_ret_pips"]
            res = evaluate_predictor(pd.Series(float(t.direction), index=f.index), y)
            res["mean_abs_window_pips"] = round(float(y.abs().mean()), 3) if len(y) else None
            res["decision"] = decide(res, n_trials=len(tests))
            rows.append({"block": block, "test": t.name, "window": t.window,
                         "direction": t.direction, "month_end_only": t.month_end_only, **res})
    return pd.DataFrame(rows)
