"""E024: post-London-fix EUR appreciation on high-volatility dates (long EUR/USD 11:05 -> 16:00 NY), DEV ONLY.

Pre-registered in experiments/2026-11-09_E024_vol_state_london_fix/ (backlog B20). Val and OOS untouched.
Decision: fxresearch.vol_state_london.decide_b20 (identical to E022's rule) on per-event signed mid returns, long 11:05 -> 16:00
NY on trading date D, events = previous trading date's mid range above the rolling 67th percentile of the 60 valid dates before it.
Everything else (control on normal dates, all dates, by year, by weekday, FOMC days, costs) is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e024_vol_state_london.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import PCTL, WINDOW, cost_summary, counts, evaluate, tradable_events
from fxresearch.vol_state_london import ENTRY_HM, EXIT_HM, decide_b20, flag_fomc, fomc_statement_dates, frame_from_bars

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

rng, df = frame_from_bars(bars)
df = flag_fomc(df, fomc_statement_dates(ROOT / "data" / "calendars" / "fomc_dates.csv"))
ev = tradable_events(df)
res = evaluate(ev["signed_pips"])
res["decision"] = decide_b20(res)
cnt = counts(rng, df)

ctrl = df[(df["state"] == "normal") & df["tradable"]] if len(df) else df
allp = df[df["state"].isin(["normal", "high"]) & df["tradable"]] if len(df) else df
ex_fomc = ev[~ev["fomc_day"]] if len(ev) else ev
desc = {
    "control_normal_dates_same_trade": evaluate(ctrl["signed_pips"]) if len(ctrl) else {},
    "all_post_burn_in_dates_same_trade": evaluate(allp["signed_pips"]) if len(allp) else {},
    "events_on_fomc_statement_days": int(ev["fomc_day"].sum()) if len(ev) else 0,
    "events_excluding_fomc_statement_days": evaluate(ex_fomc["signed_pips"]) if len(ex_fomc) else {},
    "median_daily_range_pips": round(float(rng["range_pips"].median()), 3) if len(rng) else None,
    "events_mean_prev_range_pips": round(float(ev["prev_range_pips"].mean()), 3) if len(ev) else None,
    "events_median_threshold_pips": round(float(ev["threshold_pips"].median()), 3) if len(ev) else None,
    "limitation": "WM/R fix at 11:00 NY except DST-mismatch weeks (window not shifted); overnight carry not relevant (intraday)",
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
    print(f"\nE024 DEV long EUR/USD {ENTRY_HM} -> {EXIT_HM} NY on dates after a range > p{PCTL} of the previous {WINDOW} valid "
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
print("E024 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E024_synthetic_smoke" if args.synthetic else "E024_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["dev"], "window": WINDOW, "percentile": PCTL,
      "entry_hm": list(ENTRY_HM), "exit_hm": list(EXIT_HM), "side": "long",
      "first_date": str(rng["date"].iloc[0]) if len(rng) else None,
      "last_date": str(rng["date"].iloc[-1]) if len(rng) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E024_days.csv", index=False)
