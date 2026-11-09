# Research backlog

Ordered by priority. Status: `ready` | `running` | `done` | `blocked` | `parked`.
Autonomous runs take the top `ready` item (docs/AUTONOMOUS_PROTOCOL.md). Add items at the bottom; re-rank only with a
reason in agent_logs/agent_decision_log.md. Dev = 2015-01-01..2020-12-31, val = 2021-01-21..2023-06-30, OOS locked.

Trial count so far on dev: **232** (E001: 7, E006: 14, E004: 1, E007: 4, E008: 4, E009: 192 exploratory cells, E010: 2, E011: 2, E013: 1, E018: 1, E019: 1, E020: 1, E021: 1, E022: 1). Val-only trials: **5** (E012: 2, E014: 1, E017: 1, E023: 1). Total registered trials: **237**. Update after every experiment. (R045: E023 ran, val +1. R044: E023/B19v pre-registered, 1 val trial counted when it runs. R043: E022 ran, dev +1; B19v added, 0 trials until pre-registered. R042: E022/B19 pre-registered, 1 dev trial counted when it runs. R041: refill added B19, B20: 0 trials until pre-registered. R040: E021 ran, dev +1. R039: E021/B18 pre-registered, 1 dev trial counted when it runs. R038: E020 ran, dev +1. R037: E020/B17 pre-registered, 1 dev trial counted when it runs. R036: refill added B17, B18: 0 trials until pre-registered. R035: E019 ran, dev +1. R034: E019/B16 pre-registered, 1 dev trial counted when it runs. R033: E018 ran, dev +1. R032: E018/B15 pre-registered, 1 dev trial counted when it runs. R031: refill added B15, B16: 0 trials until pre-registered. R030: E017 ran, val +1. R029: E017/B14 pre-registered, 1 val trial counted when it runs. R028: E016/B13 blocked after second CME fetch failure, 0 trials. R027: E016 phase-1 re-fetch queued, 0 trials. R026: E016/B13 pre-registered, 1 dev trial counted when phase 2 runs. R025: refill added B13, B14: 0 trials until pre-registered. R023: E015/B12 pre-registered, 1 dev trial counted when phase 2 runs. R022: E014 ran, val +1. R020: E013 phase 2 ran, dev +1. R016 refill added B11, B12: 0 trials until pre-registered. R017: E013/B11 pre-registered, 1 dev trial counted when phase 2 runs.)

---

### B1: London 4pm fix reversal (signal test, dev) → E007 · `done` (2026-11-07: NONE, B1v not earned)
- **Mechanism [PUB]:** USD appreciates into the WM/Reuters 4pm London fix and depreciates after (Krohn, Mueller & Whelan 2024, JF); very volatile and negatively autocorrelated around the fix, strongest at month end (Evans 2018, JBF).
- **Test:** per trading day, EUR/USD mid return in `pre` = 15:00-16:00 Europe/London and `post` = 16:00-17:00 Europe/London (use `outcomes.window_outcome`). Predictions: pre < 0 (USD up), post > 0.
  Also report the month-end subset (last trading day of the month) separately as a pre-registered secondary.
- **Decision rule (draft):** SIGNAL if, on dev, mean signed return (short pre / long post) > 1.0 pip with a block-bootstrap 95% CI excluding 0 and binomial p < 0.05/4 (4 trials: pre, post, pre-ME, post-ME). Then queue a val confirmation (B1v).
- **Data:** available.

### B2: Volatility timing: when to trade (descriptive + signal test, dev) → E008 · `done` (2026-11-07: NOT_USEFUL, B2v not earned)
- **Mechanism [PUB]:** activity and volatility follow regional hours (Ito & Hashimoto 2006); announcement surprises cause jumps (Andersen et al. 2003).
- **Test:** do Asian range/ATR and London range/ATR predict the absolute US-window move |08:00-12:00 NY| and the first-hour |08:00-09:00|? Spearman IC and tercile means. Not a direction test; it informs *when* short-duration strategies should trade.
- **Decision rule (draft):** USEFUL if Spearman IC > 0.10 with p < 0.01 on dev and same sign in val (val as B2v). A useful result is not a lead by itself; it becomes a filter for later strategy tests.
- **Data:** available.

### B3: Hourly return profile scan (exploratory, dev only) → E009 · `done` (2026-11-07: CANDIDATES Wed_ny_18, Thu_ny_18 -> B9, B10)
- **Purpose:** map the mean EUR/USD mid return by hour of day (UTC and New York), weekday x hour, and month-end x hour on **dev only**, to generate hypotheses. Label everything exploratory. Any hypothesis found must be pre-registered and confirmed on **val** before it counts. Count every hour cell as a trial in the hypothesis it spawns.
- **Data:** available.

### B4: ECB reference-rate reversal (signal test, dev) → E010 · `done` (2026-11-08: WEAK, pre +0.76 pips; B4v not earned)
- **Mechanism [PUB]:** as B1, for the ECB fix (14:15 CET). Windows: 13:15-14:15 and 14:15-15:15 Europe/Berlin.
- **Decision rule (draft):** as B1, 2 trials.

