"""E046: even- vs odd-week FOMC cycle (long weeks 2/4/6, short weeks -1/1/3/5, week 0 excluded), EUR/USD 20:00 NY (start of
trading date D) -> 16:55 NY D, DEV ONLY.

Pre-registered in experiments/2026-11-12_E046_fomc_cycle/ (backlog B54). Val and OOS untouched.
Decision: fxresearch.fomc_cycle.decide_b54 on per-date signed mid returns. Everything else is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e046_fomc_cycle.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fomc_cycle import (ENTRY_HM, EXIT_HM, cost_summary, counts, decide_b54, evaluate, frame_from_bars,
                                   statement_dates)
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
if args.synthetic:
    plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0)
    # Placeholder Wednesdays for the smoke run only; not FOMC dates.
    cal = pd.DataFrame({"statement_date": ["2024-01-17", "2024-02-21", "2024-04-03"], "scheduled": [True] * 3,
                        "cancelled": [False] * 3})
else:
    plan = DEFAULT_PLAN
    cal = pd.read_csv(ROOT / "data" / "calendars" / "fomc_dates.csv")
stmts = statement_dates(cal)

td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())
dates = sorted({d for d in trading_date(bars.index) if d.weekday() < 5})

df = frame_from_bars(bars, stmts, dates)
ev = df[df["tested"]]
res = evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b54(res)
cnt = counts(df)


def _ev(frame, col="signed_pips"):
    return evaluate(frame[col]) if len(frame) >= 40 else {"n": int(len(frame))}


desc = {}
by_year = pd.DataFrame()
if len(ev):
    ok = df["entry_mid"].notna() & df["exit_mid"].notna() & ~(df["entry_spread_pips"] > 2.0) & df["week"].notna()
    q = df[ok]
    desc["long_mean_by_cycle_week_incl_week0"] = {
        int(w): {"n": int(len(g)), "mean_long_pips": round(float(g["long_pips"].mean()), 3),
                 "hit_long": round(float((g["long_pips"] > 0).mean()), 4)} for w, g in q.groupby("week")}
    desc["even_long_leg"] = _ev(ev[ev["side"] > 0])
    desc["odd_short_leg"] = _ev(ev[ev["side"] < 0])
    desc["share_long"] = round(float((ev["side"] > 0).mean()), 4)
    desc["unconditional_long_same_hold"] = _ev(ev, "long_pips")
    lag = df[df["side_lag1"].ne(0) & df["entry_mid"].notna() & df["exit_mid"].notna() & ~(df["entry_spread_pips"] > 2.0)]
    desc["cycle_lagged_one_date_reported_only"] = _ev(lag.assign(s=lag["side_lag1"] * lag["long_pips"]), "s")
    desc["opposite_sign_mean_pips_reported_only"] = round(float(-ev["signed_pips"].mean()), 3)
    desc["n_statement_dates_used"] = int(sum(dates[0] <= s <= dates[-1] for s in stmts))
    by_year = (ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                    hit=("signed_pips", lambda s: (s > 0).mean())).round(3))
c = cost_summary(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE046 DEV FOMC cycle s x EUR/USD {ENTRY_HM} NY (D-1) -> {EXIT_HM} NY D (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E046 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E046_synthetic_smoke" if args.synthetic else "E046_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"), "cost_check": c, "n_trials": 1, "blocks": ["dev"],
      "entry_hm_ny": list(ENTRY_HM), "exit_hm_ny": list(EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None, "last_date": str(df["date"].iloc[-1]) if len(df) else None},
     out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E046_days.csv", index=False)
