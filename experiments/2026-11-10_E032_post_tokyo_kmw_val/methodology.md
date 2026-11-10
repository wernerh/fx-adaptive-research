# E032 Methodology (pre-registered 2026-11-10 R066, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only** (2021-01-21..2023-06-30,
  `splits.DEFAULT_PLAN`). The script first drops every bar at or after 2023-07-01 UTC, then every bar whose trading date is not `val`
  (`vol_state_fix.restrict_to_block`), **before** any computation. Dev and OOS untouched.
- **Dates:** trading dates (17:00 NY roll, SPEC 2) present in the val bars with weekday Mon-Fri. Trading date D's window runs from
  20:55 NY on NY calendar date D - 1 to 02:00 NY on calendar date D (both inside trading date D). Monday = Sunday-evening entry;
  Friday-evening entries do not exist (weekend).
- **Quotes (E011 rule):** quote at hh:mm = bid/ask **open** of the first bar in [hh:mm, hh:mm+5) NY whose trading date is D
  (`post_tokyo_kmw.td_quotes`). Entry 20:55, exit 02:00. Missing -> excluded, never filled.
- **Clock (fixed before data):** window in NY clock time, as the paper. 20:55 NY = 09:55 JST in EDT, 10:55 JST in EST; not adjusted.
  DST split is descriptive only.
- **Trade:** LONG EUR/USD; signed return = (mid exit - mid entry) / pip.
- **Exclusions, counted, first reason in this order:** `missing_entry`, `missing_exit`, `low_coverage` (< 280 of the 305 one-minute
  bars in [20:55, 02:00) NY), `entry_skipped_spread` (ask-bid at 20:55 NY > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** `post_tokyo_kmw.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block
  bootstrap 95% CI of the mean (block 20 dates, 2000 draws, seed 0). Fewer than 200 tested dates -> "insufficient sample" -> NONE.
- **Decision rule (`post_tokyo_kmw.decide_b27`, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Null calibration (code tests, written before data):** fat-tailed i.i.d. t(4) samples of 600: SIGNAL rate <= 5% over 200 draws;
  random-walk synthetic pipeline (18 months, 3 seeds): never SIGNAL.
- **Descriptive (not trials, do not change the decision):** EDT vs EST dates; first hour 20:55 -> 21:55 vs rest 21:55 -> 02:00; Monday
  (Sunday-evening entries) vs Tue-Fri; by year; by weekday; entry/exit median spreads; net per date at bid/ask, SPEC 4 (bid/ask net
  - 0.1 slippage - 0.1 commission) and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)).
- **What follows:**
  - SIGNAL -> logged as a val-only SIGNAL; if SPEC 4 and x1.5 net > 0, recorded in agent_decision_log.md as an **OOS candidate for
    the human**. Not a LEAD (no clean dev pass); no notification, no OOS run, nothing else queued on it.
  - WEAK or NONE -> B27 closed; no re-test with other windows, clocks, subsets or exits. Next: backlog refill.
- **Calendar label:** post-Tokyo-fix window; Asian session. Overlaps E011/B25/B26 windows by design.
- **Code:** `src/fxresearch/post_tokyo_kmw.py` (reuses `gotobi_fix.evaluate`, cost constants and `cost_summary`);
  `scripts/run_e032_post_tokyo_kmw.py`; tests `tests/test_post_tokyo_kmw.py` (constants fixed, window across NY midnight in the same
  trading date for EST and EDT, Monday = Sunday evening, exclusion order and 280-bar coverage edge, no look-ahead, random-walk never
  SIGNAL, rule behaviour incl. < 200 dates -> NONE). Synthetic smoke run passed (65 synthetic dates -> insufficient sample -> NONE).
- **Command:** `python scripts/run_e032_post_tokyo_kmw.py | tee backtests/validation_reports/E032_results.txt` (also writes
  `E032_results.json` and `E032_days.csv`).
