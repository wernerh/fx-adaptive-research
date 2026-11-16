"""E051: random-forest classifier on 10 lagged daily returns, next-day direction, 16:00 NY daily hold, DEV ONLY.

Pre-registered in experiments/2026-11-16_E051_rf_lags/ (backlog B62, R212). Val and OOS untouched.
Decision: fxresearch.tsmom.decide_b16 on daily signed mid returns (mean > 1 pip, block-20 bootstrap CI lower > 0,
one-sided t p < 0.05). Costs, flips, by-year, long/short, buy-and-hold, E019 TSMOM and E050 on the same dates, mean p and
feature importances are descriptive only. Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e051_rf_lags.py [--synthetic]
"""
import argparse
import sys
from datetime import date

import numpy as np
import pandas as pd
import sklearn

from _common import ROOT, dump, load_bars
from fxresearch.data import synthetic_bars
from fxresearch.rf_lags import N_LAGS, N_TREES, RANDOM_STATE, REFIT_EVERY, build_daily
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.tsmom import build_daily as tsmom_daily
from fxresearch.tsmom import cost_summary, daily_quotes, decide_b16, evaluate

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

if args.synthetic:
    bars = synthetic_bars("2023-01-02", "2024-02-29")
    plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0)
    first_fit_end = date(2023, 12, 31)
else:
    bars = load_bars(False)
    plan = DEFAULT_PLAN
    first_fit_end = date(2015, 12, 31)
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())
print("scikit-learn", sklearn.__version__)

q = daily_quotes(bars)
out_dir = ROOT / "backtests" / "validation_reports"
stem = "E051_synthetic_smoke" if args.synthetic else "E051_results"
try:
    df, skips, info = build_daily(q, first_fit_end)
except RuntimeError as e:
    print("E051 BLOCKED:", e)
    dump({"result": {"decision": "BLOCKED", "reason": str(e)}, "n_trials": 0, "blocks": ["dev"]}, out_dir / f"{stem}.json")
    sys.exit(0)

res = evaluate(df["signed_pips"])
res["decision"] = decide_b16(res)

last_model = info.pop("last_model")
importances = {f"lag{j}": round(float(v), 4) for j, v in enumerate(last_model.feature_importances_)}
desc = {"feature_importances_last_fit": importances}
if len(df):
    long_d, short_d = df[df["signal"] > 0], df[df["signal"] < 0]
    desc["long_days"] = {"n": int(len(long_d)), "mean_signed_pips": round(float(long_d["signed_pips"].mean()), 3) if len(long_d) else None}
    desc["short_days"] = {"n": int(len(short_d)), "mean_signed_pips": round(float(short_d["signed_pips"].mean()), 3) if len(short_d) else None}
    desc["buy_and_hold_mean_pips_per_day"] = round(float(df["ret_pips"].mean()), 3)
    desc["mean_p_up"] = round(float(df["p_up"].mean()), 4)
    desc["p_up_quantiles"] = {k: round(float(df["p_up"].quantile(v)), 4) for k, v in (("q10", 0.1), ("q50", 0.5), ("q90", 0.9))}
    ts, _ = tsmom_daily(q)
    m = df[["date", "signal", "signed_pips"]].merge(ts[["date", "signal", "signed_pips"]], on="date", suffixes=("", "_tsmom"))
    desc["tsmom_e019_same_dates"] = {
        "n": int(len(m)),
        "tsmom_mean_signed_pips": round(float(m["signed_pips_tsmom"].mean()), 3) if len(m) else None,
        "e051_mean_signed_pips_on_these_dates": round(float(m["signed_pips"].mean()), 3) if len(m) else None,
        "signal_agreement": round(float((m["signal"] == m["signal_tsmom"]).mean()), 4) if len(m) else None,
    }
    e050_path = out_dir / "E050_daily.csv"
    if not args.synthetic and e050_path.exists():
        e50 = pd.read_csv(e050_path, usecols=["date", "signal", "signed_pips"])
        e50["date"] = pd.to_datetime(e50["date"]).dt.date
        m2 = df[["date", "signal", "signed_pips"]].merge(e50, on="date", suffixes=("", "_e050"))
        desc["e050_same_dates"] = {
            "n": int(len(m2)),
            "e050_mean_signed_pips": round(float(m2["signed_pips_e050"].mean()), 3) if len(m2) else None,
            "e051_mean_signed_pips_on_these_dates": round(float(m2["signed_pips"].mean()), 3) if len(m2) else None,
            "signal_agreement": round(float((m2["signal"] == m2["signal_e050"]).mean()), 4) if len(m2) else None,
        }
    by_year = (df.assign(year=pd.to_datetime(df["date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"), hit=("signed_pips", lambda v: (v > 0).mean()),
                    long_share=("signal", lambda s: (s > 0).mean())).round(3))
else:
    by_year = pd.DataFrame()
c = cost_summary(df) if len(df) else {"n_days": 0}
fit_summary = {k: v for k, v in info.items() if k != "fits"}
fit_summary["n_fits_ok"] = len(info["fits"])

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE051 DEV random forest ({N_TREES} trees, random_state {RANDOM_STATE}) on {N_LAGS} lagged daily returns, "
          f"refit every {REFIT_EVERY} trading dates, 16:00 NY daily hold (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("trading dates:", len(q), "test days:", len(df), "excluded:", skips)
    print("fits:", fit_summary)
    print("\nDescriptive:", desc)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive; swap/carry NOT included):")
    print(pd.Series(c).to_string())
print("E051 decision:", res["decision"])

dump({"result": res, "n_trading_dates": int(len(q)), "n_test_days": int(len(df)), "skips": skips,
      "fit_summary": fit_summary, "fits": info["fits"], "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"), "cost_check": c,
      "first_test_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_test_date": str(df["date"].iloc[-1]) if len(df) else None,
      "n_trials": 1, "blocks": ["dev"], "n_lags": N_LAGS, "n_trees": N_TREES, "random_state": RANDOM_STATE,
      "refit_every": REFIT_EVERY, "first_fit_end": str(first_fit_end), "sklearn_version": sklearn.__version__},
     out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E051_daily.csv", index=False)
