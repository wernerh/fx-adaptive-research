# E052 Results

**Run:** GitHub Actions run 44712462069, 2026-11-20 (outputs commit 37aa727). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC; test window 2017-05-09..2020-12-31). Val and OOS untouched.
BTC/USD: Dukascopy `btcusd` m1 bid/ask, 1,752,419 bars, 2017-05-07 00:00 UTC -> 2020-12-31 21:59 UTC.
**Raw outputs:** `backtests/validation_reports/E052_results.json`, `backtests/validation_reports/E052_results.txt`,
`backtests/validation_reports/E052_daily.csv`, `backtests/validation_reports/E052_download.txt`. All figures below are copied from those files.

## Data gate
950 grid dates in range; BTC valid at both 16:00 NY points on 922 (share 0.9705 >= 0.90) -> **passed**.

## Counts
Grid dates 1562; test days **911** (2017-05-09 .. 2020-12-30). Excluded: no_next 1, missing_now 5, missing_next 5, missing_btc 28,
zero_signal 0, btc_jump 0.

## B64 (1 trial; moving-block bootstrap, block 20, 2000 draws, seed 0)
| n | mean pips | median | SD | hit | t | t p (one-sided) | 95% CI | decision |
|---|---|---|---|---|---|---|---|---|
| 911 | 2.278 | 2.55 | 48.398 | 0.5137 | 1.421 | 0.0779 | (-0.674, 5.176) | **NONE** |

## Descriptive (not tested)
- Same-day corr(B, EUR/USD prev 16:00 -> D 16:00) 0.0207 (n 906); lag corr(B, next move) 0.0486; long share 0.5258.
- B: mean 0.00267, SD 0.04857, median |B| 0.02078.
- Mondays (weekend B) n 175, mean -0.788, CI (-5.517, 7.134); Tue-Fri n 736, mean +3.007, t p 0.0462, CI (-0.118, 5.968).
- |B| terciles: low n 304 +0.843; mid n 303 +1.738; high n 304 +4.252 (CI (-2.85, 11.44)).
- Buy-and-hold on the same dates: mean +1.123, CI (-1.805, 4.094).
- By year mean (hit, long share): 2017 -3.004 (0.428, 0.559); 2018 +5.424 (0.562, 0.469); 2019 +0.296 (0.496, 0.531);
  2020 +4.141 (0.532, 0.560).

## Cost check (descriptive; swap/carry not included)
464 round trips, 456 sign flips, 1.96 days per round trip. Mean per day: mid +2.278, bid/ask net +2.137, SPEC 4 net +2.035,
costs x1.5 +1.913. SPEC 4 net per round trip +3.995. Median entry spread 0.3 pips.
