# E049 Methodology (pre-registered 2026-11-14 R156, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner), mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every bar whose FX trading date is not `dev` **before** any
  computation; val and OOS untouched. No external download.
- **Prices:** mid closes as exact integers in 2 x mid x 1e5 units (close = bid_close + ask_close; as E018/E045/E047/E048).
- **Bars (details fixed now, before data):** for m in {60, 30, 15, 5} (10 descriptive), UTC-aligned buckets [start, start + m) of the
  1-minute bars; a bar exists when its bucket holds >= 1 minute bar (no minimum-minutes filter; empty buckets do not exist);
  close = last minute's close; complete at end = start + m.
- **EMA20:** per timeframe, `ewm(span=20, adjust=False, min_periods=20)` over that timeframe's existing bars in time order (NaN for
  the first 19 bars; weekend gaps are not filled).
- **Trend state at time T:** for each of 1h, 30m, 15m the last completed bar is the bucket ending exactly at floor(T, m); if it does
  not exist the state is NONE (counted `htf_missing`). Bull if close > EMA20, bear if close < EMA20 (equal / undefined -> neither).
  State BULL if all three bull, BEAR if all three bear, else NONE.
- **Trigger:** 5m bar j with close time T = start + 5 min, London wall clock >= 07:00 and New York wall clock < 12:00 (as E048).
  Bar j-1 must be the immediately preceding 5m bucket (else no cross). Up-cross: close(j-1) <= EMA(j-1) and close(j) > EMA(j);
  down-cross: close(j-1) >= EMA(j-1) and close(j) < EMA(j). Long if up-cross and state BULL at T; short if down-cross and state BEAR
  at T. No per-day cap. Signal stamped T - 1 min so that entry = open of the first 1-minute bar at or after T (SPEC 4 bar-close rule).
- **Trade (`round_numbers.build_trades`, unchanged E018/E045/E047/E048 code, horizon 60):** exit = open of the first bar at or after
  entry + 60 min (<= + 5 min); >= 55/60 bars in the window. Skips counted under the first failing check in E018 order: entry bar
  missing (`coverage`), entry NY time in [16:30, 18:30) (`roll`), exit missing / coverage (`coverage`), exit in roll (`roll`), entry
  spread > 2.0 pips (`spread`, SPEC 4), entry before the previous trade's exit (`overlap`; signals during an open trade are skipped;
  longs and shorts share one book). Signed = direction x (mid open exit - mid open entry), pips. Cluster = FX trading date
  (`sessions.trading_date(T - 1 min)`, 17:00 NY roll).
- **Statistic (1 trial):** `post_jump.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), cluster bootstrap 95% CI
  of the mean resampling **FX trading dates** with all their trades (2000 draws, seed 0).
- **Decision rule (`mtf_alignment.decide_b59` = E045/E047/E048 thresholds, unchanged from the backlog draft):**
  - < 300 trades -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** control = every in-window 5m EMA20 cross with no alignment filter
  (direction = cross direction; does alignment add anything?); 10-minute trigger with the same alignment; long and short legs; 30- and
  120-minute holds; by year; share and mean of trades with the signal close within +-15 min of 08:30 NY, 10:00 NY and 16:00 London,
  and outside them; net at bid/ask, SPEC 4 and costs x1.5.
- **What follows:** SIGNAL -> B59v val confirmation (own pre-registration, rule unchanged, 1 val trial, < 120 trades NONE). Not a
  LEAD until B59v passes and net > 0 at SPEC 4 and costs x1.5 (AUTONOMOUS_PROTOCOL). WEAK or NONE -> B59 closed, B59v closed
  unearned; no stop/target or filter variants are run from descriptive cells (lesson R076).
- **Command (research-batch):** `python scripts/run_e049_mtf_alignment.py | tee backtests/validation_reports/E049_results.txt`
- **Outputs:** `backtests/validation_reports/E049_results.{json,txt}`, `E049_trades.csv`.
- **Tests:** `tests/test_mtf_alignment.py` (bars and EMA seeding, long signal on a dip in an uptrend with stamp and fill, short mirror,
  counter-state cross rejected but kept by the control, London/NY window both ends, state uses the last completed bucket only (data at
  or after T altered), missing higher-timeframe bucket, contiguity of the previous 5m bucket, 10m stamp, no look-ahead by truncation,
  decision rule, no SIGNAL on random walks). Synthetic smoke: NONE (145 trades).
