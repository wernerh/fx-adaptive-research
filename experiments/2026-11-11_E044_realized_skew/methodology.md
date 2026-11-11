# E044 Methodology (pre-registered 2026-11-11 R100, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner), mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any
  computation; val and OOS untouched. No external download.
- **Grid and returns:** `post_jump.slot_grid` (E043 rule): 5-minute NY-clock slots over trading time; quote at slot T = bid/ask open
  of the first 1-minute bar in [T, T+5 min); missing -> NaN, never filled. r_T = ln mid(T+5) - ln mid(T) (contiguous slots, both
  quotes present).
- **Signal window of trading date D** (`sessions.trading_date`, 17:00 NY roll): slots of D whose NY time is not in [16:55, 18:00),
  i.e. T = 18:00 NY .. 16:50 NY -> 275 returns, the last ending at 16:55 NY on D.
- **Validity:** >= 248 (90% of 275) valid returns and sum r^2 > 0; else `invalid_signal`.
- **RS(D) = sqrt(N) x sum r^3 / (sum r^2)^(3/2)**, N = valid returns of D. Position s = sign(RS(D)).
- **Trade:** entry at the 20:00 NY quote on NY calendar date D (first 1-minute bar in [20:00, 20:05), `vol_state_fix.ny_quotes`),
  exit at the 16:55 NY quote on NY calendar date D+1. Signed = s x (mid exit - mid entry) / pip.
- **Exclusions (counted, first reason in this order):** `invalid_signal`; `friday_excluded` (D a Friday, weekend); `zero_signal`
  (RS = 0); `missing_entry`; `missing_exit`; `entry_skipped_spread` (ask - bid at entry > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** `overnight_reversal.evaluate_b32`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block
  bootstrap 95% CI of the mean (blocks of 20 consecutive tested dates, 2000 draws, seed 0).
- **Decision rule (`realized_skew.decide_b50` = `overnight_reversal.decide_b34`, unchanged from the backlog draft = E041 rule):**
  - < 500 tested dates -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** share long; opposite-sign mean (reported only); unconditional long over
  the same hold; corr(RS, R(D)) with R(D) = mid 16:55 NY D - mid 18:00 NY D (slot quotes) and sign agreement; result within R(D) > 0
  and R(D) < 0; RS mean/median/SD; |RS| terciles; RS from 1-minute mid-open returns (same window, robustness) sign agreement and
  signed mean; by year (lesson R092); net at bid/ask, SPEC 4 and costs x1.5; exclusion counts.
- **Implementation choices fixed now, before data:** 248-return floor = ceil(0.9 x 275); the 18:00 slot quote is the R(D) open (NaN
  if missing); 1-minute robustness window =
  return starts 18:00 .. 16:54 NY (last ends 16:55), consecutive minutes with both bars present, no coverage floor.
- **What follows:** SIGNAL -> B51 val confirmation (own pre-registration, rule unchanged, 1 val trial, < 200 dates NONE). Not a LEAD
  until val passes and SPEC 4 and x1.5 net > 0. WEAK or NONE -> B50 closed, B51 closed unearned; no re-test with other grids,
  windows, holds or the opposite sign.
- **Power note (written before data):** ~21 h hold, SD ~40-45 pips, n ~1,200 non-Friday dev dates -> SE ~1.25 pips.
- **Code:** `src/fxresearch/realized_skew.py`; `scripts/run_e044_realized_skew.py`; tests `tests/test_realized_skew.py` (constants,
  RS formula / sign symmetry / scale invariance, 275-return window 18:00 .. 16:50 NY, coverage rule, entry 20:00 D / exit 16:55 D+1
  and sign, Friday exclusion, no look-ahead (bars after 16:55 NY on D do not change RS(D)), spread exclusion, 1-minute robustness,
  decision rule, pooled random walk -> |mean| < 1.5 and no SIGNAL). 369 tests pass. Synthetic smoke run passed (NONE, 35 dates).
- **Command (batch.sh):** `python scripts/run_e044_realized_skew.py | tee backtests/validation_reports/E044_results.txt` (also writes
  `E044_results.json` and `E044_days.csv`).
- **Trial count:** dev +1 when it runs (253 -> 254); val unchanged at 9; total 262 -> 263.
