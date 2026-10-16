#!/usr/bin/env python3
"""viral_prompt.py: run the viral prompt "wallets with 100+ trades and 70%+ win rate, rank by profit"
on our 5,916-wallet scan, first on raw data (what a 4-minute scan sees), then on corrected data."""
import json
D = "/workspace/polymarket-sim/copy/"
C = [json.loads(l) for l in open(D + "corrected.jsonl")]
raw = [c for c in C if c["resolved"] >= 100 and c["win_rate"] >= 0.70]
fix = [c for c in C if c["c_resolved"] >= 100 and c["c_win_rate"] >= 0.70]
print(f"RAW       100+ resolved & 70%+ win rate: {len(raw):,} wallets (median win rate {100*sorted(c['win_rate'] for c in raw)[len(raw)//2]:.0f}%)")
print(f"CORRECTED 100+ resolved & 70%+ win rate: {len(fix):,} wallets")
gone = [c for c in raw if c["c_win_rate"] < 0.70]
print(f"  dropped below 70% once dead bets count: {len(gone):,} of {len(raw):,}")
cap = sum(c["capped_at_1000"] for c in fix)
print(f"  of the survivors, history capped at 1,000 rows (unverifiable): {cap:,}")
top = sorted(raw, key=lambda c: -c["pnl"])[:20]
print("Top 20 by RAW profit -> corrected:")
print(f"  raw profit ${sum(c['pnl'] for c in top)/1e6:,.1f}M  ->  corrected ${sum(c['c_pnl'] for c in top)/1e6:,.1f}M;"
      f"  raw win rate {100*sum(c['win_rate'] for c in top)/20:.0f}% -> {100*sum(c['c_win_rate'] for c in top)/20:.0f}% (average)")
