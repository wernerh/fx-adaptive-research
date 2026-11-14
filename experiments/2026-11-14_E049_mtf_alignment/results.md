# E049 Results

**Run:** GitHub Actions run 43541310326, 2026-11-14 (outputs commit 577da62). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E049_results.json`, `backtests/validation_reports/E049_results.txt`,
`backtests/validation_reports/E049_trades.csv`. All figures below are copied from those files.

## Counts
5m EMA20 crosses in window 26548 (up 13259, down 13289); htf_missing 0; aligned state at the cross BULL 9831, BEAR 10215;
signals 8459. Skipped: roll 0, spread 6, coverage 6, overlap 3130. Tested **5317** trades on 1543 dates.

## B59 (1 trial; FX-trading-date cluster bootstrap, 2000 draws, seed 0)

| n | mean (pips) | median | SD | hit rate | t | t p (1-sided) | date-cluster 95% CI |
|---|---|---|---|---|---|---|---|
| 5317 | 0.216 | -0.05 | 14.978 | 0.4952 | 1.05 | 0.1469 | (-0.156, 0.599) |

**Decision (pre-registered rule): NONE** (mean < 1 pip, CI includes 0, t p > 0.05; not WEAK because neither CI lower > 0 nor p < 0.05).

## Costs (descriptive)
Mean signed mid 0.216; net bid/ask -0.056; net SPEC 4 -0.256; net costs x1.5 -0.492. Median spread entry/exit 0.3/0.3.

## Descriptive (not trials; do not change the decision)
- Control, every in-window 5m EMA20 cross, no alignment: n 8979, -0.286, CI (-0.613, 0.025), t p 0.9586; SPEC 4 net -0.755.
  Aligned minus control +0.502 pips (both below 1 pip; neither CI excludes 0).
- 10m trigger, same alignment: n 3007, +0.198, CI (-0.372, 0.757), t p 0.2423; SPEC 4 net -0.278.
- Long leg n 2606, +0.052, CI (-0.528, 0.598); short leg n 2711, +0.373, CI (-0.156, 0.95), t p 0.0938.
- Horizons: 30 min +0.077, CI (-0.201, 0.353); 120 min +0.056, CI (-0.577, 0.679).
- Release/fix windows (+-15 min): NY 08:30 n 320, +0.015; NY 10:00 n 306, +0.717; London 16:00 n 342, +0.499; outside n 4349, +0.173.
  Shares 6.0% / 5.8% / 6.4%.
- By year: 2015 +1.398, 2016 -0.076, 2017 +0.088, 2018 +0.258, 2019 -0.067, 2020 -0.296.
