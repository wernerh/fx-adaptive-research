# Research backlog

Ordered by priority. Status: `ready` | `running` | `done` | `blocked` | `parked`.
Autonomous runs take the top `ready` item (docs/AUTONOMOUS_PROTOCOL.md). Add items at the bottom; re-rank only with a
reason in agent_logs/agent_decision_log.md. Dev = 2015-01-01..2020-12-31, val = 2021-01-21..2023-06-30, OOS locked.

Trial count so far on dev: **256** (E001: 7, E006: 14, E004: 1, E007: 4, E008: 4, E009: 192 exploratory cells, E010: 2, E011: 2, E013: 1, E018: 1, E019: 1, E020: 1, E021: 1, E022: 1, E024: 1, E026: 1, E027: 1, E028: 1, E030: 1, E031: 1, E033: 2, E034: 2, E035: 2, E037: 2, E038: 1, E039: 2, E040: 1, E041: 1, E042: 1, E043: 1, E044: 1, E045: 1, E046: 1). Val-only trials: **9** (E012: 2, E014: 1, E017: 1, E023: 1, E025: 1, E029: 1, E032: 1, E036: 1). Total registered trials: **265**. Update after every experiment. (R111: E046 ran, dev +1; B55 closed unearned, 0 trials. R107: refill pass, no item added, 0 trials. R106: refill pass, no item added, 0 trials. R105: refill pass, no item added, 0 trials. R104: E045 ran, dev +1; B53 closed unearned, 0 trials. R103: E045/B52 pre-registered, 1 dev trial counted when it runs. R101: E044 ran, dev +1; B51 closed unearned, 0 trials. R100: E044/B50 pre-registered, 1 dev trial counted when it runs. R099: refill added B50 (1 dev trial when it runs), B51 (blocked): 0 trials. R098: E043 ran, dev +1; B49 closed unearned, 0 trials. R097: E043/B48 pre-registered, 1 dev trial counted when it runs. R096: refill added B48 (1 dev trial when it runs), B49 (blocked): 0 trials. R095: E042 ran, dev +1; B47 closed unearned, 0 trials. R094: E042/B46 pre-registered, 1 dev trial counted when it runs. R092: E041 ran, dev +1. R091: E041/B45 pre-registered, 1 dev trial counted when it runs. R090: E040 ran, dev +1; B44 closed unearned, 0 trials. R089: E040/B43 pre-registered, 1 dev trial counted when it runs. R087: E039 ran, dev +2; B42 closed unearned, 0 trials. R086: E039/B40+B41 pre-registered, 2 dev trials counted when it runs (0 if BLOCKED). R084: E038 ran, dev +1; B39 closed unearned, 0 trials. R083: E038/B38 pre-registered, 1 dev trial counted when it runs. R082: refill added B38 (1 dev trial when it runs), B39 (blocked): 0 trials. R081: E037 ran, dev +2; B37 closed unearned, 0 trials. R080: E037/B35+B36 pre-registered, 2 dev trials counted when it runs. R079: refill added B35, B36 (2 dev trials when they run), B37 (blocked): 0 trials. R078: E036 ran, val +1. R077: E036/B34 pre-registered, 1 val trial counted when it runs. R076: E035 ran, dev +2; B33 SIGNAL earns B34 (1 val trial when it runs). R075: E035/B32+B33 pre-registered, 2 dev trials counted when it runs. R074: refill added B32, B33 (2 dev trials when they run), B34 (blocked): 0 trials. R073: E034 ran, dev +2. R072: E034/B30 pre-registered, 2 dev trials counted when it runs. R071: refill added B30 (2 dev trials when it runs), B31 (blocked): 0 trials. R070: E033 ran, dev +2. R069: E033/B28+B29 pre-registered, 2 dev trials counted when it runs. R068: refill added B28, B29: 0 trials until pre-registered. R067: E032 ran, val +1. R066: E032/B27 pre-registered, 1 val trial counted when it runs. R065: refill added B27: 0 trials until pre-registered. R064: E031 ran, dev +1. R063: E031/B26 pre-registered, 1 dev trial counted when it runs. R062: E030 ran, dev +1. R061: E030/B25 pre-registered, 1 dev trial counted when it runs. R060: refill added B25, B26: 0 trials until pre-registered. R059: E029 ran, val +1. R058: E029/B24 pre-registered, 1 val trial counted when it runs. R057: E028 ran, dev +1. R056: E028/B23 pre-registered, 1 dev trial counted when it runs. R054: E027 ran, dev +1. R053: E027/B22 pre-registered, 1 dev trial counted when it runs. R052: E026 ran, dev +1. R051: E026/B21 pre-registered, 1 dev trial counted when it runs. R050: refill added B21, B22: 0 trials until pre-registered. R049: E025 ran, val +1. R048: E025/B20v pre-registered, 1 val trial counted when it runs. R047: E024 ran, dev +1; B20v added, 0 trials until pre-registered. R045: E023 ran, val +1. R044: E023/B19v pre-registered, 1 val trial counted when it runs. R043: E022 ran, dev +1; B19v added, 0 trials until pre-registered. R042: E022/B19 pre-registered, 1 dev trial counted when it runs. R041: refill added B19, B20: 0 trials until pre-registered. R040: E021 ran, dev +1. R039: E021/B18 pre-registered, 1 dev trial counted when it runs. R038: E020 ran, dev +1. R037: E020/B17 pre-registered, 1 dev trial counted when it runs. R036: refill added B17, B18: 0 trials until pre-registered. R035: E019 ran, dev +1. R034: E019/B16 pre-registered, 1 dev trial counted when it runs. R033: E018 ran, dev +1. R032: E018/B15 pre-registered, 1 dev trial counted when it runs. R031: refill added B15, B16: 0 trials until pre-registered. R030: E017 ran, val +1. R029: E017/B14 pre-registered, 1 val trial counted when it runs. R028: E016/B13 blocked after second CME fetch failure, 0 trials. R027: E016 phase-1 re-fetch queued, 0 trials. R026: E016/B13 pre-registered, 1 dev trial counted when phase 2 runs. R025: refill added B13, B14: 0 trials until pre-registered. R023: E015/B12 pre-registered, 1 dev trial counted when phase 2 runs. R022: E014 ran, val +1. R020: E013 phase 2 ran, dev +1. R016 refill added B11, B12: 0 trials until pre-registered. R017: E013/B11 pre-registered, 1 dev trial counted when phase 2 runs.)

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

### Refill note R068 (not an item)
- Borisenko & Pozdeev (2017 WP, PDF opened R068): currencies drift toward the expected rate decision over the ~10 days before a policy
  change, nothing before no-change meetings. Not added: needs OIS-implied expectations (not in repo; conditioning on the realised decision
  is look-ahead), and dev has almost no ECB rate changes and ~14 Fed changes, too few events (lesson 2026-11-08 E014).
- Same-time-of-day return persistence (Heston-Korajczyk-Sadka style, equities): no FX source found that tests return direction
  (two candidate papers opened were about volatility / zero returns). E009 hour cells already describe dev; lesson R067 says summed
  hour cells are a weak prior. Not added.
- Osler (2003) round-number reversals: the touch events largely coincide with B15/E018 crossing events (continuation ~0 on dev), so a
  reversal test is not new information. Not added.

### B28: Next-day reversal after a low-unexpected-volume day (signal test, dev) → E033 · `done` (2026-11-10 R070: **NONE on dev**, -2.034 pips per event signed (n 426), CI (-6.772, 3.013), t p 0.789; SPEC 4 net -2.73, x1.5 -3.078; no lead, B28 closed, refill next. Added 2026-11-10 R068 refill; pre-registered R069)
- **Mechanism [PUB, secondary source]:** Cespa, Gargano, Riddiough & Sarno, "Foreign exchange volume" (RFS; JBS summary opened R068,
  journal details UNVERIFIED): when unexpected volume (deviation from a 21-day moving average) is "abnormally low" there is "a return
  reversal over the following day" (liquidity-driven price pressure that is not information, cf. Campbell-Grossman-Wang). Their volume is
  CLS traded volume; ours is Dukascopy's single-venue volume field (`volume`, mapped from `bid_volume` in data.py): a proxy, stated as a
  limitation.
- **Volume gate (fixed now, checked first on the runner):** if `volume` is missing, or zero/NaN on > 1% of dev bars, the experiment stops
  as BLOCKED with 0 trials used; nothing else is computed.
- **Signal (fixed now):** trading date D (17:00 NY roll, `sessions.trading_date`) is valid if >= 1,300 of its 1,440 one-minute bars exist.
  V(D) = sum of `volume` over D's bars. UV(D) = V(D) / mean(V over the previous 21 valid trading dates) - 1 (past only). D is
  "low volume" if UV(D) is strictly below the 33rd percentile of UV over the previous 60 valid trading dates (rolling, past only).
  R(D) = mid at 16:55 NY on D - mid at the first bar of D (17:00 NY), pips (E011 quote rule: open of first bar in [T, T+5 min)).
- **Trade:** position -sign(R(D)) from 20:00 NY (start of trading date D+1, after the roll spread normalises, lesson R059) to 16:55 NY on
  D+1. D on a Friday excluded and counted (weekend gap, B17). R(D) = 0 skipped. Missing entry/exit bars excluded and counted; entry skipped
  if spread at 20:00 NY > 2.0 pips.
- **Test:** **dev only**, n ~ 0.33 x ~1,200 non-Friday valid dates after burn-in ~ 380 events. Shares one experiment with B29 (2 trials,
  precedent E012).
- **Decision rule (draft):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 10 events, 2000 draws, seed 0) 95%
  CI lower > 0 AND one-sided t-test p < 0.025 (Bonferroni for 2 trials). WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE.
  < 150 events -> NONE (insufficient sample). SIGNAL earns B28v (val, its own experiment).
- **Descriptive (not in rule):** mid- and high-UV terciles' reversal means (high tercile is B29's statistic: compute both in the same run);
  share of events that are also E021-type large-move events (|16:00-16:00 R| > rolling p80) and the result excluding them; correlation of
  UV with the daily range (volume proxies volatility); by year; entry/exit spreads; net at bid/ask, SPEC 4 and costs x1.5.
- **Power note:** ~21 h hold, SD roughly 40-45 pips -> SE ~2.2 pips at n ~380; a mean of roughly 4.5+ pips is needed for the CI bar.
- **Contamination note:** volume has never been used by any experiment (grep R068). E021 (dev) computed next-session returns after large
  |R| moves (NONE, -2.55 signed reversal); conditioning on volume is a different variable, but high-UV days overlap large-move days: report
  the overlap. Record in the methodology.
- **Calendar label:** daily-frequency volume-conditioned reversal; the hold contains Tokyo/ECB/London fixes and US releases.
- **Data:** price + volume data in repo only (Dukascopy via the research-batch runner).

### B29: Next-day continuation after a high-unexpected-volume day (signal test, dev) → E033 · `done` (2026-11-10 R070: **NONE on dev**, -0.213 pips per event signed (n 391), CI (-6.616, 4.78), t p 0.528; SPEC 4 net -0.894, x1.5 -1.234; no lead, B29 closed, refill next. Added 2026-11-10 R068 refill; pre-registered R069)
- **Mechanism [PUB, secondary source]:** same source as B28: the reversal "weakens and moves toward a next-day continuation of the same
  direction of returns when volume is particularly high" (informed trading revealed by volume, cf. Llorente-Michaely-Saar-Wang).
  Weaker published claim than B28 ("moves toward"), so lower prior.
