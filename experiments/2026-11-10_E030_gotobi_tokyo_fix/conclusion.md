# E030 Conclusion (2026-11-10, R062)

## Decision: **NONE on dev** (pre-registered rule `gotobi_fix.decide_b25`, applied exactly). **No LEAD.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or
p < 0.05); else NONE.
- mean +0.180 pips (< 1.0), CI (-0.552, 1.245) includes 0, t p 0.3224 (> 0.05) -> neither WEAK condition holds -> **NONE**.
- LEAD gate: condition 1 fails. Costs: SPEC 4 net -0.353, x1.5 -0.619 pips per event.

## Reading the result (no new numbers)
- Gotobi dates show no extra USD buying into the Tokyo fix in EUR/USD; if anything the gotobi mean is below the non-gotobi control
  (difference -0.231). The E011 all-date pre-fix effect (+0.32) is not concentrated on gotobi dates.
- Month-end gotobi (n 72, +2.639, CI includes 0) is a **post-hoc** subset read after the result. It is not a finding and is not queued
  as a new item on dev. It overlaps the month-end theme (B8, parked); any test of it would need its own pre-registration on fresh data
  and a reason in the decision log.
- The USD/JPY mechanism may simply not transmit to EUR/USD at this size; this test does not speak to USD/JPY.

## Next
Per methodology: B25 closed for this definition; no re-test on dev with other windows or day rules. Added to
knowledge/rejected_hypotheses.md. Next `ready` item: B26 (post-fix long 09:55 -> 10:55 Tokyo on gotobi dates, dev, 1 trial).
