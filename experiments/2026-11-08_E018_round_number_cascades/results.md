# E018 Results

**Run:** GitHub Actions run 42530297453, 2026-11-08 (outputs commit 2c6178c). Block: **dev only** (2015-01-01..2020-12-31). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E018_results.json`, `backtests/validation_reports/E018_results.txt`, `backtests/validation_reports/E018_trades.csv`.
Dev bars 2,240,215; dev trading dates with bars 1,562. Events (first crossings of 00/50 levels) 2,539; trades 2,143.
Skipped (first failing check): roll 295, overlap 92, spread 5, coverage 4.

## Pre-registered test (1 trial)
Signed = crossing direction x (mid open at exit - mid open at entry), 60-minute hold.

| n | Mean signed pips | Block-boot 95% CI (block 20) | Hit rate (Wilson CI) | Binomial p | Decision |
|---|---|---|---|---|---|
| 2143 | -0.128 | (-0.989, 0.714) | 0.4881 (0.467, 0.5093) | 0.2801 | **NONE** |

Spearman IC -0.0152 (p 0.4823).

## Descriptive (not trials; do not change the decision)
- **Control levels (23/73):** n 2196, mean -0.803 pips, CI (-1.534, -0.079), hit 0.4536, binom p < 0.001 (printed 0.0). Round minus control: +0.675 pips.
- **Other horizons:** 15 min -0.405 pips (hit 0.469, n 2143); 120 min -0.777 pips (hit 0.4757, n 2140).
- **By year (mean pips / hit):** 2015 +1.865 / 0.529 (n 486); 2016 -0.458 / 0.501; 2017 -0.313 / 0.480; 2018 -0.949 / 0.478; 2019 -0.789 / 0.452; 2020 -1.037 / 0.461.
- **By direction:** down-crossings +0.786 (hit 0.500, n 1050); up-crossings -1.006 (hit 0.477, n 1093).
- **Costs:** mid -0.128; net bid/ask -0.428; SPEC 4 net -0.628; costs x1.5 -0.879; SPEC 4 net hit 0.4722; median entry/exit spread 0.3/0.3 pips.
- **Calendar shares (event within +-15 min):** 08:30 NY 0.0649; 10:00 NY 0.0499; 11:00 NY 0.0299.
