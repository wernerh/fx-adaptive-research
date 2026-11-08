# E014 Conclusion (2026-11-08, R022)

## Decision: **NONE on val** (pre-registered E013 rule, applied exactly with `fomc.decide_b11`). **No lead.**
Rule: SIGNAL if mean > 10.0 pips AND block-4 CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- n 20, mean +19.99 pips (> 10), but CI (-9.53, 51.02) includes 0 and p 0.115 >= 0.05 -> neither SIGNAL nor WEAK -> **NONE**.
- Lead criterion 2 (pre-registered val confirmation passes) fails, so E013's dev SIGNAL is **not confirmed**. No notification.

## Reading the result (cautions, no new numbers)
- The val point estimate (+19.99) is close to dev (+21.28) and the non-FOMC benchmark is flat/negative, so the result is
  consistent with a real effect that val cannot resolve: the E013/B11v power note (written before val was seen) said val could
  only confirm a mean of roughly 35+ pips. A NONE here is "not confirmed", not "disproved".
- The rule stays as written. B11 is closed on dev+val. Per CLAUDE.md rule 5 and the protocol, the only clean further test is the
  locked OOS block, which needs an explicit human decision; it is not proposed as a lead because it did not meet the LEAD definition.
- Pooled dev+val (n 67, mean +20.9) is information only and must not be used as a test.

## Next
B11 line closed (recorded in knowledge/rejected_hypotheses.md as not confirmed on val). Next ready item: B12 (NFP 15-minute reaction continuation, dev, 1 trial).
