# Lessons learned

Process and methodology lessons. Use templates/lessons_learned_template.md for each entry.

### 2026-11-07: design lessons carried in from the planning stage
- **[ASSUMPTION]** Retail round-trip costs on EUR/USD (~0.2 to 1.0 pip with spread and slippage) can wipe out the expectancy of very short holds. Holding time must be tested against costs, not chosen up front.
- **[ASSUMPTION]** Test for a cost-free directional signal (E001) before backtesting strategies. If there is no conditional signal, strategy tuning only fits noise.
- Agents interpret; code computes. Every number must trace to a script output.

### 2026-11-07: literature changes the first experiment
- **Context:** R000 literature review
- **Observation:** published time-of-day and fixing effects mean a session predictor can look good just by picking up a scheduled drift.
- **Evidence label:** [PUB]
- **Lesson:** always compare against an unconditional same-window benchmark, and split windows around known fixes and releases.
- **Action:** added the `unconditional_long` predictor and a pre/post-fix breakdown to E001.

### 2026-11-07: E001 came back NONE; the cheap test did its job
- **Context:** E001
- **Observation:** a cost-free signal test across 2,193 days found nothing. Backtesting S002/S003 first would have meant tuning stops and targets on noise.
- **Evidence label:** [EXP]
- **Lesson:** keep running the cheapest falsification test before building strategies.
- **Action:** S002/S003 deprioritised. Next tests target a different hypothesis (S001, within London) or a different outcome window (E006), each counted as a new trial.

### 2026-11-07: break coverage
- **Observation:** London breaks the Asian range on about 97% of days, so "breakout" without a filter is not a selective event.
- **Action:** S001 relies on its Asian-range/ATR filter; test whether that filter matters (E004 vs an unfiltered variant).

### 2026-11-07: the core hypothesis failed three independent ways
- **Context:** E001, E004, E006
- **Observation:** no cross-session directional information for the 4-hour or 1-hour US windows, and the most popular London setup loses even before slippage.
- **Evidence label:** [EXP] [BT]
- **Lesson:** simple price-structure features from earlier sessions carry no usable directional information for EUR/USD in 2015-2023. Further tuning of these features on dev is likely to find only noise (22 trials used so far).
- **Action:** pivot the next research to a different information source (scheduled events / volatility timing) rather than more session-price variants. See agent_decision_log R002.

### 2026-11-07: metric definition
- **Observation:** `costs_share_of_gross` excludes the spread, because gross P&L is measured bid/ask. E004 showed 0.98% while total costs were clearly larger.
- **Action:** add a mid-price gross metric so the full cost share is visible (pipeline backlog).

### 2026-11-07: published fix-reversal effect not usable in EUR/USD dev (E007)
- **Context:** E007
- **Observation:** pre/post-fix returns had the published sign but only ~0.5-0.6 pips with CIs spanning 0; month-end subsets went the other way (post-fix ME -4.5 pips, n=72, driven by few large moves).
- **Evidence label:** [EXP]
- **Lesson:** a published effect (largely USD-index/earlier samples) can shrink below cost in one pair and 2015-2020. Small month-end subsets produce wide, unstable means; treat mean-only CI exclusions with n<100 as hypothesis-generating at most.
- **Action:** B1 closed (NONE). Month-end continuation logged as exploratory backlog item B8 (val only, pre-registered).

### 2026-11-07: session ranges add ~nothing to volatility forecasts beyond prior ATR (E008)
- **Context:** E008
- **Observation:** raw-pips correlation of Asia/London range with |US move| was 0.14-0.21, but the partial IC given prior 14-day ATR was 0.06/0.05 (Asia, CI just above 0) and ~0 (London).
- **Evidence label:** [EXP]
- **Lesson:** most of the apparent "busy session -> busy US session" link is the volatility regime. Always control for prior ATR (and avoid shared-denominator ratios) before calling a magnitude predictor useful.
- **Action:** B2 closed (NOT_USEFUL); prior ATR alone is the default volatility filter for later strategy tests.

