---
description: Run one full research cycle (load knowledge, one experiment, record, commit)
---

Run one research cycle following CLAUDE.md.

1. Use the knowledge-manager agent to load repo state and propose the next experiment. If $ARGUMENTS is given, treat it as the requested focus.
2. Confirm `pytest` passes.
3. If the experiment needs new evidence, use market-research-analyst.
4. Pre-register hypothesis and methodology in a new experiments/ folder BEFORE running anything.
5. Run the experiment with session-analyst (signal tests) or quant-strategy-researcher + validation-agent (strategy tests).
6. If any status promotion is proposed, use risk-reviewer. No promotion without APPROVE.
7. Use knowledge-manager to record results, update knowledge, and commit.
8. Finish with a 5-line summary: what was tested, result, decision, files updated, next experiment.

Never place orders. Never touch the OOS block unless the pre-registered methodology says so.
