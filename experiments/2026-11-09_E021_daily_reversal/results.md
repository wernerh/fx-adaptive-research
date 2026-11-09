# E021 Results

**Run:** GitHub Actions run 42567407426, 2026-11-09 (outputs commit 73ecba1). Block: **dev only** (2015-01-01..2020-12-31). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E021_results.json`, `backtests/validation_reports/E021_results.txt`, `backtests/validation_reports/E021_days.csv`.
Dev bars 2,240,215. Trading dates 1562, valid dates 1547, burn-in 60, large dates 299; excluded: Friday 69, next not adjacent 1,
missing 16:00 D 7, missing 16:00 prev 7, no prev 1, missing entry 0, missing exit 0, entry skipped for spread 0. Events tested 229.
Median threshold |R| 64.77 pips; mean |R| of events 93.548 pips.

## Pre-registered test (1 trial)
Signed = -sign(R(D)) x (mid 10:45 NY next trading date - mid 20:00 NY D), pips, on non-Friday dates with |R(D)| > p80 of the previous 60 valid dates.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 10 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 229 | -2.55 | -0.5 | 50.853 | 0.4934 | -0.759 | 0.7756 | (-7.097, 4.167) | **NONE** |

## Descriptive (not trials; do not change the decision)
- **16:00 -> 20:00 NY D move signed as reversal (before entry, not tradable at our rules):** n 229, mean +1.666, hit 0.5895, t p 0.0335,
  CI (-0.88, 3.866).
- **Control, non-large non-Friday dates, same trade:** n 953, mean -0.415, hit 0.4827, CI (-3.308, 2.545).
- **Up vs down moves:** up n 117, mean signed +6.625; down n 112, mean signed -12.133.
- **FOMC overlap:** move day FOMC 17, exit day FOMC 7, share either 0.1048.
- **By year (n / mean / hit):** 2015 27 / -7.176 / 0.556; 2016 41 / -2.121 / 0.488; 2017 39 / -0.486 / 0.462; 2018 44 / +0.851 / 0.500;
  2019 32 / +3.483 / 0.531; 2020 46 / -9.415 / 0.457.
- **Costs:** mid -2.55, net bid/ask -2.841, SPEC 4 net -3.041, costs x1.5 -3.287 pips per event; median spread entry 0.3, exit 0.3 pips.
