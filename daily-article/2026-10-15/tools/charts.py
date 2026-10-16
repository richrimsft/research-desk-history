import json, datetime as dt, statistics as S, collections
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for f in fm.findSystemFonts():
    if "Inter" in f: fm.fontManager.addfont(f)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,"axes.facecolor":"#0d1117","figure.facecolor":"#0d1117",
  "text.color":"#e6edf3","axes.labelcolor":"#c9d1d9","xtick.color":"#9aa4ae","ytick.color":"#9aa4ae","axes.edgecolor":"#30363d",
  "axes.grid":True,"grid.color":"#21262d","grid.linewidth":0.8})
R,G,B,Y,GR="#ff6b6b","#3fb950","#58a6ff","#e3b341","#8b949e"
D="/workspace/polymarket-sim/copy/"; O="/workspace/daily-article/2026-10-15/img/"
W=[json.loads(l) for l in open(D+"wallets.jsonl")]; C=[json.loads(l) for l in open(D+"corrected.jsonl")]
def foot(fig,t): fig.text(0.01,0.012,t,fontsize=10.5,color=GR)
def title(fig,t,s=None):
    fig.text(0.012,0.95,t,fontsize=23,fontweight="bold",va="top")
    if s: fig.text(0.012,0.885,s,fontsize=14,color=GR,va="top")
SRC="Source: my scan of Polymarket's public Data API, 5,916 leaderboard wallets, Oct 15, 2026, 2:55-4:10 AM ET (wallets.jsonl / corrected.jsonl)"
# C1 funnel
nl=[c for c in C if c["c_never_lose"]]; full=[c for c in nl if not c["capped_at_1000"]]
steps=[("Wallets scanned",len(W),GR),("10+ resolved bets",len(C),GR),("'Never lose' (raw data)",sum(w["never_lose"] for w in W),R),
 ("Still zero losses after\ncounting dead bets",len(nl),Y),("...with full history visible",len(full),B),("...and not a 95c+ penny picker",sum(not c["near_certain_buyer"] for c in full),G)]
fig,ax=plt.subplots(figsize=(14,7.4)); fig.subplots_adjust(left=0.28,right=0.97,top=0.80,bottom=0.13)
y=list(range(len(steps)))[::-1]
ax.barh(y,[s[1] for s in steps],color=[s[2] for s in steps],height=0.62)
for yi,(l,v,c) in zip(y,steps): ax.text(v+60,yi,f"{v:,}",va="center",fontsize=19,fontweight="bold",color=c)
ax.set_yticks(y); ax.set_yticklabels([s[0] for s in steps],fontsize=15); ax.set_xlim(0,6900); ax.grid(axis="y",visible=False)
ax.set_xlabel("wallets")
title(fig,"1,808 wallets 'never lose'. 7 of them hold up.","Same wallets, same API. The only change: counting bets that expired worthless.")
foot(fig,SRC); fig.savefig(O+"c01-funnel.png",dpi=100); plt.close()
# C2 histogram
fig,ax=plt.subplots(figsize=(14,7.2)); fig.subplots_adjust(left=0.07,right=0.97,top=0.80,bottom=0.13)
bins=[i/40 for i in range(41)]
ax.hist([c["win_rate"] for c in C],bins=bins,color=R,alpha=0.75,label=f"Raw /closed-positions (median {100*S.median(c['win_rate'] for c in C):.0f}%)")
ax.hist([c["c_win_rate"] for c in C],bins=bins,color=B,alpha=0.75,label=f"Corrected, dead bets counted (median {100*S.median(c['c_win_rate'] for c in C):.0f}%)")
ax.set_xlabel("win rate"); ax.set_ylabel("wallets"); ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0))
ax.legend(loc="upper center",frameon=False,fontsize=15)
title(fig,"The 'everyone wins' illusion","Win rate of 5,350 wallets with 10+ resolved bets. The big red spike at 100% is the data trap.")
foot(fig,SRC); fig.savefig(O+"c02-winrate.png",dpi=100); plt.close()
# C3 flipped wallets
fl=sorted([c for c in C if c["never_lose"] and not c["c_never_lose"]],key=lambda c:c["dead_open_pnl"])[:10]
fig,ax=plt.subplots(figsize=(14,7.6)); fig.subplots_adjust(left=0.2,right=0.97,top=0.80,bottom=0.12)
lab=[f"{c['wallet'][:6]}…{c['wallet'][-4:]}\n{c['wins']}-0 → {c['c_wins']}-{c['c_losses']}" for c in fl]
yy=list(range(len(fl)))[::-1]
ax.barh([v+0.2 for v in yy],[c["pnl"]/1e6 for c in fl],height=0.4,color=R,label="P&L the raw data shows")
ax.barh([v-0.2 for v in yy],[c["c_pnl"]/1e6 for c in fl],height=0.4,color=B,label="P&L with dead bets counted")
ax.set_yticks(yy); ax.set_yticklabels(lab,fontsize=11.5); ax.axvline(0,color="#e6edf3",lw=1)
ax.set_xlabel("$ millions"); ax.legend(frameon=False,loc="lower right",fontsize=14)
tot=-sum(c["dead_open_pnl"] for c in C if c["never_lose"] and not c["c_never_lose"])
title(fig,f"${tot/1e6:,.0f}M of losses the 'never lose' lists don't show",f"10 of the 1,493 flipped wallets with the biggest hidden losses. Labels: raw record → real record.")
foot(fig,SRC); fig.savefig(O+"c03-hidden.png",dpi=100); plt.close()
# C4 survivors + payoff math
fig,(a1,a2)=plt.subplots(1,2,figsize=(14,7.2)); fig.subplots_adjust(left=0.07,right=0.98,top=0.78,bottom=0.13,wspace=0.28)
for c in full:
    col=Y if c["near_certain_buyer"] else G
    a1.scatter(c["avg_win_entry"]*100,c["c_resolved"],s=max(60,c["c_pnl"]/40),color=col,alpha=0.85,edgecolor="white")
    a1.annotate(f"\\${c['c_pnl']:,.0f}",(c["avg_win_entry"]*100,c["c_resolved"]),xytext=(8,6) if c["avg_win_entry"]>0.05 else ((10,-16) if c["c_resolved"]<14 else (-10,12)),textcoords="offset points",fontsize=12)
