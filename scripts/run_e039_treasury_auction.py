"""E039: US Treasury coupon-auction demand shock -> EUR/USD continuation (B40: 10-date hold, B41: next-date hold), DEV ONLY, 2 trials.

Pre-registered in experiments/2026-11-11_E039_treasury_auction/ (R086). Val and OOS untouched: the auction calendar is fetched for
dev dates only and bars are restricted to dev trading dates BEFORE any computation. Decision: fxresearch.treasury_auction.decide
per arm. Everything else is descriptive.

    python scripts/run_e039_treasury_auction.py [--synthetic] [--ustb-dir data/raw_ustb]
"""
import argparse
import glob
import json
from datetime import date, time, timedelta

import numpy as np
import pandas as pd
from scipy import stats

from _common import ROOT, dump, load_bars
from fxresearch import treasury_auction as ta
from fxresearch.data import load_bid_ask_csv
from fxresearch.roll_momentum import evaluate
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import cost_summary

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
ap.add_argument("--ustb-dir", default=str(ROOT / "data" / "raw_ustb"))
args = ap.parse_args()

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E039_synthetic_smoke" if args.synthetic else "E039_results"
ARMS = list(ta.HOLDS)


def finish(payload: dict):
    payload.update({"n_trials": 2, "blocks": ["dev"], "arms": ta.HOLDS, "boot_block": ta.BOOT_BLOCK, "alpha_t": ta.ALPHA_T})
    dump(payload, out_dir / f"{stem}.json")
    print("E039 decision:", payload.get("decision"))
    raise SystemExit(0)


# ---- phase 1: auction calendar -------------------------------------------------------------------------------------------
if args.synthetic:
    recs, d = [], date(2024, 1, 2)
    while d <= date(2024, 2, 28):
        if d.weekday() < 5:
            recs.append({"auction_date": d.isoformat(), "security_type": "Note", "security_term": "5-Year",
                         "closing_time_comp": "01:00 PM", "inflation_index_security": "No", "floating_rate": "No",
                         "cusip": f"S{d:%m%d}"})
        d += timedelta(days=1)
    fetch = {"status": "ok", "records": len(recs)}
else:
    fp = out_dir / "E039_auctions_fetch.json"
    fetch = json.loads(fp.read_text()) if fp.exists() else {"status": "missing"}
    recs = []
    if fetch.get("status") == "ok":
        recs = pd.read_csv(out_dir / "E039_auctions_raw.csv", dtype=str, keep_default_na=False).to_dict(orient="records")
if fetch.get("status") != "ok":
    finish({"decision": "BLOCKED", "blocked_reason": f"auction calendar fetch {fetch.get('status')}", "fetch": fetch})

cal = ta.calendar_from_records(recs)
gate = ta.calendar_gate(cal, years=[2024] if args.synthetic else range(2015, 2021))
if args.synthetic:
    gate["pass"] = True  # synthetic smoke covers ~2 months only
cal_diag = {"reasons": cal["reason"].value_counts().to_dict(),
            "close_time_values": cal.loc[cal["qualifying"], "closing_time_comp_raw"].astype(str).value_counts().head(15).to_dict(),
            "unparsed_examples": cal.loc[cal["qualifying"] & cal["close_time"].isna(), "closing_time_comp_raw"]
            .astype(str).head(10).tolist(),
            "security_types": cal["security_type"].astype(str).value_counts().to_dict()}
print("Calendar gate:", gate)
print("Calendar diagnostics:", cal_diag)
if not args.synthetic:
    cal.to_csv(out_dir / "E039_calendar_parsed.csv", index=False)
if not gate["pass"]:
    finish({"decision": "BLOCKED", "blocked_reason": "calendar gate failed (parser may be fixed once, SPEC 11 / R086)",
            "gate": gate, "calendar_diag": cal_diag, "fetch_fields": fetch.get("field_names")})

# ---- phase 2: dev bars and events -------------------------------------------------------------------------------------------
bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())
dates = ta.weekday_trading_dates(bars)
exit_q = ta.ny_quotes(bars, *ta.EXIT_HM)

ev = ta.auction_events(cal)
df = ta.build_events(ev, bars, dates, exit_q)
results, cnts, costs = {}, {}, {}
for arm in ARMS:
    results[arm] = ta.evaluate_arm(df, arm)
    cnts[arm] = ta.counts(df, arm)
    e = ta.arm_events(df, arm)
    costs[arm] = cost_summary(e) if len(e) else {"n": 0}
    results[arm]["lead_cost_gate"] = bool(costs[arm].get("n", 0) > 0 and costs[arm]["mean_net_spec4_pips"] > 0
                                          and costs[arm]["mean_net_costs_x1_5_pips"] > 0)


def _ev(x):
    x = pd.Series(x, dtype=float).dropna()
    return evaluate(x) if len(x) >= 2 * ta.BOOT_BLOCK else {"n": int(len(x)), "mean_pips": round(float(x.mean()), 3) if len(x) else None}


