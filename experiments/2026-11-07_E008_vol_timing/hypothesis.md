# E008 Hypothesis: volatility timing (pre-registered 2026-11-07, before any run)

- **H1:** on days when the pre-US sessions are unusually active *relative to the prevailing volatility regime*, the US
  session moves more. Formally: the partial Spearman correlation between a pre-US session range (Asia 09:00-15:00 Tokyo,
  London 08:00-12:00 London; pips) and the absolute US-window return (pips), controlling for the prior 14-day ATR, is
  positive and economically meaningful (> 0.10).
- **H0:** partial correlation <= 0.10 (or not distinguishable from 0).
- **Not a direction test.** A USEFUL result does not trade anything; it becomes a candidate *filter* (when short-duration
  strategies should be active) and needs val confirmation (B2v) before use.
- **Mechanism [PUB]:** intraday activity and volatility follow regional trading hours (Ito & Hashimoto 2006); volatility
  clusters, so information arriving overnight may carry into the US session. Citations as in research/academic_studies.md.
- **Parent experiment / variable changed:** none (new question: magnitude, not direction). Uses E001 features.
- **Why now:** backlog B2 is the top `ready` item after E007 (B1) finished NONE. R002 decision log recommended (b) volatility timing.
