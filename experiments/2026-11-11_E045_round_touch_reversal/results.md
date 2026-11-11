# E045 Results

**Run:** GitHub Actions run 43103436725, 2026-11-11 (outputs commit 684336c). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E045_results.json`, `backtests/validation_reports/E045_results.txt`,
`backtests/validation_reports/E045_trades.csv`. All figures below are copied from those files.

## Counts
dev trading dates with bars 1562; touch events 1195; trades **1000** (833 dates); skipped: roll 167, spread 7, coverage 1, overlap 20.
Events per year: 2015 258, 2016 217, 2017 190, 2018 209, 2019 125, 2020 196.

## B52 (1 trial; date-cluster bootstrap, 2000 draws, seed 0)

| n | dates | mean (pips) | median | SD | hit rate | t | t p (1-sided) | date-cluster 95% CI |
|---|---|---|---|---|---|---|---|---|
| 1000 | 833 | -0.71 | 0.025 | 18.878 | 0.5 | -1.19 | 0.8828 | (-1.878, 0.401) |

**Decision (pre-registered rule): NONE** (mean < 0: neither SIGNAL nor WEAK).

## Costs (descriptive)
Mean signed mid -0.71; net bid/ask -1.008; net SPEC 4 -1.208; net costs x1.5 -1.457; SPEC 4 net hit 0.486. Median spread entry/exit 0.3/0.3.

## Descriptive (not trials; do not change the decision)
- Control levels 23/73 (same fade rule): n 1055 (846 dates), mean +1.608, median 1.35, hit 0.5545, t p 0.0077, CI (0.421, 2.809).
  Round minus control -2.318 pips.
- Up-touch shorts n 539, -0.023, CI (-1.611, 1.585); down-touch longs n 461, -1.514, CI (-3.111, 0.055). Share short 0.539.
- Level crossed by close within the hold: share 0.831 (-4.085); not crossed 0.169 (+15.885). Ex-post split, uses the outcome window.
- Continuation (opposite sign) +0.71, reported only.
- Horizons: 15 min -0.259, CI (-1.019, 0.497); 120 min -1.429, CI (-3.025, 0.222).
- Within 15 min of NY 08:30: n 65, -6.501; 10:00: n 65, +2.675; 11:00: n 34, -2.935. Outside release/fix windows n 836, -0.433, CI (-1.6, 0.781).
- By year: 2015 -3.742, 2016 -1.031, 2017 +0.104, 2018 +1.565, 2019 +1.281, 2020 -0.768.
