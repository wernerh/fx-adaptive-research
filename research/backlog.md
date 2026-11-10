# Research backlog

Ordered by priority. Status: `ready` | `running` | `done` | `blocked` | `parked`.
Autonomous runs take the top `ready` item (docs/AUTONOMOUS_PROTOCOL.md). Add items at the bottom; re-rank only with a
reason in agent_logs/agent_decision_log.md. Dev = 2015-01-01..2020-12-31, val = 2021-01-21..2023-06-30, OOS locked.

Trial count so far on dev: **238** (E001: 7, E006: 14, E004: 1, E007: 4, E008: 4, E009: 192 exploratory cells, E010: 2, E011: 2, E013: 1, E018: 1, E019: 1, E020: 1, E021: 1, E022: 1, E024: 1, E026: 1, E027: 1, E028: 1, E030: 1, E031: 1). Val-only trials: **8** (E012: 2, E014: 1, E017: 1, E023: 1, E025: 1, E029: 1, E032: 1). Total registered trials: **246**. Update after every experiment. (R067: E032 ran, val +1. R066: E032/B27 pre-registered, 1 val trial counted when it runs. R065: refill added B27: 0 trials until pre-registered. R064: E031 ran, dev +1. R063: E031/B26 pre-registered, 1 dev trial counted when it runs. R062: E030 ran, dev +1. R061: E030/B25 pre-registered, 1 dev trial counted when it runs. R060: refill added B25, B26: 0 trials until pre-registered. R059: E029 ran, val +1. R058: E029/B24 pre-registered, 1 val trial counted when it runs. R057: E028 ran, dev +1. R056: E028/B23 pre-registered, 1 dev trial counted when it runs. R054: E027 ran, dev +1. R053: E027/B22 pre-registered, 1 dev trial counted when it runs. R052: E026 ran, dev +1. R051: E026/B21 pre-registered, 1 dev trial counted when it runs. R050: refill added B21, B22: 0 trials until pre-registered. R049: E025 ran, val +1. R048: E025/B20v pre-registered, 1 val trial counted when it runs. R047: E024 ran, dev +1; B20v added, 0 trials until pre-registered. R045: E023 ran, val +1. R044: E023/B19v pre-registered, 1 val trial counted when it runs. R043: E022 ran, dev +1; B19v added, 0 trials until pre-registered. R042: E022/B19 pre-registered, 1 dev trial counted when it runs. R041: refill added B19, B20: 0 trials until pre-registered. R040: E021 ran, dev +1. R039: E021/B18 pre-registered, 1 dev trial counted when it runs. R038: E020 ran, dev +1. R037: E020/B17 pre-registered, 1 dev trial counted when it runs. R036: refill added B17, B18: 0 trials until pre-registered. R035: E019 ran, dev +1. R034: E019/B16 pre-registered, 1 dev trial counted when it runs. R033: E018 ran, dev +1. R032: E018/B15 pre-registered, 1 dev trial counted when it runs. R031: refill added B15, B16: 0 trials until pre-registered. R030: E017 ran, val +1. R029: E017/B14 pre-registered, 1 val trial counted when it runs. R028: E016/B13 blocked after second CME fetch failure, 0 trials. R027: E016 phase-1 re-fetch queued, 0 trials. R026: E016/B13 pre-registered, 1 dev trial counted when phase 2 runs. R025: refill added B13, B14: 0 trials until pre-registered. R023: E015/B12 pre-registered, 1 dev trial counted when phase 2 runs. R022: E014 ran, val +1. R020: E013 phase 2 ran, dev +1. R016 refill added B11, B12: 0 trials until pre-registered. R017: E013/B11 pre-registered, 1 dev trial counted when phase 2 runs.)

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

### B20: Post-London-fix EUR appreciation on high-volatility dates (signal test, dev) → E024 · `done` (2026-11-09 R047: **SIGNAL on dev**, +2.983 pips per event signed (n 472), CI (0.566, 4.847), t p 0.0053; SPEC 4 net +2.515, x1.5 +2.281; earns B20v. R046: pre-registered as E024, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-09 R041 refill)
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

