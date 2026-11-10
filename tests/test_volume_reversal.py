"""Tests for E033 (B28 low-volume next-day reversal, B29 high-volume continuation), written before any run (R069)."""
from datetime import date, timedelta

import numpy as np
import pandas as pd

from fxresearch import volume_reversal as vr
from fxresearch.data import PIP, synthetic_bars


def test_constants_fixed():
    assert vr.MIN_BARS == 1300 and vr.UV_WINDOW == 21 and vr.BAND_WINDOW == 60
    assert vr.LOW_PCTL == 33 and vr.HIGH_PCTL == 67
    assert vr.ALPHA == 0.025 and vr.MIN_EVENTS == 150 and vr.BOOT_BLOCK == 10
    assert vr.OPEN_HM == (17, 0) and vr.CLOSE_HM == (16, 55) and vr.ENTRY_HM == (20, 0) and vr.EXIT_HM == (16, 55)
    assert vr.MAX_ENTRY_SPREAD_PIPS == 2.0


def test_volume_gate():
    b = synthetic_bars("2024-01-01", "2024-01-10")
    assert vr.volume_gate(b)["ok"]
    assert not vr.volume_gate(b.drop(columns=["volume"]))["ok"]
    b2 = b.copy()
    b2.iloc[: int(0.02 * len(b2)), b2.columns.get_loc("volume")] = 0
    g = vr.volume_gate(b2)
    assert not g["ok"] and g["zero_or_nan_share"] > 0.01
    b3 = b.copy()
    b3.iloc[: int(0.005 * len(b3)), b3.columns.get_loc("volume")] = np.nan
    assert vr.volume_gate(b3)["ok"]


def _weekdays(n, start=date(2016, 1, 4)):
    out, d = [], start
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d += timedelta(days=1)
    return out


def _day(dates, vols, nbars=1440):
    return pd.DataFrame({"date": dates, "n_bars": nbars, "volume": vols, "range_pips": 50.0})


def test_uv_past_only_and_burn_in():
    dates = _weekdays(120)
    vols = np.arange(1, 121, dtype=float)
    d = vr.add_uv(_day(dates, vols))
    assert d["uv"].iloc[:21].isna().all()
    assert np.isclose(d["uv"].iloc[21], 22 / np.mean(np.arange(1, 22)) - 1)
    # bands need 60 prior UV values: first band at index 21 + 60
    assert d["uv_p33"].iloc[:81].isna().all() and d["uv_p33"].notna().iloc[81]
    # changing a future volume never changes earlier UV / bands / flags
    vols2 = vols.copy()
    vols2[100] = 1e9
    d2 = vr.add_uv(_day(dates, vols2))
    cols = ["uv", "uv_p33", "uv_p67", "is_low", "is_high"]
    pd.testing.assert_frame_equal(d[cols].iloc[:100], d2[cols].iloc[:100])


def test_invalid_dates_skipped_in_history():
    dates = _weekdays(30)
    vols = np.ones(30)
    nb = np.full(30, 1440)
    nb[5] = 1299
    vols[5] = 1000.0          # invalid date: must not enter the 21-day mean
    d = vr.add_uv(pd.DataFrame({"date": dates, "n_bars": nb, "volume": vols, "range_pips": 1.0}))
    assert not d["valid"].iloc[5] and np.isnan(d["uv"].iloc[5])
    assert np.isclose(d["uv"].iloc[22], 0.0)   # 22nd valid date (index 22) has a clean all-ones history


def _quotes(mapping):
    idx = pd.Index(list(mapping), name="d")
    return pd.DataFrame({"bid_open": [v - 0.00001 for v in mapping.values()],
                         "ask_open": [v + 0.00001 for v in mapping.values()]}, index=idx)


