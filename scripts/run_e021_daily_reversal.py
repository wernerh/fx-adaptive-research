"""E021: next-session reversal after a large daily move, DEV ONLY.

Pre-registered in experiments/2026-11-09_E021_daily_reversal/ (backlog B18). Val and OOS untouched.
Decision: fxresearch.daily_reversal.decide_b18 on per-event signed mid returns, 20:00 NY on D -> 10:45 NY on the next trading
date, events = |16:00 -> 16:00 NY move on D| above the rolling 80th percentile of the previous 60 valid trading dates,
Fridays excluded. Everything else (16:00-20:00 move, by year, costs, FOMC overlap, all valid non-Friday dates) is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e021_daily_reversal.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.daily_reversal import (
    PCTL, WINDOW, cost_summary, daily_frame, decide_b18, evaluate, exclusion_counts, fomc_overlap, mark_events,
    tradable_events,
)
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

df, miss = daily_frame(bars)
v = mark_events(df)
ev = tradable_events(v)
res = evaluate(ev["signed_pips"])
res["decision"] = decide_b18(res)

counts = {"trading_dates": int(len(df)), "valid_dates": int(len(v)), "burn_in": int(min(WINDOW, len(v))),
          "large_dates": int(v["is_large"].sum()), "events_tested": int(len(ev)), **miss, **exclusion_counts(v)}

cal = pd.read_csv(ROOT / "data" / "calendars" / "fomc_dates.csv")
stmt = {pd.Timestamp(s).date() for s in cal.loc[cal["scheduled"].astype(str) == "True", "statement_date"]}

post = v.iloc[WINDOW:] if len(v) > WINDOW else v.iloc[0:0]
ctrl = post[(~post["is_large"]) & (post["date"].map(lambda d: d.weekday() != 4))]
desc = {
    "events_16_to_20_move_signed_reversal_already": evaluate(ev["signed_16_20_pips"].dropna()) if len(ev) else {},
    "non_large_non_friday_dates_same_trade": evaluate(ctrl["signed_pips"].dropna()) if len(ctrl) else {},
    "events_mean_abs_move_pips": round(float(ev["move_pips"].abs().mean()), 3) if len(ev) else None,
    "events_up_move_n": int((ev["move_pips"] > 0).sum()),
    "events_up_move_mean_signed": round(float(ev.loc[ev["move_pips"] > 0, "signed_pips"].mean()), 3)
    if (ev["move_pips"] > 0).any() else None,
    "events_down_move_n": int((ev["move_pips"] < 0).sum()),
    "events_down_move_mean_signed": round(float(ev.loc[ev["move_pips"] < 0, "signed_pips"].mean()), 3)
    if (ev["move_pips"] < 0).any() else None,
    "median_threshold_pips": round(float(v["threshold_pips"].median()), 3) if v["threshold_pips"].notna().any() else None,
    "fomc_overlap": fomc_overlap(ev, stmt),
}
if len(ev):
    by_year = (ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                    hit=("signed_pips", lambda s: (s > 0).mean())).round(3))
else:
    by_year = pd.DataFrame()
c = cost_summary(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE021 DEV next-session reversal, |move| > p{PCTL} of previous {WINDOW} valid dates, "
          "20:00 NY D -> 10:45 NY next trading date (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", counts)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E021 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E021_synthetic_smoke" if args.synthetic else "E021_results"
dump({"result": res, "counts": counts, "descriptive": desc, "by_year": by_year.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["dev"], "window": WINDOW, "percentile": PCTL,
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    v.to_csv(out_dir / "E021_days.csv", index=False)
