# Scout 0730 — 2026-10-16 07:30 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (`wallet-sol-0730.json`); SPL: dust USDC only (0.000006); Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0730.json` / `wallet-t22-0730.json`). Unchanged.
- SOL ~$106.82 (CoinGecko, `sol-price-0730.json`) → est. total ~$31.8.

## Feeds
- DexScreener boosts latest/top, profiles latest, community-takeovers → `boosts-*-0730.json` / `profiles-*-0730.json`
- pump.fun currently-live 50 → `pf-live-0730.json`; pump.fun sorted lists → `pf-sorted-0730.json` (empty this run — API returned `[]`; expand still used live + Dex search)
- `lists.txt` rebuilt (4 lines; 60 unique solana)
- scan.py: **143 mints** → `scan-0730.out` / `cands-0730.json` (80 cands)
- expanded (`expand0730.py`, `expand-0730.out`) → **480 mints 457 pairs** (`expanded-0730.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | Chase | ~$9,056,665 | 0.74 | 42129 | 5.14 | pumpswap | `9TXNTWV5v7M3…SLEm` |
| PRIOR | ElonThrust | ~$1,266,144 | 2.08 | 32.9 | 1.77 | pumpswap | `pFibPnQk8ekC…pump` |
| PRIOR | Deer | ~$117,925 | 3.05 | 90.09 | -4.73 | pumpswap | `4tf5GEXU1dt7…Deer` |
| PRIOR | USDC | ~$113,599 | 0.96 | 106 | 1.41 | pumpswap | `6We2unR6HXgE…pump` |
| PRIOR | Irene | ~$104,903 | 0.77 | 104 | 4.34 | pumpswap | `NqZaNi1v6qjF…RWGU` |
| PRIOR | Irene | ~$65,628 | 1.59 | 59.69 | — | pumpswap | `5j7gTphd94qD…nEUY` |
| PRIOR | Irene | ~$42,239 | 1.16 | 112 | -4.54 | pumpswap | `Aoh85TCPn6yY…J5rm` |
| PRIOR | LULU | ~$25,549 | 3.69 | 2.19 | 0.13 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | GRAB | ~$18,253 | 0.53 | 479 | 13.5 | pumpfun | `5rB2Z8xPrUGX…pump` |
| PRIOR | normie | ~$14,358 | 0.73 | 299 | 6.78 | pumpfun | `4673spr9Zth4…pump` |
| PRIOR | BDOG | ~$11,175 | 3.13 | 10.44 | -1.13 | pumpfun | `G6NnKQTgN7Dm…pump` |
| PRIOR | TCAT | ~$10,117 | 3.16 | 11.73 | -0.76 | pumpfun | `6ZDKgWopksQP…pump` |

**NEW: 0** — no new in-window candidates.

### PRIOR notes
- **Chase** `9TXN…SLEm` — FAIL stands: prior RC 32839 / single holder ~99%; post-grad chase ~$9.1M.
- **Deer** `4tf5…Deer` — no material improvement (m5 −4.73 still fading); prior FAIL stands (creatorBal 0; 19× band; post-grad).
- **GRAB** aged into window — FAIL stands / reconfirmed: creatorBal **0**; RC score 2735 (Low Liquidity); prior 19× band (`rc-GRAB-0730.json` / `autopsy-summary-GRAB-0730.json`).
- **BDOG** returned — FAIL reconfirmed: creatorBal **0**; 19×1–5% band on 222 holders (`rc-BDOG-0730.json` / `autopsy-summary-BDOG-0730.json`); prior FAIL @0456.
- **Irene×3** (`NqZa…` / `5j7g…` / `Aoh8…`) — copycat theme; FAIL stands. (Irene `6Vdc…` dropped vs 0725.)
- **USDC** (impersonation) / **LULU** / **normie** / **TCAT** — prior FAILs stand (none materially improved).
- Dropped vs 0725: Irene `6Vdc…`, PITBULL, SocialFrnk, Ira (aged/filtered out).

## Young watch (<30m) — light RC only (do NOT buy)
| symbol | mc | age_h | verdict | note |
|--------|-----|-------|---------|------|
| Caramel | ~$13.8k | 0.07 | FAIL_PRESCREEN | creatorBal 0; 19×1–5% band on 283 holders (`rc-Caramel-0730.json`) |
| Irene | ~$12.7k | 0.14 | SKIP | copycat theme (`6N4B…XDbo`) |
| OPTIMA | ~$70.9k | 0.15 | FAIL_PRESCREEN_PRIOR | prior FAIL (creatorBal≈0; 13× band); now post-grad chase (`DdVX…pump`) |
| PAIRS | ~$13.5k | 0.16 | FAIL_PRESCREEN | creatorBal 0; 19×1–5% band on 293 holders (`rc-PAIRS-0730.json`) |
| Jato | ~$13.0k | 0.21 | FAIL_PRESCREEN_PRIOR | creatorBal 0; 15× band (`rc-Jato-0725.json`) |
| FTR | ~$11.2k | 0.26 | FAIL_PRESCREEN_PRIOR | creatorBal 0; 19× band (`rc-FTR-0725.json`) mint `BPVU…pump` |
| FTR | ~$1.01M | 0.45 | FAIL_PRESCREEN_PRIOR | creatorBal 0; early post-grad chase (`rc-FTR2-0725.json`) mint `9sv1…pump` |

## Decision
**NO-TRADE** — stay in SOL (~0.2976 SOL / ~$31.8).
- In-window: **12** | NEW: **0** | autopsy-clean: **0**
- No buy candidates pass pre-buy autopsy.
