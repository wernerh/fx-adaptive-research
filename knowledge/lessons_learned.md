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
