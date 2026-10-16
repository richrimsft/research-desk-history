#!/usr/bin/env python3
"""Polymarket audit (read-only). Uses the sim's own recorded order-book stats
(/workspace/polymarket-sim/market_stats.jsonl: per 5-min market min/median of best-ask Up+Down) -
Polymarket has no public historical order-book archive, so this live-recorded tape is the only honest data.
Arb rule: buy 1 Up + 1 Down when ask_up+ask_dn+fees < 1 - margin; payoff $1 at resolution.
Sweep margin and fee assumptions; first 70% of markets in-sample, last 30% held-out.
Upper bound: assumes fill at the per-market best moment with no latency (the live sim adds 300-500 ms)."""
import json
R = [json.loads(l) for l in open("/workspace/polymarket-sim/market_stats.jsonl")]
cut = int(len(R)*.7); IS, HO = R[:cut], R[cut:]
def ev(rows, margin, fee_mult):
    hits = []; 
    for r in rows:
        fee_part = r["min_sum_after_fees"] - r["min_raw_sum"]   # fee at that best moment
        s = r["min_raw_sum"] + fee_part*fee_mult
        if s < 1 - margin: hits.append(1 - s)
    return len(hits), round(sum(hits)*5, 4)  # $ profit if 5 sets (min size) each hit
print(f"markets={len(R)} in-sample={len(IS)} held-out={len(HO)}  ({R[0]['ts'][:16]} .. {R[-1]['ts'][:16]} ET)")
print("lowest raw sum", min(r['min_raw_sum'] for r in R), "lowest after fees", min(r['min_sum_after_fees'] for r in R))
for fm, lab in [(1, "real taker fees"), (0, "ZERO fees (fantasy)")]:
    for m in (0, .005, .01, .02):
        print(f"{lab:20} margin {m:<5}: IS hits/$ {ev(IS,m,fm)}  HO hits/$ {ev(HO,m,fm)}")