- **Signal / trade:** as B28, but D is "high volume" if UV(D) is strictly above the rolling 67th percentile of the previous 60 valid dates,
  and the position is +sign(R(D)) from 20:00 NY to 16:55 NY on D+1. Same volume gate, validity, Friday, spread and missing-bar rules.
- **Test:** **dev only**, run in the same experiment as B28 (2 trials total). Rule as B28 (mean > 1.0 pip, block-10 CI lower > 0,
  t p < 0.025; < 150 events -> NONE). SIGNAL earns B29v (val).
- **Descriptive (not in rule):** as B28, including the E021 overlap (large-move days are expected to be high-UV; E021's reversal reading
  was -2.55 signed, i.e. slight continuation, published: record that this item's prior is partly contaminated by E021).
- **Data:** as B28.

### Refill note R071 (not an item)
- Sources opened R071: Melvin & Prins (2015) IDEAS/RePEc abstract page (https://ideas.repec.org/a/eee/finmar/v22y2015icp50-72.html,
  DOI 10.1016/j.finmar.2014.11.001); Marsh, Panagiotou & Payne (2017, "The WMR Fix and its Impact on Currency Markets", preliminary,
  Norges Bank PDF https://www.norges-bank.no/contentassets/619c8b75e1ed4ba691e8ad6a006855e6/39-panagiotou---the-wmr-fix-and-its-impact-on-currency-markets-.pdf,
  first ~40% read verbatim). The Melvin-Prins slides (ECB 2013 FX workshop) and the full paper could not be opened: the paper's exact
  signal, window, index choice and EUR/USD magnitude are **UNVERIFIED**.
- Data check R071: dukascopy-node 1.51.1 (the version the workflow installs) lists `eusidxeur` (EU Stocks 50, minute candles from
  2014-06-01) and `usa500idxusd`; both can be downloaded on the runner. No other index data is in the repo.
- Hau & Rey (2006) portfolio-rebalancing / uncovered equity parity: contemporaneous equity-FX correlation, no stated next-day
  predictability; not added (search result only, abstract not opened).
- Marsh-Panagiotou-Payne: GBP/AUD/NZD only (2010-2013), post-fix one-minute reversal below the tradable horizon; not added.

### B30: Month-end pre-fix equity-hedging flow, Melvin-Prins (signal test, dev) → E034 · `done` (2026-11-10 R073: **NONE/NONE on dev**, HOUR +1.731 pips signed (n 71), CI (-4.152, 7.559), t p 0.285; DAY +3.354 (n 71), CI (-9.322, 15.498), t p 0.300; below unconditional long +3.076 / +12.501; no lead, B30 closed, B31 closed unearned, refill next. Added 2026-11-10 R071 refill; pre-registered R072: index holiday fallback of up to 5 days back and first-month exclusion fixed before data, see E034 methodology)
- **Mechanism [PUB]:** Melvin & Prins (2015, JFM 22, 50-72; abstract opened R071), verbatim: "equity market appreciation over the month
  can be used to predict currency depreciation before the end-of-month fix" (hedgers of foreign equity holdings rebalance FX hedges at
  the month-end 4pm London fix; direction identified by past equity returns). Marsh-Panagiotou-Payne (2017) describe the result as a
  country's equity outperformance "relative to other markets" giving "a statistically significant and negative effect" on its currency
  before the last fix (secondary description). Exact signal construction and EUR/USD magnitude: **UNVERIFIED**.
- **Signal (fixed now):** D = last valid trading date of each calendar month (E007 definition). S(D) = log return of EUS.IDX/EUR mid
  minus log return of USA500.IDX/USD mid, each from 16:00 London on the last trading date of the previous month to 16:00 London on D-1
  (past only; quote = open of first bar in [T, T+5 min), E011 rule). Position = -sign(S): EU equities outperformed -> short EUR/USD;
  US outperformed -> long EUR/USD. S = 0 skipped.
- **Trades (2 pre-registered windows, one experiment, 2 trials):** (a) **B30-hour:** 15:00 -> 16:00 London on D (pre-fix hour, same
  window as E007 `pre_month_end`); (b) **B30-day:** 16:00 London D-1 -> 16:00 London D. Entry skipped (counted) if spread > 2.0 pips;
  missing bars excluded and counted.
- **Data gate (checked first on the runner, 0 trials if it fails):** if either index series is missing at a required quote time for
  > 5% of dev month-ends, stop as BLOCKED. Index data downloaded on GitHub Actions only (dukascopy-node `eusidxeur`, `usa500idxusd`,
  m1 bid+ask, 2014-12..2020-12).
