"""E043 (backlog B48): post-jump reversal after 5-minute Lee-Mykland jumps, 60-minute fade, dev only.

Definitions (fixed in the backlog, R096, and pre-registered 2026-11-11 R097, before any run):
* Grid: 5-minute slots on the NY clock (UTC floor to 5 min == NY floor, offsets are whole hours) over trading time, i.e. every
  slot that is not in the weekend closure (`sessions.is_weekend_bar`, Fri 17:00 -> Sun 17:00 NY). Holidays stay on the grid
  (missing quotes).
* Quote at slot T = bid/ask OPEN of the first 1-minute bar in [T, T+5 min). Missing -> NaN, never filled.
* r_t = ln mid(t+5) - ln mid(t) (t+5 in clock time; a weekend slot or missing quote -> r_t missing).
* sigma_t^2 = mean over j = t-K+2 .. t-1 of |r_j| |r_{j-1}| with both valid (= (1/(K-2)) sum when all valid); the previous K-1 = 269
  grid returns must be >= 90% valid, else no test. r_t itself is excluded (past only).
* Jump: |r_t / sigma_t| > THRESHOLD (Lee-Mykland 2008, n = 288, alpha = 0.01 -> 5.395) AND |mid(t+5) - mid(t)| >= 5 pips.
* Exclusions, first reason in this order: `roll_hour` (slot NY time in [16:55, 17:55)), `week_open` (slot < first valid quote after
  the weekend gap + 60 min), `inside_hold` (slot before the exit time of the previous TESTED event; only tested events block),
  `missing_entry`, `missing_exit`, `entry_skipped_spread` (> 2.0 pips, SPEC 4).
* Trade: s = -sign(r_t); entry at the quote of slot t+10 min, exit at slot t+70 min. Signed = s x (mid exit - mid entry) / pip.
* Statistic: one-sided t-test; date-cluster bootstrap CI of the mean (resample trading dates of the jump slot with all their
  events, 2000 draws, seed 0). Decision: < 300 events NONE; SIGNAL mean > 1.0 AND CI lower > 0 AND p < 0.05; WEAK mean > 0 and
  (CI lower > 0 or p < 0.05); NONE otherwise.
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .sessions import NY, is_weekend_bar, trading_date
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS

SLOT = pd.Timedelta(minutes=5)
K = 270
N_PER_DAY = 288
ALPHA_JUMP = 0.01
MIN_VALID_SHARE = 0.90
MIN_ABS_MOVE = 0.0005            # 5 pips, price terms
ENTRY_DELAY = pd.Timedelta(minutes=10)
EXIT_DELAY = pd.Timedelta(minutes=70)
ROLL_START_MIN = 16 * 60 + 55    # [16:55, 17:55) NY
ROLL_END_MIN = 17 * 60 + 55
WEEK_OPEN_SKIP = pd.Timedelta(minutes=60)
SIGN = -1.0                      # fade
MIN_EVENTS = 300
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_N = 2000
BOOT_SEED = 0
EXCLUSION_ORDER = ("roll_hour", "week_open", "inside_hold", "missing_entry", "missing_exit", "entry_skipped_spread")


def lm_threshold(n: int = N_PER_DAY, alpha: float = ALPHA_JUMP) -> float:
    c = math.sqrt(2 / math.pi)
    a = math.sqrt(2 * math.log(n))
    cn = a / c - (math.log(math.pi) + math.log(math.log(n))) / (2 * c * a)
    sn = 1 / (c * a)
    beta = -math.log(-math.log(1 - alpha))
    return cn + sn * beta


THRESHOLD = lm_threshold()


def slot_grid(bars: pd.DataFrame) -> pd.DataFrame:
    """Trading-time 5-minute grid with the slot quote (first 1-minute bar open in [T, T+5)); NaN where no bar."""
    slots = bars.index.floor("5min")
    q = bars[["bid_open", "ask_open"]].groupby(slots).first()
    full = pd.date_range(slots.min(), slots.max(), freq="5min", tz="UTC")
    full = full[~is_weekend_bar(full).to_numpy()]
    g = q.reindex(full)
    g.index.name = "slot"
    g["mid"] = (g["bid_open"] + g["ask_open"]) / 2
    return g


def jump_stats(grid: pd.DataFrame, k: int = K) -> pd.DataFrame:
    """Adds r (log return slot -> slot+5), price move, sigma (bipower, past only), L and the jump flag."""
    g = grid.copy()
    idx = g.index
    mid = g["mid"].to_numpy()
    nxt = np.r_[mid[1:], np.nan]
    contiguous = np.r_[(idx[1:] - idx[:-1]) == SLOT, False]
    nxt = np.where(contiguous, nxt, np.nan)
    r = np.log(nxt) - np.log(mid)
    move = nxt - mid
    v = ~np.isnan(r)
    a = np.where(v, np.abs(r), 0.0)
    pv = np.r_[False, v[1:] & v[:-1]]
    prod = np.r_[0.0, a[1:] * a[:-1]]
    prod = np.where(pv, prod, 0.0)
    cv = np.r_[0, np.cumsum(v)]
    cp = np.r_[0.0, np.cumsum(prod)]
    cpv = np.r_[0, np.cumsum(pv)]
    n = len(r)
    i = np.arange(n)
    ok = i >= k - 1                           # need r_{i-k+1} .. r_{i-1}
    lo_r = np.clip(i - (k - 1), 0, None)      # returns window [i-k+1, i-1]
    valid_ret = cv[i] - cv[lo_r]
    lo_p = np.clip(i - (k - 2), 0, None)      # products j in [i-k+2, i-1]
    s_prod = cp[i] - cp[lo_p]
    n_prod = cpv[i] - cpv[lo_p]
    ok &= valid_ret >= MIN_VALID_SHARE * (k - 1)
    ok &= n_prod > 0
    with np.errstate(invalid="ignore", divide="ignore"):
        sigma = np.where(ok, np.sqrt(s_prod / np.where(n_prod > 0, n_prod, 1)), np.nan)
        sigma = np.where(sigma > 0, sigma, np.nan)
        L = r / sigma
    g["r"] = r
    g["move"] = move
    g["sigma"] = sigma
    g["L"] = L
    g["tested_slot"] = ~np.isnan(L)
    g["jump"] = (np.abs(np.nan_to_num(L)) > THRESHOLD) & (np.abs(np.nan_to_num(move)) >= MIN_ABS_MOVE - 1e-12)
    return g


def _week_open(grid: pd.DataFrame) -> pd.Series:
    """Per slot: time of the first valid quote after the latest weekend gap (NaT if none yet)."""
    idx = grid.index
    gap = np.r_[True, (idx[1:] - idx[:-1]) > SLOT]
    week = np.cumsum(gap)
    ts = pd.Series(idx, index=idx).where(grid["mid"].notna())
    return ts.groupby(week).transform("min")


def build_events(g: pd.DataFrame) -> pd.DataFrame:
    """One row per jump (in time order) with exclusion reason and trade outcome."""
    jumps = g[g["jump"]]
    if jumps.empty:
        return pd.DataFrame(columns=["slot", "excluded", "tested"])
    wopen = _week_open(g)
    quotes = g[["bid_open", "ask_open", "mid"]]
    rows, last_exit = [], None
    for t, row in jumps.iterrows():
        ny = t.tz_convert(NY)
        mins = ny.hour * 60 + ny.minute
        e_t, x_t, k_t = t + ENTRY_DELAY, t + EXIT_DELAY, t + SLOT
        e = quotes.loc[e_t] if e_t in quotes.index else None
        x = quotes.loc[x_t] if x_t in quotes.index else None
        sk = quotes.loc[k_t, "mid"] if k_t in quotes.index else np.nan
        e_mid = float(e["mid"]) if e is not None else np.nan
        x_mid = float(x["mid"]) if x is not None else np.nan
        e_spr = float(e["ask_open"] - e["bid_open"]) / PIP if e is not None else np.nan
        x_spr = float(x["ask_open"] - x["bid_open"]) / PIP if x is not None else np.nan
        wo = wopen.loc[t]
        if ROLL_START_MIN <= mins < ROLL_END_MIN:
            ex = "roll_hour"
        elif pd.isna(wo) or t < wo + WEEK_OPEN_SKIP:
            ex = "week_open"
        elif last_exit is not None and t < last_exit:
            ex = "inside_hold"
        elif np.isnan(e_mid):
            ex = "missing_entry"
        elif np.isnan(x_mid):
            ex = "missing_exit"
        elif e_spr > MAX_ENTRY_SPREAD_PIPS:
            ex = "entry_skipped_spread"
        else:
            ex = None
            last_exit = x_t
        side = SIGN * np.sign(row["r"])
        rows.append({"slot": t, "ny_time": ny.strftime("%H:%M"), "ny_minutes": mins, "trading_date": trading_date(t),
                     "r": row["r"], "move_pips": row["move"] / PIP, "L": row["L"], "side": side,
                     "entry_mid": e_mid, "exit_mid": x_mid, "skip_mid": float(sk),
                     "entry_spread_pips": e_spr, "exit_spread_pips": x_spr, "excluded": ex})
    df = pd.DataFrame(rows)
    df["tested"] = df["excluded"].isna()
    df["signed_pips"] = df["side"] * (df["exit_mid"] - df["entry_mid"]) / PIP
    df["skipped_bar_signed_pips"] = df["side"] * (df["entry_mid"] - df["skip_mid"]) / PIP
    df["net_bidask_pips"] = df["signed_pips"] - (df["entry_spread_pips"] + df["exit_spread_pips"]) / 2
    df["net_spec4_pips"] = df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    df["net_x1_5_pips"] = df["signed_pips"] - 1.5 * (df["signed_pips"] - df["net_spec4_pips"])
    return df


def frame_from_bars(bars: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    g = jump_stats(slot_grid(bars))
    return g, build_events(g)


def cluster_bootstrap_ci(x, clusters, n_boot: int = BOOT_N, seed: int = BOOT_SEED, alpha: float = 0.05):
    """Percentile CI of the mean, resampling clusters (trading dates) with replacement, all their events kept."""
    s = pd.DataFrame({"x": np.asarray(x, float), "c": list(clusters)}).dropna()
    agg = s.groupby("c")["x"].agg(["sum", "size"])
    m = len(agg)
    if m < 2:
        return (float("nan"), float("nan"))
    sums, cnts = agg["sum"].to_numpy(), agg["size"].to_numpy()
    rng = np.random.default_rng(seed)
    means = np.empty(n_boot)
    for b in range(n_boot):
        ix = rng.integers(0, m, size=m)
        means[b] = sums[ix].sum() / cnts[ix].sum()
    return (float(np.quantile(means, alpha / 2)), float(np.quantile(means, 1 - alpha / 2)))


def evaluate(ev: pd.DataFrame, col: str = "signed_pips") -> dict:
    s = ev[[col, "trading_date"]].dropna()
    x = s[col].to_numpy(float)
    n = len(x)
    if n < 3:
        return {"n": n, "note": "insufficient sample"}
    t = stats.ttest_1samp(x, 0.0, alternative="greater")
    lo, hi = cluster_bootstrap_ci(x, s["trading_date"])
    return {"n": n, "n_dates": int(s["trading_date"].nunique()),
            "mean_pips": round(float(x.mean()), 3), "median_pips": round(float(np.median(x)), 3),
            "sd_pips": round(float(x.std(ddof=1)), 3), "hit_rate": round(float((x > 0).mean()), 4),
            "t_stat": round(float(t.statistic), 3), "t_p_one_sided": round(float(t.pvalue), 4),
            "mean_ci95_date_cluster_boot": (round(lo, 3), round(hi, 3))}


def decide_b48(res: dict) -> str:
    if res.get("n", 0) < MIN_EVENTS or "mean_pips" not in res:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_date_cluster_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


def counts(g: pd.DataFrame, ev: pd.DataFrame) -> dict:
    vc = ev["excluded"].value_counts() if len(ev) else pd.Series(dtype=int)
    out = {"grid_slots": int(len(g)), "slots_with_quote": int(g["mid"].notna().sum()),
           "valid_returns": int(g["r"].notna().sum()), "tested_slots": int(g["tested_slot"].sum()),
           "jumps": int(len(ev))}
    for k in EXCLUSION_ORDER:
        out[k] = int(vc.get(k, 0))
    out["events_tested"] = int(ev["tested"].sum()) if len(ev) else 0
    return out


def cost_summary(ev: pd.DataFrame) -> dict:
    if len(ev) == 0:
        return {"n": 0}
    return {"n": int(len(ev)),
            "mean_signed_mid_pips": round(float(ev["signed_pips"].mean()), 3),
            "mean_net_bidask_pips": round(float(ev["net_bidask_pips"].mean()), 3),
            "mean_net_spec4_pips": round(float(ev["net_spec4_pips"].mean()), 3),
            "mean_net_costs_x1_5_pips": round(float(ev["net_x1_5_pips"].mean()), 3),
            "median_spread_entry_pips": round(float(ev["entry_spread_pips"].median()), 3),
            "median_spread_exit_pips": round(float(ev["exit_spread_pips"].median()), 3)}
