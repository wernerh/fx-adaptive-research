# Research backlog

Ordered by priority. Status: `ready` | `running` | `done` | `blocked` | `parked`.
Autonomous runs take the top `ready` item (docs/AUTONOMOUS_PROTOCOL.md). Add items at the bottom; re-rank only with a
reason in agent_logs/agent_decision_log.md. Dev = 2015-01-01..2020-12-31, val = 2021-01-21..2023-06-30, OOS locked.

Trial count so far on dev: **261** (E001: 7, E006: 14, E004: 1, E007: 4, E008: 4, E009: 192 exploratory cells, E010: 2, E011: 2, E013: 1, E018: 1, E019: 1, E020: 1, E021: 1, E022: 1, E024: 1, E026: 1, E027: 1, E028: 1, E030: 1, E031: 1, E033: 2, E034: 2, E035: 2, E037: 2, E038: 1, E039: 2, E040: 1, E041: 1, E042: 1, E043: 1, E044: 1, E045: 1, E046: 1, E047: 1, E048: 1, E049: 1, E050: 1, E051: 1). Val-only trials: **9** (E012: 2, E014: 1, E017: 1, E023: 1, E025: 1, E029: 1, E032: 1, E036: 1). Total registered trials: **270**. Update after every experiment. (R302: refill pass, no item added, 0 trials. R301: refill pass, no item added, 0 trials. R300: refill pass, no item added, 0 trials. R299: refill pass, no item added, 0 trials. R298: refill pass, no item added, 0 trials. R297: refill pass, no item added, 0 trials. R296: refill pass, no item added, 0 trials. R295: refill pass, no item added, 0 trials. R294: refill pass, no item added, 0 trials. R288: refill pass, no item added, 0 trials. R275: refill pass, no item added, 0 trials. R274: refill pass, no item added, 0 trials. R273: refill pass, no item added, 0 trials. R272: refill pass, no item added, 0 trials. R271: refill pass, no item added, 0 trials. R270: refill pass, no item added, 0 trials. R269: refill pass, no item added, 0 trials. R267: refill pass, no item added, 0 trials. R266: refill pass, no item added, 0 trials. R262: refill pass, no item added, 0 trials. R261: refill pass, no item added, 0 trials. R258: refill pass, no item added, 0 trials. R252: refill pass, no item added, 0 trials. R250: refill pass, no item added, 0 trials. R244: refill pass, no item added, 0 trials. R235: refill pass, no item added, 0 trials. R232: refill pass, no item added, 0 trials. R230: refill pass, no item added, 0 trials. R229: refill pass, no item added, 0 trials. R226: refill pass, no item added, 0 trials. R225: refill pass, no item added, 0 trials. R223: refill pass, no item added, 0 trials. R222: refill pass, no item added, 0 trials. R220: refill pass, no item added, 0 trials. R213: E051 ran, dev +1; B63 closed unearned, 0 trials. R212: E051/B62 pre-registered, 1 dev trial counted when it runs. R211: refill added B62 (1 dev trial when it runs), B63 (blocked): 0 trials. R210: E050 ran, dev +1; B61 closed unearned, 0 trials. R157: E049 ran, dev +1; B59v closed unearned, 0 trials. R156: E049/B59 pre-registered, 1 dev trial counted when it runs. R155: E048 ran, dev +1; B58v closed unearned, 0 trials. R154: E048/B58 pre-registered, 1 dev trial counted when it runs. R126: E047 ran, dev +1; B57 closed unearned, 0 trials. R125: E047/B56 pre-registered, 1 dev trial counted when it runs. R124: refill added B56 (1 dev trial when it runs), B57 (blocked): 0 trials. R111: E046 ran, dev +1; B55 closed unearned, 0 trials. R107: refill pass, no item added, 0 trials. R106: refill pass, no item added, 0 trials. R105: refill pass, no item added, 0 trials. R104: E045 ran, dev +1; B53 closed unearned, 0 trials. R103: E045/B52 pre-registered, 1 dev trial counted when it runs. R101: E044 ran, dev +1; B51 closed unearned, 0 trials. R100: E044/B50 pre-registered, 1 dev trial counted when it runs. R099: refill added B50 (1 dev trial when it runs), B51 (blocked): 0 trials. R098: E043 ran, dev +1; B49 closed unearned, 0 trials. R097: E043/B48 pre-registered, 1 dev trial counted when it runs. R096: refill added B48 (1 dev trial when it runs), B49 (blocked): 0 trials. R095: E042 ran, dev +1; B47 closed unearned, 0 trials. R094: E042/B46 pre-registered, 1 dev trial counted when it runs. R092: E041 ran, dev +1. R091: E041/B45 pre-registered, 1 dev trial counted when it runs. R090: E040 ran, dev +1; B44 closed unearned, 0 trials. R089: E040/B43 pre-registered, 1 dev trial counted when it runs. R087: E039 ran, dev +2; B42 closed unearned, 0 trials. R086: E039/B40+B41 pre-registered, 2 dev trials counted when it runs (0 if BLOCKED). R084: E038 ran, dev +1; B39 closed unearned, 0 trials. R083: E038/B38 pre-registered, 1 dev trial counted when it runs. R082: refill added B38 (1 dev trial when it runs), B39 (blocked): 0 trials. R081: E037 ran, dev +2; B37 closed unearned, 0 trials. R080: E037/B35+B36 pre-registered, 2 dev trials counted when it runs. R079: refill added B35, B36 (2 dev trials when they run), B37 (blocked): 0 trials. R078: E036 ran, val +1. R077: E036/B34 pre-registered, 1 val trial counted when it runs. R076: E035 ran, dev +2; B33 SIGNAL earns B34 (1 val trial when it runs). R075: E035/B32+B33 pre-registered, 2 dev trials counted when it runs. R074: refill added B32, B33 (2 dev trials when they run), B34 (blocked): 0 trials. R073: E034 ran, dev +2. R072: E034/B30 pre-registered, 2 dev trials counted when it runs. R071: refill added B30 (2 dev trials when it runs), B31 (blocked): 0 trials. R070: E033 ran, dev +2. R069: E033/B28+B29 pre-registered, 2 dev trials counted when it runs. R068: refill added B28, B29: 0 trials until pre-registered. R067: E032 ran, val +1. R066: E032/B27 pre-registered, 1 val trial counted when it runs. R065: refill added B27: 0 trials until pre-registered. R064: E031 ran, dev +1. R063: E031/B26 pre-registered, 1 dev trial counted when it runs. R062: E030 ran, dev +1. R061: E030/B25 pre-registered, 1 dev trial counted when it runs. R060: refill added B25, B26: 0 trials until pre-registered. R059: E029 ran, val +1. R058: E029/B24 pre-registered, 1 val trial counted when it runs. R057: E028 ran, dev +1. R056: E028/B23 pre-registered, 1 dev trial counted when it runs. R054: E027 ran, dev +1. R053: E027/B22 pre-registered, 1 dev trial counted when it runs. R052: E026 ran, dev +1. R051: E026/B21 pre-registered, 1 dev trial counted when it runs. R050: refill added B21, B22: 0 trials until pre-registered. R049: E025 ran, val +1. R048: E025/B20v pre-registered, 1 val trial counted when it runs. R047: E024 ran, dev +1; B20v added, 0 trials until pre-registered. R045: E023 ran, val +1. R044: E023/B19v pre-registered, 1 val trial counted when it runs. R043: E022 ran, dev +1; B19v added, 0 trials until pre-registered. R042: E022/B19 pre-registered, 1 dev trial counted when it runs. R041: refill added B19, B20: 0 trials until pre-registered. R040: E021 ran, dev +1. R039: E021/B18 pre-registered, 1 dev trial counted when it runs. R038: E020 ran, dev +1. R037: E020/B17 pre-registered, 1 dev trial counted when it runs. R036: refill added B17, B18: 0 trials until pre-registered. R035: E019 ran, dev +1. R034: E019/B16 pre-registered, 1 dev trial counted when it runs. R033: E018 ran, dev +1. R032: E018/B15 pre-registered, 1 dev trial counted when it runs. R031: refill added B15, B16: 0 trials until pre-registered. R030: E017 ran, val +1. R029: E017/B14 pre-registered, 1 val trial counted when it runs. R028: E016/B13 blocked after second CME fetch failure, 0 trials. R027: E016 phase-1 re-fetch queued, 0 trials. R026: E016/B13 pre-registered, 1 dev trial counted when phase 2 runs. R025: refill added B13, B14: 0 trials until pre-registered. R023: E015/B12 pre-registered, 1 dev trial counted when phase 2 runs. R022: E014 ran, val +1. R020: E013 phase 2 ran, dev +1. R016 refill added B11, B12: 0 trials until pre-registered. R017: E013/B11 pre-registered, 1 dev trial counted when phase 2 runs.)

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

### Refill note R114 (not an item; no item added)
- 2026-11-12 R114 refill pass, new angle: daylight-saving-time transitions (US and euro area switch on different Sundays in March and
  Oct/Nov, so EUR/USD gets 4 dated events per year with no external data needed). Opened: Nower (2024, Economics Letters, DOI
  10.1016/j.econlet.2024.111813; repository PDF ~95% + Durham press release; entry in research/academic_studies.md). Pre-holiday
  search returned only a trading-blog concept page and fix papers already in the library (not evidence; nothing opened).
- Not added: a "short the currency entering DST / long the one leaving" weekly test on EUR/USD. Published effect is ~10 bp (~11 pips)
  on weekly *averages* relative to currency-month-year fixed effects, not a signed return from a tradable entry; it is insignificant
  with currency FE only (Table 1 col 1), and weakest for the USD (press release; paper drops the US to sharpen it). ~24 dev events
  with a one-week target (weekly SD order 100+ pips) give a CI half-width of ~50 pips, far above the effect (lesson R090 power floor).
  A trial would only inflate the count.
- No item added (rule 3 satisfied, but R090 power floor). 0 trials used (dev 256, val 9, total 265). R105 data-needs list for the
  human unchanged; seventh refill in a row without a pre-registrable item.

### Refill note R115 (not an item; no item added)
- 2026-11-12 R115 refill pass, angles: (a) USD returns by region-of-trading hours, (b) same-time-of-day return persistence
  (Heston-Korajczyk-Sadka style) for FX. Search (a) returned only work already in research/academic_studies.md and tested:
  Krohn-Mueller-Whelan (E022-E025, E032), Breedon-Ranaldo (B14/E017, WEAK on val, closed), Ranaldo 2007/2009 (R082 note). Search (b)
  returned only the equity paper (Heston, Korajczyk & Sadka 2010, JF) and its mirrors; no FX source testing return direction, same
  finding as the R068 note. Nothing new opened; nothing cited as evidence.
- No item added (rule 3: no verified basis; R105 judgement on exhausted price-only families stands). 0 trials used (dev 256, val 9,
  total 265). Eighth refill in a row without a pre-registrable item; the queue waits on the human-decision list in
  agent_decision_log R105. Not a pipeline failure (last run 43155068137 success, recorded as E046), so no notification.

