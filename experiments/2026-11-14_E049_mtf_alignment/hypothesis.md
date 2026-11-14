# E049 Hypothesis: multi-timeframe trend alignment (1h + 30m + 15m), 5-minute EMA20-cross trigger (B59), dev only (pre-registered 2026-11-14 R156, before any run)

- **H1 (B59):** on the dev block, when the last completed UTC 1-hour, 30-minute and 15-minute EUR/USD bars all closed above (below)
  their own EMA20, a 5-minute bar closing between 07:00 London and 12:00 New York whose close crosses up (down) through its own
  EMA20 marks a long (short) entry at that 5m close; held 60 minutes, these trades earn a mean signed mid return > 1 pip per trade.
- **H0:** the mean signed return per trade is zero.
- **Origin [HUMAN / PRACTITIONER]:** the human described (2026-11-13, R153) establishing bull/bear on 1h, 30m and 15m and trading the
  5m/10m in the same direction when all agree; definitions were fixed in the backlog (R153) before any data was seen. No published
  EUR/USD evidence is claimed.
- **Mechanism (practitioner reading, not verified):** when several horizons trend the same way, a short pullback that resumes on the
  lowest timeframe joins the dominant flow (trend persistence across horizons).
- **Parent experiment / variable changed:** none (new family: multi-timeframe EMA alignment with lower-timeframe EMA-cross trigger).
  Fill/exclusion machinery reused unchanged from E045/E047/E048 (`round_numbers.build_trades`), hold 60 minutes, same time window
  and decision rule as E048.
- **Contamination note:** related, already-tested families: E048 (24h swing breakout + 5m retest, NONE, -0.744), intraday time-series
  momentum families (E024/E025/E032), Asian-range breakout (E004, rejected). None used EMA20 states or alignment; none was used to fix
  this rule. No B59 statistic has been computed in this repo. Dev usable.
- **Prior expectation:** low (technical-rule profits in developed FX largely gone: Neely-Weller 2011, Coakley-Marzano-Nankervis 2016,
  both in research/academic_studies.md; E048 NONE). ~268 registered trials after this one, so a single p just under 0.05 is expected
  noise (lesson R092); hence the separate B59v val confirmation.
- **Why now:** top `ready` backlog item (human-directed, runs after B58); last research-batch run 43528337777 (E048) recorded; nothing
  queued or in progress.
