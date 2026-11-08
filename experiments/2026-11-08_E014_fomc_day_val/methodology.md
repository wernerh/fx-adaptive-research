# E014 Methodology (pre-registered 2026-11-08 R021, before any val run)

- **Data:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only.** The script truncates bars to
  2021-01-01..2023-06-30 23:59 UTC before any computation, so no OOS bar is ever read into a computation (the 2023-07-26 meeting is OOS and excluded).
- **Events:** `data/calendars/fomc_dates.csv` (validated R019, unchanged). Statement dates assigned to blocks with
  `splits.DEFAULT_PLAN` by statement date (as E013), via `fomc.calendar_block_dates`. Expected val set: **20 scheduled statement days**
  (2021-01-27 .. 2023-06-14), no cancelled slots, no unscheduled actions. Unscheduled/cancelled would be excluded and listed.
- **Window (unchanged from E013):** entry = mid open of the first bar in [16:00, 16:05) NY on the previous business day; exit = mid close of
  the last bar in [15:55, 16:00) NY on the statement day. Missing quote -> meeting dropped and listed, never filled.
- **Trials:** 1 (val). Benchmark and sub-window are descriptive, not trials.
- **Statistics (`fomc.evaluate_long`, unchanged):** n, mean, median, sd, hit rate, one-sided t (H1 mean > 0), moving-block bootstrap 95% CI
  (block 4, 2000 draws, seed 0).
- **Decision rule (`fomc.decide_b11`, unchanged):** SIGNAL if mean > 10.0 pips AND CI lower > 0 AND one-sided t p < 0.05;
  WEAK if mean > 0 and (CI lower > 0 or p < 0.05), not SIGNAL; else NONE.
- **LEAD (docs/AUTONOMOUS_PROTOCOL.md):** only if val decision = SIGNAL AND val SPEC 4 net mean > 0 AND val costs x1.5 net mean > 0
  (dev already SIGNAL and cost-positive). Calendar label: the event effect is the strategy.
- **Cost check (unchanged):** long at ask open, exit at bid close; SPEC 4 net = bid/ask net - 0.1 entry slippage - 0.1 commission;
  x1.5 net = gross - 1.5 x (gross - SPEC 4 net).
- **Descriptive (not trials):** same window on all other val weekdays (non-FOMC benchmark); 13:00-16:00 NY sub-window; per-year table;
  per-meeting table; pooled dev+val mean reported for information only (not part of any rule).
- **What follows:**
  - LEAD -> write agent_logs/LEADS.md, notify the human, pause this line; propose (not run) the OOS command. OOS needs explicit human approval.
  - WEAK / NONE -> B11 line closed (hypothesis to knowledge/rejected_hypotheses.md); no further window/variant tests on val.
- **Command:** `python scripts/run_e014_fomc_day_val.py | tee backtests/validation_reports/E014_results.txt`
- **Code:** `src/fxresearch/fomc.py` (`calendar_block_dates`, new; no change to existing functions), `scripts/run_e014_fomc_day_val.py`;
  tests in `tests/test_fomc.py` (val set = 20 dates, no dev/OOS dates; OOS block refused).
- **Trial count:** val +1 (2 -> 3); total 229 -> 230.
