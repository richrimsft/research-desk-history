# Scout 0613 — 2026-10-16 06:13 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0613.json`); SPL: dust USDC only (0.000006) + 1 zero acct; Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0613.json` / `wallet-t22-0613.json`). Unchanged since 01:33 ET.
- SOL ~$105.77 (CoinGecko, `sol-price-0613.json`) → est. total ~$31.48.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0613.json` / `profiles-*-0613.json`
- pump.fun currently-live 48 → `pf-live-0613.json`; pump.fun sorted lists (mcap/last-trade/created) → `pf-sorted-0613.json`
- `lists.txt` rebuilt (4 lines)
- scan.py: **144 mints** → `scan-0613.out` / `cands-0613.json`
- expanded (lists + pf-live + pf-sorted + priors/watch + narrative searches, `expand0613.py`) → **444 mints / 425 pairs** (`expanded-0613.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | ElonThrust | ~$861k | 0.78 | 1851 | 2.55 | pumpswap | `pFibPnQk8ekCCtuB…pump` |
| NEW | BOUNCER | ~$257k | 0.65 | 2485 | — | pumpswap | `6X3cMFWWNQSV2pdK…3rmg` |
| PRIOR | LOOM | ~$130k | 3.35 | 13.14 | -1.84 | pumpswap | `7GCMYJcykHZ3qJH3…pump` |
| PRIOR | Irene | ~$95k | 0.85 | 137 | 38.61 | pumpswap | `6VdcMnBTCj4tJVwt…pump` |
| PRIOR | Deer | ~$42k | 1.75 | 103 | 7.78 | pumpswap | `4tf5GEXU1dt7Vfj2…Deer` |
| NEW | Irene | ~$30k | 0.66 | 221 | 22.23 | pumpswap | `2xZjZSFkuFvTef55…ThJ3` |
| PRIOR | LULU | ~$24k | 2.39 | 1.43 | 0.53 | pumpfun | `8DQzWohFEMWruKUC…pump` |
| PRIOR | Chase | ~$20k | 0.77 | 395 | 29.35 | pumpfun | `YwCKitMEdf7nagej…pump` |
| PRIOR | TCAT | ~$18k | 3.79 | 36.98 | -19.29 | pumpfun | `34HExr1pEVFWkx99…pump` |
| PRIOR | YERN | ~$15k | 0.77 | 370 | 16.24 | pumpfun | `PdtREY9H6Fp9jVMp…yern` |
| PRIOR | BDOG | ~$13k | 1.83 | 24.25 | -0.06 | pumpfun | `G6NnKQTgN7Dmo9yr…pump` |
| PRIOR | GITPAID | ~$12k | 1.01 | 243 | 19.98 | pumpfun | `2MdBA1Yiy3oCFmwy…pump` |
| PRIOR | TCAT | ~$12k | 1.86 | 158 | -17.62 | pumpfun | `6ZDKgWopksQPMBPQ…pump` |
| PRIOR | EVERYTHING | ~$12k | 2.43 | 7.77 | -0.59 | pumpswap | `DZVADw7Qkfqg2mqQ…pump` |
| PRIOR | SocialFrnk | ~$12k | 1.9 | 2.2 | -11.55 | pumpfun | `62tKjqdvzKrNHb8K…pump` |
| NEW | PITBULL | ~$11k | 2.75 | 53.36 | 13 | pumpfun | `Gmh5hNtCycP6YSyU…pump` |

→ **16** in-window, **3** NEW, **0** autopsy-clean PASS (`inwindow-0613.json` / `new-0613.json` / `_prior-rejects-0613.json`)

## NEW autopsies
### BOUNCER `6X3cMFWWNQSV2pdK5nLyGfNvGUXV6oar45xusbSV3rmg` — **FAIL**
- BOUNCER — graduated PumpSwap (liq $0), ~$257k, 0.7h, h1 +2485 / m5 None.
- FAIL: post-grad blind chase (~$257k after h1 +2485)
- FAIL: top10ex ~89.4% (>30%)
- FAIL: creator holds 9.69% (>5% linked/dev)
- FAIL: single wallet Gw3MQNQE… holds 73.60%
- FAIL: RC risks: Top 10 holders high ownership, Single holder ownership, Low Liquidity, High ownership (score 20791)
- FAIL: no socials / no website
- creator `7atkTMsN…` age 0.68h, 96 tx, now 0.0015 SOL (funded ~95.6 SOL at launch).
- whale `Gw3MQNQE…` holds 73.60% with ~11.69 SOL.
- top10ex ~89.39%; RC score 20791; holders 2063.
- `autopsy-raw-BOUNCER-0613.json` / `autopsy-summary-BOUNCER-0613.json` / `funders-BOUNCER-0613.json` / `rc-BOUNCER-0613.json`

