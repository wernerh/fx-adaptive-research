# London session findings

London open behaviour, Asian range breaks, false breakouts and continuation versus reversal.

Entries are append-only and dated. To change a conclusion, add a new entry that references the old one.
Evidence labels: **[PUB]** published research, **[BT]** our backtest, **[EXP]** our experiment, **[ASSUMPTION]** untested.

## Entries

### 2026-11-07: repository initialised
- No data has been analysed yet. Nothing in this file is a finding.

### 2026-11-07: E001: London structure carries no US-morning information
- **[EXP]** London return sign, break side, held break and false-break fade showed no predictive power for the US morning (E001).
- **[EXP]** London breaks the Asian range on about 97% of days (`lon_break_side` coverage: dev 0.966, val 0.972) and breaks both sides on a subset. A plain "break" is close to universal, so it carries little information by itself. The held-break and false-break splits were about 2/3 and 1/3 of days.

### 2026-11-07: E004: breakouts of the Asian range do not continue over 60 minutes (dev 2015-2020)
- **[BT]** First London close outside the Asian range, traded in the break direction: 1,344 trades, 45.8% wins at 1R, -0.68 pips/trade net, -0.48 pips with spread only.
- **[BT]** Average MFE 9.35 pips < average MAE 9.87 pips. Median hold = 60-minute time stop.

### 2026-11-07: London 4pm fix (E007, dev)
- NONE. 15:00-16:00 London is volatile (mean |ret| 13.3 pips; 19.7 at month end) but has no reliable direction. See experiments/2026-11-07_E007_london_fix_reversal.

### 2026-11-08: ECB 14:15 CET fix (E010, dev)
- WEAK. Pre-fix hour 13:15-14:15 Berlin: USD-up drift +0.76 pips (CI excludes 0, but hit rate 0.508); post-fix hour: nothing (+0.29). Sub-cost either way. See experiments/2026-11-08_E010_ecb_fix_reversal.

### 2026-11-09 R043: pre-ECB-fix window 02:00-08:15 NY after high-range days (E022, dev) [EXP]
- SIGNAL on dev (marginal): short EUR/USD 02:00 -> 08:15 NY on dates after a prior-date range > rolling p67, n 473, +3.646 pips,
  CI (0.011, 7.751), t p 0.0133; normal-date control +1.731 (CI incl 0). Not confirmed; val confirmation B19v pending. See
  experiments/2026-11-09_E022_vol_state_ecb_fix.

### 2026-11-09 R045: val confirmation of the pre-ECB-fix window after high-range days (E023, val) [EXP]
- NONE on val: n 204, +1.197 pips, CI (-3.144, 5.919), t p 0.304; normal val dates +1.15. Supersedes the R043 entry above as the
  current reading: E022's dev SIGNAL is not confirmed and the line is closed. See experiments/2026-11-09_E023_vol_state_ecb_fix_val.
