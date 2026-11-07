# S003 London-to-US continuation

**Status:** research_candidate   **Module:** `london_us_continuation`

## Hypothesis
When London trends strongly (move >= 0.25 ATR, closes in top/bottom 25% of its range), the US session continues that direction in its first 30 minutes.

## Proposed market mechanism [ASSUMPTION until tested]
Order flow can be persistent across sessions as institutions execute large orders over hours. It may also reverse because of US data or the 16:00 London fix.

## Rules (v0.1 defaults; see module `Params`)
- **Entry:** US session open (08:00 New York) in the London direction.
- **Stop:** 0.20 x prior ATR.
- **Target:** 1.5R.
- **Max hold:** 30 minutes, never past US session end.
- **Costs:** CostModel defaults (SPEC section 4)

## Evidence
| Type | Summary | Link |
|---|---|---|
| [PUB] | Order flow drives short-run FX (Evans & Lyons 2002): mechanism support | research/academic_studies.md |
| [PUB] | ECB fix (~08:15 NY) and London fix (11:00 NY) cause USD reversals (Krohn et al. 2024): confound | research/academic_studies.md |
| [PUB] | 08:30 NY US data produces immediate jumps (Andersen et al. 2003): confound | research/academic_studies.md |
| [BT] | none yet | |
| [EXP] | none yet | |

## Version history
| Date | Version | Change | Experiment |
|---|---|---|---|
| 2026-11-07 | 0.1 | Initial definition | none |

## Notes
Key conflict: 08:30 NY US data releases fall inside the first 30 minutes. E00x must test with and without high-impact event days.
