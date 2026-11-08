# E011 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31).
  Val and OOS are not evaluated in this experiment. Val confirmation, if earned, is a separate experiment (B5v).
- **Outcome:** per trading date, mid close of the last bar before window end minus mid open of the first bar in the window
  (`outcomes.window_outcome`), in pips. Windows on the Asia/Tokyo clock: `pre` = [08:55, 09:55), `post` = [09:55, 10:55).
  Days with fewer than 55 of 60 bars in a window are dropped for that window.
- **Tests (2 trials):** `tky_pre_all` (short EUR/USD), `tky_post_all` (long EUR/USD). No subsets.
- **Statistics:** hit rate with Wilson CI, binomial p (vs 0.5), moving-block bootstrap 95% CI of mean signed pips (block 20, 2000 draws, seed 0).
- **Decision rule (pre-registered, per test; `fxresearch.fixes.decide` with n_trials=2, unchanged code from E007/E010):**
  - **SIGNAL** if mean signed pips > 1.0 AND block-bootstrap 95% CI lower bound > 0 AND binomial p < 0.05/2 = 0.025.
  - **WEAK** if mean signed > 0 and (CI lower bound > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
  - Experiment overall = SIGNAL if any test is SIGNAL; else WEAK if any WEAK; else NONE.
  - If SIGNAL: add B5v (the SIGNAL test(s) only, val block, same rule, plus cost check) as a new pre-registered experiment.
    WEAK or NONE does **not** go to val. Wrong-sign results are not re-tested in the opposite direction.
- **Descriptive cost check (B5 asks for it; NOT part of the rule):** per test on the same dev days: median entry spread
  (ask_open - bid_open of first bar), mean round-trip cost (mid signed - bid/ask net), mean net at actual bid/ask
  (long: buy ask open, sell bid close; short: reverse), and mean net at costs x1.5. Any SIGNAL with net x1.5 <= 0 is noted
  as not tradable; the lead criterion 3 is judged only at val.
- **Code:** `src/fxresearch/fixes.py` (`TOKYO_FIX_WINDOWS`, `E011_TESTS`, `window_bidask_net`), `scripts/run_e011_tokyo_fix.py`,
  tests in `tests/test_tokyo_fix.py` (random-walk no-signal test, UTC-midnight trading-date test, bid/ask net = mid - spread test).
- **Command:** `python scripts/run_e011_tokyo_fix.py | tee backtests/validation_reports/E011_results.txt`
- **Trial count after this experiment:** 224 + 2 = 226 on dev.
