# S006 US session early momentum

**Status:** research_candidate   **Module:** `not implemented`

## Hypothesis
Direction of the first 15 to 30 minutes of the US session (or the post-08:30 data move) predicts the next 30 to 60 minutes.

## Proposed market mechanism [ASSUMPTION until tested]
Information arriving at US data releases is absorbed over minutes, not instantly; early order flow may persist.

## Rules (v0.1 defaults; see module `Params`)
- **Entry:** TBD
- **Stop:** TBD
- **Target:** TBD
- **Max hold:** TBD
- **Costs:** CostModel defaults (SPEC section 4)

## Evidence
| Type | Summary | Link |
|---|---|---|
| [PUB] | Announcement surprises cause conditional-mean jumps (Andersen et al. 2003) | research/academic_studies.md |
| [PUB] | Intraday momentum in currency futures toward the close (Baltussen et al. 2021) | research/academic_studies.md |
| [BT] | none yet | |
| [EXP] | none yet | |

## Version history
| Date | Version | Change | Experiment |
|---|---|---|---|
| 2026-11-07 | 0.1 | Initial definition | none |

## Notes
Not implemented. Needs an economic calendar source (see data/data_dictionary.md).