### Refill note R116 (not an item; no item added)
- 2026-11-12 R116 refill pass, new angle: spread / liquidity-shock states as a direction signal for EUR/USD (does a spread widening
  predict a reversal or drift?). Two standard searches; hits were FX spread-determinant and volatility papers (Kaul-Sapp Y2K 2004,
  NBER w4737 spreads vs anticipated volatility), the KMW fixings AEA 2020 page (already in research/academic_studies.md; its
  high-spread-state reversal claim stays `UNVERIFIED` and the vol-state version was tested E022-E025), Cespa-Gargano-Riddiough-Sarno
  FX volume (in library; volume tested E033) and equity tick-size work. Opened: Albuquerque, Song & Yao (Nov 2017), "The Price Effects
  of Liquidity Shocks: A Study of SEC's Tick-Size Experiment",
  [PDF](https://www.runi.ac.il/media/sseknk1u/the-price-effects-of-liquidity-shocks-a.pdf) (~34% verbatim): US small-cap equities only,
  permanent ~1-4% price drop after an exogenous tick-size increase; no FX content. Not evidence for an EUR/USD rule.
- No item added (rule 3: no verified FX basis; R105 judgement on exhausted price-only families stands). 0 trials used (dev 256, val 9,
  total 265). Ninth refill in a row without a pre-registrable item; the queue waits on the human-decision list in
  agent_decision_log R105. Not a pipeline failure (last run 43155068137 success, recorded as E046), so no notification.

### Refill note R117 (not an item; no item added)
- 2026-11-12 R117 refill pass, new angles: (a) lagged VIX / risk-off changes -> next-day EUR/USD (safe-haven USD), (b) lagged
  US-German yield-differential changes -> next-day EUR/USD. Two standard searches. Hits for (a): a 2025 high-school journal piece
  (NHSJS, "Predicting US Dollar Movements Using the VIX and Machine Learning"; not peer-reviewed, not opened, not evidence), news and
  chart-blog pages (contemporaneous USD/VIX correlation only), and two Toronto Metropolitan University working papers (not opened).
  Hits for (b): an MRU repository entry "Determining the EUR/USD exchange rate with U.S. and German government bond yields in the
  post-crisis period" (title indicates a contemporaneous level relation, not a lagged rule; not opened), FXStreet news, the Krohn FRBSF
  paper (KMW family, already tested E022-E025, E032) and a BIS WP 1320 (not opened). Nothing opened gives a verified lagged daily or
  intraday EUR/USD direction rule; both cross-asset ideas also repeat the lagged cross-asset family that returned NONE three times
  (B35/B36 equity E037, B45 oil E041, B46 gold E042), and VIX has no verified runner-downloadable minute source.
- No item added (rule 3: no verified basis). 0 trials used (dev 256, val 9, total 265). R105 data-needs list for the human unchanged;
  tenth refill in a row without a pre-registrable item. Not a pipeline failure (last run 43155068137 success, recorded as E046).

### Refill note R118 (not an item; no item added)
- 2026-11-12 R118 refill pass, new angle: intraday lead-lag from rates (Bund / US Treasury futures, yields) to EUR/USD (does a lagged
  5-60 min rates move predict the next EUR/USD move?). Two standard searches; hits were a Treasury co-jump arXiv paper, FX news and
  chart pages (contemporaneous yield/FX commentary only), an AEA 2019 page and a PhD dissertation (not opened). Opened: "Information
  arrival, jumps and cojumps in European financial markets: Evidence using tick by tick data" (June 2013, EFMA 2013 Reading,
  [PDF](https://www.efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2013-Reading/papers/Paper_June_2013.pdf), ~52% verbatim incl.
  abstract, data, method, results; authors not shown): 5-min EUR/USD, EURIBOR and index futures 2003-2010, same-interval cojumps at
  US releases only; no lead-lag, no Bund/Treasury data. Fuess-Mager-Stein-Zhao "A High-Frequency Perspective" (NTNU repository) not
  openable (fetch-permission timeout), `UNVERIFIED`, not used.
- No item added (rule 3: no verified lagged basis; minute-horizon FX lead-lag already judged below the tradable horizon, note ~line 655;
  lagged cross-asset family NONE x3, E037/E041/E042). 0 trials used (dev 256, val 9, total 265). Eleventh refill in a row without a
  pre-registrable item; queue waits on the human-decision list in agent_decision_log R105. Not a pipeline failure (last run
  43155068137 success, recorded as E046), so no notification.

### Refill note R119 (not an item; no item added)
- 2026-11-12 R119 refill pass, new angle: daily uncertainty / financial-conditions indices (EPU, NFCI) as lagged predictors of
  next-day EUR/USD direction (indices are free downloads). One standard search; opened three pages (details in
  research/academic_studies.md): Bartsch 2019 JIMF (daily EPU, USD/GBP volatility only), Christou-Gupta-Hassapis-Suleman 2018
  J. Forecasting (abstract claims return forecastability for 13 countries; frequency/horizon/magnitudes not shown, design `UNVERIFIED`),
  Fossati-Lu 2025 U. Alberta WP (weekly NFCI, 9 USD pairs incl. EUR: "does not provide a strong signal about the direction", no OOS
  point-forecast gain over the random walk).
- No item added (rule 3: no verified daily directional basis; the one verified FX-direction study is negative; lagged cross-asset /
  macro-state family NONE x3, E037/E041/E042). 0 trials used (dev 256, val 9, total 265). Twelfth refill in a row without a
  pre-registrable item; queue waits on the human-decision list in agent_decision_log R105. Not a pipeline failure (last run
  43155068137 success, recorded as E046), so no notification.

### Refill note R120 (not an item; no item added)
- 2026-11-12 R120 refill pass, angle: CFTC COT positioning *extremes* (peaks/troughs of speculators' net positions) as a lagged
  EUR/USD direction signal, distinct from the level/change relation Klitgaard-Weir 2004 found non-predictive (note R082). One standard
  search; opened the EconPapers records of Tornell & Yuan (2012, JFM 32(2); WP UMBC 09-116; entry in research/academic_studies.md):
  abstract says peaks/troughs "are generally useful predictors" with speculative measures forecasting continuation, but currencies,
  horizon, the peak/trough definition (a real-time vs ex-post identification is the crux for look-ahead) and magnitudes are not visible.
  WP PDF (umbc.edu) fetch-permission timeout, `UNVERIFIED`.
- Not added: a rule cannot be pre-registered without the indicator definition, and COT is weekly: ~300 dev weeks with extremes a small
  subset puts the CI half-width far above any plausible effect (lesson R090 power floor), and Klitgaard-Weir found no next-week
  predictability for the euro. A trial would only inflate the count.
- No item added (rule 3: design unverified; R090 power floor). 0 trials used (dev 256, val 9, total 265). Thirteenth refill in a row
  without a pre-registrable item; queue waits on the human-decision list in agent_decision_log R105. Not a pipeline failure (last run
  43155068137 success, recorded as E046), so no notification.

### Refill note R121 (not an item; no item added)
- 2026-11-12 R121 refill pass, angle: short-horizon (1-4 week) EUR/USD return momentum/reversal and sentiment-driven currency
  reversals. One standard search; opened Filippou, Taylor & Wang (2021, "Media Sentiment and Currency Reversals", CEPR DP16049,
  https://repec.cepr.org/repec/cpr/ceprdp/DP16049.pdf, ~39% verbatim; entry in research/academic_studies.md) and the CXO Advisory
  summary (https://www.cxoadvisory.com/momentum-investing/short-term-currency-exchange-rate-momentum, full page, secondary) of
  Raza-Marshall-Visaltanachoti weekly currency momentum.
- Not added: Filippou et al. sort on a news-tone score (bag-of-words on media articles), monthly rebalanced cross-sectional and
  time-series portfolios across 48 currencies; the signal needs a news-sentiment dataset the repo does not have and the runner cannot
  build from a sanctioned source (adds item (6) "news-sentiment data" to the R105 human-decision list). Raza et al. weekly momentum is
  cross-sectional over 63 currencies, gross of costs, and was already rejected for a single-pair re-test in refill note R085
  (shorter-lookback re-test of B16/E019; non-overlapping 4-week holds give ~75 dev periods, below the R090 power floor).
- No item added (rule 3 and R090). 0 trials used (dev 256, val 9, total 265). Fourteenth refill in a row without a pre-registrable item;
  queue waits on the human-decision list in agent_decision_log R105. Not a pipeline failure (last run 43155068137 success, recorded as
  E046), so no notification.

### Refill note R122 (not an item; no item added)
- 2026-11-12 R122 refill pass, angle: FX calendar anomalies (turn-of-the-month, turn-of-the-year, day-of-week) for EUR/USD daily
  returns (no external data needed). One standard search. Opened: Kumar (2018, SEF 35(3) 441-456, DOI 10.1108/SEF-08-2015-0192,
  [IDEAS](https://ideas.repec.org/a/eme/sefpps/sef-08-2015-0192.html), abstract only; already in research/academic_studies.md and
  rejected in the R065 refill, line ~453): 20 USD pairs 1995-2014, Mon/Wed negative vs Thu/Fri positive, TOM/January patterns, but
  "these calendar anomalies seem to have disappeared for almost all currencies during 2005 to 2014". Stefanescu & Dumitriu (2020,
  MPRA 99365, https://mpra.ub.uni-muenchen.de/99365, abstract only; already cited ~line 928): RON/USD turn-of-year, no magnitudes.
  Konttinen (2018, Aalto MSc thesis, https://core.ac.uk/download/162136978.pdf, ~20% verbatim): equity indices only, TOM effect
  weakening/disappearing. EconBiz record of Kumar 2018 refused automated access (not retried).
- Not added: the only FX source with a USD-pair result says the effects vanished before our dev block (2015-2020); weekday x hour
  cells were already scanned on dev in E009; no new verified basis (rule 3). A trial would only inflate the count.
- No item added. 0 trials used (dev 256, val 9, total 265). Fifteenth refill in a row without a pre-registrable item; the queue waits
  on the human-decision list in agent_decision_log R105. Not a pipeline failure (last run 43155068137 success, recorded as E046).

### Refill note R123 (not an item; no item added)
- 2026-11-12 R123 refill pass, angle: US Treasury auction days -> EUR/USD intraday direction. One standard search; hits were FX news
  and market-wrap pages (Convera, Saxo, investinglive, FXStreet, MarketPulse, a forum repost; contemporaneous commentary, not evidence,
  not opened) and FRBSF conference files (Krohn paper/slides, KMW family already tested E022-E025, E032; Somogyi slides, not opened).
  The auction-shock line was already pre-registered and tested as B40/B41 (E039: NONE, n 431). Nothing new opened; nothing cited.
- No item added (rule 3: no new verified basis; family already tested). 0 trials used (dev 256, val 9, total 265). Sixteenth refill in a
  row without a pre-registrable item; the queue waits on the human-decision list in agent_decision_log R105. Not a pipeline failure
  (last run 43155068137 success, recorded as E046), so no notification.

### B56: Pivot-point R1/S1 first touch, continuation ("inverse pivot"), EUR/USD (signal test, dev) → E047 · `done` (2026-11-12 R126: NONE, n 1270, -0.187 pips, CI (-1.588, 1.181), t p 0.6078. R125: pre-registered as E047, rule unchanged, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-12 R124 refill)
- **Mechanism [PUB, weak]:** Johnsson & Frykmer (2019, Lund University master's essay, VERIFIED partial full text,
  research/academic_studies.md): classic floor-trader pivot levels traded the traditional way (long at support, short at resistance)
  win < 50% for EUR/USD; verbatim "profits can be generated by implementing the strategy inversely" and "For two of the currency pairs,
  the support levels defined from the pivot points should be used as selling signals and the resistance levels should be used as
  buying signals". EUR/USD Table 2 (verbatim): weighted traditional win rate 41.4% (multiple 0.15%, binomial 5%), R-only 39.0%; R1 38.5%
  (10%), S1 45.8% (n.s.). Our reading: widely watched pivot levels attract stop orders just beyond them (Osler 2002/2003 stop-cluster
  logic transferred from round numbers to pivot levels), so a first touch tends to run through, not bounce. **Sign fixed now:
  continuation - long after the first touch of R1, short after the first touch of S1.** Weak basis: non-peer-reviewed thesis, win
  rates only, no costs, no P&L, 7 months of EUR/USD tick data; the S side was not significant in the thesis (symmetric test chosen
  anyway, stated before any dev statistic).
- **Levels (fixed now, = thesis eqs. 1, 2, 5):** day = UTC calendar date (thesis: "a new day starts at UTC+-0"); Sunday bars are merged
  into Monday's date (thesis); Saturday none. From the previous such date d-1 (Monday's previous date = Friday): H, L = max of mid high /
  min of mid low over all 1-minute bars of d-1, C = mid close of the last bar of d-1; P = (H + L + C)/3; R1 = 2P - L; S1 = 2P - H.
  Mid in exact 2 x mid units as E045 (`_to_units`). d-1 needs >= 1,000 bars (Friday/Monday-with-Sunday included), else date excluded
  (counted).
- **Event (fixed now, E045 touch convention):** 1-minute bar t on UTC date d, bar t-1 on the same date. R1 touch: c(t-1) < R1 <= h(t)
  -> s = +1. S1 touch: c(t-1) > S1 >= l(t) -> s = -1. Only the **first** touch of each level per date; at most one R1 and one S1 event
  per date. A bar touching both: skipped (counted).
- **Trade and exclusions (fixed now, = E045 conventions except the hold):** entry = open of the first bar at or after t + 1 min (<= t + 5
  min); exit = open of the first bar at or after entry + 120 min (<= + 5 min) (thesis target/stop resolves in "about two to three
  hours"); window needs >= 110/120 bars. Skipped and counted under the first failing check: coverage; entry or exit NY time in [16:30,
  18:30) (roll); entry spread > 2.0 pips (SPEC 4); entry before the previous trade's exit (overlap). Signed return = s x (mid open at
  exit - mid open at entry), pips.
- **Decision rule (draft, = E045 rule):** < 300 events -> NONE. SIGNAL if mean signed > 1.0 pip AND date-cluster bootstrap 95% CI lower
  > 0 (resample UTC dates with all their events, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if mean > 0 and (CI lower
  > 0 or p < 0.05); else NONE. A SIGNAL earns B57.
- **Power note:** R1 or S1 is touched on most dates (mean |R1 - S1| = H - L of the prior day); expect ~1-1.5 events per date, ~1,500-2,000
  on dev. 120-min SD ~14-16 pips -> SE ~0.4 pips; the 1-pip bar binds. ~265 registered trials: one p just under 0.05 is expected noise
  (lesson R092), hence B57.
- **Descriptive (not in rule):** R1-only and S1-only legs; 60- and 180-minute holds; the thesis-faithful bracket (target/stop = entry
  +- 0.15% x P, first hit, win rate vs 50%); traditional-direction mean (= minus the rule mean); events and mean excluding 2017-06-01 ..
  2017-12-29 (the thesis's EUR/USD sample lies inside our dev block); by year (lesson R092); share and mean of events within +-15 min of
  08:30 / 10:00 NY and 16:00 London; SPEC 4 net and costs x1.5; control levels R1/S1 shifted by +-0.0023 through the same procedure.
- **Contamination note:** the sign comes from the thesis, whose EUR/USD sample (Jun-Dec 2017) is ~10% of our dev dates; reported
  separately above. No pivot statistic has been computed in this repo (grep "pivot" R124: none). Round-number touches (E045, fade, NONE,
  -0.71) and close crossings (E018) are different levels; the E045 negative fade mean is consistent in sign with continuation but was
  not used to fix the sign. Dev usable.
- **Calendar label:** price-level effect, not a time-of-day, fix or release effect (report the release/fix-time share).
- **Data:** EUR/USD 1-minute bid/ask bars in repo; no download. Code reuses the E045 touch/fill machinery (`fxresearch.round_numbers`).

### B57: Pivot-point R1/S1 continuation, val confirmation (signal test, val only) · `done` (2026-11-12 R126: closed unearned, 0 trials; B56 NONE on dev (E047). Added 2026-11-12 R124; was: earned only if B56 returns SIGNAL on dev)
- B56 unchanged on val (2021-01-21 .. 2023-06-30), own pre-registration, 1 val trial, < 120 events -> NONE, p < 0.05, same date-cluster
  bootstrap. If B56 is not SIGNAL, B57 closes unearned with 0 trials.

### Refill note R124 (not an item)
- 2026-11-12 R124 refill pass, angle: mechanically computed support/resistance (pivot points) in intraday FX. One standard search.
  Opened (web-fetch): Osler (2000), FRBNY EPR 6(2), [HTML/PDF](https://www.newyorkfed.org/medialibrary/media/research/epr/00v06n2/0007osle.html)
  (~64% verbatim; firm-published levels only, DEM/JPY/GBP 1996-98, bounce 60.8% vs 56.2% arbitrary, 15-min horizon; not mechanical, not
  used for the sign); Johnsson & Frykmer (2019), Lund master's essay,
  [record](https://lup.lub.lu.se/student-papers/record/8979805) and [PDF](https://lup.lub.lu.se/student-papers/record/8979805/file/8979814.pdf)
  (~70% verbatim incl. method and EUR/USD Tables 2-3; conclusion and GBP/JPY results summary-only). Added B56 (dev, 1 trial when it
  runs) and B57 (val, blocked). 0 trials used (dev 256, val 9, total 265). Ends the run of 16 refills without an item.

### Refill note R127 (not an item; no item added)
- 2026-11-12 R127 refill pass, angles: (a) EUR/USD direction around the 16:00 NY US-equity close, (b) lagged realized volatility as a
  next-day EUR/USD direction predictor. Two standard searches. Hits for (a): the Krohn fixings paper (KMW family, already tested
  E022-E025, E032), Marsh & Miao (already rejected, note ~line 603), news pages (not evidence) and two CXO Advisory pages, opened via
  web-fetch: [p=16673](https://www.cxoadvisory.com/calendar-effects/intraday-u-s-stock-market-behavior/) (SPY one-minute 2007-08 only,
  no FX) and [p=21224](https://www.cxoadvisory.com/currency-trading/daily-currency-exchange-pattern/) (secondary summary of
  Breedon & Ranaldo 2012, "currencies tend to depreciate during their respective local trading hours", EUR/USD profitable after spread
  in 1997-2007; this is the B14/E017 line, WEAK on val and closed). Hits for (b): ML/volatility-forecasting arXiv papers and volatility
  surveys already in research/academic_studies.md (Erdemlioglu-Laurent-Neely 2012); no verified direction result.
- No item added (rule 3: no new verified basis; both families already tested or volatility-only). 0 trials used (dev 257, val 9,
  total 266). First refill without an item since R124. Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R128 (not an item; no item added)
- 2026-11-12 R128 refill pass, angle: PBoC daily CNY central-parity fixing (09:15 Beijing) or fixing surprise -> EUR/USD / USD direction.
  One standard search. Hits: newsquawk/FXStreet/Euromoney/poundsterlinglive news pages (not evidence) and McCauley & Shu (2018),
  "Recent RMB policy and currency co-movements", BIS WP 727, [landing page](https://www.bis.org/publ/work727.pdf) (this URL served the HTML landing page) opened via web-fetch
  (abstract/summary ~100%; the 27-page PDF fetch timed out, body UNVERIFIED). It studies how the fixing responds to lagged dollar moves
  and EM-currency co-movement with the RMB in three post-2015 phases; no EUR/USD or intraday USD test on the page.
- No item added (rule 3: no verified EUR/USD direction basis; a surprise test would also need USD/CNH data and fix expectations not in
  the repo). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R129 (not an item; no item added)
- 2026-11-12 R129 refill pass, angles: (a) post-announcement drift after euro-area releases / ECB monetary-policy announcements in
  EUR/USD, (b) prior-day high/low breakout predictability in EUR/USD. Two standard searches. Opened via web-fetch: Valentin (2022),
  "The Post-ECB Announcement Drift", Goethe University Frankfurt working paper (dated 12 Sep 2022),
  [PDF](https://acfr.aut.ac.nz/__data/assets/pdf_file/0004/691195/The_Post_ECB_Announcement_Drift_AV.pdf) (~28% verbatim, rest
  summary-only): Euro Stoxx keeps drifting in the direction of the press-conference-window shock for up to 20 trading days
  (verbatim: "160 (-114) basis points for positive (negative)" information shocks), 2002-2020, 190 announcements, intraday shocks from
  the Altavilla et al. (2019) EA-MPD; **equities and rates only, no FX result**. Da EOD paper (nd.edu) redirected cross-host and could
  not be opened (UNVERIFIED, not cited). Other hits (Cardiff/CEQURA/ICMAIF EUR/USD news-announcement papers, CESifo one-day abnormal
  returns) not opened; the abnormal-return-day family is already tested (E028/E029) and level-touch families too (E045, E047).
- No item added (rule 3: no verified FX drift basis; an EUR/USD transfer would need the ECB meeting calendar, unreachable in R106/R107,
  and ~48 dev meetings sit below the R090 power floor). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run
  43291084015 success, recorded as E047).

### Refill note R130 (not an item; no item added)
- 2026-11-13 R130 refill pass, angles: (a) US equity cash-open / intraday equity -> EUR/USD direction spillover, (b) intraday mechanical
  technical trading rules (moving-average / optimized rules) in FX. Two standard searches. Opened via web-fetch: Boehm & Kroner (2023),
  "The US, Economic News, and the Global Financial Cycle", Fed IFDP 1371,
  [PDF](https://www.federalreserve.gov/econres/ifdp/files/ifdp1371.pdf) (~14% verbatim, rest summary-only): high-frequency event study of
  US macro-news surprises on foreign equities/VIX/commodities; exchange-rate responses only as event-study reactions in an appendix
  (summary-only, UNVERIFIED), no forecasting rule. Neely & Weller (2003, JIMF 22(2)), "Intraday technical trading in the foreign exchange
  market", [Fed in Print abstract](https://www.fedinprint.org/item/fedlwp/10388/original) (abstract ~100% verbatim): "When realistic
  transaction costs and trading hours are taken into account, we find no evidence of excess returns to the trading rules"; full text
  (pairs, windows) not opened. Fuess-Mager-Stein-Zhao NTNU PDF redirected cross-host and could not be opened (UNVERIFIED, not cited).
  Marsh & Miao (City) hit already rejected (note ~line 603).
- No item added (rule 3: no verified directional EUR/USD basis; the one rule-based source is negative after costs). 0 trials used (dev
  257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R131 (not an item; no item added)
- 2026-11-13 R131 refill pass, angle: volatility-conditioned return autocorrelation / feedback trading (Sentana-Wadhwani, LeBaron style)
  in FX as a next-day EUR/USD direction rule. Two standard searches. Opened via web-fetch: Laopodis (2005), Economic Modelling 22(5),
  811-827, [IDEAS](https://ideas.repec.org/a/eee/ecmode/v22y2005i5p811-827.html) (bibliographic only, "No abstract is available";
  content UNVERIFIED, not used); Aguirre & Saidi (1999), J. Economics and Finance 23(1), 1-14,
  [IDEAS](https://ideas.repec.org/a/spr/jecfin/v23y1999i1p1-14.html) (abstract ~100% verbatim: "no feedback trading within blocks among
  developed financial markets' currencies"; feedback trading "takes place during rising volatility" only for less developed markets);
  Laopodis (2008), J. Economics and Finance 32(3), [Springer](https://link.springer.com/article/10.1007/s12197-007-9018-y) (abstract only;
  "both positive and negative feedback trading", currencies and regimes UNVERIFIED); Chen & Kao, EFMA 2009,
  [PDF](https://efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2009-Milan/papers/EFMA2009_0102_fullpaper.pdf) (~100% verbatim; CME
  Euro FX futures 1999-2005, weekly: no unconditional autocorrelation, AR(1) -0.405 in the lowest-10% signed-imbalance weeks). Saadi et al.
  EFMA 2007 PDF opened but is a CAD/USD day-of-week paper (not relevant).
- No item added (rule 3): the only verified FX statement for developed-market currencies is a null (Aguirre-Saidi); Chen-Kao needs signed
  trade imbalance (not in our bid/ask bars) and gives ~30 extreme dev weeks, below the R090 power floor; unconditional daily reversal and
  volume-conditioned reversal already tested (E021, E033). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run
  43291084015 success, recorded as E047).

### Refill note R132 (not an item; no item added)
- 2026-11-13 R132 refill pass, angles: (a) opening-range breakout rules in FX / EUR/USD, (b) recent (2023-2025) hour-of-day EUR/USD
  return predictability. Two standard searches. Opened via web-fetch: Holmberg, Lönnbark & Lundström (2013), "Assessing the
  profitability of intraday opening range breakout strategies", Finance Research Letters 10(1), 27-33, DOI 10.1016/j.frl.2012.09.001,
  [EconPapers](https://econpapers.repec.org/RePEc:eee:finlet:v:10:y:2013:i:1:p:27-33) (abstract page in full; ORB returns "significantly
  above zero" per abstract paraphrase; instrument not named in the abstract, keywords list crude oil futures; full text not opened, FX
  applicability UNVERIFIED). Zhang & Hua (2024), "Market Predictability Before the Closing Bell Rings", Risks 12(11) 180,
  DOI 10.3390/risks12110180, [MDPI](https://www.mdpi.com/2227-9091/12/11/180) (~12% verbatim): SPY/QQQ last-30-minute predictability
  2007-2018, intraday momentum "diminished over time"; equities only, no FX result. Other hits were the already-logged Krohn-Mueller-
  Whelan fix-window line (academic_studies.md), CXO p=21224 (B14/E017 line, R127), news/how-to pages (not evidence).
- No item added (rule 3: no verified EUR/USD directional basis; ORB evidence is non-FX and abstract-only). 0 trials used (dev 257, val 9,
  total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R133 (not an item; no item added)
- 2026-11-13 R133 refill pass, angles: (a) consecutive-return runs / streaks as a continuation or reversal signal for EUR/USD,
  (b) narrow-range / volatility-contraction (NR4/NR7) breakouts in FX. Two standard searches. Opened via web-fetch: Hashimoto, Ito,
  Ohnishi, Takayasu, Takayasu & Watanabe (2008), "Random Walk or A Run: Market Microstructure Analysis of the Foreign Exchange Rate
  Movements based on Conditional Probability", NBER WP 14160, DOI 10.3386/w14160 (published Quantitative Finance 12(6), 893-905, 2012),
  [NBER](https://www.nber.org/papers/w14160) (abstract page verbatim): EBS tick-by-tick USD/JPY and EUR/USD; a run in *deal* prices
  "does have some predictable information on the direction of the next price movement", but "quote prices do not show such tendency of a
  run"; horizon is "the past several ticks"; no net-of-cost result; sample period not stated. Cespa, Gargano, Riddiough & Sarno (2021),
  "Foreign Exchange Volume", WP-EMG-01-2021 (RFS forthcoming),
  [PDF](https://www.bayes.citystgeorges.ac.uk/__data/assets/pdf_file/0006/660435/WP-EMG-01-2021.pdf) (~22% verbatim): volume predicts
  next-day reversal ("stronger currency return reversal for currency pairs with abnormally low volume today"), CLS hourly volume; the
  volume-conditioned reversal family is already tested (B28/B29, E033 NONE/NONE). Search (b) returned only trading-education pages
  (LuxAlgo, FXStreet, TradingView, Chartmill; not evidence, not opened) and Erdemlioglu-Laurent-Neely 2012 (already in
  research/academic_studies.md, volatility only).
- No item added (rule 3): the runs evidence is tick-level on EBS deal prices and explicitly absent in quote prices, while the repo holds
  1-minute bid/ask quote bars, so the mechanism is below our tradable horizon and not observable in our data; NR breakout evidence is
  non-academic. 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R134 (not an item; no item added)
- 2026-11-13 R134 refill pass, angles: (a) lagged euro-area sovereign-spread (BTP-Bund) changes -> next-day EUR/USD, (b) recent
  EUR/USD intraday return-predictability / technical-pattern studies net of costs, (c) lagged Bitcoin returns -> USD (search only).
  Three standard searches. Search (a) returned only bank/broker commentary (ING Think, FXStreet, Equals, VT Markets; not evidence, not
  opened). Search (c) returned crypto-network and Granger papers on crypto prices, none on EUR/USD direction (not opened; Bitcoin is
  thin for early dev). Search for 52-week-high anchoring returned only sources already logged (Raza 2015 Massey thesis, Phylaktis &
  Yamani WP-EMG-03-2022; academic_studies.md ~line 554). Opened via web-fetch: Pombo (2022), "Technical Analysis for Profitable Trading",
  MSc dissertation, Universidade Católica Portuguesa,
  [repository](https://repositorio.ucp.pt/server/api/core/bitstreams/7af09180-483d-4568-a5cb-df0ff4aeab3a/content) (~34% verbatim):
  Dukascopy minute bars, EUR/USD, USD/JPY, GBP/CHF 2003-2022, candlestick-pattern logistic regression; "substantial minute holding period
  return predictability ... during some periods in the first decade of the 21st century" but "The confidence, predictability and
  profitability capacity of the models appears to be declining and may no longer exist" (verbatim). Sokolovski (2011), "Analysis of the
  predictive ability and profitability of an analytically derived trading algorithm in the intra-day spot foreign exchange market",
  MSc thesis, University of Cape Town, [repository](https://open.uct.ac.za/bitstreams/1ca4b008-7ebc-4b87-8804-c8674358c228/download)
  (~14% verbatim): hourly reservation-price contrarian rule, "does not capture any incremental information above what is accounted for
  by the seasonal GARCH(1,1)-MA(1) model" and "cannot generate positive profits in the presence of realistic transaction costs"
  (verbatim). Per-pair numbers in both seen only as tool summaries (UNVERIFIED, not used).
- No item added (rule 3): no verified directional EUR/USD basis; both opened studies are minute/hourly pattern rules whose own text
  reports the edge declining before our dev block (Pombo) or absent after costs (Sokolovski); sovereign-spread evidence is commentary
  only. 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R135 (not an item; no item added)
- 2026-11-13 R135 refill pass, angle: month-of-year / Halloween ("Sell in May") seasonality in EUR/USD daily returns (partitions all dev
  dates, so it would clear the R090 power floor like B54). Two standard searches. Opened via web-fetch: Cellini & Cuccia (2014),
  "Seasonal processes in the Euro--US Dollar daily exchange rate", Applied Financial Economics 24(3), 161-174, DOI
  10.1080/09603107.2013.870651, [EconPapers](https://econpapers.repec.org/RePEc:taf:apfiec:v:24:y:2014:i:3:p:161-174) (abstract only;
  full text subscriber-only): EUR/USD daily 1999-2012, "we find statistical significance of some month effects in the first-differences
  of exchange rate" (verbatim) but the abstract names no month, sign or size. Degenhardt & Auer (2018), "The 'Sell in May' effect: A
  review and new empirical evidence", NAJEF 43, 169-205, DOI 10.1016/j.najef.2017.09.003,
  [IDEAS](https://ideas.repec.org/a/eee/ecofin/v43y2018icp169-205.html) (abstract): stocks and commodity futures only, no FX. CXO
  Advisory page "U.S. Dollar Seasonal Strength/Weakness and Stock Market Returns" (2022, not evidence; paywalled, descriptive). EconBiz
  record blocked by bot protection (not opened).
- No item added (rule 3): no verified month, sign or size for EUR/USD, so any month or winter/summer direction would have to be chosen
  from data (a dev scan = many trials, and E009 already scanned calendar cells), not from a published prior. 0 trials used (dev 257,
  val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R136 (not an item; no item added)
- 2026-11-13 R136 refill pass, angles: (a) FX option-expiry pinning at the 10:00 NY cut, (b) pre-/post-holiday effects in EUR/USD.
  Two standard searches. Search (a) returned only daily expiry listings (Newsquawk, investingLive, VT Markets; not evidence, not opened):
  no study found, and no historical strike/notional expiry data the runner can download, so not testable. Search (b) opened via
  web-fetch: Adelman (2017), "Business Hours and the Foreign Exchange Market", MA thesis, University of Georgia,
  [repository](https://openscholar.uga.edu/record/20713/files/adelman_jonathan_p_201705_ma.pdf) (partly verbatim): BFIX G10 mids
  2010-2016, "the US dollar on average appreciated during US business hours" (verbatim); holidays only cited via Ranaldo, who "finds
  weak evidence that holidays have much of an effect" (verbatim); no pre-/post-holiday test. Ranaldo (2007/EFMA 2008)
  [paper](https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2008-Athens/papers/376.pdf) reopened: same-day holiday
  natural experiment only, already logged (refill notes ~line 716 and ~line 883; academic_studies.md ~line 466; below R090 power floor).
- No item added (rule 3): option-expiry pinning has no verified evidence or data; Adelman's business-hours effect is the
  Ranaldo time-of-day family already covered (E009 hour cells, E024/E025, E032), and no verified pre-/post-holiday EUR/USD direction
  exists. 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R137 (not an item; no item added)
- 2026-11-13 R137 refill pass, angle: CME FX futures expiry / IMM-date and contract-roll effects on spot EUR/USD direction (untried in
  the backlog; ~24 quarterly or ~72 monthly expiries on dev). Two standard searches; opened via web-fetch (entries in
  research/academic_studies.md): de Palacio (2016), "Is there a maturity effect on the eur/usd foreign exchange market?", Banque &
  Stratégie 348, [page](https://www.revue-banque.fr/archive/there-maturity-effect-eurusd-foreign-exchange-m-NQRB00807) and full-text
  PDF (read in full): daily EUR/USD 2003-2014, GARCH volatility vs days since last CME expiry; 4-/5-day volatility rises nearer expiry,
  described as "an upward or downward trend" (verbatim), no return sign tested; "These results are not definitive" (verbatim).
  Han, Kling & Sell (1999, JFM 19(6) 665-693, [IDEAS](https://ideas.repec.org/a/wly/jfutmk/v19y1999i6p665-693.html), abstract only):
  currency-futures volatility, days-to-expiry as a control, no direction. Joensuu (2010, Aalto MSc,
  [record](https://epub.lib.aalto.fi/en/ethesis/id/12297), abstract only): directional expiry-day effect in EURO STOXX 50, not FX.
- No item added (rule 3): no verified directional basis for spot EUR/USD around expiry; the only FX source is volatility-only and
  sign-neutral, and ~24-72 dev events put a signed test below the R090 power floor unless the effect is large. 0 trials used (dev 257,
  val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R138 (not an item; no item added)
- 2026-11-13 R138 refill pass, angles: (a) quarter-end USD funding demand -> spot EUR/USD (re-checked: already closed in refill note
  ~line 1082 and academic_studies.md ~line 577, swaps/basis only, ~24 dev quarter-ends), (b) lagged daily change in the US-German 2-year
  yield differential -> next-day EUR/USD, (c) post-announcement EUR/USD drift after BoE / SNB / ECB policy decisions. Three standard
  searches. Search (b) returned only charting and news pages (TradingView, FXStreet, BabyPips; not evidence, not opened). Search (c)
  opened via web-fetch (entries in research/academic_studies.md): Volta & Aste (2022), Royal Society Open Science 9(3),
  [EconPapers](https://econpapers.repec.org/paper/ehllserod/114947.htm) (abstract only): Euro Stoxx 50 / FTSE 100 information flow
  around ECB/BoE decisions, no FX. Vanhanen (2024), Helsinki GSE DP 25,
  [PDF](https://www.helsinkigse.fi/media/pages/discussion-papers/discussion-paper-25/be9c359dc4-1731573877/dp25re.pdf) (full text):
  same-window ECB event study (SEK/DKK); EUR/USD only as a validation regression, "The target surprise on euro US dollar rate does not
  demonstrate statistical significance" (verbatim); no post-window horizon.
- No item added (rule 3): no verified lagged/post-announcement EUR/USD direction; (c) also needs BoE/SNB/ECB decision calendars, and
  the ECB calendar was unreachable from the runner (R129); ~48 ECB meetings on dev is below the R090 power floor. 0 trials used (dev 257,
  val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R139 (not an item; no item added)
- 2026-11-13 R139 refill pass, angles: (a) lunar-cycle effects on currency returns, (b) economic-surprise indices / macro news predicting
  next-day or later EUR/USD returns. Two standard searches. (a) returned trading-forum/blog pages (MQL5, EarnForex April-fool post; not
  evidence, not opened) and Herbst (2007, J Bioeconomics, abstract only, DJIA only, null). (b) opened via web-fetch (entries in
  research/academic_studies.md): DNB WP 850 (Worms 2025; same-window EUR/USD reaction only, Bloomberg surprises) and Norges Bank Staff
  Memo 5/2026 (repricing "within the first few minutes", no drift test). Bank/broker commentary hits (BCA, Macrosynergy) not evidence.
- No item added (rule 3: no verified directional basis; surprise data proprietary and B6 calendar block still stands). 0 trials used
  (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R140 (not an item; no item added)
- 2026-11-13 R140 refill pass, angles: (a) intraday cross-pair lead-lag (GBP/USD, USD/JPY, USD/CHF lagged returns -> later EUR/USD
  returns, lag >= 1 minute), (b) Bollinger-band mean reversion on intraday EUR/USD. Two standard searches. (b) returned only vendor,
  forum and tutorial pages (cTrader, ProRealCode, NautilusTrader; not evidence, not opened). (a) opened via web-fetch (entries in
  research/academic_studies.md): Danielsson-Luo-Payne 2012 EJF (abstract + WP ~69% verbatim; contemporaneous order flow, EUR/USD ->
  GBP direction), Cai-Zhang (Durham repository; own-pair tick-quote prediction), Maier-Paape-Platen 2015 arXiv (full text; extrema
  timing on hourly candles, GBP-USD / CHF-USD extrema ~20-30 min before EUR-USD, authors call it only "a tendency").
- No item added (rule 3: no verified lagged-return basis; the only lead claim is a non-peer-reviewed extrema-timing preprint whose
  resolution (+-30 min) is coarser than the claimed lead; minute-horizon FX lead-lag already judged below the tradable horizon, note
  ~line 655; GBP/USD/CHF data not yet downloaded). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run
  43291084015 success, recorded as E047).

### Refill note R141 (not an item; no item added)
- 2026-11-13 R141 refill pass, angles: (a) weekly Fed H.4.1 balance-sheet release (Thursday 16:30 ET) as a USD direction event,
  (b) euro-area flash HICP release -> later EUR/USD drift. Two standard searches. (a) returned only the H.4.1 data release itself
  (federalreserve.gov PDF, FRED/ALFRED series pages) and a MarketNews data headline: data, not evidence of an FX effect; not opened.
  (b) returned only FXStreet/Newsquawk news previews and headlines (not evidence, not opened).
- No item added (rule 3: no verified published basis for either angle; (b) also needs a euro-area release calendar, which earlier
  runs could not source). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success,
  recorded as E047).

### Refill note R142 (not an item; no item added)
- 2026-11-13 R142 refill pass, angles: (a) daily candlestick patterns (engulfing / inside day) on EUR/USD, (b) Fibonacci retracement
  levels in FX. Two standard searches; opened via web-fetch (entries in research/academic_studies.md): Alanazi (2020, EJF 26(15),
  [IDEAS](https://ideas.repec.org/a/taf/eurjfi/v26y2020i15p1484-1505.html), abstract only): engulfing patterns "profitable" for "the
  seven majors", 24 pairs 2000-2018; pattern definition, horizon, cost treatment and EUR/USD result not in the abstract (UNVERIFIED).
  Neely & Weller (2011, St. Louis Fed WP 2011-001, [PDF](https://fraser.stlouisfed.org/docs/publications/frbsl_wp/2011-001.pdf),
  ~42% verbatim): survey, rule profits extinguished after the 1980s. Gupta (2011, Macalester honors project,
  [PDF](https://core.ac.uk/download/46721086.pdf), ~59% verbatim): Fibonacci bounce frequencies, no trading test, EUR/USD values
  unreadable. CXO page on Breedon-Ranaldo (closed B14/E017 line). Two hits not openable (BUiD thesis, CAS catalogue: bot-protection
  access denied; not circumvented).
- No item added (rule 3: the only directional source is abstract-only with an unverified pattern definition and horizon, same
  standard as R120 Tornell-Yuan; minute-horizon candlesticks already judged in R134). Possible future item if the human can supply
  the Alanazi 2020 full text (definition + horizon) -> daily engulfing continuation on dev, 1 trial. 0 trials used (dev 257, val 9,
  total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).


### Refill note R143 (not an item; no item added)
- 2026-11-13 R143 refill pass, angles: (a) daily channel (Donchian / N-day high-low) breakout rules on EUR/USD (no "Donchian" or
  channel-breakout entry in research/ before this run), (b) Friday-afternoon / end-of-week position squaring in FX. Two standard
  searches; opened via web-fetch (entries in research/academic_studies.md): Coakley, Marzano & Nankervis (2016, IRFA,
  DOI 10.1016/j.irfa.2016.03.010, [PDF](https://core.ac.uk/download/74373954.pdf), ~73% verbatim): channel breakout is the weakest rule
  family, "Virtually no traditional rule is significant in the 2006-2015 sub-sample", no costs, no data-snooping-robust EUR rule;
  CXO Advisory summaries of Hsu-Taylor (2013) and Hsu-Taylor-Wang (2016) (papers themselves UNVERIFIED): developed-pair predictability
  gone since the early 1990s, no EUR/USD or channel-specific result. (b) returned only already-logged sources (Krohn-Mueller-Whelan,
  Breedon-Ranaldo SNB WP 2011-04 / time-of-day family) and no end-of-week study; nothing new opened.
- No item added (rule 3 / R090 standard: no published directional basis for a specific channel rule on EUR/USD; the only full-text
  evidence says such rules stopped working after 2006, which overlaps our whole dev block). 0 trials used (dev 257, val 9,
  total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R144 (not an item; no item added)
- 2026-11-13 R144 refill pass, angles: (a) safe-haven channel: does a US equity fall (or vol rise) PREDICT later EUR/USD appreciation
  (lagged, not contemporaneous)? (Ranaldo-Söderlind not in research/ before this run); (b) intraday equity -> EUR/USD lead-lag.
  Two standard searches; opened via web-fetch (entries in research/academic_studies.md): Ranaldo & Söderlind (2007, SNB WP 2007-17)
  abstract only (euro appreciates vs USD "when" S&P falls, "from a few hours to several days"; lag structure UNVERIFIED; PDF fetch
  blocked by a permission prompt, not circumvented); Marsh & Miao (2012, EJF, ~35% verbatim): FX order flow -> later equity returns,
  equity -> EUR/USD not tested, in-sample, 25 days. Hits not opened: Fuess et al. NTNU (not openable in R118), CXO, vlex, others.
- No item added (rule 3 / R090 standard: no verified lagged equity -> EUR/USD direction; the only directional source is an abstract
  whose "when" reads as contemporaneous co-movement). Possible future item if the human can supply the Ranaldo-Söderlind PDF and it
  shows a lagged S&P -> EUR/USD coefficient: US500 15:00-16:00 NY return sign -> EUR/USD next hours, dev, 1 trial (US500 CFD already
  downloadable, E034). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as
  E047).

### Refill note R145 (not an item; no item added)
- 2026-11-13 R145 refill pass, angles: (a) euro-area flash PMI release (09:00-10:00 CET) -> later EUR/USD drift; (b) 17:00 NY rollover /
  end-of-day dealer-inventory effects on EUR/USD. Two standard searches. (a) returned only news/preview pages (Newsquawk, FXStreet,
  BabyPips; not evidence, not opened) and no study; release dates would also need a calendar source not reachable from the runner.
  (b) returned FXCM help pages (not evidence), the already-tested Krohn-Mueller-Whelan fixings paper (BoC SWP 2021-48; E022-E025,
  E032) and NY Fed SR 917, Boyarchenko-Larsen-Whelan "The Overnight Drift" (opened; entry in research/academic_studies.md):
  ES-futures-only overnight drift at the European open from US-close order imbalance; no FX result.
- No item added (rule 3 / R090 standard: no verified EUR/USD directional basis; European-open hour cells already covered by E009).
  0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R146 (not an item; no item added)
- 2026-11-13 R146 refill pass, angles (no "Google", "attention" or "risk reversal" entry in research/ before this run): (a) Google
  search volume / investor attention -> later EUR/USD direction, (b) FX option risk reversals (25-delta skew) -> later EUR/USD
  direction. Two standard searches; opened via web-fetch (entries in research/academic_studies.md): Goddard-Kita-Wang (Cardiff PDF,
  ~51% verbatim): attention predicts FX *volatility*, weekly 2004-2011 incl. EUR/USD, no direction result; Han-Xu-Yin 2018 (Econ.
  Modelling, abstract only): lagged attention affects currency returns at first lag, nonlinear, horizon/EUR/sign UNVERIFIED;
  Han-Wu-Yin 2018 (Applied Economics, abstract only): predictability "do[es] not exist in the currencies from developed markets".
  BUAA mirror not opened (redirect, permission prompt; not circumvented). (b) returned only practitioner/news pages and a CME
  education report (not evidence, not opened); risk-reversal history also needs a vendor feed the runner cannot download.
- No item added (rule 3 / R090 standard: the only directional sources are abstract-level and the one explicit developed-market
  statement is negative; (b) no verified basis and no data). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure
  (last run 43291084015 success, recorded as E047).

### Refill note R147 (not an item; no item added)
- 2026-11-13 R147 refill pass, angles (no "tax date" or "mid-quarter" entry in research/ before this run): (a) US corporate tax
  payment dates (15th of Mar/Jun/Sep/Dec) / TGA reserve drains -> USD funding -> EUR/USD spot direction; (b) Asian-session range
  breakout at the London open. Two standard searches. (a) opened via web-fetch (entries in research/academic_studies.md):
  Kubitza-Sigaux-Vandeweyer ECB WP 3017 (~26% verbatim; CIP basis and hedging flows, no spot direction) and Abbassi-Bräuning Boston
  Fed WP 18-6 (~29% verbatim; quarter-end forward premia, no spot); other hits news/seasonality vendor pages (not evidence, not
  opened). (b) returned only trading-education/vendor backtest pages (not evidence, not opened); the Asian-range breakout family is
  already tested and rejected (E004 S001 REJECT).
- No item added (rule 3 / R090 standard: no verified spot EUR/USD directional basis; (b) family already rejected). 0 trials used
  (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R148 (not an item; no item added)
- 2026-11-13 R148 refill pass, angles (no "CPI" or "US-only holiday" entry in research/backlog.md before this run): (a) delayed drift in
  EUR/USD hours/days after US CPI releases; (b) EUR/USD direction on US-only holidays (US closed, Europe open). Two standard searches
  plus one follow-up. (a) Bank of Canada SAN 2025-10 opened via web-fetch (~95% of text; entry in research/academic_studies.md):
  same-window CAD/USD reaction only, explicitly no drift test; Fed IFDP 823 web-archive link returned only the viewer shell (0% read,
  nothing recorded from it); other hits (CEPR DP18119, Cardiff A2006/05, Norges Bank memo 5/2026) already in the library. (b) returned
  only broker/news seasonality pages (forex.com/StoneX Thanksgiving, JFD, FXStreet; not evidence, not opened) and sources already
  logged (Adelman 2017, EFMA 2008 paper 376 holiday section, KMW fixings).
- No item added (rule 3 / R090 standard: no verified EUR/USD drift or holiday direction basis; US-only holidays give ~8-9 dev events
  per year, below the R090 power floor). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015
  success, recorded as E047).

### Refill note R149 (not an item; no item added)
- 2026-11-13 R149 refill pass, angles (no "dividend repatriation", "fiscal year" or "repatriat" entry in research/ before this run):
  (a) cross-border dividend payment flows -> EUR/USD direction; (b) Japanese fiscal-year-end (March) repatriation -> EUR/USD.
  Two standard searches. (a) Zheng 2023 UChicago JMP opened via web-fetch, both versions (~27-30% verbatim; entry in
  research/academic_studies.md): paying currency depreciates vs USD after large dividend payment dates, ~4.70 bp at t+2 and
  6.48 bp at t+8, G10 pooled incl. EUR; other hits news/vendor pages (not evidence, not opened). (b) returned only news/broker
  pages on USD/JPY seasonality (FXStreet/Nomura, forexlive, MUFG via poundsterlinglive; not evidence, not opened).
- No item added. (a) has a verified direction but no runner-downloadable dividend payment calendar (Compustat is commercial; a
  calendar-month proxy would be a month scan, refill note R135), and the pooled size (~0.5 pip on EUR/USD over 2 days) is below
  the 1-pip bar and about the SPEC 4 round-trip cost; would need a human-supplied euro-area dividend calendar (a candidate for the
  R105 human-decision data list; not acted on). (b) no verified basis and USD/JPY-focused. 0 trials used (dev 257, val 9, total
  266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R150 (not an item; no item added)
- 2026-11-13 R150 refill pass, angles (no "Beige", "jobless" or "claims" entry in research/ or knowledge/ before this run):
  (a) weekly US initial jobless claims (Thu 08:30 NY, fixed schedule, no calendar download needed) -> later EUR/USD drift;
  (b) Fed Beige Book release (Wed 14:00 NY) -> EUR/USD direction. Two standard searches. (a) returned only news/broker/blog
  pages (MQL5 blog, Dukascopy news, FXStreet, XTB, ActionForex; not evidence, not opened). (b) Zavodny-Ginther 2005 SEJ opened
  via web-fetch (~78% verbatim; entry in research/academic_studies.md): same-day US yields rise with a hand-scored Beige Book
  index, equities n.s., no FX and no drift; other hits news/calendar pages (not evidence, not opened).
- No item added (rule 3 / R090 standard: no verified EUR/USD directional or drift basis for either angle; (b) also needs a
  hand-scored text index and gives ~8 events per year, below the R090 power floor). 0 trials used (dev 257, val 9, total 266).
  Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R151 (not an item; no item added)
- 2026-11-13 R151 refill pass, angles (no "Nikkei", "Japan equit" or "Corwin" entry in research/ or knowledge/ before this run):
  (a) Asian (Tokyo) equity overnight return -> European-session EUR/USD direction; (b) bid-ask spread widening / liquidity
  shocks -> later EUR/USD direction. Two standard searches. (a) returned only sources already in research/academic_studies.md
  (KMW fixings, Bank of Canada SWP 2021-48, AEA 2019/2020 papers) and news/broker pages (City Index, forex.com, FXStreet,
  ActionForex; not evidence, not opened). (b) opened via web-fetch (entries in research/academic_studies.md): Evans 2020 MPRA
  102702 (~38% verbatim; monthly cross-sectional liquidity sorts on 17 pairs, EUR/USD contemporaneous only), Osler-Mende-Menkhoff
  2010 (~38% verbatim; trade-level dealer data), BIS WP 1229 (abstract only; PDF blocked); GFJ DOI 10.1016/j.gfj.2006.06.004 not
  openable (proxy block, not circumvented, nothing recorded from it).
- No item added (rule 3 / R090 standard: no verified EUR/USD time-series direction basis for either angle). 0 trials used (dev 257,
  val 9, total 266). Not a pipeline failure (last run 43291084015 success, recorded as E047).

### Refill note R152 (not an item; no item added)
- 2026-11-13 R152 refill pass, angles (no "ZEW" entry and no euro-area sovereign-auction FX entry in research/ or knowledge/ before
  this run): (a) German ZEW / Ifo sentiment releases -> post-release EUR/USD drift; (b) euro-area sovereign bond auction days ->
  EUR/USD direction. Two standard searches. (a) returned two academic PDFs, neither readable: CEQURA (LMU) WP 8 (redirect to
  cequra.uni-muenchen.de; fetch permission timed out, not retried) and Mannheim madoc dp09010 (bot-challenge page, not
  circumvented); the rest were news/broker pages (FXStreet, babypips, aggregator feeds; not evidence, not opened). Nothing is
  recorded from the two unread PDFs. (b) Beetsma-Giuliodori-Hanson-de Jong, JMCB 50(7) 1401-1440, DOI 10.1111/jmcb.12510
  (IDEAS and UvA DARE pages opened, abstract/metadata only): auction cycles in euro-area sovereign yields; no exchange-rate content
  in the abstract.
- No item added (rule 3 / R090 standard: no verified EUR/USD direction or drift basis; (a) would also need an official ZEW/Ifo
  release calendar, same blocker as B6). 0 trials used (dev 257, val 9, total 266). Not a pipeline failure (last run 43291084015
  success, recorded as E047).

### B58: 1-hour swing-level breakout, 5-minute break-and-retest entry (signal test, dev) → E048 · `done` (2026-11-14 R155: NONE, n 372, -0.744 pips, CI (-2.614, 1.137), t p 0.7897. R154: pre-registered as E048, rule unchanged, "24 bars" = 24 clock hours with >= 20 valid, queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-13 R153, human-directed pivot; ranked first, reason in agent_decision_log R153)
- **Origin [HUMAN / PRACTITIONER]:** the human asked (2026-11-13) to test "the one hour breakout strategy with a set resistance ... start
  there and then drop down to lower time frame for the trade", and left the level, entry and exit definitions to the agent. No
  published EUR/USD evidence is claimed; prior is low (technical-rule profits in developed FX largely gone: Neely-Weller 2011,
  Coakley-Marzano-Nankervis 2016, both in research/academic_studies.md; Asian-range breakout rejected E004). Run because the human
  asked, not because of a literature basis.
- **Level (fixed now):** 1-hour bars = UTC clock hours built from 1-minute mid (mid = (bid+ask)/2), bar valid with >= 50/60 minutes.
  At the close of 1h bar k: R = max mid high and S = min mid low over the previous 24 valid 1h bars k-24..k-1 (needs >= 20 valid).
- **Breakout (fixed now):** 1h bar k closes above R -> long setup at level L = R; closes below S -> short setup at L = S. Only
  breakout bars whose close falls in [07:00 Europe/London, 12:00 America/New_York) (London open to US midday, liquid hours).
- **Lower-timeframe entry = break-and-retest (fixed now):** 5-minute bars (UTC-aligned) in the 120 minutes after bar k closes. Long:
  the first 5m bar with low <= L + 1.0 pip AND close > L is the retest; signal at its close, entry = open of the first 1m bar at or
  after close + 1 min (SPEC 4 fill rule). If a 5m bar closes <= L before a valid retest, the setup is cancelled (failed break,
  counted). Shorts mirror. No retest within 120 min -> no trade (counted). At most one long and one short setup per trading date
  (the first of each); no overlapping trades.
- **Exit for this signal test (fixed now):** fixed 60-minute hold (exit = open of first bar at or after entry + 60 min); a stop/target
  version is a later strategy test only if this earns it. Exclusions, counted under the first failing check: window coverage
  < 55/60 bars; entry or exit NY time in [16:30, 18:30); entry spread > 2.0 pips; overlap.
- **Decision rule (= E045/E047 rule):** < 300 trades -> NONE. SIGNAL if mean signed mid return > 1.0 pip AND date-cluster bootstrap
  95% CI lower > 0 (resample trading dates with all their trades, 2000 draws, seed 0) AND one-sided t p < 0.05 (1 trial). WEAK if
  mean > 0 and (CI lower > 0 or p < 0.05); else NONE. A SIGNAL earns B58v.
- **Descriptive (not in rule):** long/short legs; 30- and 120-min holds; "enter on the breakout 1h close" (no retest) variant;
  failed-break and no-retest counts; by year; SPEC 4 net and costs x1.5; share within +-15 min of 08:30/10:00 NY and 16:00 London.
- **Data:** EUR/USD 1-minute bid/ask in repo. No download.

### B58v: B58 val confirmation (signal test, val only) · `done` (2026-11-14 R155: closed unearned, 0 trials; B58 NONE on dev (E048). Was: earned only if B58 returns SIGNAL on dev)
- B58 unchanged on val (2021-01-21 .. 2023-06-30), own pre-registration, 1 val trial, < 120 trades -> NONE, p < 0.05.

### B59: Multi-timeframe trend alignment (1h + 30m + 15m agree), 5-minute trigger (signal test, dev) → E049 · `done` (2026-11-14 R157: NONE, n 5317, +0.216 pips, CI (-0.156, 0.599), t p 0.1469. R156: pre-registered as E049, rule unchanged; details fixed before data: bar exists with >= 1 minute, EMA ewm(span 20, adjust=False, min_periods 20), state from the bucket ending at floor(T, m), previous 5m bucket must be contiguous, no per-day cap; queued on research-batch; 1 dev trial counted when it runs. Added 2026-11-13 R153, human-directed; runs after B58)
- **Origin [HUMAN / PRACTITIONER]:** the human described establishing bull/bear on 1h, 30m and 15m and trading the 5m/10m in the same
  direction when all agree; definitions left to the agent. Same low prior as B58. Separate strategy from B58 (could later be a
  filter on it, as its own experiment).
- **Trend state (fixed now):** for each of 1h, 30m, 15m (UTC-aligned bars from 1-minute mid), EMA20 of bar closes (span 20,
  adjust=False, seeded after 20 bars). A timeframe is bull if its last **completed** bar closed above its EMA20, bear if below. State
  = BULL if all three bull, BEAR if all three bear, else NONE. Only completed bars are used at any time (no look-ahead test required).
- **Trigger (fixed now):** 5-minute bar whose close crosses its own EMA20 in the state's direction (prev close <= EMA, this close >
  EMA for BULL; mirror for BEAR) while the state is BULL/BEAR at that bar's close -> signal; entry = open of first 1m bar at or after
  close + 1 min. Signals only with 5m close in [07:00 Europe/London, 12:00 America/New_York). No overlapping trades (signals during
  an open trade are skipped and counted).
- **Exit and exclusions:** fixed 60-minute hold; same exclusions as B58.
- **Decision rule:** identical to B58 (< 300 trades NONE; > 1.0 pip, date-cluster CI lower > 0, t p < 0.05; 1 trial). SIGNAL earns B59v.
- **Descriptive (not in rule):** control = same 5m EMA20 cross with no alignment filter (does alignment add anything?); 10-minute
  trigger variant; long/short legs; 30/120-min holds; by year; SPEC 4 net and costs x1.5.
- **Data:** EUR/USD 1-minute bid/ask in repo. No download.

### B59v: B59 val confirmation (signal test, val only) · `done` (2026-11-14 R157: closed unearned, 0 trials; B59 NONE on dev (E049). Was: earned only if B59 returns SIGNAL on dev)
- B59 unchanged on val, own pre-registration, 1 val trial, < 120 trades -> NONE, p < 0.05.

### Refill note R158 (not an item; no item added)
- 2026-11-14 R158 refill pass after E049 (B59 NONE). Angles: (a) retail FX positioning as a contrarian EUR/USD signal; (b) daylight-
  saving-time transitions; (c) predictable cross-border payment flows (coupons/redemptions/rebalancing) around payment dates.
  (a) search returned DailyFX/TradingView commentary (not evidence, not opened) and one academic record (UCLan clok 55052, "News and
  intraday retail investor order flow in foreign exchange markets"): redirect to knowledge.lancashire.ac.uk not answered in time, not
  retried; nothing recorded from it. Retail-positioning history is also not in the repo. (b) Nower (2024) opened again; it was
  already in the library and closed by refill note R114 (R090 power floor) - no change. (c) Three hits opened: Zou (2025) WP
  (Bund/G10 10y auction bid-to-cover -> domestic currency appreciation; entry in research/academic_studies.md) and two versions of
  Jansen-Shin-von Peter (2024; quarterly euro-investor EME bond holdings, no event study, not recorded as a source). No payment-date study.
- Not added: a Bund-auction bid-to-cover item needs an auction-results history (no verified downloadable source) and is below the
  R090 power floor (~4-5 pip daily effect, ~70 dev events, UNVERIFIED count); R152 already found no FX basis for plain auction days.
- No item added (rule 3 / R090). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure (last run
  43541310326 success, recorded as E049).

### Refill note R159 (not an item; no item added)
- 2026-11-14 R159 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles: (a) realized skewness /
  higher realized moments as a next-day or next-week EUR/USD direction predictor; (b) US Treasury quarterly refunding announcements ->
  EUR/USD. (a) Opened: Gkillas-Gupta-Pierdzioch (2019, Physica A 532, 121867, doi:10.1016/j.physa.2019.121867; UP repository record
  https://repository.up.ac.za/handle/2263/70757, abstract only): EUR/USD among six USD pairs, but the target is one-day-ahead realized
  **volatility**, not returns ("mainly realized kurtosis" helps out of sample). Sim (2016, JDQS 24(1), 119-152,
  doi:10.1108/JDQS-01-2016-B0005, abstract only): negative realized skewness -> next-week return relation for **US stocks**, no FX.
  Cespa-Gargano-Riddiough-Sarno (2021, EMG WP-EMG-01-2021) re-opened: volume-conditioned reversal, family already tested (E033).
  No verified FX direction result for realized skewness. (b) Search returned only news/commentary pages (Newsquawk, FXStreet,
  MarketPulse, Marc to Market; not evidence, not opened); ~4 refunding events per year is also far below the R090 power floor.
- No item added (rule 3 / R090). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R160 (not an item; no item added)
- 2026-11-14 R160 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles: (a) lagged copper /
  industrial-metal returns -> later EUR/USD; (b) Bund futures / euro bond prices leading EUR/USD spot (intraday lead-lag). Two
  standard searches. (a) returned news/vendor pages (FXStreet, FXEmpire, convextrade; not evidence, not opened) and commodity-currency
  papers on exchange rates forecasting commodity prices (Chen-Rogoff-Rossi family, opposite direction, commodity currencies only; not
  opened again). (b) Opened: Hossfeld-Röthig (2015, Bundesbank DP 41/2015,
  [PDF](https://bundesbank.de/resource/blob/703976/fcd518354ae96703103d929dfea7582e/472B63F073F071307366337C94F8C870/2015-11-30-dkp-41-data.pdf);
  weekly CFTC speculator positions vs USD/EUR, positions do not lead FX after multiple-test correction - "the evidence does not support a
  leading indicator role in the other direction"; no bonds) and Kenourgios-Tsioutsios (ICBE-HOU 2026 abstract only,
  [page](https://icbe-hou.eap.gr/2026/presentations/?abs_id=254); spot/futures currency lead-lag unstable over time, no sign, horizon or
  bond series). No verified Bund -> EUR/USD or copper -> EUR/USD direction result; Bund futures data also not in the repo.
- No item added (rule 3 / R090). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R161 (not an item; no item added)
- 2026-11-14 R161 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "speech", "Lagarde" or
  "implied vol" entry in research/ before this run): (a) ECB exchange-rate communication / speeches -> EUR/USD direction; (b) option-
  implied volatility / risk reversals -> later EUR/USD returns. Two standard searches. (a) Opened the VoxEU column on Comazzi et al.
  (2026, CEPR DP 21606): little evidence that ECB FX statements move the euro in the intended direction, effects fade within days;
  ~100 opening-statement events 2002-2023 and no published event list. (b) Opened Babiak-Baruník (arXiv:2101.09738): cross-sectional
  monthly sorts over 20 currencies, not a single-pair signal; implied-vol data not in repo. Entries in research/academic_studies.md.
- No item added (rule 3 / R090). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R162 (not an item; no item added)
- 2026-11-14 R162 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles: (a) session-VWAP deviation
  mean reversion (strategy S004 "Session VWAP mean reversion" has been `research_candidate` since 2026-11-07 with no evidence basis; no
  VWAP entry in research/ before this run); (b) intraday time-series momentum (first-period return -> last-period return) in FX. Two
  standard searches. (a) returned TradingView/FXStreet/NexusFi/blog pages (not evidence, not opened), arXiv:1609.04640 (minute-horizon
  lead-lag networks, family already judged below the tradable horizon, note ~line 655) and Cespa et al. 2021 (already tested, E033).
  Opened: Hashemi (2025, HEC Montréal M.Sc. thesis; entry in research/academic_studies.md): US equities only, VWAP used as an ML feature,
  no FX and no verified reversion sign. (b) returned only Elaut-Frömmel-Lampaert 2018 (RUB/USD, already in academic_studies.md and the
  backlog), Gao et al. (equities) and the Reading intraday-TSMOM manuscript (already logged, R-note ~line 1016); E027 already tested the
  London-close momentum variant. No verified FX direction basis for S004.
- No item added (rule 3). S004 stays `research_candidate` (no evidence to pre-register against). pytest 434 passed. 0 trials used
  (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R163 (not an item; no item added)
- 2026-11-14 R163 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles: (a) lagged euro-area
  sovereign-spread (BTP-Bund) changes -> later EUR/USD direction; (b) ECB monetary-policy accounts / central-bank information shocks ->
  EUR/USD post-event drift. Two standard searches. (a) returned only commentary on the contemporaneous spread/euro correlation (ING Think,
  FXStreet, Seeking Alpha, investireoggi; not evidence, not opened); no lagged FX study; spread history not in repo. (b) Opened via
  web-fetch: Franz (2020), "Central bank information shocks and exchange rates", Deutsche Bundesbank DP 13/2020,
  [PDF](https://bundesbank.de/resource/blob/828896/2d2e88314163a04e1eb8af798401a1e4/mL/2020-03-20-dkp-13-data.pdf) (~40% verbatim):
  monthly Bayesian proxy VAR, 36-month responses; EUR "appreciates strongest directly on impact following a monetary policy shock";
  for information shocks "I do not find a significant reaction of the nominal effective EUR exchange rate". No intraday/daily post-event
  drift; accounts releases not studied. Entry in research/academic_studies.md.
- Not added: monthly horizon, no verified tradable post-event EUR/USD direction; ECB-meeting events (~48 dev) below the R090 power floor
  and the post-ECB drift angle already closed by R129. No item added (rule 3 / R090). pytest 434 passed. 0 trials used (dev 259, val 9,
  total 268). Not a pipeline failure.

### Refill note R164 (not an item; no item added)
- 2026-11-14 R164 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "option expiry" or
  "geopolitical"/"GPR" entry in research/ before this run): (a) FX option-expiry pinning around the 10:00 NY cut; (b) geopolitical-risk
  index -> later EUR/USD returns. Two standard searches. (a) returned only daily expiry-notice pages (investingLive, VT Markets,
  Newsquawk; not evidence, not opened); no empirical FX pinning study; historical expiry sizes/strikes not in repo. (b) Opened the Monash
  repository record of Iyke-Phan-Narayan (2022, IRFA 81, 102099): abstract says GPR predicts 10/17 currency returns in-sample, but
  frequency, currency list, horizon and sign are not stated; GPR data not in repo. Entry in research/academic_studies.md.
- No item added (rule 3 / R090: no verified EUR/USD sign, horizon or data). pytest 434 passed. 0 trials used (dev 259, val 9,
  total 268). Not a pipeline failure.

### Refill note R165 (not an item; no item added)
- 2026-11-14 R165 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Trump"/"tweet" or
  "dollar index"/"DXY" entry in research/ before this run): (a) social-media (presidential tweet) announcements -> later EUR/USD direction;
  (b) intraday common dollar component / dollar-basket lead-lag -> later EUR/USD returns. Two standard searches. (a) Opened
  Filippou-Gozluklu-Nguyen-Viswanath-Natraj (2025 WP, ~37% verbatim): informative tweets -> USD appreciation of ~0.5 bp vs basket,
  peaking within an hour; in-sample UUP rule ~2 bp gross vs ~1.5-1.75 bp costs. (b) Returned only the KMW fixings family (already tested
  E007-E025) and cross-sectional monthly papers already logged (arXiv:2101.09738, R161); re-opened KMW BoC SWP 2021-48: post-fix reversal
  predicted by pre-fix order flow (2.5-3.5 bp, data not in repo). Entries in research/academic_studies.md.
- No item added (rule 3 / R090: effect ~0.05 pips, far below the 1-pip bar and costs; tweet series and order flow not in repo; fix family
  closed). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R166 (not an item; no item added)
- 2026-11-14 R166 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "GDELT" and only two
  "speech" mentions in research/ and knowledge/ before this run): (a) daily news tone (GDELT) -> next-day EUR/USD direction;
  (b) ECB Executive Board speeches -> post-speech EUR/USD drift. Two standard searches. (a) Opened Zhang (2025, arXiv:2505.16136v1,
  full text): fitted XGBoost on GDELT-linked headline sentiment + technicals, EUR/USD next-day Sharpe 5.87 (logistic 0.83), timestamp
  handling not explained, no CIs. (b) Opened Istrefi-Odendahl-Sestieri (2025, CEMLA, ~30% verbatim): absolute 90-min impacts only, no
  signed or delayed FX direction. Entries in research/academic_studies.md.
- No item added (rule 3 / R090: (a) no single fixed rule to pre-register, look-ahead unverified, GDELT history too large for the runner;
  (b) no verified direction basis). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R167 (not an item; no item added)
- 2026-11-14 R167 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "weather"/"sunshine" or
  "football"/"soccer"/"World Cup" entry in research/ or knowledge/ before this run): (a) financial-centre weather (mood) -> daily EUR/USD
  returns; (b) international football results -> next-day currency returns. Two standard searches. (a) Opened Andrikopoulos-Wang-Zheng
  (2019, FRL 30, accepted manuscript, full text): New York weather vs daily EUR/USD 2002-2018, only 10%-level coefficients, authors
  conclude no effect ("may have dissipated after discovery"). (b) Opened Demir-Lau-Fung (2014, JASF) abstract (Turkish lira only, win
  effect for the national team) and Samadi (2017, Erasmus thesis, ~80%: German team results vs DAX, null). Entries in
  research/academic_studies.md.
- No item added (rule 3 / R090: no verified EUR/USD effect; weather series not in repo; euro-area tournament match days far below the
  power floor). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R168 (not an item; no item added)
- 2026-11-14 R168 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "intervention" entry and
  "bitcoin"/"crypto" only in the backlog before this run): (a) Japanese MoF yen interventions -> spillover to EUR/USD direction;
  (b) bitcoin weekend returns -> Monday EUR/USD. Two standard searches. (a) Opened the RePEc record of Chortareas-Jiang-Nankervis (2013,
  Review of International Economics 21(4), 671-689, doi:10.1111/roie.12063): "No abstract is available", full text restricted; whether
  any EUR/USD return effect is reported is UNVERIFIED (title: volatility and spillovers). Intervention dates in dev are few (2011 episodes
  precede dev; no MoF yen intervention 2015-2020), so far below the R090 power floor. (b) Returned quantpedia/medium pages (not evidence,
  not opened); opened Caporale-Plastun (2019, FRL, doi:10.1016/j.frl.2018.11.012, Brunel full text): crypto-only day-of-week test
  (bitcoin Monday returns higher, 2013-2017), no fiat FX variable. Entries in research/academic_studies.md.
- No item added (rule 3 / R090: no verified EUR/USD direction basis; no dev intervention events; crypto data not in repo). pytest 434
  passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R169 (not an item; no item added)
- 2026-11-14 R169 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "rating"/"TLTRO" entry
  in the backlog before this run): (a) euro-area sovereign credit-rating announcements -> EUR/USD drift; (b) ECB TLTRO repayment /
  excess-liquidity dates -> EUR/USD. Two standard searches. (a) Opened Baum-Schäfer-Stephan (2016, JFS, doi:10.1016/j.jfs.2016.05.001;
  abstract): downgrades "had no impact on the value of the Euro currency", only on volatility (2010-2012, before dev); Yang-Zhang (2011,
  Lund master's thesis, abstract): effect on "volatility rather than the mean of USD/EUR". No verified direction effect; a ratings
  history is also not in the repo. (b) Returned only ECB Economic Bulletin boxes and an ECB MMCG money-market slide deck plus a broker
  commentary page (not opened; no FX return study); TLTRO repayment dates are ~quarterly, far below the R090 power floor.
- No item added (rule 3 / R090: null or no EUR/USD direction basis). pytest 434 passed. 0 trials used (dev 259, val 9, total 268).
  Not a pipeline failure.

### Refill note R170 (not an item; no item added)
- 2026-11-14 R170 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "index rebalancing" or
  "TGA" entry in research/ before this run): (a) equity-index rebalancing / global portfolio rebalancing flows -> EUR/USD; (b) US Treasury
  General Account (TGA) swings -> USD. Two standard searches. (a) Returned only the Camanho-Hau-Rey global-rebalancing family (already
  logged R079 and tested as B35/B36, E037) and unrelated MPRA/blog PDFs (not opened). (b) Opened the IDEAS record of Vissing-Jorgensen
  (2025, FEDS Notes, abstract): TGA and Fed balance sheet, no exchange-rate result; full note not opened (UNVERIFIED). Other results were
  NY Fed FX quarterly reports and Treasury reporting-rate tables (not studies).
- No item added (rule 3 / R090: (a) already tested; (b) no verified EUR/USD direction basis, TGA series not in repo). pytest 434 passed.
  0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R171 (not an item; no item added)
- 2026-11-14 R171 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Treasury yield" or
  "Taylor rule" entry in research/backlog.md before this run): (a) lagged US Treasury yield changes -> later EUR/USD (intraday lead);
  (b) Taylor-rule fundamentals -> EUR/USD direction. Two standard searches. (a) Returned only news/broker commentary (FXStreet, City
  Index, Forex.com; not studies, not opened); the closest tested relative is the 2-year differential angle closed in R138, and bond-yield
  intraday data are not in the repo. (b) Opened the EconPapers record of Molodtsova-Nikolsko-Rzhevskyy-Papell (2011, JMCB,
  doi:10.1111/j.1538-4616.2011.00384.x; abstract): out-of-sample predictability for USD/EUR 1999-2007 at one quarter ahead and longer
  only. Entry in research/academic_studies.md.
- No item added (rule 3 / R090: (a) no study; (b) quarterly horizon, ~24 dev quarters, below power floor, real-time macro data not in
  repo). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R172 (not an item; no item added)
- 2026-11-14 R172 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Hurst" or "Christmas"
  entry in research/ or knowledge/ before this run): (a) Hurst-exponent / long-memory regime -> EUR/USD intraday trend vs reversal;
  (b) Christmas / year-end holiday-season low liquidity -> EUR/USD drift. Two standard searches. (a) Opened Caporale-Plastun (2022, Brunel
  WP 2215, full text): EuroStoxx 50 futures only, intraday H 0.37, profitability inferred not tested; other hits were an AUD/USD arXiv
  paper, an arXiv Q-learning paper and vendor/MQL5 pages (not opened). (b) Returned only broker/news commentary (FXStreet, VT Markets,
  GO Markets; not studies, not opened); one holiday week per year gives ~3 dev events, far below the R090 power floor.
- No item added (rule 3 / R090: (a) no verified EUR/USD basis, no tested rule; (b) no study, below power floor). pytest 434 passed.
  0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R173 (not an item; no item added)
- 2026-11-14 R173 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "EIA inventory" or
  "Jackson Hole" entry in research/ or knowledge/ before this run; EIA appears only as a calendar label in E041 methodology):
  (a) EIA weekly crude-inventory release (Wed 10:30 NY) -> EUR/USD drift; (b) Jackson Hole symposium -> EUR/USD. Two standard searches.
  (a) Opened Geman-Li (2018, J. Energy Markets 11(2), doi:10.21314/JEM.2018.174; abstract only, paywalled): WTI response lasts ~25 min,
  no FX variable; and the Wen-Indriawan-Lien-Xu Energy Journal 44(5) executive summary: WTI intraday momentum on EIA days, no FX. The
  oil -> EUR/USD lag family is already tested (E041); inventory consensus/surprise data not in repo. (b) Returned only broker/news
  commentary (FXStreet, Convera, Forex.com, Euronext news; not studies, not opened); one event per year gives ~6 dev events, far below
  the R090 power floor. Entries in research/academic_studies.md.
- No item added (rule 3 / R090: no verified EUR/USD basis; (b) below power floor). pytest 434 passed. 0 trials used (dev 259, val 9,
  total 268). Not a pipeline failure.

### Refill note R174 (not an item; no item added)
- 2026-11-14 R174 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "time-series reversal"
  or "NR7"/"inside bar" test in research/ or knowledge/ before this run): (a) short-term (weekly) time-series return reversal in EUR/USD;
  (b) narrow-range (NR7 / inside-day) volatility contraction -> next-day breakout direction. Two standard searches. (a) Opened
  Caporale-Plastun-Oliinyk (Brunel WP 2005, 2020; ~65% verbatim): abnormal-day frequency explains same-month returns only (lag 0, no
  rule, no costs); and Dao-McGroarty-Urquhart (NTU repository, full text; already in research/academic_studies.md and tested as E020/B17,
  weekend-gap reversal NONE on dev): EUR/USD out-of-sample alpha 0.04 (SE 0.03), not significant. Other hits were broker/news pages
  (City Index, FXStreet) and equity papers (not opened). (b) Returned only vendor/indicator pages (LuxAlgo, TradingView, chartmill; not
  studies, not opened).
- No item added (rule 3 / R090: (a) no lagged EUR/USD direction basis beyond the already-rejected weekend-gap line; (b) no study).
  pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R175 (not an item; no item added)
- 2026-11-14 R175 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "blackout" or "coupon
  payment" entry in research/ or knowledge/ before this run): (a) FOMC communication blackout (quiet) period -> USD / EUR/USD drift;
  (b) US Treasury coupon payment dates (15th / month-end) -> foreign-holder USD selling -> EUR/USD. Two standard searches.
  (a) Opened the AEA 2017 conference copy of Karnaukh, "The Dollar Ahead of FOMC Target Rate Changes"
  (https://topcat.aeaweb.org/conference/2017/preliminary/paper/RAK7GsSa, job-market version dated 2016-11-25; ~40% verbatim): tests the
  two-day pre-FOMC window conditional on fed funds futures signals ("The week before FOMC meetings is known as the blackout period"),
  dollar index, 1994-2015; already in research/academic_studies.md and closed as the pre-FOMC family (backlog line 448; futures data not
  in repo). Other hits (Borisenko-Pozdeev, Mueller-Tahbaz-Salehi-Vedolin, RAPS 2025) already logged. (b) Returned NBER convenience-yield /
  Treasury-demand papers and market news (not event studies of coupon dates; not opened); no study.
- No item added (rule 3 / R090: (a) already covered, needs futures data; (b) no study). pytest 434 passed. 0 trials used (dev 259,
  val 9, total 268). Not a pipeline failure.

### Refill note R176 (not an item; no item added)
- 2026-11-14 R176 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Friday afternoon",
  "pre-weekend" or "Amihud"/"illiquidity" entry in research/ or knowledge/ before this run): (a) Friday / pre-weekend intraday EUR/USD
  return pattern; (b) Amihud-type illiquidity shocks -> later EUR/USD returns. Two standard searches. (a) Opened the IDEAS record of
  Popović-Đurović (2014, Applied Economics 46(32), doi:10.1080/00036846.2014.948676; abstract only): EUR/USD 2004-2014, long Friday
  00:00 -> 03:00 (time zone UNVERIFIED), no magnitude or costs. If CET, that is 18:00-21:00 NY trading-date Friday, already scanned on
  dev by E009 (Fri_ny_18/19/20 all NONE, sum ~+0.2 pips) and part of the post-roll 18:00 NY family (B9/B10, E012). Entry in
  research/academic_studies.md. (b) Returned cross-sectional / equity liquidity papers (arXiv:2609.00943, AEA/NBER/JFE PDFs; not
  single-pair direction studies, not opened); FX volume/illiquidity history beyond tick counts is not in the repo.
- No item added (rule 3 / R090: (a) dev already scanned and sub-pip, val family already used; (b) no study). pytest 434 passed. 0 trials
  used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R177 (not an item; no item added)
- 2026-11-14 R177 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "summit"/"Eurogroup" or
  "Michigan"/"consumer confidence" entry in research/ or knowledge/ before this run): (a) European Council / EU summit meetings ->
  EUR/USD; (b) University of Michigan consumer sentiment release (10:00 NY) -> later EUR/USD drift. Two standard searches. (a) Opened
  the author's LSE EUROPP summary of Smeets (JCMS, doi:10.1111/jcms.12062; entry in research/academic_studies.md): daily EUR/USD
  2008-2012, "no significant effects could be detected". Other hits (Konstanz repository, Banque de France WP859, FXEmpire Ecofin page)
  not opened. (b) Returned only broker/news pages (VT Markets, FXStreet, XTB; not evidence, not opened) and Fed IFDP 823 (web-archive
  viewer shell, already unreadable in R148); no study.
- No item added (rule 3 / R090: (a) published null and below the power floor; (b) no study). pytest 434 passed. 0 trials used
  (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R178 (not an item; no item added)
- 2026-11-14 R178 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Golden Week",
  "Chinese New Year"/"Lunar New Year" holiday or "Bank of Japan"/"BoJ" entry in research/ or knowledge/ before this run): (a) Asian
  holidays (Chinese New Year, Golden Week) liquidity -> EUR/USD; (b) Bank of Japan policy announcements -> later EUR/USD drift. Two
  standard searches. (a) Opened Krivosheev 2019 Erasmus thesis (Bitcoin only; no robust CNY effect); other hits broker/news pages
  (GO Markets, investinglive, MEXC; not evidence, not opened). (b) Opened IMF WP/25/227 (Carrière-Swallow et al. 2025; ~48% verbatim):
  USD/JPY 35-minute window only, no EUR/USD, no drift test; other hits FXStreet/Newsquawk/MUFG news pages. Entries in
  research/academic_studies.md.
- No item added (rule 3 / R090: (a) no FX study; (b) no EUR/USD evidence and ~8 events/year, below the power floor). pytest 434 passed.
  0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R179 (not an item; no item added)
- 2026-11-15 R179 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Länder"/German
  state CPI or ADP-report entry in research/ or knowledge/ before this run): (a) German state CPI releases (published hours before the
  national flash) -> EUR/USD drift; (b) US ADP employment report (08:15 NY Wednesday) -> later EUR/USD drift. Two standard searches.
  (a) Returned only Newsquawk/XTB/Continuum headline pages (not evidence, not opened); no study. (b) Returned FXStreet/Dukascopy
  preview pages (not evidence, not opened) and Jandejsek 2021 master thesis (opened, ~60% verbatim): NFP only, EUR/USD 1-minute,
  immediate jump with partial reversal, no drift test, no costs; ADP not studied. Entry in research/academic_studies.md.
- No item added (rule 3 / R090: (a) no study; (b) no ADP study, NFP family already covered by B12/E015). pytest 434 passed. 0 trials
  used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R180 (not an item; no item added)
- 2026-11-15 R180 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "volatility risk
  premium"/"realized volatility -> next-day direction" or "IMM date"/futures-roll entry in research/ or knowledge/ before this run):
  (a) realized/implied volatility -> later EUR/USD direction (safe-haven dollar); (b) CME quarterly FX-futures roll (IMM dates) -> spot
  EUR/USD. Two standard searches. (a) Opened CEPR DP9549 listing page ("Volatility Risk Premia and Exchange Rate Predictability"):
  cross-sectional, needs option-implied volatility, EUR/USD not mentioned. Other hits (thesis/central-bank volatility-modelling PDFs,
  an mql5 forum mirror) not evidence or not about direction, not opened. (b) Returned CME Group / FinanceFeeds articles on the year-end
  forward-points turn and futures-vs-forwards replication (exchange marketing, forward points only, not spot direction; not opened);
  no study; ~24 IMM dates on dev, below the R090 power floor anyway. Entry in research/academic_studies.md.
- No item added (rule 3 / R090: (a) needs options data, cross-sectional; (b) no study, below power floor). pytest 434 passed. 0 trials
  used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R181 (not an item; no item added)
- 2026-11-15 R181 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "PCE" or "maintenance
  period" entry in research/ or knowledge/ before this run): (a) US PCE price index release (08:30 NY) -> later EUR/USD drift;
  (b) ECB reserve maintenance period start / liquidity conditions -> EUR/USD. Two standard searches. (a) Returned only broker/news
  pages (FXStreet, XTB, Pound Sterling Live) and a macro blog (macroornoise.com; not evidence, not opened); no study. (b) Returned only
  language variants of an ECB Economic Bulletin 2026 Issue 4 box (ecb.ebbox202604_07); fetch of the English version refused by the
  tool (not circumvented, content UNVERIFIED, nothing recorded); no FX study.
- No item added (rule 3 / R090: (a) no study, US-inflation release family partly covered by R148 CPI angle; (b) no verified source).
  pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R182 (not an item; no item added)
- 2026-11-15 R182 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "quote volume
  imbalance" or "return autocorrelation term structure" entry in research/ or knowledge/ before this run): (a) Dukascopy bid/ask
  tick-volume (quote) imbalance -> next-interval EUR/USD return; (b) short-horizon (minutes) intraday return reversal / autocorrelation
  in EUR/USD. Two standard searches. (a) Hits were market-making / crypto order-book papers and blog posts (not FX evidence, not
  opened); market_microstructure.md already notes Dukascopy tick volume counts quote updates, not traded amounts. (b) Wisniewska (2014)
  already recorded (Low, too vague). Opened (web-fetch, first ~40k chars verbatim, rest model-summarised and UNVERIFIED):
  Boyarchenko-Larsen-Whelan, "The Overnight Drift", CEPR DP14462 (2020, https://repec.cepr.org/repec/cpr/ceprdp/DP14462.pdf):
  S&P 500 E-mini only, 02:00-03:00 ET drift turns to -3.3% p.a. after bid-ask spreads; FX only via cited papers (home-hours
  depreciation, already closed on val by E017). Baule-Schlie-Zhou, "The Term Structure of Intraday Return Autocorrelations", CESA WP 14
  (2025, https://www.fernuni-hagen.de/igas/docs/cesa_wp_14.pdf): US stocks only, strongest reversal ~15 min (-2.70% autocorrelation),
  no trading or cost analysis.
- No item added (rule 3 / R090: no EUR/USD evidence, no mechanism specific to our data). pytest 434 passed. 0 trials used (dev 259,
  val 9, total 268). Not a pipeline failure.

### Refill note R183 (not an item; no item added)
- 2026-11-15 R183 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Sentix" or
  "Eurostat"/euro-area GDP flash entry in research/ or knowledge/ before this run): (a) Sentix investor confidence release (first
  Monday of the month, 10:30 CET) -> later EUR/USD drift; (b) euro-area preliminary flash GDP release (Eurostat, 11:00 CET) -> later
  EUR/USD drift. Two standard searches. (a) Returned only broker/news headline pages (VT Markets, FXStreet) and a sentix.de special
  research print page (sentiment commentary, not an FX study; not opened); no study. (b) Returned only FXStreet "how could it affect
  EUR/USD" previews and a Continuum Economics flow note (not evidence, not opened); no study.
- No item added (rule 3 / R090: (a) no study, and would need a release-date/consensus calendar (B6 blocker); (b) no study, ~24
  quarterly flash releases on dev, below the power floor). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a
  pipeline failure.

### Refill note R184 (not an item; no item added)
- 2026-11-15 R184 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "ISM" entry in
  research/ or knowledge/ before this run; RSI only as one rule family in a daily multi-rule study): (a) US ISM manufacturing PMI release
  (10:00 NY, first business day) -> later EUR/USD drift; (b) intraday RSI mean-reversion rule in EUR/USD after real spreads. Two
  standard searches. (a) Returned only FXStreet and Dukascopy market-news pages (not evidence, not opened); no study. (b) Wiśniewska
  (2014) and Sokolovski (2011) already recorded (refill notes R055, R135-era); TradingView/Substack/MoneyShow posts not evidence. Opened
  (web-fetch, full text, quotes verbatim, table cells garbled and not used): Frömmel-Lampaert, "Does frequency matter for intraday
  technical trading?", Finance Research Letters 18 (2016) 177-183, DOI 10.1016/j.frl.2016.04.014
  (https://core.ac.uk/download/55846873.pdf): RUB/USD (MICEX) only, MA and RSI rules on 10-60 min bars, 2000-2011; "The adjustment for
  real, rather than estimated transaction costs wipes away most of the profits." No EUR/USD. Entry in research/academic_studies.md.
- No item added (rule 3 / R090: (a) no study, needs a release-date/consensus calendar (B6 blocker); (b) no EUR/USD evidence, and the
  only opened study finds costs remove the profits). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R185 (not an item; no item added)
- 2026-11-15 R185 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "ECB minutes"/"monetary
  policy accounts" or "moon" entry in research/ or knowledge/ before this run): (a) ECB monetary policy accounts release (~4 weeks after
  each meeting, 13:30 CET) -> later EUR/USD drift; (b) lunar cycle (new/full moon) -> EUR/USD daily return. Two standard searches.
  (a) Returned FXStreet/XTB/ActionForex/investinglive headline pages (not evidence, not opened) and one Aalto University bachelor's thesis
  (abstract only; full text behind login; authors and year not shown on page = UNVERIFIED): "Monetary policy announcement shocks and
  high-frequency exchange rate dynamics: evidence from the euro area"
  (https://aaltodoc.aalto.fi/items/4dcf8e0b-b547-4905-a85a-64c7d58e84a3): contemporaneous press-release-window reaction of EURUSD/EURGBP/
  EURJPY to OIS-based ECB announcement shocks, 1999-2023; about decisions, not accounts; no post-window horizon, no costs. (b) Returned
  MQL5/EarnForex blog posts (one self-described April-fool post; not evidence) and Herbst, "Lunacy in the Stock Market - What is the
  Evidence?", Journal of Bioeconomics 9(1) 2007, 1-18, DOI 10.1007/s10818-007-9016-3
  (https://ideas.repec.org/a/kap/jbioec/v9y2007i1p1-18.html, abstract only): DJIA daily, "no consistent, predictable lunar influence";
  no FX.
- No item added (rule 3 / R090: (a) no study of the accounts release, needs an accounts-date calendar, and the only opened source is a
  contemporaneous decision-window study needing OIS data; (b) published null, no FX study, no mechanism). pytest 434 passed. 0 trials used
  (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R186 (not an item; no item added)
- 2026-11-15 R186 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "press conference"
  reversal or "gold" predictor entry in rejected_hypotheses.md before this run): (a) FOMC press conference (14:30 NY) EUR/USD move
  reversing the 14:00 statement-window move; (b) lagged gold (XAU/USD) return -> next-day EUR/USD. Two standard searches.
  (a) Opened Acosta, Ajello, Bauer, Loria, Miranda-Agrippino, "Financial Market Effects of FOMC Communication: Evidence from a New
  Event-Study Database", FRBSF Working Paper 2025-30 (https://www.frbsf.org/wp-content/uploads/wp2025-30.pdf; paper dated 2026, number
  2025-30): Table 1 correlation of press-conference and statement rate-futures surprises -0.14 since April 2011 (0.44 in 2015-2019,
  -0.27 after March 2022); text says press conferences "have tended to counteract" the statement shift. Rate surprises, same-window only,
  no FX return-reversal test, no trading rule. Also opened Rosa, "The Financial Market Effect of FOMC Minutes", FRBNY Economic Policy
  Review, December 2013 (https://www.newyorkfed.org/medialibrary/media/research/epr/2013/0913rosa.pdf): volatility/volume around minutes,
  EUR/USD included, no directional result.
  (b) Opened Apergis, "Can gold prices forecast the Australian dollar movements?", International Review of Economics and Finance 29
  (2014) 75-82, DOI 10.1016/j.iref.2013.04.004 (author version:
  https://espace.curtin.edu.au/bitstream/handle/20.500.11937/4847/197566_197566.pdf?sequence=2): AUD/USD only (commodity-currency
  terms-of-trade mechanism), RMSE gains vs random walk without significance tests, no costs. A Reading JIMF 2018 revision
  (https://centaur.reading.ac.uk/82170/9/JIMF_2018_179_Revision%201.pdf) returned a bot-protection page: UNVERIFIED, not circumvented.
- No item added (rule 3 / R090: (a) ~32 dev scheduled FOMC meetings with a press conference (quarterly before 2019), the FOMC dev sample
  already used twice (E013, E040), and the published effect is a weak rate-surprise correlation, far below the > 20 pip detectability bar;
  (b) no EUR/USD study and the mechanism is specific to commodity currencies). pytest 434 passed. 0 trials used (dev 259, val 9, total
  268). Not a pipeline failure.

### Refill note R187 (not an item; no item added)
- 2026-11-15 R187 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Bitcoin -> EUR/USD"
  or "mutual-fund equity demand" entry in rejected_hypotheses.md before this run): (a) US equity-market close (16:00 NY) / global
  equity-fund demand -> EUR/USD; (b) Bitcoin intraday returns leading EUR/USD. Two standard searches.
  (a) Opened Rey, Rousset Planat, Stavrakeva, Tang, "Elephants in Equity and Currency Markets", preliminary, April 12, 2024
  (https://www.minneapolisfed.org/-/media/assets/events/2024/federal-reserve-system-committee-on-international-economic-analysis-conference-sciea/tang-elephants-in-equity-and-currency-markets.pdf;
  ~27% verbatim): contemporaneous monthly variance decomposition (net currency supply explains ~90% of FX variation), 2008-2021,
  needs ISIN-level mutual-fund holdings; no predictive horizon, no clock-time effect. Later sections UNVERIFIED (summary only).
  (b) Opened Eross, McGroarty, Urquhart, Wolfe, "The intraday dynamics of bitcoin", RIBAF 49 (2019) 71-81, DOI
  10.1016/j.ribaf.2019.01.008 (accepted version https://core.ac.uk/download/186324691.pdf, ~75% verbatim): Bitstamp 5-min
  BTC returns/volume/RV only, 2014-2017; no FX series. Reading repository copy returned a bot-protection page: not circumvented.
- No item added (rule 3 / R090: (a) proprietary fund-holdings predictor, contemporaneous monthly result only; (b) no FX study, no
  mechanism for BTC -> EUR/USD, and BTC data not in repo). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a
  pipeline failure.

### Refill note R188 (not an item; no item added)
- 2026-11-15 R188 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Fed speech" or
  "pre-announcement drift" entry in rejected_hypotheses.md before this run): (a) pre-release price drift before US macro
  announcements -> EUR/USD; (b) Fed Chair / FOMC-participant speeches -> post-speech EUR/USD drift. Two standard searches.
  (a) Opened Kurov, Sancetta, Strasser, Wolfe, "Price Drift Before U.S. Macroeconomic News", Internet Appendix, draft Nov 1, 2017
  (https://www.skidmore.edu/economics/documents/KSSWolfe-2017PriceDriftBeforeUSMacroeconomicNewsAppendix.pdf; ~68% verbatim):
  E-mini S&P 500 and 10-year T-note futures only (robustness: E-mini Dow, 30-year bond), 2008-2014; drift in [t-30min, t-5s] for
  7 of 30 releases (ISM mfg/non-mfg, pending/existing home sales, CB confidence, IP, GDP prelim) is signed by the realized surprise,
  known only at release; no FX instrument, no costs. Main JFQA paper (DOI 10.1017/S0022109018000625) not opened: UNVERIFIED.
  (b) Opened Ayadi, Ben Omrane, Wang, Welch, SEF 40(5) 2023, DOI 10.1108/SEF-01-2023-0015
  (https://ideas.repec.org/a/eme/sefpps/sef-01-2023-0015.html, abstract only): Fed/ECB official speeches have "a relatively small
  impact on currency jumps", no drift test. Opened Sekkel, Zhang, Stern, BoC SWP 2025-33
  (https://www.bankofcanada.ca/wp-content/uploads/2025/11/swp2025-33.pdf; ~33% verbatim): 211 Fed Chair + 76 Vice Chair speeches
  1997-2023, window -15 to +75 min, CAD/USD only, no FX drift or direction-knowable result. Opened Djourelova, Ferroni, Melosi,
  Villa, Chicago Fed WP 2025-23 (https://www.chicagofed.org/-/media/publications/working-papers/2025/wp2025-23.pdf; ~33% verbatim):
  FOMC-participant speeches 2011-2023, eurodollar futures/yields/equities, "little effect", no FX.
- No item added (rule 3 / R090: (a) direction of the drift is not knowable before the window (needs the surprise), and release
  timestamps/consensus are the B6 blocker; (b) no EUR/USD study, no predictable post-speech drift, and a timestamped speech
  calendar is not in repo). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R189 (not an item; no item added)
- 2026-11-15 R189 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "head-and-shoulders"
  or "volatility breakout" entry in research/ or rejected_hypotheses.md before this run): (a) head-and-shoulders chart pattern ->
  later EUR/USD direction; (b) intraday volatility-breakout / opening-range rules on EUR/USD. Two standard searches.
  (a) Opened Osler & Chang, "Head and Shoulders: Not Just a Flaky Pattern", FRBNY Staff Report 4, Aug 1995
  (https://www.newyorkfed.org/research/staff_reports/sr4.html and https://ideas.repec.org/p/fip/fednsr/4.html, abstract only):
  daily rates of major currencies vs USD, March 1973 - June 1994, objective algorithm, bootstrap vs random walk (10,000 series).
  PDF (https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr4.pdf) not openable (fetch-permission timeout, not
  circumvented): pattern algorithm, profits and significance UNVERIFIED. Published version Chang & Osler 1999, EJ 109(458): UNVERIFIED.
  (b) Opened Zarattini-Barbon-Aziz 2024 SSRN 4729284 (https://www.alexandria.unisg.ch/server/api/core/bitstreams/3c2989c4-688d-4d78-8a71-f02690990d51/content,
  ~80%): 5-min opening-range breakout on US stocks only, no FX. Vaughters 2018 Liberty DBA (https://core.ac.uk/download/213462372.pdf,
  ~13%): EUR/USD Bollinger Bands, "overall net loss from trading" (abstract). Sokolovski 2011 UCT MSc
  (https://open.uct.ac.za/bitstreams/1ca4b008-7ebc-4b87-8804-c8674358c228/download, ~14%): hourly reservation-price contrarian rule,
  11 pairs incl. EUR/USD, "cannot generate positive profits in the presence of realistic transaction costs" (abstract). None tests a
  breakout rule on FX.
- No item added (rule 3 / R090: (a) pattern definition not readable, so any algorithm would be invented here, pre-1994 sample, and
  daily H&S completions on one pair over 6 dev years give too few events; (b) no FX breakout study; the two EUR/USD technical-rule
  papers found are net-negative after costs and are logged as negative evidence only). pytest 434 passed. 0 trials used (dev 259,
  val 9, total 268). Not a pipeline failure.

### Refill note R190 (not an item; no item added)
- 2026-11-15 R190 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Ramadan"/"Hijri" or
  "Japanese fiscal year" entry in research/, knowledge/ or rejected_hypotheses.md before this run): (a) Ramadan / Hijri-calendar effect
  -> EUR/USD; (b) Japanese fiscal-year-end (March) repatriation flows -> EUR/USD. Two standard searches.
  (a) Opened Ozkan, "Hijri calendar effect in Borsa Istanbul gold market and Turkey's foreign exchange market", JIABR 10(4) 2019,
  DOI 10.1108/JIABR-04-2017-0054 (https://ideas.repec.org/a/eme/jiabrp/jiabr-04-2017-0054.html, abstract only): Turkish "Dollar and
  Euro market" (quote currency presumably TRY, UNVERIFIED), 2003-03-04 .. 2016-09-30, dummy regression + Kruskal-Wallis; "after-Ramadan
  effect in the Euro market", "the Hijri month effect does not exist in the Dollar market"; sign, size, frequency and costs UNVERIFIED
  (full text paywalled, not opened). Opened Halari-Helliar-Power-Tantisantiwong, QREF 2018, DOI 10.1016/j.qref.2018.05.018
  (https://eprints.soton.ac.uk/421696/, abstract only): equities only. Opened Lopez-Martin, RBF 14(4) 2022, DOI 10.1108/RBF-09-2021-0173
  (https://econpapers.repec.org/RePEc:eme:rbfpps:rbf-09-2021-0173, abstract only): cryptocurrencies only. DOAJ Arab Economic and
  Business Journal 2016 record (https://doaj.org/article/d4dd34bb29d84243b1046bf5bf4e0d37) not openable (client error): UNVERIFIED.
  (b) Returned only broker/news pages (FXStreet/Nomura, ForexLive/investingLive, Bloomberg, Pound Sterling Live/MUFG, MoneyShow,
  FNArena, MQL5; not evidence, not opened), all about USD/JPY or EUR/JPY, no study.
- No item added (rule 3 / R090: (a) only FX evidence is TRY-quoted with no sign or size, EUR/USD direction not derivable, and ~6
  Ramadan periods in dev are far below the power floor; (b) no study, JPY-cross mechanism, one March year-end per year). pytest 434
  passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R191 (not an item; no item added)
- 2026-11-15 R191 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "pre-holiday",
  "US holiday" or "UK bank holiday" entry in research/, knowledge/ or rejected_hypotheses.md before this run): (a) single-centre
  public holidays (one of the two currency areas closed) -> EUR/USD direction; (b) pre-holiday effect in FX. Two standard searches
  plus one follow-up. (a) Re-opened Ranaldo 2007 EFMA 2008 WP
  (https://www.efmaefm.org/0EFMAMEETINGS/EFMA%20ANNUAL%20MEETINGS/2008-Athens/papers/376.pdf, ~46% verbatim): holiday design is
  the same section 5.2 already logged in research/academic_studies.md (German-holiday days as EU proxy, n 36 for EUR/USD 1999-2005,
  no significance marks); nothing new. Search hits otherwise broker/news pages (not evidence, not opened). (b) Opened Howarth 2008
  Rhodes MCom thesis (https://researchrepository.ru.ac.za/bitstreams/cd843ec4-0cc5-415e-9c73-41ee165e0f0d/download, ~35% verbatim):
  BRL/MXN/ZAR/KRW/PLN vs USD, day-of-week only, holiday effect not tested; it cites Aydogan & Booth (2003) for exchange rates moving
  before holidays. Aydogan & Booth 2003 ("Calendar anomalies in the Turkish foreign exchange markets", Applied Financial Economics
  13(5); https://ideas.repec.org/a/taf/apfiec/v13y2003i5p353-360.html) seen as a search title only, not opened: UNVERIFIED, Turkish
  market. Dao-McGroarty-Urquhart 2016 (https://eprints.soton.ac.uk/402301, landing page) is the weekend-gap paper already tested (E020).
- No item added (rule 3 / R090: (a) already covered, ~6 single-centre holidays per year per side gives ~35 dev events, below the
  power floor; (b) no EUR/USD study). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R192 (not an item; no item added)
- 2026-11-15 R192 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no Ifo/ZEW release-drift
  or BoE-spillover entry in research/, knowledge/ or rejected_hypotheses.md before this run): (a) German Ifo business climate / ZEW
  sentiment releases -> EUR/USD post-release drift; (b) Bank of England MPC announcements -> EUR/USD spillover. Two standard searches.
  (a) Only academic hit: Mannheim/ZEW Discussion Paper 09-010 (https://madoc.bib.uni-mannheim.de/2347/1/dp09010.pdf; mirror
  https://www.zew.de/fileadmin/FTP/dp/dp09010.pdf): Mannheim copy served a bot-challenge page, ZEW copy fetch refused; not opened,
  title/content UNVERIFIED (not circumvented). Other hits broker/news pages (XTB, FXStreet, aggregators; not evidence, not opened).
  (b) Opened Volta & Aste, "Causal coupling between European and UK markets triggered by announcements of monetary policy decisions",
  Royal Society Open Science 9(3) 2022, DOI 10.1098/rsos.211342 (https://researchonline.lse.ac.uk/id/eprint/114947 and
  https://econpapers.repec.org/paper/ehllserod/114947.htm, abstract only; PMC full text served a bot-challenge page): Euro Stoxx 50 and
  FTSE 100 1-minute prices only, transfer-entropy information flow "from the market where the announcement is made towards the other",
  volatility upsurge on announcement days; no FX, no return-forecast or trading test.
- No item added (rule 3 / R090: (a) no readable study, drift direction not derivable, mechanism would be invented here; (b) equity-only,
  non-directional coupling measure, ~8 MPC dates per year). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a
  pipeline failure.

### Refill note R193 (not an item; no item added)
- 2026-11-15 R193 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles: (a) US Treasury
  auction results -> intraday EUR/USD; (b) December / turn-of-the-year USD seasonality -> EUR/USD. Two standard searches.
  (a) Only academic hit is Krohn (FRBSF PDF https://www.frbsf.org/wp-content/uploads/Krohn-Paper.pdf), already opened and logged
  2026-11-11 R085 (research/academic_studies.md ~line 394); nothing new. Other hits broker/chart pages (forex.com, TradingView; not
  evidence, not opened). (b) Hits are broker/vendor seasonality pages only (forex.com/StoneX, Seasonax, Pound Sterling Live, FXStreet
  quoting MUFG; not evidence, not opened); no academic study found.
- No item added (rule 3 / R090: (a) already covered; (b) no study, and 6 Decembers on dev is far below the power floor). pytest 434
  passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R194 (not an item; no item added)
- 2026-11-15 R194 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "BTP", "sovereign
  spread", "M&A" or "merger" entry in research/, knowledge/ or rejected_hypotheses.md before this run): (a) Italian BTP-Bund spread
  changes -> next-day EUR/USD (lagged daily cross-market signal, lesson R095); (b) cross-border M&A announcements -> EUR/USD.
  Two standard searches. (a) Hits are bank/broker/news pages only (ING Think, FXStreet, Seeking Alpha, investireoggi; not evidence,
  not opened); no academic study of a lagged spread -> EUR/USD effect found. (b) Opened Riddiough & Zhang 2022 WP "Cross-Border M&A
  Flows, Economic Growth, and Foreign Exchange Rates" (https://www.bis.org/events/221213_bis_bdi_ecb_exchange_rates/paper_riddiough.pdf,
  ~22% verbatim): monthly abnormal net US M&A flows (SDC Platinum) predict next-month currency returns in a 41-country cross-section
  vs USD; EUR/USD coverage not confirmed; FX-results section not read verbatim (figures UNVERIFIED). Opened the IDEAS record of
  Fender & Galati 2001, BIS Quarterly Review (https://ideas.repec.org/a/bis/bisqtr/0112g.html, abstract only): one event (Deutsche
  Telekom/VoiceStream, July 2000), euro -1.06% on the news day, no test.
- No item added (rule 3 / R090: (a) no study, mechanism would be invented here; (b) needs licensed deal data not in the repo, monthly
  horizon gives ~72 dev observations far below the power floor, and the EUR/USD evidence is a single 2000 event). pytest 434 passed.
  0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R195 (not an item; no item added)
- 2026-11-15 R195 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "EUR/CHF" or
  "breakeven" entry in research/, knowledge/ or rejected_hypotheses.md before this run): (a) Swiss franc / EUR/CHF moves -> next-
  session EUR/USD (lead-lag); (b) US inflation / breakeven-inflation changes -> next-period EUR/USD. Two standard searches.
  (a) Hits are broker/forum/news pages only (MQL5 blog, investing.com, FXStreet, forex.com, StoneX, a Substack; not evidence, not
  opened); no academic lead-lag study found. (b) Opened the BIS landing page of Schrimpf & Sihvonen, "Inflation and the joint
  bond-FX spanning puzzle", BIS Working Paper 1320, Dec 2025
  (https://www.bis.org/publications/working-paper-1320-inflation-and-joint-bond-fx-spanning-puzzle; the PDF URL
  https://www.bis.org/publ/work1320.pdf served the landing page, full text not read): "US inflation predicts both low bond returns
  and high dollar returns"; uses realised inflation (not breakevens per the summary), dollar counter-currency, frequency, horizon and
  coefficients UNVERIFIED.
- No item added (rule 3 / R090: (a) no study, mechanism would be invented here; (b) realised-inflation predictor is a monthly
  release, giving ~72 dev observations, far below the power floor, and EUR/USD coverage is unconfirmed). pytest 434 passed. 0 trials
  used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R196 (not an item; no item added)
- 2026-11-15 R196 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "reverse repo",
  "net liquidity" or "weekly financial statement" entry in research/, knowledge/ or rejected_hypotheses.md before this run):
  (a) Fed liquidity (reserves / overnight reverse repo / Treasury General Account changes) -> later EUR/USD; (b) ECB weekly
  financial statement (Tuesday release) -> EUR/USD. Two standard searches. (a) Opened Correa, Du & Liao, "U.S. Banks and Global
  Liquidity", Fed IFDP 1289, July 2020, DOI 10.17016/IFDP.2020.1289 (https://www.federalreserve.gov/econres/ifdp/files/ifdp1289.pdf,
  ~32% verbatim): daily FR2052a GSIB data; verbatim "an increase in the TGA balance is significantly associated with wider repo and FX
  swap spreads" (same-day association with funding spreads, not spot returns); no exchange-rate return or forecast test in the part
  read (unread ~68% UNVERIFIED). Other hits NBER/CEMFI/AEA PDFs not opened, a vendor page and news (not evidence). (b) Hits are ECB
  monetary-policy-announcement and ECB-statement studies (Fratzscher-type, ETH/KOF WP 07-174; family already covered by earlier
  "speech"/ECB-announcement refill notes); no study of the weekly financial statement found.
- No item added (rule 3 / R090: (a) contemporaneous funding-spread result only, no spot-direction mechanism or sign, a forecast
  rule would be invented here, and weekly TGA/RRP data are not in the repo; (b) no study). pytest 434 passed. 0 trials used (dev 259,
  val 9, total 268). Not a pipeline failure.

### Refill note R197 (not an item; no item added)
- 2026-11-15 R197 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Ichimoku" entry and
  MACD only as a rule list in research/ before this run): (a) Ichimoku cloud rules -> EUR/USD; (b) MACD crossover -> EUR/USD. Two
  standard searches. (a) Deng et al. 2021 IJFE, DOI 10.1002/ijfe.2067 (RePEc abstract opened): FX rules inconsistent across
  subperiods, parameter sweep found no profitable FX rule; pairs/frequency/costs UNVERIFIED. (b) Franco Silva 2012 ISCTE M.Sc. thesis
  (~45% verbatim): daily GA-optimised MACD etc.; EUR/USD MACD out-of-sample profit factor 0.97 (summary, UNVERIFIED). Other hits
  broker/vendor pages (not evidence).
- No item added (rule 3 / R090: both sources are negative evidence with no published positive mechanism or sign to pre-register;
  daily Ichimoku/MACD signals on 6 dev years give few trades; technical-rule family already NONE in E047-E049). pytest 434 passed.
  0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R198 (not an item; no item added)
- 2026-11-15 R198 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Google Trends",
  "volume profile" or "point of control" entry in research/ or knowledge/ before this run): (a) Google search attention -> later
  EUR/USD returns; (b) volume profile / extreme trading imbalance -> later EUR/USD. Two standard searches. (a) Bulut 2018, "Google
  Trends and the forecasting performance of exchange rate models", J. Forecasting 37(3) 303-315, DOI 10.1002/for.2500 (RePEc abstract
  opened, https://ideas.repec.org/a/wly/jforec/v37y2018i3p303-315.html): monthly returns, 11 OECD currencies 2004-2014, better
  out-of-sample direction for five pairs vs random walk; EUR/USD inclusion, sign and costs UNVERIFIED. Goddard, Kita & Wang,
  "Investor Attention and FX Market Volatility" (https://orca.cardiff.ac.uk/73438/1/Attetion_FX.pdf, ~51% verbatim): weekly, EUR/USD
  included, attention predicts next-week volatility, not returns. (b) Volume-profile hits are vendor/forum pages (not evidence).
  Chen & Kao, "Momentum and Reversals in Weekly Euro FX Futures Returns during Periods of Extreme Trading Imbalance", EFMA 2009
  (https://www.efmaefm.org/0efmameetings/EFMA%20ANNUAL%20MEETINGS/2009-Milan/papers/EFMA2009_0102_fullpaper.pdf, full text read):
  CME Euro FX futures 1999-2005, weekly; reversal after extreme negative signed-trade imbalance only; authors state standard
  regressions show no relation. zendy record for DOI 10.1002/fut.20226 returned an empty page (UNVERIFIED).
- No item added (rule 3 / R090: (a) monthly predictor gives ~72 dev observations, below the power floor, EUR/USD coverage unconfirmed,
  and Trends data are not in the repo; Goddard et al. is a volatility result; (b) needs signed futures trade imbalance, which
  Dukascopy spot quotes do not provide, and the extreme-week subset of ~312 dev weeks is far below the power floor; weekly reversal
  family already reviewed R174). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R199 (not an item; no item added)
- 2026-11-15 R199 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "variance ratio" or
  "Kalman" entry in research/ or knowledge/ before this run): (a) variance-ratio / return-autocorrelation inefficiency -> EUR/USD
  direction; (b) Kalman-filter trend signal -> EUR/USD. Two standard searches. (a) Bošnjak, Novak & Wittine, "Time-varying
  inefficiency in exchange rate returns: the case of euro against major currencies", Ekonomska misao i praksa 2025, DOI
  10.17818/EMIP/2025/45 (https://hrcak.srce.hr/file/486449, full text read except figures): daily ECB reference rates 1999-2025,
  rolling 500-day Escanciano-Lobato / Kim wild-bootstrap variance-ratio tests; EUR/USD flagged inefficient in ~7.4-7.6% of windows,
  sign and lag of the autocorrelation not reported, no trading rule or costs; verbatim "Substantial efficiency is a common feature of
  the exchange rate market for major currencies". Other hits (variance-ratio methodology papers, arXiv physics) not opened.
  (b) Benhamou, "Trend without hiccups - a Kalman filter approach" (https://arxiv.org/pdf/1808.03297, full text read): E-mini S&P 500
  only, daily, one year (Feb 2015-Feb 2016), parameters optimised in-sample ("Parameters for the Kalman filter models are obtained
  by a general optimization."), no FX, no out-of-sample test. Other hits vendor/blog pages (not evidence).
- No item added (rule 3 / R090: (a) no sign or horizon to pre-register, daily data, the paper's own conclusion is efficiency;
  (b) in-sample equity-index result with no FX evidence; trend-rule family already NONE in E047-E049). pytest 434 passed. 0 trials
  used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R200 (not an item; no item added)
- 2026-11-15 R200 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "lunch", "PPP" or
  "short-term reversal" entry in research/ or knowledge/ before this run): (a) London lunch-hour (12:00-13:00 London) liquidity dip /
  intraday return pattern -> EUR/USD; (b) PPP / valuation deviation -> later EUR/USD return; (c) hourly short-term reversal -> EUR/USD.
  Four standard searches. (a) Top relevant hit was Breedon & Ranaldo, "Intraday Patterns in FX Returns and Order Flow", QMUL SEF WP
  694 (2012) (https://qmul.ac.uk/sef/research/workingpapers/2012/items/694.html, landing page and abstract read; PDF fetch failed,
  0% of full text read): "a significant tendency for currencies to depreciate during local trading hours" - the published version
  is already logged (academic_studies.md, Breedon & Ranaldo 2013) and the home-hours line is closed on val (B14/E017). No study on
  a lunch-hour pattern found; other hits were fix papers already logged (Marsh-Panagiotou-Payne 2017, Krohn et al.) or a vendor page.
  (b) Hits were monthly/quarterly PPP and expectations papers (not opened): monthly predictor below the power floor (R195 reasoning).
  (c) Only hit already logged: Wiśniewska (2014) EURUSD intraday price reversal (academic_studies.md, R055); KMW BoC SWP 2021-48
  already logged.
- No item added (rule 3 / R090: no new source with a pre-registrable sign and horizon). pytest 434 passed. 0 trials used
  (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R201 (not an item; no item added)
- 2026-11-15 R201 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "sovereign CDS",
  "trade balance" or "Della Corte" entry in research/ or knowledge/ before this run): (a) euro-area sovereign CDS / credit risk ->
  later EUR/USD returns; (b) US trade-balance release -> post-release EUR/USD drift. Two standard searches. (a) Opened two PDFs
  (entries in research/academic_studies.md): Della Corte, Jeanneret & Patelli, JFE 2023 (~32% verbatim): the USD-vs-EUR quanto CDS
  credit-implied risk premium "positively predicts future dollar-euro exchange rate returns at any horizon between one week and one
  year"; daily IHS Markit quanto CDS 2010-2019, weekly+ horizons. 2017 CDS-quanto conference draft (~36% verbatim): pricing model,
  no forecast. (b) Only broker/vendor pages (mql5 blogs, XTB, ForexCracked; not evidence, not opened).
- No item added (rule 3 / R090: (a) is the first published, signed EUR/USD predictor found in many refill passes, but it needs
  licensed quanto-CDS data (IHS Markit) not in the repo and not on the runner, and its weekly horizon gives ~312 dev weeks, below the
  power floor; adding it would need a human data decision; (b) no study). pytest 434 passed. 0 trials used (dev 259, val 9,
  total 268). Not a pipeline failure.

### Refill note R202 (not an item; no item added)
- 2026-11-15 R202 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "previous week" /
  "weekly high" or "Safa"/"Maroney" entry in research/ or knowledge/ before this run): (a) breakout of the previous week's high/low
  -> EUR/USD continuation; (b) quoted bid-ask spread changes -> later EUR/USD returns. Three standard searches. (a) Only result of
  note is Caporale-Plastun-Oliinyk (Brunel WP 2005), already logged R174 (same-month only); no weekly-extreme study found. (b) Opened
  the Safa-Maroney (JECD 2012) article page (entry in research/academic_studies.md): AUD, GBP, CAD vs USD only, spread "positively
  affects" returns, frequency and lag UNVERIFIED (PDF not openable this run, not circumvented).
- No item added (rule 3: (a) no published mechanism/sign for EUR/USD weekly extremes; (b) no EUR/USD, no verified predictive lag).
  pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R203 (not an item; no item added)
- 2026-11-16 R203 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles tried: (a) US cash-equity
  close (16:00 NY) flows -> late-afternoon EUR/USD return; (b) US Treasury quarterly refunding announcements -> EUR/USD. Two standard
  searches. (a) Hits were only Krohn-Mueller-Whelan (fixings family, already tested E022-E025, E032), Evans (NYU microstructure
  meeting 2015, not opened) and the Melvin-Prins equity-hedging slides (already logged; month-end line tested E034); the equity-close
  angle was already covered by refill note R187 (~line 2123). (b) Only news/broker pages (Newsquawk, FXStreet, MarketPulse, Marc to
  Market; not evidence, not opened); the angle was already covered by refill note R159 (~line 1785, ~4 events/year, below the R090
  power floor). Keyword checks (fiscal year, repatriation, dividend, index rebalancing, MSCI, JOLTS, Fed speech) show the remaining
  candidate angles are all already logged (R149, R170, R161, R188).
- No item added (rule 3 / R090: nothing new opened; both angles duplicate earlier notes). pytest 434 passed. 0 trials used
  (dev 259, val 9, total 268). Not a pipeline failure. Search space for free, runner-downloadable, verified EUR/USD predictors
  appears exhausted under the current data constraints; see decision log R203.

### Refill note R204 (not an item; no item added)
- 2026-11-16 R204 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles: (a) CFTC COT
  speculative positioning -> EUR/USD; (b) US-German 2-year yield spread change -> next-day EUR/USD; (c) Heiken Ashi / HASTOC
  candle rules -> EUR/USD (no "Heikin"/"Heiken" entry before this run). Three standard searches. (a) Top hits Klitgaard-Weir 2004
  (FRBNY EPR) and Tornell-Yuan already logged (R082, R120): duplicate, weekly, below R090 power floor. (b) Only broker/vendor pages
  (FXStreet, FXCM, TradingView scripts; not evidence, not opened); no study. (c) Opened two IDEAS abstracts (entries in
  research/academic_studies.md): Roy Trivedi IJFE 2022 (doi:10.1002/ijfe.2245; three unnamed currencies, positive returns only for
  "select time frames", no costs stated) and MPRA 89594 (USD/INR hourly, ~4 months).
- No item added (rule 3 / R090: no EUR/USD study with a pre-registrable sign, horizon and cost treatment). pytest 434 passed.
  0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R205 (not an item; no item added)
- 2026-11-16 R205 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles: (a) Keltner-channel /
  ADX trend-strength rules -> intraday EUR/USD (no "Keltner" entry before this run; ADX only in a GA-optimised daily-rule paper);
  (b) US early-close / low-liquidity holiday sessions (day after Thanksgiving, Christmas Eve) -> EUR/USD. Two standard searches.
  (a) Top academic hit opened twice: Frömmel-Lampaert "Does frequency matter for intraday technical trading?" (FRL 18, 2016,
  doi:10.1016/j.frl.2016.04.014, CORE full text; 2015 working-paper version on unecon.ru): RUB/USD MICEX only, MA and RSI rules
  only (no Keltner/ADX), in-sample SPA, "The adjustment for real, rather than estimated transaction costs wipes away most of the
  profits" (verbatim) -> already logged in R184, duplicate. Other hits vendor/broker pages (not evidence, not opened).
  (b) Only TradingView / FXStreet / forex.com / asset-manager commentary pages (not evidence, not opened); no study; ~2 events per
  year (~12 dev dates), far below the R090 power floor.
- No item added (rule 3 / R090: no EUR/USD study with a pre-registrable sign, horizon and cost treatment). pytest 434 passed.
  0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R206 (not an item; no item added)
- 2026-11-16 R206 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Twitter"/"tweet"
  entry in research/ or knowledge/ before this run): (a) social-media (Twitter) sentiment -> later EUR/USD returns; (b) economic
  surprise index -> later EUR/USD returns. Two standard searches. (a) Opened two papers (entries in research/academic_studies.md):
  Papaioannou et al. (arXiv 1310.5306 / NETNOMICS): hourly "buy EUR/USD" tweets, 54 days, "no ARX model could significantly
  outperform the random walk" (verbatim), no costs; Gholampour & van Wincoop (NBER conf. paper 2016): informed-tweet sentiment
  predicts EUR/USD direction at 1-3 months, not magnitude; lags t..t-4 days insignificant. VoxEU column not opened (permission
  timeout, not circumvented). (b) Top academic hit DNB WP 850 already logged (R139); rest broker/vendor pages (not opened).
- No item added (rule 3 / R090: no runner-downloadable tweet archive; the only significant effect is at monthly horizons, below the
  power floor; (b) duplicate). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R207 (not an item; no item added)
- 2026-11-16 R207 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "options expiry",
  "doji", "piercing" entry in research/ or knowledge/ before this run): (a) FX option expiries at the 10:00 NY cut (strike pinning)
  -> EUR/USD around 10:00 NY; (b) intraday/daily candlestick reversal patterns (doji, hammer, piercing line / dark cloud cover)
  -> EUR/USD. Two standard searches. (a) Only daily expiry-list news pages (investingLive, Newsquawk, VT Markets; not evidence,
  not opened); no study; historical strike/notional data is not downloadable on the runner. (b) Opened (entries in
  research/academic_studies.md): Alanazi-Alanazi-McMillan 2020 Cogent (doi:10.1080/23322039.2020.1768648), abstract only, 24 pairs
  daily, "chart patterns are profitable" but "the spread is a large burden on profitability", EUR/USD not named, design UNVERIFIED
  (full text permission prompt timed out, not circumvented); same family as Alanazi 2020 EJF already logged (R142). Detollenaere-Mazza
  2012 WP: Euronext stocks, execution costs only. Alanazi 2020 EJF hit is a duplicate of R142.
- No item added (rule 3 / R090: no EUR/USD study with a verified pattern definition, horizon and cost treatment; expiry angle has
  no study and no runner data). pytest 434 passed. 0 trials used (dev 259, val 9, total 268). Not a pipeline failure.

### Refill note R208 (not an item)
- 2026-11-16 R208 refill pass (no ready item, no run queued; last run 43541310326 recorded as E049). Angles (no "Markov", "regime
  switching", "Engel", "Dueker" or "Williams %R" entry in research/ or knowledge/ before this run): (a) Markov regime-switching
  trading rules -> daily EUR/USD; (b) Williams %R / stochastic oscillator -> intraday EUR/USD. Two standard searches.
  (a) Opened Dueker & Neely (St. Louis Fed WP 2001-021, JBF; ~77% verbatim) and the Parikakis & Merika (J. Forecasting 2009)
  abstract; entries in research/academic_studies.md. (b) Only vendor/broker pages (BabyPips, TradingView, Substack); not evidence,
  not opened; not added.
- Why this line: a published, out-of-sample, cost-adjusted daily rule on a series that includes EUR/USD, with a second paper naming
  EUR/USD; price data only (no new source). Different mechanism from B16 (12-month TSMOM, sign of past return): the signal is the
  model's expected 8-day return from filtered regime probabilities, which can flip within days. Prior is weak: sample ends 2005
  (decay, Neely-Weller-Ulrich 2009) and the published gain over MA rules is ~95 bp/yr.

### B60: Markov regime-switching expected-return rule, daily EUR/USD (signal test, dev) → E050 · `done` (2026-11-16 R210: NONE, n 1290, -1.106 pips, CI (-3.478, 1.441), t p 0.7853. Added 2026-11-16 R208 refill; 1 dev trial counted when it runs)
- 2026-11-16 R209: pre-registered as E050 (experiments/2026-11-16_E050_markov_switch/), queued on research-batch; status `running`.
- **Mechanism [PUB]:** Dueker & Neely (St. Louis Fed WP 2001-021 / JBF, opened R208): a Markov switching model of daily excess
  FX returns (DEM/EUR, JPY, CHF, GBP vs USD) traded on the sign of its average expected return over eight days earns positive
  out-of-sample returns net of 10 bp costs, 1982/83-2005, modestly above moving-average rules (verbatim in academic_studies.md).
  Parikakis & Merika (2009, abstract only) report "exceptional out-of-sample returns" for EUR/USD with Dueker-Neely-type rules.
  Economic story: persistent regimes in mean/volatility ("long swings") that the filtered probabilities pick up early.
- **Model (fixed now; a simplification, state it in results):** 2-state Markov switching model on daily mid log returns r(D) =
  ln(mid 16:00 NY D / mid 16:00 NY D-1) in pips-scaled units, switching mean and switching variance, Gaussian errors, constant
  transition matrix (statsmodels `MarkovRegression(r, k_regimes=2, trend="c", switching_variance=True)`; statsmodels must be added
  to the project dependencies). No kurtosis switching, no interest differential (spot only, as B16; carry not in data). Labels are
  not needed: the forecast uses both states.
- **Signal (fixed now):** expanding window inside dev. First fit on all dev trading dates up to 2015-12-31 (~260 dates); refit every
  21 trading dates on all returns up to and including D (parameters frozen between refits; filtered probabilities updated daily with
  the frozen parameters using returns up to D only). On each trading date D from the first dev date of 2016: E8(D) = sum over
  h = 1..8 of p(D)' P^h mu, where p(D) is the filtered state probability vector at D, P the transition matrix and mu the state means.
  s(D) = sign(E8(D)) (s = 0 and date excluded if E8 = 0 exactly). Position s(D) held from 16:00 NY on D to 16:00 NY on D+1 (same
  timing as B16/E019, avoids the roll). Daily signed return = s(D) x (mid 16:00 NY D+1 - mid 16:00 NY D) in pips. Horizon 8 and
  refit interval 21 are fixed before data; other values are new trials. If a fit fails to converge, keep the previous parameters and
  count the failures (if the very first fit fails, the experiment is BLOCKED, 0 trials, and the failure is fixed before re-queueing).
- **No-look-ahead test (required):** truncating the series after D must leave s(D) unchanged; random-walk synthetic series must give
  no SIGNAL.
- **Test:** **dev only, 1 trial**; n ~1,290 (2016-2020). Dates missing either 16:00 NY bar are excluded and counted.
- **Decision rule (draft, same as B16):** SIGNAL if mean daily signed return > 1.0 pip AND moving-block bootstrap (block 20 dates,
  2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
  A SIGNAL earns B61 (val confirmation).
- **Descriptive (not in rule):** number of sign flips and mean holding spell; net per flip at bid/ask, SPEC 4 and costs x1.5; by
  year; long and short dates; buy-and-hold and E019 (TSMOM) on the same dates; refit failures; mean of the two state SDs.
- **Power note:** daily SD ~45 pips, n ~1,290 -> bootstrap CI half-width ~2.5-3 pips. Dueker-Neely's average 5.27%/yr is ~2 pips/day
  at EUR/USD ~1.13, so the published effect size is near the detection limit; a NONE does not rule it out.
- **Contamination note:** daily 16:00 NY returns on dev were used by E019 (sign of 252-day return), E037, E041; no regime model or
  multi-day expected-return statistic has been computed on dev. Record this.
- **Calendar label:** multi-day regime/trend; not a time-of-day effect.
- **Data:** price data in repo only; statsmodels on the runner (pip).

### B61: Markov regime-switching rule, val confirmation (signal test, val only) · `done` (2026-11-16 R210: closed unearned, 0 trials; B60 NONE on dev (E050). Was: added 2026-11-16 R208; earned only if B60 returns SIGNAL on dev)
- Same model, horizon, refit interval, timing and rule as B60 on val (2021-01-21 to 2023-06-30), first fit on all dev dates plus val
  dates up to D (expanding), 1 val trial at p < 0.05, block-20 bootstrap. Closed unearned (0 trials) if B60 is NONE or WEAK.

### Refill note R211 (not an item)
- 2026-11-16 R211 refill pass (no ready item, no run queued; last run 43817068619 recorded as E050). Angles (no "random forest",
  "LSTM" or "Kalman" daily-rule entry used for an item in research/ or knowledge/ before this run): (a) machine-learning classifiers
  on lagged daily returns -> next-day EUR/USD direction; (b) Kalman-filter trend rules -> daily EUR/USD. Two standard searches.
  (a) Opened Theofilatos, Likothanassis & Karathanasopoulos (ETASR 2012, doi:10.48084/etasr.200; entry in research/academic_studies.md):
  EUR/USD daily, Random Forest on 10 lagged returns, 8.29%/yr gross, 7.28% after ~1 pip costs in a 22-month 2009-2010 window. Other
  hits (SSRN mirror on a storage bucket, Glasgow thesis, arXiv 2512.12727 / 2409.04471 / 2310.04536, QME articles) not opened, not cited.
  (b) Warwick WBS WP 99-89 fetch: permission prompt timed out, not circumvented, not cited; other hits were vendor/blog pages or
  not opened.
- Why this line: a published EUR/USD-specific daily rule with costs, price data only, fixable before data (inputs, tree count, timing).
  Different from B16 (sign of 252-day return) and B60 (regime model): a nonlinear classifier on the last 10 daily returns. Prior is
  weak (single short test window, Table III possibly validation-subset, no significance tests, GA tuning not reproducible).

### B62: Random-forest classifier on 10 lagged daily returns, next-day EUR/USD direction (signal test, dev) → E051 · `done` (2026-11-16 R213: NONE, n 1241, +1.953 pips, CI (-1.244, 4.581), t p 0.0852. Added 2026-11-16 R211 refill; 1 dev trial counted when it runs)
- 2026-11-16 R212: pre-registered as E051 (experiments/2026-11-16_E051_rf_lags/), queued on research-batch; status `running`.
- **Mechanism [PUB, weak]:** Theofilatos et al. (ETASR 2012, R211): Random Forest (51 trees) on 10 lagged daily EUR/USD returns,
  always-in-market long/short on predicted direction, 53.5% hit rate and 7.28%/yr after ~1 pip costs, 2009-2010. Story: short-horizon
  nonlinear dependence (e.g. reversal after large moves, continuation after small ones) that a linear AR misses.
- **Model (fixed now; a simplification, state it in results):** daily mid log returns r(D) = ln(mid 16:00 NY D / mid 16:00 NY D-1)
  (same series as E019/E050). Features at D: r(D), r(D-1), ..., r(D-9) (10 lags, all known at 16:00 NY D). Label for a training row
  at D: 1 if r(D+1) > 0, 0 if r(D+1) < 0, row dropped if r(D+1) = 0. scikit-learn `RandomForestClassifier(n_estimators=51,
  random_state=0)`, all other arguments at library defaults (the paper's GA-tuned settings are not reported; no tuning here).
  scikit-learn must be added to the project dependencies (pin the version in the record).
- **Signal (fixed now):** expanding window inside dev, same schedule as E050. First fit on all training rows whose label date D+1 is
  <= 2015-12-31; refit every 21 trading dates on all rows whose label date is <= D (model frozen between refits). On each trading
  date D from the first dev date of 2016: p(D) = predicted probability of class 1; s(D) = +1 if p > 0.5, -1 if p < 0.5, date
  excluded (counted) if p = 0.5 exactly or any of the 10 lags is missing. Position s(D) held 16:00 NY D -> 16:00 NY D+1. Daily signed
  return = s(D) x (mid 16:00 NY D+1 - mid 16:00 NY D) in pips. Lags 10, trees 51 and refit interval 21 are fixed before data; other
  values are new trials.
- **No-look-ahead test (required):** truncating the series after D must leave s(D) unchanged; no training row may have a label date
  > D; a random-walk synthetic series must give no SIGNAL.
- **Test:** **dev only, 1 trial**; n ~1,290 (2016-2020). Dates missing either 16:00 NY bar are excluded and counted.
- **Decision rule (draft, same as B16/B60, `decide_b16`):** SIGNAL if mean daily signed return > 1.0 pip AND moving-block bootstrap
  (block 20 dates, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t-test p < 0.05. WEAK if mean > 0 and (CI lower > 0 or
  p < 0.05); else NONE. A SIGNAL earns B63 (val confirmation).
- **Descriptive (not in rule):** hit rate; number of sign flips; net per flip at bid/ask, SPEC 4 and costs x1.5; by year; long and
  short dates; buy-and-hold, E019 (TSMOM) and E050 on the same dates; mean p(D); feature importances at the last refit.
- **Power note:** daily SD ~45 pips, n ~1,290 -> bootstrap CI half-width ~2.5-3 pips. The published 8.29%/yr gross is ~3.7 pips/day
  at EUR/USD ~1.13, above the 1-pip threshold but only just above the detection limit; a NONE does not rule out a smaller effect.
- **Contamination note:** daily 16:00 NY returns on dev were used by E019, E037, E041, E050; no lagged-return classifier or AR model
  has been fitted on dev. Record this.
- **Calendar label:** short-horizon return dependence; not a time-of-day effect.
- **Data:** price data in repo only; scikit-learn on the runner (pip).

### B63: Random-forest lagged-return rule, val confirmation (signal test, val only) · `done` (2026-11-16 R213: closed unearned, 0 trials; B62 NONE on dev (E051). Was: added 2026-11-16 R211; earned only if B62 returns SIGNAL on dev)
- Same model, settings, timing and decision rule as B62, model trained on dev only (expanding refits continue into val with the same
  21-date schedule), evaluated on val dates only; 1 val trial. Pre-register as its own experiment before running. Lead criteria in
  docs/AUTONOMOUS_PROTOCOL.md (costs x1.5 net > 0) apply.

### Refill note R214 (not an item; no item added)
- 2026-11-16 R214 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "nearest neighbour",
  "k-nearest" or "Sosvilla" entry in research/ or knowledge/ before this run): (a) nearest-neighbour nonparametric forecasts of daily
  FX returns -> EUR/USD; (b) short-lookback (1-month) time-series momentum -> daily EUR/USD. Three standard searches.
  (a) Opened Fernández-Rodríguez, Sosvilla-Rivero & Andrada-Félix (FEDEA WP 2002-05 text; AFE 2003 abstract, doi:10.1080/09603100210100891;
  entry in research/academic_studies.md): nine EMS currencies vs DEM, 1978-1994, NN rule beats moving averages "in most cases" after
  costs; no EUR/USD or USD pair; per-currency numbers UNVERIFIED. (b) Only AQR dataset pages, the SSRN landing page and blogs; MOP 2012
  is already logged (R031, basis of B16).
- No item added: (a) evidence is pre-euro DEM crosses in the EMS band regime, and the mechanism (nonparametric predictor on lagged daily
  returns) is the same family as B62, which E051 just tested (NONE); a k-NN variant on the same dev series would be a re-test that
  adds a trial without a new mechanism. (b) A 1-month lookback is a parameter variant of B16/E019 (12-month, NONE) chosen without
  EUR/USD-specific evidence (lesson at backlog R-note ~line 655). pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure.

### Refill note R215 (not an item; no item added)
- 2026-11-16 R215 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "09:30", "equity open",
  "high-low range" or "Darvas" entry in research/ or knowledge/ before this run): (a) EUR/USD returns around the 09:30 NY US equity
  open; (b) daily high-low range as a next-day direction predictor; (c) long-maturity forward rates. Four standard searches.
  (a) Only Krohn-Mueller-Whelan "Foreign Exchange Fixings and Returns Around the Clock" (BoC SWP 2021-48), already logged; no study of
  the equity open itself. (b) Only vendor/blog pages and Cespa-Gargano-Riddiough-Sarno WP-EMG-01-2021 (re-opened: volume x lagged
  return reversal, family already tested E033, NONE). (c) Opened Darvas-Schepp Bruegel WP 02/2020 abstract (entry in
  research/academic_studies.md): forward-rate error-correction model beats the random walk on 12 pairs; needs forward rates not in the
  repo, monthly-plus horizon below the R090 power floor.
- No item added: (a) no evidence beyond a known logged paper, and an hour-of-day window would re-scan E009 cells; (b) no source;
  (c) data and power. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.

### Refill note R216 (not an item; no item added)
- 2026-11-16 R216 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "ECB speech",
  "Jansen", "Fanta" or "price clustering" entry in research/ or knowledge/ before this run): (a) ECB officials' speeches / verbal
  statements -> intraday EUR/USD drift; (b) price clustering at round numbers in the EUR/USD order book. Two standard searches.
  (a) Opened Jansen & de Haan (2005 WP, full text) and Fanta (IES WP 23/2025, abstract): both find only small, short-lived effects and
  no lasting directional move (entries in research/academic_studies.md). (b) Hits were a tick-size/order-book clustering paper
  (arXiv 1307.5440, not opened, not cited) and equity-market studies; round-number levels are the Osler family already tested (B52).
- No item added: (a) published evidence is null on direction, and statement timestamps are not in the repo; (b) no directional basis
  beyond the B52 family. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.

### Refill note R217 (not an item; no item added)
- 2026-11-16 R217 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "MAX effect",
  "lottery" or "Khurram" entry in research/ or knowledge/ before this run): (a) MAX / extreme-daily-return effect -> next-period
  EUR/USD direction; (b) US Treasury yield changes leading intraday EUR/USD. Two standard searches.
  (a) Opened Khurram-Ali-Jiang-Xie (ERE 2022, doi:10.1080/1331677X.2021.1965000, abstract; entry in research/academic_studies.md):
  Pakistani equities cross-section, no FX. Reading "MAX Momentum" PDF (centaur.reading.ac.uk/99101): host bot-protection refused,
  not circumvented, not cited; other hits (Trier "Maxing out", CEPR DP16128, uwasa, hrcak, AJBA) not opened, not cited.
  Cespa et al. WP-EMG-01-2021 hit already logged (R215). (b) Only broker/news pages and a FRED correlation tool (not evidence, not
  opened); intraday Treasury yields are not in the repo, and the Treasury line was already tested via auctions (E039).
- No item added: (a) no single-currency or EUR/USD evidence; a time-series "large-move" rule on daily EUR/USD would be the
  lagged-return family tested by E033/E050/E051 (all NONE); (b) no source and no data. pytest 454 passed. 0 trials used (dev 261,
  val 9, total 270). Not a pipeline failure.

### Refill note R218 (not an item; no item added)
- 2026-11-16 R218 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles: (a) realized
  semivariance / signed jump variation -> next-day EUR/USD direction; (b) Hurst-exponent / long-memory trend rules on intraday
  EUR/USD. Two standard searches.
  (a) Hits were already logged: Caporin-Shahzad (unipd PDF, R100 note), Babiak-Baruník arXiv:2101.09738 (R161, cross-sectional
  monthly), Lee-Wang 2025 (R088, post-FOMC jumps; tested E040 NONE). Dallas Fed WP 1902 and HAL signed-jumps paper not opened, not
  cited. A daily signed-jump rule would sit in the realized-moment family already tested by E044 (realized skewness, NONE).
  (b) Opened Batten-Ellis-Hogan arXiv math/0412344 (entry in research/academic_studies.md): 6 weeks of AUD/USD quotes 2000,
  hour-of-day Hurst exponents, no trading rule or direction forecast. Other hits (Bitcoin, order-flow long memory, Warwick WP 99-89
  already noted R211, Glasgow thesis, mql5 copy of a vendor PDF) not opened or not evidence, not cited.
- No item added: (a) no new single-currency source; family already tested; (b) descriptive only, sub-hour horizon, no EUR/USD
  rule. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
- Fifth consecutive refill with no item (R214-R218). Per the R217 observation, the next refill should look for a runner-downloadable
  data source not yet in the repo rather than another price-only angle.

### Refill note R219 (not an item; no item added)
- 2026-11-16 R219 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "retail sales" entry
  in research/backlog.md before this run; FRED daily series are a runner-downloadable source not yet used by the repo): (a) US retail
  sales release (08:30 NY) -> later EUR/USD drift; (b) lagged daily VIX / risk-on-off change (FRED VIXCLS) -> next-day EUR/USD. Two
  standard searches. (a) Opened Chaboud et al. FRB IFDP 823 (2004; entry in research/academic_studies.md): EBS EUR/USD 1999-2004,
  retail sales among six releases; the price jump is "generally completed within a few minutes" and later returns are "orthogonal" to
  the surprise. KSSW 2017 appendix already logged (R187 area). (b) Beber risk-on/off ECB workshop slides: permission timeout, not
  read, not cited; other hits (Engel long-horizon papers, Insper/Tsinghua/NSF/JFQA PDFs) not opened, not cited.
- No item added: (a) verified evidence against post-release drift (same as the NFP/CPI release family); (b) no verified lagged
  (predictive) basis. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.

### Refill note R220 (not an item; no item added)
- 2026-11-16 R220 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles: (a) central-bank
  communication blackout (quiet) period -> EUR/USD drift; (b) lagged daily Bitcoin / crypto returns -> next-day EUR/USD. Two standard
  searches. (a) Hits were already logged: Karnaukh "The Dollar Ahead of FOMC Target Rate Changes" (academic_studies.md; R175 note
  covered the FOMC blackout angle); CEPR DP15735 (ECB blackout communication) and Telegin quiet-period PDF not opened, not cited.
  (b) Opened Dimitriadou-Gregoriou (Entropy 2023, doi:10.3390/e25050777) and Pečiulis-Vasiliauskaitė (MSED 2021); entries in
  research/academic_studies.md: both model crypto returns with EUR/USD as a regressor, neither tests crypto -> EUR/USD direction.
  Other hits (CeBER WP, NSF PDF, uma.es, TradingView, Quantpedia) not opened or not evidence, not cited.
- No item added: (a) duplicate of R175; (b) no verified lagged basis (same result as R146-area bitcoin weekend note). pytest 454
  passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Seventh consecutive refill with no item (R214-R220).

### Refill note R221 (not an item; no item added)
- 2026-11-16 R221 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "dollar carry",
  "forward discount" or "Parabolic" entry in research/backlog.md before this run): (a) dollar carry / average forward discount ->
  EUR/USD direction; (b) Parabolic SAR rules on EUR/USD. Two standard searches. (a) Opened Lustig-Roussanov-Verdelhan JFE 2014
  (RePEc abstract + NBER WP 16427; entry in research/academic_studies.md): monthly basket signal, 1-12 month horizons, no EUR/USD-only
  or daily result; needs short rates / forward points not in the repo. (b) Opened Mir Yazdi-Habibi Lashkary 2012 (mql5 mirror of a
  ResearchGate conference paper; entry in academic_studies.md): hourly EUR/USD 2001-2010, +1,459 pips over 4,967 orders (~0.29 pips
  per order gross), no costs, in-sample. Other hits (Quantpedia, CMC Markets, IQ Option, babypips, forum pages) not evidence, not cited.
- No item added: (a) monthly horizon below the R090 power floor and data not in the repo; (b) gross edge far below the SPEC 4 cost
  model, no out-of-sample design. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Eighth
  consecutive refill with no item (R214-R221).

### Refill note R222 (not an item; no item added)
- 2026-11-16 R222 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "retail positioning",
  "tom-next" or "swap point" entry in research/ or knowledge/ before this run): (a) retail-trader positioning (contrarian sentiment
  index) -> EUR/USD direction; (b) quarter-end FX-swap funding pressure / cross-currency basis -> spot EUR/USD. Two standard searches.
  (a) Only DailyFX / TradingView / Yahoo vendor pages (IG client sentiment commentary); not evidence, not opened, not cited; no
  runner-downloadable positioning history. (b) Opened Cerutti-Obstfeld-Zhou NBER conf paper f132236 (2020, ~37% verbatim): monthly
  contemporaneous basis regressions, no spot-return forecast; Krohn-Sushko BIS WP 836 landing page: quarter-end funding shocks ->
  wider spot spreads (liquidity, not returns); PDF permission timeout, not circumvented. Entries in research/academic_studies.md.
- No item added: (a) no study, no data; (b) no verified spot-return basis, and quarter-ends give ~24 dev events (below the R090 power
  floor). pytest 454 passed (after pip install -e ".[dev]"). 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Ninth
  consecutive refill with no item (R214-R222).

### Refill note R223 (not an item; no item added)
- 2026-11-16 R223 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Moreira",
  "volatility-managed" or "EVZ" entry in research/ or knowledge/ before this run): (a) volatility-managed (inverse realized-variance)
  scaling of an FX direction signal; (b) CBOE EuroCurrency volatility index (EVZ) changes -> next-day EUR/USD. Two standard searches.
  (a) Opened Moreira-Muir NBER WP 22208 (entry in research/academic_studies.md): FX evidence is the monthly HML carry basket
  (Lustig et al. 2011), monthly rebalancing, no single-pair or daily result; scaling is a sizing overlay and the alpha for carry
  disappears under common-volatility scaling. (b) Only babypips / broker / V-Lab model pages; no study of EVZ predicting EUR/USD
  returns; not evidence, not cited.
- No item added: (a) monthly basket horizon below the R090 power floor and no surviving signal to scale; (b) no verified predictive
  basis (rule 3). 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Tenth consecutive refill with no item (R214-R223).

### Refill note R224 (not an item; no item added)
- 2026-11-16 R224 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "TD Sequential",
  "DeMark" or "SuperTrend" entry in research/ or knowledge/ before this run): (a) TD Sequential / DeMark exhaustion counts on EUR/USD;
  (b) SuperTrend (ATR trailing-band) trend rule on EUR/USD. Two standard searches.
  (a) Hits were only indicator-formula pages (oxfordstrat, Scribd/mql5/TradeStation copies of DeMark manuals); no study of FX
  profitability; not evidence, not opened, not cited. (b) Only TradingView scripts, a Quantified Strategies blog, broker pages and a
  HackerNoon post; no peer-reviewed or working-paper test; not evidence, not cited.
- No item added: no verified predictive basis for either (rule 3); (b) would also sit in the trend-following / breakout family
  already tested (E048, E049). pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Eleventh
  consecutive refill with no item (R214-R224).

### Refill note R225 (not an item; no item added)
- 2026-11-16 R225 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "BTP" spread-change or
  "Alexandridis" / forecast-combination entry in research/ or knowledge/ before this run): (a) Italy-Germany 10y (BTP-Bund) spread
  changes -> next-day EUR/USD (sovereign-risk channel); (b) cross-currency / multi-predictor daily forecast combinations for EUR/USD.
  Two standard searches. (a) Only ING Think / FXStreet / Seeking Alpha / blog commentary on the same-day correlation; no study of a
  lagged predictive link; not evidence, not opened, not cited. (b) Opened Alexandridis-Panopoulou-Souropanis (J. Forecasting 2024,
  DOI 10.1002/for.3067; entry in research/academic_studies.md): daily one-day-ahead EUR/USD forecasts from 14 lagged cross-market
  predictors, result is a ranking of combination methods, no costs seen; other-currency lags are not among its predictors (FXStreet
  "EUR/GBP predicts" pages were vendor commentary, not cited).
- No item added: (a) no verified predictive basis (rule 3) and no runner-downloadable BTP/Bund yield history in the data pipeline;
  (b) building blocks overlap lagged gold/oil/equity/VIX tests (E041, E042, R219) that lesson R095 says not to queue again, and TED,
  BDI, CRB are not available on the runner. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Twelfth consecutive refill with no item (R214-R225).

### Refill note R226 (not an item; no item added)
- 2026-11-16 R226 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "term spread", "yield curve"
  or "wavelet" entry in research/ or knowledge/ before this run): (a) relative yield-curve slope / daily rate-differential changes ->
  EUR/USD; (b) wavelet / decomposition-based daily direction forecasts and high-frequency price-shock reversals. Four standard searches.
  (a) Opened Chen-Tsang (2011 WP; entry in research/academic_studies.md): monthly CAD/GBP/JPY vs USD, 1-24 month horizons, no EUR,
  out-of-sample "does not consistently outperform" the random walk; daily-differential hits were TradingView/commentary only, not
  cited. (b) Hits were EXFormer (arXiv 2512.12727, already logged, backlog refill note near line 760), EMD + neural-network conference paper
  (fitted ML, no costs, not opened), and Wisniewska 2014 / Caporale-Plastun overreaction papers (already logged, tested E028/E029).
- No item added: (a) monthly horizon below the R090 power floor, no EUR evidence, euro-area yields not on the runner; (b) duplicates
  or fitted-model results with no pre-registrable mechanism. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a
  pipeline failure. Thirteenth consecutive refill with no item (R214-R226).

### Refill note R227 (not an item; no item added)
- 2026-11-17 R227 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "natural gas", "TTF"
  or "cointegration" entry in research/ or knowledge/ before this run): (a) European natural-gas (TTF) price changes -> next-day
  EUR/USD (energy terms-of-trade channel); (b) cointegration / pairs mean reversion between EUR/USD and another USD pair -> EUR/USD
  direction. Two standard searches.
  (a) Hits were FX commentary only (poundsterlinglive, capital.com, FXStreet, FXEmpire, TradingView) and two arXiv papers on Italian
  firm pricing / energy volatility modelling with no FX forecast; not evidence, not cited. TTF prices are also not in the repo or a
  proven runner download.
  (b) halshs-01566803 PDF (Anubis access-denied) and FAU IWF WP 05-2016 (Anubis bot challenge) could not be read, not circumvented,
  not cited; NTNU thesis link redirected to a registration record, not followed. Opened Liu, Chang & Geman (2015, "Intraday Pairs
  Trading Strategies on High Frequency Data: The Case of Oil Companies", https://core.ac.uk/download/42135919.pdf): 5-minute US oil
  stocks, no FX instrument; not relevant to EUR/USD, not logged as evidence.
- No item added: (a) no study, no data; (b) no readable FX pairs-trading evidence, and a two-leg spread is not a single-pair EUR/USD
  direction rule (a one-leg version would be a mechanism invented without evidence; intraday cross-pair lead-lag already searched).
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Fourteenth consecutive refill with no item
  (R214-R227).

### Refill note R228 (not an item; no item added)
- 2026-11-17 R228 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "variance risk premium"
  or "tick imbalance" entry in research/ or knowledge/ before this run): (a) currency / stock variance risk premium -> later EUR/USD
  returns; (b) tick-direction imbalance from high-frequency quotes -> short-horizon EUR/USD direction. Two standard searches.
  (a) Opened Londono-Zhou (FRB IFDP 1068, 2012; entry in research/academic_studies.md): EUR/USD among three pairs, monthly data,
  predictability at 1-6 month horizons, implied vol from JP Morgan OTC options; no costs seen.
  (b) Hits were older NBER/MPRA microstructure working papers (order flow with dealer data, not opened) and Guyard-Deriaz (arXiv
  2409.04471, abstract opened; entry in research/academic_studies.md): fitted ML daily direction, one-year return, no mechanism.
- No item added: (a) horizon below the R090 power floor and FX implied volatility not in the data pipeline; (b) no study of
  quote-tick imbalance as a predictor was found (Dukascopy tick-count imbalance would be a mechanism invented without evidence), and
  the ML hit duplicates the E050/E051 family. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Fifteenth consecutive refill with no item (R214-R228).

### Refill note R229 (not an item; no item added)
- 2026-11-17 R229 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Kaufman", "adaptive
  moving" or "Aroon" entry in research/ or knowledge/ before this run): (a) Kaufman adaptive moving average / efficiency-ratio trend
  rules on EUR/USD; (b) Aroon / CCI directional-indicator rules on EUR/USD. Two standard searches.
  (a) Hits: PMC5004863 (adjustable moving averages, ASEAN-5 currencies per its title) could not be opened (fetch permission timeout),
  not cited; an MQL5 forum PDF on a fractal adaptive MA for EURUSD (vendor/forum, not evidence, not opened); other hits generic
  technical-rule surveys already in the TA family (Neely-Weller, B16). No KAMA/efficiency-ratio study on EUR/USD with costs found.
  (b) Opened Shah (2024, HKUST student report; entry in research/academic_studies.md): hourly 2022-2024, regression channel + Aroon
  filter, long-only, parameters grid-searched on the reported window, no holdout, costs unquantified.
- No item added: (a) no readable evidence; (b) in-sample student work with no mechanism and no out-of-sample result; a pre-registered
  version would be a mechanism invented without evidence and overlaps the TA-rule family already NONE (E019, E047-E049). pytest 454
  passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Sixteenth consecutive refill with no item (R214-R229).

### Refill note R230 (not an item; no item added)
- 2026-11-17 R230 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "financial stress",
  "NFCI", "STLFSI", "Treasury General Account" or "dollar liquidity" entry in research/ or knowledge/ before this run): (a) financial
  stress / financial-conditions indices -> later EUR/USD returns; (b) Fed reserves / US bank dollar-liquidity -> EUR/USD. Two
  standard searches.
  (a) Opened Fossati-Lu (U. Alberta WP 2025-06; entry in research/academic_studies.md): weekly NFCI vs nine USD rates incl. EUR,
  OOS 2000-2021; no point-forecast gain over the random walk, NFCI informs uncertainty not direction; no costs.
  (b) Opened Bianchi-Bigio-Engel (NBER WP 29457; entry in research/academic_studies.md): monthly, contemporaneous liquidity-ratio
  regressions, euro included; no lagged or out-of-sample test. Other hits (vendor/news pages on TGA/reserves, MNI, tradingeconomics)
  not evidence, not cited.
- No item added: (a) the study itself finds no directional predictability (a direction test would contradict its evidence; the
  volatility angle is covered by E008); (b) contemporaneous monthly relation, below the R090 power floor and no lagged basis
  (lesson R095). pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Seventeenth consecutive refill
  with no item (R214-R230).


### Refill note R231 (not an item; no item added)
- 2026-11-17 R231 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "ECB account",
  "triple witching" or "OPEX" entry in research/ or knowledge/ before this run): (a) ECB monetary-policy accounts releases -> EUR/USD;
  (b) quarterly equity/futures expiration ("triple witching") -> EUR/USD direction. Two standard searches.
  (a) Hits were ECB-communication papers already logged (CEMLA 2025 ECB communication PDF, IES WP 23/2025, Altavilla et al. 2019
  EA-MPD) or vendor/news pages (XTB); no study of the accounts release itself on EUR/USD direction found.
  (b) Hits were equity-only expiration studies (FAJ 1987 program trading), FX option-expiry news/vendor pages (option-expiry pinning
  already covered R108/R136/R164) and CESifo WP 9360, which could not be opened (redirect to ifo.de refused by fetch permission,
  not circumvented): title and content UNVERIFIED, not cited.
- No item added: (a) no evidence beyond the ECB-communication family already logged; (b) no readable FX study. pytest 454 passed.
  0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Eighteenth consecutive refill with no item (R214-R231).

### Refill note R232 (not an item; no item added)
- 2026-11-17 R232 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "VPIN" or
  "triangular" entry in research/ or knowledge/ before this run): (a) VPIN / order-flow toxicity -> later EUR/USD direction;
  (b) triangular-arbitrage deviations (EUR/USD vs implied cross) -> later EUR/USD returns. Two standard searches.
  (a) Opened Andersen-Bondarenko JFM 2014 (DOI 10.1016/j.finmar.2013.05.005, abstract; entry in research/academic_studies.md):
  VPIN is a volatility measure, and a poor one ("poor predictor of short run volatility"); no direction test. Other hits (Easley et
  al. RFS 2015 IDEAS page, Journal of Risk pages, scribd copy) not opened, not cited.
  (b) Opened Fenn et al. arXiv 0812.0913 (full text; entry in research/academic_studies.md): EUR/USD triangles, mispricings mostly
  <= 1 second and small; market "internally self-consistent"; no directional test. Other hits (HAL 02512423 wavelet paper, EUR thesis)
  not opened, not cited.
- No item added: (a) volatility-only, disputed, and tick-volume intensity family already tested (E033); (b) sub-second horizon far
  below 5-minute bars, no directional evidence. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Nineteenth consecutive refill with no item (R214-R232).

### Refill note R233 (not an item; no item added)
- 2026-11-17 R233 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Caldara" or
  "self-exciting" entry in research/ or knowledge/ before this run): (a) Caldara-Iacoviello geopolitical risk (GPR) index -> later
  EUR/USD; (b) Hawkes / self-exciting event clustering -> intraday EUR/USD direction. Two standard searches.
  (a) Opened Iyke-Phan-Narayan IRFA 2022 (DOI 10.1016/j.irfa.2022.102099, abstract only; entry in research/academic_studies.md):
  17 currencies, out-of-sample and trading gains claimed, but frequency, EUR/USD coverage, horizon and costs UNVERIFIED (full text
  subscriber-only). Salisu et al. GPR stock-return paper opened: monthly GPR, 6-24 month horizons, no FX.
  (b) Opened Rambaldi-Pennesi-Lillo arXiv 1405.6047 and Lallouache-Challet arXiv 1406.3967: EBS EUR/USD quote/trade intensity only,
  no direction test.
- No item added: (a) no verified daily EUR/USD design (a daily-GPR item would be a design of our own on abstract-only evidence; monthly
  is below the R090 floor); (b) activity, not direction. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a
  pipeline failure. Twentieth consecutive refill with no item (R214-R233).

### Refill note R234 (not an item; no item added)
- 2026-11-17 R234 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "TIC" or "cross-border
  merger" entry in research/ or knowledge/ before this run): (a) US Treasury International Capital (TIC) monthly release (16:00 NY) ->
  later EUR/USD drift; (b) cross-border M&A flows -> EUR/USD. Two standard searches plus one follow-up.
  (a) Hits were Treasury press releases (not evidence). Opened Schmidt-Silvestrini-Szczerbowicz BdF WP 1040 (2026; entry in
  research/academic_studies.md): TIC used as monthly flow series, no release-event or FX-return test. Opened Simpson-Ramchander-Chaudhry
  JIMF 2005 (DOI 10.1016/j.jimonfin.2005.04.005, abstract only): contemporaneous surprise response, TIC inclusion and drift UNVERIFIED;
  full text refused by fetch permission. Other hits (FRB IFDP 823/784, BIS WP 626, LSE DP 475) already in the release-time family or not opened.
  (b) Top hit Riddiough-Zhang "Cross-Border M&A Flows" already logged (R194); other hits theses / not opened, not cited.
- No item added: (a) no evidence that TIC releases move EUR/USD, let alone a later drift; monthly event count (~70 dev releases) also
  near the R090 power floor; (b) duplicate of R194. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline
  failure. Twenty-first consecutive refill with no item (R214-R234).

### Refill note R235 (not an item; no item added)
- 2026-11-17 R235 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "sovereign rating",
  "Elliott" or "harmonic" entry in research/ or knowledge/ before this run): (a) euro-area sovereign credit rating announcements ->
  later EUR/USD drift; (b) harmonic (Gartley/bat/crab) and Elliott-wave pattern rules -> EUR/USD. Two standard searches.
  (a) Opened Afonso-Furceri-Gomes (UC3M author PDF; entry in research/academic_studies.md): daily bond spreads, CDS and equities only,
  reaction "within one to two days", no exchange-rate test. ECB WP 1347 not openable (fetch permission timeout), not cited. Other hits
  (DIW record, econpapers, FXStreet news on the 2025 US downgrade) not opened or news only. Euro-area rating events are also mostly
  released after the Friday close and few in dev 2016-2020 (below the R090 power floor).
  (b) Opened HKUST student report (hourly EUR/USD 2017-2021, in-sample, no costs: ~3 Gartley signals/year, "low profitability") and
  NU thesis record (Elliott wave: no significant predictive power for daily FX; PDF restricted).
- No item added: (a) no FX evidence and too few dev events; (b) negative/in-sample evidence only and signals too rare.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Twenty-second consecutive refill with no
  item (R214-R235).

### Refill note R236 (not an item; no item added)
- 2026-11-17 R236 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "point and figure"
  or "pin bar" entry in research/ or knowledge/ before this run): (a) point-and-figure charting rules -> EUR/USD; (b) pin-bar /
  single-candle price-action patterns -> EUR/USD. Two standard searches; records opened via web-fetch (entries in research/academic_studies.md).
  (a) Only study found: Anderson-Faff IRFA 2008, S&P 500 futures, no FX test; other hits forum-hosted copies of the same paper, not opened.
  (b) Orquín-Serrano Mathematics 2020 (doi:10.3390/math8050802), EUR/USD only, out-of-sample with costs: "No net positive average
  returns ... after taking into account transaction costs." Alanazi 2020 EJF hit is a duplicate of R142. Other hits vendor/blog pages.
- No item added: (a) no FX evidence; (b) negative evidence after costs on EUR/USD itself, and candlestick / fitted-ML family already NONE.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Twenty-third consecutive refill with no
  item (R214-R236).

### Refill note R237 (not an item; no item added)
- 2026-11-17 R237 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Vortex", "Chaikin"
  or "VSTOXX" entry in research/ or knowledge/ before this run): (a) Vortex indicator / Chaikin Money Flow rules -> EUR/USD;
  (b) lagged VSTOXX (euro-equity implied vol) -> next-day EUR/USD. Two standard searches.
  (a) Only candidate study: a theses.cz bachelor thesis PDF, blocked by a JavaScript bot check (not circumvented, not cited). Other
  hits TradingView/vendor pages (BTC, no study). (b) Hits were broker/news commentary; opened Ornelas-Maaud BCB WP 492 (entry in
  research/academic_studies.md): FX-option implied-vol term-structure slope, 3-6 month horizons, no equity-vol predictor.
- No item added: (a) no openable evidence; Chaikin needs real volume (tick-volume family already tested E033); (b) no verified
  daily equity-vol -> EUR/USD evidence; the cited paper is FX-option data at 3-6 month horizons, below the R090 floor and not in the
  pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Twenty-fourth consecutive refill
  with no item (R214-R237).

### Refill note R238 (not an item; no item added)
- 2026-11-17 R238 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "debt ceiling" or
  "G7" entry in research/ or knowledge/ before this run): (a) US debt-ceiling / shutdown resolutions -> later EUR/USD drift;
  (b) G7 communiqué / official FX statements -> later EUR/USD drift. Two standard searches.
  (a) Opened Nippani JAF 2016 (entry in research/academic_studies.md): one 2013 episode, daily closes, same-day move only, no drift
  test; other hits FX news/broker commentary (not cited). (b) Fratzscher ECB WP 952 not openable (fetch permission timeout after
  redirect to ecb.europa.eu), not cited; other hits (econpapers, Dallas Fed WPs) not opened.
- No item added: (a) single-event evidence and too few dev 2016-2020 events (below the R090 power floor); (b) no openable evidence,
  and G7 FX statements are rare after 2013 (also below the floor). pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Twenty-fifth consecutive refill with no item (R214-R238).

### Refill note R239 (not an item; no item added)
- 2026-11-17 R239 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "FOMC minutes" or
  "Fed minutes" entry in research/ or knowledge/; ZEW/Ifo only mentioned in passing): (a) FOMC minutes release (14:00 NY) -> later
  EUR/USD drift; (b) German Ifo / ZEW releases -> later EUR/USD drift. Two standard searches.
  (a) Opened Rosa FRBNY EPR 2013 (entry in research/academic_studies.md): volatility/volume only, no sign, effect within ~1 h and
  declining since 2008; other hits Dukascopy market-news pages (not cited). (b) Mannheim DP 09-010 PDF behind an Anubis bot check
  (not circumvented, not cited); other hits news/broker pages.
- No item added: (a) no directional evidence and ~40 dev events (below the R090 power floor); (b) no openable evidence, monthly
  events (~60 dev dates per survey) also near or below the floor. pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Twenty-sixth consecutive refill with no item (R214-R239).

### Refill note R240 (not an item; no item added)
- 2026-11-17 R240 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "permutation entropy",
  "market efficiency", "Levich" or "filter rule" entry in research/ or knowledge/ before this run): (a) entropy / time-varying
  efficiency measures as a regime filter for EUR/USD direction; (b) adaptive-markets / episodic predictability of daily FX returns.
  Two standard searches; entries in research/academic_studies.md.
  (a) Opened Tokar-Horvath arXiv 1110.2612: EUR/USD 1-minute 2004-2009, in-sample trend-sign statistics, contrarian beats trend,
  no trading rule, returns or costs. PMC7512194 (multiscale entropy) not openable (fetch permission timeout), not cited.
  (b) Opened Levich-Potì (IJF forthcoming 2013 version, ~42% verbatim): excess predictability episodic; daily strategies negative
  at 5 bp costs for all six currencies; only monthly survives costs.
- No item added: (a) no out-of-sample or cost-aware evidence, and short-horizon reversal is already logged and tested; (b) daily
  evidence is negative after costs, monthly is below the R090 power floor, and fitted lagged-return models were NONE (E051).
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Twenty-seventh consecutive refill with no
  item (R214-R240).

### Refill note R241 (not an item; no item added)
- 2026-11-17 R241 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "real yield",
  "TIPS" or "cross-rate" entry in research/ or knowledge/ before this run): (a) US real-yield (TIPS / linker) daily changes ->
  next-day EUR/USD; (b) intraday lead-lag from equity index futures -> EUR/USD. Two standard searches; entries in
  research/academic_studies.md.
  (a) Opened Clarida NBER WP 18726: daily EUR/USD vs linker yields, contemporaneous only, explicitly no causal or lagged inference,
  no out-of-sample test; other hits FX commentary (not cited). (b) Opened Canto-Kräussl CFS WP 2006/25 (equity futures, spillovers
  vanish within 5 minutes, costs likely offset) and Huth-Abergel arXiv 1111.7103 (equity tick lead/lag, unprofitable after spread);
  no FX lead-lag evidence found.
- No item added: (a) no lagged directional evidence, and real-yield data are not in the pipeline; (b) no FX evidence and the
  equity results are seconds-to-minutes effects that do not survive spread. pytest 454 passed. 0 trials used (dev 261, val 9,
  total 270). Not a pipeline failure. Twenty-eighth consecutive refill with no item (R214-R241).

### Refill note R242 (not an item; no item added)
- 2026-11-17 R242 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles: (a) central-bank
  speeches (ECB/Fed, outside meeting days) -> later EUR/USD drift; (b) US Treasury auction results -> intraday USD reaction. Two
  standard searches. (a) Only relevant hit was the IES WP 23/2025 EUR/USD CB-communication event study, already logged in
  research/academic_studies.md; other hits not FX-intraday or already covered. (b) Opened Fleming-Liu-Nguyen FRBNY SR 1188 (entry
  in research/academic_studies.md): Treasury-yield inverted-V of 0.7-1.2 bp around auctions, no FX returns.
- No item added: (a) no new evidence beyond what is logged; (b) no EUR/USD evidence (same conclusion as R123), and an auction-day
  calendar would need a new data download. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Twenty-ninth consecutive refill with no item (R214-R242).

### Refill note R243 (not an item; no item added)
- 2026-11-17 R243 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "SLOOS" / "bank
  lending survey" or euro-area balance-of-payments release entry in research/ or knowledge/ before this run): (a) ECB Bank Lending
  Survey / Fed SLOOS release -> later EUR/USD drift; (b) ECB monthly euro-area balance-of-payments / current-account release ->
  EUR/USD. Two standard searches. (a) Hits were papers on FX -> bank lending (wrong direction) and news pages (MNI, Saxo, Continuum;
  not evidence, not opened); opened Meisenzahl-Niepmann-Schmidt-Eisenlohr FEDS 2025-046 (entry in research/academic_studies.md):
  ECB surprises -> US loan spreads, no survey-release or FX-return test. (b) Returned only ECB / Banque de France press releases; no study.
- No item added: no EUR/USD evidence for either angle; both would also need a new release-calendar download and are ~4 (BLS) or
  ~12 (BoP) events a year, below the lesson-R090 power floor on dev. pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Thirtieth consecutive refill with no item (R214-R243).

### Refill note R244 (not an item; no item added)
- 2026-11-17 R244 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "closing auction",
  "MOC" or "14:00 CT" settlement entry in research/ or knowledge/ before this run): (a) US equity closing-auction / end-of-day
  equity hedging flows -> EUR/USD around 16:00 NY; (b) CME FX futures daily settlement window -> EUR/USD spot pressure. Two
  standard searches. (a) Hits were Krohn-Mueller-Whelan (BoC SWP 2021-48), Melvin-Prins (2015) and Marsh-Miao (2012), all already
  logged in research/academic_studies.md; no new study. (b) Returned only CME product/fixing pages and vendor pages (not evidence,
  not opened); no study.
- No item added: no new EUR/USD evidence for either angle. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a
  pipeline failure. Thirty-first consecutive refill with no item (R214-R244).

### Refill note R245 (not an item; no item added)
- 2026-11-17 R245 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "sovereign spread",
  "redenomination", "SOFR" or "dollar factor" entry in research/ or knowledge/ before this run): (a) euro-area sovereign spread
  (BTP-Bund) changes / redenomination risk -> next-day EUR/USD; (b) USD funding-stress indicators (SOFR spikes, FRA-OIS) -> EUR/USD.
  Two standard searches. (a) Only study hit, the CEPR/VoxEU column on Italian fiscal vs redenomination risk, failed to open (client
  error), not cited; other hits bank/FX commentary (ING, FXStreet; not evidence, not opened). (b) Opened Ostry Janeway WP 2311 (entry
  in research/academic_studies.md): monthly/3-month quantile UIP, in-sample, no daily horizon or costs; other hits glossary/vendor pages.
- No item added: no verified lagged daily/intraday EUR/USD evidence for either angle, and BTP-Bund or SOFR data are not in the pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Thirty-second consecutive refill with no
  item (R214-R245).

### Refill note R246 (not an item; no item added)
- 2026-11-17 R246 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Sintra",
  "Treasury refunding" or "QRA" entry in research/ or knowledge/ before this run): (a) US Treasury Quarterly Refunding Announcement
  -> USD / EUR/USD reaction; (b) ECB Sintra Forum / Jackson Hole symposium speeches -> EUR/USD. Two standard searches. (a) Hits were
  news/commentary pages only (Newsquawk, Marc to Market, BabyPips, MarketPulse, FXStreet, Euronext/MNI; not evidence, not opened);
  no study. (b) Only study hit was the VoxEU column on Comazzi et al. ECB exchange-rate communication, already logged in
  research/academic_studies.md (R161); other hits commentary or ECB author profile pages.
- No item added: no new EUR/USD evidence for either angle; both are ~1-4 events a year, below the lesson-R090 power floor on dev,
  and the refunding calendar is not in the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline
  failure. Thirty-third consecutive refill with no item (R214-R246).

### Refill note R247 (not an item; no item added)
- 2026-11-17 R247 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "survey
  expectation", "forecaster" or "carry trade unwind" entry in research/ or knowledge/ before this run): (a) professional / consensus
  FX forecasts -> EUR/USD returns; (b) carry-trade unwind (JPY funding shocks) -> next-day EUR/USD. Two standard searches.
  (a) Opened Ballensiefen-Somogyi-Winterberg CFR WP 26-04 (entry in research/academic_studies.md): monthly G10 panel, 24-month
  horizon, in-sample, no costs; Kiel Institute page ("Are consensus FX forecasts valuable for investors") redirected and the redirect
  could not be opened (permission timeout), not cited. (b) Only study hits were jump papers already logged (Lee et al., Erdemlioglu
  et al.) or not specific to carry unwinds; other hits commentary (FXStreet, Advisor Perspectives, Swissquote; not evidence, not opened).
- No item added: no verified daily/intraday EUR/USD evidence for either angle, and Consensus Economics data is not in the pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Thirty-fourth consecutive refill with no
  item (R214-R247).

### Refill note R248 (not an item; no item added)
- 2026-11-17 R248 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Wikipedia" or
  "Parkinson" entry in research/ or knowledge/ before this run): (a) Wikipedia page-view attention -> EUR/USD returns; (b) daily
  high-low range (range-based volatility) -> next-day EUR/USD direction. Two standard searches. (a) Opened two abstract pages
  (Pyun Econ. Letters 2024; Hervé-Zouaoui-Belvaux Econ. Modelling 2019; entries in research/academic_studies.md): equities only,
  no FX test; the one FX attention paper they cite (Han-Xu-Yin 2018) is already logged (volatility, weekly, no direction result).
  (b) Hits were vendor/forum/blog pages only (NumXL, MQL5, Forex Peace Army, Scribd, Dummies, FXStreet; not evidence, not opened).
- No item added: no verified EUR/USD evidence for either angle, and Wikipedia page-view data is not in the pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Thirty-fifth consecutive refill with no
  item (R214-R248).

### Refill note R249 (not an item; no item added)
- 2026-11-17 R249 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "durable goods",
  "Euro VIX" or "Hibbert" entry in research/ or knowledge/ before this run): (a) US durable goods orders release (08:30 NY) -> later
  EUR/USD drift; (b) Cboe EuroCurrency volatility index (EVZ) changes -> next-day EUR/USD direction. Two standard searches.
  (a) Hits were news pages only (Dukascopy market-news, FXStreet; not evidence, not opened); no study. (b) Opened the abstract of
  "Examining the Return-Volatility Relation for Foreign Exchange: Evidence from the Euro VIX" (JFM 2012; entry in
  research/academic_studies.md): FXE ETF vs EVZ, contemporaneous relation only, no predictive test; other hits vendor/glossary pages.
- No item added: no verified lagged EUR/USD evidence for either angle, and EVZ / release-calendar data are not in the pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Thirty-sixth consecutive refill with no
  item (R214-R249).

### Refill note R250 (not an item; no item added)
- 2026-11-17 R250 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "flash PMI",
  "EUR/CHF safe haven" or "Leutert" entry in research/ or knowledge/ before this run): (a) euro-area / US flash PMI releases ->
  later EUR/USD drift; (b) lagged EUR/CHF (safe-haven) returns -> next-day EUR/USD direction. Two standard searches.
  (a) Hits were news/commentary pages only (Dukascopy market-news, Newsquawk, FXStreet, BabyPips; not evidence, not opened); no study.
  (b) Opened Leutert SJES 2018 doi:10.1186/s41937-017-0014-7 (entry in research/academic_studies.md): monthly, contemporaneous
  CHF-equity covariances, no EUR/USD or predictive test; other hits broker/commentary pages.
- No item added: no verified lagged EUR/USD evidence for either angle, and a PMI release calendar is not in the pipeline (B6 blocker).
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Thirty-seventh consecutive refill with no
  item (R214-R250).

### Refill note R251 (not an item; no item added)
- 2026-11-18 R251 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Monday effect",
  "Bush" or "Cellini" entry in research/ or knowledge/ before this run): (a) Monday effect / day-of-week returns in EUR/USD;
  (b) quarter-end rebalancing flows -> EUR/USD. Two standard searches. (a) Opened two abstract pages (Bush-Stephens JBEF 2016
  doi:10.1016/j.jbef.2016.03.003; Cellini-Cuccia AFE 2014 doi:10.1080/09603107.2013.870651; entries in research/academic_studies.md):
  in-sample, regime-dependent or unnamed day/month cells, no magnitudes, no out-of-sample or cost test; day-of-week cells already
  scanned on dev (E009), weekend reversal tested (E020 NONE). (b) Hits were broker/vendor/news pages only (TradingView, FXEmpire,
  Tickmill, BNY iFlow, Pound Sterling Live; not evidence, not opened) and an IMF WP not opened; month-end windows already tested (E034).
- No item added: no verified out-of-sample EUR/USD evidence for either angle, and both are subsets of calendar cells already seen
  on dev. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Thirty-eighth consecutive refill
  with no item (R214-R251).

### Refill note R252 (not an item; no item added)
- 2026-11-18 R252 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "asset purchase",
  "ECB QE", "Japanese investors" or "Japan fiscal" entry in research/ or knowledge/ before this run): (a) ECB asset-purchase (QE)
  announcements -> later EUR/USD drift; (b) Japanese fiscal-year-end repatriation flows -> EUR/USD. Two standard searches.
  (a) Opened Uz Akdogan Empirica 2023 doi:10.1007/s10663-023-09578-9 (entry in research/academic_studies.md): HUF/PLN/TRY daily,
  domestic QE announcements in 2020, contemporaneous windows only, no EUR/USD or drift test; other hits (ECB speech, Bundesbank
  Monthly Report, CEPR DP14324, university repositories) not opened, not cited. (b) Hits were news/commentary pages only
  (investingLive/ForexLive, FXStreet, Pound Sterling Live, FX Week; not evidence, not opened); no study.
- No item added: no verified lagged EUR/USD evidence for either angle; ECB QE announcements on dev number roughly a dozen and the
  Japanese fiscal year end gives ~6 dev events, both far below the R090 power floor. pytest 454 passed. 0 trials used (dev 261,
  val 9, total 270). Not a pipeline failure. Thirty-ninth consecutive refill with no item (R214-R252).

### Refill note R253 (not an item; no item added)
- 2026-11-18 R253 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Ehlers",
  "Hilbert", "Ornstein" or "half-life" entry in research/ or knowledge/ before this run): (a) Ehlers / Hilbert-transform
  dominant-cycle indicators -> EUR/USD; (b) Ornstein-Uhlenbeck / z-score intraday mean reversion on EUR/USD. Two standard searches.
  (a) Hits were MQL5 forum/articles, TradeStation tutorial, TradingView scripts, WH SelfInvest strategy page and the indicator
  author's own mesasoftware.com notes (not evidence, not opened, not cited); no study. (b) Opened Sun, WNE UW WP 20/2025 (daily
  equity pairs, Renko/Kagi, no FX) and Holý-Tomanová arXiv 1811.09312 (tick OU estimation, NYSE oil stocks, no FX); entries in
  research/academic_studies.md. Other hits (arXiv 1303.7177 market-making, core.ac.uk, FAU, dergipark, arXiv 2412.12458 pairs)
  not opened, not cited.
- No item added: no verified EUR/USD evidence for either angle; a single-pair intraday reversion rule would overlap fade/reversal
  tests already run. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Fortieth consecutive
  refill with no item (R214-R253).

### Refill note R254 (not an item; no item added)
- 2026-11-18 R254 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "open interest",
  "abnormal volume" or "trading volume" entry in research/ or knowledge/ before this run): (a) abnormal FX trading volume ->
  next-day / intraday EUR/USD direction; (b) currency-futures open-interest changes -> later EUR/USD. Two standard searches.
  (a) The only study hit was Cespa-Gargano-Riddiough-Sarno "Foreign Exchange Volume" (CEPR DP16128, RFS 2022
  doi:10.1093/rfs/hhab095; CEPR and Cambridge repository abstract pages opened): next-day reversal stronger after abnormally low
  volume. Already in research/academic_studies.md and already tested as B28/B29 in E033 (NONE/NONE on dev). Other hits
  (thefullfx.com, CXO Advisory, VoxEU column) not evidence, not opened. (b) Opened Hong-Yogo NBER WP 16712 (entry in
  research/academic_studies.md): monthly, 12-month smoothed open-interest growth, foreign-currency portfolio vs USD, weaker for
  currencies than commodities, in-sample. Other hits (Bundesbank DP, RBA RDP 2004-07, NY Fed EPR/SR 262 on COT positioning)
  not opened; COT positioning already closed (R082, R120).
- No item added: (a) duplicates E033; (b) monthly horizon gives ~72 dev observations, far below the R090 power floor, and CME
  open-interest data are not in the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline
  failure. Forty-first consecutive refill with no item (R214-R254).

### Refill note R255 (not an item; no item added)
- 2026-11-18 R255 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "election"
  match in this file; "CNH"/"yuan" only incidental): (1) elections -> later EUR/USD drift; (2) PBoC daily USD/CNY fixing
  surprise -> EUR/USD spillover.
- (1) Opened: Jantke de Boer & Eichler (2025), ESRB workshop paper
  https://www.esrb.europa.eu/news/schedule/2025/pdf/2025-06-30-awg-mpag8-annual-workshop-session-3-paper-stefan-eichler-jantke-de-boer.pdf
  : 71 emerging-market currencies (no euro), 15-minute windows on US debate nights 1996-2016, contemporaneous reaction only, no
  drift, out-of-sample or cost test. Aizenman & Saadaoui (2024, rev. 2025), NBER WP 33193
  https://www.nber.org/system/files/working_papers/w33193/w33193.pdf : 2024 US election, 73 USD pairs with the euro explicitly
  excluded, cross-sectional in-sample regressions on 1-day/4-day/1-week moves, no sign prediction, no costs.
- (2) Search returned only broker explainers and newswire fixing headlines (forex.com, newsquawk); no study opened, nothing cited.
- No item added: (a) no study tests EUR/USD direction after elections; (b) national elections relevant to EUR/USD in dev
  2015-2020 number well under 20 events, far below the R090 power floor; (c) no evidence for the fixing angle and CNY fixing
  data are not in the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Forty-second consecutive refill with no item (R214-R255).

### Refill note R256 (not an item; no item added)
- 2026-11-18 R256 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "industrial
  production", "Dobrev" or "Bund future" entry in research/ or knowledge/ before this run): (a) euro-area / German industrial
  production release -> later EUR/USD drift; (b) intraday bond-futures (Treasury / Bund) lead-lag -> EUR/USD. Two standard searches.
  (a) Hits were FXStreet release headlines only (not evidence, not opened, not cited); no study. (b) Opened Dobrev-Schaumburg
  (2018) working paper (entry in research/academic_studies.md): Treasury and equity cash-vs-futures, lead-lag at ~5 ms, no
  minute-plus directional or cost test. Krohn-Vala-Uthemann-Yang BoC SWP 2025-29 hit is already logged (B-line at backlog l.754).
  Other hits (AgEcon Monash 185, AEA 2018 preliminary paper, Frankfurt OPUS, eflab event, Eurex hedging note) not opened, not cited.
- No item added: (a) no verified EUR/USD drift evidence; (b) the documented lead is milliseconds, below the 1-minute bar resolution
  and inside the SPEC 4 spread, and bond-futures data are not in the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9,
  total 270). Not a pipeline failure. Forty-third consecutive refill with no item (R214-R256).

### Refill note R257 (not an item; no item added)
- 2026-11-18 R257 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "minute-of-hour",
  "top of the hour" or "reinforcement" entry in research/ or knowledge/ before this run): (a) minute-of-hour / top-of-hour intraday
  seasonality in EUR/USD returns; (b) deep reinforcement learning intraday EUR/USD trading. Two standard searches.
  (a) Opened Cotter-Dowd arXiv 1103.5664: one week of 1997 DEM/USD, 3-hour GMT blocks, volatility/tail seasonality only, no
  minute-of-hour or direction test. Ito-Hashimoto NBER w12413 hit already logged. (b) Opened Huang arXiv 1807.02787: DRQN on 15-minute
  bars incl. EUR/USD 2012-2017, online training without held-out test, spreads 0.08-0.2 bp; EUR/USD ~0.1% annualised at 0.15 bp.
  Other hits (arXiv 2410.23294, 1411.2153, 2007.15982, 2110.04745, TU Delft, JBS wp0030, dekalog blog) not opened, not cited.
  Entries in research/academic_studies.md.
- No item added: (a) no verified return/direction effect at minute-of-hour resolution; (b) the only EUR/USD evidence vanishes at
  spreads far below SPEC 4 costs, has no out-of-sample split, and the ML-on-lags family is already NONE (E051). pytest 454 passed.
  0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Forty-fourth consecutive refill with no item (R214-R257).

### Refill note R258 (not an item; no item added)
- 2026-11-18 R258 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Caixin", "China PMI"
  or "nowcast" entry in research/ or knowledge/ before this run): (a) Chinese macro releases (PMI, output) -> EUR/USD; (b) macro
  nowcast / fundamentals-based short-run EUR/USD forecasting. Two standard searches.
  (a) Opened Baum-Kurov-Wolfe JIMF 2015 doi:10.1016/j.jimonfin.2015.07.002: 5-minute euro FX futures 2009-2013, contemporaneous
  surprise reaction within ~20 minutes, no drift, no out-of-sample or cost test. (b) Opened Dal Bianco-Camacho-Pérez Quirós BdE WP
  1203 (2012) page: mixed-frequency fundamentals model, weekly EUR/USD, out-of-sample gains over random walk reported (summary only,
  UNVERIFIED verbatim), no costs. Other hits (marketpulse, FXStreet, newsquawk, financemagnates, IMF WP 2025/133, Cardiff ORCA,
  Brunel, appstate/St Louis Fed Taylor-euro copies (Molodtsova et al. already logged R171), BBVA WP 1201, MQ WP 16-07, UAlberta
  WP 2025-06 (already logged R230), WEF) not opened or already logged, not cited. Entries in research/academic_studies.md.
- No item added: (a) needs consensus-surprise data not in the repo and shows only a minutes-long contemporaneous reaction; (b) needs
  a real-time US/euro-area macro panel with no sanctioned runner download path (same blocker as B12). pytest 454 passed. 0 trials
  used (dev 261, val 9, total 270). Not a pipeline failure. Forty-fifth consecutive refill with no item (R214-R258).

### Refill note R259 (not an item; no item added)
- 2026-11-18 R259 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "disposition" or
  "order book imbalance" entry in research/ or knowledge/ before this run): (a) FX traders' disposition effect / capital-gains overhang
  -> EUR/USD; (b) limit-order-book imbalance -> short-horizon EUR/USD direction. Two standard searches.
  (a) Opened Heimer-Imas AEA 2019 preliminary paper "Doing Less with More": retail myForexBook traders 2010, CFTC leverage cap reduces
  disposition effect ~13% and raises per-trade timing returns 1.9 bp; no exchange-rate predictability test. (b) Opened Kozhan-Moore-
  Payne 2012 (BoC conference PDF): Reuters D3000 2003-2004, daily/hourly contemporaneous order-flow price impact, no forecast test.
  Other hits (core.ac.uk 13240855, typeset prospect-theory PDF, JFQA dynamic loss aversion, Tsinghua PDF, arXiv 2507.22712 / 2508.06788,
  NBER w12682, NBER f121921, AEA 2009 pdfid 301, medium/emergentmind/nestegg/mql5/substack pages) not opened, not cited. Xu-Kozhan-Taylor
  prospect-theory paper already logged (academic_studies.md ~l.550). Entries in research/academic_studies.md.
- No item added: (a) trader behaviour/performance only, no verified EUR/USD price pattern, retail position data not in the pipeline;
  (b) contemporaneous only, and order-book data are not in the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Forty-sixth consecutive refill with no item (R214-R259).

### Refill note R260 (not an item; no item added)
- 2026-11-18 R260 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "stress test" or
  "transformer" entry in research/ or knowledge/ before this run): (a) Fed bank stress-test results release -> later EUR/USD drift;
  (b) transformer / attention models for EUR/USD return forecasting. Two standard searches.
  (a) No FX event study on stress-test releases among hits (Columbia monetary-policy-uncertainty PDF, NY Fed SR744, FEDS 2021-012,
  St. Gallen WPF-1814, FMG dp-54, Boston Fed ppb137, KC Fed RWP 22-01, newswire release-date page); none opened, not cited.
  (b) Opened Liu-Ślepaczuk-Tang arXiv 2512.12727 (EXFormer): daily EUR/USD/JPY/GBP 2010-2024, post-cost cumulative ~7% for EUR/USD on
  the test block, input window chosen on test outcomes. Other hits (SSRN 7405518 mirror, preprints.org 202509.0931, MDPI JRFM 19/3/203,
  emergentmind pages) not opened, not cited. Entry in research/academic_studies.md.
- No item added: (a) no verified EUR/USD basis; (b) daily horizon, test-block selection, and the ML-on-lags family is already NONE
  (E051). 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Forty-seventh consecutive refill with no item (R214-R260).

### Refill note R261 (not an item; no item added)
- 2026-11-18 R261 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "currency report",
  "manipulator" or "OPEC" entry in research/ or knowledge/ before this run): (a) US Treasury semiannual FX report / manipulator
  designations -> later EUR/USD drift; (b) OPEC meeting decisions -> EUR/USD. Three standard searches.
  (a) Hits were news/policy pages only (Taipei Times, CRS IF10049, investinglive, MNI, CSIS, fx-markets, CFR, calendar page); no FX
  event study; none opened, not cited. (b) First search: FXStreet/MarketPulse/OANDA commentary only. Second search: "OPEC News and
  Exchange Rate Forecasting Using Dynamic Bayesian Learning" (bohrium.com page) returned an anti-bot WAF challenge, not circumvented,
  UNVERIFIED, not cited; other hits (Energy Economics 32(6) 2010 RePEc record, IMF WP 2022/183, core.ac.uk 198021235, koreascience,
  aabri, crude-oil OPEC/SPR event studies) are oil-price studies or were not opened; not cited.
- No item added: (a) ~2 reports/yr (~12 dev events, below the R090 floor) and aimed at CNY/Asian currencies, no EUR/USD basis;
  (b) no verified EUR/USD study, OPEC calendar not in the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Forty-eighth consecutive refill with no item (R214-R261).

### Refill note R262 (not an item; no item added)
- 2026-11-18 R262 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "early close",
  "half-day", "geomagnetic" or "space weather" entry in research/ or knowledge/ before this run): (a) US early-close / half-day holiday
  sessions -> EUR/USD direction; (b) geomagnetic storms / space weather -> EUR/USD returns. Two standard searches.
  (a) Opened Lenzo (Russell Investments, Nov 2025) holiday trading note: liquidity/volume only (FX volumes 30-50% below normal late
  December). Other hits (Russell regional mirrors, advisorperspectives/advisoranalyst reposts) are copies, not cited. (b) No geomagnetic
  FX return study among hits; opened Lahaye-Neely St. Louis Fed WP 2014-034B (EUR/USD, USD/JPY 5-min 1999-2013, volatility/jump
  spillovers only). Other hits (fedinprint 13595, RePEc fedawp 2003-5, openICPSR 226141, ZBW PDF, WEF, Institutional Investor) not
  opened, not cited. Entries in research/academic_studies.md.
