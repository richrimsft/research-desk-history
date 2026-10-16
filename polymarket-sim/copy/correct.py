#!/usr/bin/env python3
"""Correction pass: closed-positions omits losers that expired worthless (they sit in /positions at curPrice 0).
For every scanned wallet with >=10 closed positions, add open positions with curPrice==0 (or redeemable & ~0) as losses,
redeemable at curPrice==1 as wins. Writes corrected.jsonl (resumable)."""
import json, os, urllib.request, time
from concurrent.futures import ThreadPoolExecutor
D = os.path.dirname(os.path.abspath(__file__))
def get(u):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"user-agent": "paper-sim"}), timeout=15) as r: return json.load(r)
        except Exception: time.sleep(1+i)
    return None
out = os.path.join(D, "corrected.jsonl")
done = {json.loads(l)["wallet"] for l in open(out)} if os.path.exists(out) else set()
rows = [json.loads(l) for l in open(os.path.join(D, "wallets.jsonl"))]
todo = [r for r in rows if r["resolved"] >= 10 and r["wallet"] not in done]
def fix(r):
    pos = []
    for off in range(0, 2000, 500):
        x = get(f"https://data-api.polymarket.com/positions?user={r['wallet']}&limit=500&offset={off}&sizeThreshold=0")
        if not x: break
        pos += x
        if len(x) < 500: break
    dead = [p for p in pos if p["curPrice"] <= 0.001 and (p["redeemable"] or p["curPrice"] == 0)]
    unred = [p for p in pos if p["redeemable"] and p["curPrice"] >= 0.999]
    c = dict(r); c["dead_open"] = len(dead); c["dead_open_pnl"] = sum(p["cashPnl"] for p in dead)
    c["c_wins"] = r["wins"] + len(unred); c["c_losses"] = r["losses"] + len(dead)
    n = c["c_wins"] + c["c_losses"]; c["c_resolved"] = n; c["c_win_rate"] = c["c_wins"]/n
    c["c_pnl"] = r["pnl"] + c["dead_open_pnl"] + sum(p["cashPnl"] for p in unred)
    c["c_bought_usd"] = r["bought_usd"] + sum(p["initialValue"] for p in dead + unred)
    c["c_never_lose"] = c["c_losses"] == 0
    return c
with ThreadPoolExecutor(4) as ex, open(out, "a") as f:
    for c in ex.map(fix, todo): f.write(json.dumps(c)+"\n"); f.flush()
print("corrected", len(todo))
