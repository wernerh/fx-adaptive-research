# Autonomous research protocol

Applies to every unattended run (hourly scheduled task). Adds to CLAUDE.md and docs/SPEC.md and never overrides them.

## One run = at most one experiment step

Each run does exactly ONE of the following, in this priority order, then stops:

1. **Collect:** a batch run (research-batch workflow) finished since the last run and its outputs are not yet recorded.
   Record them per CLAUDE.md "End of every run". Apply the pre-registered decision rule exactly.
2. **Wait:** a research-batch run is `queued` or `in_progress`. Append one line to agent_logs/research_run_log.md
   ("waiting on run <id>") **only if** no such line already exists for that run. Otherwise do nothing and stop. Do not commit no-op changes.
3. **Next experiment:** take the top `ready` item in research/backlog.md:
   - write `hypothesis.md`, `methodology.md` and `record.json` with a decision rule **before** any run;
   - implement the code with tests (pytest must pass; add a "no edge on random walk" or no-look-ahead test where relevant);
   - append a `preregistered` row to experiments/experiment_registry.csv;
   - set `.github/run-requests/batch.sh` to the experiment's commands;
   - commit and push (this starts the workflow). Mark the backlog item `running`.
4. **Refill:** if no item is `ready`, run a literature/evidence pass (rules in CLAUDE.md: verified links only), then add 2-3 new
   pre-registrable items to the backlog, each with mechanism, data needs and a draft decision rule.

## Hard limits (never break these)
- No live trading or broker connections of any kind.
- **Never evaluate the OOS block.** OOS evaluation needs explicit human approval, recorded in agent_logs/agent_decision_log.md.
- Never change a decision rule, threshold, session definition or cost model after seeing results. Changes go in SPEC section 11 *before* a new experiment.
- Never re-run a finished experiment with tweaked parameters and report only the better result. A variant is a new experiment and a new trial.
- Keep `experiments/experiment_registry.csv` complete: every predictor/variant tested counts toward the trial total.
- Max one new experiment pushed per run. Max ~45 minutes of work per run.
- Never delete or rewrite past results (CLAUDE.md rule 4).

## What counts as a LEAD (the only reason to contact the human)
A result is a lead when **all** hold:
1. its pre-registered rule returns SIGNAL (signal tests) or PROCEED (strategy tests) on dev, **and**
2. a pre-registered val confirmation (run as its own experiment) also passes, **and**
3. the effect survives costs (mean net > 0 at the SPEC 4 cost model, and > 0 at costs x1.5), **and**
4. it is not explained by a known calendar effect already logged (fix, release time) unless that effect *is* the strategy.

When a lead is found: write `agent_logs/LEADS.md` (date, experiment IDs, one-paragraph summary, numbers with file links,
risks, the exact OOS command proposed), commit, and notify the human. Then **pause new experiments on that
line** until the human answers. Other backlog lines may continue.

Also notify the human (once, not every hour) if the pipeline has been broken for 3 consecutive runs
(e.g. data download, workflow failure) and you cannot fix it.

Do **not** notify for: NONE/REJECT results, WEAK results, routine progress, waiting.
