# Copy-trading scan: "14,000 wallets, 47 never lose" (paper test, public data only)

**Scanned:** 5,916 wallets on Oct 15, 2026, 2:55–4:10 AM ET. They came from the data-api leaderboard (DAY/WEEK/MONTH/ALL, ranked by PNL and by VOL, up to 2,000 deep: 8,254 unique) plus 1,610 wallets from the latest 10k public trades (9,864 in total). I stopped the scan early because data-api slowed to about 0.5 wallets/s. Nearly all scanned wallets came from the leaderboard; the recent-trade wallets mostly weren't reached.

## The data trap (an audit finding, now corrected)
`/closed-positions` returns closed positions sorted by profit, capped at 1,000. Bets that expired **worthless** don't appear there. They stay in `/positions` at curPrice 0. So a raw scan makes almost everyone look like they never lose.
Example: 0x6ac5…4b6e shows 1,000-0 raw. Corrected, it's 1,000-28, and the dead positions carry -$2.14M.

| | Raw (closed-positions only) | Corrected (+ dead or redeemable open positions) |
|---|---|---|
| Wallets with ≥10 resolved | 5,350 | 5,350 |
| "Never lose" | 1,808 | 315 |
| ...of those, history not capped at 1,000 | n/a | **7** |
| ...near-certain buyers (avg winning entry ≥95c or ≥50% of entries ≥95c) | 192 of 1,808 | 74 of 315; **4 of 7** |
| Median win rate | 85% | 55% |
| Wallets with P&L > 0 | 4,816 | 3,888 |
1,493 "never lose" wallets flipped once the dead positions were counted (-$560M of hidden losses). 2,119 wallets hit the 1,000 cap, so their real loss count is unknowable from this endpoint and they were excluded from the cohort.

**Conclusion:** "never lose" is almost entirely an artifact of the endpoint. The few genuine ones are mostly 95c+ buyers who pick up pennies, where one loss wipes out about 20 wins.

## Cohorts (cohorts.json)
- **top:** corrected stats, ≥30 resolved, P&L > 0, win rate ≥70%, not a near-certain buyer, not capped. Ranked by P&L / $ bought; top 50 of 181 eligible. Median corrected win rate 76%.
- **random:** 50 random wallets with ≥30 resolved, not in top, seed 42 (luck baseline). Median corrected win rate 53%.

## Live follow (follow.py)
Polls each wallet's /trades every 60s and copies only new trades (≤5 min old). For each copy it waits a random 3–10s, then buys at current CLOB asks walking real depth, plus the market's feeSchedule taker fee. $5 cap per copy, 5-share minimum, $100 bankroll per cohort. Copies the wallet's exits at bids, otherwise holds to Gamma resolution.
