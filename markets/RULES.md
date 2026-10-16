# Markets Desk rules (draft Oct 9 2026, ACTIVE: user approved Oct 9 2026 10:30am ET)
- Account: Kraken, ~$10.13 total (0.0913 SOL ~ $10.08 at $110.38 on Oct 9). No USD cash. API key is trade-only (no withdrawals). Never request withdrawal permission, never move funds off Kraken.
- Hard cap: this account only; never add funds. Max loss = account value.
- No leverage, no margin, no futures, no shorting. Spot only.
- Goal: grow the $10 as aggressively as spot-only allows; 1000x is NOT promised and not a target we chase with leverage.
- Orders under ~$5 face Kraken minimums and fees; fees can eat a $10 account fast. Prefer few, deliberate trades; no high-frequency.
- Every trade logged in /workspace/markets/trades.log (time, pair, side, size, price, reason).
- Stop rule: if account value drops below $5, stop trading and tell the user.
- Cost-aware: checks a few times a day at most, not every 30 min.

## Update Oct 9 2026 10:55am
- User deposited $100 USD; balance now ~$110 USD cash + ~$10 SOL (~$120 total). User's stated cap: $100 more only; never ask for more than that.
- Stop-trading line moves to $60 total value (50% of ~$120). Max 50% of USD cash deployed in any one pair. Use limit orders, not market orders, to cut fees. Max 2 new trades per day. Tell the user the plan before the first trade.

## Oct 9 2026 3:52pm: user chose Research Desk to trade Kraken. Signal stopped trading and paused the kraken-check routine. Rules above still apply (spot only, no leverage, show user each order first).
