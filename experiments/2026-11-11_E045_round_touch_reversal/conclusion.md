# E045 Conclusion (2026-11-11, R104)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule: < 300 events -> NONE; SIGNAL if mean signed > 1.0 pip AND date-cluster bootstrap 95% CI lower > 0 AND one-sided t p < 0.05
(1 trial); WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B52: n 1000 events (833 dates), mean -0.71 pips, CI (-1.878, 0.401), t p 0.8828 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- Fading the first rejected touch of a 00/50 level gives no reversal over 60 min on dev; net of SPEC 4 costs it is -1.208 pips.
  Together with E018 (crossing continuation NONE), neither side of Osler's round-number mechanism shows in 1-minute EUR/USD mids
  2015-2020.
- The same fade at the control levels 23/73 is positive (+1.608, CI (0.421, 2.809), t p 0.0077). This is a control, not a trial: it
  says rejected touches of *arbitrary* levels mean-revert slightly, and round levels do worse than that (-2.318). It is the opposite of
  the published round-number effect, it is one of many descriptive cells, and it is not queued (lesson R076: no post-hoc re-tests on dev).
  It would only be tested as a new pre-registration with its own mechanism and fresh data.
- The crossed/not-crossed split conditions on the outcome window and carries no trading information.

## Next
B52 closed NONE (rejected_hypotheses.md); B53 closed unearned (0 trials). No dev re-test with other horizons, level steps, offsets,
sides or the continuation sign. No `ready` item remains: next run is a backlog refill.
