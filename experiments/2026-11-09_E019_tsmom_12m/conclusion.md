# E019 Conclusion (2026-11-09, R035)

## Decision: **NONE on dev** (pre-registered rule `tsmom.decide_b16`, applied exactly). **No lead.**
Rule: SIGNAL if mean daily signed > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean -0.644 pips/day (not > 0), CI (-3.196, 1.978) includes 0, one-sided t p 0.678 -> **NONE**.
- Per the methodology, B16 is closed for this definition; no re-test with other lookbacks or hold times on dev.
- Cost check also negative: SPEC 4 net -0.674 pips/day, costs x1.5 -0.689 (carry not modelled).

## Reading the result (cautions, no new numbers)
- A 12-month sign rule on a single pair did not capture the trend on 2016-2020 EUR/USD; the short days (the larger share) lost on average
  while buy-and-hold over the same days was positive.
- As the pre-registered power note said, the CI half-width (~2.6 pips) means only a large daily effect could have passed; NONE does not
  rule out a small portfolio-level TSMOM premium (Moskowitz, Ooi & Pedersen 2012), it rules out a usable single-pair version at the 1-pip bar.
- Carry was not modelled; it would have helped the short days, but not enough to reverse a mean that is negative on both trial and cost views.

## Next
B16 closed (recorded in knowledge/rejected_hypotheses.md). No `ready` items remain in research/backlog.md -> next run refills.
