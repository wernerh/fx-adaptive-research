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

### 2026-11-08: FOMC statement days (E013, dev) [EXP]
- On scheduled FOMC statement days the 16:00-to-16:00 NY EUR/USD return averaged +21.28 pips on dev (SIGNAL, 1 trial); the 13:00-16:00 NY part (statement + press conference) averaged +8.02 pips (n.s., descriptive). Per-meeting SD 75 pips vs 56 on other days. Val confirmation B11v pending. See experiments/2026-11-08_E013_fomc_day_drift.

### 2026-11-08: FOMC statement days on val (E014) [EXP]
- Supersedes "Val confirmation B11v pending" in the E013 entry above. Val: 16:00-to-16:00 NY mean +19.99 pips (n 20, NONE: CI includes 0, p 0.115); 13:00-16:00 NY sub-window +17.47 (descriptive, n.s.). See experiments/2026-11-08_E014_fomc_day_val.

### 2026-11-09 R052: post-08:30 NY release-window continuation, calendar-free (E026, dev) [EXP]
- NONE on dev: after a large 08:30 -> 08:45 NY move (abs > rolling p90 of 60 dates), following it 08:45 -> 10:45 NY averaged -0.42 pips
  (n 169, CI -5.278 to 2.488, t p 0.564); non-event control -0.465. No continuation at this horizon. See
  experiments/2026-11-09_E026_release_continuation.

### 2026-11-09 R057: intraday continuation on overreaction days, 12:00 -> 16:30 NY (E028, dev) [EXP]
- NONE on dev: on dates whose 17:00 NY open -> 12:00 NY move lay outside the rolling mean +/- 2 SD (60 dates), following it from
  12:00 to 16:30 NY averaged +1.061 pips (n 74, CI -5.625 to 8.569, t p 0.390); non-event long control +1.108. See
  experiments/2026-11-09_E028_overreaction_day.
