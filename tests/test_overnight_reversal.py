from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.overnight_reversal import (
    ALPHA, BOOT_BLOCK, ENTRY_HM, EXIT_HM, MIN_EVENTS, MIN_MEAN_PIPS, OPEN_HM, SMOOTH_N, arm_events, build_days, counts,
    decide_b32, decide_b33, evaluate_b32, evening_quotes, frame_from_bars, smoothed_signal,
)
from fxresearch.vol_state_fix import cost_summary


def _q(dates, mids, spread=0.00002):
    return pd.DataFrame({"bid_open": [m - spread / 2 for m in mids], "ask_open": [m + spread / 2 for m in mids]},
                        index=pd.Index(dates))


def _synthetic(r_on, r_id, start=date(2015, 1, 5)):
    ds = [start + timedelta(days=i) for i in range(len(r_on))]
    o = [1.1] * len(ds)
    i = [1.1 + r * PIP for r in r_on]
    x = [1.1 + (a + b) * PIP for a, b in zip(r_on, r_id)]
    return ds, _q(ds, o), _q(ds, i), _q(ds, x)


def test_constants_fixed():
    assert OPEN_HM == (17, 5) and ENTRY_HM == (7, 0) and EXIT_HM == (16, 55)
    assert SMOOTH_N == 20 and BOOT_BLOCK == 20 and ALPHA == 0.025 and MIN_EVENTS == 500 and MIN_MEAN_PIPS == 1.0
    assert decide_b33 is decide_b32


def test_b32_fades_overnight_move():
    df = build_days(*_synthetic([5.0, -3.0], [-2.0, -4.0]))
    assert list(df["b32_side"]) == [-1.0, 1.0]
    assert np.allclose(df["b32_signed_pips"], [2.0, -4.0])
    assert np.allclose(df["r_on_pips"], [5.0, -3.0]) and np.allclose(df["r_id_pips"], [-2.0, -4.0])


def test_smoothed_signal_past_only_and_skips_missing():
    r = pd.Series([1.0] * 5 + [np.nan] + [1.0] * 20 + [-100.0, 0.0])
    s = smoothed_signal(r, n=20)
    assert s.iloc[:21].isna().all()          # 20 valid values (indices 0-4, 6-20) needed before the first O20
    assert s.iloc[21] == 20.0                # uses indices 0-4 and 6-20, skipping the NaN
    assert s.iloc[26] == 20.0                # excludes own value (-100)
    assert np.isclose(s.iloc[27], -81.0)     # 19 x 1.0 + (-100)


def test_b33_side_and_burn_in():
    r_on = [1.0] * 20 + [5.0, 5.0]
    df = build_days(*_synthetic(r_on, [3.0] * 22))
    assert df["b33_excluded"].iloc[:20].eq("missing_signal").all()
    assert df["b33_tested"].iloc[20] and df["b33_side"].iloc[20] == -1.0
    assert np.isclose(df["o20_pips"].iloc[21], 24.0)
    assert np.isclose(df["b33_signed_pips"].iloc[21], -3.0)


def test_exclusions_in_order():
    ds, o, i, x = _synthetic([5.0, 0.0, 5.0, 5.0, 5.0], [1.0] * 5)
    o = o.drop(ds[0])
    x = x.drop(ds[2])
    i.loc[ds[3], "ask_open"] += 3 * PIP
    x = x.drop(ds[1])  # zero signal takes precedence over missing exit
    df = build_days(ds, o, i, x)
    assert list(df["b32_excluded"].iloc[:4]) == ["missing_signal", "zero_signal", "missing_exit", "entry_skipped_spread"]
    assert pd.isna(df["b32_excluded"].iloc[4])
    i2 = i.drop(ds[4])
    df2 = build_days(ds, o, i2, x)
    assert df2["b32_excluded"].iloc[4] == "missing_signal"   # 07:00 is both signal end and entry
    c = counts(df)
    assert c["b32_tested"] == 1 and c["b32_zero_signal"] == 1 and c["b32_entry_skipped_spread"] == 1


def test_no_look_ahead_side():
    r = np.random.default_rng(1)
    r_on = list(r.normal(0, 15, 100))
    a = build_days(*_synthetic(r_on, list(r.normal(0, 40, 100))))
    b = build_days(*_synthetic(r_on, list(r.normal(0, 40, 100) + 50)))
    assert list(a["b32_side"]) == list(b["b32_side"])
    assert a["b33_side"].fillna(9).tolist() == b["b33_side"].fillna(9).tolist()


