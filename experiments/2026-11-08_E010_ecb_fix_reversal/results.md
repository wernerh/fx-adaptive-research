# E010 Results

**Run:** GitHub Actions run 42429506649, 2026-11-08 (outputs commit cda15e9). Block: **dev only**. val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E010_results.json`, `backtests/validation_reports/E010_results.txt`.
Signed = short for `pre` (predicts USD up into the fix), long for `post` (predicts USD down after). Cost-free signal test.
Windows on the Europe/Berlin clock: pre = [13:15, 14:15), post = [14:15, 15:15).

| Test | n | Hit rate (95% CI) | Binom p | Mean signed pips | Block-boot 95% CI | Mean abs window pips | Decision |
|---|---|---|---|---|---|---|---|
| ecb_pre_all | 1556 | 0.5084 (0.4835, 0.5331) | 0.5262 | 0.760 | (0.124, 1.537) | 9.495 | WEAK |
| ecb_post_all | 1555 | 0.5087 (0.4838, 0.5335) | 0.5097 | 0.287 | (-0.753, 1.356) | 14.026 | NONE |

**Overall (pre-registered rule): WEAK.** Trials: 2 (dev total now 224).
