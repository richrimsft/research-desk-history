# Test report (Oct 15 2026, read-only: no orders, no config/key changes, simulators left running)
Re-run: `python3 backtest_kraken.py`, `python3 backtest_polymarket.py`. Raw output: kraken-results.txt, polymarket-results.txt.

## Kraken
Data: Kraken public daily OHLC, 721 days (Oct 24 2024 - Oct 14 2026). In-sample Oct 2024-Mar 11 2026; held-out Mar 12-Oct 14 2026 (30%, never tuned on).
The real strategy has no entry/exit rules, so it can't be backtested as written. Tested: (1) buy-and-hold of the live mix (= what it actually does), (2) do nothing, (3) a mechanical proxy "hold each coin only when yesterday's close > N-day average" so "no setup" has a meaning. Signal on day t-1 close, fill at day t open (no lookahead); 0.40% taker + 0.10% slippage per side; Kraken min sizes enforced.

| | In-sample | Held-out | Held-out max DD |
|---|---|---|---|
| Buy & hold mix | -41.3% | **+14.9%** | 30.9% |
| Do nothing | 0% | 0% | 0% |
| Trend SMA100 (best in-sample, frozen) | +9.2% | +7.2% | 14.9% |
| Trend SMA100, 2x costs | | +3.7% | 16.1% |

Sweep (N=5..100) in-sample: -69, -56, -33, -13, -0.3, +9%: one monotonic slope, not a plateau; short windows are destroyed by fees (SMA5 = 415 trades). Held-out: N=30..100 all +7 to +9% (a small plateau), but all lose to buy-and-hold. The filter only cut drawdown.
**Verdict: no edge after costs on held-out data. It underperforms buy-and-hold by ~8 points.** Live record agrees: ~$120 -> $105.69 (-12%) in 5 days, mostly market moves plus the ADA round trip and a SOL withdrawal.

## Polymarket arb
Data: the sim's own recorded books, 134 five-minute markets (Oct 14 3:25 PM - Oct 15 3:36 AM ET). No public historical order-book archive exists, so this is the only honest tape. Upper-bound test: fill at the best moment of each market with zero latency.
- With real fees: 0 opportunities in-sample and held-out at every margin (0, 0.5c, 1c, 2c). Lowest Up+Down after fees: $1.0012.
- With ZERO fees (fantasy): 1 hit in each half, $0.15 and $0.05 profit total.
- Live sim (with latency): 0 opportunities, 0 fills, $100 cash after 750 min.
**Verdict: no edge. Not even an upper bound shows profit.**

## Polymarket copy-trading (still being built: scan at ~3,100 of 9,864 wallets, cohorts not chosen, nothing followed yet)
No copy results to test yet. Data-quality test on the scan instead:
- 1,186 of 2,648 wallets with 30+ positions show **zero losses**; median win rate 91%. Not believable.
- Cause, verified: `/closed-positions` returns mostly redeemed (winning) positions sorted by profit, and is capped at 1,000 (1,375 wallets hit the cap). Losers that expire worthless stay in `/positions` at price 0. Example: wallet 0x6ac5...6e shows 1,000 wins / 0 losses, but has 28 dead positions worth **-$2.14M** in /positions.
- So win_rate, "never lose" and the top-cohort ROI ranking are all heavily survivorship-biased. The random-cohort control is good design, but the same bias hits both cohorts, so ranking skill is not measured.

## Adversarial review
| Check | Kraken | PM arb | PM copy |
|---|---|---|---|
| Lookahead | Clean (t-1 signal, t open fill) | Best-moment fill = optimistic, still 0 | follow.py uses live data: clean |
| Survivorship | Only coins that exist today (BTC/ETH/SOL - fine for this mix) | n/a | **SEVERE** (closed-positions bias) |
| Overfitting | Sweep picked edge value N=100; held-out still loses to B&H | nothing to fit | Top-50-by-ROI from 10k wallets = selection on luck |
| Unrealistic fills | Daily open fills; $35 orders ok | Ignores queue position; HFT takes gaps | 3-10 s delay modeled, good; no impact of others copying |
| Missing costs | Tier unknown, withdrawal fees ignored | Gas/USDC on/off-ramp ignored | same |
| Luck | 5 live days = noise | 12 h of data only | random cohort exists but biased data |
