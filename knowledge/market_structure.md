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

### 2026-11-10: Unexpected daily volume does not predict next-day direction (E033) [EXP]
- Dukascopy volume field usable on dev (0 zero/NaN bars). UV correlates with daily range (0.275) and |open-to-close move| (0.185);
  mean |R| 32 pips on low-UV dates vs 52 on high-UV dates.
- Next-day (20:00 -> 16:55 NY) low-UV reversal -2.034 pips, high-UV continuation -0.213, both NONE. See
  experiments/2026-11-10_E033_volume_reversal.

### 2026-11-10: Relative EU/US equity month-to-date return does not predict EUR/USD into the month-end fix (E034) [EXP]
- Dev 2015-2020, 71 month-ends, position -sign(EU50 minus US500 MTD return): pre-fix hour +1.731 pips, D-1 16:00 -> D 16:00 +3.354,
  both NONE; corr(S, move) about 0. Unconditional long EUR/USD on the same 71 month-ends: +3.076 (hour), +12.501 (day, CI (1.329, 24.105)).
- Descriptive only: long EUR/USD after US equities rose month-to-date, D-1 16:00 -> D 16:00, +23.082 (t p 0.0001), post-hoc and
  overlapping the unconditional drift. See experiments/2026-11-10_E034_month_end_hedging.

### 2026-11-10: Overnight (17:05 -> 07:00 NY) EUR/USD moves vs the NY-day return (E035) [EXP]
- Dev 2015-2020, 1,554 dates: a single overnight move does not predict 07:00 -> 16:55 NY (fade -0.285 pips, slope -0.005, NONE).
  SD overnight 35.5 pips, SD 07:00 -> 16:55 NY 45.4 pips; unconditional long 07:00 -> 16:55 NY +0.56 (not significant).
- Fading the 20-date sum of overnight moves: +2.695 pips per date (CI (0.47, 5.027), SIGNAL on dev, not yet confirmed on val; B34).
  See experiments/2026-11-10_E035_overnight_reversal.

### 2026-11-10 R078: val confirmation of the smoothed overnight fade (E036, val) [EXP]
- NONE on val 2021-01-21..2023-06-30: fading the 20-date sum of 17:05 -> 07:00 NY moves, held 07:00 -> 16:55 NY, n 616, +0.193 pips,
  CI (-2.683, 3.23), t p 0.456; SPEC 4 net -0.492. Supersedes the E035 entry above as the current reading: the dev SIGNAL is not
  confirmed and the line is closed. See experiments/2026-11-10_E036_overnight_reversal_val.

### 2026-11-10 R081: relative EU vs US equity returns and EUR/USD (E037, dev) [EXP]
- Same-day: corr(EU50 minus US500 log return, EUR/USD mid 16:00 -> 16:00 London) -0.228 on 1509 dev dates (EU outperformance with
  EUR weakness, Hau-Rey sign).
- Next day: no predictive power. -sign(daily) +1.268 pips (CI (-1.411, 3.942)), -sign(20-date) -0.88 (CI (-3.418, 1.868)), held
  16:05 London -> 16:00 London next date. See experiments/2026-11-10_E037_relative_equity.

### 2026-11-11 R084: EUR/USD into the 17:00 NY roll (E038, dev) [EXP]
- 16:25 -> 16:55 NY: SD 4.774 pips; unconditional long mean -0.282 (CI (-0.552, -0.061)); spreads median / p90 0.3 / 0.5 pips at
  16:25 NY and 0.5 / 1.0 at 16:55 NY.
- Continuation of the rest-of-day move (17:00 NY start of D -> 16:25 NY) into 16:25 -> 16:55: +0.255 pips signed, CI (0.023, 0.501)
  (WEAK, sub-cost). See experiments/2026-11-11_E038_roll_momentum.

### 2026-11-11 R087: EUR/USD around US Treasury coupon auctions (E039, dev) [EXP]
- 440 nominal Note/Bond auction events 2015-2020 (72-80 per year; competitive close 13:00 NY for 414, 11:30 NY for 24).
- Auction window T-10 -> T+10 min: SD 7.943 pips; share up 0.514. In 2019-2020 its sign agrees with the Treasury CFD window sign 59%
  of the time.
- The window sign does not predict EUR/USD to 16:00 NY next trading date (+1.655 pips, CI (-3.106, 7.394)) or 10 trading dates
  later (+1.426, CI (-11.651, 11.979)). See experiments/2026-11-11_E039_treasury_auction.

