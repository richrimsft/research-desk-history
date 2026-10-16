# Scout 0832 — 2026-10-16 08:32 ET

## Wallet
- Address: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF`
- SOL: **0.29760554** (~$31.66 @ $106.37)
- SPL: dust USDC only (6e-06); Token-2022: 12 accounts all zero
- Book: **ALL SOL — no meme positions**

## Scout counts
| Stage | Count |
|-------|------:|
| scan.py mints | 149 |
| cands | 83 |
| expanded mints | 549 |
| expanded pairs | 493 |
| strict in-window | 8 |
| NEW | 0 |
| young (<30m) | 4 |
| autopsy-clean buys | 0 |

## In-window (0.5–4h, mc≥$10k, h1>0, pumpfun|pumpswap)
- **PRIOR ElonThrust** mc~$1,603,624 age=3.09h h1=25.6 m5=0.35 pumpswap `pFibPnQk8ekC…`
- **PRIOR Irene** mc~$124,986 age=1.78h h1=14.41 m5=None pumpswap `NqZaNi1v6qjF…`
- **PRIOR Caramel** mc~$116,349 age=0.76h h1=170 m5=-13.26 pumpswap `63UjR7d4xfCD…`
- **PRIOR OPTIMA** mc~$108,405 age=1.16h h1=57.92 m5=-3.14 pumpswap `DdVXE425xZe2…`
- **PRIOR $1** mc~$78,346 age=1.24h h1=225 m5=23.94 pumpswap `5qjzEB3bUBax…`
- **PRIOR Irene** mc~$51,225 age=1.15h h1=285 m5=3.88 pumpswap `6N4BHPN8rvN2…`
- **PRIOR Tesla** mc~$21,768 age=0.6h h1=627 m5=None pumpfun `6KEm7GHTspmv…`
- **PRIOR YERN** mc~$14,732 age=3.08h h1=14.6 m5=-4.33 pumpfun `PdtREY9H6Fp9…`

### Recheck
- **Tesla** `6KEm7GHTspmv…pump` — FAIL (PRIOR recheck; aged into window). RC score **114153**; Creator history of rugged tokens; single holder **51.39%**; only **4** holders; creatorBal **0**; Tesla copycat skip. `autopsy-summary-Tesla-0832.json` / `rc-Tesla-0832.json`
- ElonThrust / Irene×2 (`NqZa…`/`6N4B…` copycats) / Caramel (m5 −13 dumping) / OPTIMA / $1 / YERN — prior FAILs stand (structural; none materially improved). Chase / Deer dropped vs 0826.

## Young pre-screen (<30m, no-buy)
- **VP** mc~$48,190 age=0.15h h1=8.33 m5=-36.4 pumpswap `3rSfVix6BUoP…`
- **CAT** mc~$10,340 age=0.16h h1=142 m5=-15.44 pumpfun `9nQNALg2SqBC…`
- **TripleT** mc~$18,908 age=0.17h h1=424 m5=1.27 pumpfun `8TB7iWUaUrtf…`
- **FI** mc~$52,257 age=0.39h h1=19.89 m5=-6.51 pumpswap `GjuiYGJi3QNt…`

### Young RC
- **CAT** `9nQNALg2SqBC…pump` — FAIL (NEW young): creatorBal **0**; **19×** 1–5% band on 359 holders; top10ex≈25.2%; age 0.16h. `rc-CAT-0832.json` / `autopsy-summary-CAT-0832.json`
- **TripleT** `8TB7iWUaUrtf…pump` — FAIL (NEW young): RC Copycat; creatorBal **0**; **19×** band + tight ~2.1–2.3% cluster; age 0.17h. `rc-TripleT-0832.json` / `autopsy-summary-TripleT-0832.json`
- VP / FI — prior FAILs stand (VP m5 −36 dumping; FI m5 −6.5 fading).

## Decision
**NONE — stay in SOL.** No autopsy-clean buys. 0 NEW in-window; Tesla recheck + CAT/TripleT young all FAIL.
