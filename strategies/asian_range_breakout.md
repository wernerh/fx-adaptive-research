# S001 Asian range breakout

**Status:** rejected (v0.1, 2026-11-07, E004)   **Module:** `asian_range_breakout`

## Hypothesis
The first decisive London break of the Asian range continues in the break direction over the next 60 minutes, after costs.

## Proposed market mechanism [ASSUMPTION until tested]
Asian-hours EUR/USD liquidity is thin and the range often reflects positioning, not information. The London open brings European order flow and information; a break may reflect informed flow that continues.

## Rules (v0.1 defaults; see module `Params`)
- **Entry:** first 1-minute mid close outside the Asian range during London (08:00 to 12:00 London); fill at next bar open.
- **Stop:** opposite side of the Asian range, capped at 25 pips (alt: 0.25 x prior ATR).
- **Target:** 1.0R.
- **Max hold:** 60 minutes, and never past London session end.
- **Costs:** CostModel defaults (SPEC section 4)

## Evidence
| Type | Summary | Link |
|---|---|---|
| [PUB] | Stop clusters beyond round numbers can accelerate breaks (Osler 2003): mechanism support | research/academic_studies.md |
| [PUB] | Intraday FX rules: no excess return after costs (Neely & Weller 2003): cautionary | research/academic_studies.md |
| [EXTERNAL] | Vendor 10-yr 1h backtest of a similar rule: PF 0.87, -28% (Backtrex) | research/external_research.md |
| [BT] | none yet | |
| [EXP] | none yet | |
| [BT] | E004 dev: 1,344 trades, 45.8% win, -0.684 pips/trade net, t=-1.96, PF 0.875; spread-only -0.484 | experiments/2026-11-07_E004_asian_range_breakout_dev |

## Version history
| Date | Version | Change | Experiment |
|---|---|---|---|
| 2026-11-07 | 0.1 | Initial definition | none |
| 2026-11-07 | 0.1 | Rejected by pre-registered rule | E004 |

## Notes
Filter: Asian range must be 0.15 to 0.60 of prior 14-day ATR. Very small ranges give noise breaks; very large ranges leave no room.
