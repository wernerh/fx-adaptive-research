from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.vol_state_fix import (
    BOOT_BLOCK, ENTRY_HM, EXIT_HM, MAX_ENTRY_SPREAD_PIPS, MIN_COVERAGE, MIN_MEAN_PIPS, PCTL, SIDE, WINDOW, build_days,
    cost_summary, counts, daily_ranges, decide_b19, evaluate, frame_from_bars, ny_quotes, tradable_events,
)


def test_constants_fixed():
    assert WINDOW == 60 and PCTL == 67 and BOOT_BLOCK == 10 and MIN_MEAN_PIPS == 1.0 and MAX_ENTRY_SPREAD_PIPS == 2.0
    assert MIN_COVERAGE == 0.90 and ENTRY_HM == (2, 0) and EXIT_HM == (8, 15) and SIDE == -1


def _weekdays(n, start=date(2015, 1, 5)):
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def _synthetic(ranges, rets, spread=0.5, valid=None):
    """Range frame and quote tables on consecutive weekdays; trade return rets[i] (pips, EUR/USD mid) on date i."""
    ds = _weekdays(len(ranges))
    rng = pd.DataFrame({"date": ds, "n_bars": 1440, "range_pips": ranges,
                        "valid": valid if valid is not None else [True] * len(ds)})
    e = pd.DataFrame({"bid_open": [1.1 - spread * PIP / 2] * len(ds), "ask_open": [1.1 + spread * PIP / 2] * len(ds)},
                     index=pd.Index(ds))
    x = pd.DataFrame({"bid_open": [1.1 + r * PIP - 0.15 * PIP for r in rets],
                      "ask_open": [1.1 + r * PIP + 0.15 * PIP for r in rets]}, index=pd.Index(ds))
    return rng, e, x


def test_threshold_past_only_strict_and_event_is_next_date():
    ranges = [float(i % 10 + 50) for i in range(60)] + [200.0, 10.0, 10.0]
    rets = [0.0] * 61 + [-20.0, 7.0]
    rng, e, x = _synthetic(ranges, rets)
    df = build_days(rng, e, x)
    # row i corresponds to D = date i+1, P = date i
    assert (df["state"].iloc[:59] == "burn_in").all()
    assert df["state"].iloc[59] == "burn_in"            # P = date 59 is still burn-in (index < 60)
    assert df["state"].iloc[60] == "high"               # P = date 60 (range 200) -> D = date 61 is the event
    assert abs(df["threshold_pips"].iloc[60] - np.percentile(ranges[:60], 67)) < 1e-9
    assert df["state"].iloc[61] == "normal"
    assert abs(df["signed_pips"].iloc[60] - 20.0) < 1e-6   # short: EUR/USD fell 20 pips -> +20
    ev = tradable_events(df)
    assert list(ev["date"]) == [df["date"].iloc[60]]
    # equal to threshold -> not high
    thr = np.percentile(ranges[:60], 67)
    rng2, e2, x2 = _synthetic(ranges[:60] + [thr, 10.0], [0.0] * 62)
    assert build_days(rng2, e2, x2)["state"].iloc[60] == "normal"


def test_invalid_prev_not_event_and_not_in_history():
    ranges = [float(i % 10 + 50) for i in range(60)] + [500.0, 200.0, 10.0]
    valid = [True] * 60 + [False, True, True]
    rng, e, x = _synthetic(ranges, [0.0] * 63, valid=valid)
    df = build_days(rng, e, x)
    assert df["state"].iloc[60] == "prev_invalid"
    # invalid 500 not in history: threshold for P = date 61 uses the 60 valid dates before it (dates 0..59)
    assert abs(df["threshold_pips"].iloc[61] - np.percentile(ranges[:60], 67)) < 1e-9
    assert df["state"].iloc[61] == "high"


def test_no_look_ahead():
    r = np.random.default_rng(3)
    ranges = list(r.uniform(30, 120, 200))
    rets = list(r.normal(0, 25, 200))
    a = build_days(*_synthetic(ranges, rets))
    b = build_days(*_synthetic(ranges[:120] + [v * 10 for v in ranges[120:]], rets[:120] + [v + 500 for v in rets[120:]]))
    # state of D = date i+1 depends on ranges up to date i only
    assert list(a["state"].iloc[:119]) == list(b["state"].iloc[:119])
    assert np.allclose(a["threshold_pips"].iloc[:119].fillna(-1), b["threshold_pips"].iloc[:119].fillna(-1))


def test_spread_skip_and_missing_quote():
    ranges = [float(i % 10 + 50) for i in range(60)] + [200.0, 10.0]
    rng, e, x = _synthetic(ranges, [0.0] * 62, spread=2.5)
    df = build_days(rng, e, x)
    assert df["state"].iloc[60] == "high" and df["excluded"].iloc[60] == "entry_skipped_spread"
    assert tradable_events(df).empty
    rng, e, x = _synthetic(ranges, [0.0] * 62)
    df = build_days(rng, e.drop(index=e.index[61]), x)
    assert df["excluded"].iloc[60] == "missing_entry"
    c = counts(rng, df)
    assert c["missing_entry"] == 1 and c["state_high"] == 1 and c["events_tested"] == 0


