# Run protocol for agents working in this repo

You are part of the Adaptive FX research team. This repo is the team's only long-term memory.
Read docs/SPEC.md before changing any code, parameter or status.

## Hard rules

1. **No live trading.** Nothing in this repo may place orders. Paper trading only after a strategy reaches `oos_validated` and the risk reviewer approves.
2. **Numbers come from code.** Every performance figure must come from a script output saved under `backtests/` or `experiments/`. Never estimate, round up or recall figures.
3. **No invented references.** Every citation in `research/` needs a working link or DOI that you actually opened. Mark anything unverified as `UNVERIFIED`.
4. **Append, never rewrite.** Do not edit past results or conclusions. Supersede them with a new dated entry that links to the old one. Rejected hypotheses stay in `knowledge/rejected_hypotheses.md`.
5. **The OOS block is locked.** Evaluate a strategy version on `oos` only once, only after its dev/val conclusion is written, and record it in `experiments/experiment_registry.csv` (`oos_touched=yes`).
6. **One variable at a time.** Each experiment changes one major variable from its parent experiment.
7. **No trade is a valid result.** Never loosen filters to produce trades.

## Start of every run

1. `git pull`
2. Read: `README.md`, `strategies/strategy_registry.csv`, `experiments/experiment_registry.csv`, `knowledge/lessons_learned.md`, `knowledge/rejected_hypotheses.md`, and the latest entry in `agent_logs/research_run_log.md`.
3. List open questions (`Next experiment` fields, unresolved items in lessons).
4. Pick the single highest-value question. Write why in `agent_logs/agent_decision_log.md`.
5. `pytest` must pass before running any experiment.

## End of every run

1. Create `experiments/YYYY-MM-DD_EXXX_<slug>/` from `templates/experiment_template.md` (hypothesis, methodology, results, conclusion, plus `record.json`).
2. Append a row to `experiments/experiment_registry.csv`.
3. Update the relevant `knowledge/*.md` and `strategies/*.md` with dated entries.
4. Update `strategies/strategy_registry.csv` if a status changed (promotion needs the gates in SPEC section 6).
5. Append to `agent_logs/research_run_log.md`.
6. Commit: `EXXX: <what was tested> -> <one-line result>`.

## Commands

```bash
pytest
python scripts/run_e001_baseline.py [--synthetic] [--include-oos]
python scripts/run_backtest.py <strategy> --block dev|val|oos --experiment EXXX [--synthetic]
```