- No item added: (a) liquidity only, ~3 events/yr (below the R090 floor); (b) no verified EUR/USD direction evidence, volatility only.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Forty-ninth consecutive refill with no item
  (R214-R262).

### Refill note R263 (not an item; no item added)
- 2026-11-18 R263 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "bank stock",
  "banking sector" or "RavenPack" entry in research/ or knowledge/ before this run): (a) euro-area bank equity returns -> next-day
  EUR/USD; (b) news-sentiment indices (RavenPack/GDELT) -> EUR/USD returns. Two standard searches.
  (a) No FX return study among hits (econbiz record on predicting Eurozone bank stock direction, ECB FSR 2006 article, FXStreet/
  poundsterlinglive commentary, arXiv 2408.13214 LLM fusion forecaster); none opened, not cited. (b) Opened Zhang arXiv 2505.16136
  (already logged in academic_studies.md: GDELT + FinBERT, daily, Sharpe ~5.9 implausible) and Kebe-Uhl, J. Behavioral Finance 25(2)
  2024, doi:10.1080/15427560.2022.2100386 (IDEAS abstract only: intraday Euro-specific news sentiment "predictive but not
  contemporaneous" for EURUSD; design, horizon, OOS and costs UNVERIFIED, full text paywalled). Entry in research/academic_studies.md.
- No item added: (a) no verified evidence; (b) a pre-registrable rule needs a timestamped news/sentiment feed, which is not in the
  pipeline (RavenPack licensed; GDELT history 2015-2023 too large for the runner, R-entry for Zhang). pytest 454 passed. 0 trials used
  (dev 261, val 9, total 270). Not a pipeline failure. Fiftieth consecutive refill with no item (R214-R263).

### Refill note R264 (not an item; no item added)
- 2026-11-18 R264 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "tariff",
  "Italian spread" or "BTP-Bund" entry in research/ or knowledge/ before this run): (a) US tariff announcements -> later EUR/USD drift;
  (b) BTP-Bund sovereign spread changes -> next-day EUR/USD. Two standard searches.
  (a) Opened Ostry-Lloyd-Corsetti BoE SWP 1,139 (2025): daily, EUR/USD included, 46 event days 2018-2020; USD ~1% up over four weeks
  after unretaliated shocks, sign flips with retaliation (defined by a foreign response within 7 days, i.e. look-ahead). Opened BIS WP
  1282 landing page only (2025 episode, dollar move attributed to non-tariff shocks; PDF failed). Other hits (CEPR column, Ostry DP20452
  mirror, Morningstar, FXStreet, Ebury) not opened or commentary; not cited. (b) Hits were commentary only (ING/FXStreet "dangerous
  correlation" 2023, FXStreet 2018, Equals, Hellenic Shipping News, Italian-language pages); no predictive study; none opened, not cited.
  Entries in research/academic_studies.md.
- No item added: (a) the unconditional sign is not identified without look-ahead on retaliation; dev events already used by the authors;
  val has no tariff episode so no pre-registered val confirmation is possible (LEAD criterion 2 unreachable); event list not in the
  pipeline; daily multi-week horizon outside the intraday frame. (b) no verified evidence; BTP/Bund yields not in the pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Fifty-first consecutive refill with no item
  (R214-R264).

### Refill note R265 (not an item; no item added)
- 2026-11-18 R265 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "stablecoin", "USDT"
  or "quiet period" entry in research/ or knowledge/ before this run): (a) stablecoin issuance / net flows -> EUR/USD; (b) ECB
  monetary-policy quiet period -> EUR/USD drift. Two standard searches.
  (a) Opened BIS WP 1340 (Aldasoro-Beltrán-Grinberg 2026) landing page: 27 fiat currencies 2021-2025, IV design, stablecoin demand
  depreciates the local currency (EM most exposed), +40 bp parity deviation per 1% inflow; no predictive or cost test; EUR coverage
  not stated. Other hits (IMF WP 2026/056, JFQA blockchain-currency PDF, SNB seminar slides, news pages) not opened; not cited.
  (b) Opened CEPR DP15735 (Gnan-Rieder) landing page: confidential breach data, market-reaction size only, no FX direction test.
  Other hits ECB explainer pages and FXStreet commentary; not cited. Entries in research/academic_studies.md.
