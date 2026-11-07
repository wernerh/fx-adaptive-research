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
