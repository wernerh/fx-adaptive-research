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