### 2026-11-11 R090: EUR/USD the day after FOMC statements (E040, dev) [EXP]
- 47 scheduled statements 2015-2020. Pre-statement drift (16:00 NY t-1 -> 13:55 NY t): mean +16.905 pips, mean |P| 31.746, up 66%
  of meetings (consistent with E013's FOMC-day USD weakness on dev).
- 02:00 -> 14:00 NY on t+1, signed against the drift: +2.623 pips, SD 61.879, CI (-14.684, 21.44); no reversal of the drift
  (slope +0.151, p 0.49). See experiments/2026-11-11_E040_post_fomc_reversal.

### 2026-11-11 R092: EUR/USD and daily WTI (E041, dev) [EXP]
- Dukascopy `lightcmdusd` CFD: valid 16:00 London quotes on both days for 98.72% of dev dates; daily log return SD 0.02372;
  11 dates with |O| > 0.10 (roll gaps / April 2020).
- Daily corr(WTI return, EUR/USD 16:00 -> 16:00 London same day) 0.0405: EUR/USD is barely oil-sensitive at daily frequency on dev.
- Next-day EUR/USD (16:05 -> 16:00 London) signed by the lagged WTI return: +2.306 pips, CI (-0.513, 5.184), NONE.
  See experiments/2026-11-11_E041_oil_lag.

### 2026-11-11 R095: EUR/USD and daily gold (E042, dev) [EXP]
- Dukascopy `xauusd`: valid 16:00 London quotes on both days for 98.97% of dev dates; daily log return SD 0.00852; no |G| > 0.10 dates.
- Daily corr(gold return, EUR/USD 16:00 -> 16:00 London same day) 0.4026: strong same-day co-move (common USD factor), unlike WTI (0.0405).
- Lagged corr(gold return, next-day EUR/USD 16:05 -> 16:00 London) 0.0058; signed by -sign(G): -1.407 pips, CI (-4.415, 0.939), NONE.
  corr(gold, WTI daily returns) on common dates 0.0329. See experiments/2026-11-11_E042_gold_lag.

### 2026-11-11 R098: EUR/USD 5-minute jumps (E043, dev) [EXP]
- Lee-Mykland (K 270, bipower, |L| > 5.395) plus |move| >= 5 pips: 2764 jumps on 445874 tested 5-min slots (2015-2020), median |jump|
  14.85 pips; busiest NY hours 08, 10, 09, 03. Release proxy 08:25-08:50 NY holds 13.5% of tested events.
- After a jump: t+5 -> t+10 signed by the fade +0.491 pips (CI (0.067, 0.946)); t+10 -> t+70 fade -0.693 pips, CI (-1.607, 0.251), NONE.
  See experiments/2026-11-11_E043_post_jump_reversal.

### 2026-11-11 R101: EUR/USD daily realized skewness (E044, dev) [EXP]
- RS of 5-min mid returns 18:00 -> 16:55 NY (median 275 returns): mean 0.0744, median 0.0226, SD 1.3169; corr with the daily return
  0.564, sign agreement 0.7666; 1-min vs 5-min RS sign agreement 0.8037. Next-day signed mean -0.183 pips, NONE.
  See experiments/2026-11-11_E044_realized_skew.

### 2026-11-11 R104: EUR/USD rejected touches of 00/50 levels (E045, dev) [EXP]
- 1195 first rejected touches (1562 dev trading dates); 1000 tradeable. Fade 60 min -0.71 pips (NONE); 15 min -0.259,
  120 min -1.429. In 83.1% of trades the close crosses the level within the hold. Control 23/73 fade +1.608 (descriptive).
  See experiments/2026-11-11_E045_round_touch_reversal.

### 2026-11-12 R111: EUR/USD daily return by FOMC-cycle week (E046, dev) [EXP]
- 20:00 NY -> 16:55 NY long mean by cycle week: -1 -0.717, 0 +4.218, 1 -7.167, 2 +3.272, 3 -0.831, 4 -1.328, 5 +8.182 (n 111),
  6 -3.257 (n 21). Even/odd partition (week 0 excluded) +1.152, NONE. See experiments/2026-11-12_E046_fomc_cycle.

### 2026-11-12 R126: EUR/USD after first touch of previous-day pivot R1/S1 (E047, dev) [EXP]
- 1349 first touches (1565 UTC dates), 1270 tradeable. Continuation 120 min -0.187 pips (NONE); 60 min +0.165, 180 min -0.231.
  R1 long -0.727, S1 short +0.351. Control levels at +-0.0023 behave the same. See experiments/2026-11-12_E047_pivot_touch.