### 2026-11-07: a 192-cell scan finds one strong hour, and it is the thinnest one (E009)
- **Context:** E009
- **Observation:** the only cells clearing a Bonferroni bar sit in the NY 18:00 hour, right after the 17:00 roll, where spreads are widest and quotes least representative.
- **Evidence label:** [EXP]
- **Lesson:** in thin, post-roll hours, mid-quote drift can come from quote/spread dynamics on one venue. Any hour-of-day effect must be checked at actual bid/ask before it counts, and weekday splits of a pooled effect are mostly noise.
- **Action:** B9/B10 (val only, 1 trial each) report spread and net bid/ask results alongside the pre-registered rule.

### 2026-11-08: fix-reversal effects in EUR/USD are sub-pip at both London and ECB fixes (E007, E010)
- **Context:** E010
- **Observation:** ECB pre-fix hour shows a USD-up mean of +0.76 pips with a bootstrap CI above 0, yet the hit rate is 0.508; the post-fix hour shows nothing. Same pattern as E007 for London.
- **Evidence label:** [EXP]
- **Lesson:** the published USD-into-fix effect, if present in EUR/USD mid quotes, is a tail-driven fraction of a pip per hour, far below round-trip cost. A CI that excludes 0 with a coin-flip hit rate means a few large days, not a tradable drift.
- **Action:** B4 closed (WEAK, not sent to val). Expect B5 (Tokyo fix) to be weaker still after Asian-hours spreads; run it as pre-registered but with a low prior.

### 2026-11-08: Tokyo fix differs from London/ECB: small but consistent (E011)
- **Context:** E011
- **Observation:** both Tokyo windows move in the predicted direction with hit rates 0.53-0.54 (London/ECB were ~0.51 with tail-driven means). Post-fix hour +0.79 pips mid; descriptive net at bid/ask +0.48 pips. Still below the pre-registered 1-pip bar.
- **Evidence label:** [EXP]
- **Lesson:** a "fails only the size bar" WEAK is still WEAK. The 1-pip bar was set before data; a descriptive cost check that looks positive is not a reason to send it to val. Across 3 fix tests (6 trials, plus 220 others on dev) one sub-pip consistent result is within what multiple testing produces.
- **Action:** B5 closed, B5v not queued. Fix-reversal line (B1, B4, B5) exhausted on dev. Any Tokyo-post re-test needs fresh data and a human decision, like B7.

### 2026-11-08: Hourly-scan candidates shrink on val and rollover hours cost too much (E012)
- **Context:** E012 (val confirmation of E009 cells Wed/Thu NY 18:00)
- **Observation:** dev means +1.33/+1.24 pips fell to +0.65/+0.94 on val with CIs including 0. Median entry spread at 18:00 NY was 1.5-1.7 pips, so net results were negative at every cost level.
- **Evidence label:** [EXP]
- **Lesson:** picking 2 of 192 cells gives roughly 50% shrinkage on fresh data, as expected from selection. Hours next to the 17:00 NY roll have the widest spreads of the day; any drift there must clear ~2 pips round trip before it matters. Screen hourly-scan candidates against the cost at that hour before spending val trials.
- **Action:** B9/B10 closed. No ready backlog items left; next run does a refill pass. New items should target liquid hours (spread < 0.5 pip) or event-driven mechanisms.

### 2026-11-08: Event-driven, literature-backed test gives the first dev SIGNAL (E013)
- **Context:** E013 (B11, FOMC statement-day long EUR/USD, dev, 1 trial)
- **Observation:** the first SIGNAL in 227 dev trials came from a pre-registered, published event mechanism at a liquid hour (entry spread 0.2 pips), not from time-of-day scans. The margin is thin (CI lower 2.7 pips, p 0.029) and per-meeting dispersion is high (SD 75 pips, one +248-pip meeting).
- **Evidence label:** [EXP]
- **Lesson:** event mechanisms with a published basis and low cost are the better line. A dev SIGNAL with ~47 events is fragile; val (~20 events) has low power, so the val rule must stay exactly as pre-registered and a val miss closes B11 on our data.
- **Action:** B11v (val only, same rule, 1 trial) ranked next. Pipeline lesson from phase 1: fetch event calendars on the runner and validate them (counts per year, cancelled/unscheduled flags) before any price data are touched.

