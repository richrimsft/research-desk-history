# Scout 0714 — 2026-10-16 07:14 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (`wallet-sol-0714.json`); SPL: dust USDC only (0.000006); Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0714.json` / `wallet-t22-0714.json`). Unchanged.
- SOL ~$107.02 (CoinGecko, `sol-price-0714.json`) → est. total ~$31.85.

## Feeds
- DexScreener boosts latest/top, profiles latest, community-takeovers → `boosts-*-0714.json` / `profiles-*-0714.json`
- pump.fun currently-live 50 → `pf-live-0714.json`; pump.fun sorted lists → `pf-sorted-0714.json`
- `lists.txt` rebuilt (4 lines; 60 unique solana)
- scan.py: **147 mints** → `scan-0714.out` / `cands-0714.json` (84 cands)
- expanded (`expand0714.py`, `expand-0714.out`) → **469 mints / 446 pairs** (`expanded-0714.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | ElonThrust | ~$1,167,456 | 1.77 | 35.23 | 2.39 | pumpswap | `pFibPnQk8ekC…pump` |
| PRIOR | Irene | ~$149,009 | 1.84 | 59.57 | 14.35 | pumpswap | `6VdcMnBTCj4t…pump` |
| PRIOR | Deer | ~$130,912 | 2.74 | 208 | 37.31 | pumpswap | `4tf5GEXU1dt7…Deer` |
| PRIOR | USDC | ~$120,059 | 0.66 | 118 | -3.37 | pumpswap | `6We2unR6HXgE…pump` |
| PRIOR | Irene | ~$65,628 | 1.28 | 12.98 | — | pumpswap | `5j7gTphd94qD…nEUY` |
| PRIOR | LULU | ~$25,478 | 3.38 | 7.59 | 0.73 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | Irene | ~$22,359 | 0.85 | 132 | -17.49 | pumpswap | `Aoh85TCPn6yY…J5rm` |
| PRIOR | YERN | ~$14,288 | 1.76 | 8.06 | -0.79 | pumpfun | `PdtREY9H6Fp9…yern` |
| PRIOR | PITBULL | ~$11,777 | 3.74 | 4.32 | 11.54 | pumpfun | `Gmh5hNtCycP6…pump` |

**NEW: 0** — no new in-window candidates.

### PRIOR notes
- **Deer** `4tf5…Deer` rechecked (RC improved vs 0703: score 1, liq ~$28.7k, h1 +208 / m5 +37) — **FAIL stands**: creatorBal 0; 19×1–5% band; top10 excl. pool ≈27%; post-grad chase. `autopsy-summary-Deer-0714.json` / `rc-Deer-0714.json`
- ElonThrust / Irene×3 / USDC / LULU / YERN / PITBULL — prior FAILs stand (copycats / impersonation / creatorBal 0 / bands / whales / post-grad; none materially improved).
- Dropped vs 0710: FSR / Chase `YwCK…` / SocialFrnk (out of window or filter).

## Young watch (<30m) — light RC only (do NOT buy)
| symbol | mc | age_h | verdict | note |
|--------|-----|-------|---------|------|
| CCAT (CyberCat) | ~$13.4k | 0.06 | FAIL_PRESCREEN | creatorBal 0; 15× band; non-pump mint; cat copycat wave (`rc-CCAT-0714.json`) |
| TCAT | ~$14.3k | 0.05 | SKIP | TCAT copycat theme |
| GRAB | ~$10.2k | 0.22 | FAIL_PRESCREEN | prior (19× band; creatorBal≈0); m5 −11.6 |
| normie | ~$17.3k | 0.42 | FAIL_PRESCREEN | prior (creatorBal 0; 19×); m5 −26.6 |
| Chase `9TXN…` | ~$6.1M | 0.43 | FAIL_PRESCREEN | prior RC 32839 / 99% holder; post-grad |
| Irene `NqZa…` | ~$89k | 0.46 | SKIP | Irene copycat |

## Decision
**NO-TRADE** — stay in SOL (~0.2976 SOL / ~$31.85).
- In-window: **9** | NEW: **0** | autopsy-clean: **0**
- No buy candidates pass pre-buy autopsy.
