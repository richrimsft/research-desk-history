#!/usr/bin/env python3
"""Kraken audit backtest. Public daily OHLC (data/*.json, fetched from api.kraken.com/0/public/OHLC).
Strategies: (1) buy-and-hold of the live mix, (2) do nothing (cash), (3) a mechanical proxy of the
routine's implied rule ("only hold when there's a setup") = per-asset trend filter: hold if prior close > SMA(N).
No lookahead: signal from close of day t-1, trade at open of day t. Costs: 0.40% taker or 0.25% maker,
+0.10% slippage per side, Kraken ordermin (BTC 0.00006, ETH 0.002, SOL 0.05) and costmin $0.50.
Split: first 70% of days = in-sample (sweep), last 30% = held-out (never tuned on)."""
import json, statistics as st
PAIRS = {"XBTUSD": 0.00006, "ETHUSD": 0.002, "SOLUSD": 0.05}
W = {"XBTUSD": .42, "ETHUSD": .33, "SOLUSD": .25}   # live mix on Oct 14 (44.36/34.02/26.50)
FEE, SLIP, START = 0.0040, 0.0010, 105.69
def load(p):
    r = json.load(open(f"data/{p}.json"))["result"]; k = [x for x in r if x != "last"][0]
    return [(int(x[0]), float(x[1]), float(x[4])) for x in r[k]]
D = {p: load(p) for p in PAIRS}; n = min(len(v) for v in D.values())
D = {p: v[-n:] for p, v in D.items()}
cut = int(n * 0.7)
def run(lo, hi, N=None, fee=FEE, slip=SLIP, bh=False):
    cash = START; q = {p: 0.0 for p in PAIRS}; trades = 0; eq = []
    for t in range(lo, hi):
        for p in PAIRS:
            o = D[p][t][1]; closes = [c for _, _, c in D[p][max(0, t-N):t]] if N else []
            want = True if bh else (len(closes) == N and D[p][t-1][2] > st.mean(closes))
            if want and q[p] == 0:
                usd = min(cash, START * W[p]) if t == lo or not bh else 0
                if not bh: usd = min(cash, W[p] * (cash + sum(q[x]*D[x][t][1] for x in PAIRS)))
                px = o * (1+slip); qty = usd / (px*(1+fee))
                if usd >= 0.5 and qty >= PAIRS[p]: q[p] = qty; cash -= usd; trades += 1
            elif not want and q[p] > 0:
                cash += q[p]*o*(1-slip)*(1-fee); q[p] = 0; trades += 1
        eq.append(cash + sum(q[p]*D[p][t][2] for p in PAIRS))
    peak = mdd = 0
    for e in eq: peak = max(peak, e); mdd = max(mdd, 1-e/peak)
    return {"ret_%": round((eq[-1]/START-1)*100, 1), "maxDD_%": round(mdd*100, 1), "trades": trades, "end_$": round(eq[-1], 2)}
day = lambda t: __import__("datetime").date.fromtimestamp(D["XBTUSD"][t][0])
print(f"days={n} in-sample {day(0)}..{day(cut-1)} | held-out {day(cut)}..{day(n-1)}")
for nm, lo, hi in [("IN-SAMPLE", 30, cut), ("HELD-OUT", cut, n)]:
    print(f"\n== {nm} ==\nbuy&hold mix: {run(lo,hi,bh=True)}\ndo nothing:   {{'ret_%': 0.0, 'end_$': {START}}}")
    if nm == "IN-SAMPLE":
        for N in (5, 10, 20, 30, 50, 100): print(f"trend SMA{N:<3}: {run(lo,hi,N)}")
best = max((5,10,20,30,50,100), key=lambda N: run(30, cut, N)["ret_%"])
print(f"\nbest in-sample N={best}; frozen and applied to held-out once:")
for N in (5,10,20,30,50,100): print(f"held-out SMA{N:<3}{'*' if N==best else ' '}: {run(cut,n,N)}")
print(f"held-out SMA{best} maker-fee 0.25%: {run(cut,n,best,fee=.0025)}")
print(f"held-out SMA{best} 2x costs:       {run(cut,n,best,fee=.008,slip=.002)}")