- No item added: (a) causal not predictive, EM-focused, sample starts in val/OOS era (no dev coverage), flow data not in pipeline;
  (b) breach records confidential, no direction evidence (ECB meeting windows already tested E022-E025 family). pytest 454 passed
  (after reinstalling dev dependencies in a fresh workspace). 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Fifty-second consecutive refill with no item (R214-R265).

### Refill note R266 (not an item; no item added)
- 2026-11-18 R266 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "cash open" or
  "North Rhine" entry in research/ or knowledge/ before this run): (a) European cash-equity open (09:00 CET) -> EUR/USD intraday;
  (b) German state (Länder) CPI releases -> EUR/USD reaction. Two standard searches.
  (a) Hits were generic FX-equity linkage papers; none addresses the cash open; opened Cagliesi-Della Bina-Tivegna (Greenwich CEPGR
  WP 2, 2014): EUR/USD 8-hour periods 2003-2011, in-sample EGARCH news model, no out-of-sample or cost test. Other hits not opened;
  not cited. (b) Hits were broker commentary (XTB, Continuum) plus Norges Bank Staff Memo 5/2026 (opened): contemporaneous news-shock
  variance shares for USDEUR, no forecasting test, no state-CPI result. Entries in research/academic_studies.md.
- No item added: (a) no verified evidence on a cash-open effect; (b) no verified state-CPI study; both papers opened need a
  surprise/consensus calendar (B6 blocker) and are in-sample/structural. pytest 454 passed. 0 trials used (dev 261, val 9,
  total 270). Not a pipeline failure. Fifty-third consecutive refill with no item (R214-R266).

