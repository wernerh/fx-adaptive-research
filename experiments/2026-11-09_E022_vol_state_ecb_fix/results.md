# E022 Results

**Run:** GitHub Actions run 42585915012, 2026-11-09 (outputs commit 6b6aba6). Block: **dev only** (2015-01-01..2020-12-31). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E022_results.json`, `backtests/validation_reports/E022_results.txt`, `backtests/validation_reports/E022_days.csv`.
Dev bars 2,240,215. Trading dates 1562, valid dates 1556, low coverage 6; states: prev_invalid 6, burn-in 60, normal 1021, high 474.
Excluded: missing entry 0, missing exit 0, entry skipped for spread 1. Events tested 473.
Mean prior-date range of events 122.928 pips; median threshold 88.155 pips; median daily range 77.075 pips.

## Pre-registered test (1 trial)
Signed = -(mid 08:15 NY - mid 02:00 NY) on trading date D, pips, on dates whose previous trading date's mid range > p67 of the 60 valid dates before it.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 10 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 473 | 3.646 | 3.65 | 35.646 | 0.5349 | 2.225 | 0.0133 | (0.011, 7.751) | **SIGNAL** |

## Descriptive (not trials; do not change the decision)
- **Control, normal dates after burn-in, same short:** n 1016, mean +1.731, median 1.65, hit 0.5226, t p 0.0371, CI (-0.098, 3.554).
- **All post-burn-in dates, same short:** n 1489, mean +2.339, hit 0.5265, t p 0.0028, CI (0.641, 4.08).
- **By year (n / mean / hit):** 2015 51 / +10.852 / 0.608; 2016 86 / +5.737 / 0.547; 2017 78 / +3.31 / 0.487; 2018 95 / -0.776 / 0.495;
  2019 70 / +1.061 / 0.514; 2020 93 / +4.506 / 0.581.
- **By weekday (n / mean / hit):** Mon 104 / +3.573 / 0.548; Tue 69 / +10.292 / 0.594; Wed 87 / +6.34 / 0.586; Thu 100 / -0.115 / 0.47;
  Fri 113 / +0.91 / 0.504.
- **Costs:** mid +3.646, net bid/ask +3.339, SPEC 4 net +3.139, costs x1.5 +2.886 pips per event; median spread entry 0.3, exit 0.3 pips.
- **Limitation (stated in pre-registration):** ECB monetary-policy days not identifiable (no ECB calendar in repo).
