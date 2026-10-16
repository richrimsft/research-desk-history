# Scout 0622 — 2026-10-16 06:22 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0622.json`); SPL: dust USDC only (0.000006) + 1 zero acct; Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0622.json` / `wallet-t22-0622.json`). Unchanged since 01:33 ET.
- SOL ~$105.97 (CoinGecko, `sol-price-0622.json`) → est. total ~$31.54.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0622.json` / `profiles-*-0622.json`
- pump.fun currently-live 50 → `pf-live-0622.json`; pump.fun sorted lists (mcap/last-trade/created) → `pf-sorted-0622.json`
- `lists.txt` rebuilt (4 lines)
- scan.py: **144 mints** → `scan-0622.out` / `cands-0622.json` (80 cands)
- expanded (lists + pf-live + pf-sorted + priors/watch + narrative searches, `expand0622.py`) → **442 mints / 422 pairs** (`expanded-0622.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | ElonThrust | ~$897k | 0.91 | 1934 | 2.38 | pumpswap | `pFibPnQk8ekCCtuB…pump` |
| PRIOR | BOUNCER | ~$257k | 0.78 | 2485 | — | pumpswap | `6X3cMFWWNQSV2pdK…3rmg` |
| PRIOR | LOOM | ~$170k | 3.48 | 98.83 | 8.15 | pumpswap | `7GCMYJcykHZ3qJH3…pump` |
| PRIOR | Irene | ~$159k | 0.98 | 296 | 58.76 | pumpswap | `6VdcMnBTCj4tJVwt…pump` |
| PRIOR | Deer | ~$58k | 1.89 | 88.14 | 47.96 | pumpswap | `4tf5GEXU1dt7Vfj2…Deer` |
| PRIOR | FSR | ~$35k | 1.67 | 20.23 | 9.71 | pumpswap | `HiKU8Lsa8aUFkhtC…pump` |
| PRIOR | Irene | ~$32k | 0.8 | 241 | 1.64 | pumpswap | `2xZjZSFkuFvTef55…ThJ3` |
| PRIOR | LULU | ~$25k | 2.52 | 8.51 | 6.93 | pumpfun | `8DQzWohFEMWruKUC…pump` |
| PRIOR | TCAT | ~$22k | 3.93 | 64.34 | 21.27 | pumpfun | `34HExr1pEVFWkx99…pump` |
| PRIOR | Chase | ~$21k | 0.91 | 413 | -14.44 | pumpfun | `YwCKitMEdf7nagej…pump` |
| PRIOR | YERN | ~$16k | 0.9 | 403 | 27.9 | pumpfun | `PdtREY9H6Fp9jVMp…yern` |
| PRIOR | BDOG | ~$13k | 1.96 | 2.65 | -1.29 | pumpfun | `G6NnKQTgN7Dmo9yr…pump` |
| PRIOR | PITBULL | ~$11k | 2.88 | 47.79 | 1.07 | pumpfun | `Gmh5hNtCycP6YSyU…pump` |
| PRIOR | Womb | ~$10k | 1.1 | 1.53 | 11.57 | pumpfun | `BxUHuVGyP9kKRoJZ…pump` |
| NEW | CSF | ~$10k | 0.54 | 152 | -31.28 | pumpfun | `6aNXLr6d9m2gAZKm…pump` |

→ **15** in-window, **1** NEW, **0** autopsy-clean PASS (`inwindow-0622.json` / `new-0622.json` / `_prior-rejects-0622.json`)

## NEW autopsies
### CSF `6aNXLr6d9m2gAZKmGn448f2PhuMeFqWhdDsnPs3Zpump` — **FAIL**
- Charles, Solomon & Francesca — pumpfun curve (curve/AMM+locker ~51.1%: Pump Fun:51.15%), ~$10.2k, 0.54h, h1 +152 / m5 −31.28.
- FAIL: creatorBal 0 (no visible dev bag / fee-share or dumped)
- FAIL: 12× wallets in 1–5% band (sniper/distribution pattern) on 898 holders
- FAIL: botty churn ~4242 tx/h on ~$10k mc (volh1 $148164.91)
- FAIL: no socials / no website
- FAIL: twin-mint CSF copycat (other mint `DDw2yrhh…pump` fading ~$6k)
- FAIL: m5 −31.28 hard fade just after aging into window
- FAIL: deployer burner-ish (wallet age ~0.41h, ≥1000 tx, 0.0059 SOL)
- creator `5EHkmYwU…` age 0.41h, ≥1000 tx, now 0.0059 SOL; pf `/coins/<mint>` 404.
- top10ex ~21.63%; band_1_5 12; graphInsiders 0; holders 898; RC score 1.
- funders: no shared 8+ same-funder bundle among sampled top holders (individual funders Biw4eeai… / 3Mbj13VT… / 5F1seMKU… when found).
- `autopsy-raw-CSF-0622.json` / `autopsy-summary-CSF-0622.json` / `funders-CSF-0622.json` / `rc-CSF-0622.json` / `dex-CSF-0622.json`

## Young watch (<30m) — `watch-extra-0622.json`
- **CHIPTO** `2paFXNaod76U…` (~$11.3k, 0.05h, h1 +71.77, m5 71.77) — too young (<30m)
- **USDC** `JCaa73V2VdbF…` (~$21.7k, 0.09h, h1 +472, m5 472) — spoof ticker; skip
- **ECONOMY** `HesfyHKTEu2V…` (~$11.7k, 0.22h, h1 +286, m5 45.35) — too young (<30m)
- **Irene** `5j7gTphd94qD…` (~$78.7k, 0.42h, h1 +769, m5 36.11) — copycat of prior-FAIL Irene; do not buy

## Prior rechecks (light)
- No prior materially improved structurally:
  - ElonThrust ~$897k (still post-grad whale/botty; prior FAIL stands)
  - BOUNCER ~$257k (73.6% whale + 9.7% creator; prior FAIL stands)
  - Irene `6Vdc…` ~$159k (m5 +59 bounce only; creatorBal 0 + insiders FAIL stands)
  - Irene2 `2xZj…` ~$32k (copycat + creatorBal 0 + botty; FAIL stands)
  - Deer / FSR / Chase / YERN / TCAT / LULU / BDOG / PITBULL / Womb / LOOM — prior FAILs stand
- GITPAID / SocialFrnk / EVERYTHING / TCAT2 / TRELLIS dropped out of in-window this pass (or below filters).

## Decision
**NO-TRADE** — stay in SOL (~0.2976). Only 1 NEW autopsy FAIL (CSF: creatorBal 0 + 12× band + ~4.2k tx/h botty + no socials + twin-mint + m5 −31). No clean PASS.

## Kraken
Watch-only. Last known USD cash ~$0.81 below min order — no proposal; no orders.
