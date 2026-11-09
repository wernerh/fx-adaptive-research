"""E022: pre-ECB-fix USD appreciation on high-volatility dates (short EUR/USD 02:00 -> 08:15 NY), DEV ONLY.

Pre-registered in experiments/2026-11-09_E022_vol_state_ecb_fix/ (backlog B19). Val and OOS untouched.
Decision: fxresearch.vol_state_fix.decide_b19 on per-event signed mid returns, short 02:00 -> 08:15 NY on trading date D,
events = previous trading date's mid range above the rolling 67th percentile of the 60 valid dates before it.
Everything else (control on normal dates, all dates, by year, by weekday, costs) is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e022_vol_state_ecb.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import (
    PCTL, WINDOW, cost_summary, counts, decide_b19, evaluate, frame_from_bars, tradable_events,
)

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

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

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE022 DEV short EUR/USD 02:00 -> 08:15 NY on dates after a range > p{PCTL} of the previous {WINDOW} valid "
          "dates (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy weekday (descriptive):\n", by_weekday.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E022 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E022_synthetic_smoke" if args.synthetic else "E022_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["dev"], "window": WINDOW, "percentile": PCTL,
      "first_date": str(rng["date"].iloc[0]) if len(rng) else None,
      "last_date": str(rng["date"].iloc[-1]) if len(rng) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E022_days.csv", index=False)
