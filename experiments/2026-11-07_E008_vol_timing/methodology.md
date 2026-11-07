# E008 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31).
  Val and OOS are not evaluated. Val confirmation, if earned, is a separate experiment (B2v).
- **Predictors (signal-safe, known before 08:00 NY):** `asia_range_pips`, `london_range_pips` (SPEC 2 sessions).
  Control: `atr_pips_prior` (mean daily range of the 14 prior trading days, shift(1); no look-ahead).
  Sessions with < 95% of expected minute bars are dropped (holidays/early closes).
- **Outcomes:** |US session return| 08:00-12:00 America/New_York (`y_us_ret_pips`, >= 228 of 240 bars) and
  |first US hour| 08:00-09:00 NY (`y_us_0800_0900_ret_pips`, >= 57 of 60 bars).
- **Tests (4 trials):** 2 predictors x 2 outcomes.
- **Statistic:** partial Spearman rho of predictor and |outcome| given prior ATR (Pearson correlation of rank residuals
  after regressing each rank on rank(ATR)); p from t with n-3 df; moving-block bootstrap 95% CI (block 20, 2000 draws, seed 0).
- **Change from the backlog draft (made before any data was seen):** the draft said "Spearman IC of range/ATR vs |move|".
  While writing the tests, a constant-volatility random walk showed that dividing predictor and outcome by the same noisy
  ATR biases the IC upward (~+0.04 mean across 20 seeds). Partial correlation tests the same idea without that bias
  (tests/test_vol_timing.py::test_no_shared_denominator_bias_on_random_walks). Also added: CI lower bound > 0 (robust to
  volatility clustering). Both make the rule stricter, not looser.
- **Decision rule (per test; `fxresearch.vol_timing.decide`):**
  - **USEFUL** if partial IC > 0.10 AND p < 0.01 AND block-bootstrap CI lower bound > 0.
  - **NOT_USEFUL** otherwise.
  - Overall = USEFUL if any test is USEFUL. A USEFUL test queues B2v (same test, val block, same rule) as a new experiment.
    USEFUL is never a lead by itself (no trades, no costs).
- **Descriptive only (no decision, not trials):** plain Spearman IC in pips, outcome means by range/ATR tercile.
- **Cost model:** none (magnitude signal test).
- **Code:** `src/fxresearch/vol_timing.py`, `scripts/run_e008_vol_timing.py`, `tests/test_vol_timing.py`
  (random-walk no-signal and no-bias tests).
- **Command:** `python scripts/run_e008_vol_timing.py | tee backtests/validation_reports/E008_results.txt`
- **Trial count after this experiment:** 26 + 4 = 30 on dev.
