# Implementation specification v0.1

Turns docs/MASTER_PROMPT.md into rules the pipeline and agents can enforce.
Thresholds marked **(default)** are judgement calls chosen before any data was seen. Change them only with
a dated entry in section 11 that gives the reason. Never change them after seeing results to make a strategy pass.

---

## 1. Scope and autonomy

| Item | Decision |
|---|---|
| Instrument | EUR/USD only until at least one strategy reaches `oos_validated` or is rejected |
| Autonomy | Research, backtesting and paper trading. **No live orders.** |
| Holding time | Not fixed. Every strategy is tested at 5, 15, 30, 60 min and session-end exits; evidence decides |
| Data frequency | 1-minute bid/ask bars (tick data later if 5-minute holds look viable) |
| Agent platform | Claude Code subagents (`.claude/agents/`) driving a deterministic Python pipeline |

## 2. Session definitions

All sessions are anchored to the **local clock** of their financial centre and converted with the IANA tz database.
Implemented in `src/fxresearch/sessions.py` and tested in `tests/test_sessions.py`.

| Session | Local window | UTC (Northern winter) | UTC (Northern summer) | DST |
|---|---|---|---|---|
| Asia | 09:00-15:00 Asia/Tokyo | 00:00-06:00 | 00:00-06:00 | Japan has none |
| London | 08:00-12:00 Europe/London | 08:00-12:00 | 07:00-11:00 | UK: last Sun Mar / last Sun Oct |
| US | 08:00-12:00 America/New_York | 13:00-17:00 | 12:00-16:00 | US: 2nd Sun Mar / 1st Sun Nov |

- **Trading day** rolls at **17:00 New York**. A bar belongs to trading date D if (New York time + 7h) falls on D.
- Intervals are half-open `[start, end)`. Timestamps mark bar **open**.
- **London ends before the US starts on every day** (tested over a full year), so all London features are known at the US open.
- **DST mismatch weeks** (US and UK change on different dates; about three weeks in March and one in Oct/Nov):
  London-to-New York offset is 4h instead of 5h. These days are kept but reported separately as a robustness check.
- Why London 08:00-12:00 and not a full London day: it gives a clean pre-US window. The London/New York overlap
  (from 08:00 NY) belongs to the US session for this research. The 16:00 London WM/Reuters fix falls at 11:00 NY,
  inside the US window. Its effect is a known confound (see research/).
- Alternatives (such as an "Asian range" from 00:00 to 07:00 London time) may be tested as a single-variable experiment.

## 3. Data

| Requirement | Rule |
|---|---|
| Primary source | Dukascopy 1-minute bid and ask, 2015-01-01 onwards, via `dukascopy-node` |
| Schema | `data/data_dictionary.md`. Mid is always derived, never stored |
| Quality gate before any experiment | Missing trading minutes < 1%, no crossed quotes, median spread recorded, p99 spread recorded. Save the report to `data/data_quality_reports.md` |
| Volume | Tick volume only. Strategies needing true traded volume (classic VWAP) must state this limitation |
| Spread realism | Before paper trading, compare broker spreads by hour against Dukascopy. If the broker's median spread is > 1.5x, re-run validation with the broker's spread profile |
| Economic calendar | Needed for event filters (S005 and robustness checks). Must include historical UTC timestamps and importance. Source TBD |

## 4. Cost model and fill rules

Implemented in `src/fxresearch/backtest.py` and tested in `tests/test_backtest.py`.

| Component | Default | Notes |
|---|---|---|
| Spread | **Actual bid/ask from data** | Longs buy at ask and exit at bid; shorts the reverse |
| Slippage | 0.1 pip per side on entry and stop exits **(default)** | Targets fill at the limit price (no positive slippage) |
| Commission | 0.1 pip per round trip **(default)** | About an ECN rate of $5 per $1m per side |
| Max spread at entry | 2.0 pips | Entry skipped if wider |
| Entry fill | Open of the first bar at or after the signal time | A signal from a bar's close is stamped open + 1 min |
| Stop and target in one bar | **Stop assumed first** | Conservative; overstates losses for wide bars |
| Gaps through stop | Fill at the worse bar open | |
| Overlapping trades | Not allowed per strategy | |
| Cost stress (required for promotion) | Costs x1.5 and x2 | Strategy must stay positive at x1.5 |

**Known bias:** 1-minute bars cannot show the order of prices inside a minute. For holds under about 10 minutes,
confirm results on tick data before promotion.

## 5. Validation design

### 5.1 Splits (`src/fxresearch/splits.py`)

| Block | Dates | Use |
|---|---|---|
| dev | 2015-01-01 to 2020-12-31 | Exploration, design, walk-forward |
| embargo | 20 days | Separates blocks so rolling features cannot cross |
| val | 2021-01-21 to 2023-06-30 | Confirm dev findings; limited re-use |
| embargo | 20 days | |
| **OOS** | 2023-07-21 to latest | **Locked.** Once per strategy version, after the dev/val conclusion is written |

The blocks cover different regimes: low-volatility negative rates (2015-19), COVID (2020), the 2022 hiking cycle
and dollar spike (val), and the post-2023 period (OOS).

