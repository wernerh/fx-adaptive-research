# S002 London false-breakout reversal

**Status:** research_candidate   **Module:** `not implemented`

## Hypothesis
When London breaks the Asian range but closes back inside it, the US session moves in the opposite direction to the break.

## Proposed market mechanism [ASSUMPTION until tested]
A break that fails may have triggered stops beyond the range (a 'liquidity sweep') without real follow-through, leaving trapped breakout traders.

## Rules (v0.1 defaults; see module `Params`)
- **Entry:** TBD after E001 (`lon_false_break_fade` predictor).
- **Stop:** TBD
- **Target:** TBD
- **Max hold:** TBD
- **Costs:** CostModel defaults (SPEC section 4)

## Evidence
| Type | Summary | Link |
|---|---|---|
| [PUB] | Take-profit clustering at round numbers supports reversals at levels (Osler 2003) | research/academic_studies.md |
| [BT] | none yet | |
| [EXP] | E001 (2026-11-07): `lon_false_break_fade` NONE (dev hit 48.1%, val 47.5%). Deprioritised. | experiments/2026-11-07_E001_session_direction_baseline |

## Version history
| Date | Version | Change | Experiment |
|---|---|---|---|
| 2026-11-07 | 0.1 | Initial definition | none |

## Notes
Not implemented. Implement only if E001 shows the predictor has signal in dev AND val.
