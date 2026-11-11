# E041 Results

**Run:** GitHub Actions run 42996346127, 2026-11-11 (outputs commit 77c2f21). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC; WTI CFD `lightcmdusd` 2,613,666 bars, 2015-01-02 -> 2020-12-31 21:59 UTC).
Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E041_results.json`, `backtests/validation_reports/E041_results.txt`,
`backtests/validation_reports/E041_days.csv`, `backtests/validation_reports/E041_oil_download.log`. All figures below are copied from
those files.

## Data gate: **pass**
Dates with a previous date 1560; valid WTI quote at both 16:00 London points on 1540 (share 0.9872 >= 0.90).

## Counts
dates 1561; burn_in 1; missing_oil_quote 20; zero_signal 1; oil_jump 11; missing_entry 3; missing_exit 6; entry_skipped_spread 0;
**tested 1519**; weekend trading dates dropped 1.

## B45 (1 trial; moving-block bootstrap, block 20 dates, 2000 draws, seed 0)

| n | mean (pips) | median | SD | hit rate | t | t p (1-sided) | block-boot 95% CI |
|---|---|---|---|---|---|---|---|
| 1519 | 2.306 | 0.25 | 56.352 | 0.5023 | 1.595 | 0.0555 | (-0.513, 5.184) |

**Decision (`oil_lag.decide_b45`): NONE** (mean > 1.0 pip, but CI lower < 0 and t p not < 0.05, so neither SIGNAL nor WEAK).

## Costs (descriptive)
Mean signed mid +2.306; net bid/ask +2.069; net SPEC 4 +1.869; net costs x1.5 +1.651. Median spread entry / exit 0.2 / 0.2.

## Descriptive (not trials; do not change the decision)
- Share long EUR/USD 0.517. O: mean -0.0001, SD 0.02372, median |O| 0.01274.
- Contemporaneous corr(O, EUR/USD 16:00 prev -> 16:00 D) 0.0405 (n 1516); lagged corr(O, next move) 0.0498.
- Unconditional long: n 1519, +0.079, CI (-2.193, 2.906).
- |O| terciles: low n 507 -2.016 CI (-5.78, 3.099); mid n 506 +2.992 CI (-1.563, 6.887); high n 506 +5.949, t p 0.015,
  CI (0.702, 10.682) - post-hoc, not a trial.
- Mondays n 295 +2.316; Fridays (weekend hold) n 301 -0.435; excluding 46 FOMC statement dates n 1473 +1.859, t p 0.0986,
  CI (-0.745, 4.693).
- By year: 2015 +11.066, 2016 +2.859, 2017 -0.542, 2018 +2.325, 2019 -3.61, 2020 +1.76.