### B20v: Post-London-fix EUR appreciation on high-volatility dates, val confirmation (signal test, val only) → E025 · `done` (2026-11-09 R049: **NONE on val**, +0.582 pips per event signed (n 204), CI (-1.992, 3.14), t p 0.369; x1.5 net -0.197; E024 not confirmed, no lead, B20 line closed. R048: pre-registered as E025, queued on research-batch; 1 val trial counted when it runs. Added 2026-11-09 R047 after E024 dev SIGNAL; E024 methodology fixed "SIGNAL -> queue val confirmation B20v" before data)
- **Origin:** E024 (B20) dev SIGNAL: n 472, mean +2.983 pips, CI (0.566, 4.847), t p 0.0053.
- **Test:** identical to E024 (`vol_state_fix` / `vol_state_london`: prior trading-date mid range > p67 of the 60 valid dates before it,
  past only, 90% coverage, 60-date burn-in; long 11:05 -> 16:00 NY on D; quote = open of first bar in [T, T+5 min); exclusions
  missing_entry, missing_exit, entry spread > 2.0 pips) on the **val block only** (2021-01-21..2023-06-30), handled exactly as E023:
  bars at or after 2023-07-01 00:00 UTC dropped first (OOS never read), then non-val bars, before any computation; rolling history and
  burn-in from val dates only. 1 val trial. ~640 val dates, ~200 events expected after burn-in.
- **Decision rule (unchanged from E024):** SIGNAL if mean signed > 1.0 pip AND moving-block bootstrap (block 10 events, 2000 draws,
  seed 0) 95% CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. "Val pass" = SIGNAL.
  LEAD (AUTONOMOUS_PROTOCOL) additionally needs val mean net > 0 at SPEC 4 and at costs x1.5 (`lead_cost_gate` as in E023), and the
  result excluding FOMC statement days stated.
- **Descriptive (not in rule):** as E024 (control normal dates, all dates, FOMC days and excl FOMC, by year, by weekday, spreads, net at
  bid/ask, SPEC 4, x1.5).
- **Power note:** ~200 events x SD ~25 pips -> SE ~1.8 pips; a val mean near the dev +3.0 could give WEAK, not SIGNAL. Stated now,
  before data; the rule is not loosened.
- **Contamination note:** E017 computed the unconditional long 12:00-17:00 NY leg on val (WEAK). No vol-conditional 11:05-16:00 NY
  return has been computed on val. Record in the methodology.
- **Data:** price data in repo only.

### Refill note R041 (not an item)
- Practitioner "month-end hedge rebalancing" models (USD direction into the month-end London fix predicted by month-to-date US vs
  foreign equity performance) were found only in broker/news commentary, not in a verified academic source, and need equity index data
  not in the repo. Not added; would need a human-supplied equity series and a verified source.

### B21: Post-08:30 NY release-window continuation, calendar-free (signal test, dev) → E026 · `done` (2026-11-09 R052: **NONE on dev**, -0.42 pips per event signed (n 169), CI (-5.278, 2.488), t p 0.564; x1.5 net -1.135; no lead, B21 line closed, B22 next. R051: pre-registered as E026, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-09 R050 refill)
- **Mechanism [PUB]:** macro news reaches exchange rates partly through subsequent order flow: about two-thirds of the news effect on
  DM/$ via order flow (Evans & Lyons 2008, JFE 88(1), 26-50) and "approximately one third of price-relevant information is incorporated
  via the trading process" (Love & Payne 2008, JFQA 43(2), 467-488); both VERIFIED (abstract) in research/academic_studies.md R050.
  Neither paper states a tradable post-release drift or its horizon (UNVERIFIED); the continuation hypothesis and every parameter below
  are fixed here, not taken from the papers.
- **Why calendar-free:** B12 (NFP) is blocked for lack of a sanctioned release-date source. Large moves in the 08:30-08:45 NY window
  occur mostly on US release days, so the jump size itself selects the events; no calendar needed. Price data in repo only.