### 2026-11-08: A dev SIGNAL on ~47 events does not survive a 20-event val test (E014)
- **Context:** E014 (B11v, val confirmation of E013, 1 trial)
- **Observation:** val mean +19.99 pips (dev +21.28) but CI (-9.53, 51.02), p 0.115 -> NONE. The pre-registered power note predicted val could only confirm a mean of ~35+ pips.
- **Evidence label:** [EXP]
- **Lesson:** for rare events (8/yr) the dev/val split cannot confirm effects of the published size; a similar point estimate is not a confirmation. Before pre-registering an event test, check that val has enough events to confirm the dev-sized effect, or choose events that occur more often (e.g. monthly releases).
- **Action:** B11 closed (rejected_hypotheses, "not confirmed"). Any further FOMC test would need the locked OOS block and a human decision; not requested since the LEAD definition was not met.

### 2026-11-08: bls.gov refuses automated requests from the GitHub runner (E015 phase 1)
- **Context:** E015 (B12) phase 1, run 42484931936
- **Observation:** the BLS Employment Situation archive index returned HTTP 403 "Access Denied" to a self-identified research script.
- **Evidence label:** [EXP]
- **Lesson:** check before pre-registering that a data source permits automated access from the runner (or offers an official API). A 403 from the source is a stop, not something to engineer around.
- **Action:** B12 blocked pending a sanctioned source (e.g. FRED API key secret, human-supplied official file). E015 kept preregistered, 0 trials.

### 2026-11-08 R027: an in-session 200 does not prove the runner can fetch
- **Context:** E016 (B13) phase 1, run 42500439921
- **Observation:** the CME settlement PDF opened from this workspace in R026 (HTTP 200), but all three CME URLs timed out (60 s, no HTTP answer) from the GitHub runner.
- **Evidence label:** [EXP]
- **Lesson:** source-access checks must be made from the runner's network, not this workspace. Fetch scripts should retry transport errors with a longer timeout (never refusals) and record per-attempt statuses.
- **Action:** one re-fetch queued with retries; a second failure blocks B13 (stop rule written before the result).

### 2026-11-08 R028: cmegroup.com does not answer the GitHub runner (E016 blocked)
- **Context:** E016 (B13) phase-1 re-fetch, run 42504753112
- **Observation:** with a 120 s timeout and 3 attempts per URL, all three official CME pages again gave no HTTP answer to the runner.
  Two of the last three event/calendar items (B12 bls.gov 403, B13 cmegroup.com timeouts) are now blocked on source access, not on data.
- **Evidence label:** [EXP]
- **Lesson:** official US agency/exchange sites often block or silently drop cloud-runner traffic. When refilling the backlog, prefer
  tests whose inputs are already in the repo (price data, committed calendars) or whose source has a documented API; flag any new
  external source as an access risk before pre-registration.
- **Action:** B13 blocked (0 trials). Next ready item B14 (home-hours depreciation, val only) needs no external source.

### 2026-11-08 R030: exits next to the 17:00 NY roll are expensive (E017)
- **Context:** E017 (B14) val, US leg exit at the 16:59 NY bar.
- **Observation:** median spread at 16:59 NY was 3.0 pips vs 0.3 at 03:00, 07:59 and 12:00 NY; a +2.18-pip mid mean became -0.38 at SPEC 4.
  The mid mean also rested on few large days (hit 0.516, binomial p 0.45).
- **Evidence label:** [EXP]
- **Lesson:** do not place entries or exits within the last minutes before the 17:00 NY roll; pre-register exits at or before 16:45 NY
  (or after the roll has normalised) and check the spread at every fixed timestamp in pre-registration, not after. A positive mean with a
  ~0.5 hit rate is a fat-tail effect, not a steady drift.
- **Action:** B14 closed. Backlog has no `ready` items -> next run refills.

### 2026-11-08 R033: no round-number stop cascades in 2015-2020 EUR/USD (E018)
- **Context:** E018 (B15) dev, first crossing of 00/50 levels per trading date, 60-minute continuation.
- **Observation:** mean -0.128 pips, hit 0.488 (n 2143); no horizon (15/60/120 min) positive; only 2015 positive by year. Control
  levels (23/73) had a mean of -0.803 with CI below 0, so after any first level crossing the mid tended to drift back slightly.
- **Evidence label:** [EXP]
- **Lesson:** a 1990s dealer-order mechanism (Osler) did not survive into the modern electronic EUR/USD market at the 1-pip bar. A
  descriptive control result (mild reversal after arbitrary level crossings) is not evidence; it needs its own pre-registration and fresh data.
