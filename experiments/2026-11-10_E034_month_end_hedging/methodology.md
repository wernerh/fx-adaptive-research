# E034 Methodology (pre-registered 2026-11-10 R072, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline), mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`): EUR/USD bars whose trading date is not `dev` are dropped **before** any computation. Index data: Dukascopy
  CFDs `eusidxeur` (EU Stocks 50, EUR) and `usa500idxusd` (US 500, USD), m1 bid and ask, downloaded on the GitHub runner only
  (`scripts/download_dukascopy_index.sh`, dukascopy-node 1.51.1, 2015-01-01 -> 2021-01-01, into `data/raw_index/`, not committed);
  index bars at or after 2021-01-01 UTC are dropped before any computation. Val and OOS untouched.
- **Month-ends:** D = last trading date of each calendar month among the EUR/USD dev trading dates (17:00 NY roll;
  `fixes.month_end_flag`, E007 definition). D-1 = previous trading date in that set. Anchor A(D) = month-end of the previous calendar
  month in the set; the first dev month-end (Jan 2015) has none -> `no_prev_month_end` (counted; expected n = 71 anchored).
- **Index quote (E011 rule + holiday fallback, fixed before data):** mid of bid/ask OPEN of the first bar in [16:00, 16:05)
  Europe/London on the target London date. If that index has no such quote on the target date (e.g. Eurex closed on 24/31 Dec, Good
  Friday), use the latest London date in [target - 5 days, target] that has one (past only); the end quote must fall on a date
  strictly after the start-quote date. Month-ends using a fallback are flagged `fallback_quote` (descriptive). No quote ->
  `missing_index_quote`.
- **Signal:** S(D) = [ln EU(D-1) - ln EU(A)] - [ln US(D-1) - ln US(A)]. Position = -sign(S). S = 0 -> `zero_signal`.
- **Trades (EUR/USD quote = bid/ask OPEN of the first bar in [T, T+5 min) Europe/London):**
  (a) **HOUR** 15:00 -> 16:00 London on D; (b) **DAY** 16:00 London on D-1 -> 16:00 London on D.
  Signed return = position x (mid exit - mid entry) / pip.
- **Exclusions per window, counted, first reason in this order:** `no_prev_month_end`, `missing_index_quote`, `zero_signal`,
  `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at entry > 2.0 pips, SPEC 4).
- **Data gate (first, fixed now):** if either index series is empty, or `missing_index_quote` occurs on > 5% of anchored dev
  month-ends, the experiment stops as **BLOCKED** with 0 trials; no trade result is computed. The index download step in batch.sh is
  allowed to fail without failing the job so that the gate records BLOCKED.
- **Statistic (2 trials):** `month_end_hedging.evaluate_b30`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), i.i.d.
  bootstrap 95% CI of the mean (block 1, 2000 draws, seed 0; month-ends are a month apart).
- **Decision rule (`month_end_hedging.decide_b30`, unchanged from the backlog draft), per window:**
  - < 50 tested events -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.025 (Bonferroni for 2 trials).
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.025), but not SIGNAL.
  - **NONE** otherwise.
- **No look-ahead:** S uses index quotes at or before 16:00 London on D-1 (bar opens); both trades enter at or after that instant
  (the DAY entry is the open of the same 16:00 London minute: the signal and entry are simultaneous bar opens, stated as a
  limitation). Tested: changing index bars after 16:05 London on D-1 and EUR/USD bars after 16:05 London on D leaves S and both
  results unchanged.
- **Null calibration (code tests, written before data):** i.i.d. t(4) samples of 71: SIGNAL rate <= 5% over 200 draws; random-walk
  EUR/USD with deterministic index paths gives NONE; direction test (EU outperformance -> short, US -> long).
- **Descriptive (not trials, do not change any decision):** unconditional long EUR/USD in each window; |S| above vs at/below median;
  EU-only leg (-sign(EU return)) and US-only leg (+sign(US return)); quarter-ends vs other months; excluding fallback-quote months;
  share of short positions; corr(S, move); by year; post-fix hour 16:00 -> 17:00 London on D under the same position (reversal
  check); S summary; entry/exit spreads; net at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5.
- **What follows:**
  - SIGNAL in a window -> that window earns B31 (val confirmation, its own pre-registered experiment). Not a LEAD yet.
  - WEAK or NONE in both -> B30 closed, B31 closed unearned; no re-test with other windows, indices or lookbacks.
  - BLOCKED -> 0 trials; B30 `blocked` (index data unusable); one diagnosis/re-fetch allowed if the failure is a download error.
- **Code:** `src/fxresearch/month_end_hedging.py`; `scripts/run_e034_month_end_hedging.py`; `scripts/download_dukascopy_index.sh`;
  tests `tests/test_month_end_hedging.py`. Synthetic smoke run passed (random-walk index bars, 2 anchored month-ends -> NONE/NONE,
  gate ok).
- **Command (batch.sh):** `bash scripts/download_dukascopy_index.sh` then
  `python scripts/run_e034_month_end_hedging.py | tee backtests/validation_reports/E034_results.txt` (also writes
  `E034_results.json` and `E034_month_ends.csv`).
