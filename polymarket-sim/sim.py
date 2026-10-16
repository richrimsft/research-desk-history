#!/usr/bin/env python3
"""Paper-trading sim: Polymarket 5m BTC/ETH Up/Down complete-set arb. READ-ONLY public data. No orders, no keys."""
import json, time, random, urllib.request, datetime, os, sys
from zoneinfo import ZoneInfo
ET = ZoneInfo("America/New_York")
D = os.path.dirname(os.path.abspath(__file__))
GAMMA = "https://gamma-api.polymarket.com/markets"
CLOB = "https://clob.polymarket.com/books"
POLL = 1.0            # seconds between book polls (low CPU)
TRADE_USD = 9.0
BANKROLL0 = 100.0
MIN_SHARES = 5        # Polymarket orderMinSize for these markets
ASSETS = ["btc", "eth"]

def now_et(): return datetime.datetime.now(ET).isoformat(timespec="milliseconds")
def log(fn, obj):
    with open(os.path.join(D, fn), "a") as f: f.write(json.dumps(obj) + "\n")
def http(url, data=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data is not None else None,
          headers={"content-type": "application/json", "user-agent": "paper-sim/1.0"})
    with urllib.request.urlopen(req, timeout=5) as r: return json.load(r)
def err(where, e): log("errors.jsonl", {"ts": now_et(), "where": where, "err": repr(e)})

def get_market(slug, closed=False):
    r = http(f"{GAMMA}?slug={slug}" + ("&closed=true" if closed else ""))
    return r[0] if r else None

def fee_per_share(p, fs):
    rate = fs.get("rate", 0.07); ex = fs.get("exponent", 1)
    return rate * (p * (1 - p)) ** ex   # docs: fee = C*feeRate*p*(1-p) (exponent from market feeSchedule)

def asks(book):
    return sorted([(float(a["price"]), float(a["size"])) for a in book.get("asks", [])])

def books(tokens):
    res = http(CLOB, [{"token_id": t} for t in tokens])
    m = {b["asset_id"]: asks(b) for b in res}
    return [m.get(t, []) for t in tokens]

def buy(levels, usd, fs, max_shares=None):
    """Walk ask levels; spend up to usd (incl fee). Returns shares, cost."""
    sh = cost = 0.0
    for p, s in levels:
        unit = p + fee_per_share(p, fs)
        take = min(s, (usd - cost) / unit)
        if max_shares is not None: take = min(take, max_shares - sh)
        if take <= 0: break
        sh += take; cost += take * unit
    return sh, cost

class State:
    def __init__(s):
        s.cash = BANKROLL0; s.positions = []  # dicts awaiting resolution
        p = os.path.join(D, "state.json")
        if os.path.exists(p):
            j = json.load(open(p)); s.cash = j["cash"]; s.positions = j["positions"]
    def save(s): json.dump({"cash": s.cash, "positions": s.positions}, open(os.path.join(D, "state.json"), "w"))

def simulate_fill(st, mk, tokens, fs, signal):
    lat = random.uniform(0.3, 0.5); time.sleep(lat)
    try: up, dn = books(tokens)
    except Exception as e: err("refill", e); return
    if not up or not dn: return
    s_after = up[0][0] + fee_per_share(up[0][0], fs) + dn[0][0] + fee_per_share(dn[0][0], fs)
    survived = s_after < 1.0
    rec = {"ts": now_et(), "slug": mk["slug"], "latency_ms": round(lat*1000), "survived": survived,
           "sum_after_fees_after_latency": round(s_after, 4), "signal_sum_after_fees": signal}
    budget = min(TRADE_USD, st.cash)
    if survived and budget >= 1:
        # only buy levels where the pair still costs < $1 after fees; leg sizes limited to the book
        pairs_levels_up, pairs_levels_dn = [], []
        i = j = 0; uq = [list(x) for x in up]; dq = [list(x) for x in dn]; sh = 0.0; cost = 0.0
        while i < len(uq) and j < len(dq):
            pu, pd = uq[i][0], dq[j][0]
            unit = pu + fee_per_share(pu, fs) + pd + fee_per_share(pd, fs)
            if unit >= 1.0: break
            take = min(uq[i][1], dq[j][1], (budget - cost) / unit)
            if take <= 1e-9: break
            sh += take; cost += take * unit
            uq[i][1] -= take; dq[j][1] -= take
            if uq[i][1] <= 1e-9: i += 1
            if dq[j][1] <= 1e-9: j += 1
        if sh >= MIN_SHARES:
            st.cash -= cost
            pos = {"slug": mk["slug"], "sets": sh, "cost": cost, "up_extra": 0.0, "dn_extra": 0.0,
                   "end": mk["endDate"], "opened": now_et()}
            st.positions.append(pos); st.save()
            rec.update(filled=True, sets=round(sh, 3), cost=round(cost, 4), locked_edge=round(sh - cost, 4))
        else:
            rec.update(filled=False, reason=f"pair depth {sh:.2f} sh < min {MIN_SHARES} or budget")
    else:
        rec.update(filled=False, reason="gap closed after latency" if not survived else "no cash")
    log("fills.jsonl", rec)

