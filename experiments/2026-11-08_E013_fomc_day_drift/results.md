# E013 Results (phase 2, dev test)

**Run:** GitHub Actions run 42467005834, 2026-11-08 (outputs commit 48d4d0e). Block: **dev only** (statement dates 2015-01-01..2020-12-31). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E013_results.json`, `backtests/validation_reports/E013_results.txt`.
**Date file:** `data/calendars/fomc_dates.csv` (phase 1, runs 42458841737 / 42462817989; reviewed in R018/R019).

**Events:** 47 scheduled statement days; dropped for missing quotes: none. Excluded and listed: unscheduled 2019-10-04, 2020-03-02,
2020-03-15; cancelled scheduled slot 2020-03-18.

## Pre-registered test (1 trial): long EUR/USD 16:00 NY prev business day -> 16:00 NY statement day

| n | Mean pips (mid) | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 4) | Decision |
|---|---|---|---|---|---|---|---|---|
| 47 | 21.284 | 28.3 | 75.131 | 0.617 | 1.942 | 0.02913 | (2.747, 38.163) | **SIGNAL** |

Rule check: mean 21.284 > 10.0; CI lower 2.747 > 0; p 0.029 < 0.05 -> SIGNAL (`fomc.decide_b11`).

## Cost check (descriptive; gates only the LEAD label)

| Median entry spread | Net at bid/ask | Net at SPEC 4 | Net at costs x1.5 |
|---|---|---|---|
| 0.2 pips | 21.011 | 20.811 | 20.574 |

## Descriptive (not trials)

| Series | n | Mean | Median | SD | Hit | One-sided p | Block-boot CI |
|---|---|---|---|---|---|---|---|
| Same window, non-FOMC dev weekdays | 1495 | -0.39 | -0.2 | 56.333 | 0.499 | 0.605 | (-3.31, 2.667) |
| 13:00-16:00 NY on statement day | 47 | 8.022 | 1.9 | 65.662 | 0.532 | 0.203 | (-4.427, 19.986) |

Per year (mean pips, 8 meetings each, 2020: 7): 2015 +43.175, 2016 +34.256, 2017 +9.506, 2018 -1.525, 2019 +10.838, 2020 +32.907.
Per-meeting table: see `E013_results.txt`. Largest single meeting: 2015-03-18 +248.00 pips.

**Trials:** 1 (dev total 226 -> 227; total registered 228 -> 229).
