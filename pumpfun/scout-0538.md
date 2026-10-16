# Scout 0538 — 2026-10-16 05:38 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0538.json`); SPL: dust USDC only (0.000006) + USDT 0; Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0538.json` / `wallet-t22-0538.json`). Unchanged since 01:33 ET.
- SOL ~$106.53 (CoinGecko, `sol-price-0538.json`) → est. total ~$31.70.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0538.json` / `profiles-*-0538.json`
- pump.fun currently-live 48 → `pf-live-0538.json`
- `lists.txt` rebuilt (4 lines)
- scan.py: **143 mints** → 82 cands (`scan-0538.out` / `cands-0538.json`)
- expanded (lists + pf-live + priors/watch + narrative searches) → **305 mints / 285 pairs** (`expanded-0538.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | GOAT11 | ~$210k | 1.09 | +165 | +10.6 | pumpswap | `GjkMsvYmuFR37SyK…pump` |
| NEW | Deer | ~$44k | 1.18 | +76 | −5.9 | pumpswap | `4tf5GEXU1dt7Vfj2…Deer` |
| PRIOR | ROADSTER | ~$36k | 3.55 | +5.9 | +0.3 | pumpswap | `TB6QtGti9j2zadAr…pump` |
| PRIOR | LULU | ~$24k | 1.81 | +4.6 | +0.5 | pumpfun | `8DQzWohFEMWruKUC…pump` |
| PRIOR | TCAT | ~$19k | 3.22 | +130 | +5.6 | pumpfun | `34HExr1pEVFWkx99…pump` |
| PRIOR | SOL | ~$15k | 0.56 | +266 | — | pumpfun | `2ezhap3jauQous1Z…pump` |
| PRIOR | BDOG | ~$13k | 1.25 | +18 | +1.5 | pumpfun | `G6NnKQTgN7Dmo9yr…pump` |
| NEW | DEER | ~$11k | 0.59 | +182 | −5.8 | pumpfun | `DYhpuvytVM4SCiR5…pump` |

→ **8** in-window, **2** NEW, **0** autopsy-clean PASS (`inwindow-0538.json` / `new-0538.json` / `_prior-rejects-0538.json`)

## NEW autopsies
### Deer `4tf5GEXU1dt7Vfj21oCu4P96ZEKEm3zMYqpzZsoCDeer` — **FAIL**
- The Kafkaesque Deer — PumpSwap ~$44k, 1.18h, h1 +76 / m5 −5.9, ~717/605 buys/sells.
- creatorBal **0**; **19×** 1–5% holder band; top10 ex-pool **~27.6%**; cabal `5tzFki…` hits ≥1 top holder.
- Socials: X community link + Instagram reel only (same IG as DEER). Post-grad chase.
- `autopsy-raw-Deer-0538.json` / `autopsy-summary-Deer-0538.json` / `_funders-Deer-0538.json`

### DEER `DYhpuvytVM4SCiR56q8oz4nXAN2BPFaYnxVftS9wpump` — **FAIL**
- Deer In Subway — aged in from watch-extra-0531 (was 0.46h). Curve ~57% bonding, ~$10.8k, 0.59h, h1 +182 / m5 −5.8.
- creatorBal **0**; **19×** 1–5% band; top10 ex-curve ~23.8%; status-tweet + same IG reel as Deer (copycat cluster; shared wallets VJSDW6S7 / 3VwmH9qY).
- Confirms prior RC pre-screen. `autopsy-raw-DEER-0538.json` / `autopsy-summary-DEER-0538.json` / `_funders-DEER-0538.json`

## Young watch (<30m) — `watch-extra-0538.json`
- **Irene** `6Vdc…pump` (~$80k PumpSwap, 0.29h, m5 +89) — RC FAIL-likely: creatorBal 0, band 14, 4 graphInsiders, post-grad chase. Do not buy.
- **GITPAID** `2MdBA…pump` (~$11k, 0.45h) — RC FAIL-likely: creatorBal≈0, band 15, top10ex ~29%.
- **BOUNCER / TRELLIS / Womb / Chase** — noted in young raw; not fully screened.
- **SLUDGE** (~$8.3k, 0.53h, m5 −26) — age past 30m but mc <$10k (excluded); still dumping; RC creatorBal 0 + band 19.

## Prior rechecks (light)
- **GOAT11** (~$210k, m5 +10.6, still ~1.3k tx/h) — RC recheck (`rc-GOAT11-0538.json`): prior FAIL stands (post-grad botty, cabal, empty X). creatorBal residual tiny; band 5; structure not clean enough + already chased.
- **TCAT** (~$19k, 3.22h, h1 +130 / m5 +5.6) — prior FAIL stands (creatorBal 0, 19× band); >3h not narrative leader.
- **ROADSTER / LULU / BDOG / SOL** — prior FAILs stand (copycat/BUNDLE/creatorBal 0 / age-gate FAIL at 0509).

## Decision
**NO-TRADE** — stay in SOL (~0.2976). Both NEW autopsies FAIL (creatorBal 0 + sniper bands / copycat deer cluster). No clean PASS.

## Kraken
Watch-only. Last known USD cash ~$0.81 below min order — no proposal; no orders.
