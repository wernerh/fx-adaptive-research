# Strategy registry

Machine-readable source of truth: `strategy_registry.csv`. This file explains statuses and history.

## Status ladder (docs/SPEC.md section 6)

`research_candidate` -> `backtest_validated` -> `oos_validated` -> `paper_validated` -> `approved_for_live_consideration`

Any status can also move to `rejected` or `suspended`. Promotions need the gate evidence linked and risk-reviewer sign-off from `oos_validated` upwards.
Approval for live consideration needs explicit **human** sign-off, recorded here with name and date.

## History

| Date | Strategy | From | To | Evidence | Approved by |
|---|---|---|---|---|---|
| 2026-11-07 | S001 to S006 | none | research_candidate | Initial research list | repo init |
