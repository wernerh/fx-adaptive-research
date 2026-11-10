# E036 Conclusion (2026-11-10, R078)

## Decision: **NONE on val** (pre-registered rule `overnight_reversal.decide_b34`, applied exactly). **Not a LEAD.**
Rule: < 500 tested dates -> NONE; SIGNAL if mean > 1.0 pip AND block-bootstrap (block 20) CI lower > 0 AND one-sided t p < 0.05;
WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- n 616 (>= 500), mean +0.193 (not > 1.0), CI lower -2.683 (not > 0), t p 0.456 (not < 0.05) -> **NONE**.
- LEAD condition 2 (val confirmation) fails; cost gate also fails (SPEC 4 net -0.492, x1.5 -0.834). No notification.

## Reading the result (cautions, no new numbers)
- E035's B33 dev SIGNAL (+2.695 pips, p 0.0093) does not confirm on val: the val mean is about zero and below costs. This matches the
  dev decay already visible in 2019-2020 (below +1 pip) and the prior expectation written before data.
- All four dev SIGNALs in the project (E013, E022, E024, E035) have now failed their val confirmation (E014, E023, E025, E036). Consistent with chance at ~253 trials.
- The high-|O20| tercile is positive on val (+5.664) as on dev (+4.304), but it is descriptive, was not pre-registered as a trial, and
  the low/mid terciles are negative on val. It must not be turned into a test on val; a tercile-restricted version would need fresh
  data and its own pre-registration with a human decision.

## Next
Per methodology: B33/B34 line closed; no re-test with other smoothing lengths, windows or blocks. E035 B33 + E036 go to
rejected_hypotheses.md. No other `ready` backlog item -> next run is a backlog refill.
