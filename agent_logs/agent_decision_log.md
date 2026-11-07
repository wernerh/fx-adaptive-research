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

### 2026-11-07 R002
- **Decision:** ran E004 and E006 together (user request), both pre-registered and committed before the run (0a57f09).
- **Decision:** rejected S001 v0.1 and did not run val, per the rule.
- **Decision:** did NOT follow up the exploratory `lon_false_break_fade` 08:00-09:00 observation. It would be trial 23 on dev, chosen after seeing the data.
- **Recommendation for R003:** pivot away from session-price predictors. Candidates: (a) US data release reaction (S005; needs a historical calendar with timestamps); (b) time-of-day volatility timing for entry windows (predicting *when* to trade, not direction); (c) London-fix reversal (published mechanism, Krohn et al. 2024).

### 2026-11-07 R004 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42395207715) already recorded in 7cc4427.
- **Decision:** took top `ready` backlog item B1 -> E007 London 4pm fix reversal, dev only, 4 trials. Pre-registered rule in experiments/2026-11-07_E007_london_fix_reversal/methodology.md, committed before the run.
- **Reason:** published mechanism (Krohn, Mueller & Whelan 2024; Evans 2018), a different information source from the three failed session-price tests, and data already available.

### 2026-11-07 R005 (unattended)
- **State:** research-batch run 42400981266 completed; outputs (0db6d13) not yet recorded -> Collect step.
- **Decision:** applied E007 rule exactly -> NONE on all 4 tests; B1v not queued. No lead; no notification.
- **Decision:** logged the wrong-sign month-end post-fix result as exploratory backlog B8, `parked` (not `ready`): post hoc, n=72, binomial n.s.

### 2026-11-07 R006 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42400981266) already recorded in eece61e.
- **Decision:** took top `ready` backlog item B2 -> E008 volatility timing, dev only, 4 trials (2 predictors x 2 outcomes).
- **Judgement call (before any data):** decision statistic changed from the draft "IC of range/ATR vs |move|" to partial Spearman given prior ATR, because the random-walk test showed a shared-denominator bias (~+0.04). Rule is stricter (adds CI lower > 0). Recorded in methodology.md.

### 2026-11-07 R007 (unattended)
- **State:** research-batch run 42411061401 completed; outputs (0a4f98d) not yet recorded -> Collect step.
- **Decision:** applied E008 rule exactly -> NOT_USEFUL on all 4 tests; B2v not queued. No lead; no notification.
- **Next:** top `ready` backlog item is B3 (hourly return profile scan, exploratory, dev only).
