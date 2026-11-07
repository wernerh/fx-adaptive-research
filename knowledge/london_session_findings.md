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