### 5.2 Required checks before promotion
1. **Walk-forward:** 3-year train / 6-month test rolling folds over dev+val. Fixed parameters must be positive in at least 60% of folds **(default)**.
2. **Parameter sensitivity:** each parameter +/-20%. Expectancy must not change sign.
3. **Random-entry benchmark:** the same number of trades, with random entry times in the same window and the same stop, target and hold, over 1,000 runs. The strategy must beat the 95th percentile.
4. **Year-by-year:** no single year contributes more than 50% of total net P&L.
5. **Event exclusion:** results with high-impact event days removed must still pass.
6. **Multiple testing:** every predictor or variant tried is counted in `experiment_registry.csv`. Report the Bonferroni-adjusted p-value and, for strategies, the Deflated Sharpe Ratio (Bailey & López de Prado, 2014) using the total number of trials.

### 5.3 Statistics
- Signal tests (E001-type): hit rate with Wilson CI, binomial p, Spearman IC, moving-block bootstrap CI of mean signed return.
- Strategy tests: t-stat of per-trade net pips, Sharpe from **daily** P&L including zero-trade days, block-bootstrap CI of expectancy.

## 6. Promotion gates

| To status | Evidence required **(defaults)** | Sign-off |
|---|---|---|
| `research_candidate` | Written hypothesis and mechanism; a predictor or rules definable without look-ahead | Any agent |
| `backtest_validated` | dev+val: >= 200 trades (>= 80 in val); net expectancy > 0 in BOTH blocks; combined t-stat >= 2.0; profit factor >= 1.15; all of 5.2 checks 1-5 pass; costs x1.5 still positive | Validation agent |
| `oos_validated` | OOS: >= 80 trades; net expectancy > 0 and >= 50% of val expectancy; max drawdown <= 1.5x val max drawdown | Validation agent + **risk reviewer APPROVE** |
| `paper_validated` | >= 100 paper trades AND >= 3 months; realised slippage <= 1.5x modelled; paper expectancy within the backtest's 95% CI | Risk reviewer APPROVE |
| `approved_for_live_consideration` | All of the above plus a written risk memo | **Named human only** |

**Demotion:** any later evidence that fails the gate for the current status moves the strategy down one level
(or to `suspended`), with a dated entry. Rejected strategies keep their history.

## 7. Time-in-market evaluation

Every strategy result reports: average and median hold, % closed within 5 / 15 / 30 min, net pips per exposure hour,
MAE, MFE, win rate after costs, and costs as a share of gross P&L.

To compare short against long holds, run the same entry with exits at 5, 15, 30, 60 min and session end.
Prefer the shorter hold only if its **net expectancy per trade is not significantly lower** (overlapping block-bootstrap CIs)
and its pips per exposure hour are higher. Never shorten a hold if costs exceed 50% of gross P&L.

## 8. Experiment protocol

1. Pre-register `hypothesis.md` and `methodology.md`, including the decision rule, **before** running.
2. One major variable changed versus the parent experiment.
3. Results come from script output only, saved as JSON or CSV under `backtests/validation_reports/`.
4. Conclusions are append-only; superseded conclusions link to the new one.
5. Every run updates `experiment_registry.csv`, the knowledge files, the logs, and commits.

**Experiment roadmap (dependency order):**
- **E001** Session direction baseline (cost-free). Gates everything below.
- **E002** If E001 finds SIGNAL: the strategy built on the strongest predictor at the 5/15/30/60/session-end exit grid, on dev.
- **E003** E001 by volatility regime (asia_range_atr terciles) and with event days excluded.
- **E004** Asian range breakout (S001) on dev, run regardless of E001, since it is a London-session trade.
- **E005** US window split at the London 4pm fix (08:00-10:55 vs 11:05-12:00 NY), following Krohn, Mueller & Whelan (2024).
- Later: S005 data release reaction (needs calendar data), S004 VWAP reversion (tick-volume caveat).

## 9. Agent architecture

| Agent (master prompt #) | Claude Code agent | Writes to |
|---|---|---|
| Market Research Analyst (1) | `market-research-analyst` | research/, knowledge/market_structure.md |
| Asian / London / US analysts (2-4) | `session-analyst` (merged; the computation is shared code) | knowledge/*_session_findings.md |
| Quant Strategy Researcher (5) | `quant-strategy-researcher` | src/fxresearch/strategies/, strategies/ |
| Backtesting and Validation (6) | `validation-agent` | backtests/ |
| Risk Management (7) | `risk-reviewer` | risk/, strategy_registry.md approvals |
| Learning and Knowledge (8) | `knowledge-manager` | experiments/, knowledge/, agent_logs/ |

The three session analysts are merged because their numbers come from one feature pipeline. Separate agents would
produce three inconsistent interpretations of the same data. The independence that matters is kept:
**the strategy author never validates or risk-approves its own strategy.**

## 10. Known limitations (v0.1)

- Bar-based fills with the stop assumed first (conservative but imprecise for very short holds).
- Dukascopy is a single venue; EUR/USD trades across many venues and dealers. Its spreads may be tighter than your broker's.
- Tick volume is not traded volume.
- No economic calendar yet, so event filters cannot run.
- Session windows are fixed defaults. Alternatives must be tested explicitly, not tuned.
- **Not yet implemented in code** (required before the first `backtest_validated` promotion): walk-forward runner
  (fold generator exists in `splits.py`), parameter-sensitivity runner, random-entry benchmark, cost-stress runner,
  Deflated Sharpe Ratio, Monte Carlo drawdown resampling, economic-calendar loader, paper-trading harness.

## 11. Change log

| Date | Change | Reason |
|---|---|---|
| 2026-11-07 | v0.1 created | Initial specification from master prompt |
| 2026-11-07 | v0.1.1: E001 adds `unconditional_long` benchmark and fix-split breakdown; E005 added | Literature review (research/academic_studies.md) |
