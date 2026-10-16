# Verdict (plain language) - Oct 15 2026
Nothing was traded, changed, or stopped.

## Kraken (~$105.69 in BTC/ETH/SOL)
- **Edge after costs on held-out data? No.** There are no written buy/sell rules, so in practice it's buy-and-hold. The best rule-based version I could build made +7.2% on the held-out 7 months vs **+14.9% for just holding** the same mix. It lowered the worst drop (15% vs 31%) but earned less.
- **Doing nothing (cash)** would have beaten everything in the first 17 months (hold: -41%).
- **Top 3 risks:** (1) Crypto falling: a repeat of the 57% drop in this data would hit the $60 floor (needs ~-43%). (2) No rules: "no setup justified" isn't testable, and the ADA round trip cost money. (3) Logging gap: an ADA->SOL swap and a SOL withdrawal (Oct 11-12) aren't in trades.log. Worth confirming you made that withdrawal.

## Polymarket arbitrage (paper)
- **Edge? No.** 0 opportunities in 134 markets, even assuming perfect zero-delay fills. Up+Down never cost under $1.0012 after fees. Only with no fees would 2 tiny gaps (20 cents total) appear.
- **Top 3 risks:** fees erase all gaps; fast bots take any gap first; the main exchange blocks US users (the US app is under a NY lawsuit).

## Polymarket copy-trading (paper, still being built)
- **Edge? Can't tell yet, and the data feeding it is wrong.** The wallet scan says 1,186 wallets "never lose". That's false: Polymarket's closed-positions list mostly shows winners. One "1,000 wins, 0 losses" wallet actually holds 28 dead bets worth -$2.14M. Picking "top wallets" from that list picks lucky, hidden-loss wallets. That's exactly the trick in the post you asked about.
- **Fix before trusting results:** count losses from /positions (price 0 = loss) too, then pick cohorts. The random comparison group is the right idea, so keep it.
- **Top 3 risks:** fake win rates; copying late at worse prices; top-by-profit picks are mostly luck.

## What could blow up this account?
Kraken: a broad crypto crash (-43%) hits $60. An unlogged manual trade or withdrawal skips the rules. A leaked API key (trade-only, so funds can't be withdrawn, but could be churned in bad trades). Polymarket: nothing, it's paper. If ever made real: putting money in on fake "never lose" stats, and geoblock/legal freezes.
