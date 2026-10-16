# Spec: Kraken strategy (as written + as actually run)
Source: /workspace/markets/RULES.md, trades.log, snapshots.log, kraken.py (API wrapper only - no strategy code exists).
- Universe: spot BTC/USD, ETH/USD, SOL/USD (ADA held Oct 10-11, then swapped back). Spot only, no leverage/margin/futures/shorts.
- Capital: ~$120 on Oct 9 ($10 SOL + $100 deposit); $105.69 on Oct 14 17:50 ET. Never add funds.
- Stop rule: stop trading below $60 total value. (Older $5 rule superseded.)
- Sizing: max 50% of USD cash per pair; limit orders only; max 2 new trades/day; user shown each order first.
- Entries: UNKNOWN. Logs say "no setup justified" but no setup is ever defined (no indicator, threshold, or timeframe).
- Exits / stop-loss / take-profit per position: UNKNOWN. Snapshots note "no rule-based exit" - none exists.
- Rebalance: UNKNOWN (none defined). In practice: bought ~42/33/25 BTC/ETH/SOL on Oct 9, then hold.
- Check cadence: twice a day (~09:45 and ~17:50 ET).
- Fees: Kraken Pro base 0.25% maker / 0.40% taker (account tier UNKNOWN; AssetPairs returned no fee schedule). Min order: BTC 0.00006, ETH 0.002, SOL 0.05, $0.50 cost min.
- Observed reality: it is a discretionary buy-and-hold with one rotation trade. USD left = $0.81, so it cannot trade at all without selling.
- Logging gap: the ADA->SOL swap and a SOL withdrawal between Oct 11 17:47 and Oct 12 10:06 ET are NOT in trades.log (only noted in a snapshot).
