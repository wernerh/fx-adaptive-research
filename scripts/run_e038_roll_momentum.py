"""E038: intraday momentum into the 17:00 NY spot roll (B38: sign(17:00 -> 16:25 NY) x 16:25 -> 16:55 NY), DEV ONLY, 1 trial.

Pre-registered in experiments/2026-11-11_E038_roll_momentum/ (R083). Val and OOS untouched: bars are restricted to dev trading
dates BEFORE any computation. Decision: fxresearch.roll_momentum.decide_b38. Everything else is descriptive.

    python scripts/run_e038_roll_momentum.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch import roll_momentum as rm
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import cost_summary

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

df, n_weekend = rm.frame_from_bars(bars)
ev = rm.events(df) if len(df) else df
res = rm.evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = rm.decide_b38(res)
res["reversal_exploratory"] = rm.reversal_flag(res)
cnt = rm.counts(df, n_weekend)


def _ev(x):
    x = pd.Series(x).dropna()
    return rm.evaluate(x) if len(x) >= 2 * rm.BOOT_BLOCK else {"n": int(len(x))}


stmt = set()
cal_path = ROOT / "data" / "calendars" / "fomc_dates.csv"
if cal_path.exists() and not args.synthetic:
    cal = pd.read_csv(cal_path)
    cal = cal[cal["scheduled"].astype(str).str.lower().eq("true") & ~cal["cancelled"].astype(str).str.lower().eq("true")]
    stmt = {pd.Timestamp(x).date() for x in cal["statement_date"]}

desc = {}
if len(ev):
    desc["slope_r2_on_r1"] = rm.slope(ev)
    desc["sd_r1_pips"] = round(float(ev["r1_pips"].std()), 3)
    desc["sd_r2_pips"] = round(float(ev["r2_pips"].std()), 3)
    desc["share_long"] = round(float((ev["side"] > 0).mean()), 3)
    desc["unconditional_long_r2"] = _ev(ev["r2_pips"])
    terc = pd.qcut(ev["r1_pips"].abs(), 3, labels=["low", "mid", "high"])
    for k in ["low", "mid", "high"]:
        desc[f"abs_r1_tercile_{k}"] = _ev(ev.loc[terc == k, "signed_pips"])
    for col in ("entry_spread_pips", "exit_spread_pips"):
        s = df[col].dropna()
        desc[f"{col}_median_p90"] = (round(float(s.median()), 3), round(float(s.quantile(0.9)), 3)) if len(s) else None
    # EDT vs EST: NY UTC offset at 16:25 NY on D
    off = [pd.Timestamp(d).tz_localize("America/New_York").utcoffset().total_seconds() / 3600 for d in ev["date"]]
    ev = ev.assign(edt=np.array(off) == -4)
    desc["edt"] = _ev(ev.loc[ev["edt"], "signed_pips"])
    desc["est"] = _ev(ev.loc[~ev["edt"], "signed_pips"])
    desc["fridays"] = _ev(ev.loc[ev["weekday"] == 4, "signed_pips"])
    desc["mon_thu"] = _ev(ev.loc[ev["weekday"] != 4, "signed_pips"])
    desc["next_date_reversal_reading_sign_r1_x_1705_to_1625_next"] = _ev(ev["side"] * ev["next_day_pips"])
    desc["excl_fomc_statement_dates"] = _ev(ev.loc[~ev["date"].isin(stmt), "signed_pips"])
    desc["fomc_statement_dates_in_tested"] = int(ev["date"].isin(stmt).sum())
    dts = pd.to_datetime(df["date"])
    last_in_month = set(df.loc[dts.groupby(dts.dt.to_period("M")).transform("max") == dts, "date"])
    desc["excl_month_end"] = _ev(ev.loc[~ev["date"].isin(last_in_month), "signed_pips"])

by_year = []
if len(ev):
    g = ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")["signed_pips"]
    by_year = (pd.DataFrame({"n": g.size(), "mean": g.mean(), "hit": g.apply(lambda s: (s > 0).mean())}).round(3)
               .reset_index().to_dict(orient="records"))
cost = cost_summary(ev) if len(ev) else {"n": 0}
res["lead_cost_gate"] = bool(cost.get("n", 0) > 0 and cost["mean_net_spec4_pips"] > 0 and cost["mean_net_costs_x1_5_pips"] > 0)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE038 DEV sign({rm.START_HM} -> {rm.ENTRY_HM} NY) x ({rm.ENTRY_HM} -> {rm.EXIT_HM} NY) (pre-registered, 1 trial, "
          f"block {rm.BOOT_BLOCK}, binomial p < {rm.ALPHA})")
    print(pd.Series(res).to_string())
    print("\nCounts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):", by_year)
    print("\nDEV cost check (descriptive):", cost)
print("E038 decision:", res["decision"], "| reversal (exploratory):", res["reversal_exploratory"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E038_synthetic_smoke" if args.synthetic else "E038_results"
dump({"result_b38": res, "counts": cnt, "descriptive": desc, "by_year": by_year, "cost_check": cost, "n_trials": 1,
      "blocks": ["dev"], "boot_block": rm.BOOT_BLOCK, "start_hm_ny": list(rm.START_HM), "entry_hm_ny": list(rm.ENTRY_HM),
      "exit_hm_ny": list(rm.EXIT_HM), "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None, "decision": res["decision"]}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E038_days.csv", index=False)