### B5: Tokyo fix (signal test, dev) → E011 · `done` (2026-11-08: WEAK, post +0.79 pips hit 0.539, below 1-pip bar; B5v not earned)
- **Mechanism [PUB]:** as B1, Tokyo fix 09:55 JST. Windows: 08:55-09:55 and 09:55-10:55 Asia/Tokyo. Asian-hours spreads are wider, so check costs carefully.

### B6: US data release reaction (strategy) → (ID assigned when unblocked; E012 went to B9/B10) · `blocked`
- **Mechanism [PUB]:** announcement surprises move FX within minutes (Andersen et al. 2003).
- **Blocked on:** a historical economic calendar with UTC timestamps, actual and consensus values (2015+). A refill pass should find a source the GitHub runner can download, and document licence/terms.

### B7: London false-break fade, 08:00-09:00 NY (signal test, pre-registered) · `parked`
- **Origin:** exploratory note in E006 (+1.4/+1.6 pips dev/val, n.s.). Already seen on val, so a fair test needs fresh data: **park** until the human decides whether OOS may be used for it.

### B8: Month-end post-fix USD continuation (signal test, val only) · `parked`
- **Origin:** post-hoc observation in E007 (dev): post-fix 16:00-17:00 London on month-end days, EUR/USD signed-long mean -4.51 pips,
  bootstrap CI (-7.19, -1.88), but hit rate 0.417 (binom p = 0.19), n = 72; opposite to the pre-registered direction.
- **Test if un-parked:** short EUR/USD 16:00-17:00 London on last trading day of month, **val block only**, 1 trial; SIGNAL rule as B1
  (mean > 1.0 pip, CI lower > 0, binom p < 0.05). Val has only ~30 month ends, so power is low.
- **Why parked:** chosen after seeing dev, wrong-sign vs published mechanism, tiny n, and val would be its only clean test. Un-park only with a reason in the decision log.

### B9: NY 18:00 hour drift on trading-date Wednesday (signal test, val only, dev-derived) → E012 · `done` (2026-11-08: WEAK on val, +0.65 pips, CI includes 0; cost gate fails)
- **Origin:** E009 CANDIDATE (exploratory, dev): Wed_ny_18 mean +1.333 pips, block-boot CI (0.703, 2.055), t p 2e-5, n 312. Selected from 192 cells.
- **Mechanism [hypothesis, unverified]:** post-roll (17:00 NY) liquidity rebuild / early Asia-Pacific flow; risk that it is a spread-normalisation artifact of mid quotes.
- **Test:** long EUR/USD mid return over the 18:00-19:00 America/New_York hour on trading dates that are Wednesdays (`sessions.trading_date`, same bar/coverage rules as E009), **val block only**, 1 trial.
- **Decision rule (draft, B1 rule):** SIGNAL if mean signed return > 1.0 pip AND block-bootstrap 95% CI lower > 0 AND binomial p < 0.05. Also report (descriptive, not part of the rule) the median bid/ask spread at 18:00 NY entry and the net long result at actual bid/ask and costs x1.5.
- **Calendar label:** rollover-adjacent hour; not London fix / ECB / NY 10:00.
- **Data:** available.

### B10: NY 18:00 hour drift on trading-date Thursday (signal test, val only, dev-derived) → E012 · `done` (2026-11-08: NONE on val, +0.94 pips, CI includes 0; cost gate fails)
- **Origin:** E009 CANDIDATE (exploratory, dev): Thu_ny_18 mean +1.240 pips, CI (0.749, 2.024), t p 9e-5, up-share 0.654, n 313.
- **Test / rule:** as B9 for trading-date Thursdays, val only, 1 trial. B9 and B10 may share one experiment run but are 2 trials.

### B11: FOMC statement-day USD weakness (signal test, dev) → E013 · `done` (2026-11-08 R020: **SIGNAL on dev**, +21.28 pips, CI (2.75, 38.16), p 0.029; B11v queued as next. R017: pre-registered; phase 1 = FOMC date fetch on runner queued; next run reviews backtests/calendars/fomc_fetch_report.json, promotes the CSV to data/calendars/ and queues phase 2; R018: first fetch invalid for 2017-2019 (cross-month heading parse), parser fixed + cancelled flag, fetch re-queued; R019: re-fetch valid, file promoted, phase 2 queued)
- **Mechanism [PUB]:** short-USD/long-foreign currency positions earn larger excess returns on scheduled FOMC announcement days, read as compensation for monetary-policy uncertainty (Mueller, Tahbaz-Salehi & Vedolin 2017, JF, DOI 10.1111/jofi.12499). Karnaukh (2018 WP) finds a 5-10 bp USD drift down into neutral meetings. Prediction for us: EUR/USD rises on statement days. EUR's negative rate differential vs USD for most of the sample predicts a *smaller* effect than for high yielders, so the prior is low-to-moderate.
- **Test:** long EUR/USD mid from 16:00 America/New_York on the business day before each **scheduled** FOMC statement to 16:00 NY on statement day (covers the 14:00 statement and 14:30 press conference). Dev block only, 1 trial (~48 meetings, 2015-2020). Unscheduled actions (e.g. March 2020) are excluded and listed. Descriptive (not in rule): same window on all non-FOMC days as benchmark, and the 13:00-16:00 NY sub-window.
- **Decision rule (draft):** SIGNAL if mean signed return > 10 pips AND moving-block bootstrap 95% CI lower > 0 AND one-sided t-test p < 0.05. Then queue val confirmation B11v (~20 meetings, also low power). Power note: daily EUR/USD sd is ~40-50 pips, so with n ~48 only a mean around +12 pips or more can clear the CI bar; a NONE result does not rule out the published few-bp effect. Costs are negligible relative to a daily hold (one round trip at a liquid hour).
- **Data:** FOMC scheduled statement dates 2015-2023 are **not yet in the repo**. They must come from official Federal Reserve pages (fomchistoricalYYYY.htm for 2015-2020; fomccalendars.htm / historical pages for 2021-2023) and be committed as `data/calendars/fomc_dates.csv` with the source URL per row. This workspace could not open federalreserve.gov in R016 (permission timeout), so the pre-registration run must either (a) download and parse the pages in the research-batch workflow and commit the CSV for review before the experiment runs, or (b) fetch them in-session if access works. A test must assert 8 scheduled meetings per year. No date may be typed from memory.
- **Calendar label:** this *is* the event effect; not a fix or rollover hour.

