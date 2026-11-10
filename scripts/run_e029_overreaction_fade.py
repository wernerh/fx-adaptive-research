"""E029 (B24): next-morning fade after an overreaction day (17:00 -> 16:55 NY move beyond rolling mean +/- 2 SD of 60 valid val
dates, faded 17:05 -> 02:00 NY next trading date), VAL ONLY.

Pre-registered in experiments/2026-11-10_E029_overreaction_fade_val/ (backlog B24). Dev and OOS untouched.
Bars at or after 2023-07-01 UTC are dropped first, then every bar whose trading date is not `val` is dropped BEFORE any computation
(val-only burn-in, as E023/E025). OOS is never read.
Decision: fxresearch.overreaction_fade.decide_b24 on per-event signed mid returns (block-5 bootstrap). Everything else is descriptive.

    python scripts/run_e029_overreaction_fade.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.data import PIP
from fxresearch.overreaction_fade import (ALT_EXIT_HM, ALT_KS, BOOT_BLOCK, CLOSE_HM, ENTRY_HM, EXIT_HM, K, OPEN_HM, WINDOW,
                                          counts, decide_b24, evaluate_b24, frame_from_bars)
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
if len(df):
    df = flag_fomc(df, fomc_statement_dates(ROOT / "data" / "calendars" / "fomc_dates.csv"))
ev = df[df["tested"]] if len(df) else df
res = evaluate_b24(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b24(res)
cnt = counts(df)


def _ev(frame, col="signed_pips"):
    return evaluate_b24(frame[col]) if len(frame) else {}


desc = {"continuation_reading_note": "a negative mean (continuation) is logged as exploratory only (not a trial)"}
if len(ev):
    desc["positive_days"] = _ev(ev[ev["side"] > 0])
    desc["negative_days"] = _ev(ev[ev["side"] < 0])
    desc["exit_03_00_ny"] = _ev(ev[ev["signed_alt_exit_pips"].notna()], "signed_alt_exit_pips")
    for ka in ALT_KS:
        desc[f"k_{ka}"] = _ev(df[df[f"is_event_k{ka}"] & df["tradable"]])
    post = df[df["valid"] & df["hist_sd_pips"].notna() & df["tradable"] & ~df["is_event"]]
    desc["control_non_event_long_1705_0200_mean_pips"] = round(float(
        (post["exit_mid"] - post["entry_mid"]).mean() / PIP), 3) if len(post) else None
    desc["events_on_fomc_statement_days"] = int(ev["fomc_day"].sum())
    desc["excl_fomc"] = _ev(ev[~ev["fomc_day"]])
    desc["events_on_first_fridays"] = int(ev["first_friday"].sum())
    desc["share_short"] = round(float((ev["side"] > 0).mean()), 3)
    desc["mean_abs_R_pips_events"] = round(float(ev["r_pips"].abs().mean()), 3)
    desc["median_hist_sd_pips_events"] = round(float(ev["hist_sd_pips"].median()), 3)
all_ev = df[df["is_event"] & df["valid"]] if len(df) else df
desc["median_entry_spread_all_events_pips"] = (round(float(all_ev["entry_spread_pips"].median()), 3)
                                               if len(all_ev) and all_ev["entry_spread_pips"].notna().any() else None)


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
    print(f"\nE029 VAL overreaction-day fade (R = {OPEN_HM}->{CLOSE_HM} NY beyond mean +/- {K} SD of {WINDOW} valid val dates), "
          f"fade {ENTRY_HM} -> {EXIT_HM} NY next date (pre-registered, 1 trial, block {BOOT_BLOCK}):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy weekday of D (descriptive):\n", by_weekday.to_string())
    print("\nVAL cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E029 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E029_synthetic_smoke" if args.synthetic else "E029_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["val"], "boot_block": BOOT_BLOCK, "window": WINDOW, "k": K,
      "alt_ks": list(ALT_KS), "open_hm_ny": list(OPEN_HM), "close_hm_ny": list(CLOSE_HM), "entry_hm_ny": list(ENTRY_HM),
      "exit_hm_ny": list(EXIT_HM), "alt_exit_hm_ny": list(ALT_EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E029_days.csv", index=False)
