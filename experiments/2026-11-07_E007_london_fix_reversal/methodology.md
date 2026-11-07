# E007 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31).
  Val and OOS are not evaluated in this experiment. Val confirmation, if earned, is a separate experiment (B1v).
- **Outcome:** per trading date, mid close of the last bar before window end minus mid open of the first bar in the window
  (`outcomes.window_outcome`), in pips. Windows on the Europe/London clock (DST-aware):
  `pre` = [15:00, 16:00), `post` = [16:00, 17:00). Days with fewer than 55 of 60 bars in a window are dropped for that window.
- **Tests (4 trials):** `pre_all` (short), `post_all` (long), `pre_month_end` (short), `post_month_end` (long).
  Month end = last trading date of each calendar month in the data.
- **Cost model:** none in this signal test (cost-free, like E001). Costs are applied in any follow-up strategy test.
  Reported for context: mean |window return|.
- **Statistics:** hit rate with Wilson CI, binomial p (vs 0.5), moving-block bootstrap 95% CI of mean signed pips (block 20, 2000 draws, seed 0).
- **Decision rule (pre-registered, per test; implemented in `fxresearch.fixes.decide`):**
  - **SIGNAL** if mean signed pips > 1.0 AND block-bootstrap 95% CI lower bound > 0 AND binomial p < 0.05/4 = 0.0125.
  - **WEAK** if mean signed > 0 and (CI lower bound > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
  - Experiment overall = SIGNAL if any test is SIGNAL; else WEAK if any WEAK; else NONE.
  - If SIGNAL: queue B1v (same tests, val block, same rule except the trial count stays as pre-registered there) as a new experiment.
    A WEAK or NONE result does **not** go to val.
- **Code:** `src/fxresearch/fixes.py`, `scripts/run_e007_london_fix.py`, tests in `tests/test_fixes.py` (random-walk no-signal test).
- **Command:** `python scripts/run_e007_london_fix.py | tee backtests/validation_reports/E007_results.txt`
- **Trial count after this experiment:** 22 + 4 = 26 on dev.
