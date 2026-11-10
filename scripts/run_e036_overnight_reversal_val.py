"""E036 (B34): val confirmation of E035/B33. Position -sign(O20) held 07:00 -> 16:55 NY, VAL ONLY, 1 trial.

Pre-registered in experiments/2026-11-10_E036_overnight_reversal_val/. Definitions identical to E035 B33
(fxresearch.overnight_reversal); rule fxresearch.overnight_reversal.decide_b34 (E035 rule with p < 0.05 for 1 trial).
Bars at or after 2023-07-01 UTC are dropped first, then every bar whose trading date is not `val` is dropped BEFORE any
computation (O20 burn-in inside val, no dev history), exactly as E023/E025. OOS is never read.

    python scripts/run_e036_overnight_reversal_val.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.overnight_reversal import (ALPHA_VAL, BOOT_BLOCK, ENTRY_HM, EXIT_HM, OPEN_HM, SMOOTH_N, arm_events, counts,
                                           decide_b34, evaluate_b32, frame_from_bars)
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import cost_summary, restrict_to_block
from fxresearch.vol_state_london import flag_fomc, fomc_statement_dates

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

df = frame_from_bars(bars)
df = flag_fomc(df, fomc_statement_dates(ROOT / "data" / "calendars" / "fomc_dates.csv"))
if len(df):
    dts = pd.to_datetime(df["date"])
    df["month_end"] = dts.dt.to_period("M").ne(dts.shift(-1).dt.to_period("M")).to_numpy()
ev = arm_events(df, "b33") if len(df) else df
res = evaluate_b32(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b34(res)
cnt = {k: v for k, v in counts(df).items() if not k.startswith("b32_")}
c = cost_summary(ev)
res["lead_cost_gate"] = bool(c.get("n", 0) > 0 and c["mean_net_spec4_pips"] > 0 and c["mean_net_costs_x1_5_pips"] > 0)
res["lead"] = bool(res["decision"] == "SIGNAL" and res["lead_cost_gate"])


def _ev(frame, col="signed_pips"):
    return evaluate_b32(frame[col]) if len(frame) else {}


desc = {}
if len(ev):
    terc = pd.qcut(ev["o20_pips"].abs(), 3, labels=["low", "mid", "high"])
    for k in ["low", "mid", "high"]:
        desc[f"abs_o20_tercile_{k}"] = _ev(ev[terc == k])
    desc["share_long"] = round(float((ev["side"] > 0).mean()), 3)
    desc["long_days"] = _ev(ev[ev["side"] > 0])
    desc["short_days"] = _ev(ev[ev["side"] < 0])
    desc["unconditional_long_r_id"] = _ev(ev, "r_id_pips")
    desc["events_on_fomc_statement_days"] = int(ev["fomc_day"].sum())
    desc["excluding_fomc_statement_days"] = _ev(ev[~ev["fomc_day"]])
    desc["events_on_month_end_dates"] = int(ev["month_end"].sum())
    desc["excluding_month_end_dates"] = _ev(ev[~ev["month_end"]])
    desc["mondays"] = _ev(ev[ev["weekday"] == 0])
    desc["tue_fri"] = _ev(ev[ev["weekday"] != 0])
    desc["sd_r_on_pips"] = round(float(df["r_on_pips"].std()), 3)
    desc["sd_r_id_pips"] = round(float(ev["r_id_pips"].std()), 3)
    desc["b32_daily_arm_same_trade_not_a_trial"] = _ev(arm_events(df, "b32"))


def _by_year(frame):
    if not len(frame):
        return []
    g = frame.assign(year=pd.to_datetime(frame["date"]).dt.year).groupby("year")["signed_pips"]
    return (pd.DataFrame({"n": g.size(), "mean": g.mean(), "hit": g.apply(lambda s: (s > 0).mean())}).round(3)
            .reset_index().to_dict(orient="records"))


by_year = _by_year(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE036 VAL -sign(O{SMOOTH_N}) x ({ENTRY_HM} -> {EXIT_HM} NY), r_on from {OPEN_HM} NY (pre-registered, 1 trial, "
          f"block {BOOT_BLOCK}, p < {ALPHA_VAL}):")
    print(pd.Series(res).to_string())
    print("\nCounts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):", by_year)
    print("\nVAL cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E036 decision:", res["decision"], "| lead:", res["lead"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E036_synthetic_smoke" if args.synthetic else "E036_results"
dump({"result": res, "counts": cnt, "descriptive": desc, "by_year": by_year, "cost_check": c, "n_trials": 1,
      "blocks": ["val"], "boot_block": BOOT_BLOCK, "smooth_n": SMOOTH_N, "alpha": ALPHA_VAL,
      "open_hm_ny": list(OPEN_HM), "entry_hm_ny": list(ENTRY_HM), "exit_hm_ny": list(EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E036_days.csv", index=False)