a1.set_xlabel("average entry price of winning bets (cents)"); a1.set_ylabel("resolved bets"); a1.set_xlim(-5,110); a1.set_yscale("log"); a1.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter()); a1.set_yticks([10,20,50,100,200,300]); a1.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
a1.set_title("The 7 real zero-loss wallets (dot size = profit)",fontsize=14,color="#e6edf3")
a1.scatter([],[],color=Y,label="95c+ penny pickers (4)"); a1.scatter([],[],color=G,label="others (3)"); a1.legend(frameon=False,fontsize=12,loc="upper center")
ps=[50,60,70,80,87,90,92,95,97,99]; need=[p/(100-p) for p in ps]
a2.bar([str(p) for p in ps],need,color=[Y if p>=87 else B for p in ps]); a2.set_yscale("log"); a2.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter()); a2.set_yticks([1,2,5,10,20,50,100]); a2.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
for i,n in enumerate(need): a2.text(i,n*1.12,f"{n:.0f}" if n>=2 else f"{n:.1f}",ha="center",fontsize=12)
a2.set_xlabel("entry price (cents)"); a2.set_ylabel("wins needed to pay for ONE loss")
a2.set_title("The math of buying near-certainties",fontsize=14,color="#e6edf3")
title(fig,"The few real 'never lose' wallets are tiny or pick up pennies","Left: data from my scan. Right: plain arithmetic, a win earns (100 - price) cents, a loss costs price cents.")
foot(fig,SRC); fig.savefig(O+"c04-survivors.png",dpi=100); plt.close()
# C5 arb
M=[json.loads(l) for l in open("/workspace/daily-article/2026-10-15/data/snapshot/market_stats.jsonl")]
t=[dt.datetime.fromisoformat(m["ts"]) for m in M]
fig,ax=plt.subplots(figsize=(14,7.2)); fig.subplots_adjust(left=0.08,right=0.97,top=0.80,bottom=0.14)
ax.scatter(t,[m["min_raw_sum"] for m in M],s=22,color=GR,label="cheapest Up + Down seen (before fees)")
ax.scatter(t,[m["min_sum_after_fees"] for m in M],s=22,color=R,label="cheapest Up + Down seen, after taker fees")
ax.axhline(1.0,color=G,lw=2); ax.text(t[0],0.9985,"$1.00 payout: anything below this line is free money",color=G,fontsize=13,va="top")
ax.set_ylabel("cost of one Up + one Down share ($)"); ax.legend(frameon=False,loc="upper right",fontsize=13)
import matplotlib.dates as md; ax.xaxis.set_major_formatter(md.DateFormatter("%-I %p",tz=t[0].tzinfo))
lo=min(m["min_sum_after_fees"] for m in M)
title(fig,f"{len(M)} markets, 0 free dollars after fees",f"Polymarket 5-minute BTC/ETH Up/Down, best moment of every market, {t[0]:%b %-d %-I:%M %p} to {t[-1]:%b %-d %-I:%M %p} ET. Lowest after fees: ${lo:.4f}.")
foot(fig,"Source: my paper simulator polling the public CLOB order book every 1 s (market_stats.jsonl). Fee = 0.07 x p x (1-p) per share, from each market's feeSchedule.")
fig.savefig(O+"c05-arb.png",dpi=100); plt.close()
# C6 copy
cp=[json.loads(l) for l in open("/workspace/daily-article/2026-10-15/data/snapshot/copy/copies.jsonl")]; b=[x for x in cp if x["action"]=="buy"]
fig,(a1,a2)=plt.subplots(1,2,figsize=(14,7.2)); fig.subplots_adjust(left=0.07,right=0.98,top=0.78,bottom=0.13,wspace=0.25)
for c,col in (("top",B),("random",GR)):
    bb=[x for x in b if x["cohort"]==c]
    a1.scatter([x["their_price"]*100 for x in bb],[x["our_avg_incl_fee"]*100 for x in bb],color=col,s=60,alpha=0.85,label=f"{c} cohort ({len(bb)} copies)")