def resolve(st):
    keep = []
    for p in st.positions:
        end = datetime.datetime.fromisoformat(p["end"].replace("Z", "+00:00"))
        if datetime.datetime.now(datetime.timezone.utc) < end + datetime.timedelta(seconds=30): keep.append(p); continue
        try: m = get_market(p["slug"], closed=True)
        except Exception as e: err("resolve", e); keep.append(p); continue
        if not m or not m.get("closed"): keep.append(p); continue
        op = [float(x) for x in json.loads(m["outcomePrices"])]
        payout = p["sets"] * 1.0 + p["up_extra"] * op[0] + p["dn_extra"] * op[1]
        st.cash += payout
        log("resolutions.jsonl", {"ts": now_et(), "slug": p["slug"], "winner": "Up" if op[0] > op[1] else "Down",
             "sets": p["sets"], "cost": p["cost"], "payout": payout, "pnl": payout - p["cost"],
             "leftover_pnl": p["up_extra"]*op[0] + p["dn_extra"]*op[1], "cash_after": st.cash})
    if len(keep) != len(st.positions): st.positions = keep; st.save()

def main():
    st = State(); cur = {}; gaps = {}; last_res = 0
    log("events.jsonl", {"ts": now_et(), "event": "start", "cash": st.cash})
    while True:
        t0 = time.time(); w = int(t0) // 300 * 300
        for a in ASSETS:
            slug = f"{a}-updown-5m-{w}"
            if cur.get(a, {}).get("slug") != slug:
                try:
                    m = get_market(slug)
                    if m:
                        o = cur.get(a)
                        if o and o.get("n"): log("market_stats.jsonl", {"ts": now_et(), "slug": o["slug"], "samples": o["n"], "min_raw_sum": o["min_raw"], "min_sum_after_fees": round(o["min_af"], 4), "median_raw_sum": sorted(o["raws"])[len(o["raws"])//2]})
                        cur[a] = {"slug": slug, "m": m, "tokens": json.loads(m["clobTokenIds"]), "fs": m.get("feeSchedule") or {"rate": 0.07, "exponent": 1}}
                        log("events.jsonl", {"ts": now_et(), "event": "roll", "slug": slug, "q": m["question"], "fee": cur[a]["fs"]})
                except Exception as e: err("gamma", e)
            c = cur.get(a)
            if not c or c["slug"] != slug: continue
            try: up, dn = books(c["tokens"])
            except Exception as e: err("book", e); continue
            if not up or not dn: continue
            fs = c["fs"]; pu, su = up[0]; pd, sd = dn[0]
            raw = pu + pd; af = raw + fee_per_share(pu, fs) + fee_per_share(pd, fs)
            c["n"] = c.get("n", 0) + 1; c["min_raw"] = min(c.get("min_raw", 9), raw); c["min_af"] = min(c.get("min_af", 9), af); c.setdefault("raws", []).append(round(raw, 3))
            g = gaps.get(a)
            if af < 1.0:
                if not g or g["slug"] != slug:
                    gaps[a] = {"slug": slug, "start": time.time(), "ts": now_et(), "up_ask": pu, "dn_ask": pd, "sum": raw,
                               "sum_after_fees": round(af, 4), "edge_c": round((1-af)*100, 3), "up_size": su, "dn_size": sd,
                               "best_edge_c": round((1-af)*100, 3), "secs_to_close": round(w+300-t0)}
                    simulate_fill(st, c["m"], c["tokens"], fs, round(af, 4))
                else: g["best_edge_c"] = max(g["best_edge_c"], round((1-af)*100, 3))
            elif g:
                g["duration_s"] = round(time.time() - g.pop("start"), 2); log("opportunities.jsonl", g); gaps.pop(a)
        for a, g in list(gaps.items()):   # close gaps from rolled markets
            if g["slug"] != f"{a}-updown-5m-{w}":
                g["duration_s"] = round(time.time() - g.pop("start"), 2); g["ended_by_rollover"] = True
                log("opportunities.jsonl", g); gaps.pop(a)
        if time.time() - last_res > 30: resolve(st); last_res = time.time()
        with open(os.path.join(D, "heartbeat"), "w") as f: f.write(now_et())
        time.sleep(max(0.05, POLL - (time.time() - t0)))

if __name__ == "__main__": main()
