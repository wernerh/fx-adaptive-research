# E047 Results

**Run:** GitHub Actions run 43291084015, 2026-11-12 (outputs commit 5ed400d). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E047_results.json`, `backtests/validation_reports/E047_results.txt`,
`backtests/validation_reports/E047_trades.csv`. All figures below are copied from those files.

## Counts
UTC dates 1565; dates excluded (previous-day bars) 10; both-touch 0; events 1349; skipped roll 55, spread 2, coverage 4,
overlap 18; tested **1270** trades on 1154 dates. Events per year 213-238.

## B56 (1 trial; UTC-date cluster bootstrap, 2000 draws, seed 0)

| n | mean (pips) | median | SD | hit rate | t | t p (1-sided) | date-cluster 95% CI |
|---|---|---|---|---|---|---|---|
| 1270 | -0.187 | -0.5 | 24.389 | 0.489 | -0.274 | 0.6078 | (-1.588, 1.181) |

**Decision (pre-registered rule): NONE** (mean < 1 pip, CI includes 0, t p > 0.05).

## Costs (descriptive)
Mean signed mid -0.187; net bid/ask -0.463; net SPEC 4 -0.663; net costs x1.5 -0.900. Median spread entry/exit 0.3/0.3.

## Descriptive (not trials; do not change the decision)
- R1 long n 634, -0.727, CI (-2.724, 1.255); S1 short n 636, +0.351, CI (-1.389, 2.196). Traditional (fade) direction +0.187 (reported only).
- Horizons: 60 min +0.165, CI (-0.798, 1.146); 180 min -0.231, CI (-1.824, 1.352).
- Control levels +0.0023: n 1351, -0.212, CI (-1.378, 0.983); -0.0023: n 1351, -0.962, CI (-2.158, 0.143).
- Thesis bracket 0.15%: win rate (resolved) 0.4847 (602 win / 640 loss). Thesis window only: n 116, +2.359, CI (-2.102, 6.853);
  excluding that window: n 1154, -0.443.
- Release/fix windows (+-15 min): NY 08:30 n 102, -0.176; NY 10:00 n 60, -0.363; London 16:00 n 44, +2.782; outside n 1064, -0.301.
- By year: 2015 +2.563, 2016 -2.554, 2017 +1.493, 2018 -0.447, 2019 -0.407, 2020 -1.663.