### B11v: FOMC statement-day long EUR/USD, val confirmation of E013 (signal test, val only) → E014 · `done` (2026-11-08 R022: **NONE on val**, +19.99 pips, CI (-9.53, 51.02), p 0.115; E013 not confirmed, no lead, B11 closed. Added 2026-11-08 R020; ranked above B12, reason in agent_decision_log R020. R021: pre-registered as E014, 20 val statement days, queued on research-batch; 1 val trial counted when it runs)
- **Origin:** E013 SIGNAL on dev (n 47, mean +21.28 pips, block-4 CI (2.75, 38.16), one-sided t p 0.029). The E013 methodology fixed this follow-up before the run.
- **Test:** exactly the E013 window and rule on the **val block only** (scheduled statement dates 2021-01-21..2023-06-30 from `data/calendars/fomc_dates.csv`; unscheduled/cancelled excluded and listed), 1 trial. Reuse `fomc.evaluate_long` / `fomc.decide_b11` and the same descriptive cost check, benchmark and 13:00-16:00 sub-window.
- **Decision rule (fixed by E013, unchanged):** SIGNAL if mean > 10.0 pips AND moving-block bootstrap (block 4, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. LEAD only if SIGNAL and SPEC 4 net > 0 and costs x1.5 net > 0.
- **Power note:** ~20 val meetings; with SD ~75 pips only a mean of roughly 35+ pips clears the CI bar. Written before val is seen.
- **Data:** available (date file already validated for 2021-2023).

### B12: NFP release: does the first 15-minute reaction continue over the next hour? (signal test, dev) → E015 · `blocked` (2026-11-08 R024: BLS archive index returned HTTP 403 Access Denied to the runner in phase 1 (run 42484931936); not circumvented. Needs a human decision on a sanctioned release-date source, e.g. a FRED API key as an Actions secret (FRED release dates, release_id 50; would need a data-rule note here before use) or an official calendar file supplied by the human. 0 trials used. Earlier: added 2026-11-08, R016 refill. R023: pre-registered as E015; phase 1 = BLS release-date fetch on runner queued; next run reviews backtests/calendars/nfp_fetch_report.json, promotes the CSV to data/calendars/ and queues phase 2; 1 dev trial counted when phase 2 runs)
- **Mechanism [PUB]:** US scheduled releases move FX within minutes (Andersen et al. 2003); for DEM/USD the news effect is significant over the first 15 minutes and fades with longer horizons (Almeida, Goodhart & Payne 1998, JFQA, DOI 10.2307/2331101). Efficient-market prior: **no** continuation after 08:45. A continuation would point to slow liquidity rebuilding after the release (a microstructure, not information, effect).
- **Test:** on US Employment Situation release days (08:30 America/New_York), let r1 = EUR/USD mid return 08:30-08:45 NY and r2 = 08:45-09:45 NY. Signed return = sign(r1) x r2 (continuation). Dev only, 1 trial (~72 releases). Days with |r1| below 1 pip are counted as no trade and reported (not dropped from n). Descriptive: spread at 08:45 entry, net at bid/ask and costs x1.5, and the reversal reading (negative mean) reported but not a separate trial.
- **Decision rule (draft, B1 rule):** SIGNAL if mean signed return > 1.0 pip AND block-bootstrap 95% CI lower > 0 AND binomial p < 0.05 (hit rate of sign agreement). A significant *negative* mean (reversal) is logged as exploratory only and needs its own pre-registration.
- **Data:** release dates must come from the BLS Employment Situation archive/schedule pages (not from a "first Friday" rule, which has exceptions), committed as `data/calendars/nfp_dates.csv` with source URL. Fetch on the research-batch runner if this workspace cannot reach bls.gov; test that there are 12 releases per year (2013 shutdown-type exceptions documented). This also builds the first piece of B6's calendar.
- **Calendar label:** release-time effect; 08:45-09:45 NY is a liquid hour (London/NY overlap).

### B13: Intraday momentum into the CME FX futures settlement (signal test, dev) → E016 · `blocked` (2026-11-08 R028: re-fetch run 42504753112 timed out again on all 3 CME URLs (3 attempts x 120 s, no HTTP answer); stop rule applied, B13 blocked, 0 trials. Unblocking needs a human-supplied official CME settlement-time source. R027: phase-1 fetch run 42500439921 timed out on all 3 CME URLs (no HTTP answer, not a refusal); one re-fetch queued with 120 s timeout + transport-only retries; if it fails again the item is blocked (stop rule in E016 methodology addendum). 0 trials. R026: pre-registered as E016; phase 1 = official CME settlement-time fetch on runner queued; next run reviews backtests/calendars/cme_settlement_fetch_report.json, promotes S to data/calendars/cme_fx_settlement.json and queues phase 2, or blocks; 1 dev trial counted when phase 2 runs. Added 2026-11-08 R025 refill)
- **Mechanism [PUB]:** across 60+ futures including currencies, the return over the rest of the day predicts the return in the last 30 minutes before the futures close; attributed to gamma hedging by option market makers and leveraged products, with reversal over the following days (Baltussen, Da, Lammers & Martens 2021, JFE, DOI 10.1016/j.jfineco.2021.04.029; entry in research/academic_studies.md, VERIFIED (abstract) 2026-11-07). For RUB/USD, Elaut, Frömmel & Lampaert (2018, JFM) find a similar effect tied to fixed trading hours. Our question: does the effect show up in **spot** EUR/USD around the CME Euro FX (6E) settlement, where option hedging of the futures should transmit to spot by arbitrage?
- **Settlement time: UNVERIFIED.** The official CME daily settlement window for Euro FX futures could not be opened from this workspace in R025 (fetch permission timeout). It must be read from an official cmegroup.com page fetched on the research-batch runner (phase 1), saved under `backtests/calendars/` with the URL, and reviewed before any price data are touched. No time may be typed from memory. If CME refuses automated access (403), the item becomes `blocked` (no circumvention, R024 lesson).
- **Test (fixed relative to the verified settlement time S, in America/Chicago converted per day to America/New_York):** predictor r1 = EUR/USD mid return from 17:00 NY on the previous trading date to S - 30 min; target r2 = mid return S - 30 min to S. Signed return = sign(r1) x r2. Dev only, 1 trial (~1,500 trading days; days with missing bars excluded per SPEC coverage rule and counted). Descriptive (not in rule): OLS slope of r2 on r1, median bid/ask spread at S - 30 min, net at bid/ask, SPEC 4 and costs x1.5, and the next-day reversal reading.
- **Decision rule (draft, B1 rule):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap 95% CI lower > 0 AND binomial p < 0.05 (hit rate of sign agreement). WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. A SIGNAL earns a val confirmation (B13v, ~640 days, enough power for the same bar).
- **Power note:** a 30-minute window has a much smaller SD than a daily hold, so the 1-pip bar (not the CI) will usually bind; the bar is kept because it is roughly the round-trip cost at retail spreads.
- **Contamination note:** E009 scanned unconditional hourly means on dev; this conditional (sign-agreement) statistic was not computed there, so dev is still usable. Record this in the methodology.
- **Calendar label:** futures-settlement effect; not the London 4pm fix (11:00 NY) or the 17:00 NY roll.
- **Data:** price data available; settlement time needs phase 1.

### B14: Home-hours depreciation, EUR in European hours and USD in US hours (signal test, val only) → E017 · `done` (2026-11-08 R030: **WEAK on val**, +2.179 pips signed, CI (0.001, 4.265), binom p 0.451; SPEC 4 net -0.382, x1.5 -1.663; rejected, no lead. R029: pre-registered as E017, queued on research-batch; SNB paper still could not be opened (fetch-permission timeout), windows unchanged; 1 val trial counted when it runs. Added 2026-11-08 R025 refill)
- **Mechanism [PUB]:** currencies tend to depreciate during their own region's trading hours and appreciate outside them, consistent with local participants being net buyers of foreign currency; the SNB working-paper abstract says a simple EUR/USD strategy based on it was profitable (Breedon & Ranaldo 2013, JMCB, DOI 10.1111/jmcb.12032; entry in research/academic_studies.md, VERIFIED (abstract) 2026-11-07). Sample ended 2007; the effect may have been arbitraged away (Neely, Weller & Ulrich 2009).
- **Windows (fixed now, from the mechanism, not from data):** European-only hours 03:00-08:00 America/New_York (London morning before the US opens): predicted EUR/USD **down**. US-only hours 12:00-17:00 America/New_York (after the London close, before the roll): predicted EUR/USD **up**. The paper's exact hour definitions were not re-read in R025 (fetch permission timeout); the pre-registration run should try to open the SNB working paper and note any difference, **without** changing these windows.
- **Test:** daily signed return = -(mid return 03:00-08:00 NY) + (mid return 12:00-17:00 NY), one value per trading date. **Val block only**, 1 trial (~640 days). Reason for val only: E009 scanned every hour of the dev block, so dev is no longer clean for any time-of-day window. Descriptive (not in rule): each leg separately, median spreads at 03:00, 08:00, 12:00 and 17:00 NY (the 17:00 exit sits next to the roll; check its cost), net at bid/ask, SPEC 4 and x1.5.
- **Decision rule (draft, B1 rule):** SIGNAL if mean daily signed return > 1.0 pip AND moving-block bootstrap 95% CI lower > 0 AND binomial p < 0.05. WEAK / NONE as B1. Because dev was scanned (E009) and val is the only clean block, a val SIGNAL cannot by itself meet the LEAD definition (it needs a dev pass and a separate val confirmation). A val SIGNAL surviving costs x1.5 is therefore logged in agent_decision_log.md as a candidate needing a human OOS decision (no notification, not a LEAD); this is fixed now, before any data.
- **Prior:** low. E001 found no drift 08:00-12:00 NY (`unconditional_long` +0.59 dev / +0.71 val, CIs include 0), and E007/E010/E011 found sub-pip time-of-day effects.
- **Calendar label:** time-of-day effect; the windows avoid the ECB fix (08:15 NY) and the London 4pm fix (11:00 NY) but the 17:00 exit is the roll.
- **Data:** available.

### B15: Round-number crossing continuation, "price cascades" (signal test, dev) → E018 · `done` (2026-11-08 R033: **NONE on dev**, -0.128 pips signed, CI (-0.989, 0.714), binom p 0.280; SPEC 4 net -0.628, x1.5 -0.879; rejected, no lead. R032: pre-registered as E018, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-08 R031 refill)
- **Mechanism [PUB]:** stop-loss orders cluster just beyond round numbers (rates ending in 00 or 50), so crossing a round number
  triggers stops and a rapid, self-reinforcing move; "Most results are statistically significant for hours, although not for days"
  (Osler 2002, FRBNY Staff Report 150, opened 2026-11-08 R031; journal version 2005, venue UNVERIFIED). Consistent with Osler (2003, JF,
  VERIFIED (abstract)): stops cluster beyond round numbers, take-profits at them. Data are 1990s/2000 dealer orders; e-trading may have
  arbitraged the effect away (Neely, Weller & Ulrich 2009).
- **Event (fixed now):** round levels L = every multiple of 0.0050 (00 and 50, the paper's definition). An up-crossing at bar t means
  mid close(t-1) < L <= mid close(t); a down-crossing the reverse. Only the **first** crossing of each level per trading date
  (`sessions.trading_date`) counts. Entry at the open of bar t+1 (SPEC 4 fill rule); exit at the open of the bar 60 minutes later.
  Overlapping trades not allowed: an event while a trade is open is skipped and counted.
- **Exclusions (fixed now, R030 lesson):** no entry or exit between 16:30 and 18:30 America/New_York (roll); entry skipped if spread > 2.0 pips
  (SPEC 4); both counted and reported. Coverage: the 60-minute exit window needs >= 55 of 60 bars.
- **Test:** signed return = crossing direction x mid return entry->exit, one value per event. **Dev only, 1 trial.**
- **Decision rule (draft, B1 rule):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 20 events, 2000 draws,
  seed 0) 95% CI lower > 0 AND binomial p < 0.05 (hit rate of continuation). WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
  A SIGNAL earns a val confirmation (B15v) with the same rule. A significant **negative** mean (reversal at round numbers, the take-profit
  reading) is logged as exploratory only and needs its own pre-registration.
- **Descriptive (not in rule):** control levels offset by 23 pips (levels ending 23 and 73) run through the identical procedure; difference
  round minus control; 15- and 120-minute horizons; by year; median spread at entry; net at bid/ask, SPEC 4 and costs x1.5.
- **Power note:** expect roughly 1-2 events per trading day (~2,000 on dev); a 60-minute SD of ~10-12 pips gives SE ~0.3 pips, so the
  1-pip bar binds, not the CI.
- **Contamination note:** E009 scanned unconditional hour-of-day means; E006 tested Asian-range false breaks. No price-level-conditional
  statistic has been computed on dev, so dev is clean for this test. Record in the methodology.
- **Calendar label:** price-level effect, not a time-of-day, fix or release effect (events can occur at fix/release times; report the
  share of events within +-15 min of 10:00 NY, 11:00 NY and 08:30 NY).
- **Data:** price data in repo only; no external source (R028 lesson).

### B16: Time-series momentum, 12-month lookback, daily hold (signal test, dev) → E019 · `done` (2026-11-09 R035: **NONE on dev**, -0.644 pips/day signed, CI (-3.196, 1.978), t p 0.678; SPEC 4 net -0.674, x1.5 -0.689; rejected, no lead. R034: pre-registered as E019, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-08 R031 refill)
- **Mechanism [PUB]:** "persistence in returns for one to 12 months that partially reverses over longer horizons" across 58 futures including
  currencies, attributed to initial under-reaction and delayed over-reaction (Moskowitz, Ooi & Pedersen 2012, JFE 104(2), 228-250,
  DOI 10.1016/j.jfineco.2011.11.003; abstract opened 2026-11-08 R031). Evidence is portfolio-level; a single pair over 6 years has low power.
- **Signal (fixed now):** on each trading date D, s(D) = sign(mid at 16:00 NY on D - mid at 16:00 NY on the trading date 252 trading dates
  earlier). Position s(D) held from 16:00 NY on D to 16:00 NY on D+1 (avoids the roll and its spreads, R030 lesson). Daily signed
  return = s(D) x mid return. The 252-day lookback is the upper end of the abstract's 1-12 month range, fixed before any data; other
  lookbacks are new trials.
- **Test:** **dev only, 1 trial**; first test date is the first dev date with 252 prior trading dates (early 2016), so n ~1,250.
  Days missing either 16:00 NY bar (or the bar 252 dates back) are excluded and counted.
- **Decision rule (draft):** SIGNAL if mean daily signed return > 1.0 pip AND moving-block bootstrap (block 20 days, 2000 draws, seed 0)
  95% CI lower > 0 AND one-sided t-test p < 0.05. (t-test, not hit rate, because trend returns are fat-tailed: the effect lives in the
  mean, as in E013.) WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. A SIGNAL earns a val confirmation (B16v).
- **Descriptive (not in rule):** number of sign flips; net per actual flip at bid/ask, SPEC 4 and costs x1.5; by year; long and short days
  separately; buy-and-hold benchmark. **Limitation:** overnight swap/carry is not in the data (EUR paid negative carry vs USD for most of
  2015-2020, which would hurt the long days and help the short days); state this in results.
- **Power note:** daily SD ~45 pips, n ~1,250, overlapping signals -> bootstrap SE ~1.5-2 pips; only a mean of roughly 3-4 pips/day
  (8-10%/yr) can clear the CI bar. A NONE does not rule out a small effect.
- **Contamination note:** no daily-horizon or multi-day trend statistic has been computed on dev (E001-E017 are intraday). Record this.
- **Calendar label:** multi-day trend; not a time-of-day effect.
- **Data:** price data in repo only.

### B17: Weekend-gap reversal (signal test, dev) → E020 · `done` (2026-11-09 R038: **NONE on dev**, -1.574 pips per event signed (n 90), CI (-12.699, 7.03), t p 0.627; SPEC 4 net -2.108, x1.5 -2.374; rejected, no lead. R037: pre-registered as E020, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-09 R036 refill)
- **Mechanism [PUB]:** in spot FX (8 major, 9 emerging currencies), "after a large price difference between Friday close and subsequent
  Monday open, most markets are likely to reverse" over horizons in the following week, read as weekend overreaction; the abstract reports
  the reversal strategy survives costs and interest rates out of sample (Dao, McGroarty & Urquhart 2016, JMFM 37-38, 158-167,
  DOI 10.1016/j.mulfin.2016.11.001; entry in research/academic_studies.md, VERIFIED (abstract) 2026-11-09 R036). Data period, currency
  list, gap threshold and horizons are UNVERIFIED (not on the pages opened); everything below is fixed here, not taken from the paper.
- **Timestamps (fixed now, R030 lesson: nothing between 16:30 and 18:30 NY):** quote at T = open of the first bar in [T, T+5 min).
  Friday close F = mid at 16:00 NY Friday. Monday open M = mid at 20:00 NY Sunday (first bar of trading-date Monday at or after the Tokyo
  open in either DST state, 3 h after the roll so Sunday-open spreads have time to normalise). Exit X = mid at 16:00 NY on trading-date
  Monday. Gap G = M - F (pips).
- **Event:** a weekend is "large" if |G| is strictly above the 67th percentile of |G| over the previous 26 valid weekends (rolling, past
  only; no event until 26 valid weekends exist). Weekends with a missing F, M or X bar are excluded and counted (holiday weekends included).
- **Test:** signed return = -sign(G) x (X - M) mid, one value per large weekend. **Dev only, 1 trial.** Entry skipped (counted) if the
  ask-bid spread at 20:00 NY Sunday is > 2.0 pips (SPEC 4).
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 4 events, 2000 draws, seed 0) 95% CI
  lower > 0 AND one-sided t-test p < 0.05 (t, not hit rate: the effect is in the mean of a fat-tailed ~20 h return, as E013/E019).
  WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. A SIGNAL earns a val confirmation (B17v) with the same rule.