desc = {"events_total": int(len(df)), "multi_auction_events": int((df["n_auctions"] > 1).sum()) if len(df) else 0,
        "share_long": round(float((df["side"] > 0).mean()), 3) if len(df) else None,
        "window_pips_sd": round(float(df["window_pips"].std()), 3) if len(df) else None,
        "close_times": df["close_time"].astype(str).value_counts().to_dict() if len(df) else {}}
by_year = {}
for arm in ARMS:
    e = ta.arm_events(df, arm)
    if len(e) < 3:
        continue
    r = stats.linregress(e["window_pips"], e[f"{arm}_ret_pips"])
    desc[f"{arm}_slope_ret_on_window"] = {"n": int(len(e)), "slope": round(float(r.slope), 4),
                                          "t_stat": round(float(r.slope / r.stderr), 3), "p_two_sided": round(float(r.pvalue), 4)}
    for tb in ("short", "long", "mixed", "unknown"):
        sub = e.loc[e["tenor"] == tb, "signed_pips"]
        if len(sub):
            desc[f"{arm}_tenor_{tb}"] = _ev(sub)
    desc[f"{arm}_unconditional_long"] = _ev(e[f"{arm}_ret_pips"])
    g = e.assign(year=pd.to_datetime(e["date"]).dt.year).groupby("year")["signed_pips"]
    by_year[arm] = (pd.DataFrame({"n": g.size(), "mean": g.mean(), "hit": g.apply(lambda s: (s > 0).mean())}).round(3)
                    .reset_index().to_dict(orient="records"))

# non-auction control (same T, same weekday one week earlier, not itself an auction date)
ctrl = ta.build_events(ta.control_events(ev, cal), bars, dates, exit_q)
for arm in ARMS:
    desc[f"{arm}_control_week_earlier"] = _ev(ta.arm_events(ctrl, arm)["signed_pips"]) if len(ctrl) else {"n": 0}

# ustbondtrusd window sign (2019-2020 sub-sample, descriptive; data failure never blocks)
ustb = {"status": "not_available"}
bid_f = sorted(glob.glob(f"{args.ustb_dir}/ustbondtrusd-m1-bid-*.csv"))
ask_f = sorted(glob.glob(f"{args.ustb_dir}/ustbondtrusd-m1-ask-*.csv"))
if bid_f and ask_f and len(df) and not args.synthetic:
    try:
        ub = load_bid_ask_csv(bid_f, ask_f)
        pre = ta.quotes_at(ub, [ta._ny_utc(d, t, -ta.WINDOW_MIN) for d, t in zip(df["date"], df["close_time"])])
        post = ta.quotes_at(ub, [ta._ny_utc(d, t, ta.WINDOW_MIN) for d, t in zip(df["date"], df["close_time"])])
        u = ((post["bid"] + post["ask"]) / 2 - (pre["bid"] + pre["ask"]) / 2).to_numpy()
        df["ustb_window"] = u
        df["ustb_side"] = np.sign(u)   # T-Bond CFD up = demand up = USD down = EUR/USD up
        m = df["ustb_side"].notna() & (df["ustb_side"] != 0) & (df["side"] != 0)
        ustb = {"status": "ok", "events_with_ustb": int(m.sum()),
                "sign_agreement_with_eurusd": round(float((df.loc[m, "ustb_side"] == df.loc[m, "side"]).mean()), 3) if m.any() else None}
        for arm in ARMS:
            t = df[df[f"{arm}_tested"] & m]
            ustb[f"{arm}_eurusd_signal_same_events"] = _ev(t[f"{arm}_signed_pips"])
            ustb[f"{arm}_ustb_signal"] = _ev(t["ustb_side"] * t[f"{arm}_ret_pips"])
    except Exception as exc:  # noqa: BLE001 - descriptive only
        ustb = {"status": "failed", "error": repr(exc)[:300]}
desc["ustbondtrusd"] = ustb

decision = {arm: results[arm]["decision"] for arm in ARMS}
with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE039 DEV Treasury coupon auctions: sign(EUR/USD T-10 -> T+10 min) x (T+10 -> 16:00 NY +h trading dates), "
          f"pre-registered, 2 trials, block {ta.BOOT_BLOCK}, t p < {ta.ALPHA_T}")
    for arm in ARMS:
        print(f"\n{arm} (hold {ta.HOLDS[arm]} trading dates):", pd.Series(results[arm]).to_string(), sep="\n")
        print("Counts:", cnts[arm])
        print("DEV cost check (descriptive):", costs[arm])
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
    print("\nBy year (descriptive):", by_year)

if not args.synthetic:
    df.to_csv(out_dir / "E039_events.csv", index=False)
finish({"result_b40": results["B40"], "result_b41": results["B41"], "counts": cnts, "cost_check": costs, "descriptive": desc,
        "by_year": by_year, "gate": gate, "calendar_diag": cal_diag, "fetch_fields": fetch.get("field_names"),
        "first_event": str(df["date"].iloc[0]) if len(df) else None, "last_event": str(df["date"].iloc[-1]) if len(df) else None,
        "decision": decision})
