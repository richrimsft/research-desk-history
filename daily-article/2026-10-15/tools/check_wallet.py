#!/usr/bin/env python3
"""check_wallet.py: does this Polymarket wallet really "never lose"? Public data only, no keys.
Usage: python3 check_wallet.py 0xWALLET"""
import json, sys, urllib.request
API = "https://data-api.polymarket.com"
def get(path):
    req = urllib.request.Request(API + path, headers={"user-agent": "wallet-check"})
    with urllib.request.urlopen(req, timeout=20) as r: return json.load(r)
w = sys.argv[1].lower()
closed = []                                   # 1) what the "never lose" posts read
for off in range(0, 1000, 50):
    page = get(f"/closed-positions?user={w}&limit=50&offset={off}")
    closed += page
    if len(page) < 50: break
wins = sum(p["realizedPnl"] > 0 for p in closed); losses = len(closed) - wins
print(f"RAW  /closed-positions : {len(closed)} closed, {wins} wins, {losses} losses"
      + ("  (hit the 1,000 cap: older history is invisible)" if len(closed) >= 1000 else ""))
opn = []                                      # 2) where the dead bets sit
for off in range(0, 2000, 500):
    page = get(f"/positions?user={w}&limit=500&offset={off}&sizeThreshold=0")
    opn += page
    if len(page) < 500: break
dead = [p for p in opn if p["curPrice"] <= 0.001 and (p["redeemable"] or p["curPrice"] == 0)]
unred = [p for p in opn if p["redeemable"] and p["curPrice"] >= 0.999]
print(f"     /positions        : {len(opn)} open rows, {len(dead)} expired worthless (price 0), "
      f"{len(unred)} unredeemed winners")
print(f"     dead-bet P&L      : ${sum(p['cashPnl'] for p in dead):,.0f}")
W, L = wins + len(unred), losses + len(dead)
print(f"REAL record            : {W} wins, {L} losses -> win rate {100*W/max(W+L,1):.1f}%"
      f"  (raw said {100*wins/max(len(closed),1):.1f}%)")
worst = sorted(dead, key=lambda p: p["cashPnl"])[:3]
for p in worst: print(f"     worst dead bet    : ${p['cashPnl']:,.0f}  {p['title'][:60]} ({p['outcome']})")