- **Descriptive (not in rule):** all weekends (no threshold); horizons to 16:00 NY Tuesday and Friday; by year; median spread at F, M
  and X; net at bid/ask, SPEC 4 and costs x1.5; the 17:00-20:00 NY Sunday move (gap already reversing before entry?).
- **Power note:** ~310 dev weekends, ~95 events after burn-in; ~20 h SD ~40-50 pips -> SE ~4-5 pips; only a mean of roughly 8-10 pips
  clears the CI bar. A NONE does not rule out a small effect.
- **Contamination note:** E009 scanned unconditional weekday x hour means on dev; no gap-conditional statistic has been computed on dev
  (E019 used 16:00 quotes but only a 252-day sign). Dev is clean for this test; record in the methodology.
- **Calendar label:** weekend calendar effect; entry 20:00 NY Sunday, exit 16:00 NY Monday (avoids the roll, the London 4pm fix at 11:00
  NY is inside the hold).
- **Data:** price data in repo only (R028 lesson). **Spread risk:** Sunday 20:00 NY spreads are unknown until the run; reported, and the
  2.0-pip skip rule applies.

### B18: Next-session reversal after a large daily move (signal test, dev) → E021 · `done` (2026-11-09 R040: **NONE on dev**, -2.55 pips per event signed (n 229), CI (-7.097, 4.167), t p 0.776; SPEC 4 net -3.041, x1.5 -3.287; rejected, no lead. R039: pre-registered as E021, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-09 R036 refill)
- **Mechanism [PUB]:** "Significant intraday price-reversal patterns are observed in five of the seven currency futures contracts" after
  large 1-day returns and opening gaps, CME 1988-2003, mostly reversals after the euro's introduction (Rentzler, Tandon & Yu 2006, JFM
  26(11), 1089-1130, DOI 10.1002/fut.20226; entry in research/academic_studies.md, VERIFIED (abstract) 2026-11-09 R036). Threshold and
  horizon UNVERIFIED; old futures data, may be arbitraged away (Neely, Weller & Ulrich 2009).
