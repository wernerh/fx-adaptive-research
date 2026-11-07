# E009 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31). Val and OOS are not evaluated.
- **Unit of observation:** one (date, clock hour). Return = mid close of the last bar in the hour minus mid open of the first bar, in pips.
  Hours with fewer than 55 of 60 bars are dropped.
  - UTC cells: date = UTC calendar date, hour = UTC hour.
  - New York cells: date = FX trading date (17:00 NY roll, `sessions.trading_date`), hour = America/New_York clock hour (DST-aware).
- **Cells (192 trials):** `utc_hour` 24; `ny_hour` 24; `weekday_x_ny_hour` 120 (Mon-Fri trading date x NY hour);
  `month_end_x_ny_hour` 24 (last trading date of each month x NY hour). UTC and NY families overlap in content; all are counted anyway.
- **Cost model:** none (signal scan). Hourly round-trip costs (SPEC 4) are checked in any follow-up.
- **Statistics per cell:** n, mean, sd, up-share; one-sample t-test p; sign-test binomial p; moving-block bootstrap 95% CI of the mean (block 20, 2000 draws, seed 0).
- **Decision rule (pre-registered, `fxresearch.hourly_profile.decide`):**
  - **CANDIDATE** if |mean| >= 1.0 pip AND bootstrap CI excludes 0 on the side of the mean AND t-test p < 0.05/192 AND sign-test p < 0.05.
  - **NOTE** if |mean| >= 1.0 pip AND t-test p < 0.01 but not CANDIDATE (listed in results; spawns nothing).
  - **NONE** otherwise (also any cell with n < 40).
  - Experiment overall = CANDIDATES if >= 1 CANDIDATE cell, else NONE.
- **Follow-up rule:** at most the 3 CANDIDATE cells with the smallest t-test p become backlog items, each a **val-only**, 1-trial,
  pre-registered signal test in the observed direction with the B1 rule (mean signed > 1.0 pip, block-bootstrap CI lower > 0, binomial p < 0.05),
  marked as dev-derived. Cells explained by a known calendar effect already logged (London fix 16:00 London, ECB 14:15 CET, NY 10:00 releases)
  are labelled as such. Nothing from this scan is a lead by itself.
- **Code:** `src/fxresearch/hourly_profile.py`, `scripts/run_e009_hourly_profile.py`; tests in `tests/test_hourly_profile.py` (rule, NY clock, random-walk no-candidate test).
- **Command:** `python scripts/run_e009_hourly_profile.py | tee backtests/validation_reports/E009_results.txt`
- **Trial count after this experiment:** 30 + 192 = 222 on dev.
