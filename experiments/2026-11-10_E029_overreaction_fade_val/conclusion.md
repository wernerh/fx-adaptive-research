# E029 Conclusion (2026-11-10, R059)

## Decision: **NONE on val** (pre-registered rule `overreaction_fade.decide_b24`, applied exactly). **No LEAD.**
Rule: fewer than 10 tested events -> "insufficient sample" -> NONE; otherwise SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0
AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- Only 4 of 34 events were tested (19 skipped by the pre-registered 2.0-pip entry-spread filter at 17:05 NY, 9 Fridays, 2 missing
  entry) -> insufficient sample -> **NONE**. The mean of the 4 (+6.05 mid) is not evidence and is not interpreted.
- LEAD gate: a val-only test cannot be a LEAD (no clean dev pass), and condition 1 fails anyway.

## Reading the result (no new numbers)
- The test was not informative: it failed on tradability, not on the return. The 17:05 NY entry sits inside the daily rollover
  spread widening, and on large-move days that widening is bigger (median entry spread of events 3.6 pips vs the 2.0-pip SPEC 4 cap).
  The power note expected 15-35 tested events; it did not account for the spread filter. This is a design lesson, not a market finding.
- The k 1.5 descriptive (n 12, +2.437, CI includes 0) and the non-event control (+1.474) give no sign of an effect large enough to
  have passed with the planned sample either.
- Rule 7 (no trade is a valid result) applies: the spread filter is not loosened and the entry time is not moved after seeing this.

## Next
Per methodology: B24 closed for this definition; no re-test with other k, windows, hours, exits or entry times on val. Added to
knowledge/rejected_hypotheses.md (as untestable at this entry time, not as a rejected effect). No `ready` backlog item -> refill next.
