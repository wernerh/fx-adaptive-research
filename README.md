# fx-adaptive-research

Long-term memory and research pipeline for the **Adaptive FX Trading Intelligence Team**.
Instrument: **EUR/USD**. Mode: **research, backtesting and paper trading only. No live execution.**

> Core question: can information from the Asian and London sessions give a statistically
> useful, cost-surviving edge for short-duration trades in the US session?
> This is a hypothesis to test, not an assumption. "No edge found" is a valid, recordable result.

## How the system is split

| Layer | What it does | Where |
|---|---|---|
| **Deterministic pipeline** (Python) | Loads data, labels sessions (DST-aware), builds features, runs predictive tests and backtests with bid/ask costs. Same inputs give the same outputs. | `src/fxresearch/`, `scripts/`, `tests/` |
| **Agents** (Claude Code subagents) | Read the repo, choose the next experiment, run the pipeline, interpret results, review risk, write knowledge files. Agents never compute performance numbers by hand. | `.claude/agents/`, `.claude/commands/` |
| **Knowledge base** (Markdown + CSV) | What has been tested, what failed, what is promising, what to do next. Append-only for conclusions. | `knowledge/`, `strategies/`, `experiments/`, `backtests/` |

The full rules (session definitions, cost model, validation splits, promotion gates) are in
**[docs/SPEC.md](docs/SPEC.md)**. The original brief is in [docs/MASTER_PROMPT.md](docs/MASTER_PROMPT.md).

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest                                  # 26 tests: DST, look-ahead, fill realism

# 1. Get data (Node.js). See scripts/ingest_dukascopy.py for exact commands.
npx dukascopy-node -i eurusd -from 2015-01-01 -to 2026-11-01 -t m1 -p bid -f csv -dir data/raw
npx dukascopy-node -i eurusd -from 2015-01-01 -to 2026-11-01 -t m1 -p ask -f csv -dir data/raw
python scripts/ingest_dukascopy.py data/raw/<bid>.csv data/raw/<ask>.csv

# 2. Experiment E001: is there any directional signal at all? (dev + val only)
python scripts/run_e001_baseline.py

# 3. Only if E001 finds something: backtest a strategy on the dev block
python scripts/run_backtest.py london_us_continuation --block dev --experiment E002
```

**No local machine needed:** the GitHub Action `.github/workflows/e001-data-baseline.yml` downloads the data,
runs E001 (dev + val only) and commits the raw outputs to `backtests/validation_reports/`. Start it from the
Actions tab, or by editing `.github/run-requests/e001.txt`. The processed parquet is kept as a 90-day run artifact.

Everything can be smoke-tested without data using `--synthetic` (random walk with no edge).

## Running a research cycle with Claude Code

```
/research-run
```

This follows the run protocol in [CLAUDE.md](CLAUDE.md): load knowledge, pick the highest-value open question,
run one controlled experiment, record results, update knowledge, commit.

## Current state

| Item | Status |
|---|---|
| Pipeline | v0.1, tested on synthetic data |
| Data | Dukascopy m1 bid/ask 2015-01-01 to 2026-10-30, quality gate passed (0.87% missing) |
| E001 session-direction baseline | **NONE**: no Asian/London predictor of US-morning direction (dev+val) |
| Strategies | All `research_candidate`; S002/S003 deprioritised after E001; S001 next (E004) |
| Live trading | Not permitted |

## Repository map

```
docs/            SPEC.md (implementation rules), MASTER_PROMPT.md (original brief)
knowledge/       findings by session, confirmed patterns, rejected hypotheses, lessons
strategies/      registry (CSV + MD) and one file per strategy
experiments/     experiment_registry.csv + one folder per experiment
backtests/       performance_summary.csv, validation_reports/, strategy_comparisons/
research/        literature review, microstructure notes, external research
risk/            risk framework, position sizing, trading restrictions
data/            data dictionary, data quality reports (raw data is git-ignored)
agent_logs/      research run log, agent decision log
templates/       experiment, strategy, daily session and lessons templates
src/fxresearch/  pipeline code      scripts/  CLI entry points      tests/  pytest suite
```
