# Scout 0928 — 2026-10-16 09:28 ET

## Wallet
- SOL: **0.29760554** (`wallet-sol-0928.json`)
- SOL/USD: **~$105.48** → est. **~$31.39**
- SPL: USDC dust 6e-06 only; Token-2022 all zero — **no meme positions**

## Scout counts
- lists: boosts latest/top + profiles + CTOs → `lists.txt`
- pf-live: 50 (`pf-live-0928.json`)
- scan: 142 mints → `cands-0928.json` / `scan-0928.out`
- expand: **638 mints / 561 pairs** → `expand-0928.out`
- strict in-window (0.5–4h, mc≥$10k, h1>0, pumpfun|pumpswap): **6**
- NEW: **2** (SOCKSS, EI)
- young (<0.5h): **4** (Scud, INU, RIBBIT, ELON)

## Autopsies
| Sym | Mint | Role | Verdict | One-line |
|-----|------|------|---------|----------|
| SOCKSS | Egk3…pump | NEW | **FAIL** | creatorBal 0; 11× 1.0–1.1% sniper band; fresh post-grad |
| EI | 8qGJ…pump | NEW | **FAIL** | creatorBal 0; 19× 1–5% band; top10ex≈26.6%; insiderNetworks |
| RIBBIT | 78ZB…pump | YOUNG | **FAIL** | too young + creatorBal 0 |
| Scud | 74St…pump | YOUNG | **FAIL** | too young + creatorBal 0 + tight bands |
| INU | 5xri…pump | YOUNG | **FAIL** | too young + creatorBal 0 + 19× band |
| $1 / OPTIMA / Irene / pump | — | PRIOR | prior FAIL stands | structural; not re-autopsied |

## Decision
**NO_BUY** — stay in SOL. Prefer cash over any borderline; zero autopsy-clean candidates.

## Artifacts
- `wallet-sol-0928.json`, `wallet-spl-0928.json`, `wallet-t22-0928.json`, `sol-price-0928.json`
- `lists.txt`, `boosts-*-0928.json`, `profiles-latest-0928.json`, `ctos-latest-0928.json`, `pf-live-0928.json`
- `scan0928.py`, `scan-0928.out`, `cands-0928.json`
- `expand0928.py`, `expand-0928.out`, `expanded-0928.json`, `inwindow-0928.json`, `new-0928.json`, `watch-extra-0928.json`
- `rc-{SOCKSS,EI,RIBBIT,Scud,INU}-0928.json`, `autopsy-summary-*-0928.json`
- `trade-log.md` appended