- **Signal (fixed now):** J(D) = mid at 08:45 NY - mid at 08:30 NY on trading date D (quote = open of first bar in [T, T+5 min)), pips.
  D is an event if |J(D)| is strictly above the 90th percentile of |J| over the previous 60 valid trading dates (rolling, past only; no
  event until 60 exist). Dates with a missing 08:30 or 08:45 bar are invalid and counted.
- **Trade:** position sign(J(D)) from 08:45 NY to 10:45 NY on D (exit before the London 4pm fix at 11:00 NY). Signed return =
  sign(J) x (X - E) mid, pips. Missing exit excluded and counted; entry skipped (counted) if spread at 08:45 NY > 2.0 pips (SPEC 4).
- **Test:** **dev only, 1 trial**; n ~ 0.10 x ~1,500 dates ~ 140-150 events after burn-in.
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 10 events, 2000 draws, seed 0) 95%
  CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. SIGNAL earns B21v (val, same
  rule, val-only burn-in as E023/E025).
- **Descriptive (not in rule):** reversal reading (negative mean) logged as exploratory only; 08:45 -> 09:30 and 08:45 -> 12:00 NY
  horizons; p80 and p95 thresholds; share of events on first-Friday-of-month dates (NFP proxy, computable from dates alone) and the
  result on them; share on FOMC statement dates (data/calendars/fomc_dates.csv; none expected, statements at 14:00 NY); by year;
  median spread at entry/exit; net at bid/ask, SPEC 4 and costs x1.5.
- **Power note:** 2 h SD after a large release move ~20-25 pips -> SE ~1.8-2.1 pips; a mean of roughly 4 pips is needed to clear the
  CI bar. A NONE does not rule out a small effect.
- **Contamination note:** E006 tested the 08:35-09:30 NY window with E001 session predictors (not the 08:30 jump); E009 scanned
  unconditional hour means. No return conditional on the 08:30-08:45 move has been computed on dev. Record in the methodology.
- **Calendar label:** US 08:30 NY release window; the hold contains the 10:00 NY releases; exit before the London fix.
- **Data:** price data in repo only.

### B22: London-open intraday momentum into the pre-fix half hour (signal test, dev) → E027 · `done` (2026-11-09 R054: **NONE on dev**, -0.008 pips per date signed (n 1551), CI (-0.553, 0.455), t p 0.511; x1.5 net -0.685; no lead, B22 line closed, refill next. R053: pre-registered as E027, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-09 R050 refill)
- **Mechanism [PUB]:** in RUB/USD (Moscow exchange) the first half-hour return predicts the last half-hour return, attributed to
  liquidity providers' reluctance to hold positions overnight (Elaut, Frömmel & Lampaert 2018, JFM 37, 35-51); market intraday momentum in equities (Gao,
  Han, Li & Zhou 2018, JFE) and in futures including currencies (Baltussen et al. 2021, JFE); all VERIFIED (abstract) in
  research/academic_studies.md. EUR/USD has no exchange open/close; the London session is the analogue (the R000 entry flagged this as
  a loose analogue). Parameters below fixed here.
- **Signal (fixed now, London local time so DST mismatches do not shift it):** r1(D) = mid at 08:30 London - mid at 08:00 London on
  trading date D (quote = open of first bar in [T, T+5 min)), pips. Every valid date is an event (no threshold); r1 = 0 -> no trade,
  counted.
- **Trade:** position sign(r1) from 15:25 London to 15:55 London on D (the last half hour before the 16:00 London fix, exiting before
  the fix window). Signed return = sign(r1) x (X - E) mid, pips. Missing bars excluded and counted; entry skipped (counted) if spread
  at 15:25 London > 2.0 pips.
- **Test:** **dev only, 1 trial**; n ~ 1,500 dates.
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 20 events, 2000 draws, seed 0) 95%
  CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. SIGNAL earns B22v (val).
  The 1.0-pip bar is binding here (30-min SD ~6-8 pips -> SE ~0.2 pips): a statistically significant but sub-pip effect is WEAK at
  best, by design (costs ~0.5 pip round trip).
