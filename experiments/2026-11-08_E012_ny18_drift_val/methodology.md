# E012 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only** for the test (2021-01-21..2023-06-30).
  OOS is not evaluated. Dev is used only to reproduce the E009 cell means as a code consistency check (no new trial; must match
  +1.333 / +1.240 pips, n 312 / 313, else the run is treated as a code error, not a result).
- **Unit / outcome (identical to E009):** per FX trading date (17:00 NY roll, `sessions.trading_date`), the 18:00 America/New_York
  clock hour (DST-aware). Return = mid close of last bar minus mid open of first bar, in pips. Hours with < 55 of 60 bars dropped.
  Weekday = weekday of the trading date (Wed = 2, Thu = 3), so the hour falls on the previous calendar evening in New York.
- **Tests (2 trials, val):** `wed_ny18_long` (B9), `thu_ny18_long` (B10), both long EUR/USD. No other weekdays, hours or subsets.
- **Statistics:** `predictive.evaluate_predictor` with a constant +1 signal: hit rate with Wilson CI, binomial p vs 0.5,
  moving-block bootstrap 95% CI of mean signed pips (block 20, 2000 draws, seed 0).
- **Decision rule (pre-registered by the E009 follow-up rule and backlog B9/B10; `fixes.decide(res, n_trials=1)`, per test):**
  - **SIGNAL** if mean signed pips > 1.0 AND block-bootstrap 95% CI lower bound > 0 AND binomial p < 0.05.
  - **WEAK** if mean signed > 0 and (CI lower > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
  - Overall = SIGNAL if any test is SIGNAL, else WEAK if any WEAK, else NONE. A binomial p x2 (Bonferroni over the two tests)
    is reported descriptively and does not change the decision.
- **Cost check (reported for every test; gates only the LEAD label, not the SIGNAL decision):** on the same val days, long
  trade buying the ask open of the first 18:00 bar and selling the bid close of the last bar. Reported: median entry spread,
  mean net at bid/ask, mean net at the SPEC 4 model (bid/ask minus 0.1 pip entry slippage minus 0.1 pip commission),
  mean net at costs x1.5 (gross mid - 1.5 x (gross - SPEC 4 net)), and SPEC 4 net hit rate.
- **What follows:**
  - SIGNAL with SPEC 4 net > 0 AND costs x1.5 net > 0 -> LEAD per docs/AUTONOMOUS_PROTOCOL.md (criterion 1 = E009 CANDIDATE
    under its pre-registered dev rule; criterion 2 = this val test; criterion 3 = cost gate; criterion 4 = rollover-adjacent hour,
    not a logged fix or release effect). Write agent_logs/LEADS.md, notify, pause this line; OOS needs human approval.
  - SIGNAL failing the cost gate -> recorded as "mid-quote drift, not tradable"; no lead, no further test of these cells.
  - WEAK or NONE -> hypothesis rejected for these cells; not re-tested with other hours or weekdays on val.
- **Code:** `src/fxresearch/ny_hour_drift.py`, `scripts/run_e012_ny18_drift.py`; tests `tests/test_ny_hour_drift.py`
  (E009 definition match, post-roll trading-date mapping, net = mid - spread, random-walk no-SIGNAL).
- **Command:** `python scripts/run_e012_ny18_drift.py | tee backtests/validation_reports/E012_results.txt`
- **Trial count:** dev unchanged at 226; val trials +2 (first val-only experiment; E001/E006 also evaluated val).
