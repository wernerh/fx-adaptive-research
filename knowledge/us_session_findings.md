# US session findings

US session continuation and reversal versus earlier sessions, economic release effects and entry windows.

Entries are append-only and dated. To change a conclusion, add a new entry that references the old one.
Evidence labels: **[PUB]** published research, **[BT]** our backtest, **[EXP]** our experiment, **[ASSUMPTION]** untested.

## Entries

### 2026-11-07: repository initialised
- No data has been analysed yet. Nothing in this file is a finding.

### 2026-11-07: E001: no directional bias from earlier sessions (whole US morning)
- **[EXP]** Across 1,556 dev and 637 val days, none of seven Asian/London predictors predicted the sign of the 08:00-12:00 NY return (hit rates 47.5-52.1%, all CIs include 50%).
- **[EXP]** No unconditional drift in the window either: mean +0.59 pips (dev) and +0.71 pips (val), CIs include zero.
- Open: shorter windows (08:00-09:00), event-day exclusion, pre/post 4pm fix split.