- **Signal (fixed now):** R(D) = mid at 16:00 NY on trading date D - mid at 16:00 NY on the previous trading date (pips). D is "large"
  if |R(D)| is strictly above the 80th percentile of |R| over the previous 60 valid trading dates (rolling, past only).
- **Trade:** position -sign(R(D)) from 20:00 NY (start of the next trading date, after the roll and the Tokyo open) to 10:45 NY on that
  next trading date (before the London 4pm fix at 11:00 NY). Signed return = -sign(R(D)) x mid return. D on a Friday is excluded and
  counted (the weekend gap belongs to B17). Missing bars excluded and counted; entry skipped if spread at 20:00 NY > 2.0 pips.
- **Test:** **dev only, 1 trial**, n ~ 0.2 x ~1,200 non-Friday dates ~ 240 events after burn-in.
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 10 events, 2000 draws, seed 0) 95% CI
  lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. SIGNAL earns B18v (val).
- **Descriptive (not in rule):** the 16:00-20:00 NY move (reversal before entry, not tradable at our rules); continuation reading
  (negative mean) logged as exploratory only; by year; median spread at entry/exit; net at bid/ask, SPEC 4 and costs x1.5.
- **Power note:** ~15 h SD ~35-40 pips -> SE ~2.5 pips; a mean of roughly 5 pips is needed to clear the CI bar.
- **Contamination note:** E009 scanned unconditional hour-of-day means; E019 computed 16:00-16:00 daily returns conditional only on the
  252-day sign. No return conditional on a large prior-day move has been computed on dev. Record in the methodology.
