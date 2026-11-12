# E047 Conclusion (2026-11-12, R126)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule: < 300 events -> NONE; SIGNAL if mean signed > 1.0 pip AND UTC-date cluster bootstrap 95% CI lower > 0 AND one-sided t p < 0.05
(1 trial); WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B56: n 1270, mean -0.187 pips, CI (-1.588, 1.181), t p 0.6078 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- Continuation after the first touch of previous-day pivot R1/S1 gives no EUR/USD drift on dev over 120 min; neither leg, nor the
  60/180-min horizons, nor the traditional fade direction differs from zero.
- Pivot levels behave like the arbitrary +-0.0023 control levels; no special status of R1/S1 is visible in mid prices.
- The thesis-period subset (+2.359, n 116) is descriptive and does not replicate outside that window.
- Net of SPEC 4 costs the mean is -0.663 pips.

## Next
B56 closed NONE (rejected_hypotheses.md); B57 closed unearned (0 trials). No dev re-test with other pivot levels (R2/S2, P), holds,
entry lags, the fade sign or control offsets. No `ready` item remains: next run is a backlog refill.
