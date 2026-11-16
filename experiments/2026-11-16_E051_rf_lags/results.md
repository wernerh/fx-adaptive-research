# E051 Results

**Run:** GitHub Actions run 43840273851, 2026-11-16 (outputs commit 32b9e54). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched. scikit-learn 1.9.1.
**Raw outputs:** `backtests/validation_reports/E051_results.json`, `backtests/validation_reports/E051_results.txt`,
`backtests/validation_reports/E051_daily.csv`. All figures below are copied from those files.

## Counts
Trading dates 1562; test days **1241** (2016-01-12 .. 2020-12-23). Excluded: missing_lag 49, missing_now 5, missing_next 5,
flat 0, no_next 1. Fits: 62 attempted, 62 ok, 0 failures; first fit n 233 (to 2015-12-31, up share 0.4936); last fit 2020-12-04 n 1460.

## B62 (1 trial; moving-block bootstrap, block 20, 2000 draws, seed 0)
| n | mean pips | median | SD | hit | t | t p (one-sided) | 95% CI | decision |
|---|---|---|---|---|---|---|---|---|
| 1241 | 1.953 | 1.45 | 50.14 | 0.5109 | 1.372 | 0.0852 | (-1.244, 4.581) | **NONE** |

## Descriptive (not tested)
- Long days n 598, mean signed +2.973; short days n 643, mean signed +1.004. Buy-and-hold mean +0.912 pips/day.
- Mean p(up) 0.4967; quantiles q10 0.3529, q50 0.4902, q90 0.6471.
- TSMOM (E019) on the same 1236 dates -0.673; E051 on those dates +2.006; sign agreement 0.5316.
- E050 on the same 1241 dates -1.268; sign agreement 0.4988.
- Feature importances at last fit: all 10 lags 0.091-0.1063 (no dominant lag).
- By year mean (hit, long share): 2016 +0.270 (0.480, 0.547); 2017 -3.093 (0.480, 0.504); 2018 +3.669 (0.504, 0.427);
  2019 +6.641 (0.569, 0.472); 2020 +2.461 (0.523, 0.456).

## Cost check (descriptive; swap/carry not included)
629 round trips, 625 sign flips, 1.97 days per round trip. Mean per day: mid +1.953, bid/ask net +1.816, SPEC 4 net +1.715,
costs x1.5 +1.596. SPEC 4 net per round trip +3.383. Median entry spread 0.2 pips.
