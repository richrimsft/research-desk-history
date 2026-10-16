#!/usr/bin/env python3
"""arb_check.py: is there a free dollar in Polymarket's 5-minute BTC/ETH Up/Down markets right now?
Buys 1 Up + 1 Down at the best asks. One of them pays $1 at the end. Public data only."""
import json, time, urllib.request
def get(url, data=None):
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None,
                                 headers={"content-type": "application/json", "user-agent": "arb-check"})
    with urllib.request.urlopen(req, timeout=10) as r: return json.load(r)
w = int(time.time()) // 300 * 300
for coin in ("btc", "eth"):
    m = get(f"https://gamma-api.polymarket.com/markets?slug={coin}-updown-5m-{w}")[0]
    fs = m["feeSchedule"]; up, dn = json.loads(m["clobTokenIds"])
    print(m["question"], "| fee:", fs)
    for i in range(5):
        books = {b["asset_id"]: b for b in get("https://clob.polymarket.com/books", [{"token_id": up}, {"token_id": dn}])}
        a = [min(float(x["price"]) for x in books[t]["asks"]) for t in (up, dn)]
        fee = sum(fs["rate"] * (p * (1 - p)) ** fs["exponent"] for p in a)   # docs: fee = rate x p(1-p) per share
        tot = a[0] + a[1] + fee
        print(f"  Up {a[0]:.3f} + Down {a[1]:.3f} = {a[0]+a[1]:.3f}  + taker fees {fee:.4f}  = ${tot:.4f}  -> "
              + ("ARB: profit %.2fc/set" % ((1-tot)*100) if tot < 1 else "no arb (costs more than the $1 payout)"))
        time.sleep(2)