def test_costs_order():
    ranges = [float(i % 10 + 50) for i in range(60)] + [200.0, 200.0, 200.0, 10.0]
    rng, e, x = _synthetic(ranges, [0.0] * 61 + [-5.0, 3.0, -4.0])
    ev = tradable_events(build_days(rng, e, x))
    c = cost_summary(ev)
    assert c["n"] == 3 and abs(c["mean_signed_mid_pips"] - ev["signed_pips"].mean()) < 1e-3
    assert c["mean_net_costs_x1_5_pips"] < c["mean_net_spec4_pips"] < c["mean_net_bidask_pips"] < c["mean_signed_mid_pips"]


def test_ranges_and_quotes_from_bars():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    rng = daily_ranges(bars)
    d = date(2024, 3, 5)
    r = rng[rng["date"] == d].iloc[0]
    lo_t = pd.Timestamp("2024-03-04 17:00", tz="America/New_York").tz_convert("UTC")
    hi_t = pd.Timestamp("2024-03-05 17:00", tz="America/New_York").tz_convert("UTC")
    sl = bars[(bars.index >= lo_t) & (bars.index < hi_t)]
    exp = (((sl["bid_high"] + sl["ask_high"]) / 2).max() - ((sl["bid_low"] + sl["ask_low"]) / 2).min()) / PIP
    assert r["n_bars"] == 1440 and r["valid"] and abs(r["range_pips"] - exp) < 1e-9
    q = ny_quotes(bars, *ENTRY_HM)
    t = pd.Timestamp("2024-03-05 02:00", tz="America/New_York").tz_convert("UTC")
    assert abs(q.loc[d, "bid_open"] - bars.loc[t, "bid_open"]) < 1e-12
    q = ny_quotes(bars, *EXIT_HM)
    t = pd.Timestamp("2024-03-05 08:15", tz="America/New_York").tz_convert("UTC")
    assert abs(q.loc[d, "ask_open"] - bars.loc[t, "ask_open"]) < 1e-12
    rng2, df = frame_from_bars(bars)
    row = df[df["date"] == d].iloc[0]
    assert row["prev"] == date(2024, 3, 4)


def test_low_coverage_invalid():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    lo_t = pd.Timestamp("2024-03-05 03:00", tz="America/New_York").tz_convert("UTC")
    bars = bars[(bars.index < lo_t) | (bars.index >= lo_t + pd.Timedelta(minutes=200))]
    rng, df = frame_from_bars(bars)
    assert not rng.loc[rng["date"] == date(2024, 3, 5), "valid"].iloc[0]
    assert df.loc[df["date"] == date(2024, 3, 6), "state"].iloc[0] == "prev_invalid"
    assert counts(rng, df)["low_coverage"] == 1


def test_random_walk_no_signal():
    """No edge by construction: SIGNAL rate over 40 seeds must stay near the one-sided alpha (<= 0.10).
    (A fixed 5-seed 'never SIGNAL' check is not a valid test at alpha 0.05: seed 0 gives a chance SIGNAL.)"""
    sig = 0
    for seed in range(40):
        r = np.random.default_rng(seed)
        n = 1500
        df = build_days(*_synthetic(list(r.uniform(30, 120, n)), list(r.normal(0, 28, n))))
        res = evaluate(tradable_events(df)["signed_pips"])
        assert res["n"] > 300
        sig += decide_b19(res) == "SIGNAL"
    assert sig / 40 <= 0.10


def test_strong_effect_gives_signal():
    r = np.random.default_rng(1)
    n = 1500
    ranges = r.uniform(30, 120, n)
    # EUR/USD falls 6 pips on dates after a high-range day
    hi_prev = np.concatenate([[False], ranges[:-1] > 90])
    rets = np.where(hi_prev, -6.0, 0.0) + r.normal(0, 20, n)
    df = build_days(*_synthetic(list(ranges), list(rets)))
    assert decide_b19(evaluate(tradable_events(df)["signed_pips"])) == "SIGNAL"


def test_decide_rule_edges():
    base = {"mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.2, 2.8)}
    assert decide_b19(base) == "SIGNAL"
    assert decide_b19({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b19({**base, "mean_ci95_block_boot": (-0.1, 2.8), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b19({**base, "mean_pips": -0.5}) == "NONE"
    assert decide_b19({"n": 3, "note": "insufficient sample"}) == "NONE"


def test_restrict_to_block_val_only_and_no_later_bars():
    """E023 (B19v): only val trading dates survive; nothing at/after the cut-off is kept; dev/embargo/oos dropped."""
    from fxresearch.splits import SplitPlan
    from fxresearch.vol_state_fix import restrict_to_block
    from fxresearch.sessions import trading_date
    idx = pd.date_range("2024-01-01", "2024-03-31 23:59", freq="1h", tz="UTC")
    bars = pd.DataFrame({"x": np.arange(len(idx))}, index=idx)
    plan = SplitPlan(date(2024, 1, 20), date(2024, 2, 29), embargo_days=5)
    cut = pd.Timestamp("2024-03-01", tz="UTC")
    out = restrict_to_block(bars, plan, "val", before_utc=cut)
    assert len(out) > 0 and out.index.max() < cut
    td = pd.Index(trading_date(out.index))
    assert (plan.assign(td).to_numpy() == "val").all()
    assert min(td) > date(2024, 1, 25)