- **Calendar label:** daily-move reversal; the hold contains the ECB fix (08:15 NY) and US 08:30 releases; report the share of events
  whose hold contains an FOMC statement date (data/calendars/fomc_dates.csv).
- **Data:** price data in repo only.

### B19: Pre-ECB-fix USD appreciation on high-volatility dates (signal test, dev) → E022 · `done` (2026-11-09 R043: **SIGNAL on dev**, +3.646 pips per event signed (n 473), CI (0.011, 7.751), t p 0.0133; SPEC 4 net +3.139, x1.5 +2.886; marginal; earns B19v. R042: pre-registered as E022, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-09 R041 refill)
- **Mechanism [PUB]:** the USD "systematically appreciates against all currencies ahead of the three major currency fixes" (Krohn,
  Mueller & Whelan, fixings paper; JF 2024 version VERIFIED (abstract) in research/academic_studies.md; AEA 2020 draft opened
  2026-11-09 R041). The draft's report that the fix reversals are larger in high-volatility / high-spread states, and its EUR window
  2:00-8:15 a.m. ET, were read only via a model summary: **UNVERIFIED**. Everything below is fixed here, not taken from the paper.
- **Variable changed (one):** vol-state conditioning. Unconditional relatives already tested: E010 (ECB fix 1 h windows, dev WEAK),
  E017 (short 03:00-08:00 NY as one leg of home-hours, val WEAK).
