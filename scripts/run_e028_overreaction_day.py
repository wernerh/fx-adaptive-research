"""E028: intraday continuation on overreaction days (17:00 -> 12:00 NY move beyond rolling mean +/- 2 SD of 60 valid dates,
followed 12:00 -> 16:30 NY), DEV ONLY.

Pre-registered in experiments/2026-11-09_E028_overreaction_day/ (backlog B23). Val and OOS untouched.
Decision: fxresearch.overreaction_day.decide_b23 on per-event signed mid returns (block-5 bootstrap). Everything else is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e028_overreaction_day.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.overreaction_day import (ALT_KS, BOOT_BLOCK, ENTRY_HM, EXIT_HM, K, OPEN_HM, WINDOW, counts, decide_b23,
                                         evaluate_b23, frame_from_bars)
from fxresearch.data import PIP
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import cost_summary
from fxresearch.vol_state_london import flag_fomc, fomc_statement_dates

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

df = frame_from_bars(bars)
if len(df):
    df = flag_fomc(df, fomc_statement_dates(ROOT / "data" / "calendars" / "fomc_dates.csv"))
ev = df[df["tested"]] if len(df) else df
res = evaluate_b23(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b23(res)
cnt = counts(df)


def _ev(frame, col="signed_pips"):
    return evaluate_b23(frame[col]) if len(frame) else {}


desc = {"reversal_reading_note": "a negative mean is logged as exploratory only (not a trial)"}
if len(ev):
    desc["positive_events"] = _ev(ev[ev["side"] > 0])
    desc["negative_events"] = _ev(ev[ev["side"] < 0])
    for ka in ALT_KS:
        sub = df[df[f"is_event_k{ka}"] & df["tradable"]]
        desc[f"k_{ka}"] = _ev(sub)
    post = df[df["valid"] & df["hist_sd_pips"].notna() & df["tradable"]]
    desc["control_non_event_long_12_1630_mean_pips"] = round(float(
        (post[~post["is_event"]]["exit_mid"] - post[~post["is_event"]]["entry_mid"]).mean() / PIP), 3)
    desc["events_on_fomc_statement_days"] = int(ev["fomc_day"].sum())
    desc["excl_fomc"] = _ev(ev[~ev["fomc_day"]])
    desc["events_on_first_fridays"] = int(ev["first_friday"].sum())
    desc["excl_first_fridays"] = _ev(ev[~ev["first_friday"]])
    desc["share_long"] = round(float((ev["side"] > 0).mean()), 3)
    desc["mean_abs_r_pips_events"] = round(float(ev["r_pips"].abs().mean()), 3)
    desc["median_hist_sd_pips_events"] = round(float(ev["hist_sd_pips"].median()), 3)


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
    print(f"\nE028 DEV overreaction days (r = {OPEN_HM}->{ENTRY_HM} NY beyond mean +/- {K} SD of {WINDOW} valid dates), "
          f"follow {ENTRY_HM} -> {EXIT_HM} NY (pre-registered, 1 trial, block {BOOT_BLOCK}):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy weekday (descriptive):\n", by_weekday.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E028 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E028_synthetic_smoke" if args.synthetic else "E028_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["dev"], "boot_block": BOOT_BLOCK, "window": WINDOW, "k": K,
      "alt_ks": list(ALT_KS), "open_hm_ny": list(OPEN_HM), "entry_hm_ny": list(ENTRY_HM), "exit_hm_ny": list(EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E028_days.csv", index=False)
