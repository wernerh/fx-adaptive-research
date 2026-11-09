"""E026: post-08:30 NY release-window continuation, calendar-free (sign(J) from 08:45 -> 10:45 NY), DEV ONLY.

Pre-registered in experiments/2026-11-09_E026_release_continuation/ (backlog B21). Val and OOS untouched.
Decision: fxresearch.release_continuation.decide_b21 on per-event signed mid returns; events = |mid 08:45 - mid 08:30 NY| above
the rolling 90th percentile of the 60 valid dates before it. Everything else is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e026_release_continuation.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.release_continuation import (ALT_EXITS_HM, ALT_PCTLS, EXIT_HM, JUMP_END_HM, JUMP_START_HM, PCTL, WINDOW,
                                             counts, decide_b21, frame_from_bars)
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import cost_summary, evaluate
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
df = flag_fomc(df, fomc_statement_dates(ROOT / "data" / "calendars" / "fomc_dates.csv"))
ev = df[df["tested"]] if len(df) else df
res = evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b21(res)
cnt = counts(df)


def _ev(frame, col="signed_pips"):
    return evaluate(frame[col]) if len(frame) else {}


ctrl = df[df["threshold_pips"].notna() & ~df["is_event"] & df["tradable"]] if len(df) else df
desc = {
    "reversal_reading_note": "a negative mean is logged as exploratory only (not a trial)",
    "horizon_0845_0930": _ev(ev, "signed_exit_0930_pips"),
    "horizon_0845_1200": _ev(ev, "signed_exit_1200_pips"),
    "control_non_event_post_burn_in_same_trade": _ev(ctrl),
    "events_on_first_friday": int(ev["first_friday"].sum()) if len(ev) else 0,
    "first_friday_events": _ev(ev[ev["first_friday"]]) if len(ev) else {},
    "non_first_friday_events": _ev(ev[~ev["first_friday"]]) if len(ev) else {},
    "events_on_fomc_statement_days": int(ev["fomc_day"].sum()) if len(ev) else 0,
    "events_mean_abs_jump_pips": round(float(ev["jump_pips"].abs().mean()), 3) if len(ev) else None,
    "events_median_threshold_pips": round(float(ev["threshold_pips"].median()), 3) if len(ev) else None,
    "share_long": round(float((ev["side"] > 0).mean()), 3) if len(ev) else None,
}
if len(df):
    from fxresearch.release_continuation import add_threshold
    for p in ALT_PCTLS:
        alt = add_threshold(df, WINDOW, p, col="thr_alt")
        alt_ev = alt[alt["valid"] & alt["thr_alt"].notna() & (alt["jump_pips"].abs() > alt["thr_alt"]) & alt["tradable"]]
        desc[f"threshold_p{p}"] = _ev(alt_ev)


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
    print(f"\nE026 DEV sign(J) {JUMP_END_HM} -> {EXIT_HM} NY when |J {JUMP_START_HM}->{JUMP_END_HM}| > p{PCTL} of the previous "
          f"{WINDOW} valid dates (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy weekday (descriptive):\n", by_weekday.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E026 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E026_synthetic_smoke" if args.synthetic else "E026_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["dev"], "window": WINDOW, "percentile": PCTL,
      "jump_hm": [list(JUMP_START_HM), list(JUMP_END_HM)], "exit_hm": list(EXIT_HM),
      "alt_exits_hm": {k: list(v) for k, v in ALT_EXITS_HM.items()},
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E026_days.csv", index=False)