- **Signal (fixed now):** RNG(D-1) = high - low of mid over the previous trading date (17:00 NY -> 17:00 NY, pips), from 1-min bars.
  Trading date D is "high-vol" if RNG(D-1) is strictly above the 67th percentile of RNG over the 60 valid trading dates before D-1
  (rolling, past only; no event until 60 exist). Days with < 90% of expected bars in D-1 are invalid and counted.
- **Trade:** short EUR/USD from 02:00 NY to 08:15 NY on high-vol trading date D (quote = open of first bar in [T, T+5 min)).
  Signed return = -(X - E) mid, pips. Missing bars excluded and counted; entry skipped if spread at 02:00 NY > 2.0 pips (SPEC 4).
- **Test:** **dev only, 1 trial**; n ~ 0.33 x ~1,500 dates ~ 480 events.
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 10 events, 2000 draws, seed 0)
  95% CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. SIGNAL earns B19v (val).
- **Descriptive (not in rule):** same trade on non-high-vol dates (control) and on all dates; by year; by weekday; median spread at
  entry/exit; net at bid/ask, SPEC 4 and costs x1.5; share of events on ECB monetary-policy days is NOT computable (no ECB calendar in
  repo) -> stated as a limitation.
- **Power note:** ~6 h SD ~25-30 pips -> SE ~1.2-1.4 pips; a mean of roughly 2.5-3 pips is needed to clear the CI bar.
- **Contamination note:** E009 scanned unconditional weekday x hour means on dev (the 02:00-08:00 NY hours included); E008 used ATR
  as a control for US-window absolute moves, not for this window's signed return. No vol-conditional signed return of this window has
  been computed on dev. Record in the methodology.
