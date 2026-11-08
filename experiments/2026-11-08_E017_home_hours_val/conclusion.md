# E017 Conclusion (2026-11-08, R030)

## Decision: **WEAK on val** (pre-registered B1 rule, `fixes.decide(res, n_trials=1)`, applied exactly). **No lead, not a candidate.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- Mean +2.179 pips (> 1) and CI lower 0.001 (> 0, barely), but binomial p 0.4512 >= 0.05 -> not SIGNAL -> **WEAK**.
- Per the methodology, WEAK means the hypothesis is rejected for these windows; no re-test with other hours on val.
- Cost gate also fails: SPEC 4 net -0.382 pips, costs x1.5 -1.663 pips. Even a SIGNAL would have been "mid drift, not tradable".

## Reading the result (cautions, no new numbers)
- The mid mean comes mostly from the European short leg (+1.776, CI includes 0); the US long leg is near zero (+0.403).
- Hit rate is ~0.52: the mean is driven by a few large days, not a consistent daily drift.
- The 16:59 NY exit sits in the rollover spread widening (median 3.0 pips vs 0.3 elsewhere); that single exit eats most of the gross edge.
  An earlier US exit would be a different window and a new trial, and only on fresh data (val now seen for this hypothesis).
- Consistent with the effect documented to 2007 (Breedon & Ranaldo) being small or gone net of costs in 2021-2023.

## Next
B14 closed (recorded in knowledge/rejected_hypotheses.md). No `ready` items remain in research/backlog.md (B6/B12/B13 blocked,
B7/B8 parked) -> next run is a refill pass (literature/evidence, verified links only, 2-3 new items, prefer inputs already in the repo).
