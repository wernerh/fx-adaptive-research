# E027 Results

**Run:** GitHub Actions run 42683469479, 2026-11-09 (outputs commit 405319c). Block: **dev only** (2015-01-01..2020-12-31). Val not
used, OOS untouched (dev bars 2,240,215, last bar 2020-12-31 21:59 UTC).
**Raw outputs:** `backtests/validation_reports/E027_results.json`, `backtests/validation_reports/E027_results.txt`, `backtests/validation_reports/E027_days.csv`.
Trading dates 1562, valid 1556, invalid (missing signal quote) 6, zero signal 4, missing entry 0, missing exit 0, entry skipped for
spread 1. Events tested 1551 (105 on DST-mismatch dates). Share long 0.518; mean |r1| 9.043 pips.

## Pre-registered test (1 dev trial)
Signed = sign(r1) x (mid 15:55 - mid 15:25 London) on dev trading date D, pips, r1 = mid 08:30 - mid 08:00 London.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 20 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 1551 | -0.008 | -0.05 | 11.553 | 0.4984 | -0.029 | 0.5114 | (-0.553, 0.455) | **NONE** |

## Descriptive (not trials; do not change the decision)
- **Reversal reading:** mean -0.008, essentially zero; nothing to log as exploratory.
- **First-hour signal (08:00 -> 09:00 London), same hold:** n 1548, mean -0.07, CI (-0.587, 0.459).
- **OLS slope of 15:25-15:55 return on r1:** 0.016 (t 0.674, p 0.500).
- **|r1| terciles:** low n 517 +0.062 (CI -0.725, 0.969); mid n 518 -0.257 (CI -1.653, 0.618); high n 516 +0.17 (CI -0.869, 0.986).
- **Month-end:** n 72, -1.79 (CI -3.854, 0.482); other dates n 1479, +0.078 (CI -0.437, 0.558).
- **DST-mismatch dates:** n 105, -0.32 (CI -1.739, 0.749).
- **Unconditional 15:25-15:55 London mean:** -0.567 pips.
- **By year (n / mean / hit):** 2015 259 / -0.052 / 0.471; 2016 259 / -0.569 / 0.459; 2017 258 / -0.089 / 0.519; 2018 259 / -0.428 / 0.502;
  2019 258 / +1.025 / 0.574; 2020 258 / +0.066 / 0.465.
- **By weekday (n / mean / hit):** Mon 310 / -0.391 / 0.516; Tue 309 / -0.458 / 0.472; Wed 310 / +0.417 / 0.494; Thu 312 / -0.679 / 0.503;
  Fri 310 / +1.071 / 0.506. (Post-hoc, not evidence.)
- **Costs:** mid -0.008, net bid/ask -0.26, SPEC 4 net -0.46, costs x1.5 -0.685 pips per event; median spread entry 0.2, exit 0.2 pips.
