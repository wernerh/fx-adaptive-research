# E039 Conclusion (2026-11-11, R087)

## Decision: **NONE / NONE on dev** (pre-registered rule `treasury_auction.decide`, applied exactly). **Not a LEAD.**
Rule per arm: < 150 tested events -> NONE; SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND one-sided t p < 0.025;
WEAK if mean > 0 and (CI lower > 0 or t p < 0.025); else NONE. Calendar gate passed (50-110 per year, parsed share 1.0).
- B40 (10-date hold): n 431, mean +1.426, CI (-11.651, 11.979), t p 0.4334 -> **NONE**.
- B41 (1-date hold): n 437, mean +1.655, CI (-3.106, 7.394), t p 0.2733 -> **NONE**.
- LEAD condition 1 fails in both arms. No notification.

## Reading the result (cautions, no new numbers)
- The EUR/USD auction-window move does not predict the next-day or 10-day EUR/USD return. The means are above 1 pip, but with SDs of
  57 and 176 pips they are indistinguishable from zero, as is the non-auction control.
- This tests a **proxy** (EUR/USD's own window move), not the paper's Treasury-futures shock. On the 2019-2020 subset where the
  Treasury CFD exists, its window sign agrees with EUR/USD's only 59% of the time, and the CFD sign did not help either (descriptive,
  n ~140). The NONE therefore does not refute Krohn-Vala-Uthemann-Yang; it says the proxy has no usable edge on dev.
- The negative long-tenor slice (B40 long, CI upper -0.239) is a post-hoc subset of a NONE result and must not be turned into a dev
  re-test (lesson R076).

## Next
Per methodology: B40 and B41 closed NONE; B42 (val confirmation) closed unearned, 0 trials. No re-test on dev with other windows,
holds, tenors or the CFD sign. Both arms go to rejected_hypotheses.md. No other `ready` backlog item -> next run is a backlog refill.
