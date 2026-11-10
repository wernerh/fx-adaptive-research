# Asian session findings

Asian range, volatility, momentum and how Asian behaviour relates to London and US sessions.

Entries are append-only and dated. To change a conclusion, add a new entry that references the old one.
Evidence labels: **[PUB]** published research, **[BT]** our backtest, **[EXP]** our experiment, **[ASSUMPTION]** untested.

## Entries

### 2026-11-07: repository initialised
- No data has been analysed yet. Nothing in this file is a finding.

### 2026-11-07: E001
- **[EXP]** Asian-session return sign does not predict the US-morning direction (dev hit rate 51.5%, val 50.8%, n.s.).

### 2026-11-08: Tokyo 09:55 JST fix (E011, dev)
- **[EXP]** WEAK. Pre-fix hour 08:55-09:55 Tokyo: USD-up +0.32 pips signed (hit 0.530, p 0.021, CI includes 0). Post-fix hour 09:55-10:55 Tokyo: USD-down +0.79 pips signed (hit 0.539, p 0.003, CI 0.32-1.17), below the 1-pip bar. Descriptive post net at bid/ask +0.48 pips (median spread 0.2). Dev only; not sent to val. See experiments/2026-11-08_E011_tokyo_fix_reversal.

### 2026-11-10 R059: overnight fade after a 2-SD NY day (E029, val) [EXP]
- NONE (insufficient sample): 4 of 34 events tradable; the 17:05 NY entry spread exceeded 2.0 pips on 19 events (median event entry
  spread 3.6 pips). Nothing learned about the return; the roll-hour spread is the binding constraint. See
  experiments/2026-11-10_E029_overreaction_fade_val.

### 2026-11-10 R062: gotobi dates and the pre-Tokyo-fix hour (E030, dev) [EXP]
- NONE: short 08:55 -> 09:55 Tokyo on 458 gotobi dates, mean +0.180 pips, CI (-0.552, 1.245), t p 0.322; below the non-gotobi control
  (+0.411). The E011 all-date pre-fix effect is not concentrated on gotobi dates in EUR/USD. Month-end gotobi subset (n 72, +2.639,
  CI includes 0) is post-hoc only. See experiments/2026-11-10_E030_gotobi_tokyo_fix.
