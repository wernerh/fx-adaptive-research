# E041 Methodology (pre-registered 2026-11-11 R091, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. Dukascopy WTI crude CFD `lightcmdusd` 1-minute bid/ask
  (dukascopy-node 1.51.1 metadata: minute data from 2011-09-23, checked R088), downloaded on the GitHub Actions runner only
  (`scripts/download_dukascopy_oil.sh`, 2015-01-01 -> 2021-01-01, into `data/raw_oil/`, git-ignored). **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every EUR/USD bar whose trading date is not `dev` and every WTI
  bar at or after 2021-01-01 UTC **before** any computation; val and OOS untouched.
- **Dates:** sorted EUR/USD dev trading dates (17:00 NY roll, SPEC 2) on Monday-Friday (`relative_equity.fx_dates`, weekend
  artefacts dropped and counted). Previous / next valid trading date = neighbour in this list (weekends and holidays held).
- **Quotes:** bid/ask **open** of the first 1-minute bar in [T, T+5 min) Europe/London on London calendar date D
  (`month_end_hedging.london_quotes`, DST-aware). Missing or non-positive bid/ask -> invalid, never filled, **no holiday fallback**.
- **Signal (fixed in backlog R088):** O(D) = ln WTI(D, 16:00 London) - ln WTI(prev, 16:00 London). Position +sign(O).
  Dukascopy CFD roll handling is UNVERIFIED; |O| > 0.10 is skipped as a probable roll gap or the April 2020 episode.
- **Trade:** enter at the 16:05 London EUR/USD quote on D, exit at the 16:00 London quote on the next date. Signed return = position x
  (mid exit - mid entry) / pip. Trades never overlap.
- **Exclusions (counted, first reason in this order):** `burn_in` (first date), `missing_oil_quote` (either end), `zero_signal`,
  `oil_jump` (|O| > 0.10), `missing_entry`, `missing_exit` (incl. last dev date), `entry_skipped_spread` (entry ask-bid > 2.0 pips,
  SPEC 4).
- **Data gate (first, 0 trials if it fails):** WTI series empty, or a valid WTI quote at BOTH 16:00 London points (D and previous) on
  < 90% of the dev dates that have a previous date -> BLOCKED; no trade result computed. On BLOCKED: fix the download once, else block
  the item (0 trials).
- **Statistic (1 trial):** `oil_lag.evaluate` (= `overnight_reversal.evaluate_b32`): mean, median, SD, hit rate, one-sided t-test
  (H1 mean > 0), moving-block bootstrap 95% CI of the mean (**block 20 dates**, 2000 draws, seed 0).
- **Decision rule (`decide_b45` = `overnight_reversal.decide_b34`, unchanged from the backlog draft):**
  - < 500 tested dates -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** contemporaneous corr(O, EUR/USD 16:00 prev -> 16:00 D) and lagged corr;
  |O| terciles; by year; Mondays; Fridays (weekend hold); excluding FOMC statement dates; unconditional long; share long; median
  spreads; net per date at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5. Brent not used.
- **What follows:** SIGNAL -> add a val confirmation item (own experiment and pre-registration, rule unchanged, 1 val trial). Not a
  LEAD until val passes and SPEC 4 and x1.5 net > 0. WEAK or NONE -> B45 closed; no re-test on dev with other lags, windows or
  oil benchmarks. Next: backlog refill (no other `ready` item).
- **Power note (written before data):** ~1,550 dev dates, daily SD ~50 pips -> SE ~1.3 pips (block bootstrap may widen it); the
  p < 0.05 bar binds near +2.1 pips.
- **Calendar label:** entry just after the London 4pm fix; holds through 08:30 NY releases, the 10:30 NY EIA inventory release
  (Wednesdays) and the next fix (exit at it). Not a fix strategy.
- **Code:** `src/fxresearch/oil_lag.py`; `scripts/run_e041_oil_lag.py`; tests `tests/test_oil_lag.py` (constants, sign convention,
  16:05 -> next 16:00 trade, oil_jump and no fallback, exclusion order, no look-ahead, random-walk SIGNAL rate, injected effect ->
  SIGNAL and < 500 -> NONE, data gate boundary, cost columns, quotes from bars at London 16:00/16:05). Synthetic smoke run passed.
- **Command (batch.sh):** `bash scripts/download_dukascopy_oil.sh` (log `E041_oil_download.log`; a failure does not fail the job, the
  gate records BLOCKED) then `python scripts/run_e041_oil_lag.py | tee backtests/validation_reports/E041_results.txt` (also writes
  `E041_results.json` and `E041_days.csv`).
- **Trial count:** dev +1 when it runs (250 -> 251); val unchanged at 9; total 259 -> 260.
