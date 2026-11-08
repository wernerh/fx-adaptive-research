# E010 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31).
  Val and OOS are not evaluated in this experiment. Val confirmation, if earned, is a separate experiment (B4v).
- **Outcome:** per trading date, mid close of the last bar before window end minus mid open of the first bar in the window
  (`outcomes.window_outcome`), in pips. Windows on the Europe/Berlin clock (DST-aware):
  `pre` = [13:15, 14:15), `post` = [14:15, 15:15). Days with fewer than 55 of 60 bars in a window are dropped for that window.
- **Tests (2 trials):** `ecb_pre_all` (short EUR/USD), `ecb_post_all` (long EUR/USD). No month-end subsets (B4 draft: 2 trials).
- **Cost model:** none in this signal test (cost-free, as E007). Costs are applied in any follow-up test. Reported for context: mean |window return|.
- **Statistics:** hit rate with Wilson CI, binomial p (vs 0.5), moving-block bootstrap 95% CI of mean signed pips (block 20, 2000 draws, seed 0).
- **Decision rule (pre-registered, per test; `fxresearch.fixes.decide` with n_trials=2, unchanged code from E007):**
  - **SIGNAL** if mean signed pips > 1.0 AND block-bootstrap 95% CI lower bound > 0 AND binomial p < 0.05/2 = 0.025.
  - **WEAK** if mean signed > 0 and (CI lower bound > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
  - Experiment overall = SIGNAL if any test is SIGNAL; else WEAK if any WEAK; else NONE.
  - If SIGNAL: add B4v (the SIGNAL test(s) only, val block, same rule, plus the US-release-day split for the post window) as a new
    pre-registered experiment. WEAK or NONE does **not** go to val. Wrong-sign results are not re-tested in the opposite direction.
- **Code:** `src/fxresearch/fixes.py` (`ECB_FIX_WINDOWS`, `E010_TESTS`), `scripts/run_e010_ecb_fix.py`,
  tests in `tests/test_ecb_fix.py` (random-walk no-signal test, Berlin-clock DST test).
- **Command:** `python scripts/run_e010_ecb_fix.py | tee backtests/validation_reports/E010_results.txt`
- **Trial count after this experiment:** 222 + 2 = 224 on dev.
