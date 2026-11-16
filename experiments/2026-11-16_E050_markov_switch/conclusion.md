# E050 Conclusion (2026-11-16, R210)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule (E019): SIGNAL if mean daily signed > 1.0 pip AND moving-block bootstrap (block 20, 2000 draws, seed 0) 95% CI lower > 0 AND
one-sided t p < 0.05 (1 trial); WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- B60: n 1290, mean -1.106 pips, CI (-3.478, 1.441), t p 0.7853 -> **NONE** (mean < 0, so not WEAK).
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- The sign of the 8-day expected return of a walk-forward 2-state Markov switching model gives no daily EUR/USD edge on 2016-2020;
  the point estimate is negative. Dueker-Neely's 1982-2005 out-of-sample result does not carry over to this sample with this
  simplified model (2 states, switching mean+variance, mid returns, no interest differential).
- The signal changes rarely (19 round trips in 5 years), so it behaves like a slow regime/trend position; the short days drive the
  loss and the result sits close to the E019 TSMOM result on the same dates (both negative).
- Costs are negligible at this turnover; the failure is the gross signal, not costs.

## Next
B60 closed NONE (rejected_hypotheses.md); B61 closed unearned (0 trials). No dev re-test with 3 states, other horizons, refit
intervals, interest-differential excess returns or one leg. No `ready` item remains: next run is a backlog refill.
