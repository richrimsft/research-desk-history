# Scout 0720 — 2026-10-16 07:20 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (`wallet-sol-0720.json`); SPL: dust USDC only (0.000006); Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0720.json` / `wallet-t22-0720.json`). Unchanged.
- SOL ~$106.86 (CoinGecko, `sol-price-0720.json`) → est. total ~$31.8.

## Feeds
- DexScreener boosts latest/top, profiles latest, community-takeovers → `boosts-*-0720.json` / `profiles-*-0720.json`
- pump.fun currently-live 50 → `pf-live-0720.json`; pump.fun sorted lists → `pf-sorted-0720.json` (via expand)
- `lists.txt` rebuilt (4 lines; 62 unique solana)
- scan.py: **147 mints** → `scan-0720.out` / `cands-0720.json` (86 cands)
- expanded (`expand0720.py`, `expand-0720.out`) → **477 mints / 456 pairs** (`expanded-0720.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | Chase | ~$7,003,960 | 0.55 | 32557 | 16.61 | pumpswap | `9TXNTWV5v7M3…SLEm` |
| PRIOR | ElonThrust | ~$1,203,980 | 1.89 | 35.03 | 2.26 | pumpswap | `pFibPnQk8ekC…pump` |
| PRIOR | Deer | ~$120,209 | 2.86 | 121 | -6.21 | pumpswap | `4tf5GEXU1dt7…Deer` |
| PRIOR | Irene | ~$90,083 | 0.57 | 75.41 | -1.69 | pumpswap | `NqZaNi1v6qjF…RWGU` |
| PRIOR | USDC | ~$86,696 | 0.77 | 57.38 | -26.55 | pumpswap | `6We2unR6HXgE…pump` |
| PRIOR | Irene | ~$25,924 | 0.96 | 169 | 5.92 | pumpswap | `Aoh85TCPn6yY…J5rm` |
| PRIOR | LULU | ~$25,515 | 3.49 | 0.93 | 0.15 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | normie | ~$20,499 | 0.54 | 470 | 4.35 | pumpfun | `4673spr9Zth4…pump` |
| PRIOR | PITBULL | ~$11,381 | 3.85 | 5.51 | -3.04 | pumpfun | `Gmh5hNtCycP6…pump` |
| PRIOR | SocialFrnk | ~$10,911 | 3.01 | 10.54 | 8.9 | pumpfun | `62tKjqdvzKrN…pump` |
| PRIOR | Ira | ~$10,155 | 1.00 | 153 | 4.77 | pumpfun | `Aq8Jdz2m4Vda…pump` |

**NEW: 0** — no new in-window candidates.

### PRIOR notes
- **Chase** `9TXN…SLEm` aged into window from young — **FAIL stands**: prior RC 32839 / single holder ~99%; post-grad chase at ~$7M.
- **Deer** `4tf5…Deer` — no material improvement (m5 −6.21 fading); prior FAIL stands (creatorBal 0; 19× band; post-grad).
- **normie** aged into window — FAIL stands (creatorBal 0; 19× band).
- ElonThrust / Irene×2 (copycats) / USDC (impersonation) / LULU / PITBULL / SocialFrnk / Ira — prior FAILs stand (none materially improved).
- Dropped vs 0714: Irene `6Vdc…` / Irene `5j7g…` / YERN (out of window or filter).

## Young watch (<30m) — light RC only (do NOT buy)
| symbol | mc | age_h | verdict | note |
|--------|-----|-------|---------|------|
| OPTIMA | ~$24.6k | 0.09 | FAIL_PRESCREEN | creatorBal 0; 13×1–5% band on 366 holders (`rc-OPTIMA-0720.json`) |
| FTR | ~$822k | 0.25 | FAIL_PRESCREEN | creatorBal 0; early post-grad chase ~$822k MC (`rc-FTR-0720.json`) |
| ONE | ~$10.6k | 0.28 | FAIL_PRESCREEN | prior (creatorBal 0; band; graphInsiders) |
| GRAB | ~$12.9k | 0.34 | FAIL_PRESCREEN | prior (19× band; creatorBal≈0) |

## Decision
**NO-TRADE** — stay in SOL (~0.2976 SOL / ~$31.8).
- In-window: **11** | NEW: **0** | autopsy-clean: **0**
- No buy candidates pass pre-buy autopsy.