- **Descriptive (not in rule):** first-hour signal (08:00 -> 09:00 London) variant; predictive regression slope of last-half-hour
  return on r1; |r1| terciles; month-end dates separately (E007/B8 month-end fix flows); by year; spreads; net at bid/ask, SPEC 4, x1.5.
- **Contamination note:** E001 tested the sign of the whole London session return against 08:00-12:00 NY (NONE); E007 computed the
  unconditional 15:00-16:00 London pre-fix return on dev (NONE). No 15:25-15:55 London return conditional on the first London
  half-hour has been computed on dev. Record in the methodology.
- **Calendar label:** London open -> pre-London-fix half hour; overlaps US 10:00 NY releases only when US/UK DST differ (state count).
- **Data:** price data in repo only.

### B23: Intraday continuation on overreaction days (signal test, dev) → E028 · `done` (2026-11-09 R057: **NONE on dev**, +1.061 pips per event signed (n 74), CI (-5.625, 8.569), t p 0.390; x1.5 net +0.229; no lead, B23 line closed, B24 next. R056: pre-registered as E028, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-09 R055 refill)
- **Mechanism [PUB]:** Caporale & Plastun (2019, Brunel WP 19-09; entry in research/academic_studies.md, opened R055): on EURUSD
  overreaction days (open-to-close move beyond mean + 2 SD), "prices tend to change in the direction of the overreaction during the
  overreaction day"; their Strategy 1 follows the move from the identification hour (19:00 / 17:00 data clock) to day end, no costs.
  The paper's trigger uses the full-day return, not known in real time; the version below uses only information available at entry.
  Data-clock to NY mapping (19:00 data clock ~ 12:00 NY) is our assumption (UNVERIFIED). Parameters fixed here.
- **Signal (fixed now):** trading date D starts 17:00 NY (SPEC 2). r(D) = mid at 12:00 NY on D - mid at 17:00 NY at the start of D
  (quote = open of first bar in [T, T+5 min)), pips. Over the previous 60 valid trading dates (rolling, past only; no event until 60
  exist) compute mean m and SD s of r. D is an event if r(D) > m + 2s (positive) or r(D) < m - 2s (negative).
- **Trade:** position sign(r(D) - m) from 12:00 NY to 16:30 NY on D (exit before the 17:00 roll spread widening). Signed return =
  sign x (X - E) mid, pips. Missing bars excluded and counted; entry skipped (counted) if spread at 12:00 NY > 2.0 pips (SPEC 4).
- **Test:** **dev only, 1 trial**; n ~ 0.03-0.05 x ~1,500 dates ~ 45-75 events (a 2-SD tail; fat tails may give more).
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 5 events, 2000 draws, seed 0) 95%
  CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. SIGNAL earns B23v (val, same
  rule, val-only burn-in as E023/E025).
- **Descriptive (not in rule):** positive vs negative events separately (paper reports both); k = 1.5 and k = 2.5; reversal reading
  logged as exploratory only; share of events on FOMC statement dates and first-Friday dates; by year; spreads; net at bid/ask, SPEC 4,
  costs x1.5.
- **Power note:** 4.5 h SD on large-move days ~20-25 pips -> SE ~3 pips at n ~60; a mean of roughly 6 pips is needed to clear the CI
  bar. A NONE does not rule out a small effect.
