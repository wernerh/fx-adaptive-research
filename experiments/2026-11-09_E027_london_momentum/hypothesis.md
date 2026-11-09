# E027 Hypothesis: London-open intraday momentum into the pre-London-fix half hour (dev only; pre-registered 2026-11-09 R053, before any run)

- **H1 (B22):** on every valid dev trading date D, a position in the direction of the first London half-hour mid return
  r1(D) = mid 08:30 - mid 08:00 London, held from 15:25 to 15:55 London on D (the last half hour before the 16:00 London fix),
  earns a mean signed mid return > 1 pip per date.
- **H0:** the mean signed return per date is zero.
- **Mechanism [PUB]:** in RUB/USD (Moscow exchange) the first half-hour return predicts the last half-hour return, attributed to
  liquidity providers' reluctance to hold positions overnight (Elaut, Frömmel & Lampaert 2018, JFM 37, 35-51); market intraday
  momentum in equities (Gao, Han, Li & Zhou 2018, JFE) and futures incl. currencies (Baltussen et al. 2021, JFE); all VERIFIED
  (abstract) in research/academic_studies.md. EUR/USD has no exchange open/close; the London session is a **loose analogue**
  (flagged in R000). Every parameter was fixed in the backlog (R050) before any data, not taken from the papers.
- **Parent experiment / variable changed:** none formally. New variable relative to E001 (sign of the whole London session vs
  08:00-12:00 NY) and E007 (unconditional 15:00-16:00 London pre-fix return): conditioning the pre-fix half hour on the first London
  half hour.
- **Prior expectation:** low. Loose analogue; long run of NONE/WEAK on dev. n ~1,500, 30-min SD ~6-8 pips -> SE ~0.2 pips, so the
  binding bar is the 1.0-pip mean (costs ~0.5 pip round trip): a significant sub-pip effect is WEAK at best, by design.
- **Why dev is clean:** no 15:25-15:55 London return conditional on the first London half hour has been computed on dev (E001 used
  the whole session and a different target window; E007 was unconditional).
- **Why now:** top `ready` backlog item (B22) after B21/E026 closed NONE (R052).
