# Agent decision log

Why each run chose what it did, and any judgement calls.

### 2026-11-07 R000
- **Decision:** first experiment is E001 (cost-free directional signal test), not a strategy backtest.
- **Reason:** cheapest way to test the core hypothesis; avoids tuning strategies on noise.
- **Decision:** added the unconditional benchmark to E001 after the literature review found documented time-of-day drift and fixing effects.
- **Decision:** default sessions anchored to local exchange clocks (Tokyo / London / New York), see SPEC 2.

### 2026-11-07 R001
- **Decision:** ran E001 via GitHub Actions; the workspace cannot reach Dukascopy and the user is away from their PC.
- **Decision:** applied the pre-registered rule exactly -> NONE. Did not run unregistered variants to find a positive result.
- **Decision:** deprioritised S002/S003 without formally rejecting them (statuses unchanged); their core premise is in rejected_hypotheses.md.