- **Action:** B15 closed. Next ready item B16 (12-month TSMOM, daily hold, dev).

### 2026-11-09 R035: single-pair 12-month TSMOM has no daily edge on 2016-2020 EUR/USD (E019)
- **Context:** E019 (B16) dev, sign of the 252-trading-date 16:00 NY mid change, held 16:00 -> 16:00 NY next trading date.
- **Observation:** mean -0.644 pips/day, CI (-3.196, 1.978), t p 0.678 (n 1292); short days -1.516, long days +0.475; buy-and-hold over
  the same days +1.06. Only 77 round trips, so costs were small (SPEC 4 net -0.674/day); the failure is in the signal, not the costs.
- **Evidence label:** [EXP]
- **Lesson:** a portfolio-level published premium (58 futures, decades) does not transfer to one pair over five test years at a 1-pip/day
  bar; the CI half-width (~2.6 pips/day) was close to the pre-registered power note. Daily-horizon tests on one pair need either a large
  expected effect or a longer sample than dev offers.
- **Action:** B16 closed. Backlog has no `ready` items -> next run refills.

### 2026-11-09 R038: no weekend-gap reversal in 2015-2020 EUR/USD (E020)
- **Context:** E020 (B17) dev, fade weekends with |Fri 16:00 -> Sun 20:00 NY gap| > rolling p67 of 26 weekends, exit Mon 16:00 NY.
- **Observation:** n 90, mean -1.574 pips, median -7.425, hit 0.378, CI (-12.699, 7.03), t p 0.627. Descriptive: Sun 17:00-20:00 NY
  move against the gap -6.41 (CI excludes 0), Tue exit -12.743: large gaps tended to extend, not reverse. SPEC 4 net -2.108.
- **Evidence label:** [EXP]
- **Lesson:** a spot-FX weekend-overreaction result from a multi-currency study did not transfer to modern EUR/USD; with ~90 events per
  dev block, weekend-conditioned tests can only detect effects of ~10 pips. The extension reading is post-hoc and not evidence.
- **Action:** B17 closed. Next ready item B18 (next-session reversal after a large daily move, dev).

### 2026-11-09 R040: no next-session reversal after large daily moves in 2015-2020 EUR/USD (E021)
- **Context:** E021 (B18) dev, fade non-Friday dates with |16:00 -> 16:00 NY move| > rolling p80 of 60 valid dates, 20:00 NY D -> 10:45 NY next trading date.
- **Observation:** n 229, mean -2.55 pips, median -0.5, hit 0.493, CI (-7.097, 4.167), t p 0.776. Control (non-large dates) -0.415.
  Up moves +6.625, down moves -12.133 signed (mirrors the dev downtrend; post-hoc). SPEC 4 net -3.041.
- **Evidence label:** [EXP]
- **Lesson:** the 1988-2003 currency-futures intraday reversal after large 1-day returns did not transfer to 2015-2020 EUR/USD spot.
  Third consecutive multi-day / event-conditioned reversal or momentum idea (E019 TSMOM, E020 weekend gap, E021 large-day reversal)
  to come back NONE; dev SEs of 2.5-5 pips per event mean only large daily-horizon effects are detectable on one pair.
- **Action:** B18 closed. Backlog has no `ready` items -> next run refills.

### 2026-11-09 R043: pre-ECB-fix short on high-vol dates gives a marginal dev SIGNAL (E022)
- **Context:** E022 (B19) dev, short EUR/USD 02:00 -> 08:15 NY on dates whose prior trading-date mid range > rolling p67 of 60 valid dates.
- **Observation:** n 473, mean +3.646 pips, hit 0.535, CI (0.011, 7.751), t p 0.0133 -> SIGNAL. Control normal dates +1.731 (CI incl 0),
  all dates +2.339 (CI excludes 0). 2015-2016 carry much of it; 2018 negative. SPEC 4 net +3.139, x1.5 +2.886.
- **Evidence label:** [EXP]
- **Lesson:** first dev SIGNAL after a long run of NONE/WEAK, but marginal (CI lower 0.011) after ~236 trials; the vol-state
  conditioning is not shown to add to an unconditional European-morning USD-up drift. Treat as a hypothesis for val, not a finding.
- **Action:** B19 done; B19v (val confirmation, rule unchanged) queued ahead of B20.

