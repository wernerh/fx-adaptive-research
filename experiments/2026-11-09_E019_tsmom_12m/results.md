# E019 Results

**Run:** GitHub Actions run 42540081769, 2026-11-09 (outputs commit 99da3aa). Block: **dev only** (2015-01-01..2020-12-31). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E019_results.json`, `backtests/validation_reports/E019_results.txt`, `backtests/validation_reports/E019_daily.csv`.
Dev bars 2,240,215; dev trading dates 1,562; test days 1,292.
Excluded (first failing check): missing_now 6, missing_past 5, missing_next 6, no_next 1.

## Pre-registered test (1 trial)
Signed = sign(mid16(D) - mid16(D-252)) x (mid16(D+1) - mid16(D)), pips, 16:00 NY to 16:00 NY.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 20 days) | Decision |
|---|---|---|---|---|---|---|---|---|
| 1292 | -0.644 | 0.625 | 50.069 | 0.5031 | -0.462 | 0.678 | (-3.196, 1.978) | **NONE** |

## Descriptive (not trials; do not change the decision)
- **Long vs short days:** long n 566, mean signed +0.475; short n 726, mean signed -1.516; flat days 0.
- **Buy-and-hold mean over the same days:** +1.06 pips/day.
- **By year (n / mean / hit / long share):** 2015 7 / +14.407 / 0.714 / 0.000; 2016 258 / -4.497 / 0.457 / 0.547;
  2017 258 / +0.100 / 0.523 / 0.570; 2018 257 / -1.523 / 0.494 / 0.553; 2019 257 / +0.863 / 0.510 / 0.000; 2020 255 / +1.456 / 0.525 / 0.533.
- **Costs (swap/carry NOT included):** 77 round trips, 65 sign flips, mean 16.78 days per round trip; per day: mid -0.644, net bid/ask -0.662,
  SPEC 4 net -0.674, costs x1.5 -0.689; SPEC 4 net per round trip -11.306 pips; median 16:00 NY entry spread 0.2 pips.
