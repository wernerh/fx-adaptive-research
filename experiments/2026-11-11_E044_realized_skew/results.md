# E044 Results

**Run:** GitHub Actions run 43078625073, 2026-11-11 (outputs commit 1587b7d). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E044_results.json`, `backtests/validation_reports/E044_results.txt`,
`backtests/validation_reports/E044_days.csv`. All figures below are copied from those files.

## Counts
trading dates 1565; valid signal dates 1556; invalid signal 9; Friday excluded 310; zero signal 0; missing entry 4; missing exit 4;
entry skipped (spread) 0; **tested 1238**. Median valid returns per date 275.

## B50 (1 trial; moving-block bootstrap, block 20 dates, 2000 draws, seed 0)

| n | mean (pips) | median | SD | hit rate | t | t p (1-sided) | block-20 95% CI |
|---|---|---|---|---|---|---|---|
| 1238 | -0.183 | -1.7 | 58.627 | 0.4847 | -0.11 | 0.5436 | (-3.845, 4.329) |

**Decision (pre-registered rule): NONE** (mean < 0: neither SIGNAL nor WEAK).

## Costs (descriptive)
Mean signed mid -0.183; net bid/ask -0.665; net SPEC 4 -0.865; net costs x1.5 -1.206. Median spread entry / exit 0.3 / 0.5.

## Descriptive (not trials; do not change the decision)
- Share long 0.5129. Opposite sign mean +0.183 (reported only). Unconditional long same hold: -0.99, CI (-3.829, 2.394).
- corr(RS(D), R(D)) 0.564; sign agreement 0.7666. Within R(D) > 0: n 610, -2.28, CI (-6.826, 4.087); within R(D) < 0: n 628, +1.854, CI (-2.319, 7.079).
- RS mean 0.0744, median 0.0226, SD 1.3169.
- 1-minute RS: sign agreement with 5-min 0.8037; signed mean +0.181, CI (-3.628, 4.556).
- |RS| terciles: low -1.063; mid -2.77; high +3.279, CI (-1.742, 11.123) (post-hoc, not a trial).
- By year: 2015 +2.291, 2016 +0.936, 2017 -8.823, 2018 +2.833, 2019 +0.361, 2020 +1.346.
