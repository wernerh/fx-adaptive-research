from datetime import date

import numpy as np
import pandas as pd

from fxresearch.data import PIP, synthetic_bars
from fxresearch.vol_state_fix import build_days, evaluate, tradable_events
from fxresearch.vol_state_london import (
    ENTRY_HM, EXIT_HM, SIDE, decide_b20, flag_fomc, fomc_statement_dates, frame_from_bars,
)
from test_vol_state_fix import _synthetic


def test_constants_fixed():
    assert ENTRY_HM == (11, 5) and EXIT_HM == (16, 0) and SIDE == 1


def test_long_sign_and_e022_default_unchanged():
    ranges = [float(i % 10 + 50) for i in range(60)] + [200.0, 10.0]
    rng, e, x = _synthetic(ranges, [0.0] * 61 + [12.0])
    assert abs(build_days(rng, e, x, side=1)["signed_pips"].iloc[60] - 12.0) < 1e-6
    assert abs(build_days(rng, e, x)["signed_pips"].iloc[60] + 12.0) < 1e-6   # E022 default stays short


def test_quotes_from_bars_use_b20_window():
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    rng, df = frame_from_bars(bars)
    d = date(2024, 3, 5)
    row = df[df["date"] == d].iloc[0]
    te = pd.Timestamp("2024-03-05 11:05", tz="America/New_York").tz_convert("UTC")
    tx = pd.Timestamp("2024-03-05 16:00", tz="America/New_York").tz_convert("UTC")
    em = (bars.loc[te, "bid_open"] + bars.loc[te, "ask_open"]) / 2
    xm = (bars.loc[tx, "bid_open"] + bars.loc[tx, "ask_open"]) / 2
    assert abs(row["entry_mid"] - em) < 1e-12 and abs(row["exit_mid"] - xm) < 1e-12
    assert abs(row["signed_pips"] - (xm - em) / PIP) < 1e-6
    assert row["prev"] == date(2024, 3, 4)


def test_no_look_ahead_state():
    r = np.random.default_rng(5)
    ranges = list(r.uniform(30, 120, 200))
    rets = list(r.normal(0, 25, 200))
    a = build_days(*_synthetic(ranges, rets), side=1)
    b = build_days(*_synthetic(ranges[:120] + [v * 10 for v in ranges[120:]], rets[:120] + [v + 500 for v in rets[120:]]),
                   side=1)
    assert list(a["state"].iloc[:119]) == list(b["state"].iloc[:119])


def test_random_walk_no_signal():
    sig = 0
    for seed in range(40):
        r = np.random.default_rng(100 + seed)
        n = 1500
        df = build_days(*_synthetic(list(r.uniform(30, 120, n)), list(r.normal(0, 25, n))), side=1)
        sig += decide_b20(evaluate(tradable_events(df)["signed_pips"])) == "SIGNAL"
    assert sig / 40 <= 0.10


def test_strong_long_effect_gives_signal():
    r = np.random.default_rng(2)
    n = 1500
    ranges = r.uniform(30, 120, n)
    hi_prev = np.concatenate([[False], ranges[:-1] > 90])
    rets = np.where(hi_prev, 6.0, 0.0) + r.normal(0, 20, n)
    df = build_days(*_synthetic(list(ranges), list(rets)), side=1)
    assert decide_b20(evaluate(tradable_events(df)["signed_pips"])) == "SIGNAL"


def test_fomc_flag(tmp_path):
    p = tmp_path / "f.csv"
    p.write_text("year,meeting_start,statement_date,scheduled,cancelled,source_label,source_url\n"
                 "2015,2015-01-27,2015-01-28,True,False,a,u\n2020,2020-03-17,2020-03-18,True,True,b,u\n")
    ds = fomc_statement_dates(p)
    assert ds == {date(2015, 1, 28)}
    df = flag_fomc(pd.DataFrame({"date": [date(2015, 1, 28), date(2015, 1, 29)]}), ds)
    assert list(df["fomc_day"]) == [True, False]


def test_e025_val_restriction_feeds_b20_frame_with_val_dates_only():
    """E025 (B20v): after restrict_to_block(val) the B20 frame contains only val trading dates, the first WINDOW valid val dates
    are burn-in (no earlier-block history), and no bar at/after the cut-off is used."""
    from fxresearch.splits import SplitPlan
    from fxresearch.vol_state_fix import WINDOW, restrict_to_block
    bars = synthetic_bars("2023-10-01", "2024-08-31")
    plan = SplitPlan(date(2023, 12, 31), date(2024, 6, 30), embargo_days=0)
    cut = pd.Timestamp("2024-07-01", tz="UTC")
    vb = restrict_to_block(bars, plan, "val", before_utc=cut)
    assert vb.index.max() < cut
    rng, df = frame_from_bars(vb)
    assert len(df) > WINDOW
    assert min(df["date"]) > date(2023, 12, 31) and max(df["date"]) <= date(2024, 6, 30)
    first_states = df["state"].iloc[:WINDOW].tolist()
    assert "high" not in first_states and "normal" not in first_states
