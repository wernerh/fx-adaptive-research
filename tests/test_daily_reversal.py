from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch.daily_reversal import (
    BOOT_BLOCK, MAX_ENTRY_SPREAD_PIPS, MIN_MEAN_PIPS, PCTL, WINDOW, cost_summary, daily_frame, decide_b18, evaluate,
    exclusion_counts, fomc_overlap, mark_events, tradable_events,
)
from fxresearch.data import PIP, synthetic_bars


def test_constants_fixed():
    assert WINDOW == 60 and PCTL == 80 and BOOT_BLOCK == 10 and MIN_MEAN_PIPS == 1.0 and MAX_ENTRY_SPREAD_PIPS == 2.0


def _weekdays(n, start=date(2015, 1, 5)):
    out, d = [], start
    while len(out) < n + 1:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def _df(moves, rets, entry_spread=0.5, pre=None):
    """Synthetic daily frame on consecutive weekdays: close mid path from moves, trade return rets (pips) on next date."""
    ds = _weekdays(len(moves))
    rows, c = [], 1.1
    for i, (m, r) in enumerate(zip(moves, rets)):
        c += m * PIP
        e = c + (pre[i] if pre else 0.0) * PIP
        rows.append({"date": ds[i], "prev": ds[i - 1] if i else None, "next": ds[i + 1], "valid": True, "missing": None,
                     "move_pips": m, "close_mid": c, "entry_mid": e, "entry_spread_pips": entry_spread,
                     "exit_mid": e + r * PIP, "exit_spread_pips": 0.3})
    return pd.DataFrame(rows)


def test_threshold_past_only_strict_and_friday_excluded():
    moves = [float(i % 10 + 1) for i in range(60)] + [100.0, 1.0, -100.0]
    rets = [0.0] * 60 + [-30.0, 5.0, 40.0]
    v = mark_events(_df(moves, rets))
    assert not v["is_large"].iloc[:60].any()
    thr = np.percentile(np.abs(moves[:60]), 80)
    assert abs(v["threshold_pips"].iloc[60] - thr) < 1e-9
    assert list(v["is_large"].iloc[60:]) == [True, False, True]
    assert abs(v["signed_pips"].iloc[60] - 30) < 1e-6 and abs(v["signed_pips"].iloc[62] - 40) < 1e-6
    # equal to threshold -> not large
    assert not mark_events(_df(moves[:60] + [thr], rets[:61]))["is_large"].iloc[60]
    # Fridays: large moves on Fridays are excluded and counted
    big = mark_events(_df(moves[:60] + [100.0] * 5, [0.0] * 65))
    fri = big[big["is_large"] & big["date"].map(lambda d: d.weekday() == 4)]
    assert len(fri) >= 1 and (fri["excluded"] == "friday").all() and not fri["tested"].any()
    assert exclusion_counts(big)["friday"] == len(fri)


def test_no_look_ahead():
    rng = np.random.default_rng(3)
    moves = list(rng.normal(0, 45, 200))
    rets = list(rng.normal(0, 35, 200))
    a = mark_events(_df(moves, rets))
    b = mark_events(_df(moves[:120] + [m * 10 for m in moves[120:]], rets[:120] + [r + 500 for r in rets[120:]]))
    assert list(a["is_large"].iloc[:120]) == list(b["is_large"].iloc[:120])
    assert np.allclose(a["threshold_pips"].iloc[:121].fillna(-1), b["threshold_pips"].iloc[:121].fillna(-1))


def test_spread_skip_and_non_adjacent_next():
    moves = [float(i % 10 + 1) for i in range(60)] + [100.0]
    v = mark_events(_df(moves, [0.0] * 61, entry_spread=2.5))
    assert v["is_large"].iloc[60] and v["excluded"].iloc[60] in ("entry_skipped_spread", "friday")
    assert tradable_events(v).empty
    df = _df(moves, [0.0] * 61)
    if df["date"].iloc[60].weekday() != 4:
        df.loc[60, "next"] = df["date"].iloc[60] + timedelta(days=2)
        assert mark_events(df)["excluded"].iloc[60] == "next_not_adjacent"