- **Calendar label:** pre-ECB-fix window (ECB reference rate 14:15 CET ~ 08:15 NY); exit before US 08:30 releases.
- **Data:** price data in repo only.

### B19v: Pre-ECB-fix USD appreciation on high-volatility dates, val confirmation (signal test, val only) → E023 · `done` (2026-11-09 R045: **NONE on val**, +1.197 pips per event signed (n 204), CI (-3.144, 5.919), t p 0.304; E022 not confirmed, no lead, B19 line closed. R044: pre-registered as E023, queued on research-batch; 1 val trial counted when it runs. Added 2026-11-09 R043 after E022 dev SIGNAL; ranked above B20, reason in agent_decision_log.md R043)
- **Origin:** E022 (B19) dev SIGNAL: n 473, mean +3.646 pips, CI (0.011, 7.751), t p 0.0133. E022 methodology fixed before data:
  "SIGNAL -> queue val confirmation B19v as its own experiment with this rule unchanged".
- **Test:** identical to E022 (`vol_state_fix`: prior trading-date mid range > p67 of the 60 valid dates before it, past only, 90%
  coverage, 60-date burn-in; short 02:00 -> 08:15 NY on D; quote = open of first bar in [T, T+5 min); exclusions missing_entry,
  missing_exit, entry spread > 2.0 pips) on the **val block only** (2021-01-21..2023-06-30). The script drops non-val bars before any
  computation; the rolling history is built from val dates only (burn-in on val, no dev history used). 1 val trial. ~640 val dates,
  ~190 events expected after burn-in.
- **Decision rule (unchanged from E022):** SIGNAL if mean signed > 1.0 pip AND moving-block bootstrap (block 10 events, 2000 draws,
  seed 0) 95% CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. "Val pass" = SIGNAL.
  LEAD (AUTONOMOUS_PROTOCOL) additionally needs val mean net > 0 at SPEC 4 and at costs x1.5.
- **Descriptive (not in rule):** as E022 (control normal dates, all dates, by year, by weekday, spreads, net at bid/ask, SPEC 4, x1.5).
- **Power note:** ~190 events x SD ~30-36 pips -> SE ~2.2-2.6 pips; a val mean near the dev +3.6 would likely give WEAK, not SIGNAL.
  Stated now, before data; the rule is not loosened.
- **Contamination note:** E017 computed the unconditional short 03:00-08:00 NY leg on val (+1.776). No vol-conditional 02:00-08:15 NY
  return has been computed on val. Record in the methodology.
- **Data:** price data in repo only.

### B20: Post-London-fix EUR appreciation on high-volatility dates (signal test, dev) · `ready` (Added 2026-11-09 R041 refill)
- **Mechanism [PUB]:** same source family as B19 (USD depreciates after the fixes; EUR "strongly increase[s] in value against the
  U.S. dollar between 8:00 a.m. and 5:00 p.m.", Krohn-Mueller-Whelan AEA 2019 draft, opened 2026-11-09 R041). Vol-state amplification
  and the 11:00 a.m.-5:00 p.m. ET window: **UNVERIFIED** (model summary only).
- **Variable changed (one):** vol-state conditioning of the post-London-fix long. Unconditional relatives: E007 (London fix 1 h
  windows, dev NONE), E017 (long 12:00-17:00 NY leg, val WEAK; the 16:59 exit spread was 3.0 pips -> R030 lesson).
- **Signal:** identical high-vol definition to B19 (RNG(D-1) > rolling p67 of 60 valid dates; past only).
- **Trade:** long EUR/USD from 11:05 NY (after the 5-minute fix window) to 16:00 NY on high-vol trading date D (exit before 16:30 NY
  per R030 lesson). Signed return = X - E mid, pips. Missing bars excluded and counted; entry skipped if spread at 11:05 NY > 2.0 pips.
- **Test:** **dev only, 1 trial**; ~480 events.
- **Decision rule (draft):** as B19 (mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05 -> SIGNAL; WEAK/NONE as
  B19). SIGNAL earns B20v (val).
- **Descriptive (not in rule):** control on non-high-vol dates and all dates; by year; share of events on FOMC statement days
  (data/calendars/fomc_dates.csv; 14:00 NY statement is inside the hold) and the result excluding them; spreads; net at bid/ask,
  SPEC 4 and x1.5.
- **Power note:** ~5 h SD ~22-28 pips -> SE ~1.1-1.3 pips.
- **Contamination note:** E009 (unconditional hours) and E007 (1 h post-fix) on dev; no vol-conditional 11:05-16:00 NY return computed.
- **Independence from B19:** both use the same condition; if both are run they are 2 separate trials and count separately. Run B19
  first; B20 does not depend on B19's result (no re-ranking after B19 unless logged with a reason before B20 is pre-registered).
- **Data:** price data in repo only.

### Refill note R041 (not an item)
- Practitioner "month-end hedge rebalancing" models (USD direction into the month-end London fix predicted by month-to-date US vs
  foreign equity performance) were found only in broker/news commentary, not in a verified academic source, and need equity index data
  not in the repo. Not added; would need a human-supplied equity series and a verified source.
