# Scout 0551 — 2026-10-16 05:51 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0551.json`); SPL: dust USDC only (0.000006) + USDT 0; Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0551.json` / `wallet-t22-0551.json`). Unchanged since 01:33 ET.
- SOL ~$106.41 (CoinGecko, `sol-price-0551.json`) → est. total ~$31.67.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0551.json` / `profiles-*-0551.json`
- pump.fun currently-live 46 → `pf-live-0551.json`
- `lists.txt` rebuilt (4 lines)
- scan.py: **147 mints** → 89 cands (`scan-0551.out` / `cands-0551.json`)
- expanded (lists + pf-live + priors/watch + narrative searches) → **622 mints / 603 pairs** (`expanded-0551.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | Irene | ~$118k | 0.56 | +180 | -20.79 | pumpswap | `6VdcMnBTCj4tJVwt…pump` |
| PRIOR | ROADSTER | ~$37k | 3.83 | +10.4 | — | pumpswap | `TB6QtGti9j2zadAr…pump` |
| PRIOR | FSR | ~$35k | 1.25 | +72.4 | -14.11 | pumpswap | `HiKU8Lsa8aUFkhtC…pump` |
| PRIOR | Deer | ~$34k | 1.46 | +147 | -11.62 | pumpswap | `4tf5GEXU1dt7Vfj2…Deer` |
| PRIOR | TCAT | ~$25k | 3.50 | +200 | +12.65 | pumpfun | `34HExr1pEVFWkx99…pump` |
| PRIOR | LULU | ~$24k | 2.09 | +1.24 | — | pumpfun | `8DQzWohFEMWruKUC…pump` |
| NEW | TRELLIS | ~$21k | 0.59 | +526 | -34.32 | pumpfun | `4VucxZWxDstE6at1…pump` |
| PRIOR | GITPAID | ~$19k | 0.71 | +415 | +45.38 | pumpfun | `2MdBA1Yiy3oCFmwy…pump` |
| PRIOR | SOL | ~$15k | 0.84 | +266 | — | pumpfun | `2ezhap3jauQous1Z…pump` |
| NEW | Womb | ~$13k | 0.68 | +309 | -28.31 | pumpfun | `BxUHuVGyP9kKRoJZ…pump` |

→ **10** in-window, **2** NEW, **0** autopsy-clean PASS (`inwindow-0551.json` / `new-0551.json` / `_prior-rejects-0551.json`)

## NEW autopsies
### TRELLIS `4VucxZWxDstE6at1ZhpjkDYfBejPcaHoKfupHzV4pump` — **FAIL**
- trellistools — pumpfun curve ~49.2% (~41.842590028 SOL), ~$15,322, 0.58h, h1 +367 / m5 -46.74.
- FAIL: creatorBal 0 (dev sold/out)
- FAIL: 19× wallets in 1–5% band (sniper/distribution pattern)
- FAIL: no socials on DexScreener; empty RC description
- FAIL: botty churn ~2262 tx/h on ~$15,322 mc
- FAIL: m5 -46.74% dumping
- creatorBal **0**; **19×** 1–5% band; top10ex ~18.37%; holders 561.
- `autopsy-raw-TRELLIS-0551.json` / `autopsy-summary-TRELLIS-0551.json` / `_funders-TRELLIS-0551.json` / `rc-TRELLIS-0551.json`

### Womb `BxUHuVGyP9kKRoJZ5h8LvWamCZNCTZcMasUxp9Pjpump` — **FAIL**
- Womb — pumpfun curve ~40.4% (~34.330240866 SOL), ~$13,398, 0.67h, h1 +321 / m5 -11.7.
- FAIL: creatorBal residual ~0.012% (effectively out)
- FAIL: 18× wallets in 1–5% band (sniper/distribution pattern)
- FAIL: graphInsiders 4
- FAIL: no socials on DexScreener; empty RC description
- FAIL: botty churn ~2194 tx/h on ~$13,398 mc
- creatorBal residual ~0.0119%; **18×** 1–5% band; graphInsiders **4**; top10ex ~23.6%; holders 536.
- `autopsy-raw-Womb-0551.json` / `autopsy-summary-Womb-0551.json` / `_funders-Womb-0551.json` / `rc-Womb-0551.json`

## Young watch (<30m) — `watch-extra-0551.json`
- **Crow** `6pub1XbJn779…` (~$17.9k, 0.26h, pumpfun, h1 +398, m5 21.27)
- **BOUNCER** `6X3cMFWWNQSV…` (~$159.6k, 0.36h, pumpswap, h1 +1505, m5 53.76) — post-grad chase <$30m; do not buy blind
- **Irene** `2xZjZSFkuFvT…` (~$21.4k, 0.37h, pumpswap, h1 +127, m5 27.29) — different mint from prior Irene; still <30m
- **BOUNCER** `EiSW6PbKGxdx…` (~$16.2k, 0.46h, pumpfun, h1 +379, m5 27.19)
- **Chase** `YwCKitMEdf7n…` (~$13.2k, 0.48h, pumpfun, h1 +227, m5 -5.56) — prior FAIL theme / watch
- **BOUNCER** `EFxr7QmqvoDB…` (~$12.5k, 0.48h, pumpfun, h1 +272, m5 38.19)
- **ElonThrust** `pFibPnQk8ekC…` (~$729.5k, 0.49h, pumpswap, h1 +1547, m5 14.56) — huge post-grad spike; age gate

## Prior rechecks (light)
- **Irene** `6Vdc…pump` (~$102k PumpSwap, aged into window ~0.51h, m5 −16.6) — RC recheck (`rc-Irene-recheck-0551.json` / `rc-Irene-0551.json`): creatorBal **0**; **12** graphInsiders; band 10; prior FAIL-likely **stands**.
- **GITPAID** (~$19k, m5 +45) — prior FAIL stands (top10ex ~31%, high churn); price action bounce does not clear structure. `rc-GITPAID-0546.json`
- **FSR** (~$35k, m5 −14) / **Deer** (~$34k, m5 −12) / **TCAT** (~$25k) / **LULU** (BUNDLE) / **ROADSTER** / **SOL** — prior FAILs stand.
- **GOAT11 / BDOG** — dropped out of in-window this pass (h1≤0 or mc/age filter); prior FAILs stand if they return.

## Decision
**NO-TRADE** — stay in SOL (~0.2976). Both NEW autopsies FAIL (creatorBal 0/residual + sniper bands / insiders / no socials / botty + dumps). No clean PASS.

## Kraken
Watch-only. Last known USD cash ~$0.81 below min order — no proposal; no orders.
