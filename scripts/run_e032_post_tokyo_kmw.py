"""E032 (B27): post-Tokyo-fix EUR appreciation, long EUR/USD 20:55 -> 02:00 America/New_York (Krohn-Mueller-Whelan window),
VAL ONLY.

Pre-registered in experiments/2026-11-10_E032_post_tokyo_kmw_val/ (backlog B27). Dev and OOS untouched.
Bars at or after 2023-07-01 UTC are dropped first, then every bar whose trading date is not `val` is dropped BEFORE any computation.
Decision: fxresearch.post_tokyo_kmw.decide_b27 on per-date signed mid returns (block-20 bootstrap). Everything else is descriptive.

    python scripts/run_e032_post_tokyo_kmw.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.post_tokyo_kmw import (BOOT_BLOCK, ENTRY_HM, EXIT_HM, cost_summary, counts, decide_b27, evaluate,
                                       evaluate_desc, frame_from_bars)
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import restrict_to_block

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
ev = df[df["tested"]] if len(df) else df
res = evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "insufficient sample"}
res["decision"] = decide_b27(res)
cnt = counts(df) if len(df) else {}

sub = lambda m: evaluate_desc(ev.loc[m, "signed_pips"]) if m.any() else {}  # noqa: E731
desc = {}
if len(ev):
    desc = {
        "edt_dates": sub(ev["edt"]),
        "est_dates": sub(~ev["edt"]),
        "first_hour_20_55_21_55": evaluate_desc(ev["first_hour_pips"]),
        "rest_21_55_02_00": evaluate_desc(ev["rest_pips"]),
        "monday_sunday_evening_entries": sub(ev["weekday"] == 0),
        "tuesday_to_friday": sub(ev["weekday"] != 0),
        "raw_means": {"edt": (int(ev["edt"].sum()), round(float(ev.loc[ev["edt"], "signed_pips"].mean()), 3)
                              if ev["edt"].any() else None),
                      "est": (int((~ev["edt"]).sum()), round(float(ev.loc[~ev["edt"], "signed_pips"].mean()), 3)
                              if (~ev["edt"]).any() else None)},
        "note": "clock: window fixed in NY time (paper's); starts at the Tokyo fix in EDT, one hour after it in EST. "
                "Val window 20:55 -> 02:00 NY not computed by any earlier experiment (E029 used 4 conditional events of "
                "17:05 -> 02:00 NY).",
    }


def _group(frame, key):
    if not len(frame):
        return pd.DataFrame()
    k = pd.to_datetime(frame["date"]).dt.year if key == "year" else pd.to_datetime(frame["date"]).dt.day_name()
    return (frame.assign(**{key: k.to_numpy()}).groupby(key)
            .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                 hit=("signed_pips", lambda s: (s > 0).mean())).round(3))


by_year = _group(ev, "year")
by_weekday = _group(ev, "weekday")
c = cost_summary(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE032 VAL long EUR/USD {ENTRY_HM} -> {EXIT_HM} America/New_York, every valid trading date "
          f"(pre-registered, 1 trial, block {BOOT_BLOCK}):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy trading-date weekday (descriptive; Monday = Sunday-evening entry):\n", by_weekday.to_string())
    print("\nVAL cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E032 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E032_synthetic_smoke" if args.synthetic else "E032_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["val"],
      "entry_hm_ny": list(ENTRY_HM), "exit_hm_ny": list(EXIT_HM), "side": "long",
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E032_days.csv", index=False)
