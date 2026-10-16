#!/usr/bin/env python3
"""Historical wallet scan (public data-api only). Writes copy/wallets.jsonl, copy/cohorts.json."""
import json, urllib.request, random, statistics, os, time
from concurrent.futures import ThreadPoolExecutor
D = os.path.dirname(os.path.abspath(__file__)); API = "https://data-api.polymarket.com"
def get(path):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(API+path, headers={"user-agent": "paper-sim"}), timeout=15) as r: return json.load(r)
        except Exception: time.sleep(1+i)
    return None
wallets = {}
for period in ["DAY", "WEEK", "MONTH", "ALL"]:
    for order in ["PNL", "VOL"]:
        for off in range(0, 2000, 50):
            r = get(f"/v1/leaderboard?timePeriod={period}&orderBy={order}&limit=50&offset={off}")
            if not r: break
            for x in r: wallets.setdefault(x["proxyWallet"].lower(), "leaderboard")
print("leaderboard wallets", len(wallets), flush=True)
for off in range(0, 10000, 500):
    r = get(f"/trades?limit=500&offset={off}")
    if not r: break
    for x in r: wallets.setdefault(x["proxyWallet"].lower(), "recent_trades")
print("total wallets", len(wallets), flush=True)
def scan(w):
    pos = []
    for off in range(0, 1000, 50):
        r = get(f"/closed-positions?user={w}&limit=50&offset={off}")
        if not r: break
        pos += r
        if len(r) < 50: break
    if not pos: return {"wallet": w, "source": wallets[w], "resolved": 0}
    wins = [p for p in pos if p["realizedPnl"] > 0]; losses = [p for p in pos if p["realizedPnl"] <= 0]
    wp = [p["avgPrice"] for p in wins]
    allp = [p["avgPrice"] for p in pos]
    return {"wallet": w, "source": wallets[w], "resolved": len(pos), "wins": len(wins), "losses": len(losses),
            "win_rate": len(wins)/len(pos), "pnl": sum(p["realizedPnl"] for p in pos),
            "bought_usd": sum(p["totalBought"]*p["avgPrice"] for p in pos),
            "avg_win_entry": sum(wp)/len(wp) if wp else None,
            "share_entries_ge95": sum(1 for x in allp if x >= 0.95)/len(allp),
            "worst_loss": min((p["realizedPnl"] for p in pos), default=0), "capped_at_1000": len(pos) >= 1000}
with ThreadPoolExecutor(6) as ex, open(os.path.join(D, "wallets.jsonl"), "w") as f:
    for i, r in enumerate(ex.map(scan, list(wallets))):
        r["never_lose"] = r["resolved"] >= 10 and r.get("losses") == 0
        r["near_certain_buyer"] = bool(r.get("avg_win_entry") and r["avg_win_entry"] >= 0.95 or r.get("share_entries_ge95", 0) >= 0.5)
        f.write(json.dumps(r)+"\n")
        if i % 500 == 0: print("scanned", i, flush=True)
rows = [json.loads(l) for l in open(os.path.join(D, "wallets.jsonl"))]
RULE = ("resolved>=30 AND pnl>0 AND win_rate>=0.70 AND NOT near_certain_buyer (avg winner entry<0.95 and <50% of entries >=0.95); "
        "rank by pnl/bought_usd (ROI), take top 50")
elig = [r for r in rows if r["resolved"] >= 30 and r["pnl"] > 0 and r["win_rate"] >= 0.70 and not r["near_certain_buyer"]]
elig.sort(key=lambda r: r["pnl"]/max(r["bought_usd"], 1), reverse=True)
top = [r["wallet"] for r in elig[:50]]
pool = [r["wallet"] for r in rows if r["resolved"] >= 30 and r["wallet"] not in top]
random.seed(42); rnd = random.sample(pool, min(50, len(pool)))
json.dump({"rule": RULE, "random_rule": "50 random wallets with >=30 resolved positions, not in top cohort (seed 42)",
           "top": top, "random": rnd, "eligible_count": len(elig)}, open(os.path.join(D, "cohorts.json"), "w"), indent=1)
print("done", len(rows), "eligible", len(elig))
