# Spec: Polymarket paper simulator (read from /workspace/polymarket-sim, not modified)
## A. Complete-set arb (sim.py, running since Oct 14 3:07 PM ET)
- Markets: 5-min BTC and ETH Up/Down. Poll books every 1 s.
- Entry: buy matched Up+Down sets only while ask_up+fee+ask_dn+fee < $1.00, after a simulated 300-500 ms latency re-check of the book.
- Fee: rate 0.07 x p(1-p) per share (from market feeSchedule, taker-only). Size: $9/trade, $100 bankroll, min 5 shares.
- Exit: hold to resolution ($1 per set). No directional leftovers.
- UNKNOWN: queue position/whether we'd actually be filled at the touch; gas/withdrawal costs; legal access (main exchange geoblocks US).
## B. Copy-trading (copy/scan.py running, copy/follow.py built, cohorts.json not yet written)
- Cohort "top": wallets with >=30 resolved positions, pnl>0, win_rate>=70%, not near-certain buyers; top 50 by ROI. Control: 50 random wallets (seed 42).
- Copy: on a followed wallet's buy, wait 3-10 s, buy up to $5 at current asks incl. fee; skip if <5 shares. $100 bankroll per cohort, poll every 60 s.
- Exit: UNKNOWN in what I read (presumably hold to resolution; copying the leader's sells not confirmed).
- Data: data-api /closed-positions (win/loss), /trades, leaderboard.