- **Test:** **dev only**, n ~ 72 month-ends. Decision rule (draft), per window: SIGNAL if mean signed return > 1.0 pip AND iid bootstrap
  (block 1, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.025 (Bonferroni for 2 trials). WEAK if mean > 0 and (CI
  lower > 0 or p < 0.025); else NONE. < 50 events -> NONE (insufficient sample). SIGNAL earns B30v (val, own experiment).
- **Power note:** E007 month-end pre-fix hour SD 19.7 pips -> SE ~2.3 at n 72, so a mean of ~5 pips is needed; the full day has a
  larger SD (~50 pips, estimate to be reported). Val has only ~29 month-ends, so even a dev SIGNAL is unlikely to be confirmable on val
  (lesson 2026-11-08 E014). The published effect size is unknown here (lesson R070 asks for a stated effect size): lower priority than
  an item that has one, but it is the only item in the queue.
- **Contamination note:** E007 published the unconditional dev month-end pre-fix hour (`pre_month_end`, short, -2.771 pips, i.e.
  EUR/USD rose on average) and post-fix hour (B8, parked). Conditioning on the equity signal has never been computed; report the
  unconditional mean beside the conditional one. B8 stays parked.
- **Descriptive (not in rule):** |S| above vs below median; EU-only and US-only legs of S; quarter-ends vs other months; by year; 16:00
  -> 17:00 London post-fix hour under the same position (reversal check, not a trial); spreads; net at bid/ask, SPEC 4, costs x1.5.
- **Calendar label:** month-end London 4pm fix (WMR). The fix *is* the strategy (AUTONOMOUS_PROTOCOL lead criterion 4).
- **Data:** EUR/USD in repo + two Dukascopy index CFDs (new download step in the workflow; cache key must change).

### B31: Month-end equity-hedging flow, val confirmation (signal test, val only) · `done` (2026-11-10 R073: closed unearned, B30 returned NONE in both windows; 0 trials. Added 2026-11-10 R071; earned only if B30 returns SIGNAL)
- Same signal, the window(s) that returned SIGNAL on dev, val only (~29 month-ends, < 20 events -> NONE), rule unchanged. Power is low
  by construction; a val NONE after a dev SIGNAL closes the line (precedent E014).

### Refill note R074 (not an item)
- Sources opened R074 (web-fetch, first ~40% of each PDF verbatim, the rest model-summarised and treated as UNVERIFIED):
  Krohn, Mueller & Whelan, "Uncovered Interest Parity in High Frequency" (first version Nov 2024,
  https://jbs.cam.ac.uk/wp-content/uploads/2024/11/uncovered-interest-parity-in-high-frequency.pdf); Lou, Polk & Skouras, "The Day
  Destroys the Night, Night Extends the Day" (LSE FMG DP 961, July 2026, https://www.fmg.ac.uk/sites/default/files/2026-07/DP961.pdf).
- Not used: Marsh & Miao (2012, EJF 18(9), City PDF opened) tests FX order flow -> equity, not equity -> FX, 25 days in 2005; Kloks,
  Mattille & Ranaldo "Hunting for Dollars" (2024, ECB PDF opened) studies FX swaps/basis at quarter-ends, not spot; Jiang (2019)
  "Currency Returns in Different Time Zones" could not be opened (Kellogg page served a generic listing): UNVERIFIED, not used.
- KMW-UIP **unconditional** intraday long EUR/USD 07:00 -> 17:00 ET: per-currency EUR means (overnight -1.71 bp, intraday +2.03 bp)
  are summary-only (UNVERIFIED). Dev is known in aggregate via E009 hour cells, and val is largely seen (E017 legs 03:00-08:00 and
  12:00-17:00 NY, E001/E006 08:00-12:00 NY). Same situation as the R065 pre-ECB window: only the locked OOS block is clean. Not added;
  listed for the human in agent_decision_log R074.
- FX announcement-day carry (KMW-UIP: >60% of carry returns on FOMC/macro days) needs the release calendar (B6/B12 blocked). Not added.

### B32: Overnight -> intraday reversal, daily (signal test, dev) → E035 · `done` (2026-11-10 R076: NONE, n 1554, mean -0.285 pips, CI (-2.421, 1.843); closed) (Added 2026-11-10 R074 refill; one experiment with B33, 2 trials; pre-registered R075, rule unchanged)
- **Mechanism [PUB, partly]:** Krohn, Mueller & Whelan (UIP in High Frequency, 2024 WP, opened R074), verbatim: the Fama slope
  "switches from a positive value of 1.32 ... during the overnight hours, to -1.28 during the intraday period"; overnight = 17:00 ET t-1
  -> 7:00 ET t, intraday = 7:00 -> 17:00 ET; they read this as different clienteles pricing currencies at different times. Lou, Polk &
  Skouras (2026, opened R074) find for US equities that intraday returns mean-revert past overnight returns ("t-statistic of -3.98"),
  but with a smoothed multi-year signal. **Our test is an FX daily analogue, not a replication:** neither paper reports that a single
  EUR/USD overnight move reverses intraday. Prior: weak; a clean NONE is informative.
- **Definitions (fixed now):** for trading date D, r_on = EUR/USD mid return from 17:05 America/New_York on the evening that opens D
  (Sunday 17:05 for Mondays) to 07:00 NY on D; r_id = mid return 07:00 -> 16:55 NY on D (16:55 avoids the 17:00 roll, lesson R059).
  Quotes = open of first bar in [T, T+5 min) (E011 rule). Signed return = -sign(r_on) x r_id (fade the overnight move). r_on = 0 skipped.
  Entry skipped (counted) if the 07:00 NY spread > 2.0 pips; missing bars excluded and counted.
- **Test:** **dev only**, every valid trading date (n ~ 1,500). Decision rule (draft): SIGNAL if mean signed return > 1.0 pip AND
  moving-block bootstrap (block 20 dates, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.025 (Bonferroni for the
  2 trials B32+B33). WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE. < 500 dates -> NONE (insufficient sample).
  SIGNAL earns B34 (val confirmation, own experiment); not a lead until then.
- **Power note:** 07:00 -> 16:55 NY SD likely ~45 pips (report it) -> SE ~1.2 pips at n 1,500; the p < 0.025 bar binds near +2.4 pips.
- **Contamination note:** E009 published unconditional hour means on dev (no sign-agreement statistic); E021 (fade large daily moves
  from 20:00 NY), E027 (London-open sign -> pre-fix half hour) and E028 (2-SD 17:00 -> 12:00 moves) use different predictors/windows.
  The overnight-sign conditional statistic has never been computed. Record this in the methodology.
- **Descriptive (not in rule):** continuation reading (sign); |r_on| terciles; OLS slope of r_id on r_on; unconditional long r_id
  (KMW-UIP intraday direction, descriptive only); Mondays vs other days; by year; spreads; net at bid/ask, SPEC 4, costs x1.5.
- **Calendar label:** contains the London 4pm fix (11:00 NY), the 08:30 NY releases and 10:00 NY option cut; not a fix strategy.
- **Data:** EUR/USD price data in repo only.

### B33: Smoothed overnight -> intraday reversal, 20-date signal (signal test, dev) → E035 · `done` (2026-11-10 R076: SIGNAL, n 1536, mean +2.695 pips, CI (0.47, 5.027), t p 0.0093; earns B34) (Added 2026-11-10 R074 refill; same experiment as B32; pre-registered R075, rule unchanged)
- **Mechanism [PUB, partly]:** as B32; closer to Lou-Polk-Skouras, whose predictor is a *smoothed* history of overnight returns
  (their EWMA has a ~10-year centre of mass on monthly data, impossible on 6 dev years; a 20-date window is our choice, fixed now).
- **Signal (fixed now):** O20(D) = sum of r_on over the 20 previous valid trading dates D-20..D-1 (excludes D's own overnight; dates
  with missing r_on are skipped, the window extends back to collect 20 values; first 20 dev dates are burn-in, counted). Position =
  -sign(O20); signed return = -sign(O20) x r_id(D). Same entry/exit, spread skip and quote rules as B32.
- **Test and rule:** as B32 (block 20, p < 0.025, mean > 1.0 pip, CI lower > 0, < 500 dates -> NONE). SIGNAL earns B34.
- **Descriptive (not in rule):** O20 terciles; overlap of B32 and B33 positions (share of dates with the same position); net costs.

### B34: Overnight -> intraday reversal, val confirmation (signal test, val only) → E036 · `done` (2026-11-10 R078: **NONE on val**, n 616, mean +0.193 pips, CI (-2.683, 3.23), t p 0.456; SPEC 4 net -0.492; E035/B33 not confirmed, no lead, B33/B34 line closed. R077: pre-registered as E036, queued on research-batch; 1 val trial counted when it runs. Added 2026-11-10 R074; earned R076 by B33 SIGNAL on dev (E035); B33 arm only, B32 was NONE, so 1 val trial at p < 0.05)
- **Test if earned:** the arm(s) that returned SIGNAL, unchanged, on val only (2021-01-21 .. 2023-06-30, ~620 dates, B33 burn-in from
  val dates only), own pre-registration, 1 trial per arm, p < 0.05 (or < 0.025 if both arms). Val has ~620 dates: enough power for a
  ~3-pip effect.

### Refill note R079 (not an item)
- Sources opened R079 (abstract pages only, via web-fetch summary with short verbatim fragments): Hau & Rey (2006, RFS 19(1)
  273-317; RePEc + NBER WP 9398 pages) and Camanho, Hau & Rey (2022, RFS 35(11) 5228-5274; RePEc + NBER WP 24320 pages). Full texts
  not opened. Entries in research/academic_studies.md.
- Search hits not opened and not used: Neely-Weller-Ulrich (2009) technical-rule decay is already in academic_studies.md and B16
  (12-month TSMOM) was NONE; a canonical moving-average rule would mostly re-test B16. FX lead-lag papers (minute horizon) are below the
  tradable horizon after SPEC 4 costs. Not added.
- Why this line: every price-only EUR/USD timing idea in the literature passes so far has been NONE/WEAK or failed val (lesson R078).
  B35/B36 use a second data source (index CFDs, already proven downloadable on the runner in E034) and a published mechanism with a
  stated sign. Prior is weak: Hau-Rey is contemporaneous; the lag is our extension.

### B35: Relative equity performance -> next-day EUR/USD, daily (signal test, dev) → E037 · `done` (2026-11-10 R081: **NONE on dev**, n 1509, mean +1.268 pips, CI (-1.411, 3.942), t p 0.191; closed, no lead. R080: pre-registered as E037 with B36, rule unchanged, queued on research-batch; 2 dev trials counted when it runs)
- **Mechanism [PUB, contemporaneous only]:** Hau & Rey (2006, abstract opened R079): higher home equity returns relative to foreign
  returns go with a home-currency depreciation (portfolio rebalancing under incomplete FX hedging), at daily, monthly and quarterly
  frequencies. Camanho-Hau-Rey (2022): funds rebalance after excess foreign returns. **Our test is a lagged extension, not a
  replication:** if rebalancing flows are spread over the following day, yesterday's relative equity return predicts EUR/USD today in
  the same direction. Prior: weak; effect size not published (lesson R070).
- **Signal (fixed now):** for valid dev trading date D, S1(D) = log return of EU Stocks 50 CFD mid (`eusidxeur`) minus log return of
  US 500 CFD mid (`usa500idxusd`), each from 16:00 Europe/London on the previous valid trading date to 16:00 London on D (quote = mid of
  bid/ask OPEN of the first bar in [16:00, 16:05) London, E011 rule; E034 index loader). Position = -sign(S1): US outperformed ->
  long EUR/USD; EU outperformed -> short (same sign as B30). S1 = 0 skipped. **No holiday fallback** (daily signal): a missing index
  quote at either end skips the date (counted `missing_index_quote`).
- **Trade:** EUR/USD from 16:05 London on D (after the WMR fix window) to 16:00 London on the next valid trading date (weekends held;
  Friday dates included). Quotes = open of first bar in [T, T+5 min). Entry skipped (counted) if the entry spread > 2.0 pips; missing
  bars excluded and counted.
- **Data gate (first, on the runner, 0 trials if it fails):** either index series empty, or `missing_index_quote` on > 10% of dev
  dates -> BLOCKED. Index download on GitHub Actions only (`scripts/download_dukascopy_index.sh`, as E034).
- **Test:** **dev only**, every valid date (n ~ 1,400). Decision rule (draft): SIGNAL if mean signed return > 1.0 pip AND moving-block
  bootstrap (block 20 dates, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.025 (Bonferroni for the 2 trials
  B35+B36). WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE. < 500 dates -> NONE (insufficient sample). SIGNAL earns B37.
- **Power note:** 16:05 -> 16:00 next-date EUR/USD SD likely ~50 pips (report it) -> SE ~1.4 pips at n 1,400; the p < 0.025 bar
  binds near +2.7 pips.
- **Contamination note:** E034 reported corr(S, move) only on 71 month-ends with a month-to-date signal; the daily lagged statistic has
  never been computed. E019 (TSMOM) and E021 use EUR/USD's own past moves, not equity data.
- **Descriptive (not in rule):** contemporaneous check: corr(S1(D), EUR/USD 16:00 D-1 -> 16:00 D) and its sign (Hau-Rey says
  negative in our sign convention; if it is not, say so); |S1| terciles; EU-only and US-only legs; Mondays; by year; spreads; net at
  bid/ask, SPEC 4, costs x1.5; results excluding FOMC statement days and month-ends.
- **Calendar label:** entry just after the London 4pm fix; holds through 08:30 NY releases and the next fix. Not a fix strategy.
- **Data:** EUR/USD in repo + two Dukascopy index CFDs (runner download, as E034).

### B36: Smoothed relative equity performance, 20-date signal (signal test, dev) → E037 · `done` (2026-11-10 R081: **NONE on dev**, n 1482, mean -0.88 pips, CI (-3.418, 1.868), t p 0.728; closed, no lead. Same experiment as B35; pre-registered R080, rule unchanged)
- **Mechanism:** as B35; rebalancing responds to accumulated excess returns (Camanho-Hau-Rey: fund-level rebalancing after excess
  foreign returns; horizon UNVERIFIED). A 20-date window is our choice, fixed now.
- **Signal (fixed now):** S20(D) = EU50 minus US500 log return from 16:00 London on the valid trading date 20 dates before D to 16:00
  London on D (both index quotes required at both ends; missing -> date skipped, counted; the first 20 dev dates are burn-in, counted).
  Position = -sign(S20). Same trade, gate, quote and skip rules as B35.
- **Test and rule:** as B35 (block 20, p < 0.025, mean > 1.0 pip, CI lower > 0, < 500 dates -> NONE). SIGNAL earns B37.
- **Caution (lesson R078):** E035/B33, also a 20-date smoothed sign held one day, was SIGNAL on dev and NONE on val. A B36 SIGNAL alone
  means little; only B37 counts.
- **Descriptive (not in rule):** S20 terciles; share of dates where B35 and B36 positions agree.

### B37: Relative equity performance -> EUR/USD, val confirmation (signal test, val only) · `done` (2026-11-10 R081: closed unearned, 0 trials; B35 and B36 both NONE on dev (E037). Was: earned only if B35 or B36 returns SIGNAL on dev)
- The arm(s) that returned SIGNAL, unchanged, on val only (2021-01-21 .. 2023-06-30, ~620 dates; index data downloaded for val dates
  only, S20 burn-in from val dates only), own pre-registration, 1 trial per arm, p < 0.05 (or < 0.025 if both arms). If neither arm
  is SIGNAL, B37 closes unearned with 0 trials.

### Refill note R082 (not an item)
- Sources opened R082 (web-fetch summaries with short verbatim fragments): Klitgaard & Weir (2004, FRBNY Economic Policy Review,
  May 2004, 17-28; full PDF) and Ranaldo (2007 working paper, EFMA 2008, "Segmentation and Time-of-Day Patterns in Foreign Exchange
  Markets"; first ~40% verbatim, holiday section only as an untrusted summary). Baltussen-Da-Lammers-Martens preprint
  (www3.nd.edu/~zda/intramom.pdf) could not be opened (fetch-permission timeout); only the abstract-level entry from 2026-11-07 is used.
- Not added: CFTC COT positioning -> next-week EUR/USD. Klitgaard-Weir find a strong contemporaneous weekly relation (euro adj. R^2
  .36, 74% sign agreement) but "position data do not help predict exchange rate changes over the following week" (euro Granger
  F 0.31, p 0.73). Lesson R081: without a published lagged effect, expect NONE.
- Not added: Ranaldo Thursday US-hours USD depreciation (verbatim: "On Thursdays, the dollar experiences an additional depreciation of
  2%-4%"): a subset of the home-hours windows already closed on val by E017 ("no re-test with other hours on val") and scanned on dev
  in E009 hour cells. Ranaldo's holiday natural experiment: numbers seen only in an untrusted summary (UNVERIFIED), ~40 non-overlapping
  US-holiday dates on dev. Not added.
- Why B38: B13 (Baltussen et al. intraday momentum into the futures close, the one published *lagged* intraday effect that includes
  currencies) is blocked only because the CME settlement time cannot be verified. The spot market's own daily close, the 17:00 NY roll,
  needs no external source (already the repo's trading-date boundary, `sessions.trading_date`). One variable changed vs B13: the anchor.

### B38: Intraday momentum into the 17:00 NY spot roll (signal test, dev) → E038 · `done` (2026-11-11 R084: WEAK, n 1542, +0.255 pips, CI (0.023, 0.501), binom p 0.069; below the 1-pip bar, SPEC 4 net -0.425; B39 not earned. Added 2026-11-11 R082 refill; pre-registered 2026-11-11 R083)
- **Mechanism [PUB, abstract only]:** Baltussen, Da, Lammers & Martens (2021, JFE 142(1) 377-403, DOI 10.1016/j.jfineco.2021.04.029;
  research/academic_studies.md, VERIFIED (abstract)): across 60+ futures including currencies, the rest-of-day return predicts the last
  30 minutes before the close (hedging demand: option gamma hedging, leveraged products). Gao et al. (2018) and Elaut et al. (2018,
  RUB/USD) report the same pattern with fixed trading hours. Exact currency-futures close convention and currency effect sizes:
  UNVERIFIED (preprint not opened). **Our test is an anchor variant**: EUR/USD spot has no exchange close; the 17:00 NY value-date roll
  is the market-wide daily cut (and the CME Globex daily break). Prior: weak; a 30-minute target may be too small for the 1-pip bar.
- **Test (fixed now, NY clock, DST-aware):** for each valid dev trading date D (17:00 NY roll, `sessions.trading_date`; Mon-Fri
  trading dates; Sunday-open dates follow the repo convention), predictor r1 = EUR/USD mid return from 17:00 NY at the start of D
  (first bar in [17:00, 17:05) NY) to 16:25 NY; target r2 = mid return 16:25 NY -> 16:55 NY (quotes = open of the first bar in
  [T, T+5 min), E011 rule). Exit at 16:55 NY, not 17:00, to stay clear of the roll spread widening (E029: median spread 3.6 pips at
  17:05 NY). Signed return = sign(r1) x r2; r1 = 0 skipped. Entry skipped (counted) if the 16:25 NY spread > 2.0 pips (SPEC);
  missing bars excluded and counted (SPEC coverage rule).
- **Decision rule (draft, B13 rule unchanged):** SIGNAL if mean signed return > 1.0 pip AND moving-block bootstrap (block 20 dates,
  2000 draws, seed 0) 95% CI lower > 0 AND one-sided binomial p < 0.05 on sign agreement (hit rate). WEAK if mean > 0 and (CI lower
  > 0 or p < 0.05); else NONE. < 500 dates -> NONE (insufficient sample). 1 dev trial. SIGNAL earns B39.
- **Power note:** 30-minute SD probably ~5-8 pips late in the NY session (report it) -> SE ~0.2 pips at n ~1,500; the 1.0-pip bar,
  not the CI, will bind. The bar is kept (roughly the round-trip cost; never loosened, CLAUDE.md rule 7).
- **Contamination note:** E009 scanned unconditional hourly means on dev (incl. NY 16:00 cells); this conditional sign(r1) x r2
  statistic was never computed. E027/B22 used a London-open predictor and a pre-fix target; E026/B21 a 08:30 NY predictor. Dev usable.
- **Descriptive (not in rule):** OLS slope of r2 on r1 (t); |r1| terciles; median/p90 spread at 16:25 and 16:55 NY; net at bid/ask,
  SPEC 4 and costs x1.5; by year; EDT vs EST; Fridays separately; next-date reversal reading (sign(r1) x 17:05 NY D+1 -> 16:25 NY D+1,
  Baltussen report reversal over following days); excluding FOMC statement dates and month-ends.
- **Calendar label:** end-of-day roll effect; not the London 4pm fix (11:00 NY) and not the CME settlement (B13, still blocked).
- **Data:** EUR/USD 1-minute bars in repo (no download needed beyond the usual runner data step).

### B39: Intraday momentum into the 17:00 NY roll, val confirmation (signal test, val only) · `done` (2026-11-11 R084: closed unearned, 0 trials; B38 WEAK on dev (E038). Was: earned only if B38 returns SIGNAL on dev)
- B38 unchanged on val only (2021-01-21 .. 2023-06-30, ~620 dates), own pre-registration, 1 trial, p < 0.05, same 1.0-pip bar and
  block-20 bootstrap. If B38 is not SIGNAL, B39 closes unearned with 0 trials.

### Refill note R085 (not an item)
- Sources opened R085 (web-fetch; first ~25-40% of each PDF verbatim, the rest model-summarised and treated as UNVERIFIED):
  Krohn, Vala, Uthemann & Yang, "Demand-Driven Risk Premia in Foreign Exchange and Bond Markets" (Bank of Canada SWP 2025-29, last
  updated 2025-11-03, DOI 10.34989/swp-2025-29, https://www.bankofcanada.ca/wp-content/uploads/2025/11/swp2025-29.pdf; earlier version
  Jan 2025 https://www.frbsf.org/wp-content/uploads/Krohn-Paper.pdf); Krohn, Mueller & Whelan BIS workshop slides (13 Dec 2022,
  https://www.bis.org/events/221213_bis_bdi_ecb_exchange_rates/mueller.pdf, full); Raza, Marshall & Visaltanachoti (2014, JIMF 45,
  38-60, DOI 10.1016/j.jimonfin.2014.02.009, IDEAS abstract); Valentin (2022, "The Post-ECB Announcement Drift", AUT PDF, partial);
  Fanta (2025, IES WP 2025/23, IDEAS abstract); Kloks-Mattille-Ranaldo "Hunting for Dollars" (slides + 2025 draft, Banxico PDFs);
  Liu-Slepaczuk-Tang EXFormer (arXiv 2512.12727, partial).
- Not added: Raza et al. weekly currency momentum (cross-sectional 63-currency portfolios, no EUR result; a single-pair version is a
  shorter-lookback re-test of B16/E019, whose conclusion requires fresh data and a human decision). Valentin: equity (Euro Stoxx) drift,
  no FX series. Fanta: ECB communication gives "no lasting directional moves" in EUR/USD. Kloks et al.: FX swaps/basis, not spot.
  EXFormer: a fitted ML model with the window chosen on its own test set; not a pre-registrable mechanism. KMW slides give EUR window
  means verbatim (bp, 1999-2019: pre-Tokyo -1.80, post-Tokyo +2.34, pre-ECB -3.52, ECB-London +0.63, post-London +2.73), but every
  window is already seen on dev and val (refill notes R065, R074; E024/E025, E032): only OOS is clean, a human decision. Ranaldo holiday
  section still not read verbatim (UNVERIFIED).
- Why B40/B41: KVUY report a published *lagged* USD response (lesson R081) with a large-SD target (lesson R084): "U.S. dollar
  depreciation peaks at nearly 20 basis points around 10 days after an auction" (verbatim), ~70 coupon auctions a year (1,395 in
  2004-2024, verbatim), so dev has a few hundred events. Data check R085: dukascopy-node 1.51.1 lists `ustbondtrusd` (US T-Bond CFD)
  but minute candles start 2018-12-18 (package metadata), so the paper's Treasury-futures shock cannot be measured on most of dev; the
  primary signal is the EUR/USD move in the paper's own auction window (the FX side of the same shock; the paper reports a significant
  same-window FX response, EUR figure summary-only). That proxy is the one variable that differs from the paper.

### B40: Treasury-auction demand shock -> EUR/USD continuation, 10-date hold (signal test, dev) → E039 · `done` (2026-11-11 R087: NONE, n 431, +1.426 pips, CI (-11.651, 11.979), t p 0.4334. Pre-registered 2026-11-11 R086; added 2026-11-11 R085 refill; one experiment with B41, 2 trials)
- **Mechanism [PUB, partial text]:** Krohn, Vala, Uthemann & Yang (2025, BoC SWP 2025-29): a positive Treasury demand shock at a US
  coupon auction (Treasury futures up in a window "from 10 minutes before the time of the auction (i.e., say at 13:00) until 10 minutes
  after", verbatim, Eastern Time) is followed by USD depreciation against G9 currencies that "peaks at nearly 20 basis points around 10
  days after an auction", "gradually reverting to insignificance after 14 days" (verbatim, local projections). Same-window FX response
  ~2 bp (verbatim, pooled); EUR-specific coefficient (2.12 bp) seen only in a summary: UNVERIFIED. The paper reports no trading rule,
  costs or OOS test. Prior: weak to moderate (proxy signal is noisy; 10-date holds overlap).
- **Phase 1 (data, on the runner):** US Treasury auction calendar from the Fiscal Data API `v1/accounting/od/auctions_query`
  (https://api.fiscaldata.treasury.gov; field names incl. `auction_date`, `security_type`, `security_term`, `closing_time_comp` are
  UNVERIFIED until the runner reads them). Keep nominal Note and Bond auctions (incl. reopenings; exclude Bills, TIPS, FRNs), 2015-2023.
  Gate (fixed now): 50-110 qualifying auctions per full year and a parsed competitive close time for >= 95%; otherwise fix the parser
  once or block. If the API refuses the runner (403/timeouts on 2 attempts), the item is `blocked` with 0 trials; no other source is
  substituted without a human decision. Also download `ustbondtrusd` minute bid/ask (descriptive only; its failure does not block).
- **Signal (fixed now, NY clock, DST-aware):** T = competitive close time on auction date D (America/New_York). s = sign(EUR/USD mid at
  T+10 min - mid at T-10 min) (quotes = open of the first bar in [t, t+5 min), E011 rule). EUR up = USD down = positive demand shock;
  position s (continuation). Two auctions with the same T on the same date form one event; distinct times on one date are separate
  events. s = 0 skipped (counted).
- **Hold (B40):** enter at T+10 min (spread at entry > 2.0 pips -> skipped, counted), exit at 16:00 NY on the 10th trading date after D
  (`sessions.trading_date`, 16:00 NY quote as in E019). Signed return per event in pips. Events whose exit date leaves dev are dropped.
- **Decision rule (draft, per arm):** SIGNAL if mean signed > 1.0 pip AND moving-block bootstrap 95% CI lower > 0 (blocks of 20
  consecutive events in time order, 2000 draws, seed 0) AND one-sided t p < 0.025 (2 arms in one experiment). WEAK if mean > 0 and
  (CI lower > 0 or p < 0.025); else NONE. < 150 events -> NONE (insufficient sample). A SIGNAL in either arm earns B42.
- **Power note:** 10-date SD ~140 pips; events overlap (~3-4 open at a time), effective n maybe ~150 -> SE ~10 pips; the published
  peak (~20 bp ~ 22 pips per 1-SD shock) is detectable only if the EUR/USD proxy captures the shock sign well. A NONE does not rule out
  the paper's effect measured with Treasury futures.
- **Descriptive (not in rule):** by tenor (2/3/5/7 vs 10/20/30-year); hit rate; OLS slope on the window return; 2019-2020 sub-sample
  with the `ustbondtrusd` window sign as the signal and the sign agreement between the two signals; non-auction control (same T on
  the same weekday one week earlier, if not itself an auction date); SPEC 4 net and costs x1.5 per event; by year.
- **Contamination note:** no auction-date conditioning has been computed on dev. E009 hour cells (13:00 NY) are unconditional; E026 used
  08:30 NY windows; E019 used 16:00 -> 16:00 trend. Dev usable.
- **Calendar label:** Treasury auction (scheduled supply event); not a fix, not a data release.
- **Data:** auction calendar (phase 1, runner); EUR/USD 1-minute bars in repo; `ustbondtrusd` descriptive only.

### B41: Treasury-auction demand shock -> EUR/USD continuation, next-date hold (signal test, dev) → E039 · `done` (2026-11-11 R087: NONE, n 437, +1.655 pips, CI (-3.106, 7.394), t p 0.2733. Pre-registered 2026-11-11 R086; added 2026-11-11 R085 refill; same experiment as B40)
- Same events, signal, entry and rule as B40 (second trial, p < 0.025); exit at 16:00 NY on the first trading date after D. Tests whether
  the response starts early (KVUY local projections build over days; per-day path seen only in a figure, not read: UNVERIFIED).
  Lower SD (~45 pips, little overlap), so a small but real early drift is easier to see; the 1-pip bar applies.

### B42: Treasury-auction demand shock -> EUR/USD, val confirmation (signal test, val only) · `done` (2026-11-11 R087: closed unearned, 0 trials; B40 and B41 NONE on dev (E039). Was: earned only if B40 or B41 returns SIGNAL on dev)
- The SIGNAL arm(s), unchanged, on val only (2021-01-21 .. 2023-06-30, auction calendar for val dates), own pre-registration, 1 trial
  per arm, p < 0.05 (or < 0.025 if both arms). If neither arm is SIGNAL, B42 closes unearned with 0 trials.

### Refill note R088 (not an item)
- Sources opened R088 (web-fetch; entries in research/academic_studies.md): Lee & Wang (2025, RAPS, IDEAS abstract); Ferraro, Rogoff &
  Rossi (NBER WP 17998, ~45% verbatim); Chen & Hsu (2019, J. Forecasting, abstract); Stavrakeva & Tang (CEPR DP18119, ~35% verbatim);
  Bae, Da & Zurita (2024, Mgmt Sci, ~35% verbatim); Chernov-Dahlquist-Lochstoer (NBER WP 28260) and Filippou-Taylor-Wang (CEPR DP16049),
  partial. Data check R088: dukascopy-node 1.51.1 metadata lists `lightcmdusd` (WTI CFD) minute candles from 2011-09-23 and
  `brentcmdusd` from 2010-12-02, so an oil signal covers all of dev (lesson R087: source-market signal over the full dev span).
- Not added: Chen-Hsu next-day stock-return differentials (= B35/E037, NONE); Stavrakeva-Tang lagged macro news (needs surprise data);
  Bae-Da-Zurita (predicts equities); Chernov et al., Filippou et al. (monthly cross-sectional).
- Why B43/B45: both have a *published lagged* effect (lesson R081): Lee-Wang a 12-24 h post-FOMC reversal in currencies; FRR a lagged
  daily oil -> FX relation (commodity currencies; EUR is our extension, weak prior). B43 is ranked first (USD-specific event, unseen
  target window); it is underpowered (48 dev events), stated in its power note.

### B43: Post-FOMC reversal of the pre-statement EUR/USD drift, 12-24 h after the statement (signal test, dev) → E040 · `done` (2026-11-11 R090: NONE, n 47, +2.623 pips, CI (-14.684, 21.44), t p 0.3863. Pre-registered 2026-11-11 R089; added 2026-11-11 R088 refill; 1 dev trial counted when it runs)
- **Mechanism [PUB, abstract only]:** Lee & Wang (2025, RAPS 15(3-4) 247-287): post-FOMC currency returns are "mostly realized
  between 12 and 24 hours after FOMC announcements", "cancelling out approximately 65% of positive pre-FOMC announcement drifts"
  (verbatim). Currency set, sign convention and EUR magnitude UNVERIFIED, so the item is symmetric in the drift sign.
- **Events (fixed now):** scheduled, not cancelled FOMC statement dates t in data/calendars/fomc_dates.csv inside dev (2015-2020; 48
  expected). Statement time 14:00 NY (America/New_York, DST-aware). Unscheduled meetings excluded.
- **Signal:** P = EUR/USD mid at 13:55 NY on t minus mid at 16:00 NY on the previous trading date (the E013 window; quotes = open of
  the first bar in [x, x+5 min), E011 rule). Position s = -sign(P) (reversal). P = 0 skipped (counted).
- **Hold:** enter 02:00 NY on the next calendar day (t+12 h), exit 14:00 NY that day (t+24 h). Entry spread > 2.0 pips -> skipped
  (counted); missing quote -> skipped (counted). Signed return in pips. If t+1 is not a trading day (no bars), skipped (counted).
- **Decision rule (draft):** < 40 events -> NONE (insufficient sample). SIGNAL if mean signed > 1.0 pip AND i.i.d. bootstrap 95% CI
  lower > 0 (2000 draws, seed 0; events do not overlap) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI lower > 0 or
  p < 0.05); else NONE. A SIGNAL earns B44.
- **Power note:** 12-h EUR/USD SD roughly 30-40 pips -> SE ~5 pips with 48 events; only a reversal of ~10+ pips (E013 dev pre-drift
  mean +21.28 pips; 65% of it ~14) can show. A NONE does not rule out the published effect.
- **Descriptive (not in rule):** unconditional short EUR/USD over the same window; P > 0 subset only; the 14:00 -> 02:00 NY window
  (0-12 h); OLS slope of the target on P; by year; SPEC 4 net and costs x1.5.
- **Contamination note:** E013/E014 measured only the pre-statement window (16:00 t-1 -> 13:55 t); the 02:00 -> 14:00 NY t+1 window on
  FOMC dates has not been computed on dev or val. E009 hour cells are unconditional. Dev usable.
- **Calendar label:** FOMC statement (scheduled policy event); this effect *is* the strategy if it passes.
- **Data:** FOMC calendar (in repo, validated 2015-2023); EUR/USD 1-minute bars in repo. No runner download needed beyond the usual.

### B44: Post-FOMC reversal, val confirmation (signal test, val only) · `done` (2026-11-11 R090: closed unearned, 0 trials; B43 NONE on dev (E040). Was: added 2026-11-11 R088; earned only if B43 returns SIGNAL on dev)
- B43 unchanged on val (2021-01-21 .. 2023-06-30; ~20 statements), own pre-registration, 1 val trial, < 15 events -> NONE, p < 0.05.
  Lesson 2026-11-08 (E014): val has low power for 8/yr events; a val NONE would close the line and leave only OOS (human decision).
  If B43 is not SIGNAL, B44 closes unearned with 0 trials.

### B45: Lagged daily oil return -> next-day EUR/USD (signal test, dev) → E041 · `done` (2026-11-11 R092: NONE, n 1519, +2.306 pips, CI (-0.513, 5.184), t p 0.0555. 2026-11-11 R091: pre-registered as E041, rule unchanged, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-11 R088 refill)
- **Mechanism [PUB, partial text; EUR is our extension]:** Ferraro, Rogoff & Rossi (2012 NBER WP 17998 / JIMF 2015): daily oil price
  changes forecast commodity-currency exchange rates; "the predictive ability of the lagged realized oil prices is more ephemeral"
  (verbatim) than the contemporaneous one. Sign used here: oil up -> USD weaker -> EUR/USD up next day (stated before data; the
  contemporaneous corr is reported descriptively). Prior weak (lesson R081: lags are often absorbed the same day).
- **Phase 1 (data, on the runner):** dukascopy-node `lightcmdusd` 1-minute bid/ask for dev (2015-2020). Gate (fixed now): a valid WTI
  quote at both 16:00 London points for >= 90% of dev EUR/USD trading dates; otherwise fix the download once or block (0 trials).
- **Signal (fixed now, London clock, DST-aware):** O = log(WTI mid at 16:00 London D) - log(WTI mid at 16:00 London on the previous
  trading date), quotes = open of the first bar in [x, x+5 min). Position s = sign(O); O = 0 or missing -> skipped (counted). |O| >
  0.10 (e.g. a contract-roll gap or the April 2020 negative-price episode) -> skipped (counted; Dukascopy CFD roll handling UNVERIFIED).
- **Hold:** EUR/USD 16:05 London D -> 16:00 London on the next trading date (E037 convention); entry spread > 2.0 pips -> skipped.
- **Decision rule (draft):** < 500 dates -> NONE. SIGNAL if mean signed > 1.0 pip AND moving-block bootstrap 95% CI lower > 0 (blocks
  of 20 consecutive dates, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI lower > 0 or p < 0.05);
  else NONE. A SIGNAL earns a val confirmation item (to be added then, 1 val trial).
- **Power note:** daily SD ~50 pips, n ~1500 -> SE ~1.3 pips; a ~3-pip edge is detectable.
- **Descriptive (not in rule):** contemporaneous corr(O, EUR/USD same 16:00 -> 16:00 London day); by year; |O| terciles; Brent not used.
- **Contamination note:** no oil series has been used in this repo; E037 used equity indices with the same hold window (different
  signal). Dev usable.
- **Data:** WTI CFD (phase 1, runner); EUR/USD 1-minute bars in repo.

### Refill note R093 (not an item)
- Sources opened R093 (web-fetch; entries in research/academic_studies.md): Apergis (2014, IREF 29, 75-82, DOI
  10.1016/j.iref.2013.04.004; EconPapers abstract verbatim + Curtin author manuscript full text); Basnarkov, Stojkoski, Utkovski &
  Kocarev (arXiv 1906.10388, Physica A, full text); Ranaldo (2007 SNB WP / EFMA 2008) section 5.2 holidays, now read verbatim; Krohn,
  Mueller & Whelan (BoC SWP 2021-48, ~35% verbatim). Data check R093: dukascopy-node 1.51.1 metadata lists `xauusd` (XAU/USD) minute
  candles from 2003-05-05, so a gold signal covers all of dev (lesson R087).
- Not added: Basnarkov et al. (lagged effects "absent" for most currency pairs; significant leads are 1-minute, bid-only, no costs;
  EUR/USD only as a lagger of USD/CZK). Ranaldo German-holiday reversal of the EU-hours USD appreciation (Table 7: EUR/USD 36
  holiday days in 1999-2005, no significance marks; ~35 dev events and a 4-hour target, below the power floor of lesson R090; the
  home-hours line is closed on val, B14/E017). KMW 2021: fixes, vol state and price pressure already tested (E007, E010, E011, E022-E025,
  E030-E032); nothing new.
- Why B46: Apergis reports a published *lagged* daily gold -> exchange-rate relation (lesson R081) with a source-market signal over the
  full dev span (lesson R087). EUR/USD is our extension (AUD/USD only in the paper): weak prior. Gold and WTI are both USD-priced, so
  the signal is partly correlated with E041's (stated in the contamination note); the hold window is E041's, so the one variable
  changed vs E041 is the source market (and with it the paper's sign).

### B46: Lagged daily gold return -> next-day EUR/USD (signal test, dev) → E042 · `done` (2026-11-11 R095: NONE, n 1533, -1.407 pips, CI (-4.415, 0.939), t p 0.8352. 2026-11-11 R094: pre-registered as E042, rule unchanged, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-11 R093 refill)
- **Mechanism [PUB, AUD/USD only; EUR is our extension]:** Apergis (2014, IREF 29, 75-82): "the out-of-sample predictive ability is
  strong and robust across short- and long-run horizons" (verbatim abstract) for gold -> AUD/USD, daily 2000-2012, ECM with 8 lags.
  Author-manuscript Table 3: lagged gold returns enter the exchange-rate equation with **negative** short-run coefficients (lag 1
  -0.328, t -4.34; lags 2-5 also negative). The paper's long-run sign reading is internally inconsistent (UNVERIFIED which way AUD is
  quoted). Sign used here, fixed now from the printed short-run coefficients: gold up on D -> EUR/USD down over D -> D+1 (partial
  reversal of the same-day USD co-move). Prior weak (lesson R081; Basnarkov et al. find most daily-and-shorter FX lags absent).
- **Phase 1 (data, on the runner):** dukascopy-node `xauusd` 1-minute bid/ask for dev (2015-2020), raw files git-ignored. Gate (fixed
  now): a valid gold quote at both 16:00 London points for >= 90% of dev EUR/USD trading dates; otherwise fix the download once or
  block (0 trials).
- **Signal (fixed now, London clock, DST-aware; E041 conventions):** G = log(XAU/USD mid at 16:00 London D) - log(mid at 16:00 London
  on the previous trading date), quotes = open of the first bar in [x, x+5 min). Position s = -sign(G); G = 0 or missing -> skipped
  (counted). |G| > 0.10 -> skipped (counted; data-error guard, same as E041).
- **Hold:** EUR/USD 16:05 London D -> 16:00 London on the next trading date (E037/E041 convention); entry spread > 2.0 pips -> skipped.
- **Decision rule (draft, = E041 rule):** < 500 dates -> NONE. SIGNAL if mean signed > 1.0 pip AND moving-block bootstrap 95% CI
  lower > 0 (blocks of 20 consecutive dates, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI lower >
  0 or p < 0.05); else NONE. A SIGNAL earns B47.
- **Power note:** daily SD ~50 pips, n ~1500 -> SE ~1.3 pips; a ~3-pip edge is detectable. ~261 registered trials: a single p just
  under 0.05 is expected noise (lesson R092), hence the val confirmation.
- **Descriptive (not in rule):** contemporaneous corr(G, EUR/USD same 16:00 -> 16:00 London day); corr(G, WTI O of E041) on common
  dates; the opposite-sign (continuation) mean, reported only; by year (lesson R092: check one-year concentration); |G| terciles;
  SPEC 4 net and costs x1.5.
- **Contamination note:** no gold series has been used in this repo. The target window equals E041's (and E037's), whose
  unconditional and oil-signed means on dev are known; G is correlated with E041's O (both USD-priced commodities). The sign is fixed
  from the paper, not from E041 (E041's positive oil-continuation mean would favour the opposite sign). Record in the methodology.
- **Calendar label:** daily cross-market signal, not a fix or release effect (the 16:00 London point is the WM/R fix: report the
  16:00 -> 16:05 London gap excluded by the entry rule, as in E041).
- **Data:** XAU/USD (phase 1, runner); EUR/USD 1-minute bars in repo.

### B47: Lagged daily gold return -> EUR/USD, val confirmation (signal test, val only) · `done` (2026-11-11 R095: closed unearned, 0 trials; B46 NONE on dev (E042). Was: added 2026-11-11 R093; earned only if B46 returns SIGNAL on dev)
- B46 unchanged on val (2021-01-01 .. 2023-06-30; ~640 dates), own pre-registration, 1 val trial, < 200 dates -> NONE, p < 0.05,
  block-20 bootstrap, gold gate on val dates. If B46 is not SIGNAL, B47 closes unearned with 0 trials.

### Refill note R096 (not an item)
- Sources opened R096 (web-fetch; entries in research/academic_studies.md): Xiao, Yin & Zhao (2020, JFR 43(3), DOI 10.1111/jfir.12223,
  abstract + introduction); Frömmel, Han & Van Gysegem (2015, EMFT 51(4), DOI 10.1080/1540496X.2015.1046348, abstract); Erdemlioglu,
  Laurent & Neely (FRB St. Louis WP 2012-008, method only); Kumar (2015, IJMF, TOM in INR pairs), Ştefănescu & Dumitriu (MPRA 99365),
  Vasileiou (2024), Aydoğan & Booth (2003), Caporin & Shahzad (not used).
- Not added: turn-of-month / turn-of-year EUR/USD (published only for INR, RON, ZAR, TRY crosses; one event per month or year, far below
  the power floor of lesson R090; month-end windows already tested in E034). More lagged daily cross-market signals (lesson R095).
- Why B48: a new family (event-time, calendar-free, all hours) with a published post-jump reversal over ~60 min (equity ETFs; HUF/EUR
  abstract) and a large dev sample (EUR/USD 5-min jumps ~0.2% of bars per Erdemlioglu et al., UNVERIFIED count). Price data in repo only;
  no external download. Relatives: B21/E026 (continuation after large 08:30-08:45 NY moves, NONE, mean -0.42 i.e. faint reversal) and
  B23/E028 (daily overreaction continuation, NONE): neither tested a jump test or a 60-min fade at all hours.

### B48: Post-jump reversal, 5-minute Lee-Mykland jumps, 60-minute fade (signal test, dev) → E043 · `done` (2026-11-11 R098: NONE, n 1896, -0.693 pips, CI (-1.607, 0.251), t p 0.9238. Pre-registered 2026-11-11 R097)
- **Mechanism [PUB, not EUR/USD]:** Xiao, Yin & Zhao (2020): "No-news jumps are followed by significant return reversals for at least
  60 minutes"; scheduled-news jumps also reverse, unscheduled-news jumps continue (verbatim; US equity ETFs). Frömmel et al. (2015):
  "postjump reversal patterns" in HUF/EUR (abstract). Liquidity-provision reading: a jump overshoots on one-sided order flow and dealers
  are paid to absorb it. EUR/USD is our extension; prior weak to medium (EUR/USD is the deepest pair; B21 found no 08:30 continuation).
- **Grid and returns (fixed now):** 5-minute grid on the NY clock; quote at T = open of the first 1-minute bar in [T, T+5 min), mid.
  r_t = ln(mid(t+5)) - ln(mid(t)). Missing quote at either end -> r_t missing.
- **Jump test (fixed now, Lee-Mykland 2008 form, no periodicity filter):** L_t = r_t / sigma_t, sigma_t^2 = (1/(K-2)) x sum over the
  previous K-1 returns of |r_j| |r_{j-1}| (bipower, past only, r_t excluded), K = 270. Require >= 90% of those K-1 returns valid, else
  no test. Jump if |L_t| > C_n + S_n x beta*, n = 288, alpha = 0.01: C_n = sqrt(2 ln n)/c - (ln pi + ln ln n)/(2 c sqrt(2 ln n)),
  S_n = 1/(c sqrt(2 ln n)), c = sqrt(2/pi), beta* = -ln(-ln(1 - alpha)) -> threshold 5.395. Also require |r_t| >= 5 pips (in price
  terms, |mid(t+5) - mid(t)| >= 0.0005) so that quiet-hour noise is not called a jump.
- **Exclusions (fixed now, counted):** jump bar starting in 16:55-17:55 NY (roll hour, spreads) or within the first 60 minutes after
  the Sunday open; entry spread > 2.0 pips (SPEC 4); missing entry or exit quote. Non-overlap: after an event, the next jump may start
  only at or after that event's exit time (jumps inside a hold are counted, not traded).
- **Trade:** position s = -sign(r_t). Entry at the quote at t+10 min (one 5-min bar after the jump ends, no same-quote fill), exit at
  t+70 min (60-minute hold). Signed return = s x (mid exit - mid entry), pips.
- **Decision rule (draft):** < 300 events -> NONE. SIGNAL if mean signed > 1.0 pip AND date-cluster bootstrap 95% CI lower > 0
  (resample trading dates with all their events, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI
  lower > 0 or p < 0.05); else NONE. A SIGNAL earns B49.
- **Power note:** expected ~500-1500 events on dev; 60-min SD after a jump perhaps 10-15 pips -> SE ~0.4-0.7 pip; a 1-2 pip edge is
  detectable. ~261 registered trials: one p just under 0.05 is expected noise (lesson R092), hence the val confirmation.
- **Descriptive (not in rule):** continuation mean (opposite sign, reported only); positive vs negative jumps (Xiao asymmetry); jumps
  starting 08:25-08:50 NY (US-release proxy, overlaps B21) vs the rest; London 02:00-04:00 NY open vs rest; by year (lesson R092);
  |L| terciles; mean of the skipped t+5 -> t+10 bar; SPEC 4 net and costs x1.5; event count per year.
- **Contamination note:** B21/E026 dev result is known (08:30-08:45 moves, 2-h continuation, mean -0.42, i.e. a faint reversal). Jumps
  at 08:30 NY are a subset of B48 events; the sign (reversal) is fixed from Xiao et al., not from E026. No 5-min jump test has been
  run in this repo before. Dev usable.
- **Calendar label:** event-time, calendar-free. If the effect is concentrated at 08:30 NY it is a release effect; report the share.
- **Data:** EUR/USD 1-minute bid/ask bars in repo; no download.

### B49: Post-jump reversal, val confirmation (signal test, val only) · `done` (2026-11-11 R098: closed unearned, 0 trials; B48 NONE on dev (E043). Was: earned only if B48 returns SIGNAL on dev)
- B48 unchanged on val (2021-01-21 .. 2023-06-30), own pre-registration, 1 val trial, < 120 events -> NONE, p < 0.05, same bootstrap.
  If B48 is not SIGNAL, B49 closes unearned with 0 trials.

### Refill note R099 (not an item)
- Sources opened R099 (web-fetch; entries in research/academic_studies.md): Jiang, Han & Yin (2019, NAJEF 48, 628-641, DOI
  10.1016/j.najef.2018.07.018, EconPapers abstract); Gkillas, Gupta & Pierdzioch (2019, Physica A 532, DOI 10.1016/j.physa.2019.121867,
  abstract); Hoque, Le & Hassan (2020, IMFI 17(3), DOI 10.21511/imfi.17(3).2020.17, PDF).
- Not added: realized moments -> next-day realized volatility (Gkillas et al.; volatility target, E008 closed vol timing); options smirk
  -> next-day return (Hoque et al.; no options data in the repo).
- Why B50: a new signal family (shape of the intraday return distribution, not its level, volume or a cross-market return) with a
  published *forward* relation to currency returns and a stated sign (lesson R081); price data in repo only, no download. Prior weak:
  the paper is cross-sectional and its skewness measure and horizon are UNVERIFIED; the single-pair daily version is our extension.

### B50: Daily realized skewness -> next-day EUR/USD (signal test, dev) → E044 · `done` (2026-11-11 R101: NONE, n 1238, -0.183 pips, CI (-3.845, 4.329), t p 0.5436. R100: pre-registered as E044, rule unchanged, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-11 R099 refill)
- **Mechanism [PUB, cross-section only; EUR/USD time series is our extension]:** Jiang, Han & Yin (2019): "a positive and significant
  relationship between skewness and future currency excess returns" (verbatim abstract). Reading: positive skew = right-tail (EUR-buying)
  bursts not yet fully priced; negative skew = crash-risk premium paid later. Measure, horizon and currency list UNVERIFIED; sign
  fixed now from the abstract: **positive skew on D -> long EUR/USD on D+1**.
- **Signal (fixed now):** trading date D (17:00 NY boundary, `sessions.trading_date`). 5-minute mid returns r_i = ln mid(t+5) - ln
  mid(t) on the NY-clock grid from 18:00 NY (start of D, after the roll hour; E043 roll window [16:55, 17:55) excluded) to 16:55 NY on D;
  quote = open of the first 1-minute bar in [T, T+5 min) (E043 rule). Missing quote at either end -> r_i missing. Valid D: >= 90% of
  the 275 returns present. RS(D) = sqrt(N) x sum r_i^3 / (sum r_i^2)^(3/2), N = valid returns (Amaya et al. form as used by Gkillas et
  al.; not otherwise tuned). Position s = sign(RS(D)); RS = 0 -> skipped (counted).
- **Trade (fixed now, E033 convention):** entry at 20:00 NY (start of trading date D+1, after the roll spread normalises, lesson R059),
  exit at 16:55 NY on D+1. D a Friday -> excluded (counted; weekend). Missing entry/exit quote -> excluded (counted); entry spread >
  2.0 pips -> skipped (counted). Signed return = s x (mid exit - mid entry), pips.
- **Decision rule (draft, = E041 rule):** < 500 dates -> NONE. SIGNAL if mean signed > 1.0 pip AND moving-block bootstrap 95% CI
  lower > 0 (blocks of 20 consecutive dates, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI lower >
  0 or p < 0.05); else NONE. A SIGNAL earns B51.
- **Power note:** ~21 h hold, SD ~40-45 pips, n ~1,200 non-Friday dev dates -> SE ~1.25 pips; a ~2.5-3 pip edge is detectable.
  ~262 registered trials: one p just under 0.05 is expected noise (lesson R092), hence the val confirmation.
- **Descriptive (not in rule):** share of s = +1; corr(RS(D), R(D)) with R(D) = mid 16:55 NY D - mid 18:00 NY D (skew vs plain
  daily-return sign; E021/E033 reversal tests used R(D)) and the result within R(D) > 0 and R(D) < 0 halves; |RS| terciles; opposite
  sign mean (reported only); by year (lesson R092); RS computed with 1-minute returns (robustness only); unconditional long mean over the
  same hold; SPEC 4 net and costs x1.5.
- **Contamination note:** no skewness or higher-moment statistic has been computed in this repo (grep R099). The hold window (20:00 NY
  -> 16:55 NY D+1) is the E033 window, whose daily-return-conditioned means on dev are known (B28 NONE -2.034, B29 NONE -0.213), and
  RS is correlated with R(D); report the overlap. Sign fixed from the paper, not from E033. Dev usable.
- **Calendar label:** daily distribution-shape signal; the hold contains Tokyo/ECB/London fixes and US releases (not a calendar effect).
- **Data:** EUR/USD 1-minute bid/ask bars in repo; no download.

### B51: Daily realized skewness -> EUR/USD, val confirmation (signal test, val only) · `done` (2026-11-11 R101: closed unearned, 0 trials; B50 NONE on dev (E044). Added 2026-11-11 R099; was: earned only if B50 returns SIGNAL on dev)
- B50 unchanged on val (2021-01-21 .. 2023-06-30), own pre-registration, 1 val trial, < 200 dates -> NONE, p < 0.05, block-20
  bootstrap. If B50 is not SIGNAL, B51 closes unearned with 0 trials.

### Refill note R102 (not an item)
- Sources attempted R102: Li, Sakkas & Urquhart (2022, JFM 57, 100619, DOI 10.1016/j.finmar.2021.100619, accepted manuscript at
  https://reading-9.eprints-hosting.org/95566/1/Accepted-Version.pdf, ~25% verbatim): intraday TSMOM in 16 MSCI equity indices; FX is
  used only to convert to USD, no currency result. Xu, Kozhan & Taylor ("Prospect Theory and Currency Returns", AEA 2020 preliminary,
  https://aeaweb.org/conference/2020/preliminary/paper/RTR7eK6k): cross-sectional, monthly. Phylaktis & Yamani (Bayes WP-EMG-03-2022):
  monthly lagged equity/bond returns -> FX (B35/E037 family, NONE). Raza (2015 Massey PhD thesis): 52-week-high currency momentum is
  cross-sectional and loses money. None added. The newyorkfed.org (Osler SR 125, Osler 2000 EPR) and ideas.repec.org fetches failed this
  run on a fetch-permission timeout (not a server refusal; not retried, lesson R024).
- Why B52: the one published *reversal* mechanism already VERIFIED in this repo that has never been tested: Osler (2003, JF 58(5),
  1791-1819, DOI 10.1111/1540-6261.00588, abstract VERIFIED 2026-11-07) - take-profit orders cluster at round numbers, "which helps
  explain reversals at support and resistance" (repo entry wording). B15/E018 tested only the stop-loss arm (continuation after a close
  crosses a level, NONE) and wrote that the take-profit reversal "needs its own pre-registration". B52 uses the events E018 never
  contained: bars that touch a round level and close back on the near side (rejected touches). Prior weak: E018 dev showed round-level
  crossings reverse *less* than control-level crossings (-0.128 vs -0.803), the 1990s order data may not describe modern e-trading
  (lesson R033), and E043 found no hour-scale post-move drift. Price data in repo only; no download.

### B52: Take-profit reversal at round numbers, rejected touches (signal test, dev) → E045 · `done` (2026-11-11 R104: NONE, n 1000, -0.71 pips, CI (-1.878, 0.401), t p 0.8828. R103: pre-registered as E045, rule unchanged, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-11 R102 refill)
- **Mechanism [PUB]:** Osler (2003, JF, DOI 10.1111/1540-6261.00588, VERIFIED abstract): take-profit orders cluster at round numbers
  (00/50 definition taken from Osler 2002, VERIFIED abstract; Osler 2003's own digit definition UNVERIFIED), so rising rates meet a wall of sell orders at the level and falling rates a wall of buys; trends tend to reverse
  there. Hour-scale persistence and the exact touch/bounce definition in the paper are UNVERIFIED (full text could not be opened R102).
  Parent E018 (stop-loss arm, NONE on dev). **Variable changed (one):** the event - a rejected touch of the level instead of a close
  crossing it, with the sign the take-profit arm implies (fade).
- **Levels (fixed now, = E018):** L = every multiple of 0.0050 (00 and 50). Prices in exact 1e-5 units of 2 x mid (E018 `_to_units`).
  Mid high h(t) = bid_high + ask_high, mid low l(t) = bid_low + ask_low, mid close c(t) = bid_close + ask_close (all in 2 x mid units).
- **Event (fixed now):** 1-minute bar t, bars t-1 and t in the same trading date (`sessions.trading_date`).
  Up-touch of L: c(t-1) < L, h(t) >= L, c(t) < L (reaches the level from below, closes back below). Down-touch: c(t-1) > L,
  l(t) <= L, c(t) > L. If one bar touches several levels, the level nearest c(t) counts. Only the **first** event (either side) of each
  level per trading date counts, and a level that was already *crossed by close* (E018 event) earlier the same trading date is no
  longer eligible that date. Position s = -1 after an up-touch, +1 after a down-touch.
- **Trade and exclusions (fixed now, = E018 conventions):** entry = open of the first bar at or after t + 1 min (<= t + 5 min); exit =
  open of the first bar at or after entry + 60 min (<= + 5 min); window needs >= 55/60 bars. Skipped and counted under the first failing
  check: coverage; entry or exit NY time in [16:30, 18:30) (roll); entry spread > 2.0 pips (SPEC 4); entry before the previous trade's
  exit (overlap). Signed return = s x (mid open at exit - mid open at entry), pips.
- **Decision rule (draft):** < 300 events -> NONE. SIGNAL if mean signed > 1.0 pip AND date-cluster bootstrap 95% CI lower > 0 (resample
  trading dates with all their events, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI lower > 0 or
  p < 0.05); else NONE. A SIGNAL earns B53.
- **Power note:** expected ~1-2 events per trading date (~1,500-3,000 on dev); 60-min SD ~10-12 pips -> SE ~0.3 pips; the 1-pip bar
  binds, not the CI. ~263 registered trials: one p just under 0.05 is expected noise (lesson R092), hence the val confirmation.
- **Descriptive (not in rule):** control levels offset 0.0023 (ending 23/73, E018 control) through the identical procedure and the
  round-minus-control difference (the mechanism predicts round > control); 15- and 120-minute horizons; up- vs down-touches; share of
  events whose level is crossed by close within the hold; by year (lesson R092); events per year; median entry spread; SPEC 4 net and
  costs x1.5; events within +-15 min of 08:30, 10:00 and 11:00 NY (share and mean).
- **Contamination note:** E018 dev results are known for close-crossing events (mean -0.128, controls -0.803, 15/120 min -0.405/-0.777);
  rejected-touch events are disjoint from E018 events at bar t, but later crossings on the same date overlap in time. The sign is fixed
  from Osler (2003), not from E018 (E018 controls would favour fading any level, round or not; hence the control comparison is
  reported). No touch-based statistic has been computed on dev. Dev usable.
- **Calendar label:** price-level effect, not a time-of-day, fix or release effect (report the release/fix-time share).
- **Data:** EUR/USD 1-minute bid/ask bars in repo; no download. Code reuses `fxresearch.round_numbers` level arithmetic.

### B53: Take-profit reversal at round numbers, val confirmation (signal test, val only) · `done` (2026-11-11 R104: closed unearned, 0 trials; B52 NONE on dev (E045). Added 2026-11-11 R102; was: earned only if B52 returns SIGNAL on dev)
- B52 unchanged on val (2021-01-21 .. 2023-06-30), own pre-registration, 1 val trial, < 120 events -> NONE, p < 0.05, same date-cluster
  bootstrap. If B52 is not SIGNAL, B53 closes unearned with 0 trials.

### Refill note R105 (not an item; no item added)
- Sources opened R105 (web-fetch; entries in research/academic_studies.md): Osler (2002), FRBNY Staff Report 150,
  [PDF](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.pdf) (first ~40% verbatim, rest summary) and its
  [RePEc record](https://econpapers.repec.org/RePEc:fip:fednsr:150); Kloks, Mattille & Ranaldo (2024), "Hunting for Dollars",
  [PDF](https://ecb.europa.eu/press/conferences/shared/pdf/20241107_money_markets/Ranaldo_paper.pdf) (~60% verbatim).
- Not added: Osler-faithful "confirmed crossing" variant of B15/E018 (reach = within 0.01% of a 00/50 level, crossed = still beyond it
  15 minutes later, verbatim definitions). The published effect is *relative* (round vs arbitrary numbers): dollar-mark "moves an
  average 0.061 percent during the 15 minutes after crossing a round number, but only 0.054 percent after crossing an arbitrary number"
  (verbatim), i.e. ~0.7 bp (< 1 pip) of excess movement, measured from the crossing itself. An entry after the 15-minute confirmation
  misses it, and the excess is below the 1-pip bar and SPEC 4 costs, so the test cannot return SIGNAL by construction (lesson R090
  power floor; trial would only inflate the count). E018 descriptive round-minus-control (+0.675 pips) is already consistent with a
  relative effect of that size; it is not tradable.
- Not added: previous-trading-date high/low breakout (stop cascades beyond recent extremes). Osler's verbatim text places stop clusters
  "just above"/"just below" round numbers only; nothing on recent highs/lows or previous-day range (summary agrees). No published
  basis; range-breakout relative S001/E004 negative on dev.
- Not added: quarter-end dollar funding squeeze (Kloks-Mattille-Ranaldo 2024; Du-Tepper-Verdelhan 2018 via that paper). The verbatim
  text is about FX-swap volumes and the cross-currency basis; no spot-rate direction, size or timing. Month-end windows tested in E034;
  ~24 quarter-ends on dev, below the power floor.
- Search pass (standard + extended) for recent EUR/USD intraday predictability papers returned only families already tested (KMW
  fixes, intraday momentum, news) or non-FX markets.
- **Why nothing added:** after E001-E045 the price-only, calendar-free families with a published EUR/USD-relevant mechanism and
  enough dev events are exhausted (time-of-day, fixes, sessions, momentum/reversal at 1 min to 12 months, levels, jumps, moments,
  volume, cross-asset daily lags). The remaining published mechanisms need data the repo lacks: a US/euro-area release calendar with
  timestamps and consensus (B6/B12 blocked), fed funds futures / OIS expectations (Karnaukh, Neuhierl-Weber, Borisenko-Pozdeev), options
  data (Hoque et al., Kostakis et al.), dealer order flow, or the locked OOS block (KMW pre-ECB window, R065). These are human
  decisions; listed in agent_logs/agent_decision_log.md R105. Later refill runs should look for a sanctioned free source of one of
  these (e.g. a public release-date file the runner can download) before adding further price-only items.

### Refill note R106 (not an item; no item added)
- 2026-11-12 R106 refill pass, focused (per R105) on a free, runner-downloadable release-date source. Candidates tried: ECB
  Euro Area Monetary Policy Event-Study Database (Altavilla et al. 2019, JME, DOI 10.1016/j.jmoneco.2019.08.016; would give ECB
  meeting dates and announcement windows), ALFRED/FRED vintage dates for PAYEMS without an API key, BLS Employment Situation
  schedule pages, DOL weekly-claims pages. **None could be opened**: every web fetch (9 URLs) failed with a fetch-permission
  timeout (no HTTP answer, nothing read), and the workspace proxy refuses these hosts (403 CONNECT). All of the above stay
  `UNVERIFIED`; nothing is cited as evidence.
- No item added: the verified-links rule (CLAUDE.md rule 3) forbids pre-registering on sources not opened, and R105's judgement
  that price-only families are exhausted stands. 0 trials used (dev 255, val 9, total 264).
- Next refill run: retry the ECB EA-MPD dataset page first (it would unblock an ECB-meeting event line without an API key), then
  ALFRED. A runner-side reachability probe of these URLs is possible but was not queued: it is a data-source decision listed for
  the human in agent_decision_log R105.

### Refill note R107 (not an item; no item added)
- 2026-11-12 R107 refill pass. Retried per R106: ECB EA-MPD dataset file
  (`https://www.ecb.europa.eu/pub/pdf/annex/Dataset_EA-MPD.xlsx`), the ECB Governing Council meeting calendar, the ECB press
  conference index and the Fed FOMC historical page for 2016. **All 4 failed** with the same fetch-permission timeout as R106 (no
  HTTP answer, nothing read). All stay `UNVERIFIED`; nothing cited.
- Checked repo state instead: the research-batch runner has reached federalreserve.gov before (`backtests/calendars/fomc_dates.csv`,
  75 rows, used by E040) but got HTTP 403 from bls.gov (`backtests/calendars/nfp_fetch_report.json`, B12 blocked R024) and timeouts
  from cmegroup.com (B13). An ECB-meeting line would also sit below the R090 power floor (~48 meetings on dev, ECB rate changes on dev
  almost none, academic_studies note R068), so the ECB calendar alone would not yield a passable item.
- No item added (rule 3; R105 judgement on exhausted price-only families stands). 0 trials used (dev 255, val 9, total 264).
- Third consecutive refill run without a new item (R105, R106, R107). The queue now waits on the human-decision list in
  agent_decision_log R105 (sanctioned release calendar / FRED API key secret, OIS or options data, OOS use for seen windows). This is
  not a pipeline failure (research-batch healthy, last run 43103436725 success), so no notification under the protocol.

### Refill note R108 (not an item; no item added)
- 2026-11-12 R108 refill pass, new angle: FX option-expiry pinning at the 10:00 NY cut (spot attracted to large strikes, delta-hedge
  mechanism known from equity options). Searches returned only broker/news expiry lists (vtmarkets.com, newsquawk.com,
  investinglive.com; not evidence) and one academic record: Mozayyan Esfahani (2019), "Algorithmic Trading and Prediction of Foreign
  Exchange Rates Based on the Option Expiration Effect", KTH bachelor thesis 2019:068,
  [record](https://openaccess.library.uitm.edu.my/Record/ndltd-UPSALLA1-oai-DiVA.org-kth-252297/Details) (opened: metadata + abstract
  only). Abstract: an "option relevance coefficient" built from expiring options, used in a GARCH-X model; "more scientific research
  is required to be able to draw significant conclusions" (verbatim). Full text (urn.kb.se resolver) failed with a fetch-permission
  timeout; pairs, period, windows and effect sizes stay `UNVERIFIED`.
- Not added: the mechanism needs per-date strike/notional expiry data (DTCC/broker lists), which the repo lacks; a round-number proxy
  would re-test the E018/E045 level family (both NONE on dev) without a verified basis. Adds to the R105 data-needs list
  (option-expiry notional by strike).
- No item added (rule 3; R105 judgement stands). 0 trials used (dev 255, val 9, total 264). Fourth consecutive refill without an item.

### B54: Even- vs odd-week FOMC cycle, EUR/USD daily (signal test, dev) → E046 · `done` (2026-11-12 R111: NONE, n 1281, +1.152 pips, CI (-2.517, 4.226), t p 0.2265. R110: pre-registered as E046, rule unchanged, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-12 R109 refill)
- **Mechanism [PUB for equities only; EUR/USD is our extension]:** Cieslak, Morse & Vissing-Jorgensen (2014 draft, VERIFIED partial,
  research/academic_studies.md): risk-asset returns are high in even FOMC-cycle weeks (0, 2, 4, 6) and flat/negative in odd weeks,
  also for non-US equities in USD; fed funds futures volatility is higher in even weeks (Fed news arrives then). Our reading: Fed news
  flow in even weeks is on average accommodative / risk-on, which weakens the USD. **Sign fixed now: long EUR/USD in weeks 2, 4, 6;
  short in weeks -1, 1, 3, 5.** Week 0 is **excluded** (it holds the FOMC statement day, already tested as B11/E013 SIGNAL dev,
  E014 NONE val; a known calendar effect, LEAD criterion 4). No FX evidence in the text read; pattern absent pre-1994 per the paper.
- **Cycle (fixed now):** day 0 = `statement_date` of scheduled, non-cancelled meetings in `backtests/calendars/fomc_dates.csv`
  (unscheduled meetings ignored). Days counted in EUR/USD trading dates Mon-Fri (`sessions.trading_date`, 17:00 NY boundary; US
  holidays are not skipped, deviation from the paper's business days, stated as a limitation). For trading date D: k_next = -(trading
  dates from D to the next statement date); if k_next >= -6 use it, else k = trading dates since the previous statement date. Weeks:
  -1: k -6..-2; 0: -1..3; 1: 4..8; 2: 9..13; 3: 14..18; 4: 19..23; 5: 24..28; 6: 29..33; k > 33 -> unassigned, excluded (counted).
  Dates before the first 2015 meeting's week -1 -> excluded (counted).
- **Trade (fixed now, E044 convention):** entry 20:00 NY at the start of trading date D (after the roll spread normalises, lesson
  R059), exit 16:55 NY on D. Missing entry/exit quote -> excluded (counted); entry spread > 2.0 pips -> skipped (counted). Position s =
  +1 (weeks 2, 4, 6) or -1 (weeks -1, 1, 3, 5). Signed return = s x (mid exit - mid entry), pips.
- **Decision rule (draft, = E041/E044 rule):** < 500 dates -> NONE. SIGNAL if mean signed > 1.0 pip AND moving-block bootstrap 95% CI
  lower > 0 (blocks of 20 consecutive dates, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI lower >
  0 or p < 0.05); else NONE. A SIGNAL earns B55.
- **Power note:** ~48 dev meetings x ~25 assigned non-week-0 dates -> n ~1,200; ~21 h hold, SD ~40-45 pips -> SE ~1.3 pips; a ~2.5-3
  pip edge is detectable. 264 registered trials so far: a single p just under 0.05 is expected noise (lesson R092), hence B55.
- **Descriptive (not in rule):** mean by cycle week (-1..6) incl. week 0 (reported only); even-only long and odd-only short legs
  separately; by year (lesson R092); unconditional long mean over the same hold; same test with the cycle lagged one trading date
  (paper's Panel B analogue, reported only); SPEC 4 net and costs x1.5.
- **Contamination note:** the week-0 statement day was tested (E013/E014) and is excluded; E040 tested the 12-24 h post-FOMC window
  (inside week 0, excluded). No other FOMC-cycle partition has been computed in this repo (grep R109). Daily holds 20:00 -> 16:55 NY
  were used in E044 (unconditional mean known as descriptive only). Dev usable.
- **Calendar label:** this *is* a calendar effect (FOMC cycle); if it ever became a lead it is the strategy itself, not a confound.
- **Data:** EUR/USD 1-minute bid/ask bars and fomc_dates.csv (2015-2023, already validated E013) in repo; no download.

### B55: FOMC-cycle even/odd weeks, val confirmation (signal test, val only) · `done` (2026-11-12 R111: closed unearned, 0 trials; B54 NONE on dev (E046). Added 2026-11-12 R109; was: earned only if B54 returns SIGNAL on dev)
- B54 unchanged on val (2021-01-21 .. 2023-06-30), own pre-registration, 1 val trial, < 200 dates -> NONE, p < 0.05, block-20
  bootstrap. If B54 is not SIGNAL, B55 closes unearned with 0 trials.

### Refill note R109 (not an item)
- 2026-11-12 R109 refill pass, new angle: FOMC-cycle calendar using the FOMC date file already in the repo (avoids the blocked
  release-date sources). Opened: Cieslak-Morse-Vissing-Jorgensen 2014 draft (NBER conference PDF, ~32% verbatim). Not opened: Stern
  PDF (fetch-permission timeout), BIS link (agenda page only). Added B54 (dev, 1 trial) and B55 (val, blocked). 0 trials used.

### Refill note R112 (not an item; no item added)
- 2026-11-12 R112 refill pass, new angle: FOMC minutes releases (14:00 ET, a date set disjoint from the statement days used in
  E013/E014/E040 and from week 0 of E046). Opened: Rosa (2013, FRBNY EPR, full extracted text; entry in research/academic_studies.md).
  Data check: official minutes release dates ("Released <date>") are in the federalreserve.gov pages the runner already saved
  (`backtests/calendars/raw_html/fomchistorical2017-2019.html`, `fomccalendars.html` for 2021-2026); 2017 releases are all 21 days
  after the statement date. 2015, 2016 and 2020 pages are not saved (a phase-1 runner fetch would be needed; runner reaches
  federalreserve.gov, E013).
- Not added: a continuation test of the first post-release reaction (sign(13:59 -> 14:15 ET) x 14:15 -> 15:15 ET). Rosa measures
  volatility and volume only: no direction, no tone/surprise, no drift or reversal, and the response "has declined since 2008"
  (verbatim), so a continuation edge on dev (2015-2020) has no published basis. ~48 dev releases with a ~1-hour target put the CI
  half-width at several pips (lesson R090 scaling); an unpublished continuation of that size is implausible, and the calendar-free
  08:30 continuation (B21/E026) was NONE. A trial would only inflate the count. Rosa is usable later only as a volatility filter
  (B2-type "when to trade"), not as a direction signal.
- No item added (rule 3 + R090 power floor). 0 trials used (dev 256, val 9, total 265). R105 data-needs list for the human unchanged.

### Refill note R113 (not an item; no item added)
- 2026-11-12 R113 refill pass, angle: daily dollar-factor / cross-currency time-series predictability for EUR/USD (other USD pairs
  are downloadable on the runner). One extended search; hits were Krohn-Mueller-Whelan (already in academic_studies.md, tested E022-E025,
  E032), Bollerslev et al. intraday *equity* factor-zoo predictability (not FX), and a 2026 JIFMIM "Factor timing in currency markets"
  (monthly, cross-sectional portfolios; not opened). Nothing opened that gives a single-pair EUR/USD daily or intraday direction rule;
  FX lead-lag at minute horizons was already judged below the tradable horizon (R080 note, line ~655).
- No item added (rule 3: nothing verified to build on). 0 trials used (dev 256, val 9, total 265). R105 data-needs list for the human
  unchanged; this is the sixth refill in a row without a pre-registrable item.
