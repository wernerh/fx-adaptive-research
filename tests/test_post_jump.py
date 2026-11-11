"""E043 (B48) post-jump reversal tests: constants, past-only bipower, grid, exclusions, trade timing, bootstrap, decision."""
import numpy as np
import pandas as pd

from fxresearch.data import OHLC, PIP, synthetic_bars
from fxresearch.post_jump import (
    ALPHA, BOOT_N, EXCLUSION_ORDER, K, MIN_ABS_MOVE, MIN_EVENTS, MIN_MEAN_PIPS, SIGN, THRESHOLD, build_events,
    cluster_bootstrap_ci, counts, decide_b48, evaluate, frame_from_bars, jump_stats, lm_threshold, slot_grid,
)


def _shift(bars, offsets_pips: pd.Series):
    b = bars.copy()
    off = offsets_pips.reindex(b.index).fillna(0.0).to_numpy() * PIP
    for side in ("bid", "ask"):
        for f in OHLC:
            b[f"{side}_{f}"] = b[f"{side}_{f}"] + off
    return b


def _inject(bars, starts, size_pips, revert_pips, seed=1):
    """Level jump of +/-size at start+2 min (inside the slot starting at `start`), then revert `revert_pips` (same sign as the
    fade) linearly between start+15 and start+65 min. Returns shifted bars."""
    rng = np.random.default_rng(seed)
    off = pd.Series(0.0, index=bars.index)
    mins = (bars.index - bars.index[0]).total_seconds().to_numpy() / 60
    t0 = bars.index[0]
    for s in starts:
        sgn = rng.choice([-1.0, 1.0])
        m = (s - t0).total_seconds() / 60
        jump = np.where(mins >= m + 2, sgn * size_pips, 0.0)
        frac = np.clip((mins - (m + 15)) / 50, 0, 1)
        rev = -sgn * revert_pips * frac
        off += jump + rev
    return _shift(bars, off)


def _starts(bars, every_hours=7):
    """Jump slots every `every_hours` hours, NY time away from 16:00-18:30, not in the first day."""
    g = slot_grid(bars)
    ny = g.index.tz_convert("America/New_York")
    ok = ((ny.hour < 16) | (ny.hour >= 19)) & (ny.minute == 0) & (g.index >= g.index[0] + pd.Timedelta(days=2))
    cand = g.index[ok]
    out, last = [], None
    for t in cand:
        if last is None or t - last >= pd.Timedelta(hours=every_hours):
            out.append(t)
            last = t
    return out


def test_constants_fixed():
    assert K == 270 and SIGN == -1.0 and MIN_ABS_MOVE == 0.0005
    assert round(THRESHOLD, 3) == 5.395 and round(lm_threshold(288, 0.01), 3) == 5.395
    assert MIN_EVENTS == 300 and MIN_MEAN_PIPS == 1.0 and ALPHA == 0.05 and BOOT_N == 2000
    assert EXCLUSION_ORDER == ("roll_hour", "week_open", "inside_hold", "missing_entry", "missing_exit",
                               "entry_skipped_spread")


def test_grid_skips_weekend_and_quote_is_first_bar_open():
    b = synthetic_bars("2024-01-01", "2024-01-15")
    g = slot_grid(b)
    ny = g.index.tz_convert("America/New_York")
    assert not ((ny.dayofweek == 5).any())
    t = g.index[100]
    assert g.loc[t, "bid_open"] == b.loc[t, "bid_open"]
    gs = jump_stats(g)
    # return of the last Friday slot (16:55 NY) has no t+5 inside the grid -> missing
    fri = gs[(ny.dayofweek == 4) & (ny.hour == 16) & (ny.minute == 55)]
    assert fri["r"].isna().all()


def test_sigma_is_past_only():
    b = synthetic_bars("2024-01-01", "2024-01-20")
    g = jump_stats(slot_grid(b))
    i = 2000
    t = g.index[i]
    b2 = _shift(b, pd.Series(30.0, index=b.index[b.index >= t + pd.Timedelta(minutes=2)]))
    g2 = jump_stats(slot_grid(b2))
    assert np.allclose(g["sigma"].iloc[: i + 1], g2["sigma"].iloc[: i + 1], equal_nan=True)
    assert np.allclose(g["L"].iloc[:i], g2["L"].iloc[:i], equal_nan=True)
    assert abs(g2["L"].iloc[i]) > THRESHOLD and g2["jump"].iloc[i]


def test_jump_needs_5_pips_and_burn_in():
    b = synthetic_bars("2024-01-01", "2024-01-20", vol_pips_per_min=0.05)
    g = jump_stats(slot_grid(b))
    assert g["sigma"].iloc[: K - 1].isna().all()
    t = g.index[2000]
    b2 = _shift(b, pd.Series(4.0, index=b.index[b.index >= t + pd.Timedelta(minutes=2)]))
    g2 = jump_stats(slot_grid(b2))
    assert abs(g2.loc[t, "L"]) > THRESHOLD and not g2.loc[t, "jump"]   # big L but < 5 pips
    b3 = _shift(b, pd.Series(6.0, index=b.index[b.index >= t + pd.Timedelta(minutes=2)]))
    assert jump_stats(slot_grid(b3)).loc[t, "jump"]


