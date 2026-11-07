# EUR/USD market structure

Session characteristics, liquidity and volatility patterns, fixings, and macro drivers relevant to EUR/USD.

Entries are append-only and dated. To change a conclusion, add a new entry that references the old one.
Evidence labels: **[PUB]** published research, **[BT]** our backtest, **[EXP]** our experiment, **[ASSUMPTION]** untested.

Session definitions used everywhere are in docs/SPEC.md section 2. Do not use any others.

## Entries

### 2026-11-07: repository initialised
- No data has been analysed yet. Nothing in this file is a finding.

### 2026-11-07: literature review, first pass (see research/academic_studies.md)
- **[PUB]** Time-of-day drift: currencies tend to weaken in their own trading hours (Breedon & Ranaldo 2013). Implication: EUR/USD may have an unconditional US-hours drift; conditional signals must beat it.
- **[PUB]** Fixing reversals: USD strengthens into the Tokyo, ECB and London fixes and weakens after (Krohn, Mueller & Whelan 2024). The London fix (11:00 NY) and ECB fix (about 08:15 NY) sit inside our US window.
- **[PUB]** 08:30 NY US data produces near-immediate jumps (Andersen et al. 2003).
- **[PUB]** Stop-loss clusters just beyond round numbers can accelerate breaks; take-profits at round numbers can cause reversals (Osler 2003).
- **[PUB]** Intraday FX technical rules showed no excess return after realistic costs (Neely & Weller 2003); known rules decay (Neely, Weller & Ulrich 2009).
- Net: the mechanisms are documented; a cost-surviving cross-session EUR/USD edge is **not**. Prior: skeptical.

### 2026-11-07: hourly drift map (E009, exploratory, dev) [EXP]
- Time-of-day mean drift in EUR/USD mid is < 1 pip/hour in almost all 192 cells (UTC hour, NY hour, weekday x NY hour, month-end x NY hour).
- Exception: the NY 18:00-19:00 hour (first full hour after the 17:00 roll) drifts up on every weekday (pooled +0.87 pips, t p 3e-7); trading-date Wed/Thu exceed 1 pip (+1.33/+1.24). Possibly a spread-normalisation artifact; val tests B9/B10 queued. See experiments/2026-11-07_E009_hourly_profile.
