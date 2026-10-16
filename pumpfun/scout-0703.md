# Scout 0703 — 2026-10-16 07:03 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (`wallet-sol-0703.json`); SPL: dust USDC only (0.000006); Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0703.json` / `wallet-t22-0703.json`). Unchanged.
- SOL ~1.76$106.73 (CoinGecko, `sol-price-0703.json`) → est. total ~1.76$31.76.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0703.json` / `profiles-*-0703.json`
- pump.fun currently-live 50 → `pf-live-0703.json`; pump.fun sorted lists → `pf-sorted-0703.json`
- `lists.txt` rebuilt (4 lines; 59 unique solana)
- scan.py: **145 mints** → `scan-0703.out` / `cands-0703.json` (81 cands)
- expanded (`expand0703.py`) → **474 mints / 450 pairs** (`expanded-0703.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | ELON | ~1.76$1,430,584 | 1.02 | 263 | 5.49 | pumpswap | `HGcVEA6uF6Ln…sobn` |
| PRIOR | ElonThrust | ~1.76$1,108,933 | 1.61 | 36.29 | 2.31 | pumpswap | `pFibPnQk8ekC…pump` |
| PRIOR | BOUNCER | ~1.76$257,054 | 1.48 | 17.05 | — | pumpswap | `6X3cMFWWNQSV…3rmg` |
| PRIOR | Irene | ~1.76$120,824 | 1.68 | 48.36 | -4 | pumpswap | `6VdcMnBTCj4t…pump` |
| PRIOR | Deer | ~1.76$104,134 | 2.58 | 207 | 15.74 | pumpswap | `4tf5GEXU1dt7…Deer` |
| PRIOR | Irene | ~1.76$65,628 | 1.11 | 148 | — | pumpswap | `5j7gTphd94qD…nEUY` |
| PRIOR | FSR | ~1.76$37,943 | 2.37 | 21.15 | -2.32 | pumpswap | `HiKU8Lsa8aUF…pump` |
| PRIOR | LULU | ~1.76$25,264 | 3.21 | 6.97 | 0.29 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | Irene | ~1.76$24,325 | 0.69 | 152 | 5.37 | pumpswap | `Aoh85TCPn6yY…J5rm` |
| PRIOR | Chase | ~1.76$16,887 | 1.6 | 30.3 | 3.46 | pumpfun | `YwCKitMEdf7n…pump` |
| PRIOR | HASHED | ~1.76$11,872 | 0.5 | 275 | 6.72 | pumpfun | `BMRjts1YYzGu…rSoL` |
| PRIOR | PITBULL | ~1.76$10,559 | 3.58 | 21.74 | -2.21 | pumpfun | `Gmh5hNtCycP6…pump` |

**NEW: 0** — no full pre-buy autopsy this cycle (no NEW mints in window).

### PRIOR notes (none materially improved)
- **HASHED** `BMRj…rSoL` aged into window (0.50h, ~1.76$11.9k, h1 +275) — **FAIL**: creatorBal **0**; 18×1–5% band (0655 holders); top10ex ~1.7626.5%; non-pump suffix; no socials. Fresh RC 0703 confirms creatorBal 0 (holders endpoint empty this run). `autopsy-summary-HASHED-0703.json` / `rc-HASHED-0703.json`
- **Deer** (~1.76$104k, m5 +15.7) — **FAIL/worse**: RC score **14432** (was ~1.761); LP unlocked 100% + liq ~1.76$68; creatorBal 0; prior band/cabal/social fails stand. `autopsy-summary-Deer-0703.json`
- **ELON** — FAIL stands: ~1.7647k tx/h on ~1.76$50k vol (~1.76$1.04/tx bot micro-churn); creatorBal 0; whale concentration; no socials.
- ELON-theme / BOUNCER / Irene×3 / FSR / LULU / Chase / PITBULL — prior FAILs stand (none materially improved).
- Dropped vs 0655: YERN / Ira (h1≤0 or out of window).

## Young watch (<30m) — light RC only (do NOT buy)
| symbol | mc | age_h | verdict | note |
|--------|-----|-------|---------|------|
| ROADSTER | ~1.76$10.1k | 0.00 | FAIL_PRESCREEN | creatorBal 0; RC 1001 Missing metadata; 19× band (0650); dead tape |
| normie | ~1.76$25.5k | 0.26 | FAIL_PRESCREEN | creatorBal 0; 19× band; thin X status social; h1 +610 but <30m |
| Chase | ~1.76$4.9M | 0.27 | FAIL_PRESCREEN | prior RC 32839 / 99.2% holder; post-grad chase |
| Irene `NqZa…` | ~1.76$83k | 0.29 | SKIP | Irene copycat |
| USDC | ~1.76$125k | 0.49 | SKIP | impersonation name; m5 −18.6 |

## Decision
**NO-TRADE** — stay in SOL (~0.2976 SOL / ~$31.76).
- In-window: **12** | NEW: **0** | autopsy-clean: **0**
- No buy candidates pass pre-buy autopsy.
