# Scout 0802 — 2026-10-16 08:02 ET

## Wallet
- Address: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF`
- SOL: **0.29760554** (~$31.71 @ $106.56)
- SPL: dust USDC only (6e-06); Token-2022: 12 accounts all zero
- Book: **ALL SOL — no meme positions**

## Scout counts
| Stage | Count |
|-------|------:|
| scan.py mints | 139 |
| cands | 77 |
| expanded mints | 481 |
| expanded pairs | 462 |
| strict in-window | 9 |
| NEW | 0 |
| young (<30m) | 7 |
| autopsy-clean buys | 0 |

## In-window (0.5–4h, mc≥$10k, h1>0, pumpfun|pumpswap)
- **PRIOR Chase** mc~$9,344,013 age=1.24h h1=97.94 m5=None pumpswap `9TXNTWV5v7M3…`
- **PRIOR ElonThrust** mc~$1,433,300 age=2.58h h1=29.89 m5=1.67 pumpswap `pFibPnQk8ekC…`
- **PRIOR Irene** mc~$124,986 age=1.27h h1=50.33 m5=0.37 pumpswap `NqZaNi1v6qjF…`
- **PRIOR OPTIMA** mc~$60,221 age=0.65h h1=40.82 m5=55.14 pumpswap `DdVXE425xZe2…`
- **PRIOR Irene** mc~$44,629 age=1.66h h1=110 m5=None pumpswap `Aoh85TCPn6yY…`
- **PRIOR Irene** mc~$35,809 age=0.64h h1=280 m5=24.93 pumpswap `6N4BHPN8rvN2…`
- **PRIOR YERN** mc~$16,584 age=2.56h h1=29.46 m5=-0.79 pumpfun `PdtREY9H6Fp9…`
- **PRIOR SocialFrnk** mc~$14,503 age=3.7h h1=52.87 m5=-1.11 pumpfun `62tKjqdvzKrN…`
- **PRIOR BDOG** mc~$11,614 age=3.63h h1=4.65 m5=8.99 pumpfun `G6NnKQTgN7Dm…`

### Recheck
- **OPTIMA** `DdVXE425…pump` — FAIL (rechecked). Price hot (h1 +41 / m5 was +55) + socials appeared, but 12×1–5% band, top wallets ~18%+10%, post-grad pumpswap; prior 0720 FAIL structure persists. `autopsy-summary-OPTIMA-0802.json` / `rc-OPTIMA-0802.json`
- Chase / ElonThrust / Irene×3 / YERN / SocialFrnk / BDOG — prior FAILs stand (structural: 99% holder, whales, copycats, creatorBal 0 / bands). Irene `6N4B…`+`NqZa…`+`Aoh8…` = copycat theme skip.

## Young pre-screen (<30m, no-buy)
- **17/10** mc~$10,328 age=0.04h h1=187 m5=187 pumpfun `AGEG7Top8SGq…`
- **FI** mc~$11,188 age=0.06h h1=113 m5=113 pumpfun `GjuiYGJi3QNt…`
- **Tesla** mc~$21,768 age=0.09h h1=627 m5=627 pumpfun `6KEm7GHTspmv…`
- **DTR** mc~$145,486 age=0.18h h1=222 m5=-17.41 pumpswap `4ti7DQpMPKHc…`
- **Jato** mc~$45,758 age=0.21h h1=0.6 m5=17.21 pumpswap `HtqVqejZuh9B…`
- **Caramel** mc~$199,589 age=0.25h h1=348 m5=41.01 pumpswap `63UjR7d4xfCD…`
- **Cub** mc~$14,706 age=0.27h h1=308 m5=24.48 pumpfun `DG5cR2W2Ms5Q…`

### Young RC
- **17/10** `AGEG7…pump` — FAIL: creatorBal 0; 0.04h; mc faded. `rc-1710-0802.json`
- **FI** `Gjui…pump` — FAIL: creatorBal 0; 13× band. `rc-FI-0802.json`
- **Tesla** `6KEm…pump` — FAIL: RC 6153; single holder 51%; 7 holders. `rc-Tesla-0802.json`
- **DTR** `4ti7…pump` ("Doge Tesla Roadster") — FAIL: 18× band; top10ex≈32%; post-grad ~$145k chase; m5 fading. `rc-DTR-0802.json`
- Jato / Caramel / Cub — prior FAILs stand.

## Decision
**NONE — stay in SOL.** No autopsy-clean buys.