- **Contamination note:** E024/E025 computed long 11:05 -> 16:00 NY on high prior-date-range dates (unsigned by the day's own move);
  E021 conditioned on the full 16:00 -> 16:00 move with a next-day hold. No 12:00 -> 16:30 NY return signed by the same-day
  17:00 -> 12:00 move has been computed on dev. Record in the methodology.
- **Calendar label:** post-London-fix afternoon (hold starts after the 11:00 NY fix; contains 14:00 NY FOMC statements on those dates).
- **Data:** price data in repo only.

### B24: Next-morning fade after an overreaction day (signal test, val only) → E029 · `done` (2026-11-10 R059: **NONE on val**, insufficient sample: 4 of 34 events tested, 19 skipped by the 2.0-pip entry spread at 17:05 NY (median event entry spread 3.6); no lead, B24 line closed, refill next. R058: pre-registered as E029, queued on research-batch; 1 val trial counted when it runs. Added 2026-11-09 R055 refill)
- **Mechanism [PUB]:** Caporale & Plastun (2019, as B23): after an overreaction day EURUSD "move[s] in the opposite direction on the
  following day", from the start of the day to the start of the European session (09:00 / 08:00 data clock, ~ 02:00 / 01:00 NY under our
  UNVERIFIED mapping); their Strategy 2 passed for positive days (t 2.45) and failed for negative days (t 1.23), no costs.
- **Why val only:** E021 (dev) logged the 16:00 -> 20:00 NY move after large 16:00 -> 16:00 days as descriptive (+1.666 pips reversal,
  p 0.034). That overlaps this hold (17:00 -> 20:00 NY), so dev is contaminated; the only clean test is val. Rejected relative: E021
  (20:00 NY -> 10:45 NY next date fade, dev NONE).
- **Signal (fixed now):** R(D) = mid at 16:55 NY on trading date D - mid at 17:00 NY at the start of D (open-to-close of the trading
  date, as the paper's open-to-close return), pips. Mean m and SD s of R over the previous 60 valid val trading dates (val-only burn-in,
  as E023/E025). D is an event if R(D) > m + 2s or R(D) < m - 2s. D on a Friday excluded and counted (weekend gap belongs to B17).
- **Trade:** position -sign(R(D) - m) from 17:05 NY (start of D+1, after the roll) to 02:00 NY on D+1 (before the Frankfurt/London
  open). Signed return = -sign x (X - E) mid, pips. Entry skipped (counted) if spread at 17:05 NY > 2.0 pips; missing bars excluded and
  counted. Report the median entry spread (roll hour spreads are wide).
- **Test:** **val only, 1 trial**; val 2021-01-21 to 2023-06-30 ~ 620 dates minus 60 burn-in -> n ~ 15-35 events. Low power, stated up front.
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 5 events, 2000 draws, seed 0) 95%
  CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. A val-only SIGNAL cannot meet the
  LEAD definition (no clean dev pass): it is logged, and any further test (OOS) needs a human decision (AUTONOMOUS_PROTOCOL).
- **Descriptive (not in rule):** positive vs negative days separately; exit 03:00 NY; by year; spreads; net at bid/ask, SPEC 4, x1.5.
- **Calendar label:** Asian session after a large NY day; contains the Tokyo fix (19:55 NY / 20:55 NY by DST).
- **Data:** price data in repo only.
- **Order:** B23 first (clean dev test, paper's stronger result); B24 second.

### Refill note R060 (not an item)
- Popović & Đurović (2014, Applied Economics 46(32), 3968-3979, DOI 10.1080/00036846.2014.948676; abstract opened R060) report
  an EUR/USD Friday anomaly: buy EUR at 00:00, sell at 03:00 (hourly Swiss-market data 2004-2014; time zone not stated, UNVERIFIED).
  Under a Zurich-time reading this is trading-date Friday 18:00-21:00 NY, which E009 already scanned on dev (Fri_ny_18..20 means
  +0.685, -0.471, +0.021 pips, all NONE): dev is contaminated and does not support it, the time zone is unknown, and val would be the
  only clean test of a claim dev already fails to show. Not added.
- Zheng (2023, UChicago Booth JMP "Dividend Flows and the Foreign Exchange Rate", PDF opened R060): local currency depreciates vs USD
  after large dividend payment dates (G10, 2001-2023, ~4.70 bp after two days). Needs a dividend-payment calendar not in the repo; not
  added. A year-end USD effect it cites (Fei 2023) was seen only second-hand: UNVERIFIED, not added.

### B25: USD appreciation into the Tokyo fix on gotobi days (signal test, dev) → E030 · `done` (2026-11-10 R062: **NONE on dev**, +0.180 pips per event signed (n 458), CI (-0.552, 1.245), t p 0.322; non-gotobi control +0.411; SPEC 4 net -0.353, x1.5 -0.619; no lead, B25 line closed, B26 next. R061: pre-registered as E030, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-10 R060 refill)
- **Mechanism [PUB]:** Ito & Yamada (2017, JIE 109, 214-234, DOI 10.1016/j.jinteco.2017.09.005; NBER WP 22820, abstracts opened
  R060): customer order flow before the Tokyo fix is biased toward buying dollars, giving a predictable price pattern, and "calendar
  effects also matter for determination of the fixing rate and the price fluctuation around fixing time". The gotobi definition
  and any gotobi magnitude in the paper could NOT be read (full-text PDF fetch was not permitted): the day rule below is the common
  practitioner convention and is UNVERIFIED as the paper's. The paper studies USD/JPY; EUR/USD is the USD leg only (loose transfer,
  stated up front).
