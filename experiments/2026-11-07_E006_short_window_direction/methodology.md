# E006 Methodology (pre-registered before any run)

- **Data / blocks:** same as E001; dev + val only, OOS locked.
- **Outcome:** mid close of the last bar before the window end minus mid open of the first bar in the window, per trading date.
- **Statistics:** as E001. **Bonferroni multiplier = 14** (7 predictors x 2 windows).
- **Decision rule (pre-registered, same structure as E001):**
  - SIGNAL if Bonferroni p < 0.05 in dev AND same sign with unadjusted p < 0.05 in val AND mean signed pips > 1.0 in both blocks
    AND it beats `unconditional_long` in the same window and block.
  - WEAK if significant in one block only, or mean signed pips <= 1.0.
  - NONE otherwise.
- Also reported: mean |window return| per block, to show how large any edge would have to be relative to about 1 pip of costs.
- **Command:** `python scripts/run_e006_short_window.py`
