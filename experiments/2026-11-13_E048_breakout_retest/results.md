# E048 Results

**Run:** GitHub Actions run 43528337777, 2026-11-13 (outputs commit c3259d5). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E048_results.json`, `backtests/validation_reports/E048_results.txt`,
`backtests/validation_reports/E048_trades.csv`. All figures below are copied from those files.

## Counts
UTC hours 52584, valid 37336; breakouts in window 1735 (plus 725 with < 20 valid look-back hours); setups 907 -> retest 372,
failed break 235, no retest 300. Skipped: roll 0, spread 0, coverage 0, overlap 0. Tested **372** trades on 366 dates.
Retests per year 54-69.

## B58 (1 trial; FX-trading-date cluster bootstrap, 2000 draws, seed 0)

| n | mean (pips) | median | SD | hit rate | t | t p (1-sided) | date-cluster 95% CI |
|---|---|---|---|---|---|---|---|
| 372 | -0.744 | -0.675 | 17.808 | 0.4785 | -0.806 | 0.7897 | (-2.614, 1.137) |

**Decision (pre-registered rule): NONE** (mean < 1 pip, CI includes 0, t p > 0.05).

## Costs (descriptive)
Mean signed mid -0.744; net bid/ask -1.001; net SPEC 4 -1.201; net costs x1.5 -1.429. Median spread entry/exit 0.2/0.2.

## Descriptive (not trials; do not change the decision)
- Long leg n 174, +0.594, CI (-1.528, 2.918); short leg n 198, -1.921, CI (-4.851, 0.724).
- Horizons: 30 min -0.832, CI (-2.089, 0.42); 120 min -0.908, CI (-3.945, 1.889).
- Enter at the breakout 1h close (no retest): n 906, +0.312, CI (-0.716, 1.353), t p 0.2942; SPEC 4 net -0.175, x1.5 -0.419.
- Release/fix windows (+-15 min): NY 08:30 n 5, -9.76; NY 10:00 n 36, +0.211; London 16:00 n 22, -3.539; outside n 309, -0.511.
- By year: 2015 -3.091, 2016 -2.466, 2017 +0.787, 2018 +0.235, 2019 -1.811, 2020 +1.426.
