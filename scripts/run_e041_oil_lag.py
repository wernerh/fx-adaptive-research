"""E041 (B45): lagged daily WTI return -> next-day EUR/USD (Ferraro-Rogoff-Rossi, EUR extension), DEV ONLY, 1 trial.

Pre-registered in experiments/2026-11-11_E041_oil_lag/ (backlog B45). Val and OOS untouched.
EUR/USD bars are restricted to dev trading dates BEFORE any computation; WTI bars are cut at 2021-01-01 UTC.
The data gate runs first: if it fails, the run stops as BLOCKED (0 trials used) and no trade result is computed.
Decision: fxresearch.oil_lag.decide_b45 on per-date signed mid returns. Everything else is descriptive.

    python scripts/run_e041_oil_lag.py [--synthetic] [--oil-dir data/raw_oil]
"""
import argparse
import sys
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch import month_end_hedging as mh
from fxresearch import oil_lag as ol
from fxresearch.data import synthetic_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
ap.add_argument("--oil-dir", default=str(ROOT / "data" / "raw_oil"))
args = ap.parse_args()

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E041_synthetic_smoke" if args.synthetic else "E041_results"

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

if args.synthetic:
    oil = synthetic_bars("2024-01-01", "2024-03-31", seed=21)
else:
    oil = mh.load_index(args.oil_dir, ol.OIL)
    oil = oil[oil.index < pd.Timestamp("2021-01-01", tz="UTC")]  # dev only: never read WTI bars from val/OOS dates
oil_desc = {"bars": int(len(oil)), "first": str(oil.index.min()) if len(oil) else None,
            "last": str(oil.index.max()) if len(oil) else None}
print("oil data:", oil_desc)

df, dropped = ol.frame_from_bars(bars, oil) if len(oil) else (pd.DataFrame(), 0)
gate = ol.data_gate(df, oil)
print("Data gate:", gate)
if not gate["ok"]:
    print("E041 decision: BLOCKED (data gate failed; 0 trials used)")
    dump({"status": "BLOCKED", "data_gate": gate, "oil_data": oil_desc, "n_trials": 0, "blocks": ["dev"]},
         out_dir / f"{stem}.json")
    sys.exit(0)

ev = ol.events(df)
res = ol.evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = ol.decide_b45(res)
n = len(ev)


def _r(x):
    return round(float(x), 3) if n else None


costs = {"n": int(n), "mean_signed_mid_pips": _r(ev["signed_pips"].mean()),
         "mean_net_bidask_pips": _r(ev["net_bidask_pips"].mean()), "mean_net_spec4_pips": _r(ev["net_spec4_pips"].mean()),
         "mean_net_costs_x1_5_pips": _r(ev["net_x1_5_pips"].mean()),
         "median_spread_entry_pips": _r(ev["entry_spread_pips"].median()),
         "median_spread_exit_pips": _r(ev["exit_spread_pips"].median())}
cnt = {**ol.counts(df), "weekend_trading_dates_dropped": int(dropped)}


def _ev(x):
    x = pd.Series(x).dropna()
    return ol.evaluate(x) if len(x) >= 2 * ol.BOOT_BLOCK else {"n": int(len(x))}


stmt = set()
cal_path = ROOT / "data" / "calendars" / "fomc_dates.csv"
if cal_path.exists() and not args.synthetic:
    cal = pd.read_csv(cal_path)
    cal = cal[cal["scheduled"].astype(str).str.lower().eq("true") & ~cal["cancelled"].astype(str).str.lower().eq("true")]
    stmt = {pd.Timestamp(x).date() for x in cal["statement_date"]}

desc = {}
if n:
    terc = pd.qcut(ev["o"].abs(), 3, labels=["low", "mid", "high"]) if n >= 30 else None
    desc = {
        "share_long_eurusd": round(float((ev["side"] > 0).mean()), 3),
        "o_stats": {"mean": round(float(ev["o"].mean()), 5), "sd": round(float(ev["o"].std()), 5),
                    "abs_median": round(float(ev["o"].abs().median()), 5)},
        "mondays": _ev(ev.loc[ev["weekday"] == 0, "signed_pips"]),
        "fridays_weekend_hold": _ev(ev.loc[ev["weekday"] == 4, "signed_pips"]),
        "excl_fomc_statement_dates": _ev(ev.loc[~ev["date"].isin(stmt), "signed_pips"]),
        "fomc_statement_dates_in_tested": int(ev["date"].isin(stmt).sum()),
        "unconditional_long_eurusd": _ev(ev["move_pips"]),
        "sd_move_pips": round(float(ev["move_pips"].std()), 3),
        "by_year": (ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")["signed_pips"]
                    .agg(n="size", mean="mean", hit=lambda x: (x > 0).mean()).round(3).reset_index()
                    .to_dict(orient="records")),
    }
    if terc is not None:
        for lab in ("low", "mid", "high"):
            desc[f"abs_o_tercile_{lab}"] = _ev(ev.loc[terc == lab, "signed_pips"])
    cont = ev[ev["contemp_move_pips"].notna()]
    desc["contemporaneous_corr_o_vs_eurusd_1600_prev_to_1600_D"] = {
        "n": int(len(cont)), "corr": round(float(cont["o"].corr(cont["contemp_move_pips"])), 4) if len(cont) > 2 else None,
        "note": "stated sign: oil up with EUR/USD up -> positive"}
    desc["lag_corr_o_vs_next_move"] = round(float(ev["o"].corr(ev["move_pips"])), 4)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE041 DEV lagged WTI -> next-day EUR/USD, position = +sign(ln WTI 16:00 London D / prev), 16:05 D -> 16:00 next")
    print(pd.Series(res).to_string())
    print("Costs (descriptive):", costs)
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
print("E041 decision B45:", res["decision"])

dump({"status": "complete", "data_gate": gate, "oil_data": oil_desc, "result_b45": res, "counts": cnt, "cost_check": costs,
      "descriptive": desc, "n_trials": 1, "blocks": ["dev"], "boot_block": ol.BOOT_BLOCK,
      "first_date": str(df["date"].iloc[0]), "last_date": str(df["date"].iloc[-1])}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E041_days.csv", index=False)
