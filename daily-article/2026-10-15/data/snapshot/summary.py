#!/usr/bin/env python3
import json, os, statistics, datetime
D = os.path.dirname(os.path.abspath(__file__))
def rd(f):
    p = os.path.join(D, f); return [json.loads(l) for l in open(p)] if os.path.exists(p) else []
ev, op, fi, rs, er = map(rd, ["events.jsonl", "opportunities.jsonl", "fills.jsonl", "resolutions.jsonl", "errors.jsonl"])
st = json.load(open(os.path.join(D, "state.json"))) if os.path.exists(os.path.join(D, "state.json")) else {"cash": 100, "positions": []}
start = datetime.datetime.fromisoformat([e for e in ev if e["event"] == "start"][0]["ts"])
hrs = (datetime.datetime.now(start.tzinfo) - start).total_seconds() / 3600
print(f"Running since {start:%Y-%m-%d %I:%M %p} ET ({hrs*60:.0f} min); markets rolled: {sum(e['event']=='roll' for e in ev)}")
print(f"Opportunities (sum of asks + fees < $1): {len(op)}  -> {len(op)/hrs if hrs else 0:.1f}/hour")
if op:
    print(f"  median edge at detection: {statistics.median(o['edge_c'] for o in op):.2f}c/set; median best edge: {statistics.median(o['best_edge_c'] for o in op):.2f}c")
    print(f"  median gap duration: {statistics.median(o['duration_s'] for o in op):.1f}s; median raw sum ${statistics.median(o['sum'] for o in op):.3f}")
    print(f"  median top-of-book size Up/Down: {statistics.median(o['up_size'] for o in op):.0f}/{statistics.median(o['dn_size'] for o in op):.0f} sh")
surv = [f for f in fi if f["survived"]]; filled = [f for f in fi if f.get("filled")]
print(f"Fill attempts: {len(fi)}; survived 300-500ms latency: {len(surv)} ({100*len(surv)/len(fi) if fi else 0:.0f}%); filled >= min size: {len(filled)}")
pnl = sum(r["pnl"] for r in rs); lo = [r["leftover_pnl"] for r in rs if r["leftover_pnl"]]
print(f"Resolved positions: {len(rs)}; realized P&L ${pnl:.4f}; open positions: {len(st['positions'])} (cost ${sum(p['cost'] for p in st['positions']):.2f})")
print(f"Cash ${st['cash']:.2f} of $100 bankroll")
print(f"Directional leftovers: {sum(1 for x in lo if x>0)} won / {sum(1 for x in lo if x<=0)} lost (${sum(lo):.2f}) [leftovers off by default: only matched sets are bought]")
ms=rd("market_stats.jsonl")
if ms: print(f"Near-miss: {len(ms)} markets; lowest raw Up+Down ask sum seen ${min(m['min_raw_sum'] for m in ms):.3f}; median of per-market medians ${statistics.median(m['median_raw_sum'] for m in ms):.3f}")
print(f"API errors logged: {len(er)}")

# ---- copy-trading paper module ----
C = os.path.join(D, "copy")
def rc(f):
    p = os.path.join(C, f); return [json.loads(l) for l in open(p)] if os.path.exists(p) else []
if os.path.exists(os.path.join(C, "follow_state.json")):
    fst = json.load(open(os.path.join(C, "follow_state.json"))); cps, cls = rc("copies.jsonl"), rc("closes.jsonl")
    print("\n== Copy-trading paper module ==")
    for c in ("top", "random"):
        b = [x for x in cps if x["cohort"] == c and x["action"] == "buy"]; sk = [x for x in cps if x["cohort"] == c and x["action"] == "skip"]
        cl = [x for x in cls if x["cohort"] == c]; s = fst[c]
        openv = sum(p["cost"] for p in s["pos"].values())
        print(f"[{c}] copies {len(b)} (skipped {len(sk)}); closed {len(cl)}: {sum(1 for x in cl if x['pnl']>0)} won / {sum(1 for x in cl if x['pnl']<=0)} lost"
              f" ({100*sum(1 for x in cl if x['pnl']>0)/len(cl) if cl else 0:.0f}% win); realized P&L ${sum(x['pnl'] for x in cl):.2f}; "
              f"cash ${s['cash']:.2f} + open cost ${openv:.2f} ({len(s['pos'])} pos)")
        if b: print(f"      avg slippage vs wallet entry (incl fee): {statistics.mean(x['slippage_c'] for x in b):+.2f}c/share")
    hb = os.path.join(C, "heartbeat"); print("  follower heartbeat:", open(hb).read() if os.path.exists(hb) else "none")
