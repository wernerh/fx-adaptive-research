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
