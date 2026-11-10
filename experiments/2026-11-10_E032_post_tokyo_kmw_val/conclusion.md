# E032 Conclusion (2026-11-10, R067)

## Decision: **NONE on val** (pre-registered rule `post_tokyo_kmw.decide_b27`, applied exactly). **No LEAD.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or
p < 0.05); else NONE; < 200 dates -> NONE.
- n 636 (>= 200). mean -0.534 pips (not > 0) -> neither SIGNAL nor WEAK -> **NONE**. t p 0.830, CI (-1.606, 0.669).
- Not an OOS candidate (no SIGNAL; SPEC 4 net -1.106, x1.5 -1.392). LEAD gate fails at condition 1.

## Reading the result (no new numbers)
- The published post-Tokyo-fix USD depreciation (KMW, 1999-2019, 20:55 -> 02:00 ET) does not appear in EUR/USD on val 2021-2023:
  the sign is opposite to the hypothesis in every year and in both DST regimes. The dev-implied ~+1.2 pips (E009 cells) did not carry over.
- The first hour after 20:55 NY is flat on val (+0.033), unlike the dev post-fix hour (E011 +0.785, WEAK).

## Next
Per methodology: NONE -> B27 closed; no re-test with other windows, clocks, subsets or exits. Added to
knowledge/rejected_hypotheses.md. No `ready` item remains: next run is a backlog refill.
