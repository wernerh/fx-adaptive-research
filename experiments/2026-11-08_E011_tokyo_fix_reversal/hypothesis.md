# E011 Hypothesis: Tokyo 09:55 JST fix reversal (pre-registered 2026-11-08, before any run)

- **H1:** around the Tokyo fix (09:55 JST) the USD appreciates into the fix and depreciates after it. For EUR/USD: mid return
  over 08:55-09:55 Asia/Tokyo is negative on average (pre), and over 09:55-10:55 Asia/Tokyo positive (post).
- **H0:** the mean signed return (short pre / long post) is zero.
- **Mechanism [PUB]:** Krohn, Mueller & Whelan (2024, Journal of Finance) report USD appreciation into the Tokyo, ECB and London
  fixes and depreciation after (dealer hedging of unconditional USD demand). Citation as listed in research/academic_studies.md.
  The Tokyo fix is mainly a USD/JPY event; any EUR/USD effect would be the USD leg spilling over.
- **Parent experiment / variable changed:** none formally; sibling of E007/E010 (same test design and rule), variable changed =
  which fix (Tokyo 09:55 JST). Backlog B5.
- **Prior expectation:** low. London (E007, NONE) and ECB (E010, WEAK, +0.76 pips) versions were sub-pip on dev, and Asian-hours
  EUR/USD spreads are wider.
- **Known calendar notes (stated before data):** windows are 23:55-01:55 UTC, inside one FX trading date (17:00 NY roll), no DST
  in Japan. Japanese gotobi days (5th/10th/... ) are a known stronger-fix subset in USD/JPY; **not** tested here (would be extra trials).
- **Why now:** top `ready` backlog item (B5).
