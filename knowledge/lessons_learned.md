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