### 2026-11-09 R045: the marginal pre-ECB-fix dev SIGNAL does not confirm on val (E023)
- **Context:** E023 (B19v), val confirmation of E022 with the rule unchanged and a val-only burn-in.
- **Observation:** n 204, mean +1.197 pips, median -2.875, hit 0.471, CI (-3.144, 5.919), t p 0.304 -> NONE. Normal val dates +1.15,
  all val dates +1.167: the high-vol conditioning adds nothing. Dev weekday pattern did not repeat.
- **Evidence label:** [EXP]
- **Lesson:** a dev SIGNAL with CI lower bound near 0 after ~236 trials was chance-sized, as cautioned in R043. The val step did its
  job. Any residual European-morning USD-up drift is ~1 pip, below costs-robust size and already seen on both dev and val.
- **Action:** B19 line closed (E022 + E023 in rejected_hypotheses.md). Next: B20 (dev).

### 2026-11-09 R047: post-London-fix long on high-vol dates gives a dev SIGNAL (E024)
- **Context:** E024 (B20) dev, long EUR/USD 11:05 -> 16:00 NY on dates whose prior trading-date mid range > rolling p67 of 60 valid dates.
- **Observation:** n 472, mean +2.983 pips, hit 0.534, CI (0.566, 4.847), t p 0.0053 -> SIGNAL. Control normal dates +0.901 (CI incl 0),
  all dates +1.562 (CI excludes 0). Excluding 12 FOMC days +3.143. 2018-2019 negative. SPEC 4 net +2.515, x1.5 +2.281.
- **Evidence label:** [EXP]
- **Lesson:** second dev SIGNAL from the same vol-state condition (after E022, which failed val in E023). Clearer than E022, but the
  conditioning is again not shown to add to an unconditional drift, and two of six years are negative. Val decides.
- **Action:** B20 done; B20v (val confirmation, rule unchanged) added as the top `ready` item.

### 2026-11-09 R049: the post-London-fix dev SIGNAL does not confirm on val either (E025)
- **Context:** E025 (B20v), val confirmation of E024 with the rule unchanged and a val-only burn-in.
- **Observation:** n 204, mean +0.582 pips, median 0.575, hit 0.510, CI (-1.992, 3.14), t p 0.369 -> NONE. Normal val dates -0.053,
  all val dates +0.172, excl FOMC -0.298. x1.5 net -0.197.
- **Evidence label:** [EXP]
- **Lesson:** both vol-state-conditioned fix-window dev SIGNALs (E022, E024) failed val. With ~238 trials, dev SIGNALs whose own
  normal-date control is not clearly weaker should be expected to fail val; the prior-day range condition has shown no incremental value.
- **Action:** B20 line closed (E024 + E025 in rejected_hypotheses.md). Backlog has no `ready` item -> refill next.

### 2026-11-09 R052: no continuation after large 08:30 NY moves (E026)
- **Context:** E026 (B21), calendar-free test of the order-flow continuation mechanism after US 08:30 NY releases, dev only.
- **Observation:** n 169, mean -0.42 pips, CI (-5.278, 2.488), t p 0.564 -> NONE; non-event control -0.465; p80/p95 and other horizons
  (descriptive) also not positive. SPEC 4 net -0.896.
- **Evidence label:** [EXP]
- **Lesson:** published order-flow incorporation of news (Evans-Lyons, Love-Payne) does not translate into a tradable 2-hour drift after
  the first 15 minutes of the 08:30 NY window on 2015-2020 EUR/USD. Papers that describe a mechanism without a stated horizon have
  produced NONE repeatedly; prefer items whose source states a tradable horizon.
- **Action:** B21 closed (rejected_hypotheses.md). B22 is the next `ready` item.

### 2026-11-09 R054: no London-open intraday momentum into the pre-fix half hour (E027)
- **Context:** E027 (B22), loose EUR/USD analogue of exchange-session intraday momentum (Elaut et al. 2018, RUB/USD), dev only.
- **Observation:** n 1551, mean -0.008 pips, CI (-0.553, 0.455), t p 0.511 -> NONE; slope of last half hour on r1 insignificant;
  first-hour variant and |r1| terciles (descriptive) not positive. SPEC 4 net -0.46.
