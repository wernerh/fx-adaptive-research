"""E015 (B12): BLS archive-index parser, 08:30/08:45/09:45 NY edges, no look-ahead, decision rule, random walk."""
from datetime import date

import numpy as np
import pandas as pd
import pytest

from fxresearch.data import synthetic_bars
from fxresearch.nfp import (
    cost_summary, decide_b12, evaluate, parse_archive_index, reaction_frame, reversal_flag, validate_year,
)

# Synthetic HTML shaped like the BLS archive index. Dates are invented test inputs, not real release dates.
_DATES_2099 = ["01092099", "02062099", "03062099", "04032099", "05082099", "06052099", "07022099", "08072099",
               "09042099", "10022099", "11062099", "12042099"]
INDEX = "<ul>" + "".join(
    f'<li>Employment Situation <a href="/news.release/archives/empsit_{d}.htm">HTML</a> '
    f'<a href="/news.release/archives/empsit_{d}.pdf">PDF</a></li>' for d in _DATES_2099
) + '<li><a href="/news.release/archives/empsit_12052098.htm">HTML</a></li>' \
    '<li><a href="/news.release/archives/empsit_13452099.htm">bad</a></li></ul>'


def test_parse_archive_index_dedup_and_bad_dates():
    rs = parse_archive_index(INDEX)
    ds = [r.release_date for r in rs]
    assert len(ds) == 13  # 12 in 2099 + 1 in 2098; html/pdf pair counted once; month 13 ignored
    assert ds[0] == date(2098, 12, 5) and ds[-1] == date(2099, 12, 4)
    assert rs[1].link == "empsit_01092099.htm"


def test_validate_year():
    rs = parse_archive_index(INDEX)
    ok, note = validate_year(rs, 2099)
    assert ok or "weekend" in note  # invented dates; structure check only
    ok2, note2 = validate_year(rs[:8], 2099)
    assert not ok2 and "releases" in note2
    two_in_june = parse_archive_index(INDEX.replace("05082099", "06302099"))
    ok3, note3 = validate_year(two_in_june, 2099)
    assert not ok3 and "month" in note3


def _mid(row):
    return (row.filter(like="bid").to_numpy() + row.filter(like="ask").to_numpy()) / 2


def test_edges_dst_aware():
    bars = synthetic_bars("2024-03-01", "2024-03-20")
    d = date(2024, 3, 8)   # before US DST (Mar 10): 08:30 NY = 13:30 UTC
    f = reaction_frame(bars, [d])
    b = bars
    p0 = (b.loc[pd.Timestamp("2024-03-08 13:30", tz="UTC"), ["bid_open", "ask_open"]]).mean()
    p1 = (b.loc[pd.Timestamp("2024-03-08 13:44", tz="UTC"), ["bid_close", "ask_close"]]).mean()
    e = (b.loc[pd.Timestamp("2024-03-08 13:45", tz="UTC"), ["bid_open", "ask_open"]]).mean()
    x = (b.loc[pd.Timestamp("2024-03-08 14:44", tz="UTC"), ["bid_close", "ask_close"]]).mean()
    assert abs(f.loc[d, "r1_pips"] - (p1 - p0) / 1e-4) < 1e-9
    assert abs(f.loc[d, "r2_pips"] - (x - e) / 1e-4) < 1e-9
    d2 = date(2024, 3, 15)  # after DST: 08:30 NY = 12:30 UTC
    g = reaction_frame(bars, [d2])
    p0 = (b.loc[pd.Timestamp("2024-03-15 12:30", tz="UTC"), ["bid_open", "ask_open"]]).mean()
    p1 = (b.loc[pd.Timestamp("2024-03-15 12:44", tz="UTC"), ["bid_close", "ask_close"]]).mean()
    assert abs(g.loc[d2, "r1_pips"] - (p1 - p0) / 1e-4) < 1e-9