def test_quotes_from_bars_ny_time():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df = frame_from_bars(bars)

    def mid(ts):
        t = pd.Timestamp(ts, tz="America/New_York").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2
    row = df[df["date"] == date(2024, 3, 5)].iloc[0]          # Tuesday: opens Monday 17:05 NY
    assert abs(row["open_mid"] - mid("2024-03-04 17:05")) < 1e-12
    assert abs(row["entry_mid"] - mid("2024-03-05 07:00")) < 1e-12
    assert abs(row["exit_mid"] - mid("2024-03-05 16:55")) < 1e-12
    eq = evening_quotes(bars)
    if date(2024, 3, 4) in eq.index:                          # Monday opens Sunday 17:05 NY if bars exist then
        t = pd.Timestamp("2024-03-03 17:05", tz="America/New_York").tz_convert("UTC")
        if t in bars.index:
            assert abs(eq.loc[date(2024, 3, 4), "bid_open"] - bars.loc[t, "bid_open"]) < 1e-12


def test_random_walk_no_signal():
    sig = 0
    for seed in range(40):
        r = np.random.default_rng(500 + seed)
        n = 1500
        df = build_days(*_synthetic(list(r.normal(0, 15, n)), list(r.normal(0, 45, n))))
        for arm in ("b32", "b33"):
            sig += decide_b32(evaluate_b32(df[df[f"{arm}_tested"]][f"{arm}_signed_pips"])) == "SIGNAL"
    assert sig / 80 <= 0.05


def test_strong_reversal_gives_signal_and_small_sample_none():
    r = np.random.default_rng(3)
    n = 1500
    r_on = r.normal(0, 15, n)
    df = build_days(*_synthetic(list(r_on), list(-np.sign(r_on) * 6.0 + r.normal(0, 45, n))))
    assert decide_b32(evaluate_b32(df[df["b32_tested"]]["b32_signed_pips"])) == "SIGNAL"
    small = df[df["b32_tested"]]["b32_signed_pips"].iloc[:400]
    assert decide_b32(evaluate_b32(small)) == "NONE"


def test_arm_events_costs():
    df = build_days(*_synthetic([5.0, -3.0], [-2.0, -4.0]))
    ev = arm_events(df, "b32")
    c = cost_summary(ev)
    assert c["n"] == 2 and c["mean_net_spec4_pips"] < c["mean_signed_mid_pips"]
    assert c["mean_net_costs_x1_5_pips"] < c["mean_net_spec4_pips"]


# --- E036 (B34): val confirmation of the B33 arm, 1 trial, p < 0.05 ---------------------------------------------------------

def test_b34_rule_constants_and_thresholds():
    from fxresearch.overnight_reversal import ALPHA_VAL, decide_b34
    assert ALPHA_VAL == 0.05 and ALPHA == 0.025      # E035 rule untouched
    base = {"n": 600, "mean_pips": 2.0, "t_p_one_sided": 0.04, "mean_ci95_block_boot": (0.1, 4.0)}
    assert decide_b34(base) == "SIGNAL"
    assert decide_b32(base) == "WEAK"                 # p 0.04 fails the dev Bonferroni bar, passes the val bar
    assert decide_b34({**base, "t_p_one_sided": 0.06, "mean_ci95_block_boot": (-0.1, 4.0)}) == "NONE"
    assert decide_b34({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b34({**base, "n": 499}) == "NONE"
    assert decide_b34({"n": 0, "note": "no events"}) == "NONE"


def test_b34_random_walk_signal_rate():
    from fxresearch.overnight_reversal import decide_b34
    sig = 0
    for seed in range(60):
        r = np.random.default_rng(900 + seed)
        n = 620
        df = build_days(*_synthetic(list(r.normal(0, 15, n)), list(r.normal(0, 45, n))))
        sig += decide_b34(evaluate_b32(df[df["b33_tested"]]["b33_signed_pips"])) == "SIGNAL"
    assert sig / 60 <= 0.1


def test_e036_val_restriction_burn_in_inside_val():
    from fxresearch.splits import SplitPlan
    from fxresearch.sessions import trading_date
    from fxresearch.vol_state_fix import restrict_to_block
    bars = synthetic_bars(date(2024, 1, 1), date(2024, 3, 31))
    plan = SplitPlan(date(2024, 1, 31), date(2024, 3, 15), embargo_days=0)
    cut = pd.Timestamp("2024-03-16", tz="UTC")
    vb = restrict_to_block(bars, plan, "val", before_utc=cut)
    assert vb.index.max() < cut
    td = pd.Index(trading_date(vb.index))
    assert (plan.assign(td).to_numpy() == "val").all()
    df = frame_from_bars(vb)
    assert min(df["date"]) > date(2024, 1, 31)
    assert df["burn_in"].iloc[:SMOOTH_N].all()          # O20 history built from val dates only
