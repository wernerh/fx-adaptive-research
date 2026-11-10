# E029 Results

**Run:** GitHub Actions run 42728790080, 2026-11-10 (outputs commit cf4751a). Block: **val only** (2021-01-21..2023-06-30). Dev not
used, OOS untouched (val bars 910,768, last bar 2023-06-30 20:59 UTC).
**Raw outputs:** `backtests/validation_reports/E029_results.json`, `backtests/validation_reports/E029_results.txt`, `backtests/validation_reports/E029_days.csv`.
Trading dates 637, valid 635, invalid (missing signal quote) 2, burn-in 60, post burn-in valid 575. Events 34 (15 positive R,
19 negative R). Exclusions (first reason): Friday 9, missing entry 2, missing exit 0, **entry skipped for spread 19**; events tested **4**.
Median entry spread of all events 3.6 pips (median of the 4 tested: 1.8). Mean |R| of events 134.475 pips; median band SD 53.576 pips.

## Pre-registered test (1 val trial)
Signed = -sign(R(D) - m(D)) x (mid 02:00 NY on D+1 - mid 17:05 NY at the start of D+1), pips; event = R(D) (17:00 NY open -> 16:55 NY)
outside m +/- 2 s of the 60 prior valid val dates; Fridays excluded.

| n | Note | Decision |
|---|---|---|
| 4 | insufficient sample (< 10 events) | **NONE** |

## Descriptive (not trials; do not change the decision)
- Positive-R days n 1, negative-R days n 3, exit 03:00 NY n 4, k 2.5 n 3, excluding FOMC n 3: all "insufficient sample".
- k 1.5: n 12, mean +2.437, median 2.925, SD 14.625, hit 0.6667, t p 0.2877, CI (-7.771, 8.133).
- Control (long 17:05 -> 02:00 NY on post-burn-in tradable non-event dates): +1.474.
- FOMC statement-date events 1; first-Friday events 0; share short 0.25.
- By year (n / mean / hit): 2021 1 / +3.9 / 1.0; 2022 2 / -1.0 / 0.5; 2023 1 / +22.3 / 1.0.
- By weekday of D (n / mean / hit): Tue 2 / +18.15 / 1.0; Wed 1 / +3.9 / 1.0; Thu 1 / -16.0 / 0.0.
- Costs (n 4): mid +6.05, net bid/ask +4.975, SPEC 4 net +4.775, costs x1.5 +4.137 pips per event; median spread entry 1.8, exit 0.5 pips.
