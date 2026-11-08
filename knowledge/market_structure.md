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

### 2026-11-08: NY 18:00 hour drift does not confirm on val (E012) [EXP]
- Supersedes the "val tests B9/B10 queued" note in the 2026-11-07 hourly drift map entry above.
- Val: trading-date Wed +0.65 pips (WEAK), Thu +0.94 pips (NONE), CIs include 0. Median entry spread at 18:00 NY 1.5-1.7 pips; net negative at bid/ask, SPEC 4 and costs x1.5. Treat the post-roll mid drift as untradable. See experiments/2026-11-08_E012_ny18_drift_val.

### 2026-11-08: FOMC statement-day USD weakness, dev SIGNAL (E013) [EXP]
- Long EUR/USD from 16:00 NY on the prior business day to 16:00 NY on scheduled FOMC statement days, dev 2015-2020: n 47, mean +21.28 pips, median +28.3, hit 0.617, block-boot CI (2.75, 38.16), t p 0.029 -> SIGNAL under the pre-registered rule. Same window on non-FOMC weekdays: -0.39 pips (flat).
- Consistent with the published FOMC-day short-USD premium [PUB: Mueller, Tahbaz-Salehi & Vedolin 2017, DOI 10.1111/jofi.12499]. **Not confirmed**: val test B11v pending; not a lead and not a confirmed pattern. See experiments/2026-11-08_E013_fomc_day_drift.

### 2026-11-08: FOMC statement-day USD weakness not confirmed on val (E014) [EXP]
- Supersedes the "val test B11v pending" note in the 2026-11-08 E013 entry above.
- Val 2021-01-21..2023-06-30: n 20, mean +19.99 pips, hit 0.70, block-boot CI (-9.53, 51.02), t p 0.115 -> NONE under the unchanged E013 rule. Point estimate similar to dev but val (20 meetings) is underpowered. Not a confirmed pattern; no lead. See experiments/2026-11-08_E014_fomc_day_val.