def test_trade_sign_exclusions_and_returns():
    dates = _weekdays(100)
    rng = np.random.default_rng(1)
    vols = rng.uniform(50, 150, 100)
    day = _day(dates, vols)
    q_open = _quotes({d: 1.1000 for d in dates})
    q_close = _quotes({d: (1.1010 if i % 2 else 1.0990) for i, d in enumerate(dates)})
    q_entry = _quotes({d: 1.2000 for d in dates})
    q_exit = _quotes({d + timedelta(days=1): 1.2005 for d in dates})
    df = vr.build_days(day, q_open, q_close, q_entry, q_exit)
    nf = df[df["tradable"]]
    up = nf[nf["r_pips"] > 0]
    dn = nf[nf["r_pips"] < 0]
    assert np.allclose(up["reversal_pips"], -5.0) and np.allclose(up["continuation_pips"], 5.0)
    assert np.allclose(dn["reversal_pips"], 5.0) and np.allclose(dn["continuation_pips"], -5.0)
    fri = df[[d.weekday() == 4 for d in df["date"]]]
    assert (fri["excluded"] == "friday_excluded").all()
    # spread just over / just under the cap
    q_entry2 = q_entry.copy()
    q_entry2.loc[dates[1], "ask_open"] = q_entry2.loc[dates[1], "bid_open"] + 2.01 * PIP
    q_entry2.loc[dates[3], "ask_open"] = q_entry2.loc[dates[3], "bid_open"] + 1.99 * PIP
    df2 = vr.build_days(day, q_open, q_close, q_entry2, q_exit)
    assert df2.loc[1, "excluded"] == "entry_skipped_spread" and pd.isna(df2.loc[3, "excluded"])
    # missing exit / zero move / missing signal quote
    q_close3 = q_close.copy()
    q_close3.loc[dates[1], ["bid_open", "ask_open"]] = [1.09999, 1.10001]
    df3 = vr.build_days(day, q_open, q_close3, q_entry, q_exit.drop(index=dates[3] + timedelta(days=1)))
    assert df3.loc[1, "excluded"] == "zero_move" and df3.loc[3, "excluded"] == "missing_exit"
    df4 = vr.build_days(day, q_open.drop(index=dates[2]), q_close, q_entry, q_exit)
    assert df4.loc[2, "excluded"] == "missing_signal_quote"


def test_decision_rule():
    base = {"n": 300, "mean_pips": 2.0, "t_p_one_sided": 0.01, "mean_ci95_block_boot": (0.5, 3.5)}
    assert vr.decide_b28(base) == "SIGNAL"
    assert vr.decide_b28({**base, "t_p_one_sided": 0.03}) == "WEAK"          # 0.03 >= 0.025, CI lower > 0
    assert vr.decide_b28({**base, "t_p_one_sided": 0.03, "mean_ci95_block_boot": (-0.1, 3)}) == "NONE"
    assert vr.decide_b28({**base, "mean_pips": 0.9}) == "WEAK"
    assert vr.decide_b28({**base, "n": 149}) == "NONE"
    assert vr.decide_b28({"n": 5, "note": "insufficient sample"}) == "NONE"
    assert vr.decide_b29 is vr.decide_b28


def test_null_calibration_fat_tails():
    rng = np.random.default_rng(0)
    sig = sum(vr.decide_b28(vr.evaluate_b28(rng.standard_t(4, 380) * 30)) == "SIGNAL" for _ in range(200))
    assert sig <= 10


def test_random_walk_never_signal():
    """Random daily volumes and random-walk prices: neither trial may return SIGNAL."""
    for seed in range(3):
        rng = np.random.default_rng(seed)
        dates = _weekdays(1500)
        day = _day(dates, rng.lognormal(0, 0.3, len(dates)))
        steps = rng.normal(0, 40 * PIP, 3 * len(dates))
        px = 1.1 + np.cumsum(steps)
        q_open = _quotes({d: px[3 * i] for i, d in enumerate(dates)})
        q_close = _quotes({d: px[3 * i + 1] for i, d in enumerate(dates)})
        q_entry = _quotes({d: px[3 * i + 1] for i, d in enumerate(dates)})
        q_exit = _quotes({d + timedelta(days=1): px[3 * i + 2] for i, d in enumerate(dates)})
        df = vr.build_days(day, q_open, q_close, q_entry, q_exit)
        r28 = vr.evaluate_b28(df.loc[df["tested_low"], "reversal_pips"])
        r29 = vr.evaluate_b28(df.loc[df["tested_high"], "continuation_pips"])
        assert r28["n"] >= 150 and r29["n"] >= 150
        assert vr.decide_b28(r28) != "SIGNAL" and vr.decide_b29(r29) != "SIGNAL"


def test_pipeline_on_synthetic_bars_no_lookahead():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    df = vr.frame_from_bars(bars)
    assert len(df) > 50 and df["valid"].sum() > 40
    # entry at 20:00 NY on calendar D is after D's last bar; truncating bars after 16:59 NY on D cannot change D's flags
    d = df["date"].iloc[40]
    cut = pd.Timestamp(d.isoformat() + " 17:00", tz="America/New_York").tz_convert("UTC")
    df_cut = vr.frame_from_bars(bars[bars.index < cut])
    row_full = df[df["date"] == d].iloc[0]
    row_cut = df_cut[df_cut["date"] == d].iloc[0]
    for c in ("volume", "uv", "r_pips", "n_bars"):
        a, b = row_full[c], row_cut[c]
        assert (np.isnan(a) and np.isnan(b)) or np.isclose(a, b)
