# E034 Conclusion (2026-11-10, R073)

## Decision: **B30-hour NONE, B30-day NONE on dev** (pre-registered rule `month_end_hedging.decide_b30`, applied exactly). **No LEAD.**
Rule per window: < 50 tested events -> NONE; SIGNAL if mean > 1.0 pip AND i.i.d. bootstrap CI lower > 0 AND one-sided t p < 0.025;
WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE. Data gate passed (0 missing index quotes), so both trials are used.
- HOUR: n 71 (>= 50), mean +1.731 > 1 but CI lower -4.152 (not > 0) and t p 0.285 (not < 0.025) -> **NONE**.
- DAY: n 71, mean +3.354 > 1 but CI lower -9.322 and t p 0.300 -> **NONE**.
- LEAD gate fails at condition 1 for both windows.

## Reading the result (no new numbers)
- The relative-equity (EU50 minus US500) month-to-date return does not predict EUR/USD into the month-end London fix on dev
  2015-2020 with n 71. Point estimates have the hypothesised sign but are below the unconditional long EUR/USD in both windows, and
  corr(S, move) is about zero. With SD 26 (hour) and 54 (day) pips the test could only detect ~5 / ~13 pips, as the power note said.
- The descriptive US-only leg (long EUR/USD after US equities rose month-to-date) is large on the DAY window (+23.082, t p 0.0001),
  but it was not pre-registered, it is one of many descriptive cells, and it overlaps the unconditional long drift (+12.501) because
  US equities rose in most dev months. It is not evidence for B30 and must not be re-tested on dev; any test would need its own
  pre-registration on val (~29 month-ends, low power) and counts as a new trial.
- This does not refute Melvin-Prins (their signal construction and sample are UNVERIFIED here).

## Next
Per methodology: NONE in both windows -> B30 closed, B31 closed unearned; no re-test with other windows, indices or lookbacks. Added
to knowledge/rejected_hypotheses.md. No `ready` item remains: next run is a backlog refill.
