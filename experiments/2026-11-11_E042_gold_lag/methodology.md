# E042 Methodology (pre-registered 2026-11-11 R094, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. Dukascopy XAU/USD spot `xauusd` 1-minute bid/ask
  (dukascopy-node 1.51.1 metadata: minute candles from 2003-05-05, checked R094), downloaded on the GitHub Actions runner only
  (`scripts/download_dukascopy_gold.sh`, 2015-01-01 -> 2021-01-01, into `data/raw_gold/`, git-ignored). **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every EUR/USD bar whose trading date is not `dev` and every
  gold bar at or after 2021-01-01 UTC **before** any computation; val and OOS untouched.
- **Dates, quotes, trade, exclusions, statistic:** identical to E041 (`oil_lag` code reused by `gold_lag`): Mon-Fri EUR/USD dev
  trading dates; bid/ask open of the first bar in [T, T+5 min) Europe/London, DST-aware, no fill and no holiday fallback; enter
  16:05 London D, exit 16:00 London next date; signed return = position x (mid exit - mid entry) / pip; exclusions counted in order
  `burn_in`, `missing_gold_quote`, `zero_signal`, `gold_jump` (|G| > 0.10, data-error guard), `missing_entry`, `missing_exit`,
  `entry_skipped_spread` (> 2.0 pips, SPEC 4).
- **Signal:** G(D) = ln XAU(D, 16:00 London) - ln XAU(prev, 16:00 London). Position **-sign(G)**.
- **Data gate (first, 0 trials if it fails):** gold series empty, or a valid gold quote at BOTH 16:00 London points (D and previous)
  on < 90% of the dev dates that have a previous date -> BLOCKED; no trade result computed. On BLOCKED: fix the download once, else
  block the item (0 trials).
- **Statistic (1 trial):** `gold_lag.evaluate` (= `overnight_reversal.evaluate_b32`): mean, median, SD, hit rate, one-sided t-test
  (H1 mean > 0), moving-block bootstrap 95% CI of the mean (**block 20 dates**, 2000 draws, seed 0).
- **Decision rule (`decide_b46` = `decide_b34`, = E041 rule, unchanged from the backlog draft):**
  - < 500 tested dates -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** contemporaneous corr(G, EUR/USD 16:00 prev -> 16:00 D); lagged corr;
  corr(G, E041's O) on common dates (from the committed `E041_days.csv`); opposite-sign (continuation) mean, reported only; |G|
  terciles; by year (lesson R092: check one-year concentration); Mondays; Fridays; excluding FOMC statement dates; unconditional
  long; median spreads; net at bid/ask, SPEC 4 and costs x1.5.
- **What follows:** SIGNAL -> B47 val confirmation (own pre-registration, rule unchanged, 1 val trial). Not a LEAD until val passes
  and SPEC 4 and x1.5 net > 0. WEAK or NONE -> B46 closed, B47 closed unearned; no re-test with the opposite sign, other lags,
  windows or metals.
- **Power note (written before data):** ~1,550 dev dates, daily SD ~56 pips (E041) -> SE ~1.4 pips; the p < 0.05 bar binds near
  +2.3 pips. ~260 registered trials: a single p just under 0.05 is expected noise (lesson R092), hence the val confirmation.
- **Calendar label:** daily cross-market signal; entry just after the London 4pm fix (16:00 -> 16:05 gap excluded by the entry
  rule); not a fix or release strategy.
- **Code:** `src/fxresearch/gold_lag.py`; `scripts/run_e042_gold_lag.py`; tests `tests/test_gold_lag.py` (constants and sign,
  16:05 -> next 16:00 trade, gold_jump and no fallback, exclusion order, no look-ahead, random-walk SIGNAL rate, injected reversal
  effect -> SIGNAL, injected continuation effect -> NONE, < 500 -> NONE, data gate boundary, cost columns, London-time quotes).
  Synthetic smoke run passed (NONE on synthetic data).
- **Command (batch.sh):** `bash scripts/download_dukascopy_gold.sh` (log `E042_gold_download.log`; a failure does not fail the
  job) then `python scripts/run_e042_gold_lag.py | tee backtests/validation_reports/E042_results.txt` (also writes
  `E042_results.json` and `E042_days.csv`).
- **Trial count:** dev +1 when it runs (251 -> 252); val unchanged at 9; total 260 -> 261.
