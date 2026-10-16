#!/usr/bin/env python3
"""funnel.py: raw vs corrected stats for every scanned wallet (reads the scan files, no network)."""
import json, statistics as st
D = "/workspace/polymarket-sim/copy/"
W = [json.loads(l) for l in open(D + "wallets.jsonl")]
C = [json.loads(l) for l in open(D + "corrected.jsonl")]
nl_raw = [w for w in W if w["never_lose"]]
nl_c = [c for c in C if c["c_never_lose"]]
full = [c for c in nl_c if not c["capped_at_1000"]]
flip = [c for c in C if c["never_lose"] and not c["c_never_lose"]]
print(f"wallets scanned ............................ {len(W):,}")
print(f"  with 10+ resolved bets ................... {len(C):,}")
print(f"'never lose' (raw /closed-positions) ....... {len(nl_raw):,}")
print(f"'never lose' after counting dead bets ...... {len(nl_c):,}")
print(f"  ...and full history visible (<1,000 cap) . {len(full)}")
print(f"  ...of those, 95c+ 'penny pickers' ........ {sum(c['near_certain_buyer'] for c in full)}")
print(f"median win rate  raw {100*st.median(c['win_rate'] for c in C):.0f}%  ->  corrected {100*st.median(c['c_win_rate'] for c in C):.0f}%")
print(f"wallets in profit raw {sum(c['pnl']>0 for c in C):,}  ->  corrected {sum(c['c_pnl']>0 for c in C):,}")
print(f"'never lose' wallets that flipped .......... {len(flip):,}  (hidden losses ${-sum(c['dead_open_pnl'] for c in flip)/1e6:,.0f}M)")
print(f"wallets capped at 1,000 closed rows ........ {sum(c['capped_at_1000'] for c in C):,}")
