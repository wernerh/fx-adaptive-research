"""E020: weekend-gap reversal, DEV ONLY.

Pre-registered in experiments/2026-11-09_E020_weekend_gap/ (backlog B17). Val and OOS untouched.
Decision: fxresearch.weekend_gap.decide_b17 on per-event signed mid returns, 20:00 NY Sunday -> 16:00 NY Monday, events =
|Friday 16:00 -> Sunday 20:00 gap| above the rolling 67th percentile of the previous 26 valid weekends.
Everything else (all weekends, Tue/Fri horizons, by year, costs, Sunday 17-20 move) is descriptive only.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e020_weekend_gap.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.weekend_gap import (
    PCTL, WINDOW, cost_summary, decide_b17, evaluate, mark_events, tradable_events, weekend_frame,
)

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

wf, skips = weekend_frame(bars)
v = mark_events(wf)
ev = tradable_events(v)
res = evaluate(ev["signed_pips"])
res["decision"] = decide_b17(res)

counts = {"candidate_weekends": int(len(wf)), "valid_weekends": int(len(v)), "burn_in": int(min(WINDOW, len(v))),
          "events": int(v["is_event"].sum()), "events_entry_skipped_spread": int(v["entry_skipped"].sum()),
          "events_tested": int(len(ev)), **skips}

post = v.iloc[WINDOW:] if len(v) > WINDOW else v.iloc[0:0]
desc = {
    "all_weekends_after_burn_in": evaluate(post["signed_pips"]) if len(post) else {},
    "events_exit_tue_16ny": evaluate(ev["signed_tue_pips"].dropna()) if len(ev) else {},
    "events_exit_fri_16ny": evaluate(ev["signed_fri_pips"].dropna()) if len(ev) else {},
    "events_sun17_to_20_reversal_already": evaluate(ev["signed_sun17_20_pips"].dropna()) if len(ev) else {},
    "events_mean_abs_gap_pips": round(float(ev["gap_pips"].abs().mean()), 3) if len(ev) else None,
    "events_up_gap_n": int((ev["gap_pips"] > 0).sum()),
    "events_up_gap_mean_signed": round(float(ev.loc[ev["gap_pips"] > 0, "signed_pips"].mean()), 3)
    if (ev["gap_pips"] > 0).any() else None,
    "events_down_gap_n": int((ev["gap_pips"] < 0).sum()),
    "events_down_gap_mean_signed": round(float(ev.loc[ev["gap_pips"] < 0, "signed_pips"].mean()), 3)
    if (ev["gap_pips"] < 0).any() else None,
    "median_threshold_pips": round(float(v["threshold_pips"].median()), 3) if v["threshold_pips"].notna().any() else None,
}
if len(ev):
    by_year = (ev.assign(year=pd.to_datetime(ev["monday"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                    hit=("signed_pips", lambda s: (s > 0).mean())).round(3))
else:
    by_year = pd.DataFrame()
c = cost_summary(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE020 DEV weekend-gap reversal, |gap| > p{PCTL} of previous {WINDOW} valid weekends, "
          "20:00 NY Sun -> 16:00 NY Mon (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", counts)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E020 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E020_synthetic_smoke" if args.synthetic else "E020_results"
dump({"result": res, "counts": counts, "descriptive": desc, "by_year": by_year.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["dev"], "window": WINDOW, "percentile": PCTL,
      "first_monday": str(wf["monday"].iloc[0]) if len(wf) else None,
      "last_monday": str(wf["monday"].iloc[-1]) if len(wf) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    v.to_csv(out_dir / "E020_weekends.csv", index=False)
