"""E040: post-FOMC reversal (B43: -sign(16:00 NY t-1 -> 13:55 NY t) x 02:00 -> 14:00 NY t+1), DEV ONLY, 1 trial.

Pre-registered in experiments/2026-11-11_E040_post_fomc_reversal/ (R089). Val and OOS untouched: bars are restricted to dev trading
dates BEFORE any computation. Decision: fxresearch.post_fomc_reversal.decide_b43. Everything else is descriptive.

    python scripts/run_e040_post_fomc_reversal.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch import post_fomc_reversal as pf
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import cost_summary

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
if args.synthetic:
    plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0)
    # Placeholder Wednesdays for the smoke run only; not FOMC dates.
    cal = pd.DataFrame({"statement_date": ["2024-01-17", "2024-01-31", "2024-02-14", "2024-03-13"], "scheduled": [True] * 4,
                        "cancelled": [False] * 4})
else:
    plan = DEFAULT_PLAN
    cal = pd.read_csv(ROOT / "data" / "calendars" / "fomc_dates.csv")

td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

cal["statement_date"] = pd.to_datetime(cal["statement_date"]).dt.date
cal["block"] = plan.assign(pd.Index(cal["statement_date"])).to_numpy()
dev_cal = cal[cal["block"] == "dev"]
is_s = dev_cal["scheduled"].astype(str).str.lower().eq("true")
is_c = dev_cal["cancelled"].astype(str).str.lower().eq("true")
sched = sorted(dev_cal.loc[is_s & ~is_c, "statement_date"])
unsched = sorted(dev_cal.loc[~is_s, "statement_date"])
cancelled = sorted(dev_cal.loc[is_s & is_c, "statement_date"])

df = pf.frame_from_bars(bars, sched)
ev = pf.events(df) if len(df) else df
res = pf.evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = pf.decide_b43(res)
cnt = pf.counts(df)
cost = cost_summary(ev) if len(ev) else {"n": 0}
res["lead_cost_gate"] = bool(cost.get("n", 0) > 0 and cost["mean_net_spec4_pips"] > 0 and cost["mean_net_costs_x1_5_pips"] > 0)

desc = {}
if len(ev):
    desc["unconditional_short_r"] = pf.evaluate(-ev["r_pips"])
    desc["p_pos_subset"] = pf.evaluate(ev.loc[ev["p_pips"] > 0, "signed_pips"])
    desc["p_neg_subset"] = pf.evaluate(ev.loc[ev["p_pips"] < 0, "signed_pips"])
    desc["window_0_12h_signed"] = pf.evaluate(ev["signed_0_12_pips"].dropna())
    desc["slope_r_on_p"] = pf.slope(ev)
    desc["mean_p_pips"] = round(float(ev["p_pips"].mean()), 3)
    desc["mean_abs_p_pips"] = round(float(ev["p_pips"].abs().mean()), 3)
    desc["share_short"] = round(float((ev["side"] < 0).mean()), 3)
    # Control: every dev Wednesday that is not a scheduled / unscheduled / cancelled FOMC date, same rule.
    fomc_all = set(sched) | set(unsched) | set(cancelled)
    ny_days = sorted(pf.ny_dates_with_bars(bars))
    weds = [d for d in ny_days if d.weekday() == 2 and d not in fomc_all]
    cdf = pf.frame_from_bars(bars, weds)
    cev = pf.events(cdf) if len(cdf) else cdf
    desc["control_non_fomc_wednesdays"] = pf.evaluate(cev["signed_pips"]) if len(cev) else {"n": 0}
    desc["control_counts"] = pf.counts(cdf)

by_year = []
if len(ev):
    g = ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")["signed_pips"]
    by_year = (pd.DataFrame({"n": g.size(), "mean": g.mean(), "hit": g.apply(lambda s: (s > 0).mean())}).round(3)
               .reset_index().to_dict(orient="records"))

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE040 DEV -sign(16:00 NY t-1 -> 13:55 NY t) x (02:00 -> 14:00 NY t+1) (pre-registered, 1 trial, i.i.d. bootstrap, "
          f"t p < {pf.ALPHA}, >= {pf.MIN_EVENTS} events)")
    print("Scheduled dev statements:", len(sched), "| unscheduled excluded:", [str(d) for d in unsched] or "none",
          "| cancelled excluded:", [str(d) for d in cancelled] or "none")
    print(pd.Series(res).to_string())
    print("\nCounts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):", by_year)
    print("\nDEV cost check (descriptive):", cost)
    print("\nPer event:\n", df.round(2).to_string())
print("E040 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E040_synthetic_smoke" if args.synthetic else "E040_results"
dump({"result_b43": res, "counts": cnt, "descriptive": desc, "by_year": by_year, "cost_check": cost, "n_trials": 1,
      "blocks": ["dev"], "n_scheduled_dev": len(sched), "unscheduled_excluded": [str(d) for d in unsched],
      "cancelled_excluded": [str(d) for d in cancelled], "decision": res["decision"]}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E040_events.csv", index=False)