- **Why now:** E011 (dev) tested the Tokyo fix on all dates (pre WEAK +0.32 pips, CI incl 0) and explicitly left the gotobi subset
  untested (E011 hypothesis.md). No gotobi split has been computed on dev or val.
- **Gotobi dates (fixed now):** Tokyo calendar date G is gotobi if its day of month is 5, 10, 15, 20, 25 or 30, or it is the last
  calendar day of the month; if such a day is a Saturday or Sunday, the gotobi date is the preceding Friday (if that Friday is not
  already gotobi). Japanese public holidays are not in the repo and are not shifted (state the count of such dates as a limitation
  where computable; none adjusted).
- **Trade (same windows as E011):** short EUR/USD from 08:55 to 09:55 Asia/Tokyo on gotobi Tokyo dates (quote = open of first bar in
  [T, T+5 min), as E011). Signed return = -(X - E) mid, pips. Missing bars excluded and counted; entry skipped (counted) if spread at
  08:55 Tokyo > 2.0 pips (E011 median entry spread 0.4).
- **Test:** **dev only, 1 trial**; n ~ 0.30 x ~1,560 Tokyo dates ~ 450-470 events.
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 20 events, 2000 draws, seed 0)
  95% CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. SIGNAL earns B25v
  (val, same rule).
- **Descriptive (not in rule):** non-gotobi control (same window); 5/10th-day subsets separately from month-end gotobi; weekend-shifted
  dates separately; 09:25 -> 09:55 Tokyo last half hour; by year; spreads; net at bid/ask, SPEC 4, costs x1.5.
- **Power note:** E011 pre-window mean abs move 6.4 pips -> SD ~8 pips -> SE ~0.4 pips at n ~460; the 1.0-pip bar is binding, so a
  significant sub-pip effect is WEAK at best, by design.
- **Contamination note:** E011 published the all-date pre-fix mean (+0.321, n 1560) on dev; gotobi dates are ~30% of those dates, so
  the all-date number bounds but does not reveal the subset. Record in the methodology.
- **Calendar label:** Tokyo 09:55 JST fix (= 19:55 NY in EST, 20:55 NY in EDT, previous NY calendar date; same trading date as the
  Tokyo date); month-end gotobi dates overlap B8/E007 month-end themes (different window).
- **Data:** price data in repo only; gotobi dates computed from the calendar.

### B26: USD depreciation after the Tokyo fix on gotobi days (signal test, dev) → E031 · `done` (2026-11-10 R064: **WEAK on dev**, +0.799 pips per event signed (n 460), CI (-0.154, 1.632), t p 0.024; non-gotobi control +0.778 (difference +0.021); SPEC 4 net +0.290, x1.5 +0.036; no lead, B26 line and gotobi Tokyo-fix line closed on dev, refill next. R063: pre-registered as E031, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-10 R060 refill)
- **Mechanism [PUB]:** as B25 (Ito & Yamada 2017): fix-time price spikes driven by predictable dollar-buying order imbalance imply a
  partial reversal once the imbalance is filled; strongest where the imbalance is largest (gotobi, UNVERIFIED as the paper's
  finding). E011 (dev) found the all-date post-fix reversal WEAK (+0.785 pips, CI (0.318, 1.173), below the 1-pip bar).
