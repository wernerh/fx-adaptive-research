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

### 2026-11-07: E006: no early-US directional bias either
- **[EXP]** Same 7 predictors vs 08:00-09:00 and 08:35-09:30 NY: no signal (min p 0.16, all Bonferroni 1.0).
- **[EXP]** Typical |move| in the first US hour is about 13-14 pips; a 1-pip cost is small relative to the move. The problem is direction, not costs.

### 2026-11-07: US-window move size vs pre-US ranges (E008) [EXP]
- Mean |EUR/USD 08:00-12:00 NY| on dev ~25 pips; ~13 pips for 08:00-09:00 NY.
- Beyond prior ATR, Asia range adds a tiny positive effect (partial IC ~0.05-0.06) and London range adds nothing. See experiments/2026-11-07_E008_vol_timing.
