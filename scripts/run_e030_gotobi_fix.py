"""E030: USD appreciation into the Tokyo fix on gotobi dates (short EUR/USD 08:55 -> 09:55 Asia/Tokyo), DEV ONLY.

Pre-registered in experiments/2026-11-10_E030_gotobi_tokyo_fix/ (backlog B25). Val and OOS untouched.
Decision: fxresearch.gotobi_fix.decide_b25 on per-event signed mid returns. Everything else (non-gotobi control, month-end and
weekend-shifted subsets, 09:25 -> 09:55 last half hour, by year, by weekday, costs) is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e030_gotobi_fix.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.gotobi_fix import (BOOT_BLOCK, ENTRY_HM, EXIT_HM, cost_summary, counts, decide_b25, evaluate,
                                   frame_from_bars)
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

df = frame_from_bars(bars)
ev = df[df["tested"]]
res = evaluate(ev["signed_pips"])
res["decision"] = decide_b25(res)
cnt = counts(df)

ctrl = df[~df["gotobi"] & df["tradable"]]
sub = lambda m: evaluate(ev.loc[m, "signed_pips"]) if m.any() else {}  # noqa: E731
desc = {
    "control_non_gotobi_same_trade": evaluate(ctrl["signed_pips"]),
    "gotobi_month_end": sub(ev["month_end"]),
    "gotobi_not_month_end": sub(~ev["month_end"]),
    "gotobi_weekend_shifted": sub(ev["weekend_shifted"]),
    "gotobi_not_weekend_shifted": sub(~ev["weekend_shifted"]),
    "gotobi_last_half_hour_09_25_09_55": evaluate(ev["late_signed_pips"]),
    "control_last_half_hour_09_25_09_55": evaluate(ctrl["late_signed_pips"]),
    "difference_gotobi_minus_control_mean_pips": (round(float(ev["signed_pips"].mean() - ctrl["signed_pips"].mean()), 3)
                                                  if len(ev) and len(ctrl) else None),
    "limitation": "Japanese public holidays not in repo: not shifted, count not computed; gotobi rule is practitioner "
                  "convention, UNVERIFIED as Ito & Yamada's; EUR/USD is the USD leg of a USD/JPY effect",
}
# Subsets under 40 events are "insufficient sample" in evaluate (block 20); report their raw n and mean as well.
desc["subset_raw_means"] = {k: (int(m.sum()), round(float(ev.loc[m, "signed_pips"].mean()), 3) if m.any() else None)
                            for k, m in {"month_end": ev["month_end"], "weekend_shifted": ev["weekend_shifted"]}.items()}


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
c_ctrl = cost_summary(ctrl)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE030 DEV short EUR/USD {ENTRY_HM} -> {EXIT_HM} Asia/Tokyo on gotobi dates (pre-registered, 1 trial, "
          f"block {BOOT_BLOCK}):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy weekday (descriptive):\n", by_weekday.to_string())
    print("\nDEV cost check, events (descriptive):")
    print(pd.Series(c).to_string())
    print("\nDEV cost check, non-gotobi control (descriptive):")
    print(pd.Series(c_ctrl).to_string())
print("E030 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E030_synthetic_smoke" if args.synthetic else "E030_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "cost_check_control": c_ctrl, "n_trials": 1, "blocks": ["dev"],
      "entry_hm_tokyo": list(ENTRY_HM), "exit_hm_tokyo": list(EXIT_HM), "side": "short",
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E030_days.csv", index=False)
