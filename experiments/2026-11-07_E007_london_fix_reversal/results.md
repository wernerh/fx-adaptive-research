# E007 Results

**Run:** GitHub Actions run 42400981266, 2026-11-07 (outputs commit 0db6d13). Block: **dev only**. val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E007_results.json`, `backtests/validation_reports/E007_results.txt`.
Signed = short for `pre` (predicts USD up), long for `post` (predicts USD down). Cost-free signal test.

| Test | n | Hit rate (95% CI) | Binom p | Mean signed pips | Block-boot 95% CI | Mean abs window pips | Decision |
|---|---|---|---|---|---|---|---|
| pre_all | 1556 | 0.5231 (0.4983, 0.5479) | 0.0718 | 0.637 | (-0.528, 1.547) | 13.345 | NONE |
| post_all | 1555 | 0.5106 (0.4858, 0.5354) | 0.4171 | 0.476 | (-0.182, 1.117) | 9.529 | NONE |
| pre_month_end | 72 | 0.4583 (0.3483, 0.5726) | 0.5560 | -2.771 | (-10.099, 3.895) | 19.736 | NONE |
| post_month_end | 72 | 0.4167 (0.3099, 0.5319) | 0.1945 | -4.506 | (-7.189, -1.877) | 12.596 | NONE |

**Overall (pre-registered rule): NONE.** Trials: 4 (dev total now 26).
