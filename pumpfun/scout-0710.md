# Scout 0710 — 2026-10-16 07:10 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (`wallet-sol-0710.json`); SPL: dust USDC only (0.000006); Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0710.json` / `wallet-t22-0710.json`). Unchanged.
- SOL ~$106.64 (CoinGecko, `sol-price-0710.json`) → est. total ~$31.74.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0710.json` / `profiles-*-0710.json`
- pump.fun currently-live 50 → `pf-live-0710.json`; pump.fun sorted lists → `pf-sorted-0710.json`
- `lists.txt` rebuilt (4 lines; 60 unique solana)
- scan.py: **146 mints** → `scan-0710.out` / `cands-0710.json` (83 cands)
- expanded (`expand0710.py`) → **466 mints / 442 pairs** (`expanded-0710.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | ElonThrust | ~$1,147,272 | 1.73 | 35.11 | 2.06 | pumpswap | `pFibPnQk8ekC…pump` |
| PRIOR | Irene | ~$129,997 | 1.80 | 70.83 | 4.51 | pumpswap | `6VdcMnBTCj4t…pump` |
| NEW | USDC | ~$105,104 | 0.61 | 90.79 | -7.54 | pumpswap | `6We2unR6HXgE…pump` |
| PRIOR | Deer | ~$95,947 | 2.70 | 134 | 0.09 | pumpswap | `4tf5GEXU1dt7…Deer` |
| PRIOR | Irene | ~$65,628 | 1.23 | 5.23 | — | pumpswap | `5j7gTphd94qD…nEUY` |
| PRIOR | FSR | ~$35,450 | 2.49 | 12.13 | -5.39 | pumpswap | `HiKU8Lsa8aUF…pump` |
| PRIOR | LULU | ~$25,393 | 3.33 | 7.44 | 0.39 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | Irene | ~$21,638 | 0.80 | 124 | -7.51 | pumpswap | `Aoh85TCPn6yY…J5rm` |
| PRIOR | Chase | ~$19,942 | 1.72 | 21.31 | 19.65 | pumpfun | `YwCKitMEdf7n…pump` |
| PRIOR | YERN | ~$13,934 | 1.71 | 8.71 | -3.25 | pumpfun | `PdtREY9H6Fp9…yern` |
| PRIOR | SocialFrnk | ~$12,666 | 2.85 | 28.32 | 10.56 | pumpfun | `62tKjqdvzKrN…pump` |
| PRIOR | PITBULL | ~$10,559 | 3.69 | 10.8 | — | pumpfun | `Gmh5hNtCycP6…pump` |

**NEW: 1** — full pre-buy autopsy below.

### NEW autopsy
- **USDC** `6We2unR6HXgE…pump` (name "UpSide Down Cat", ~$105k PumpSwap, 0.61h, h1 +91 / m5 −7.5) — **FAIL**: USDC impersonation / RC Copycat of Circle mint; creatorBal **0**; **18×**1–5% band; social is coinbase status (stolen); post-grad chase. `autopsy-summary-USDC-0710.json` / `rc-USDC-0710.json`

### PRIOR notes (none materially improved)
- **Chase** `YwCK…pump` m5 +19.7 but structural FAIL stands (creatorBal 0 / band / botty tape from 0603) — not borderline; no re-autopsy.
- ElonThrust / Irene×3 / Deer / FSR / LULU / YERN / SocialFrnk / PITBULL — prior FAILs stand (copycats / creatorBal 0 / bands / whales / post-grad).
- Dropped vs 0703: ELON / BOUNCER / HASHED (h1≤0 or out of window / mc filter).

## Young watch (<30m) — light RC only (do NOT buy)
| symbol | mc | age_h | verdict | note |
|--------|-----|-------|---------|------|
| ONE | ~$12.7k | 0.12 | FAIL_PRESCREEN | creatorBal 0; 11× band; graphInsiders 4 |
| GRAB | ~$11.9k | 0.18 | FAIL_PRESCREEN | creatorBal≈0; **19×** band; low liq |
| TCAT | ~$12.5k | 0.03 | SKIP | TCAT copycat theme |
| normie | ~$17.2k | 0.38 | FAIL_PRESCREEN | prior (creatorBal 0; 19×); m5 −24 |
| Chase `9TXN…` | ~$5.7M | 0.39 | FAIL_PRESCREEN | prior RC 32839 / 99% holder; post-grad |
| Irene `NqZa…` | ~$86k | 0.41 | SKIP | Irene copycat |

## Decision
**NO-TRADE** — stay in SOL (~0.2976 SOL / ~$31.74).
- In-window: **12** | NEW: **1** | autopsy-clean: **0**
- No buy candidates pass pre-buy autopsy.
