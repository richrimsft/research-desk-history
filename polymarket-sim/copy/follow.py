#!/usr/bin/env python3
"""Paper copy-trader: follows cohorts in copy/cohorts.json using public data only. No orders, no keys."""
import json, urllib.request, time, random, os, datetime, threading
from zoneinfo import ZoneInfo
ET = ZoneInfo("America/New_York"); D = os.path.dirname(os.path.abspath(__file__))
DATA = "https://data-api.polymarket.com"; GAMMA = "https://gamma-api.polymarket.com/markets"; CLOB = "https://clob.polymarket.com/book"
CAP = 5.0; MIN_SH = 5; BANK = 100.0; CYCLE = 60
lock = threading.Lock()
def now_et(): return datetime.datetime.now(ET).isoformat(timespec="seconds")
def log(fn, o):
    o.setdefault("ts", now_et())
    with lock, open(os.path.join(D, fn), "a") as f: f.write(json.dumps(o)+"\n")
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"user-agent": "paper-sim"}), timeout=10) as r: return json.load(r)
_mk = {}
def market(cid):
    if cid not in _mk or time.time()-_mk[cid][0] > 600:
        r = get(f"{GAMMA}?condition_ids={cid}") or get(f"{GAMMA}?condition_ids={cid}&closed=true")
        _mk[cid] = (time.time(), r[0] if r else None)
    return _mk[cid][1]
def fee(p, m):
    fs = (m or {}).get("feeSchedule") or {}
    if not (m or {}).get("feesEnabled"): return 0.0
    return fs.get("rate", 0) * (p*(1-p)) ** fs.get("exponent", 1)
cfg = json.load(open(os.path.join(D, "cohorts.json")))
sp = os.path.join(D, "follow_state.json")
st = json.load(open(sp)) if os.path.exists(sp) else {c: {"cash": BANK, "pos": {}, "seen": {}} for c in ("top", "random")}
def save():
    with lock: json.dump(st, open(sp, "w"))
def copy_buy(c, t):
    time.sleep(random.uniform(3, 10))
    s = st[c]; rec = {"cohort": c, "wallet": t["proxyWallet"], "title": t["title"], "outcome": t["outcome"], "asset": t["asset"],
                      "their_price": t["price"], "their_ts": datetime.datetime.fromtimestamp(t["timestamp"], ET).isoformat()}
    try:
        m = market(t["conditionId"]); b = get(f"{CLOB}?token_id={t['asset']}")
    except Exception as e: rec.update(action="skip", reason=f"api {e!r}"); log("copies.jsonl", rec); return
    asks = sorted((float(a["price"]), float(a["size"])) for a in b.get("asks", []))
    budget = min(CAP, s["cash"]); sh = cost = 0.0
    for p, z in asks:
        u = p + fee(p, m); take = min(z, (budget-cost)/u)
        if take <= 0: break
        sh += take; cost += take*u
    if not asks or sh < MIN_SH:
        rec.update(action="skip", reason="no asks" if not asks else f"only {sh:.2f} sh affordable/on book (<5)"); log("copies.jsonl", rec); return
    avg = cost/sh
    with lock:
        s["cash"] -= cost; k = t["asset"]; p0 = s["pos"].get(k, {"sh": 0, "cost": 0, "cid": t["conditionId"], "title": t["title"], "idx": t.get("outcomeIndex"), "wallet": t["proxyWallet"]})
        p0["sh"] += sh; p0["cost"] += cost; s["pos"][k] = p0
    rec.update(action="buy", shares=round(sh, 3), cost=round(cost, 4), our_avg_incl_fee=round(avg, 4), slippage_c=round((avg-t["price"])*100, 2)); log("copies.jsonl", rec); save()
def copy_sell(c, t):
    time.sleep(random.uniform(3, 10)); s = st[c]; k = t["asset"]
    if k not in s["pos"]: return
    try: m = market(t["conditionId"]); b = get(f"{CLOB}?token_id={k}")
    except Exception as e: log("errors.jsonl", {"where": "sell", "err": repr(e)}); return
    bids = sorted(((float(x["price"]), float(x["size"])) for x in b.get("bids", [])), reverse=True)
    with lock:
        p0 = s["pos"][k]; left = p0["sh"]; got = 0.0
        for p, z in bids:
            q = min(z, left); got += q*(p-fee(p, m)); left -= q
            if left <= 1e-9: break
        sold = p0["sh"]-left
        if sold <= 0: return
        basis = p0["cost"]*sold/p0["sh"]; s["cash"] += got; p0["cost"] -= basis; p0["sh"] = left
        if left <= 1e-9: s["pos"].pop(k)
    log("closes.jsonl", {"cohort": c, "how": "copied_exit", "title": t["title"], "shares": sold, "proceeds": got, "pnl": got-basis, "their_price": t["price"]}); save()
def resolve():
    for c in st:
        for k, p in list(st[c]["pos"].items()):
            try: m = market(p["cid"])
            except Exception: continue
            if not m or not m.get("closed"): continue
            op = [float(x) for x in json.loads(m["outcomePrices"])]; toks = json.loads(m["clobTokenIds"])
            val = op[toks.index(k)] if k in toks else 0.0
            if val not in (0.0, 1.0): continue
            with lock: st[c]["cash"] += p["sh"]*val; st[c]["pos"].pop(k)
            log("closes.jsonl", {"cohort": c, "how": "resolution", "title": p["title"], "shares": p["sh"], "proceeds": p["sh"]*val, "pnl": p["sh"]*val-p["cost"]})
    save()
def poll(c, w):
    try: tr = get(f"{DATA}/trades?user={w}&limit=50&takerOnly=false")
    except Exception as e: log("errors.jsonl", {"where": "trades", "wallet": w, "err": repr(e)}); return
    last = st[c]["seen"].get(w)
    if last is None: st[c]["seen"][w] = max([t["timestamp"] for t in tr], default=0); return  # baseline: only copy NEW trades
    new = sorted([t for t in tr if t["timestamp"] > last], key=lambda t: t["timestamp"])
    if new: st[c]["seen"][w] = new[-1]["timestamp"]
    for t in new:
        if time.time()-t["timestamp"] > 300: continue  # too stale to be a realistic copy
        threading.Thread(target=copy_buy if t["side"] == "BUY" else copy_sell, args=(c, t), daemon=True).start()
log("events.jsonl", {"event": "start"})
n = 0
while True:
    t0 = time.time()
    for c in ("top", "random"):
        for w in cfg[c]: poll(c, w); time.sleep(0.15)
    save(); n += 1
    if n % 5 == 1: resolve()
    open(os.path.join(D, "heartbeat"), "w").write(now_et())
    time.sleep(max(1, CYCLE-(time.time()-t0)))
