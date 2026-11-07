"""E009: exploratory hourly return profile scan (DEV ONLY).

Per (date, hour) the mid return over the clock hour (close of last bar minus open of first bar, pips),
kept only if the hour has >= 55 of 60 one-minute bars. Cells:
  * utc_hour            24 cells, date = UTC calendar date
  * ny_hour             24 cells, date = FX trading date (17:00 New York roll), hour on the NY clock
  * weekday_x_ny_hour  120 cells (Mon-Fri trading date x NY hour)
  * month_end_x_ny_hour 24 cells (last trading date of each month x NY hour)
Total 192 cells = 192 trials. Calendar-only conditioning, so nothing can look ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP, mid
from .fixes import month_end_flag
from .metrics import block_bootstrap_mean_ci
from .sessions import NY, trading_date

MIN_BARS = 55
N_CELLS = 24 + 24 + 120 + 24
WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri")


def hourly_returns(bars: pd.DataFrame) -> pd.DataFrame:
    """One row per (clock, date, hour): columns clock, date, hour, ret_pips, bars."""
    m = mid(bars)
    out = []
    utc = bars.index
    ny = utc.tz_convert(NY)
    for clock, dates, hours in (
        ("utc", pd.Index(utc.date), utc.hour),
        ("ny", pd.Index(trading_date(utc)), ny.hour),
    ):
        df = pd.DataFrame({"date": dates, "hour": np.asarray(hours),
                           "open": m["open"].to_numpy(), "close": m["close"].to_numpy()})
        g = df.groupby(["date", "hour"], sort=True)
        r = pd.DataFrame({"ret_pips": (g["close"].last() - g["open"].first()) / PIP, "bars": g["close"].size()})
        r = r[r["bars"] >= MIN_BARS].reset_index()
        r.insert(0, "clock", clock)
        out.append(r)
    return pd.concat(out, ignore_index=True)


def decide(res: dict, n_trials: int = N_CELLS, min_abs_mean: float = 1.0, alpha: float = 0.05) -> str:
    """Pre-registered E009 cell rule.

    CANDIDATE: |mean| >= 1.0 pip AND block-bootstrap 95% CI excludes 0 (same side as the mean)
               AND one-sample t-test p < alpha / n_trials AND sign-test binomial p < alpha.
    NOTE:      |mean| >= 1.0 pip AND t-test p < 0.01 but not CANDIDATE (listed, spawns nothing).
    NONE:      otherwise.
    """
    if res.get("n", 0) < 40 or np.isnan(res.get("ci_lo", np.nan)):
        return "NONE"
    m, lo, hi = res["mean_pips"], res["ci_lo"], res["ci_hi"]
    ci_ok = (lo > 0) if m > 0 else (hi < 0)
    if abs(m) >= min_abs_mean and ci_ok and res["t_p"] < alpha / n_trials and res["sign_p"] < alpha:
        return "CANDIDATE"
    if abs(m) >= min_abs_mean and res["t_p"] < 0.01:
        return "NOTE"
    return "NONE"


def cell_stats(y: pd.Series) -> dict:
    y = y.dropna().to_numpy(dtype=float)
    n = len(y)
    if n < 40:
        return {"n": n, "mean_pips": float(np.mean(y)) if n else float("nan"), "ci_lo": float("nan"),
                "ci_hi": float("nan"), "t_p": 1.0, "sign_p": 1.0}
    t_p = float(stats.ttest_1samp(y, 0.0).pvalue)
    pos = int((y > 0).sum())
    nz = int((y != 0).sum())
    sign_p = float(stats.binomtest(pos, nz, 0.5).pvalue) if nz else 1.0
    lo, hi = block_bootstrap_mean_ci(y)
    return {"n": n, "mean_pips": round(float(y.mean()), 3), "sd_pips": round(float(y.std(ddof=1)), 3),
            "up_share": round(pos / nz, 4) if nz else float("nan"), "ci_lo": round(lo, 3), "ci_hi": round(hi, 3),
            "t_p": t_p, "sign_p": round(sign_p, 6)}


def scan(hr: pd.DataFrame, split_of_date) -> pd.DataFrame:
    """Run all 192 cells on rows whose date is in the `dev` block. `split_of_date(dates)` -> labels Series."""
    hr = hr.copy()
    hr["block"] = split_of_date(pd.Index(hr["date"])).to_numpy()
    hr = hr[hr["block"] == "dev"]
    ny = hr[hr["clock"] == "ny"].copy()
    ny_dates = pd.Index(sorted(ny["date"].unique()))
    me = month_end_flag(ny_dates)
    ny["month_end"] = ny["date"].map(me.to_dict()).astype(bool)
    ny["weekday"] = pd.to_datetime(ny["date"]).dt.dayofweek

    rows = []

    def add(family, cell, hour, y):
        res = cell_stats(y)
        rows.append({"family": family, "cell": cell, "hour": hour, **res, "decision": decide(res)})

    utc = hr[hr["clock"] == "utc"]
    for h in range(24):
        add("utc_hour", f"utc_{h:02d}", h, utc.loc[utc["hour"] == h, "ret_pips"])
    for h in range(24):
        add("ny_hour", f"ny_{h:02d}", h, ny.loc[ny["hour"] == h, "ret_pips"])
    for wd, name in enumerate(WEEKDAYS):
        for h in range(24):
            add("weekday_x_ny_hour", f"{name}_ny_{h:02d}", h,
                ny.loc[(ny["weekday"] == wd) & (ny["hour"] == h), "ret_pips"])
    for h in range(24):
        add("month_end_x_ny_hour", f"ME_ny_{h:02d}", h, ny.loc[ny["month_end"] & (ny["hour"] == h), "ret_pips"])
    out = pd.DataFrame(rows)
    assert len(out) == N_CELLS
    out["t_p_bonferroni"] = (out["t_p"] * N_CELLS).clip(upper=1.0)
    return out