### Refill note R267 (not an item; no item added)
- 2026-11-18 R267 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "dealer gamma",
  "carbon" or "EU ETS" entry in research/ or knowledge/ before this run; volatility-managed momentum, same-time-of-day persistence
  and realized skewness were checked and found already covered: R223, ~line 503/1214, E044): (a) FX option dealer gamma
  positioning / strike pinning -> EUR/USD; (b) EU ETS carbon price returns -> next-day EUR/USD. Three standard searches.
  (a) Hits were trade press (Risk.net, FX Markets, Newsquawk expiry headlines, an mql5 blog); no study; none opened; not cited.
  Option-expiry effects already covered in earlier refills. (b) Opened Salvagnin et al. arXiv 2406.05094: daily 2014-2023, EUR/USD
  is a driver of carbon prices, not a predicted variable; no carbon -> FX test. Other hits (arXiv 2510.22341, 2505.10384, IE news,
  GDELT blog) not opened; not cited. Entry in research/academic_studies.md.
- No item added: (a) no verified evidence and dealer positioning data not available; (b) wrong causal direction, EUA prices not in
  the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Fifty-fourth consecutive
  refill with no item (R214-R267).

### Refill note R268 (not an item; no item added)
- 2026-11-18 R268 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "swap line",
  "TARGET2" or "Target2" entry in research/ or knowledge/ before this run): (a) Fed central-bank dollar swap-line usage -> EUR/USD;
  (b) TARGET2 balances -> EUR/USD. Two standard searches.
  (a) Opened Kloks (St. Gallen WP, Sep 2025, Boston Fed conference PDF): daily CLS FX-swap data 2012-2022 incl. EUR/USD, swap-line
  supply lowers FX-swap effective spreads (0.7 bp per 1 s.d. net USD demand); no spot-return forecast, no OOS or cost test. Other
  hits (NBER w31901/w28585, DNB WP 752, CEPS note, glossary pages) not opened; not cited. (b) Opened Bettendorf-Jochem, Applied
  Economics 2023 abstract: BVAR of German TARGET claims, no FX variable. Other hits not opened; not cited. Entries in
  research/academic_studies.md.
