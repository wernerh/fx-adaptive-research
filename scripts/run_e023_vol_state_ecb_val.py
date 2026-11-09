"""E023 (B19v): val confirmation of E022. Short EUR/USD 02:00 -> 08:15 NY on high-vol dates, VAL ONLY.

Pre-registered in experiments/2026-11-09_E023_vol_state_ecb_fix_val/. Definitions and rule identical to E022
(fxresearch.vol_state_fix.decide_b19). Bars at or after 2023-07-01 UTC are dropped first, then every bar whose trading date is
not `val` is dropped BEFORE any computation (burn-in inside val, no dev history). OOS is never read.

    python scripts/run_e023_vol_state_ecb_val.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import (
    PCTL, WINDOW, cost_summary, counts, decide_b19, evaluate, frame_from_bars, restrict_to_block, tradable_events,
)

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
if args.synthetic:
    # Smoke run only: dev ends before the synthetic range so the whole range is "val".
    plan, cut = SplitPlan(date(2023, 12, 31), date(2024, 6, 30), embargo_days=0), pd.Timestamp("2024-07-01", tz="UTC")
else:
    plan, cut = DEFAULT_PLAN, pd.Timestamp("2023-07-01", tz="UTC")
bars = restrict_to_block(bars, plan, "val", before_utc=cut)
assert len(bars) == 0 or bars.index.max() < cut
print("val bars:", len(bars), bars.index.min(), "->", bars.index.max())

rng, df = frame_from_bars(bars)
ev = tradable_events(df)
res = evaluate(ev["signed_pips"])
res["decision"] = decide_b19(res)
cnt = counts(rng, df)

ctrl = df[(df["state"] == "normal") & df["tradable"]] if len(df) else df
allp = df[df["state"].isin(["normal", "high"]) & df["tradable"]] if len(df) else df
desc = {
    "control_normal_dates_same_trade": evaluate(ctrl["signed_pips"]) if len(ctrl) else {},
    "all_post_burn_in_dates_same_trade": evaluate(allp["signed_pips"]) if len(allp) else {},
    "median_daily_range_pips": round(float(rng["range_pips"].median()), 3) if len(rng) else None,
    "events_mean_prev_range_pips": round(float(ev["prev_range_pips"].mean()), 3) if len(ev) else None,
    "events_median_threshold_pips": round(float(ev["threshold_pips"].median()), 3) if len(ev) else None,
    "limitation": "ECB monetary-policy days not identifiable (no ECB calendar in repo); overnight carry not relevant (intraday)",
}


def _group(frame, key):
    if not len(frame):
        return pd.DataFrame()
    return (frame.assign(**{key: key_fn[key](frame)}).groupby(key)
            .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                 hit=("signed_pips", lambda s: (s > 0).mean())).round(3))


key_fn = {"year": lambda f: pd.to_datetime(f["date"]).dt.year,
          "weekday": lambda f: pd.to_datetime(f["date"]).dt.day_name()}
by_year = _group(ev, "year")
by_weekday = _group(ev, "weekday")
c = cost_summary(ev)
res["lead_cost_gate"] = bool(c.get("n", 0) > 0 and c["mean_net_spec4_pips"] > 0 and c["mean_net_costs_x1_5_pips"] > 0)
res["lead"] = bool(res["decision"] == "SIGNAL" and res["lead_cost_gate"])

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE023 VAL short EUR/USD 02:00 -> 08:15 NY on dates after a range > p{PCTL} of the previous {WINDOW} valid "
          "dates (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy weekday (descriptive):\n", by_weekday.to_string())
    print("\nVAL cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E023 decision:", res["decision"], "| lead:", res["lead"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E023_synthetic_smoke" if args.synthetic else "E023_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["val"], "window": WINDOW, "percentile": PCTL,
      "first_date": str(rng["date"].iloc[0]) if len(rng) else None,
      "last_date": str(rng["date"].iloc[-1]) if len(rng) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E023_days.csv", index=False)