- **Evidence label:** [EXP]
- **Lesson:** exchange open/close mechanisms (overnight inventory aversion) do not transfer to 24-hour EUR/USD via a London-session
  proxy. With n ~1,500 the CI is tight (+/-0.5 pip), so this is a clean null, not a power problem. Prefer hypotheses whose mechanism
  exists in the spot FX market itself.
- **Action:** B22 closed (rejected_hypotheses.md). No `ready` item -> refill next.

### 2026-11-09 R057: no real-time intraday continuation on overreaction days (E028)
- **Context:** E028 (B23), real-time version of Caporale & Plastun (2019) overreaction-day continuation, dev only.
- **Observation:** n 74, mean +1.061 pips, CI (-5.625, 8.569), t p 0.390 -> NONE; non-event long control +1.108; k 1.5 / 2.5
  (descriptive) not positive. SPEC 4 net +0.507.
- **Evidence label:** [EXP]
- **Lesson:** rare-event conditioning (2-SD days, ~12 events a year) gives SE ~4 pips on dev; only effects of ~+8 pips per event can
  pass the rule. Tail-day hypotheses need a much larger expected effect, or a longer sample, to be worth a trial. A subset split that
  looks good (up-moves) mirrors the unconditional afternoon drift and is not a new hypothesis.
- **Action:** B23 closed (rejected_hypotheses.md). B24 (val only) is the next `ready` item.

### 2026-11-10 R059: a roll-hour entry can make a test untestable (E029)
- **Context:** E029 (B24), val-only fade of the 17:05 -> 02:00 NY overnight session after a 2-SD open-to-close day.
- **Observation:** 34 events, but 19 were skipped by the pre-registered 2.0-pip entry-spread cap at 17:05 NY (median entry spread of
  events 3.6 pips) and 9 were Fridays -> 4 tested -> insufficient sample -> NONE.
- **Evidence label:** [EXP]
- **Lesson:** entries within ~10 minutes of the 17:00 NY roll hit the daily spread widening, and more so after large-move days. Before
  pre-registering any test that enters near the roll, check the entry-spread distribution on the **dev** block (descriptive, no
  returns) and size the power note on events that pass the spread cap, not on raw events.
- **Action:** B24 closed (rejected_hypotheses.md, as untestable at this entry, not as a rejected effect). Refill next.

### 2026-11-10 R062: a USD/JPY calendar effect did not carry to EUR/USD (E030)
- **Context:** E030 (B25), short EUR/USD into the Tokyo fix on gotobi dates, dev.
- **Observation:** gotobi mean +0.180 pips vs non-gotobi control +0.411 (n 458 / 1097); NONE. Only the month-end gotobi subset was
  positive (n 72, +2.639, CI includes 0), read post-hoc.
- **Evidence label:** [EXP]
- **Lesson:** order-flow effects documented in USD/JPY (gotobi dollar demand from Japanese importers) are not visible in the EUR/USD
  USD leg at a size that clears costs. Treat cross-pair transfers of Tokyo-fix mechanisms as low-prior. Month-end subsets keep
  appearing post-hoc (E007, E030); they stay exploratory unless pre-registered on fresh data with a human decision.
- **Action:** B25 closed (rejected_hypotheses.md). B26 (post-fix, gotobi) is next; its prior is lowered by this result, but its
  pre-registered rule is unchanged.

### 2026-11-10 R064: a calendar subset that matches its control adds nothing (E031)
- **Context:** E031 (B26), long EUR/USD in the hour after the Tokyo fix on gotobi dates, dev.
- **Observation:** gotobi mean +0.799 pips (WEAK) vs non-gotobi control +0.778 (n 460 / 1096); difference +0.021.
- **Evidence label:** [EXP]
- **Lesson:** when a parent effect is already present on all dates (E011 post-fix, WEAK), a subset test mostly re-measures the parent
  at lower power. Pre-registered subset tests should report the subset-minus-control difference as a descriptive check (done here),
  and future refills should prefer mechanisms that predict a *difference* from the control, or a new signal, over date restrictions
  of a known WEAK effect.
- **Action:** B26 closed (rejected_hypotheses.md); gotobi Tokyo-fix line closed on dev. Refill next.

