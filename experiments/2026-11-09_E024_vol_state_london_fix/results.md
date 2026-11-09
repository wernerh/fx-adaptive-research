# E024 Results

**Run:** GitHub Actions run 42617055931, 2026-11-09 (outputs commit a1bfd0d). Block: **dev only** (2015-01-01..2020-12-31). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E024_results.json`, `backtests/validation_reports/E024_results.txt`, `backtests/validation_reports/E024_days.csv`.
Dev bars 2,240,215. Trading dates 1562, valid dates 1556, low coverage 6; states: prev_invalid 6, burn-in 60, normal 1021, high 474.
Excluded: missing entry 0, missing exit 1, entry skipped for spread 1. Events tested 472.
Mean prior-date range of events 123.083 pips; median threshold 88.266 pips; median daily range 77.075 pips.

## Pre-registered test (1 trial)
Signed = +(mid 16:00 NY - mid 11:05 NY) on trading date D, pips, on dates whose previous trading date's mid range > p67 of the 60 valid dates before it.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 10 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 472 | 2.983 | 1.9 | 25.264 | 0.5339 | 2.565 | 0.0053 | (0.566, 4.847) | **SIGNAL** |

## Descriptive (not trials; do not change the decision)
- **Control, normal dates after burn-in, same long:** n 1015, mean +0.901, median 0.4, hit 0.5094, t p 0.1299, CI (-0.669, 2.68).
- **All post-burn-in dates, same long:** n 1487, mean +1.562, median 0.7, hit 0.5171, t p 0.0089, CI (0.397, 2.871).
- **FOMC statement days:** 12 events; excluding them n 460, mean +3.143, hit 0.5348, t p 0.0036, CI (0.787, 4.991).
- **By year (n / mean / hit):** 2015 51 / +6.91 / 0.608; 2016 86 / +5.913 / 0.581; 2017 78 / +2.702 / 0.564; 2018 95 / -1.776 / 0.474;
  2019 70 / -0.591 / 0.414; 2020 92 / +5.94 / 0.576.
- **By weekday (n / mean / hit):** Mon 104 / +3.357 / 0.529; Tue 68 / +4.038 / 0.515; Wed 87 / +5.413 / 0.575; Thu 100 / +2.35 / 0.56;
  Fri 113 / +0.693 / 0.496.
- **Costs:** mid +2.983, net bid/ask +2.715, SPEC 4 net +2.515, costs x1.5 +2.281 pips per event; median spread entry 0.2, exit 0.2 pips.
- **Limitation (stated in pre-registration):** WM/R fix at 11:00 NY except DST-mismatch weeks (window not shifted).
