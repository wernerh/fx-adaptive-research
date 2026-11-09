# E023 Results

**Run:** GitHub Actions run 42600685892, 2026-11-09 (outputs commit 4ab24c6). Block: **val only** (2021-01-21..2023-06-30). Dev not
re-used, OOS untouched (val bars 910,768, last bar 2023-06-30 20:59 UTC).
**Raw outputs:** `backtests/validation_reports/E023_results.json`, `backtests/validation_reports/E023_results.txt`, `backtests/validation_reports/E023_days.csv`.
Trading dates 637, valid 637, low coverage 0; states: prev_invalid 0, burn-in 60, normal 372, high 204.
Excluded: missing entry 0, missing exit 0, entry skipped for spread 0. Events tested 204.
Mean prior-date range of events 118.539 pips; median threshold 88.424 pips; median daily range 74.4 pips.

## Pre-registered test (1 val trial)
Signed = -(mid 08:15 NY - mid 02:00 NY) on val trading date D, pips, on dates whose previous trading date's mid range > p67 of the 60 valid val dates before it.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 10 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 204 | 1.197 | -2.875 | 33.278 | 0.4706 | 0.514 | 0.304 | (-3.144, 5.919) | **NONE** |

`lead_cost_gate` True (net > 0 at SPEC 4 and x1.5) but `lead` False (no SIGNAL).

## Descriptive (not trials; do not change the decision)
- **Control, normal val dates, same short:** n 370, mean +1.15, median -0.425, hit 0.4919, t p 0.2478, CI (-1.241, 4.012).
- **All post-burn-in val dates, same short:** n 574, mean +1.167, median -0.875, hit 0.4843, t p 0.1965, CI (-0.948, 3.899).
- **By year (n / mean / hit):** 2021 63 / +0.349 / 0.397; 2022 103 / +1.823 / 0.495; 2023 38 / +0.907 / 0.526.
- **By weekday (n / mean / hit):** Mon 42 / -7.095 / 0.333; Tue 30 / -13.375 / 0.333; Wed 31 / -2.994 / 0.355; Thu 50 / +6.881 / 0.52;
  Fri 51 / +13.573 / 0.686. (Dev weekday pattern did not repeat; post-hoc, not evidence.)
- **Costs:** mid +1.197, net bid/ask +0.822, SPEC 4 net +0.622, costs x1.5 +0.335 pips per event; median spread entry 0.4, exit 0.3 pips.