def test_costs_order():
    moves = [float(i % 10 + 1) for i in range(60)] + [100.0, -100.0, 100.0, -100.0]
    v = mark_events(_df(moves, [0.0] * 60 + [-20.0, 10.0, -20.0, 10.0]))
    ev = tradable_events(v)
    c = cost_summary(ev)
    assert c["n"] >= 2 and abs(c["mean_signed_mid_pips"] - ev["signed_pips"].mean()) < 1e-3
    assert c["mean_net_costs_x1_5_pips"] < c["mean_net_spec4_pips"] < c["mean_net_bidask_pips"] < c["mean_signed_mid_pips"]


def test_daily_frame_from_bars_uses_correct_quotes():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df, counts = daily_frame(bars)
    assert counts["no_prev"] == 1 and counts["missing_16_D"] == 0 and counts["missing_16_prev"] == 0
    r = df[df["date"] == date(2024, 3, 5)].iloc[0]  # Tuesday
    assert r["prev"] == date(2024, 3, 4) and r["next"] == date(2024, 3, 6)

    def mid(ts):
        t = pd.Timestamp(ts, tz="America/New_York").tz_convert("UTC")
        return (bars.loc[t, "bid_open"] + bars.loc[t, "ask_open"]) / 2

    assert abs(r["move_pips"] - (mid("2024-03-05 16:00") - mid("2024-03-04 16:00")) / PIP) < 1e-9
    assert abs(r["entry_mid"] - mid("2024-03-05 20:00")) < 1e-12
    assert abs(r["exit_mid"] - mid("2024-03-06 10:45")) < 1e-12


def test_missing_bar_excluded_and_counted():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    t = pd.Timestamp("2024-03-05 16:00", tz="America/New_York").tz_convert("UTC")
    bars = bars[(bars.index < t) | (bars.index >= t + pd.Timedelta(minutes=5))]
    df, counts = daily_frame(bars)
    assert counts["missing_16_D"] == 1 and counts["missing_16_prev"] == 1
    assert df.loc[df["date"] == date(2024, 3, 5), "missing"].iloc[0] == "missing_16_D"
    assert df.loc[df["date"] == date(2024, 3, 6), "missing"].iloc[0] == "missing_16_prev"


def test_random_walk_no_signal():
    for seed in range(5):
        rng = np.random.default_rng(seed)
        n = 1500
        v = mark_events(_df(list(rng.normal(0, 45, n)), list(rng.normal(0, 35, n))))
        res = evaluate(tradable_events(v)["signed_pips"])
        assert res["n"] > 150
        assert decide_b18(res) != "SIGNAL"


def test_strong_reversal_gives_signal():
    rng = np.random.default_rng(1)
    n = 1500
    moves = rng.normal(0, 45, n)
    rets = -0.3 * moves + rng.normal(0, 20, n)
    v = mark_events(_df(list(moves), list(rets)))
    assert decide_b18(evaluate(tradable_events(v)["signed_pips"])) == "SIGNAL"


def test_decide_rule_edges():
    base = {"mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.2, 2.8)}
    assert decide_b18(base) == "SIGNAL"
    assert decide_b18({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b18({**base, "mean_ci95_block_boot": (-0.1, 2.8), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b18({**base, "mean_pips": -0.5}) == "NONE"
    assert decide_b18({"n": 3, "note": "insufficient sample"}) == "NONE"


def test_fomc_overlap():
    moves = [float(i % 10 + 1) for i in range(60)] + [100.0, -100.0, 100.0, -100.0]
    ev = tradable_events(mark_events(_df(moves, [0.0] * 64)))
    d0 = ev["date"].iloc[0]
    o = fomc_overlap(ev, {d0})
    assert o["move_day_is_fomc"] == 1 and o["n"] == len(ev)
