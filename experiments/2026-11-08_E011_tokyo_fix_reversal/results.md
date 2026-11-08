# E011 Results

**Run:** GitHub Actions run 42438344654, 2026-11-08 (outputs commit b985245). Block: **dev only**. val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E011_results.json`, `backtests/validation_reports/E011_results.txt`.
Signed = short for `pre` (predicts USD up into the fix), long for `post` (predicts USD down after). Signal test is cost-free (mid).
Windows on the Asia/Tokyo clock: pre = [08:55, 09:55), post = [09:55, 10:55).

| Test | n | Hit rate (95% CI) | Binom p | Mean signed pips | Block-boot 95% CI | Mean abs window pips | Decision |
|---|---|---|---|---|---|---|---|
| tky_pre_all | 1560 | 0.5295 (0.5047, 0.5542) | 0.0212 | 0.321 | (-0.098, 0.756) | 6.407 | WEAK |
| tky_post_all | 1560 | 0.5385 (0.5137, 0.5631) | 0.0026 | 0.785 | (0.318, 1.173) | 6.129 | WEAK |

**Descriptive cost check (not part of the decision rule):**

| Test | Mean signed mid | Median entry spread | Mean round-trip cost | Mean net at bid/ask | Mean net at costs x1.5 |
|---|---|---|---|---|---|
| tky_pre_all | 0.321 | 0.4 | 0.345 | -0.024 | -0.196 |
| tky_post_all | 0.785 | 0.2 | 0.310 | 0.475 | 0.320 |

**Overall (pre-registered rule): WEAK.** Trials: 2 (dev total now 226).