### Irene (2nd mint) `2xZjZSFkuFvTef55EWVrvapihgVwTgrfHFnAfU9aThJ3` — **FAIL**
- Irene The Orangutan — graduated PumpSwap (liq $33319.18), ~$30k, 0.71h, h1 +221 / m5 26.7.
- FAIL: creatorBal 0 (no visible dev bag / fee-share or dumped)
- FAIL: 8× wallets in 1–5% band
- FAIL: botty churn ~4051 tx/h on ~$30k mc (volh1 $128527.13)
- FAIL: no socials / no website
- FAIL: copycat of prior-FAIL Irene theme (different mint)
- top10ex ~13.04%; band_1_5 8; holders 2100; RC score 11400.
- `autopsy-raw-Irene2-0613.json` / `autopsy-summary-Irene2-0613.json` / `funders-Irene2-0613.json` / `rc-Irene2-0613.json`

### PITBULL `Gmh5hNtCycP6YSyU1Cd4Q77oDL9BdgoBoTWcSMvQpump` — **FAIL**
- Pitbull At Barber — pumpfun curve (curve/AMM+locker ~49.1%: Pump Fun:49.13%), ~$11.3k, 2.79h, h1 +53.36 / m5 13.
- FAIL: creatorBal 0 (no visible dev bag / fee-share or dumped)
- FAIL: 19× wallets in 1–5% band (sniper/distribution pattern) on 103 holders
- FAIL: graphInsiders 14
- FAIL: socials = X-community link only (https://x.com/i/communities/2022855185475764628)
- FAIL: shared funder 9iHgaD24… on 2 top holders (bundle signal)
- deployer `8NZkwtXm…` burner-ish (15 tx, 0.000650254 SOL, age 2.01h).
- top10ex ~24.84%; band_1_5 19; graphInsiders 14; holders 103.
- `autopsy-raw-PITBULL-0613.json` / `autopsy-summary-PITBULL-0613.json` / `funders-PITBULL-0613.json` / `rc-PITBULL-0613.json`

## Young watch (<30m) — `watch-extra-0613.json`
- **uıoɔ** `32yWxejbNvdX…` (~$32.8k, 0.06h, h1 +715, m5 715) — garbled ticker; skip
- **CHAIR** `3jWCPoGE8GBB…` (~$30.1k, 0.21h, h1 +608, m5 63.23) — too young (<30m)
- **CSF** `DDw2yrhhZNCp…` (~$10.2k, 0.26h, h1 +126, m5 -38.94) — twin-mint CSF still young/fading
- **Irene** `5j7gTphd94qD…` (~$63.1k, 0.29h, h1 +596, m5 36.7) — copycat of prior-FAIL Irene; do not buy
- **CSF** `6aNXLr6d9m2g…` (~$13.1k, 0.41h, h1 +225, m5 -11.74) — twin-mint CSF still young/fading

## Prior rechecks (light)
- No prior materially improved structurally:
  - ElonThrust ~$861k (still post-grad whale/botty; prior FAIL stands)
  - Irene `6Vdc…` ~$95k (m5 +39 bounce only; creatorBal 0 + insiders FAIL stands)
  - Chase `YwCK…` ~$20k (m5 +29 bounce; fresh 5.6% wallet + band FAIL stands)
  - YERN / TCAT×2 / Deer / LULU / BDOG / GITPAID / SocialFrnk / EVERYTHING / LOOM — prior FAILs stand
- LOOM re-entered in-window (~$130k, 3.35h) — prior FAIL (insiders/structure) unchanged; not re-autopsied.
- CCAT / ROADSTER / SOL / Womb / TRELLIS dropped out of in-window this pass.

## Decision
**NO-TRADE** — stay in SOL (~0.2976). All 3 NEW autopsies FAIL (BOUNCER post-grad 73.6% whale + 9.7% creator; Irene2 copycat + creatorBal 0 + botty; PITBULL creatorBal 0 + 19× band + graphInsiders 14 + shared funder). No clean PASS.

## Kraken
Watch-only. Last known USD cash ~$0.81 below min order — no proposal; no orders.
