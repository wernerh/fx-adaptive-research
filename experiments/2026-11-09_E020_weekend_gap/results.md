# E020 Results

**Run:** GitHub Actions run 42556248995, 2026-11-09 (outputs commit 7e24c07). Block: **dev only** (2015-01-01..2020-12-31). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E020_results.json`, `backtests/validation_reports/E020_results.txt`, `backtests/validation_reports/E020_weekends.csv`.
Dev bars 2,240,215. Candidate weekends 313, valid 308 (missing_F 3, missing_M 1, missing_X 1), burn-in 26, events 91,
entry skipped for spread 1, events tested 90. Median threshold |gap| 10.637 pips; mean |gap| of events 22.889 pips.

## Pre-registered test (1 trial)
Signed = -sign(G) x (mid 16:00 NY Mon - mid 20:00 NY Sun), pips, on weekends with |G| > p67 of the previous 26 valid weekends.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 4 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 90 | -1.574 | -7.425 | 46.074 | 0.3778 | -0.324 | 0.6267 | (-12.699, 7.03) | **NONE** |

## Descriptive (not trials; do not change the decision)
- **All valid weekends after burn-in (no threshold):** n 282, mean -0.396, median -2.675, hit 0.461, CI (-5.685, 5.002).
- **Longer exits (events):** Tue 16:00 NY n 88, mean -12.743, CI (-24.634, 1.816); Fri 16:00 NY n 89, mean -7.824, CI (-30.792, 17.066).
- **Sun 17:00 -> 20:00 NY move signed against the gap:** n 89, mean -6.41, hit 0.292, CI (-9.077, -3.351) -- i.e. in the first 3 h
  after the open the gap tended to **extend**, not reverse, before the pre-registered entry.
- **Up vs down gaps:** up n 47, mean signed +3.159; down n 43, mean signed -6.748.
- **By year (n / mean / hit):** 2015 6 / +6.750 / 0.500; 2016 16 / +9.600 / 0.500; 2017 18 / -6.022 / 0.333; 2018 15 / -3.910 / 0.333;
  2019 17 / -3.138 / 0.294; 2020 18 / -6.411 / 0.389.
- **Costs:** mid -1.574, net bid/ask -1.908, SPEC 4 net -2.108, costs x1.5 -2.374 pips per event; median spread F 0.3, M 0.3, X 0.2 pips.
