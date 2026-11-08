"""E014 (B11v): val confirmation of E013. Long EUR/USD 16:00 NY (previous business day) -> 16:00 NY (scheduled FOMC
statement day). VAL ONLY. OOS is never evaluated: bars are truncated to the val date range before any computation.

Pre-registered in experiments/2026-11-08_E014_fomc_day_val/. Window, rule and cost check are unchanged from E013.

    python scripts/run_e014_fomc_day_val.py [--synthetic]
"""
import argparse
import json
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fomc import calendar_block_dates, cost_summary, decide_b11, evaluate_long, window_frame
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
if args.synthetic:
    # Smoke run only: dev ends before the synthetic range so the whole range is "val". Placeholder Wednesdays, not FOMC dates.
    plan = SplitPlan(date(2023, 12, 31), date(2024, 6, 30), embargo_days=0)
    cal = pd.DataFrame({"statement_date": ["2024-01-17", "2024-02-14", "2024-03-13"], "scheduled": [True] * 3,
                        "cancelled": [False] * 3})
    lo_ts, hi_ts = pd.Timestamp("2024-01-01", tz="UTC"), pd.Timestamp("2024-07-01", tz="UTC")
else:
    plan = DEFAULT_PLAN
    cal = pd.read_csv(ROOT / "data" / "calendars" / "fomc_dates.csv")
    # Val statement days start 2021-01-27 (entry 2021-01-26); last val day 2023-06-30. Nothing at or after 2023-07-01 is read.
    lo_ts, hi_ts = pd.Timestamp("2021-01-01", tz="UTC"), pd.Timestamp("2023-07-01", tz="UTC")

bars = bars[(bars.index >= lo_ts) & (bars.index < hi_ts)]
assert bars.index.max() < hi_ts

sets = calendar_block_dates(cal, plan, "val")
sched, cancelled, unsched = sets["scheduled"], sets["cancelled"], sets["unscheduled"]

idx_dates = pd.Index(sorted(set(bars.index.tz_convert("America/New_York").date)))
val_days = [d for d, b in zip(idx_dates, plan.assign(idx_dates)) if b == "val" and d.weekday() < 5]
excl = set(sched) | set(unsched) | set(cancelled)
bench_days = [d for d in val_days if d not in excl]

f = window_frame(bars, sched)
b = window_frame(bars, bench_days)
dropped = [str(d) for d in f.index[f["ret_pips"].isna()]]

res = evaluate_long(f["ret_pips"])
res["decision"] = decide_b11(res)
costs = cost_summary(f)
res["lead_cost_gate"] = bool(costs["mean_net_spec4_pips"] > 0 and costs["mean_net_costs_x1_5_pips"] > 0)
res["lead"] = bool(res["decision"] == "SIGNAL" and res["lead_cost_gate"])
bench = evaluate_long(b["ret_pips"])
sub = evaluate_long(f["sub_ret_pips"])
yearly = f["ret_pips"].groupby(pd.to_datetime(pd.Index(f.index)).year).agg(["count", "mean"]).round(3)

pooled = None
if not args.synthetic:
    dev_path = ROOT / "backtests" / "validation_reports" / "E013_results.json"
    if dev_path.exists():
        dev_vals = [m["ret_pips"] for m in json.loads(dev_path.read_text())["per_meeting"] if m["ret_pips"] is not None]
        allv = pd.Series(dev_vals + f["ret_pips"].dropna().tolist())
        pooled = {"n": int(len(allv)), "mean_pips": round(float(allv.mean()), 3)}

print(f"E014 VAL ONLY. Scheduled statement days in val: {len(sched)}; dropped for missing quotes: {dropped or 'none'}")
print("Unscheduled actions excluded:", [str(d) for d in unsched] or "none")
print("Cancelled scheduled meetings excluded:", [str(d) for d in cancelled] or "none")
print("\nPre-registered test (1 trial): long EUR/USD 16:00 NY prev business day -> 16:00 NY statement day")
print(res)
print("\nCost check (gates the LEAD label):", costs)
print("\nDescriptive (not trials): non-FOMC val weekdays same window:", bench)
print("Descriptive: 13:00-16:00 NY sub-window on statement day:", sub)
print("Descriptive: pooled dev+val (information only, no rule):", pooled)
print("\nPer-year (descriptive):\n", yearly.to_string())
print("\nPer-meeting:\n", f.round(2).to_string())
print("\nE014 decision:", res["decision"], "| LEAD:", res["lead"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E014_synthetic_smoke" if args.synthetic else "E014_results"
dump({"test": res, "cost_check": costs, "benchmark_non_fomc_days": bench, "sub_window_13_16": sub,
      "pooled_dev_val_descriptive": pooled,
      "per_year": yearly.reset_index().to_dict(orient="records"),
      "per_meeting": f.reset_index().astype({"date": str, "start_date": str}).to_dict(orient="records"),
      "unscheduled_excluded": [str(d) for d in unsched], "cancelled_excluded": [str(d) for d in cancelled],
      "dropped": dropped, "n_trials": 1, "blocks": ["val"], "decision": res["decision"], "lead": res["lead"]},
     out_dir / f"{stem}.json")