- No item added: (a) swap-market pricing, not spot direction, and swap-line operations are sparse outside crises (2020 only in dev);
  (b) no FX evidence and monthly data not in the pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a
  pipeline failure. Fifty-fifth consecutive refill with no item (R214-R268).

### Refill note R269 (not an item; no item added)
- 2026-11-18 R269 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "pension", "corporate
  hedging", "Schatz" or "Italian auction" entry in research/ or knowledge/ before this run; equity-hedging fix flows already covered
  by Melvin-Prins): (a) euro-area government bond auctions -> EUR/USD; (b) institutional investors' time-varying FX hedge ratios ->
  EUR/USD. Two standard searches.
  (a) Opened Lengyel-Giuliodori DNB WP 674 (2020): bond-futures auction demand shocks, outcomes yields/CDS/equities, no FX. Other
  hits (ECB WP 2056/2927, UvA chapter, Melbourne and ICMAIF PDFs) not opened; not cited. (b) Opened Bräuer-Hau (BIS conference
  paper 2022): monthly CLS hedging pressure, EUR/USD included, contemporaneous plus in-sample VAR, no OOS or cost test. Other hits
  (AEA 2024 program, AFA, ESRB WP 148, VoxEU column, CESifo WP 10065, State Street notes) not opened; not cited. Entries in
  research/academic_studies.md.
