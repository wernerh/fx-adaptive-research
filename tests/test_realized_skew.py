"""E044 (B50) daily realized skewness tests: formula, window, coverage, trade timing, exclusions, decision, no edge on RW."""
from datetime import date

import numpy as np
import pandas as pd

from fxresearch.data import OHLC, PIP, synthetic_bars
from fxresearch.post_jump import slot_grid
from fxresearch.realized_skew import (
    ALPHA, BOOT_BLOCK, EXCLUSION_ORDER, EXPECTED_RETURNS, MIN_EVENTS, MIN_MEAN_PIPS, MIN_VALID_RETURNS, counts,
    decide_b50, evaluate, frame_from_bars, minute_skew, realized_skew, slot_returns, daily_signal,
)
from fxresearch.sessions import NY


def _shift(bars, off_pips: pd.Series):
    b = bars.copy()
    off = off_pips.reindex(b.index).fillna(0.0).to_numpy() * PIP
    for side in ("bid", "ask"):
        for f in OHLC:
            b[f"{side}_{f}"] = b[f"{side}_{f}"] + off
    return b


def test_constants_preregistered():
    assert EXPECTED_RETURNS == 275 and MIN_VALID_RETURNS == 248
    assert MIN_EVENTS == 500 and MIN_MEAN_PIPS == 1.0 and ALPHA == 0.05 and BOOT_BLOCK == 20
    assert EXCLUSION_ORDER[0] == "invalid_signal" and EXCLUSION_ORDER[-1] == "entry_skipped_spread"


def test_realized_skew_formula():
    r = np.array([0.001, -0.0005, 0.0002, 0.003, -0.001, np.nan])
    x = r[~np.isnan(r)]
    exp = np.sqrt(len(x)) * np.sum(x ** 3) / np.sum(x ** 2) ** 1.5
    assert np.isclose(realized_skew(r), exp)
    assert realized_skew(-r) == -realized_skew(r)
    assert np.isnan(realized_skew(np.zeros(5)))
    # scale invariant
    assert np.isclose(realized_skew(3 * x), realized_skew(x))


def test_window_has_275_returns_per_full_day():
    bars = synthetic_bars("2024-01-08", "2024-01-20")
    g = slot_returns(slot_grid(bars))
    w = g[g["in_window"]]
    per = w.groupby("trading_date")["r"].count()
    # full mid-week trading dates (Tue..Thu) have all 275 returns
    for d in (date(2024, 1, 10), date(2024, 1, 11)):
        assert per.loc[d] == 275
    first = w[w["trading_date"] == date(2024, 1, 10)].index
    assert first[0].tz_convert(NY).strftime("%H:%M") == "18:00"
    assert first[-1].tz_convert(NY).strftime("%H:%M") == "16:50"


def test_coverage_rule_invalidates_sparse_day():
    bars = synthetic_bars("2024-01-08", "2024-01-20")
    ny = bars.index.tz_convert(NY)
    drop = (pd.Index(ny.date) == date(2024, 1, 10)) & (np.asarray(ny.hour) >= 3) & (np.asarray(ny.hour) < 6)
    g = slot_returns(slot_grid(bars[~drop]))
    sig = daily_signal(g).set_index("date")
    assert sig.loc[date(2024, 1, 10), "n_returns"] < MIN_VALID_RETURNS
    assert not sig.loc[date(2024, 1, 10), "valid"]
    assert sig.loc[date(2024, 1, 11), "valid"]


def test_trade_timing_and_sign():
    bars = synthetic_bars("2024-01-08", "2024-01-20")
    _, df = frame_from_bars(bars)
    d = date(2024, 1, 10)
    row = df.set_index("date").loc[d]
    ny = bars.index.tz_convert(NY)
    e = bars[(pd.Index(ny.date) == d) & (np.asarray(ny.hour) == 20) & (np.asarray(ny.minute) == 0)].iloc[0]
    x = bars[(pd.Index(ny.date) == date(2024, 1, 11)) & (np.asarray(ny.hour) == 16) & (np.asarray(ny.minute) == 55)].iloc[0]
    em, xm = (e["bid_open"] + e["ask_open"]) / 2, (x["bid_open"] + x["ask_open"]) / 2
    assert np.isclose(row["entry_mid"], em) and np.isclose(row["exit_mid"], xm)
    assert np.isclose(row["signed_pips"], np.sign(row["rs"]) * (xm - em) / PIP)
    # Friday trading date excluded
    assert df.set_index("date").loc[date(2024, 1, 12), "excluded"] == "friday_excluded"


def test_signal_ignores_future_bars():
    """Changing bars after 16:55 NY on D (entry/hold) must not change RS(D)."""
    bars = synthetic_bars("2024-01-08", "2024-01-20")
    _, a = frame_from_bars(bars)
    ny = bars.index.tz_convert(NY)
    after = pd.Series(0.0, index=bars.index)
    late = (pd.Index(ny.date) == date(2024, 1, 10)) & (np.asarray(ny.hour) * 60 + np.asarray(ny.minute) >= 16 * 60 + 56)
    after[late] = 50.0
    _, b = frame_from_bars(_shift(bars, after))
    assert np.isclose(a.set_index("date").loc[date(2024, 1, 10), "rs"], b.set_index("date").loc[date(2024, 1, 10), "rs"])


def test_spread_exclusion():
    bars = synthetic_bars("2024-01-08", "2024-01-20")
    ny = bars.index.tz_convert(NY)
    sel = (pd.Index(ny.date) == date(2024, 1, 9)) & (np.asarray(ny.hour) == 20) & (np.asarray(ny.minute) < 5)
    b = bars.copy()
    for f in OHLC:
        b.loc[sel, f"ask_{f}"] = b.loc[sel, f"bid_{f}"] + 3 * PIP
    _, df = frame_from_bars(b)
    assert df.set_index("date").loc[date(2024, 1, 9), "excluded"] == "entry_skipped_spread"
    c = counts(df)
    assert c["entry_skipped_spread"] == 1 and c["tested"] == int(df["tested"].sum())


def test_minute_skew_runs():
    bars = synthetic_bars("2024-01-08", "2024-01-20")
    ms = minute_skew(bars)
    assert ms.notna().sum() >= 8


def test_decision_rule():
    base = {"n": 600, "mean_pips": 2.0, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.5, 3.5)}
    assert decide_b50(base) == "SIGNAL"
    assert decide_b50({**base, "n": 499}) == "NONE"
    assert decide_b50({**base, "mean_pips": 0.8}) == "WEAK"
    assert decide_b50({**base, "mean_ci95_block_boot": (-0.1, 3.0), "t_p_one_sided": 0.2}) == "NONE"
    assert decide_b50({**base, "mean_pips": -1.0}) == "NONE"
    assert decide_b50({**base, "t_p_one_sided": 0.06, "mean_ci95_block_boot": (-0.1, 3.0)}) == "NONE"


def test_evaluate_and_no_edge_on_random_walk():
    """Pooled over 4 random-walk years (no edge by construction): no SIGNAL, |mean| small."""
    parts = []
    for seed in (1, 2, 3, 4):
        _, df = frame_from_bars(synthetic_bars("2024-01-01", "2024-12-31", seed=seed))
        ev = df[df["tested"]]
        assert len(ev) > 150
        parts.append(ev["signed_pips"].to_numpy())
    res = evaluate(np.concatenate(parts))
    assert res["n"] >= MIN_EVENTS
    assert abs(res["mean_pips"]) < 1.5
    assert decide_b50(res) != "SIGNAL"
