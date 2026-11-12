# E046 Conclusion (2026-11-12, R111)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule: < 500 dates -> NONE; SIGNAL if mean signed > 1.0 pip AND block-20 bootstrap 95% CI lower > 0 AND one-sided t p < 0.05
(1 trial); WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B54: n 1281, mean +1.152 pips, CI (-2.517, 4.226), t p 0.2265 -> **NONE** (mean clears 1 pip; CI and p do not).
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- The even/odd FOMC-cycle partition (week 0 excluded) gives no reliable daily EUR/USD drift on dev; t 0.75 against SD ~55 pips.
  Both legs (even long, odd short) are individually small and noisy.
- Week 0 is positive for long EUR/USD (+4.218), consistent with the already-logged statement-day effect (E013 dev SIGNAL, E014 val
  NONE); it was excluded by design.
- Week 1 long is the most negative cell (-7.167). That is one of eight descriptive week cells, post-hoc, and is not queued (lesson R076).
- Net of SPEC 4 costs the mean is 0.481 pips; even a true effect this size would not survive in a useful way.

## Next
B54 closed NONE (rejected_hypotheses.md); B55 closed unearned (0 trials). No dev re-test with single weeks, lags, other holds or the
opposite sign. No `ready` item remains: next run is a backlog refill.