def test_trade_timing_fade_sign_and_skipped_bar():
    b = synthetic_bars("2024-01-01", "2024-01-20", vol_pips_per_min=0.05, spread_pips_=0.2)
    t = slot_grid(b).index[2100]                              # 02:00 NY, outside the roll hour
    off = pd.Series(0.0, index=b.index)
    off[b.index >= t + pd.Timedelta(minutes=2)] += 20.0       # jump up
    off[b.index >= t + pd.Timedelta(minutes=7)] -= 1.0        # skipped bar t+5 -> t+10
    off[b.index >= t + pd.Timedelta(minutes=40)] -= 8.0       # reversal inside the hold
    off[b.index >= t + pd.Timedelta(minutes=72)] -= 50.0      # after exit: must not count
    g, ev = frame_from_bars(_shift(b, off))
    row = ev[ev["slot"] == t].iloc[0]
    assert row["side"] == -1.0 and row["tested"]
    assert abs(row["signed_pips"] - 8.0) < 0.6
    assert abs(row["skipped_bar_signed_pips"] - 1.0) < 0.6


def test_exclusions_roll_hold_spread_missing():
    b = synthetic_bars("2024-01-01", "2024-01-25", vol_pips_per_min=0.05)
    g = slot_grid(b)
    ny = g.index.tz_convert("America/New_York")
    roll = g.index[(ny.hour == 17) & (ny.minute == 10)][3]
    t1 = g.index[(ny.hour == 10) & (ny.minute == 0)][5]
    t2 = t1 + pd.Timedelta(minutes=30)                         # inside t1's hold
    t3 = t1 + pd.Timedelta(days=2)                             # spread at entry widened
    t4 = t1 + pd.Timedelta(days=3)                             # exit bars removed
    off = pd.Series(0.0, index=b.index)
    for t in (roll, t1, t2, t3, t4):
        off[b.index >= t + pd.Timedelta(minutes=2)] += 15.0
    bb = _shift(b, off)
    e = (bb.index >= t3 + pd.Timedelta(minutes=10)) & (bb.index < t3 + pd.Timedelta(minutes=15))
    bb.loc[e, "ask_open"] += 3 * PIP
    bb = bb[~((bb.index >= t4 + pd.Timedelta(minutes=70)) & (bb.index < t4 + pd.Timedelta(minutes=75)))]
    g2, ev = frame_from_bars(bb)
    ex = dict(zip(ev["slot"], ev["excluded"]))
    assert ex[roll] == "roll_hour" and pd.isna(ex[t1]) and ex[t2] == "inside_hold"
    assert ex[t3] == "entry_skipped_spread" and ex[t4] == "missing_exit"
    c = counts(g2, ev)
    assert c["events_tested"] == int(ev["tested"].sum()) and c["jumps"] == len(ev)


def test_week_open_exclusion():
    b = synthetic_bars("2024-01-01", "2024-01-25", vol_pips_per_min=0.05)
    g = slot_grid(b)
    ny = g.index.tz_convert("America/New_York")
    t = g.index[(ny.dayofweek == 6) & (ny.hour == 18) & (ny.minute == 0)][1]
    t_ok = t + pd.Timedelta(minutes=60)
    # drop the first hour of quotes after that Sunday open so the open is 18:00 NY
    bb = b[~((b.index >= t - pd.Timedelta(hours=1)) & (b.index < t))]
    off = pd.Series(0.0, index=bb.index)
    for x in (t + pd.Timedelta(minutes=30), t_ok + pd.Timedelta(hours=3)):
        off[bb.index >= x + pd.Timedelta(minutes=2)] += 15.0
    _, ev = frame_from_bars(_shift(bb, off))
    ex = dict(zip(ev["slot"], ev["excluded"]))
    assert ex[t + pd.Timedelta(minutes=30)] == "week_open"
    assert pd.isna(ex[t_ok + pd.Timedelta(hours=3)])


def test_cluster_bootstrap_resamples_dates():
    x = np.r_[np.full(10, 5.0), np.full(10, -5.0)]
    lo, hi = cluster_bootstrap_ci(x, ["a"] * 10 + ["b"] * 10)
    assert lo == -5.0 and hi == 5.0                       # only two clusters -> all-a or all-b draws possible
    lo2, hi2 = cluster_bootstrap_ci(x, list(range(20)))
    assert -5.0 < lo2 < 0 < hi2 < 5.0


def test_decision_rule():
    base = {"n": 400, "mean_pips": 1.5, "t_p_one_sided": 0.01, "mean_ci95_date_cluster_boot": (0.2, 2.5)}
    assert decide_b48(base) == "SIGNAL"
    assert decide_b48({**base, "n": 299}) == "NONE"
    assert decide_b48({**base, "mean_pips": 0.9}) == "WEAK"
    assert decide_b48({**base, "mean_ci95_date_cluster_boot": (-0.1, 2.5), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b48({**base, "mean_pips": -0.5, "t_p_one_sided": 0.9, "mean_ci95_date_cluster_boot": (-1, 0)}) == "NONE"


def test_injected_reversal_signal_and_no_reversal_none():
    b = synthetic_bars("2024-01-01", "2024-09-30", vol_pips_per_min=0.3)
    starts = _starts(b, every_hours=7)
    rev = _inject(b, starts, 12.0, 4.0)
    _, ev = frame_from_bars(rev)
    tested = ev[ev["tested"]]
    assert len(tested) >= MIN_EVENTS
    r = evaluate(tested)
    assert r["mean_pips"] > 2.5 and decide_b48(r) == "SIGNAL"
    cont = _inject(b, starts, 12.0, -4.0)                 # continuation, not reversal
    _, ev2 = frame_from_bars(cont)
    assert decide_b48(evaluate(ev2[ev2["tested"]])) == "NONE"


def test_random_walk_no_signal():
    hits = 0
    for seed in range(3):
        b = synthetic_bars("2024-01-01", "2024-09-30", vol_pips_per_min=0.3, seed=seed)
        jumps = _inject(b, _starts(b, every_hours=7), 12.0, 0.0, seed=seed)   # pure jumps, no after-effect
        _, ev = frame_from_bars(jumps)
        hits += decide_b48(evaluate(ev[ev["tested"]])) == "SIGNAL"
    assert hits == 0
