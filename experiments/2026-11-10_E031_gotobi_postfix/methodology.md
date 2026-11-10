# E031 Methodology (pre-registered 2026-11-10 R063, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Universe, gotobi dates, quote rule:** exactly as E030 (`gotobi_fix.universe`, `gotobi_fix.gotobi_info`,
  `gotobi_fix.local_quotes`; see experiments/2026-11-10_E030_gotobi_tokyo_fix/methodology.md). 09:55-10:55 Tokyo = 00:55-01:55 UTC,
  after the 17:00 NY roll, so the trading date equals the Tokyo calendar date (tested). Japanese public holidays not shifted
  (limitation).
- **Trade:** LONG EUR/USD, entry = mid of the 09:55 Tokyo quote (bid/ask open of the first bar in [09:55, 10:00)), exit = mid of the
  10:55 Tokyo quote. Signed return = +(mid exit - mid entry) / pip.
- **Exclusions, counted, first reason in this order:** `missing_entry`, `missing_exit`, `low_coverage` (< 55 of the 60 one-minute bars
  in [09:55, 10:55) Tokyo), `entry_skipped_spread` (ask-bid at 09:55 > 2.0 pips, SPEC 4). The 08:55 quote is used only for the
  descriptive pre-fix move and never excludes an event.
- **Statistic (1 trial):** `gotobi_fix.evaluate` unchanged: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block
  bootstrap 95% CI of the mean (**block 20 events**, 2000 draws, seed 0). Fewer than 40 tested events -> insufficient sample -> NONE.
- **Decision rule (`gotobi_postfix.decide_b26` = `decide_b25`, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** non-gotobi control (same trade on tradable non-gotobi dates) and the
  difference gotobi minus control; month-end vs other gotobi; weekend-shifted vs not; 10:25 -> 10:55 last half hour (gotobi and
  control); **exploratory** post-fix return conditional on the sign of the pre-fix move (mid 09:55 - mid 08:55), gotobi down/up and
  control down; by year; by weekday; median spreads; net per event at bid/ask, SPEC 4 and costs x1.5, for events and control.
- **What follows:**
  - SIGNAL -> queue val confirmation B26v as its own experiment with this rule unchanged, and note the control comparison. LEAD needs
    dev SIGNAL + val pass + SPEC 4 and x1.5 net > 0 (AUTONOMOUS_PROTOCOL). Calendar label: the Tokyo fix *is* the strategy.
  - WEAK or NONE -> B26 closed; the gotobi Tokyo-fix line is closed on dev (no further windows or day rules). Next: backlog refill.
- **Calendar label:** post-Tokyo-fix hour, Asian session (= 20:55-21:55 NY in EST, 21:55-22:55 in EDT, previous NY calendar date).
- **Code:** `src/fxresearch/gotobi_postfix.py` (reuses `gotobi_fix`); `scripts/run_e031_gotobi_postfix.py`; tests
  `tests/test_gotobi_postfix.py` (constants fixed, Tokyo-date keying with long sign and pre-fix move, exclusions use the post-fix
  window and the 08:55 spread never excludes, no look-ahead, random-walk pipeline gives no SIGNAL (3 seeds), fat-tailed null SIGNAL
  rate <= 5% over 200 draws, strong effect -> SIGNAL, insufficient sample -> NONE). Synthetic smoke run passed (NONE, 13 events).
- **Command:** `python scripts/run_e031_gotobi_postfix.py | tee backtests/validation_reports/E031_results.txt` (also writes
  `E031_results.json` and `E031_days.csv`).
- **Trial count:** dev +1 when it runs (237 -> 238); val unchanged at 7; total 244 -> 245.