### 2026-11-10 R067: dev hourly cells summed into a window did not carry over to val (E032)
- **Context:** E032 (B27), long EUR/USD over the KMW post-Tokyo window 20:55 -> 02:00 NY, val only (dev contaminated by E009 cells).
- **Observation:** the E009 dev cells implied about +1.2 pips; val gave -0.534 (n 636, CI (-1.606, 0.669)), NONE.
- **Evidence label:** [EXP]
- **Lesson:** a window built by summing small, individually insignificant dev hour cells (plus a published effect from an earlier
  sample) is a weak prior. The post-Tokyo-fix reversal now has: dev first hour WEAK (E011), gotobi subsets NONE/WEAK (E030/E031),
  val full window NONE (E032). Further Tokyo-fix windows on dev or val would be specification search on a closed line.
- **Action:** B27 closed (rejected_hypotheses.md). Tokyo-fix line closed on dev and val. Refill next.

### 2026-11-10 R070: Dukascopy daily volume does not condition next-day EUR/USD returns (E033)
- **Context:** E033 (B28+B29), dev, next-day reversal after low unexpected volume and continuation after high unexpected volume,
  20:00 NY D -> 16:55 NY D+1, 2 trials.
- **Observation:** low-UV reversal -2.034 pips (n 426), high-UV continuation -0.213 (n 391), both NONE; all-dates reversal control
  -0.417. UV correlates with the daily range (0.275), so it mostly re-measures volatility. Per-event SD 52-61 pips.
- **Evidence label:** [EXP]
- **Lesson:** daily-hold signals on EUR/USD need effects of ~4-5 pips per event to be detectable on dev (SE ~2.5-3 pips), which
  published daily-frequency FX effects rarely reach. This is the fourth daily-frequency reversal/momentum idea to come back NONE
  (E019, E020, E021, E033). Future refills should prefer intraday windows (lower SD) or mechanisms with a stated effect size that
  clears the power bar.
- **Action:** B28 and B29 closed (rejected_hypotheses.md). Refill next.

### 2026-11-10 R073: month-end equity-hedging signal is NONE on dev; strong post-hoc cells are not leads (E034)
- **Context:** E034 (B30), dev, -sign(EU50 minus US500 month-to-date return) into the month-end 16:00 London fix, 2 windows, n 71.
- **Observation:** HOUR +1.731, DAY +3.354 pips, both NONE and both below unconditional long EUR/USD (+3.076 / +12.501). The
  descriptive US-only leg on the DAY window is +23.082 (t p 0.0001) but it was one of ~12 descriptive cells per window and shares
  most of its sign with the unconditional long (US equities rose in most dev months).
- **Evidence label:** [EXP]
- **Lesson:** with n ~70 events, descriptive cells will regularly show p < 0.01 by chance and through overlap with drift. A refill may
  pre-register such a cell only on val (dev is used), only against the unconditional-long control, and counted as a new trial; the
  val month-end sample (~29) makes that low power (lesson E014). Month-end/fix lines now: E007 pre/post-fix (parked/NONE), E034 NONE.
- **Action:** B30 closed, B31 closed unearned (rejected_hypotheses.md). Refill next.

### 2026-11-10 R076: daily overnight move does not reverse intraday; the 20-date smoothed overnight fade is a dev SIGNAL (E035)
- **Observation:** B32 (-sign of the 17:05 -> 07:00 NY move, hold 07:00 -> 16:55 NY) -0.285 pips, NONE, slope about 0. B33
  (-sign of the 20-date sum of overnight moves) +2.695 pips, CI (0.47, 5.027), t p 0.0093, SIGNAL; SPEC 4 net +2.047, x1.5 +1.723.
  B33 is front-loaded (2015 +8.9; 2019-2020 below +1) and agrees with B32 on only ~half of dates.
- **Evidence label:** [EXP]
- **Lesson:** the fourth dev SIGNAL of the project; all three earlier ones (E013, E022, E024) returned NONE on val
  (E014, E023, E025). With ~252 trials, a single p 0.009 is
  expected by chance; treat val (B34) as the test and do not tune the window, tercile or hold on dev. Smoothed-signal arms can pass
  where the raw daily signal is flat, so the pre-registered pairing of raw + smoothed arms was worth its extra trial.
- **Action:** B32 closed (rejected_hypotheses.md). B34 now `ready`: B33 arm unchanged on val, 1 val trial, p < 0.05.
