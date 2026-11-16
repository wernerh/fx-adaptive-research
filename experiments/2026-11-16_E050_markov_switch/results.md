# E050 Results

**Run:** GitHub Actions run 43817068619, 2026-11-16 (outputs commit 73d73f3). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E050_results.json`, `backtests/validation_reports/E050_results.txt`,
`backtests/validation_reports/E050_daily.csv`. All figures below are copied from those files.

## Counts
Trading dates 1562; test days **1290** (2016-01-04 .. 2020-12-30). Excluded: missing_now 5, missing_next 5, flat 0, no_next 1.
Fits: 62 attempted, 62 ok, 0 failures; first fit n 256 (to 2015-12-31); model pairs dropped (missing 16:00 quote) 14.

## B60 (1 trial; moving-block bootstrap, block 20, 2000 draws, seed 0)
| n | mean pips | median | SD | hit | t | t p (one-sided) | 95% CI | decision |
|---|---|---|---|---|---|---|---|---|
| 1290 | -1.106 | 0.625 | 50.239 | 0.5023 | -0.79 | 0.7853 | (-3.478, 1.441) | **NONE** |

## Descriptive (not tested)
- Long days n 739, mean signed -0.0; short days n 551, mean signed -2.588. Buy-and-hold mean +1.105 pips/day.
- TSMOM (E019) on the same 1285 dates -0.726; E050 on those dates -1.11; sign agreement 0.5564.
- First fit: mu (-7.1475, 10.6805), sigma (61.9534, 115.8187), p_stay (0.9395, 0.7415). Last fit (2020-12-04, n 1530): mu (0.9319,
  -2.443), sigma (40.5266, 74.7647), p_stay (0.9961, 0.9888).
- By year mean (hit, long share): 2016 +1.420 (0.515, 0.000); 2017 -4.091 (0.512, 0.380); 2018 -2.517 (0.508, 0.988);
  2019 -0.854 (0.500, 0.829); 2020 +0.507 (0.477, 0.672).

## Cost check (descriptive; swap/carry not included)
19 round trips, 13 sign flips, 67.89 days per round trip. Mean per day: mid -1.106, bid/ask net -1.111, SPEC 4 net -1.114,
costs x1.5 -1.119. Median entry spread 0.2 pips.
