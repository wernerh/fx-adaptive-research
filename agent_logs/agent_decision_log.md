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

### 2026-11-07 R008 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42411061401) already recorded in 022a6c2.
- **Decision:** took top `ready` backlog item B3 -> E009 hourly return profile scan, exploratory, dev only, 192 cells (all counted as trials).
- **Rule fixed before data:** CANDIDATE needs |mean| >= 1 pip, bootstrap CI excluding 0, t p < 0.05/192 and sign p < 0.05; at most 3 candidates become val-only 1-trial backlog items. No lead can come from this scan alone.

### 2026-11-07 R009 (unattended)
- **State:** research-batch run 42420473476 completed; outputs (89082ec) not yet recorded -> Collect step.
- **Decision:** applied E009 rule exactly (re-checked from the JSON) -> CANDIDATES: Wed_ny_18, Thu_ny_18 (both long). Per the pre-registered follow-up rule, added B9/B10 (val only, 1 trial each) at the bottom of the backlog as `ready`; not re-ranked. Exploratory scan, so no lead; no notification.
- **Next:** top `ready` backlog item is B4 (ECB fix, dev).

### 2026-11-08 R010 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42420473476) already recorded in 56295b1.
- **Decision:** took top `ready` backlog item B4 -> E010 ECB 14:15 CET fix reversal, dev only, 2 trials (pre short, post long), E007 rule with n_trials=2.
- **Noted before data:** post window contains 08:30 NY US releases on most days; a SIGNAL would need a release-day split at val before any lead claim.

### 2026-11-08 R011 (unattended)
- **State:** research-batch run 42429506649 completed; outputs (cda15e9) not yet recorded -> Collect step.
- **Decision:** applied E010 rule exactly -> WEAK overall (pre WEAK: +0.76 pips < 1.0 bar, p 0.53; post NONE). WEAK does not go to val; B4v not queued. No lead; no notification.
- **Next:** top `ready` backlog item is B5 (Tokyo fix, E011).

### 2026-11-08 R012 (unattended)
- **State:** no research-batch run queued or in progress; last batch (42429506649) already recorded in 03e47f7.
- **Decision:** took top `ready` backlog item B5 -> E011 Tokyo 09:55 JST fix reversal, dev only, 2 trials (pre short, post long), E007 rule with n_trials=2.
- **Added before data:** descriptive bid/ask cost check (median entry spread, net, net at costs x1.5), because B5 flags wider Asian-hours spreads. Not part of the decision rule. Gotobi-day subset deliberately not tested (would add trials).
