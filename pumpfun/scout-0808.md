# Scout 0808 — 2026-10-16 08:08 ET

## Wallet
- Address: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF`
- SOL: **0.29760554** (~$31.61 @ $106.21)
- SPL: dust USDC only (6e-06); Token-2022: 12 accounts all zero
- Book: **ALL SOL — no meme positions**

## Scout counts
| Stage | Count |
|-------|------:|
| scan.py mints | 137 |
| cands | 75 |
| expanded mints | 481 |
| expanded pairs | 460 |
| strict in-window | 9 |
| NEW | 0 |
| young (<30m) | 6 |
| autopsy-clean buys | 0 |

## In-window (0.5–4h, mc≥$10k, h1>0, pumpfun|pumpswap)
- **PRIOR Chase** mc~$9,344,013 age=1.35h h1=76.92 m5=None pumpswap `9TXNTWV5v7M3…`
- **PRIOR ElonThrust** mc~$1,468,753 age=2.69h h1=29.31 m5=1.75 pumpswap `pFibPnQk8ekC…`
- **PRIOR Deer** mc~$176,535 age=3.66h h1=82.88 m5=22.99 pumpswap `4tf5GEXU1dt7…`
- **PRIOR Irene** mc~$124,986 age=1.38h h1=46.96 m5=None pumpswap `NqZaNi1v6qjF…`
- **PRIOR OPTIMA** mc~$110,856 age=0.76h h1=159 m5=24.45 pumpswap `DdVXE425xZe2…`
- **PRIOR Irene** mc~$44,629 age=1.77h h1=64.69 m5=None pumpswap `Aoh85TCPn6yY…`
- **PRIOR Irene** mc~$35,892 age=0.75h h1=281 m5=1.96 pumpswap `6N4BHPN8rvN2…`
- **PRIOR SocialFrnk** mc~$13,601 age=3.82h h1=9.98 m5=-6.22 pumpfun `62tKjqdvzKrN…`
- **PRIOR BDOG** mc~$11,614 age=3.74h h1=4.65 m5=None pumpfun `G6NnKQTgN7Dm…`

### Recheck
- **Deer** `4tf5GEXU1dt7…Deer` — FAIL (rechecked). Hot rebound (h1 +83 / m5 +23, liq ~$36.7k) but creatorBal **0**; **19×** 1–5% band; top10ex≈27.5%; post-grad chase; prior 0714 FAIL stands. `autopsy-summary-Deer-0808.json` / `rc-Deer-0808.json`
- **OPTIMA** `DdVXE425…pump` — FAIL (rechecked). Still hot (h1 +159 / m5 +24, ~$111k) but **13×** band; top10ex≈27.8%; post-grad pumpswap; 0720/0802 structure persists. `autopsy-summary-OPTIMA-0808.json` / `rc-OPTIMA-0808.json`
- Chase / ElonThrust / Irene×3 (`NqZa…`/`Aoh8…`/`6N4B…` copycats) / SocialFrnk / BDOG — prior FAILs stand (none materially improved). YERN dropped vs 0802.

## Young pre-screen (<30m, no-buy)
- **FI** mc~$28,479 age=0.17h h1=441 m5=16.07 pumpfun `GjuiYGJi3QNt…`
- **Tesla** mc~$21,768 age=0.2h h1=627 m5=None pumpfun `6KEm7GHTspmv…`
- **DJT** mc~$19,957 age=0.21h h1=395 m5=120 pumpfun `5aGRLchKmNDv…`
- **DTR** mc~$164,819 age=0.29h h1=265 m5=2.89 pumpswap `4ti7DQpMPKHc…`
- **Caramel** mc~$63,432 age=0.36h h1=42.39 m5=-46.66 pumpswap `63UjR7d4xfCD…`
- **Cub** mc~$10,312 age=0.38h h1=186 m5=-7.52 pumpfun `DG5cR2W2Ms5Q…`

### Young RC
- **DJT** `5aGRL…TTLG` — FAIL (NEW young): RC Copycat of DJTu7…; creatorBal 0; 19× band. `rc-DJT-0808.json` / `autopsy-summary-DJT-0808.json`
- **FI** `Gjui…pump` — FAIL: creatorBal 0; 14× band. `rc-FI-0808.json`
- **Tesla** `6KEm…pump` — FAIL: RC 6153; single holder 51%; 7 holders. `rc-Tesla-0808.json`
- **DTR** `4ti7…pump` — FAIL stands: young post-grad chase ~$165k; prior band/copycat narrative. `rc-DTR-0808.json`
- Caramel / Cub — prior FAILs stand (m5 fading on Caramel −47).

## Decision
**NONE — stay in SOL.** No autopsy-clean buys. 0 NEW in-window; Deer+OPTIMA rechecks still FAIL.

