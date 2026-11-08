# E010 Hypothesis: ECB 14:15 CET reference-rate reversal (pre-registered 2026-11-08, before any run)

- **H1:** around the ECB euro foreign exchange reference rate (set at 14:15 CET/CEST) the USD appreciates into the fix and
  depreciates after it. For EUR/USD: mid return over 13:15-14:15 Europe/Berlin is negative on average (pre), and over
  14:15-15:15 Europe/Berlin positive (post).
- **H0:** the mean signed return (short pre / long post) is zero.
- **Mechanism [PUB]:** Krohn, Mueller & Whelan (2024, Journal of Finance) report USD appreciation into the Tokyo, ECB and London
  fixes and depreciation after (dealer hedging of unconditional USD demand). Citation as listed in research/academic_studies.md.
- **Parent experiment / variable changed:** none formally; sibling of E007 (same test design and rule), variable changed = which fix
  (ECB 14:15 CET instead of WM/Reuters 16:00 London). Backlog B4.
- **Prior expectation:** low. E007 found the London-fix version below 1 pip on dev (NONE).
- **Known calendar confound (stated before data):** the post window 14:15-15:15 Berlin contains 08:30 New York (US data releases,
  e.g. NFP, CPI) on most days (except DST-mismatch weeks). A positive post-window mean could be a USD-release effect, not a
  fix effect. If SIGNAL, the val confirmation must report the post window split by US release days vs other days before any
  lead claim (AUTONOMOUS_PROTOCOL lead criterion 4).
- **Why now:** top `ready` backlog item (B4).
