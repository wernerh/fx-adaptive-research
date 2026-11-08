"""E013: FOMC statement-day long EUR/USD, 16:00 NY (previous business day) -> 16:00 NY (statement day). DEV ONLY.

Pre-registered in experiments/2026-11-08_E013_fomc_day_drift/ (backlog B11). OOS and val are never evaluated here.
Requires the reviewed date file data/calendars/fomc_dates.csv (scheduled meetings only enter the test;
unscheduled actions are listed and excluded).

    python scripts/run_e013_fomc_day.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fomc import cost_summary, decide_b11, evaluate_long, window_frame
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
if args.synthetic:
    plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0)  # whole synthetic range = "dev"
    # Placeholder Wednesdays for the smoke run only; not FOMC dates.
    cal = pd.DataFrame({"statement_date": ["2024-01-17", "2024-02-14", "2024-03-13"], "scheduled": [True] * 3,
                        "cancelled": [False] * 3})
else:
    plan = DEFAULT_PLAN
    path = ROOT / "data" / "calendars" / "fomc_dates.csv"
    if not path.exists():
        raise SystemExit(f"{path} missing: promote the reviewed backtests/calendars/fomc_dates.csv first.")
    cal = pd.read_csv(path)

cal["statement_date"] = pd.to_datetime(cal["statement_date"]).dt.date
cal["block"] = plan.assign(pd.Index(cal["statement_date"])).to_numpy()
dev_cal = cal[cal["block"] == "dev"]
if "cancelled" not in dev_cal.columns:
    raise SystemExit("date file lacks the 'cancelled' column: re-fetch with the R018 parser")
is_s = dev_cal["scheduled"].astype(bool)
is_c = dev_cal["cancelled"].astype(bool)
sched = sorted(dev_cal.loc[is_s & ~is_c, "statement_date"])
cancelled = sorted(dev_cal.loc[is_s & is_c, "statement_date"])  # no statement issued: excluded, listed
unsched = sorted(dev_cal.loc[~is_s, "statement_date"])

# Benchmark days: every dev weekday that is not a scheduled or unscheduled FOMC date.
idx_dates = pd.Index(sorted(set(bars.index.tz_convert("America/New_York").date)))
dev_days = [d for d, b in zip(idx_dates, plan.assign(idx_dates)) if b == "dev" and d.weekday() < 5]
bench_days = [d for d in dev_days if d not in set(sched) | set(unsched) | set(cancelled)]

f = window_frame(bars, sched)
b = window_frame(bars, bench_days)
dropped = [str(d) for d in f.index[f["ret_pips"].isna()]]

res = evaluate_long(f["ret_pips"])
res["decision"] = decide_b11(res)
costs = cost_summary(f)
res["lead_cost_gate"] = bool(costs["mean_net_spec4_pips"] > 0 and costs["mean_net_costs_x1_5_pips"] > 0)
bench = evaluate_long(b["ret_pips"])
sub = evaluate_long(f["sub_ret_pips"])
yearly = f["ret_pips"].groupby(pd.to_datetime(pd.Index(f.index)).year).agg(["count", "mean"]).round(3)

print(f"E013 DEV ONLY. Scheduled statement days in dev: {len(sched)}; dropped for missing quotes: {dropped or 'none'}")
print("Unscheduled actions excluded:", [str(d) for d in unsched] or "none")
print("Cancelled scheduled meetings excluded (no statement):", [str(d) for d in cancelled] or "none")
print("\nPre-registered test (1 trial): long EUR/USD 16:00 NY prev business day -> 16:00 NY statement day")
print(res)
print("\nCost check (descriptive; gates only the LEAD label):", costs)
print("\nDescriptive (not trials): non-FOMC weekdays same window:", bench)
print("Descriptive: 13:00-16:00 NY sub-window on statement day:", sub)
print("\nPer-year (descriptive):\n", yearly.to_string())
print("\nPer-meeting:\n", f.round(2).to_string())
print("\nE013 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E013_synthetic_smoke" if args.synthetic else "E013_results"
dump({"test": res, "cost_check": costs, "benchmark_non_fomc_days": bench, "sub_window_13_16": sub,
      "per_year": yearly.reset_index().to_dict(orient="records"),
      "per_meeting": f.reset_index().astype({"date": str, "start_date": str}).to_dict(orient="records"),
      "unscheduled_excluded": [str(d) for d in unsched], "cancelled_excluded": [str(d) for d in cancelled],
      "dropped": dropped,
      "n_trials": 1, "blocks": ["dev"], "decision": res["decision"]}, out_dir / f"{stem}.json")
