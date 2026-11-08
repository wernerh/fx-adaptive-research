# Research backlog

Ordered by priority. Status: `ready` | `running` | `done` | `blocked` | `parked`.
Autonomous runs take the top `ready` item (docs/AUTONOMOUS_PROTOCOL.md). Add items at the bottom; re-rank only with a
reason in agent_logs/agent_decision_log.md. Dev = 2015-01-01..2020-12-31, val = 2021-01-21..2023-06-30, OOS locked.

Trial count so far on dev: **227** (E001: 7, E006: 14, E004: 1, E007: 4, E008: 4, E009: 192 exploratory cells, E010: 2, E011: 2, E013: 1). Val-only trials: **3** (E012: 2, E014: 1). Total registered trials: **230**. Update after every experiment. (R027: E016 phase-1 re-fetch queued, 0 trials. R026: E016/B13 pre-registered, 1 dev trial counted when phase 2 runs. R025: refill added B13, B14: 0 trials until pre-registered. R023: E015/B12 pre-registered, 1 dev trial counted when phase 2 runs. R022: E014 ran, val +1. R020: E013 phase 2 ran, dev +1. R016 refill added B11, B12: 0 trials until pre-registered. R017: E013/B11 pre-registered, 1 dev trial counted when phase 2 runs.)

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

### B13: Intraday momentum into the CME FX futures settlement (signal test, dev) → E016 · `running` (2026-11-08 R027: phase-1 fetch run 42500439921 timed out on all 3 CME URLs (no HTTP answer, not a refusal); one re-fetch queued with 120 s timeout + transport-only retries; if it fails again the item is blocked (stop rule in E016 methodology addendum). 0 trials. R026: pre-registered as E016; phase 1 = official CME settlement-time fetch on runner queued; next run reviews backtests/calendars/cme_settlement_fetch_report.json, promotes S to data/calendars/cme_fx_settlement.json and queues phase 2, or blocks; 1 dev trial counted when phase 2 runs. Added 2026-11-08 R025 refill)
- **Mechanism [PUB]:** across 60+ futures including currencies, the return over the rest of the day predicts the return in the last 30 minutes before the futures close; attributed to gamma hedging by option market makers and leveraged products, with reversal over the following days (Baltussen, Da, Lammers & Martens 2021, JFE, DOI 10.1016/j.jfineco.2021.04.029; entry in research/academic_studies.md, VERIFIED (abstract) 2026-11-07). For RUB/USD, Elaut, Frömmel & Lampaert (2018, JFM) find a similar effect tied to fixed trading hours. Our question: does the effect show up in **spot** EUR/USD around the CME Euro FX (6E) settlement, where option hedging of the futures should transmit to spot by arbitrage?
- **Settlement time: UNVERIFIED.** The official CME daily settlement window for Euro FX futures could not be opened from this workspace in R025 (fetch permission timeout). It must be read from an official cmegroup.com page fetched on the research-batch runner (phase 1), saved under `backtests/calendars/` with the URL, and reviewed before any price data are touched. No time may be typed from memory. If CME refuses automated access (403), the item becomes `blocked` (no circumvention, R024 lesson).
- **Test (fixed relative to the verified settlement time S, in America/Chicago converted per day to America/New_York):** predictor r1 = EUR/USD mid return from 17:00 NY on the previous trading date to S - 30 min; target r2 = mid return S - 30 min to S. Signed return = sign(r1) x r2. Dev only, 1 trial (~1,500 trading days; days with missing bars excluded per SPEC coverage rule and counted). Descriptive (not in rule): OLS slope of r2 on r1, median bid/ask spread at S - 30 min, net at bid/ask, SPEC 4 and costs x1.5, and the next-day reversal reading.
- **Decision rule (draft, B1 rule):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap 95% CI lower > 0 AND binomial p < 0.05 (hit rate of sign agreement). WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. A SIGNAL earns a val confirmation (B13v, ~640 days, enough power for the same bar).
- **Power note:** a 30-minute window has a much smaller SD than a daily hold, so the 1-pip bar (not the CI) will usually bind; the bar is kept because it is roughly the round-trip cost at retail spreads.
- **Contamination note:** E009 scanned unconditional hourly means on dev; this conditional (sign-agreement) statistic was not computed there, so dev is still usable. Record this in the methodology.
- **Calendar label:** futures-settlement effect; not the London 4pm fix (11:00 NY) or the 17:00 NY roll.
- **Data:** price data available; settlement time needs phase 1.

### B14: Home-hours depreciation, EUR in European hours and USD in US hours (signal test, val only) · `ready` (added 2026-11-08 R025 refill; 0 trials until pre-registered)
- **Mechanism [PUB]:** currencies tend to depreciate during their own region's trading hours and appreciate outside them, consistent with local participants being net buyers of foreign currency; the SNB working-paper abstract says a simple EUR/USD strategy based on it was profitable (Breedon & Ranaldo 2013, JMCB, DOI 10.1111/jmcb.12032; entry in research/academic_studies.md, VERIFIED (abstract) 2026-11-07). Sample ended 2007; the effect may have been arbitraged away (Neely, Weller & Ulrich 2009).
- **Windows (fixed now, from the mechanism, not from data):** European-only hours 03:00-08:00 America/New_York (London morning before the US opens): predicted EUR/USD **down**. US-only hours 12:00-17:00 America/New_York (after the London close, before the roll): predicted EUR/USD **up**. The paper's exact hour definitions were not re-read in R025 (fetch permission timeout); the pre-registration run should try to open the SNB working paper and note any difference, **without** changing these windows.
- **Test:** daily signed return = -(mid return 03:00-08:00 NY) + (mid return 12:00-17:00 NY), one value per trading date. **Val block only**, 1 trial (~640 days). Reason for val only: E009 scanned every hour of the dev block, so dev is no longer clean for any time-of-day window. Descriptive (not in rule): each leg separately, median spreads at 03:00, 08:00, 12:00 and 17:00 NY (the 17:00 exit sits next to the roll; check its cost), net at bid/ask, SPEC 4 and x1.5.
- **Decision rule (draft, B1 rule):** SIGNAL if mean daily signed return > 1.0 pip AND moving-block bootstrap 95% CI lower > 0 AND binomial p < 0.05. WEAK / NONE as B1. Because dev was scanned (E009) and val is the only clean block, a val SIGNAL cannot by itself meet the LEAD definition (it needs a dev pass and a separate val confirmation). A val SIGNAL surviving costs x1.5 is therefore logged in agent_decision_log.md as a candidate needing a human OOS decision (no notification, not a LEAD); this is fixed now, before any data.
- **Prior:** low. E001 found no drift 08:00-12:00 NY (`unconditional_long` +0.59 dev / +0.71 val, CIs include 0), and E007/E010/E011 found sub-pip time-of-day effects.
- **Calendar label:** time-of-day effect; the windows avoid the ECB fix (08:15 NY) and the London 4pm fix (11:00 NY) but the 17:00 exit is the roll.
- **Data:** available.