- No item added: (a) no FX evidence; (b) contemporaneous/monthly and CLS positioning data not in the pipeline. pytest 454 passed.
  0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Fifty-sixth consecutive refill with no item (R214-R269).

### Refill note R270 (not an item; no item added)
- 2026-11-18 R270 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "AAII" or "Heiden"
  entry in research/ or knowledge/ before this run; Sentix release angle searched R183; BDI only as one of 14 daily predictors in an
  already-logged study): (a) investor sentiment surveys -> EUR/USD; (b) Baltic Dry Index / freight -> EUR/USD. Two standard searches.
  (a) Opened Heiden-Klein-Zwergel EFM 2013 abstract: EUR/USD, institutional sentiment predicts medium-term returns, private sentiment
  unstable, OOS trading strategy reported significant, frequency/source/costs UNVERIFIED. FXStreet AAII column, AEA 2017, NBER and
  Frankfurt PDFs not opened; not cited. Media-sentiment reversals (Filippou et al.) already logged. (b) Opened Han-Wan-Xu FRL 2020
  abstract: 14 currencies vs USD, long-run predictability, no cost/strategy test. Other hits not opened; not cited. Entries in
  research/academic_studies.md.
- No item added: (a) medium-term horizon and survey data not in the pipeline; (b) long-run horizon, BDI not in the pipeline, no cost
  test. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Fifty-seventh consecutive refill with no item (R214-R270).

### Refill note R271 (not an item; no item added)
- 2026-11-18 R271 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Brexit" or "Draghi"
  entry in research/ or knowledge/ before this run; ECB press-conference statements already logged): (a) Brexit/UK political shocks ->
  later EUR/USD; (b) ECB policymaker speeches outside meetings -> EUR/USD drift. Two standard searches.
  (a) Opened Dao-McGroarty-Urquhart JIFMIM 2019 abstract: Brexit-vote effect on intraday correlation/volatility transmission, no
  direction test. Other hits (Leicester thesis, Southampton, CORE, NTU repository, ProQuest, Warwick URSS, DOSM journal) not opened;
  not cited. (b) Opened ECB Blog 24 Sep 2026 (Istrefi-Odendahl-Sestieri, authors partly UNVERIFIED): contemporaneous OIS/asset
  reactions to ~5,000 communication events 1999-2024, no separate EUR/USD result, no forecast test. Other hits (BSI Ehrmann slides,
  ICMAIF PDF, Berkeley project, Emerald paper, VoxEU column already logged) not opened; not cited. Entries in
  research/academic_studies.md.
- No item added: (a) single event, volatility/correlation only; (b) contemporaneous only and no speech-time calendar in the pipeline.
  pytest 454 passed (after reinstalling dev dependencies in this workspace). 0 trials used (dev 261, val 9, total 270). Not a
  pipeline failure. Fifty-eighth consecutive refill with no item (R214-R271).

### Refill note R272 (not an item; no item added)
- 2026-11-18 R272 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "estimated tax" or
  "Lunar New Year" entry in research/ or knowledge/ before this run; TGA mentioned only in passing): (a) US quarterly corporate
  tax dates / Treasury General Account cash drains -> EUR/USD; (b) Chinese Lunar New Year holiday -> EUR/USD. Two standard searches.
  (a) Opened Huther-Pettit-Wilkinson FEDS Note 16 Dec 2019: TGA/reserves weekly volatility, descriptive, no FX, return, OOS or cost
  test. Other hits (FXStreet, ABA, MNI, Accounting Today, BNY PDF, crypto news) not opened; not cited. (b) Opened Yuan-Gupta QREF 2014
  doi:10.1016/j.qref.2014.06.001 (Griffith PDF): seven Asian equity indices 1999-2012, pre-holiday ARMA-GARCH dummies, equities only,
  no FX, no OOS; trading/cost figures from the later part UNVERIFIED. Other hits (FXStreet, ForexLive, EUR thesis, ecomod gold PDF)
  not opened; not cited. Entries in research/academic_studies.md.
- No item added: (a) no FX evidence and ~24 quarterly tax dates on dev, below the R090 power floor; (b) equities only, ~6 dev events.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Fifty-ninth consecutive refill with no item
  (R214-R272).

### Refill note R273 (not an item; no item added)
- 2026-11-18 R273 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Swiss National Bank",
  "Tokyo lunch" or "Tokyo experiment" entry in research/ or knowledge/ before this run): (a) SNB policy decisions -> EUR/USD;
  (b) Tokyo lunch-hour liquidity -> EUR/USD. Two standard searches.
  (a) Opened Borner SNB WP 2025-01 landing page: 30-min event windows, futures/stocks/FX, contemporaneous only, no EUR/USD forecast,
  OOS or cost test; sample UNVERIFIED. Other hits (LSE DP550, NYU, JPMorgan Chase Institute pages, FXStreet, Euromoney, SUERF note)
  not opened; not cited. (b) Opened Ito-Lyons-Melvin NBER w5936 / JF 1998: lunch return variance doubles once lunch trading allowed,
  volatility only. Other hits (AEA 2020 paper, Krohn WU PDF already covered by KMW entries, BoC SWP 2021-48, LSEG notes, Columbia,
  SNB WP 2011-04 already logged, w12413) not opened; not cited. Entries in research/academic_studies.md.
- No item added: (a) contemporaneous CHF reaction, ~4 decisions/yr, below the R090 power floor; (b) volatility only, 1990s regime,
  Tokyo-hours windows already scanned (E009) and home-hours line closed on val (E017). pytest 454 passed. 0 trials used (dev 261,
  val 9, total 270). Not a pipeline failure. Sixtieth consecutive refill with no item (R214-R273).

### Refill note R274 (not an item; no item added)
- 2026-11-18 R274 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles: (a) hidden-Markov /
  regime-switching intraday direction -> EUR/USD (only daily Markov-switching entries before this run); (b) FX dealer inventory /
  end-of-day reversal (no "market maker inventory" entry before this run); plus a check of social-media/retail sentiment hits.
  Three standard searches. (a) Opened Chaudhary arXiv 2606.06190 (2026): EUR/USD MS-GARCH, volatility regimes, OOS directional IC
  +0.025 with no cost/P&L test, test period 2021-2024 overlaps val/OOS. Other hits (MPRA 21154, GUPEA thesis, arXiv 2402.05272,
  J. Forecasting 10.1002/for.1135) not opened; not cited. (b) Every relevant hit (Krohn-Mueller-Whelan fixings, BoC SWP 2021-48,
  NY Fed SR917, CEPR DP14462) is already logged; nothing new opened. Sentiment hits (Gholampour-van Wincoop tweets) already logged.
  Entry in research/academic_studies.md.
- No item added: (a) volatility tool, tiny uncosted IC, Markov-switching direction already NONE on dev (E050); (b) no new source.
  0 trials used (dev 261, val 9, total 270). Not a pipeline failure. Sixty-first consecutive refill with no item (R214-R274).

### Refill note R275 (not an item; no item added)
- 2026-11-19 R275 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "turn of the year",
  "January effect", "leverage effect" or "asymmetric volatility" entry in research/ or knowledge/ before this run): (a) turn-of-the-year /
  January effect -> EUR/USD; (b) asymmetric (semi)volatility / realized volatility -> next-day EUR/USD direction. Two standard searches.
  (a) Opened Kumar SEF 2018 doi:10.1108/SEF-08-2015-0192 (IDEAS abstract): 20 USD pairs 1995-2014, OLS-GARCH in-sample, January returns
  higher but calendar effects largely vanish in 2005-2014; pair list (EUR/USD inclusion) UNVERIFIED; no OOS or cost test. Other hits
  (Econ. Modelling 81 2019 RePEc page, HAL 02314156, City Index, Peter Brandt PDFs) not opened; not cited. (b) Opened Cho-Rho Empirical
  Economics 2022 doi:10.1007/s00181-021-02091-7 (abstract): 5-min quotes 2004-2017, HAR quantile regressions with semivariances,
  volatility forecasting only, no direction/OOS/cost test, currency list UNVERIFIED; Gkillas-Gupta-Pierdzioch Physica A 2019
  doi:10.1016/j.physa.2019.121867 (IDEAS abstract): EUR/USD among 6 pairs 2003-2015, realized skew/kurtosis improve OOS one-day RV
  forecasts, volatility only. Other hits (BCB WPS454, Londono-Zhou, CEPR DP9549, mql5 copy, core.ac.uk, AEA 2014, arXiv 2101.09738)
  not opened; not cited. Entries in research/academic_studies.md.
- No item added: (a) effect reported to have disappeared after 2005 and ~6 Januaries on dev, below the R090 power floor; (b) volatility
  forecasting only, and realized skewness -> direction already NONE on dev (E044/B50). pytest 454 passed. 0 trials used (dev 261,
  val 9, total 270). Not a pipeline failure. Sixty-second consecutive refill with no item (R214-R275).

### Refill note R276 (not an item; no item added)
- 2026-11-19 R276 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "prediction market",
  "Polymarket" or "Kalshi" entry in research/ or knowledge/ before this run; "yield curve" already covered R226, Chen-Tsang logged):
  (a) prediction-market probabilities (Polymarket/Kalshi) -> EUR/USD; (b) abnormal FX/futures volume -> next-day EUR/USD. Two standard
  searches. (a) Hits were vendor blogs/market pages only (sparkco.ai, keyrock, frenzycap, struct.to, allmind.ai, Payden PoV commentary);
  no academic or backtested FX study among them; none opened; not cited. (b) Hits point to Cespa-Gargano-Riddiough-Sarno RFS 2022
  (IDEAS rfinst v35 p2386), already logged in research/academic_studies.md; JBS/Cambridge Network press items and Bayes WP-EMG-01-2021
  not opened; not cited. No new entries in research/academic_studies.md.
- No item added: (a) no study; prediction-market history starts ~2020-2024, mostly outside dev, and no EUR/USD contract series in the
  pipeline; (b) no new source; FX volume data (CLS) not in pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Sixty-third consecutive refill with no item (R214-R276).

### Refill note R277 (not an item; no item added)
- 2026-11-19 R277 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "settlement risk",
  "bank reserves" or "H.4.1"-reserves entry in research/ or knowledge/ before this run; IMM/futures roll already covered R137,
  sovereign ratings R169): (a) FX settlement-holiday / value-date and CLS settlement-risk effects -> EUR/USD; (b) weekly Fed H.4.1
  reserve-balance changes -> next-week EUR/USD. Two standard searches. (a) Opened Lee-Ranaldo-Tsuruga IMF WP/2026/156 (landing page
  and markdown rendering of the PDF): CEE currencies only (HUF treated, 2015-2016), daily excess returns ~10 bp lower after CLS
  adoption, US-holiday test on 4 CEE/USD pairs, in-sample DiD with one treated unit, no EUR/USD direction, no OOS or cost test.
  Interactive Brokers / thismatter / gojust pages are broker explainers; not cited. (b) Hits were FRED/ALFRED data series and
  FXStreet/TradingView commentary only; no study; none opened; not cited. Entry in research/academic_studies.md.
- No item added: (a) no EUR/USD direction evidence (EUR/USD already CLS-settled throughout the data); (b) no study, and weekly
  reserve data would give ~300 dev weeks with no verified mechanism. pytest 454 passed (after reinstalling dev extras; statsmodels
  was missing from this workspace, not a repo fault). 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Sixty-fourth consecutive refill with no item (R214-R277).

### Refill note R278 (not an item; no item added)
- 2026-11-19 R278 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "MOVE index" or
  "VVIX" entry in research/ or knowledge/ before this run): (a) Treasury implied volatility (ICE BofA MOVE) -> next-day EUR/USD;
  (b) volatility-of-volatility (VVIX) / FX volatility risk premia -> later EUR/USD returns. Two standard searches. (a) Hits were
  broker/news commentary only (rankiapro, myfxbook/liquidityfinder, Continuum Economics, StoneX); no study; none opened; not cited.
  (b) Re-opened Babiak-Baruník arXiv:2101.09738 abstract (already logged R161: cross-sectional option-implied volatility network,
  not vol-of-vol); opened Ornelas-Mauad BCB WP 455 (entry in research/academic_studies.md: VRP -> 1-3 month index returns,
  in-sample, post-crisis only, no EUR/USD target). Other hits (Scribd VVIX deck, Frankfurt SSRN-id3183610, Vienna thesis,
  Cambridge repository) not opened; not cited.