def test_signed_and_bidask_net():
    bars = synthetic_bars("2024-03-01", "2024-03-20", spread_pips_=0.3)
    f = reaction_frame(bars, [date(2024, 3, 8), date(2024, 3, 15)])
    for d, r in f.iterrows():
        if abs(r["r1_pips"]) < 1.0:
            assert r["direction"] == 0 and r["signed_pips"] == 0
        else:
            assert r["signed_pips"] == pytest.approx(np.sign(r["r1_pips"]) * r["r2_pips"])
            assert r["signed_pips"] - r["net_bidask_pips"] == pytest.approx(0.3, abs=1e-6)


def test_no_look_ahead_r1_ignores_bars_from_0845():
    bars = synthetic_bars("2024-03-01", "2024-03-20")
    d = date(2024, 3, 8)
    base = reaction_frame(bars, [d])
    shocked = bars.copy()
    after = shocked.index >= pd.Timestamp("2024-03-08 13:45", tz="UTC")
    shocked.loc[after, [c for c in bars.columns if c != "volume"]] += 0.0050  # +50 pips from 08:45 NY on
    s = reaction_frame(shocked, [d])
    assert s.loc[d, "r1_pips"] == pytest.approx(base.loc[d, "r1_pips"])
    assert s.loc[d, "direction"] == base.loc[d, "direction"]


def test_missing_quotes_nan_not_filled():
    bars = synthetic_bars("2024-03-01", "2024-03-20")
    cut = bars[~((bars.index >= pd.Timestamp("2024-03-08 13:40", tz="UTC"))
                 & (bars.index < pd.Timestamp("2024-03-08 13:50", tz="UTC")))]
    f = reaction_frame(cut, [date(2024, 3, 8)])
    assert np.isnan(f.loc[date(2024, 3, 8), "signed_pips"])


def test_no_trade_days_stay_in_n():
    f = pd.DataFrame({"r1_pips": [5, -4, 0.5, 3, -2, 0.2], "r2_pips": [2, 1, 9, -1, -3, -9],
                      "direction": [1, -1, 0, 1, -1, 0], "signed_pips": [2, -1, 0, -1, 3, 0],
                      "net_bidask_pips": [1.8, -1.2, 0, -1.2, 2.8, 0], "entry_spread_pips": [0.2] * 6})
    r = evaluate(f)
    assert r["n"] == 6 and r["n_traded"] == 4 and r["n_no_trade"] == 2
    assert r["mean_signed_pips"] == pytest.approx(0.5)
    assert r["hits"] == 2 and r["hit_rate_traded"] == 0.5
    c = cost_summary(f)
    assert c["n_traded"] == 4 and c["mean_net_spec4_pips"] == pytest.approx((1.8 - 1.2 - 1.2 + 2.8) / 4 - 0.2)


def test_decide_rule():
    base = {"mean_signed_pips": 2.0, "binom_p": 0.01, "mean_signed_ci95_block_boot": (0.5, 3.5)}
    assert decide_b12(base) == "SIGNAL"
    assert decide_b12({**base, "mean_signed_pips": 0.8}) == "WEAK"
    assert decide_b12({**base, "binom_p": 0.2}) == "WEAK"
    assert decide_b12({**base, "mean_signed_ci95_block_boot": (-0.5, 3.5), "binom_p": 0.2}) == "NONE"
    assert decide_b12({**base, "mean_signed_pips": -2.0}) == "NONE"
    assert decide_b12({"n": 1}) == "NONE"
    assert reversal_flag({"mean_signed_pips": -2.0, "mean_signed_ci95_block_boot": (-3.0, -0.5)})
    assert not reversal_flag(base)


@pytest.mark.parametrize("seed", [1, 2, 3])
def test_no_signal_on_random_walk(seed):
    bars = synthetic_bars("2023-01-01", "2024-12-31", seed=seed)
    fridays = [d for d in pd.date_range("2023-01-06", "2024-12-27", freq="7D").date][::4]  # ~ monthly
    f = reaction_frame(bars, fridays)
    assert f["signed_pips"].notna().sum() >= 20
    assert decide_b12(evaluate(f)) != "SIGNAL"