- **Trade:** long EUR/USD from 09:55 to 10:55 Asia/Tokyo on gotobi Tokyo dates (definition exactly as B25). Signed return = (X - E)
  mid, pips. Exclusions and spread cap as B25.
- **Test:** **dev only, 1 trial** (separate trial from B25, as E011 counted pre and post separately); n ~ 450-470.
- **Decision rule (draft):** as B25 (mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND one-sided t p < 0.05 -> SIGNAL; WEAK /
  NONE as B25). SIGNAL earns B26v (val).
- **Descriptive (not in rule):** non-gotobi control; subsets as B25; post-fix return conditional on the sign of the pre-fix move
  (exploratory only); by year; spreads; net at bid/ask, SPEC 4, x1.5.
- **Contamination note:** E011 published the all-date post-fix mean (+0.785, n 1560) on dev; the gotobi subset was not computed.
  Because the all-date effect is already positive, a gotobi SIGNAL must also beat the non-gotobi control descriptively to be
  interesting; this does not change the rule. Record in the methodology.
- **Calendar label:** post-Tokyo-fix hour; Asian session.
- **Data:** price data in repo only.
- **Order:** B25 first (paper's primary claim: dollar-buying into the fix); B26 second.

### Refill note R065 (not an item)
- FOMC pre-announcement drift (Karnaukh 2018, already in academic_studies.md: unconditional "neutral meeting" USD drift down of
  5-10 bp from 14:00 two days before to 14:00 on announcement day; Neuhierl & Weber 2017 "Monetary Momentum", Chicago Booth page
  opened R065, abstract says the drift is present in "the US-dollar exchange rate"): not added. Only 47 scheduled statements on dev and
  20 on val, and lesson 2026-11-08 (E014) says val cannot confirm an effect of the published size for 8/yr events; the window also
  overlaps the published E013 window (16:00 NY t-1 -> 13:55 NY t). Lucca & Moench (2015) could not be opened (NY Fed page timed out).
- Turn-of-month (Kumar 2015 IJMF 11(2) 232-243, DOI 10.1108/IJMF-05-2014-0068; Kumar 2018 SEF 35(3) 441-456, DOI
  10.1108/SEF-08-2015-0192; RePEc abstracts opened R065): INR pairs / 20 USD pairs, sign convention not stated in the abstracts, and
  the 2018 paper says calendar anomalies "seem to have disappeared for almost all currencies during 2005 to 2014". Not added.
- Krohn-Mueller-Whelan unconditional **pre-ECB** window (short EUR/USD 02:00 -> 08:15 NY, all dates): dev is already known in
  aggregate (E009 ny_02..ny_07 cells) and val is contaminated by E023's descriptive split (high-vol +1.197 and normal +1.15 val dates).
  Only the locked OOS block is clean, which needs a human decision. Not added; listed for the human in agent_decision_log R065.
- KMW **pre-Tokyo** window (17:00 -> 20:55 NY, short EUR): entry at the 17:00 NY roll is not tradable at the SPEC 4 spread cap
  (lesson R059, median 17:05 spread 3.6 pips) and the dev E009 cells for 17:00-20:00 NY sum to about +0.8 pips (wrong sign). Not added.

### B27: Post-Tokyo-fix EUR appreciation, KMW window 20:55 -> 02:00 NY (signal test, val only) → E032 · `done` (2026-11-10 R067: **NONE on val**, -0.534 pips per date signed (n 636), CI (-1.606, 0.669), t p 0.830; SPEC 4 net -1.106, x1.5 -1.392; no lead, not an OOS candidate, B27 closed, refill next. Added 2026-11-10 R065 refill; pre-registered R066)
- **Mechanism [PUB]:** Krohn, Mueller & Whelan (JF 2024, 79(1) 541-578; Bank of Canada SWP 2021-48 PDF opened R065, first ~40k
  characters verbatim): "an appreciation of the U.S. dollar pre-fix and a depreciation post-fix", explained by dealers hedging an
  unconditional dollar demand at the fixes ("Dealers hedge this demand pre-fix, driving intraday reversals"). The paper's window,
  verbatim: post-Tokyo = 8:55 p.m. to 2:00 a.m. ET; 5-minute Refinitiv mid-quotes, 1999-2019, EUR included. The EUR post-Tokyo
  magnitude (+5.89% p.a., t 9.29) was read only through a model summary: **UNVERIFIED**. Robustness, verbatim: "not driven by day
  of the week or month of the year effects".
- **Why now / why val only:** the full post-Tokyo window has never been tested as its own trial. E011 (dev) tested only the first hour
  after the fix (09:55 -> 10:55 Tokyo, +0.785 WEAK); B25/B26 tested gotobi subsets (dev). On dev the window is effectively already
  known: E009 published every NY-hour cell (ny_21 +0.655, ny_22 +0.591, ny_23 -0.027, ny_00 +0.197, ny_01 -0.240; sum about +1.18
  pips), so a dev test would be contaminated. Val has not been computed for this window by any experiment (E029's val window
  17:05 -> 02:00 NY used 4 conditional events only; record this in the methodology). Precedent: B14/E017, B24/E029 (val only).
- **Trade:** long EUR/USD from 20:55 to 02:00 America/New_York on every valid val trading date (entry = the evening that belongs to
  trading date D under `sessions.trading_date`; exit 02:00 NY the next calendar morning, same trading date). Quote = open of the first
  bar in [T, T+5 min) (E011 rule). Signed return = (X - E) mid, pips. Fridays-evening entries do not exist (weekend); Sunday-evening
  entries included. Missing bars excluded and counted; require >= 280 of the 305 one-minute bars in the window (coverage cap fixed now);
  entry skipped (counted) if spread at 20:55 NY > 2.0 pips.
- **Clock note (fixed now, before data):** the paper's window is used verbatim in New York clock time. 20:55 NY = 09:55 JST (the
  Tokyo fix) in EDT but 10:55 JST in EST; the window therefore starts at the fix in summer and one hour after it in winter. Not
  adjusted; DST split reported descriptively only.
