# Scout 0725 — 2026-10-16 07:25 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (`wallet-sol-0725.json`); SPL: dust USDC only (0.000006); Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0725.json` / `wallet-t22-0725.json`). Unchanged.
- SOL ~$106.77 (CoinGecko, `sol-price-0725.json`) → est. total ~$31.8.

## Feeds
- DexScreener boosts latest/top, profiles latest, community-takeovers → `boosts-*-0725.json` / `profiles-*-0725.json`
- pump.fun currently-live 50 → `pf-live-0725.json`; pump.fun sorted lists → `pf-sorted-0725.json` (via expand)
- `lists.txt` rebuilt (4 lines; 60 unique solana)
- scan.py: **148 mints** → `scan-0725.out` / `cands-0725.json` (85 cands)
- expanded (`expand0725.py`, `expand-0725.out`) → **473 mints / 452 pairs** (`expanded-0725.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | Chase | ~$7,825,037 | 0.62 | 36386 | 9.6 | pumpswap | `9TXNTWV5v7M3…SLEm` |
| PRIOR | ElonThrust | ~$1,225,965 | 1.96 | 33.87 | 1.76 | pumpswap | `pFibPnQk8ekC…pump` |
| PRIOR | Irene | ~$152,059 | 2.03 | 9.39 | 14.15 | pumpswap | `6VdcMnBTCj4t…pump` |
| PRIOR | Deer | ~$115,175 | 2.93 | 78.72 | -3.29 | pumpswap | `4tf5GEXU1dt7…Deer` |
| PRIOR | Irene | ~$96,569 | 0.65 | 88.04 | 4.34 | pumpswap | `NqZaNi1v6qjF…RWGU` |
| PRIOR | USDC | ~$89,590 | 0.84 | 62.63 | 7.81 | pumpswap | `6We2unR6HXgE…pump` |
| PRIOR | Irene | ~$65,628 | 1.47 | 6.83 | — | pumpswap | `5j7gTphd94qD…nEUY` |
| PRIOR | Irene | ~$28,337 | 1.04 | 67.19 | -3.28 | pumpswap | `Aoh85TCPn6yY…J5rm` |
| PRIOR | LULU | ~$25,517 | 3.57 | 0.77 | 0.01 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | normie | ~$13,201 | 0.61 | 267 | -35.71 | pumpfun | `4673spr9Zth4…pump` |
| PRIOR | PITBULL | ~$11,381 | 3.93 | 5.51 | — | pumpfun | `Gmh5hNtCycP6…pump` |
| PRIOR | SocialFrnk | ~$10,788 | 3.09 | 7.27 | -1.13 | pumpfun | `62tKjqdvzKrN…pump` |
| PRIOR | Ira | ~$10,568 | 1.08 | 20.89 | 4.07 | pumpfun | `Aq8Jdz2m4Vda…pump` |
| PRIOR | TCAT | ~$10,208 | 3.04 | 12.28 | 10.96 | pumpfun | `6ZDKgWopksQP…pump` |

**NEW: 0** — no new in-window candidates.

### PRIOR notes
- **Chase** `9TXN…SLEm` — FAIL stands: prior RC 32839 / single holder ~99%; post-grad chase ~$7.8M.
- **Deer** `4tf5…Deer` — no material improvement (m5 −3.29 still fading); prior FAIL stands (creatorBal 0; 19× band; post-grad).
- **normie** — FAIL stands (creatorBal 0; 19× band); m5 −35.71 dumping.
- **Irene×4** (`6Vdc…` returned / `NqZa…` / `5j7g…` returned / `Aoh8…`) — copycat theme; FAIL stands.
- **TCAT** returned to window — copycat / prior FAIL stands.
- ElonThrust / USDC (impersonation) / LULU / PITBULL / SocialFrnk / Ira — prior FAILs stand (none materially improved).
- Dropped vs 0720: (none material; OPTIMA aged out of young into nowhere / filtered).

## Young watch (<30m) — light RC only (do NOT buy)
| symbol | mc | age_h | verdict | note |
|--------|-----|-------|---------|------|
| Jato | ~$16.8k | 0.09 | FAIL_PRESCREEN | creatorBal 0; 15×1–5% band on 421 holders (`rc-Jato-0725.json`) |
| FTR | ~$12.5k | 0.14 | FAIL_PRESCREEN | creatorBal 0; 19×1–5% band on 275 holders (`rc-FTR-0725.json`) mint `BPVUcKX5…pump` |
| FTR | ~$997k | 0.33 | FAIL_PRESCREEN_PRIOR | creatorBal 0; early post-grad chase (`rc-FTR2-0725.json`) mint `9sv13ToY…pump` |
| GRAB | ~$15.1k | 0.41 | FAIL_PRESCREEN_PRIOR | creatorBal≈0; 19× band (`rc-GRAB-0725.json`) |

## Decision
**NO-TRADE** — stay in SOL (~0.2976 SOL / ~$31.8).
- In-window: **14** | NEW: **0** | autopsy-clean: **0**
- No buy candidates pass pre-buy autopsy.