a1.plot([0,100],[0,100],color="#e6edf3",lw=1,ls="--"); a1.text(62,55,"same price\nas the wallet",fontsize=11,color="#e6edf3")
a1.set_xlabel("price the wallet paid (cents)"); a1.set_ylabel("price my copy paid incl. fee (cents)")
a1.set_title("Above the line = I paid more. Bottom-left = bought a dying ticket",fontsize=12.5,color="#e6edf3"); a1.legend(frameon=False,fontsize=12,loc="upper left")
cl=[json.loads(l) for l in open("/workspace/daily-article/2026-10-15/data/snapshot/copy/closes.jsonl")]
for c,col in (("top",B),("random",GR)):
    xs=sorted([x for x in cl if x["cohort"]==c],key=lambda x:x["ts"]); cum=0; tt=[];vv=[]
    for x in xs: cum+=x["pnl"]; tt.append(dt.datetime.fromisoformat(x["ts"])); vv.append(cum)
    a2.step(tt,vv,where="post",color=col,lw=3,label=f"{c}: {len(xs)} closed, \\${cum:,.2f}")
a2.axhline(0,color="#e6edf3",lw=1); a2.set_ylabel("realized P&L (\\$, \\$100 paper bankroll each)"); a2.legend(frameon=False,fontsize=12,loc="lower left")
a2.xaxis.set_major_formatter(md.DateFormatter("%-I %p",tz=tt[0].tzinfo)); a2.set_title("Realized P&L so far (tiny sample, not a verdict)",fontsize=12.5,color="#e6edf3")
title(fig,"Copying 'top wallets' in real time: you pay more, and late","Paper copy-trader, public data only, Oct 15 from 4:11 AM ET. Median delay from their trade to my copy: 2.3 minutes.")
foot(fig,"Source: my paper copy-trader (copies.jsonl, closes.jsonl), snapshot Oct 15, 2026, 10:44 AM ET. $5 per copy, real order-book asks plus taker fee. No real money.")
fig.savefig(O+"c06-copy.png",dpi=100); plt.close()
# C7 template spread
X=json.load(open("/workspace/daily-article/2026-10-15/data/x-template-2k12k.json")); P=X["posts"]; U=X["users"]
fig,ax=plt.subplots(figsize=(14,7.2)); fig.subplots_adjust(left=0.08,right=0.97,top=0.80,bottom=0.12)
acc=sorted({U[p["author_id"]]["username"] for p in P}); cmap=plt.get_cmap("tab20")
for p in P:
    u=U[p["author_id"]]["username"]; ax.scatter(dt.datetime.fromisoformat(p["created_at"].replace("Z","+00:00")),p["public_metrics"]["impression_count"],s=120,color=cmap(acc.index(u)%20),edgecolor="white")
ax.set_yscale("log"); ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v,_: f"{v:,.0f}")); ax.set_ylabel("views (log scale)"); ax.xaxis.set_major_formatter(md.DateFormatter("%b %-d"))
v=sum(p["public_metrics"]["impression_count"] for p in P)
title(fig,"'Turned \\$2K into \\$12K in one night.' 28 times.",f"The same post, word for word, from {len(acc)} accounts, Jul 29 to Oct 13, 2026: {v:,} views combined.\nEach dot is one post; each color is one account.")
foot(fig,"Source: X API full-archive search for the exact phrase, retweets excluded, pulled Oct 15, 2026, 10:37 AM ET. View counts as of that time.")
fig.savefig(O+"c07-template.png",dpi=100); plt.close()
print("charts ok")
