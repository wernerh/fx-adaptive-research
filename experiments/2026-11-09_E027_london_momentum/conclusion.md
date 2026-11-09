# E027 Conclusion (2026-11-09, R054)

## Decision: **NONE on dev** (pre-registered rule `london_momentum.decide_b22`, applied exactly). **No LEAD.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean -0.008 pips (not > 0), CI (-0.553, 0.455) includes 0, one-sided t p 0.5114 -> **NONE**.
- LEAD gate: condition 1 fails; costs also negative (SPEC 4 net -0.46, x1.5 -0.685).

## Reading the result (no new numbers)
- The first London half hour carries no information about the last half hour before the 16:00 London fix on dev: the mean is
  zero to two decimals, the slope is insignificant and no |r1| tercile or the first-hour variant (descriptive) is positive.
- The CI is narrow (about +/-0.5 pip), so with n 1551 this definition rules out an effect large enough to cover costs.
- The RUB/USD exchange-session analogue (Elaut et al. 2018) does not transfer to 24-hour EUR/USD with the London session as proxy.
  Prior written before data (low) held.

## Next
Per methodology: B22 closed for this definition; no re-test on dev with other windows, horizons or the first-hour variant. Added to
knowledge/rejected_hypotheses.md. No other `ready` backlog item -> refill next.
