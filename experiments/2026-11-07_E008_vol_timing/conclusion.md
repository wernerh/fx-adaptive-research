# E008 Conclusion (2026-11-07)

## Decision: **NOT_USEFUL** (pre-registered rule, applied exactly)
Rule per test: USEFUL if partial IC > 0.10 AND p < 0.01 AND block-bootstrap CI lower > 0. No test met the IC or p threshold.
**B2v (val) is not queued.**

## What we learned
- Pre-US session ranges carry almost no information about the size of the US move **beyond the prior-ATR regime**.
  The raw-pips correlations (0.14-0.21) are what volatility clustering alone produces; once prior ATR is controlled, they
  collapse to 0.06/0.05 (Asia) and ~0 (London).
- The Asia partial IC is small but its bootstrap CI excludes 0 (lower bound ~0.01), i.e. a probably-real but economically
  tiny effect (high vs low Asia tercile: ~3 pips on a ~25-pip mean |US move|). Below the pre-registered 0.10 bar; not used.
- A London range that is large for the regime does **not** foreshadow a larger US move (tercile means even slightly decline).
- Practical implication: for any later short-duration strategy, prior ATR is a sufficient volatility filter; adding session
  ranges as a "when to trade" filter is not supported.

## Next
B2 done. Next ready backlog item: B3 (hourly return profile scan, exploratory, dev only).
