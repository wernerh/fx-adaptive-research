# E036 Results

**Run:** GitHub Actions run 42885844344, 2026-11-10 (outputs commit 69cf81e). Block: **val only** (910,768 EUR/USD bars,
2021-01-20 22:00 UTC -> 2023-06-30 20:59 UTC). Dev not used, OOS untouched.
**Raw outputs:** `backtests/validation_reports/E036_results.json`, `backtests/validation_reports/E036_results.txt`,
`backtests/validation_reports/E036_days.csv`.

Trading dates 637; valid r_on dates 632. B33 burn-in 20 valid dates (missing signal 20), zero signal 0, missing entry 0,
missing exit 0, entry spread > 2 pips 1, **tested 616**.

## Pre-registered test (1 val trial, -sign(O20) x 07:00 -> 16:55 NY, signed mid pips, block-20 bootstrap)

| Arm | n | mean | median | SD | hit | t | t p (1-sided) | block boot CI 95% | Decision |
|---|---|---|---|---|---|---|---|---|---|
| B34 (B33 on val) | 616 | +0.193 | -2.3 | 43.302 | 0.4659 | 0.11 | 0.4561 | (-2.683, 3.23) | **NONE** |

`lead_cost_gate` False, `lead` False.

## Costs (descriptive)
- Mid +0.193, net bid/ask -0.292, SPEC 4 **-0.492**, x1.5 **-0.834**; median spread entry 0.3, exit 0.6.

## Descriptive (not trials; do not change the decision)
- |O20| terciles low/mid/high: -3.79 / -1.277 / +5.664 (high n 205, CI (1.33, 10.861), t p 0.029; descriptive only, not a trial).
- Share long 0.596; long days -0.512 (n 367), short days +1.231 (n 249). Unconditional long r_id -0.803.
- Excluding FOMC statement days (19 events): +0.423, CI (-2.454, 3.826). Excluding month-end dates (29 events): +0.715,
  CI (-2.244, 4.063).
- Mondays +3.185 (n 122), Tue-Fri -0.546 (n 494).
- SD r_on 34.045, SD r_id 43.295 pips.
- B32 daily arm on val (not a trial, B32 closed on dev): n 630, +0.138, CI (-3.162, 3.494).
- By year: 2021 -0.83 (n 227), 2022 +2.819 (n 259), 2023 H1 -3.255 (n 130).