- No item added: (a) no study, and MOVE / option data are not in the pipeline; (b) monthly in-sample index regressions only, no
  EUR/USD daily or intraday direction evidence. pytest 454 passed (after reinstalling dev extras). 0 trials used (dev 261, val 9,
  total 270). Not a pipeline failure. Sixty-fifth consecutive refill with no item (R214-R278).

### Refill note R279 (not an item; no item added)
- 2026-11-19 R279 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "stock-bond",
  "equity-bond correlation" or "dollar smile" entry in research/ or knowledge/ before this run): (a) stock-bond correlation regime
  -> EUR/USD direction; (b) "dollar smile" (USD direction conditional on US equity drawdowns / risk-off). Two standard searches.
  (a) Opened Phylaktis-Yamani JEF 2025 doi:10.1016/j.jempfin.2025.101641 abstract (entry in research/academic_studies.md): OOS
  stock/bond returns -> FX, profitable only for emerging markets, none in developed-country data; not a correlation-regime study.
  Other hits (Bayes WP-EMG-03-2022, City thesis, State Street stock-bond correlation paper, ISEG REM WP 0366, etf.com, FXStreet)
  not opened; not cited. (b) Hits were asset-manager / broker commentary only (J.P. Morgan AM, T. Rowe Price, rankiapro) plus
  Daniel-Hodrick-Lu carry-trade paper (not opened; not cited); no empirical test of the dollar smile; none opened.
- No item added: (a) the only opened study is negative for developed currencies and the equity/bond-return -> FX family is
  already NONE (B35/E037); (b) no study. pytest passed (see run log). 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Sixty-sixth consecutive refill with no item (R214-R279).

### Refill note R280 (not an item; no item added)
- 2026-11-19 R280 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "EPFR", "fund flow",
  "COFER" or "reserve manager" entry in research/ or knowledge/ before this run): (a) international mutual-fund / ETF flows (EPFR)
  -> later EUR/USD; (b) central-bank reserve-currency diversification (IMF COFER) -> EUR/USD. Two standard searches.
  (a) Opened Li-de Haan-Scholtens OER 2018 doi:10.1007/s11079-017-9469-5 (entry in research/academic_studies.md): monthly EPFR flows,
  53 countries, in-sample panel, mostly contemporaneous co-movement, no EUR/USD pair, no OOS/cost test. Other hits (isimarkets blog,
  BIS WP 1042, fa-mag / wealthmanagement / financial-planning ETF articles, Informa dataset page) not opened; not cited.
  (b) Opened Gefang-Hall-Tavlas arXiv:2608.24468 (entry in research/academic_studies.md): annual reserve shares 1999-2023, models
  shares not FX returns. Other hits (OER 2022 s11079-022-09681-7, VoxEU column, NY Fed SR1087, IMF blogs, Ito JIMF paper) not opened; not cited.
- No item added: (a) in-sample monthly contemporaneous panel, flow data not in pipeline; (b) annual, no return-prediction test, COFER
  is quarterly with a lag (far below the R090 event floor). 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Sixty-seventh consecutive refill with no item (R214-R280).

### Refill note R281 (not an item; no item added)
- 2026-11-19 R281 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "barrier",
  "pollution" or "air quality" entry in research/ or knowledge/ before this run): (a) FX option barrier levels -> EUR/USD spot
  behaviour (defence / pinning / reversal near barriers); (b) air pollution / investor mood -> EUR/USD. Two standard searches.
  (a) Opened Jessen-Poulsen QF 2013 doi:10.1080/14697688.2012.723820 (CBS open archive; entry in research/academic_studies.md):
  barrier-option pricing-model comparison on USD/EUR 2004-2005, no spot-behaviour or trading test. Other hits (arXiv 1511.00848
  pricing method, UvA slides, SGGW article, GlobalCapital news, mql5 vendor blog, mathfinance fixing-delay notes/slides) not opened; not cited.
  (b) Opened Heyes-Neidell-Saberian NBER WP 22753 (entry in research/academic_studies.md): Manhattan PM2.5 -> same-day S&P 500
  returns, equities only. Other hits (MSU thesis, The World news, Frontiers public-health article, CFA digest, Southampton eprint) not opened; not cited.
- No item added: (a) no spot-direction evidence and barrier-level data is not in the pipeline (vendor/bank feed); (b) no FX test,
  pollution data not in pipeline. pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Sixty-eighth consecutive refill with no item (R214-R281).

### Refill note R282 (not an item; no item added)
- 2026-11-19 R282 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "credit spread",
  "HY spread" or "yield curve slope" entry in research/ or knowledge/ before this run): (a) US high-yield credit-spread changes ->
  later EUR/USD; (b) US yield-curve slope -> EUR/USD. Two standard searches.
  (a) Opened Rossi Júnior Insper BEWP 198/2014 (entry in research/academic_studies.md): weekly, 27 non-euro currencies vs USD,
  HY spread as a contemporaneous "realized fundamental", no costs. Also re-opened Della Corte-Jeanneret-Patelli AEA 2020 draft
  (already logged R201: licensed quanto-CDS data, weekly+ horizon). Other hits (Liège skewness PDFs, Engel appendix, AEA 2018/2021
  drafts, UCP thesis) not opened; not cited.
  (b) Top hit Chen-Tsang NBER WP 16427 already logged (R221/R226: monthly basket signal). Other hits (UW, AOF, core.ac.uk, Chinn
  foreign yield curves, vLex, WU slides, Bond Vigilantes blog) not opened; not cited.
- No item added: (a) no EUR/USD tradable-forecast evidence and credit-spread data not in pipeline; (b) already-logged monthly
  evidence only. pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Sixty-ninth consecutive refill with no item (R214-R282).

### Refill note R283 (not an item; no item added)
- 2026-11-19 R283 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no Fed "blackout"
  or US-German 2-year spread entry in research/ or knowledge/ before this run; ECB quiet period was R265): (a) FOMC blackout
  period -> USD / EUR/USD drift; (b) daily change in the US-German 2-year yield spread -> next-day EUR/USD. Two standard searches.
  (a) Opened the Fed IFDP note of 22 Sep 2017 (entry in research/academic_studies.md): dollar index, same-day sensitivity on FOMC
  days, no drift or blackout test. Karnaukh and Borisenko-Pozdeev hits already logged. Other hits (AEA/AFA preliminary pages,
  Boston Fed PPB 13-7, FRBSF WP 2015-18, Macrosynergy commentary, RePEc pages) not opened; not cited.
  (b) Hits were FXStreet/FXCM/Investing.com commentary and TradingView scripts only (contemporaneous co-movement claims); none
  opened, not cited; daily German/US 2-year yields are also not in the pipeline.
- No item added: (a) no verified pre-FOMC blackout drift result beyond already-logged Karnaukh work; (b) no study.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventieth consecutive refill with no item (R214-R283).

### Refill note R284 (not an item; no item added)
- 2026-11-19 R284 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Mrs Watanabe",
  "toshin"/"Japanese retail" or "ECB balance sheet" entry in research/ or knowledge/ before this run): (a) Japanese retail FX
  margin-trader positioning -> later EUR/USD; (b) Eurosystem weekly financial statement (Tuesday release) -> EUR/USD. Two standard searches.
  (a) Opened Hayo-Iwatsubo Kobe DP 1909 / CityU GRU WP 2019-026 (same study; entry in research/academic_studies.md): survey of
  trader profitability, no exchange-rate prediction test. Other hits (RBA Bulletin Mar 2009, Kobe repository PDF, BoJ Review
  rev23e07, MDPI 14/18/11662, Bloomberg/Japan Times/FX-Markets/MUFG news) not opened; not cited. Retail positioning data
  (e.g. broker or exchange position ratios) is also not in the pipeline.
  (b) Hits were the weekly statements themselves (ECB, Banque de France, Banca d'Italia, Banco de Espana PDFs), no study; none
  opened, not cited.
- No item added: (a) no verified positioning -> EUR/USD direction evidence and no data in pipeline; (b) no study.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-first consecutive refill with no item (R214-R284).

### Refill note R285 (not an item; no item added)
- 2026-11-19 R285 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Keloharju",
  "return seasonalit" or "Barroso" entry in research/ or knowledge/ before this run): (a) same-calendar-month return seasonality
  -> EUR/USD; (b) volatility-managed currency momentum -> EUR/USD. Two standard searches.
  (a) Opened Keloharju-Linnainmaa-Nyberg NBER WP 20815 (entry in research/academic_studies.md): stocks, commodities, country
  indices only, no currencies. Other hits (Bauer/AQR copies of the same paper, RePEc, vLex, SUFE, Nasdaq PDF) not opened; not cited.
  (b) Opened Barroso-Menichetti-Reichenecker 2018 draft (entry in research/academic_studies.md): monthly cross-sectional overlay,
  no EUR/USD single-pair result. Other hits (Quantpedia, ADU/CORE/BIS WP 366/UCP/Reschenhofer PDFs) not opened; not cited
  (Menkhoff et al. currency momentum already in academic_studies.md).
- No item added: (a) no FX evidence; (b) cross-sectional monthly design, no single-pair evidence, data not in pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-second consecutive refill with no item (R214-R285).

### Refill note R286 (not an item; no item added)
- 2026-11-19 R286 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (only one prior
  "risk reversal" mention and no "crowd"/CTA-positioning study entry in research/ or knowledge/ before this run): (a) EUR/USD 25-delta
  risk reversals -> next-day spot direction; (b) CTA / speculator crowding -> EUR/USD. Two standard searches.
  (a) Hits were trade press (GlobalCapital, FXStreet), a vendor glossary (LuxAlgo) and an exotic-pricing paper (arXiv 2602.01376,
  pricing only per title/snippet); none opened, not cited. Option risk-reversal data are also not in the pipeline.
  (b) Opened Pojarliev-Levich NBER WP 15698 and Sokolovski 2016 JMP (entries in research/academic_studies.md): manager-factor
  crowding (no formal test) and monthly carry-portfolio crowding (costs ignored); no EUR/USD single-pair direction test. Other hits
  (BofA/Tickmill/Investing/FXStreet CTA and COT commentary) not opened; not cited (COT -> EUR/USD already argued against, R082).
- No item added: (a) no study; (b) no single-pair evidence, data not in pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-third consecutive refill with no item (R214-R286).

### Refill note R287 (not an item; no item added)
- 2026-11-19 R287 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "flash inflation"
  entry and no "volatility risk premium" phrase in research/ or knowledge/ before this run): (a) euro-area flash HICP release ->
  intraday EUR/USD direction; (b) FX volatility risk premium (implied minus realized) -> later EUR/USD returns. Two standard searches.
  (a) Hits were FXStreet release/news pages only (not evidence); none opened, not cited. No study.
  (b) Hits were CEPR DP9549 "Volatility Risk Premia and Exchange Rate Predictability" (already logged R180, academic_studies.md
  ~line 1081; also re-surfaced R276), its Imperial/City/mql5 copies and BCB WPS454 (VRP -> commodities, Ornelas-Mauad family
  already logged R278); none newly opened, not cited. Option implied-vol data are also not in the pipeline.
- No item added: (a) no study; (b) family already logged, data not in pipeline.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-fourth consecutive refill with no item (R214-R287).

### Refill note R288 (not an item; no item added)
- 2026-11-19 R288 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "ARIMA" entry and only
  one "wavelet" mention in research/ or knowledge/ before this run): (a) ARIMA / univariate time-series forecasts -> next-day EUR/USD
  direction net of costs; (b) wavelet-decomposition forecasts -> EUR/USD. Two standard searches.
  (a) Opened Costantini-Crespo Cuaresma-Hlouskova 2016 (J. Forecasting, doi:10.1002/for.2398; entry in research/academic_studies.md):
  abstract only, multivariate macro models and forecast combinations, "excess return per unit of deviation is limited"; manuscript
  PDF fetch failed (body UNVERIFIED). Other hits (EXFormer arXiv 2512.12727, Brunel thesis already logged; IIETA, Springer jdhf,
  Bohrium, MDPI, ResearchSquare) not opened; not cited.
  (b) Hits were EMD/neural-network conference papers, Souropanis and Essex papers (already logged), ISI proceedings pages, CORE and
  SCIK PDFs; none newly opened, not cited.
- No item added: (a) macro inputs not in pipeline, no verified daily cost-inclusive result; univariate daily-lag model families
  already tested (E050 Markov switching, E051 random forest); (b) no verified single-pair evidence.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-fifth consecutive refill with no item (R214-R288).

### Refill note R289 (not an item; no item added)
- 2026-11-19 R289 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Reddit" or
  "superstition"/"Friday the 13" entry in research/ or knowledge/ before this run): (a) Reddit / retail social-media attention ->
  EUR/USD; (b) calendar superstition effects (Friday the 13th, Chinese lucky/unlucky days) -> EUR/USD. Two standard searches.
  (a) Hits were the Twitter EUR/USD papers already logged (Papaioannou et al. arXiv 1310.5306 / 1402.1624) and NBER papers not about
  FX; no Reddit-FX study found; none newly opened, not cited.
  (b) Opened Chung & Li (2013), "Chinese Superstition and Foreign Currency Returns", Academy of Taiwan Business Management Review 9(1)
  (https://research-repository.griffith.edu.au/items/8417cb6c-2c1f-542d-ae55-683fa290e588): metadata + abstract only, eight
  currencies, day-of-month dummies; abstract reports unlucky day 24 linked to higher EUR returns; pair, frequency, sample and any
  OOS/cost test UNVERIFIED (PDF not read). Opened Lucey (2001), "Friday the 13th: international evidence", Appl. Econ. Lett. 8(9)
  577-579, doi:10.1080/13504850010025664 (EconPapers abstract): 19 equity indices 1988-2000, no currencies.
- No item added: (a) no study and no social-media feed in the pipeline; (b) the single EUR result is one cell of a multi-currency,
  multi-day dummy scan with no stated mechanism or out-of-sample test (garden-of-forking-paths risk; SPEC needs a mechanism), and
  Friday-the-13th has no FX evidence and ~1-2 events/yr (below the R090 power floor). 0 trials.

### Refill note R290 (not an item; no item added)
- 2026-11-19 R290 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "sight deposit" or
  "current account" entry in research/ or knowledge/ before this run): (a) weekly SNB sight-deposit changes (intervention proxy) ->
  later EUR/USD; (b) euro-area monthly balance-of-payments / current-account release -> EUR/USD drift. Two standard searches.
  (a) Opened Kugler (2020), "The Short-Run Impact of SNB Sight Deposits on Exchange Rates: Results from Weekly Data 2015 - 2018",
  WWZ Working Paper 2020/04, University of Basel (https://ideas.repec.org/p/bsl/wpaper/2020-04.html; full text
  https://core.ac.uk/download/294761712.pdf): weekly, ~2015-2018 (paper states the sample end inconsistently), GMM simultaneous
  system; targets EUR/CHF and USD/CHF only and assumes SNB policy does not move EUR/USD; contemporaneous effect (1% sight-deposit
  rise -> ~0.38-0.41% CHF depreciation), no lagged predictor in the FX equations, no out-of-sample or cost test.
  (b) Hits were ECB/Banque de France BoP press releases and EUR/USD news-announcement papers (Cardiff A2006 and Greenwich CEPGR
  already logged; CESifo WP 7239 not opened, not cited); no study of the BoP release -> EUR/USD.
- No item added: (a) contemporaneous, CHF crosses only, and by the paper's own assumption no EUR/USD channel; sight-deposit data not
  in the pipeline; (b) no verified EUR/USD evidence and ~12 events/yr with no mechanism for a drift. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-seventh consecutive refill with no item (R214-R290).

### Refill note R291 (not an item; no item added)
- 2026-11-19 R291 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Columbus",
  "Veterans" or "Riksbank" entry in research/ or knowledge/ before this run): (a) US bond-market-only holidays (Columbus Day,
  Veterans Day: SIFMA closes cash Treasuries, FX and equities open) -> EUR/USD drift or range on those days; (b) Riksbank policy
  decisions -> EUR/USD spillover. Two standard searches.
  (a) Hits were trade-press / news pages only (FXStreet "Forex Today" 2024-10-14, investinglive, OANDA, fxnx; not cited as
  evidence), no study of FX returns on US bond-only holidays.
  (b) Opened Artta, Nessén, Savoia, Vredin (2025), "Financial Flows and Exchange Rate Dynamics: Evidence from Sweden", Sveriges
  Riksbank Working Paper No. 456
  (https://www.riksbank.se/globalassets/media/rapporter/working-papers/2025/no.-456-financial-flows-and-exchange-rate-dynamics-evidence-from-sweden.pdf):
  daily, from Feb 2021; dependent variables EUR/SEK and USD/SEK, EUR/USD only a control; local-projection impulse responses to
  flow shocks, no predictive regression, no out-of-sample or cost test (remainder of PDF only summarised; sample end stated
  inconsistently in the paper). Riksbank event-study database page seen in results (not opened, not cited).
- No item added: (a) no verified evidence and only ~2 events/yr (below the R090 power floor); (b) SEK crosses only, EUR/USD is a
  control, no lagged EUR/USD channel. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-eighth consecutive refill with no item (R214-R291).

### Refill note R292 (not an item; no item added)
- 2026-11-19 R292 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "World Economic
  Outlook" or "excess liquidity" entry in research/ or knowledge/ before this run; TLTRO mentioned once in passing): (a) IMF World
  Economic Outlook releases -> later EUR/USD drift; (b) euro-area excess liquidity / TLTRO III repayment dates -> EUR/USD. Two
  standard searches.
  (a) Hits were IMF working papers on other topics (natural disasters and exchange rates, high-frequency monetary policy shocks,
  taper tantrum) and an IMF press-briefing transcript; none studies WEO releases and FX. Not opened, not cited.
  (b) Opened ECB Economic Bulletin Focus, Issue 8/2024, "TLTRO III phase-out and bank lending conditions"
  (https://www.ecb.europa.eu/press/economic-bulletin/focus/2025/html/ecb.ebbox202408_07~220d11edeb.en.html; body read only
  via a fetch summary, authorship UNVERIFIED): bank funding replacement and lending conditions, Sept 2022 - 2024, no exchange-rate
  or FX return test. ECB Occasional Paper 355 seen in results (not opened, not cited).
- No item added: (a) no study, and WEO releases are ~2-4 events/yr (below the R090 power floor); (b) no EUR/USD evidence, and
  repayment dates are few and clustered in 2022-2024 (val/OOS only, nothing on dev). 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Seventy-ninth consecutive refill with no item (R214-R292).

### Refill note R293 (not an item; no item added)
- 2026-11-19 R293 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Good Friday",
  "German election" or "French election" entry in research/ or knowledge/ before this run; "Easter" absent): (a) European-only
  holidays with the US open (Good Friday, Easter Monday, TARGET2 closing days) -> EUR/USD drift or range; (b) German / French
  national elections -> EUR/USD. Two standard searches.
  (a) Hits were trade-press pages (FXStreet, investinglive, investing.com, moneyshow; not cited as evidence) and a QuantRocket
  blog post opened via fetch summary: Stanley (2019), "Exploiting Business Day Patterns in FX Markets"
  (https://quantrocket.com/blog/business-day-fx-patterns): not a holiday study but a replication of the Breedon-Ranaldo home-hours
  rule on EUR/USD (short 03:00-11:00 NY, long 11:00-16:00 NY), IB data from 2005, in-sample only, no t-stats or trade counts,
  CAGR/Sharpe claims UNVERIFIED (charts not readable). That family is already tested and closed on val (E017, B14).
  (b) Hits were news pages (FXStreet, marketnews) and NBER w33193 (2024 US election, already logged in the backlog); no EUR/USD election study.
- No item added: (a) no verified holiday evidence and ~2-4 events/yr (below the R090 power floor); the only study-like hit is the
  already-closed home-hours family; (b) a handful of events per decade, no study. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Eightieth consecutive refill with no item (R214-R293).

### Refill note R294 (not an item; no item added)
- 2026-11-19 R294 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Dunne", "Cenedese"
  or "Caixin" entry in research/ or knowledge/ before this run): (a) Chinese PMI releases -> intraday EUR/USD; (b) Asian/foreign equity
  session returns -> later EUR/USD. Two standard searches.
  (a) Hits were trade-press/broker pages only (FXStreet, marketpulse, marketnews, TradingView; not cited as evidence); no study.
  (b) Opened Dunne-Hau-Moore 2005 (daily, same-day equity/FX/order-flow regressions, no predictive test), Cenedese et al. BoE WP 537
  (monthly 42-country cross-section, no EUR/USD pair) and Phylaktis-Yamani WP-EMG-02-2025 (WP version of the logged JEF 2025 paper:
  no profitability for developed currencies). Entries in research/academic_studies.md.
- No item added: (a) no study, and Chinese release calendar not in pipeline; (b) contemporaneous or monthly cross-sectional only,
  developed-currency predictability explicitly absent. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Eighty-first consecutive refill with no item (R214-R294).

### Refill note R295 (not an item; no item added)
- 2026-11-19 R295 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "earnings" entry in
  research/ or knowledge/ before this run): (a) aggregate US corporate earnings surprises -> later USD / EUR/USD; (b) US earnings-season
  timing -> EUR/USD. Two standard searches.
  (a) Opened Sharpe & Gil de Rubio Cruz, FEDS 2024-049 (quarterly S&P 500 earnings and stock returns; the broad dollar is only a
  regressor for profit growth; no FX return forecast, no OOS/cost FX test, no EUR/USD). Other hits already in the library (Bae-Da-Zurita
  2024, Stavrakeva-Tang DP18119) or off-topic. (b) Hits were macro-news announcement studies already covered by the release-time family;
  no earnings-season / FX study found.
- No item added: no verified evidence that earnings predict EUR/USD; earnings data not in the pipeline; quarterly frequency outside the
  intraday frame. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Eighty-second consecutive refill with no item (R214-R295).

### Refill note R296 (not an item; no item added)
- 2026-11-19 R296 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Herstatt",
  "volatility targeting" or "Hasbrouck" entry in research/ or knowledge/ before this run): (a) CLS settlement window / settlement-time
  flows -> intraday EUR/USD direction; (b) volatility-targeted trend following on a single pair (EUR/USD). Two standard searches.
  (a) Opened Hasbrouck-Levich (2019), CLS settlement data April 2010/2013/2016: price-impact and liquidity metrics only, no predictive,
  OOS or cost test; it cites Ranaldo-Somogyi (2018) CLS hourly net flow -> spot, not fetched (UNVERIFIED), and CLS flow data are not in
  the pipeline (the volume-proxy line is already tested, B28/B29). IMF WP/2026/156 already logged (R277). (b) Opened Etienne et al.
  arXiv:2510.23150 (pooled CTA futures universe, horizon weighting; EUR futures one instrument among many, no EUR/USD-specific test;
  trend/momentum family already tested on dev). Entries in research/academic_studies.md.
- No item added: no verified EUR/USD direction evidence with an OOS or cost test; required data not in the pipeline for (a). 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Eighty-third consecutive refill with no item (R214-R296).

### Refill note R297 (not an item; no item added)
- 2026-11-19 R297 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "ChatGPT", "Izadyar"
  or "Levich-Poti" entry in research/ or knowledge/ before this run): (a) LLM (ChatGPT/GPT-4o) forecasts -> EUR/USD direction;
  (b) adaptive-market / time-varying predictability of EUR/USD. Two standard searches.
  (a) Opened Izadyar arXiv:2608.00761 (Aug 2026): GPT-4o classifies macro releases, monthly G10 cross-sectional long-short, Sharpe > 0.7
  gross, no net-of-cost figures, no daily/intraday EUR/USD direction result. arXiv 2408.13214 / 2411.07560 (LLM text-fusion EUR/USD
  forecasters) seen in hits, not opened, not cited. (b) Opened Levich-Poti NBER WP 14597 (2008): daily/monthly 1971-2006 incl. ECU/EUR,
  rolling ARMA R-squared vs good-deal bound, in-sample (stated), daily max-Sharpe strategies negative at 5 bp costs; monthly survive.
  Entries in research/academic_studies.md.
- No item added: (a) monthly cross-sectional, gross only, needs release-text + LLM pipeline not in repo; (b) in-sample, daily
  predictability does not survive 5 bp costs, nothing intraday. 0 trials.
  pytest 454 passed (after reinstalling dev deps; statsmodels was missing in this workspace). 0 trials used (dev 261, val 9, total 270).
  Not a pipeline failure. Eighty-fourth consecutive refill with no item (R214-R297).

### Refill note R298 (not an item; no item added)
- 2026-11-19 R298 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "economic surprise
  index" or "real rate differential" entry in research/ or knowledge/ before this run): (a) economic surprise index momentum -> later
  EUR/USD; (b) real interest-rate / Taylor-rule differentials -> EUR/USD. Two standard searches.
  (a) Hits: DNB WP 850 (already logged R139), Phylaktis-Yamani WP-EMG-03-2022 (already logged), Essex Alexandridis et al. (already
  logged R225), Erasmus theses and FXStreet commentary (not evidence, not opened). No study testing a surprise index as a lagged
  EUR/USD direction predictor. (b) Opened Molodtsova-Papell (2011), "Phoenix Taylor Rule Exchange Rate Forecasting During the
  Financial Crisis" (Banque de France-hosted PDF): quarterly real-time 1999Q4-2010Q4, rolling one-quarter-ahead MSPE vs random walk
  (Clark-West), no directional/trading/cost result in the part read; Taylor-rule family already logged (R171). Entry in
  research/academic_studies.md.
- No item added: no verified EUR/USD evidence at a daily or intraday horizon with an OOS cost test; quarterly frequency gives
  far fewer than the R090 power floor of events on dev. 0 trials.
  pytest 454 passed (after reinstalling dev deps; statsmodels was missing in this workspace again). 0 trials used (dev 261, val 9,
  total 270). Not a pipeline failure. Eighty-fifth consecutive refill with no item (R214-R298).

### Refill note R299 (not an item; no item added)
- 2026-11-20 R299 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Kyle" or "sports"
  entry in research/ or knowledge/ before this run): (a) FX illiquidity / price-impact shocks -> later EUR/USD returns; (b) sports
  (international football) sentiment -> EUR/USD. Two standard searches.
  (a) Hits were all already logged (Ranaldo-Santucci, Hasbrouck-Levich, Marsh-Miao, arXiv 2101.09738, NBER f121921); none re-opened.
  (b) Opened Edmans-García-Norli (2005 draft): national stock indices only, next-day loss effect -21 to -49 bp, no FX test, no
  OOS/cost test seen. Entry in research/academic_studies.md.
- No item added: (a) nothing new; (b) no FX evidence, and elimination-loss events for euro-area teams/US are a handful per year,
  far below the R090 power floor on dev. 0 trials.
  pytest 454 passed (after reinstalling dev deps). 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Eighty-sixth consecutive refill with no item (R214-R299).

### Refill note R300 (not an item; no item added)
- 2026-11-20 R300 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (no "Thanksgiving week"
  or "fiscal year-end" entry in research/ or knowledge/ before this run): (a) US Thanksgiving / December holiday-week effects ->
  EUR/USD; (b) Japanese fiscal year-end (March) repatriation -> EUR/USD via USD leg. Four standard searches (two on angles first
  checked and found already logged: US government shutdown -> USD (articlegateway JAF paper, logged) and month-end rebalancing
  (Krohn-Mueller-Whelan, Melvin-Prins, logged)).
  (a) Opened Russell Investments "Holiday trading effect" (Lenzo, 11 Nov 2026): practitioner liquidity note, FX volume 50-80% below
  normal late December, explicitly no direction signal, no OOS/cost test. Other hits were broker seasonality blogs (investing.com,
  forex.com, FXStreet; not evidence, not opened). (b) Hits were trade press only (FXStreet/Nomura note, ForexLive, Japan Times,
  Bloomberg); no study; not opened. Entry in research/academic_studies.md.
- No item added: no verified EUR/USD direction evidence with an OOS cost test; Thanksgiving/fiscal-year-end give one event per year
  (5 on dev), far below the R090 power floor. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Eighty-seventh consecutive refill with no item (R214-R300).

### Refill note R301 (not an item; no item added)
- 2026-11-20 R301 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (keyword checks first:
  "consensus forecast" and "insider"/"short interest" had no entry; ETF flows already logged): (a) consensus/survey FX forecasts as a
  trading signal -> EUR/USD; (b) currency-ETF (FXE) flows -> EUR/USD. Two standard searches.
  (a) Opened EconPapers abstract of Kwas-Beckmann-Rubaszek IJF 2024 doi:10.1016/j.ijforecast.2023.02.007: Consensus Economics
  survey signals add up to 2 pp/yr over momentum/carry/value portfolios; EUR/USD, frequency, OOS and costs UNVERIFIED (abstract
  only; IfW page fetch refused). Entry in research/academic_studies.md. (b) Hits were advisor/trade press (WealthManagement,
  FA-Mag, WisdomTree blog) and spam pages; no study; not opened; ETF angle already logged.
- No item added: (a) monthly survey data not in the pipeline and ~72 dev months, below the R090 power floor; (b) no evidence. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Eighty-eighth consecutive refill with no item (R214-R301).

### Refill note R302 (not an item; no item added)
- 2026-11-20 R302 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (keyword checks first:
  "Fed speak"/"central bank communication" and "Japanese holiday" had no entry): (a) Fed speeches / central-bank communication ->
  intraday EUR/USD; (b) Japanese public holidays (Tokyo closed) -> Asian-session EUR/USD. Two standard searches.
  (a) Opened Sekkel-Zhang (Bank of Canada, Nov 2024 draft): FOMC/Fed-speech event study 1997-2023 on CAD/USD only, contemporaneous
  windows, no post-event direction, OOS or cost test. Other hits already logged (IES WP 23/2025, Ayadi et al. SEF 2023, VoxEU ECB
  press-conference column). Entry in research/academic_studies.md. (b) Hits were a Japanese-equity paper on US Monday holidays
  (not FX, not opened) and trade press (investinglive, resident.com; not evidence, not opened).
- No item added: (a) no EUR/USD direction evidence and no timestamped speech calendar in the pipeline (B6 blocker); (b) no FX evidence.
  0 trials. pytest 454 passed (after reinstalling dev deps). 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Eighty-ninth consecutive refill with no item (R214-R302).

### Refill note R303 (not an item; no item added)
- 2026-11-20 R303 refill pass (no ready item, no run queued; last run 43840273851 recorded as E051). Angles (keyword checks first:
  "tax day" and "window dressing" had no entry): (a) US tax dates / TGA cash drains -> USD / EUR/USD; (b) bank quarter-end window
  dressing -> EUR/USD spot. Two standard searches.
  (a) Opened Dao-Tan-Zhou IMF WP/25/127 (USD repo spreads vs TGA, no FX) and Correa-Du-Liao NBER 2021 draft (US bank reserves ->
  repo/FX-swap intermediation, CIP basis only, no spot forecast). FEDS Note on fiscal flows already logged; other hits trade press
  (Accounting Today, FXStreet, ABA Journal; not opened). (b) All study hits already logged (BIS WP 836, Boston Fed WP 18-6, Ranaldo
  ECB 2024 paper); risk.net/fx-markets news not opened. Entries in research/academic_studies.md.
- No item added: no verified EUR/USD spot-direction evidence with an OOS cost test; tax dates are ~4 events/yr (~20 on dev), below the
  R090 power floor; quarter-end effects appear in FX-swap basis, not spot, and month-/quarter-end spot angles are already logged. 0 trials.
  pytest 454 passed. 0 trials used (dev 261, val 9, total 270). Not a pipeline failure.
  Ninetieth consecutive refill with no item (R214-R303).
