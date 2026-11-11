# E042 Results

**Run:** GitHub Actions run 43021489775, 2026-11-11 (outputs commit 4d2b887). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC; XAU/USD `xauusd` 2,633,898 bars, 2015-01-01 00:00 -> 2020-12-31 21:59 UTC).
Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E042_results.json`, `backtests/validation_reports/E042_results.txt`,
`backtests/validation_reports/E042_days.csv`, `backtests/validation_reports/E042_gold_download.log`. All figures below are copied from
those files.

## Data gate: **pass**
Dates with a previous date 1560; valid gold quote at both 16:00 London points on 1544 (share 0.9897 >= 0.90).

## Counts
dates 1561; burn_in 1; missing_gold_quote 16; zero_signal 0; gold_jump 0; missing_entry 3; missing_exit 6; entry_skipped_spread 2;
**tested 1533**; weekend trading dates dropped 1.

## B46 (1 trial; moving-block bootstrap, block 20 dates, 2000 draws, seed 0)

| n | mean (pips) | median | SD | hit rate | t | t p (1-sided) | block-boot 95% CI |
|---|---|---|---|---|---|---|---|
| 1533 | -1.407 | 0.15 | 56.498 | 0.5003 | -0.975 | 0.8352 | (-4.415, 0.939) |

**Decision (`gold_lag.decide_b46`): NONE** (mean < 0: neither SIGNAL nor WEAK).

## Costs (descriptive)
Mean signed mid -1.407; net bid/ask -1.645; net SPEC 4 -1.845; net costs x1.5 -2.063. Median spread entry / exit 0.2 / 0.2.

## Descriptive (not trials; do not change the decision)
- Share long EUR/USD 0.473. G: mean 0.00025, SD 0.00852, median |G| 0.00423.
- Contemporaneous corr(G, EUR/USD 16:00 prev -> 16:00 D) 0.4026 (n 1530); lagged corr(G, next move) 0.0058.
- Opposite-sign (continuation) mean +1.407 (reported only, not a trial).
- corr(G, E041 O) on common dates 0.0329 (n 1520).
- Unconditional long: n 1533, -0.021, CI (-2.4, 2.838).
- |G| terciles: low n 511 -0.07; mid n 511 -3.285 CI (-7.44, 0.631); high n 511 -0.868.
- Mondays n 300 -4.588 CI (-10.941, -0.229); Fridays (weekend hold) n 302 -2.899; excluding 47 FOMC statement dates n 1486 -1.737,
  CI (-4.763, 0.554).
- By year: 2015 -2.09, 2016 +2.355, 2017 -1.016, 2018 -4.46, 2019 -2.701, 2020 -0.549.
