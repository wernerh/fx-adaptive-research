# E048 Methodology (pre-registered 2026-11-13 R154, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner), mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every bar whose FX trading date is not `dev` **before** any
  computation; val and OOS untouched. No external download.
- **Prices:** exact integers in 2 x mid x 1e5 units (as E018/E045/E047): high = bid_high + ask_high, low = bid_low + ask_low,
  close = bid_close + ask_close. 1 pip = 20 units.
- **1-hour bars:** UTC clock hours [H, H+60); valid with >= 50 one-minute bars; close = last minute's close, high/low = max/min.
- **Level (bar k, close time t_c = H + 60 min):** R = max high, S = min low over the **valid** bars among the 24 clock hours
  k-24..k-1; requires >= 20 valid bars there and bar k valid (else counted `breakouts_lookback_short`; this excludes Monday
  mornings after the weekend gap). Detail fixed now, before data: "24 bars" = 24 clock hours (the backlog's "needs >= 20 valid").
- **Breakout:** close(k) > R -> long setup at L = R; close(k) < S -> short setup at L = S (strict). Only t_c with London wall clock
  >= 07:00 and New York wall clock < 12:00. Only the **first** long and the **first** short setup per FX trading date (17:00 NY roll,
  date of t_c - 1 min); later breakouts that date are ignored even if the first setup was cancelled.
- **Retest (5-minute bars, UTC-aligned, built from the 1-minute bars with open time in [t_c, t_c + 120 min)):** long - the first 5m
  bar with low <= L + 1.0 pip AND close > L is the retest; if a 5m bar with close <= L comes first, the setup is cancelled
  (`failed_break`); none within 120 min -> `no_retest`. A bar meeting the low test but closing <= L cancels. Short mirror (high >=
  L - 1.0 pip AND close < L; close >= L cancels). Signal = the retest 5m bar's close (bucket start + 5 min), stamped bucket start +
  4 min so that entry = open of the first 1-minute bar at or after bucket start + 5 min (SPEC 4 bar-close rule; <= 5 min delay).
- **Trade (`round_numbers.build_trades`, unchanged E018/E045/E047 code, horizon 60):** exit = open of the first bar at or after entry
  + 60 min (<= + 5 min); >= 55/60 bars in the window. Skips counted under the first failing check in E018 order: entry bar missing
  (`coverage`), entry NY time in [16:30, 18:30) (`roll`), exit missing / coverage (`coverage`), exit in roll (`roll`), entry spread
  > 2.0 pips (`spread`, SPEC 4), entry before the previous trade's exit (`overlap`; longs and shorts share one book). Signed =
  direction x (mid open exit - mid open entry), pips.
- **Statistic (1 trial):** `post_jump.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), cluster bootstrap 95%
  CI of the mean resampling **FX trading dates** with all their trades (2000 draws, seed 0).
- **Decision rule (`breakout_retest.decide_b58` = E045/E047 thresholds, unchanged from the backlog draft):**
  - < 300 trades -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** long and short legs; 30- and 120-minute holds; "enter at the breakout
  1h close" variant (no retest, same exits/exclusions); setups by outcome (retest / failed_break / no_retest) per year; by year;
  share and mean of trades with the retest signal within +-15 min of 08:30 NY, 10:00 NY and 16:00 London, and outside them; net at
  bid/ask, SPEC 4 and costs x1.5.
- **What follows:** SIGNAL -> B58v val confirmation (own pre-registration, rule unchanged, 1 val trial, < 120 trades NONE). Not a
  LEAD until B58v passes and net > 0 at SPEC 4 and costs x1.5 (AUTONOMOUS_PROTOCOL). WEAK or NONE -> B58 closed, B58v closed
  unearned; a stop/target version is not run. B59 (multi-timeframe alignment) is independent and runs next either way.
- **Command (research-batch):** `python scripts/run_e048_breakout_retest.py | tee backtests/validation_reports/E048_results.txt`
- **Outputs:** `backtests/validation_reports/E048_results.{json,txt}`, `E048_trades.csv`.
- **Tests:** `tests/test_breakout_retest.py` (hourly levels, 20-valid-hour floor, London/NY window both ends, long retest with
  signal stamp and fill, 1.5-pip near miss + close-through cancel, no retest, short mirror, first setup per date, breakout-close
  variant stamp, no look-ahead by truncation, decision rule, no SIGNAL on random walks). Synthetic smoke: NONE (14 trades).
