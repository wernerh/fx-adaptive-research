# Agent decision log

Why each run chose what it did, and any judgement calls.

### 2026-11-07 R000
- **Decision:** first experiment is E001 (cost-free directional signal test), not a strategy backtest.
- **Reason:** cheapest way to test the core hypothesis; avoids tuning strategies on noise.
- **Decision:** added the unconditional benchmark to E001 after the literature review found documented time-of-day drift and fixing effects.
- **Decision:** default sessions anchored to local exchange clocks (Tokyo / London / New York), see SPEC 2.
