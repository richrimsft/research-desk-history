#!/usr/bin/env python3
"""Pick cohorts from CORRECTED stats. Writes cohorts.json."""
import json, os, random
D = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(D, "corrected.jsonl"))]
RULE = ("Corrected stats (closed-positions + dead/unredeemed open positions): c_resolved>=30 AND c_pnl>0 AND c_win_rate>=0.70 "
        "AND not near-certain buyer (avg winner entry<0.95 and <50% of entries >=0.95) AND closed history not capped at 1000; rank by c_pnl/c_bought_usd, top 50")
el = [r for r in rows if r["c_resolved"] >= 30 and r["c_pnl"] > 0 and r["c_win_rate"] >= 0.70 and not r["near_certain_buyer"] and not r["capped_at_1000"]]
el.sort(key=lambda r: r["c_pnl"]/max(r["c_bought_usd"], 1), reverse=True); top = [r["wallet"] for r in el[:50]]
pool = [r["wallet"] for r in rows if r["c_resolved"] >= 30 and r["wallet"] not in top]
random.seed(42); rnd = random.sample(pool, min(50, len(pool)))
json.dump({"rule": RULE, "random_rule": "50 random wallets with c_resolved>=30, not in top (seed 42)", "eligible_count": len(el),
           "top": top, "random": rnd}, open(os.path.join(D, "cohorts.json"), "w"), indent=1)
print("eligible", len(el))