- **Test:** **val only (2021-01-21..2023-06-30), 1 trial**; n ~ 600 dates.
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 20 dates, 2000 draws, seed 0)
  95% CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE. < 200 valid dates ->
  NONE (insufficient sample).
- **What a SIGNAL means:** it cannot be a LEAD under AUTONOMOUS_PROTOCOL (no clean pre-registered dev SIGNAL exists, dev being
  contaminated by E009). A val SIGNAL that also survives costs x1.5 is logged in agent_decision_log.md as an **OOS candidate for the
  human** (no notification, no OOS run); nothing else is queued on it.
- **Descriptive (not in rule):** EDT vs EST dates; first hour (20:55 -> 21:55) vs rest; by weekday; by year; Mondays-after-weekend
  (Sunday-evening entries) separately; entry/exit spreads; net at bid/ask, SPEC 4, costs x1.5.
- **Power note:** dev hourly SDs in this window are ~6-9 pips (E009), so a 5-hour SD of roughly 15-20 pips; SE ~0.7-0.8 pips at
  n ~600 before block correction. The 1.0-pip bar plus CI lower > 0 needs a val mean of roughly 1.6+ pips; the dev-implied +1.2 would
  be WEAK at best, by design.
- **Cost note:** E011 median spread at the Tokyo fix 0.4 pips; SPEC 4 round trip ~0.5 pips (E030 gross-net gap 0.53). A +1.2-pip
  gross would leave ~+0.4 at x1.5: thin.
- **Calendar label:** post-Tokyo-fix window; Asian session. Overlaps the Tokyo fix (E011, B25/B26) by design.
- **Data:** price data in repo only.
