# E012 Results

**Run:** GitHub Actions run 42446726453, 2026-11-08 (outputs commit 82c6ccd). Block: **val only** (2021-01-21..2023-06-30). OOS untouched.
**Raw outputs:** `backtests/validation_reports/E012_results.json`, `backtests/validation_reports/E012_results.txt`.

**Dev consistency check (not a trial):** wed_ny18_long n 312, mean +1.333 pips; thu_ny18_long n 313, mean +1.240 pips. Matches E009 exactly, so the code reproduces the candidate definition.

| Test | n | Hit rate (95% CI) | Binom p | Mean signed pips (mid) | Block-boot 95% CI | Bonferroni p (x2, descriptive) | Decision |
|---|---|---|---|---|---|---|---|
| wed_ny18_long | 114 | 0.5965 (0.5047, 0.6820) | 0.0487 | 0.647 | (-0.079, 2.016) | 0.0974 | WEAK |
| thu_ny18_long | 117 | 0.5726 (0.4821, 0.6586) | 0.1388 | 0.938 | (-0.357, 2.465) | 0.2776 | NONE |

**Cost check (gates only the LEAD label):**

| Test | Mean signed mid | Median entry spread | Net at bid/ask | Net at SPEC 4 | Net at costs x1.5 | SPEC 4 net hit rate |
|---|---|---|---|---|---|---|
| wed_ny18_long | 0.647 | 1.7 | -0.460 | -0.660 | -1.313 | 0.4386 |
| thu_ny18_long | 0.938 | 1.5 | -0.116 | -0.316 | -0.943 | 0.4444 |

**Overall (pre-registered rule): WEAK.** Lead candidates: none. Trials: 2 (val total now 2 for val-only experiments; dev total unchanged at 226).
