"""E019: time-series momentum, 12-month (252 trading date) lookback, daily 16:00 NY hold, DEV ONLY.

Pre-registered in experiments/2026-11-09_E019_tsmom_12m/ (backlog B16). Val and OOS untouched.
Decision: fxresearch.tsmom.decide_b16 on daily signed mid returns (mean > 1 pip, block-20 bootstrap CI lower > 0,
one-sided t p < 0.05). Costs, flips, by-year, long/short days and buy-and-hold are descriptive only.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e019_tsmom.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.tsmom import LOOKBACK, build_daily, cost_summary, daily_quotes, decide_b16, evaluate

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

q = daily_quotes(bars)
df, skips = build_daily(q)
res = evaluate(df["signed_pips"])
res["decision"] = decide_b16(res)

desc = {}
if len(df):
    long_d, short_d = df[df["signal"] > 0], df[df["signal"] < 0]
    desc["long_days"] = {"n": int(len(long_d)), "mean_signed_pips": round(float(long_d["signed_pips"].mean()), 3) if len(long_d) else None}
    desc["short_days"] = {"n": int(len(short_d)), "mean_signed_pips": round(float(short_d["signed_pips"].mean()), 3) if len(short_d) else None}
    desc["flat_days"] = int((df["signal"] == 0).sum())
    desc["buy_and_hold_mean_pips_per_day"] = round(float(df["ret_pips"].mean()), 3)
    by_year = (df.assign(year=pd.to_datetime(df["date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"), hit=("signed_pips", lambda v: (v > 0).mean()),
                    long_share=("signal", lambda s: (s > 0).mean())).round(3))
else:
    by_year = pd.DataFrame()
c = cost_summary(df)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE019 DEV time-series momentum, lookback {LOOKBACK} trading dates, 16:00 NY daily hold (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("trading dates:", len(q), "test days:", len(df), "excluded:", skips)
    print("\nDescriptive:", desc)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive; swap/carry NOT included):")
    print(pd.Series(c).to_string())
print("E019 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E019_synthetic_smoke" if args.synthetic else "E019_results"
dump({"result": res, "n_trading_dates": int(len(q)), "n_test_days": int(len(df)), "skips": skips,
      "descriptive": desc, "by_year": by_year.reset_index().to_dict(orient="records"), "cost_check": c,
      "first_test_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_test_date": str(df["date"].iloc[-1]) if len(df) else None,
      "n_trials": 1, "blocks": ["dev"], "lookback": LOOKBACK}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E019_daily.csv", index=False)
