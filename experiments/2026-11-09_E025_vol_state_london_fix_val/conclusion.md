# E025 Conclusion (2026-11-09, R049)

## Decision: **NONE on val** (pre-registered rule `vol_state_london.decide_b20`, applied exactly). **No LEAD.** E024 not confirmed.
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean +0.582 pips (< 1.0), CI (-1.992, 3.14) includes 0, one-sided t p 0.3687 (>= 0.05) -> neither WEAK condition holds -> **NONE**.
- LEAD gate: condition 2 (val pass) fails; the cost gate also fails (x1.5 net -0.197).

## Reading the result (no new numbers)
- The val mean on high-vol dates (+0.582) is close to zero and close to the normal-date control (-0.053) and all val dates (+0.172).
  Excluding the 4 FOMC-day events it is -0.298. The dev SIGNAL in E024 (+2.983, CI lower 0.566) did not carry over.
- Same pattern as the sibling B19 line (E022 dev SIGNAL -> E023 val NONE): two vol-conditioned fix-window dev signals among ~238
  trials, neither replicated. The dev controls had already hinted that the conditioning was not the source.
- The prior expectation written before data (low-to-moderate; val likely WEAK at best) held.

## Next
Per methodology: B20 line closed for this definition; no re-test with other percentiles, windows, vol measures or blocks. Added to
knowledge/rejected_hypotheses.md. No `ready` backlog item remains -> next run is a refill pass (protocol step 4).
