# Scout 0531 — 2026-10-16 05:31 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0531.json`); SPL: dust USDC only (0.000006) + USDT 0; Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0531.json` / `wallet-t22-0531.json`). Unchanged since 01:33 ET.
- SOL ~$106.59 (CoinGecko, `sol-price-0531.json`) → est. total ~$31.72.

## Feeds
- DexScreener boosts latest/top (29+30), profiles latest (30), community-takeovers (8) → `boosts-*-0531.json` / `profiles-*-0531.json`
- pump.fun currently-live 49 → `pf-live-0531.json`
- `lists.txt` rebuilt (4 lines)
- scan.py: **147 mints** → 82 cands (`scan-0531.out` / `cands-0531.json`)
- expanded (lists + pf-live + priors/watch + narrative searches) → **238 mints / 224 pairs** (`expanded-0531.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | GOAT11 | ~$185k | 0.96 | +330 | −0.5 | pumpswap | `GjkMsvYmuFR37SyK…pump` |
| PRIOR | ROADSTER | ~$36k | 3.42 | +9 | −0.6 | pumpswap | `TB6QtGti9j2zadAr…pump` |
| PRIOR | LULU | ~$23k | 1.68 | +3.9 | +0.3 | pumpfun | `8DQzWohFEMWruKUC…pump` |
| PRIOR | TCAT | ~$19k | 3.09 | +137 | +32 | pumpfun | `34HExr1pEVFWkx99…pump` |
| PRIOR | BDOG | ~$12k | 1.12 | +18 | +8.6 | pumpfun | `G6NnKQTgN7Dmo9yr…pump` |

→ **5** in-window, **0** NEW, **0** autopsy-clean PASS (`inwindow-0531.json` / `new-0531.json` / `_prior-rejects-0531.json`)

## NEW autopsies
None — no NEW names in window.

## SLUDGE / DEER (from watch-extra-0525)
Still **under 30m** by DexScreener pairCreatedAt (pump.fun `/coins/{mint}` 404s): DEER **0.46h** (~$11.5k, h1 +202), SLUDGE **0.38h** (~$12.7k, h1 +265, m5 **−34**, off ~$19k). Not in window. RugCheck pre-screen (`rc-DEER-0531.json` / `rc-SLUDGE-0531.json`) already shows standard fail flags on both: **creatorBal 0**, **19×1–5% holder band**, top10 ex-curve ~26% (DEER) / ~22% (SLUDGE), no insiders flagged. Expect FAIL when they age in.
- GITPAID `2MdBA1Yiy3oC…pump` (~$20k, 0.30h, h1 +450) — too young; noted in `watch-extra-0531.json`.

## Prior rechecks (light)
- **TCAT** (~$19k, 3.09h, h1 +137 / m5 +32 — the only material move) — RugCheck recheck (`rc-TCAT-0531.json`): creatorBal **0**, 19×1–5% band, top10 ex-curve ~21%, 256 holders. Still FAIL; also >3h and not the narrative leader.
- **GOAT11** (~$185k, ~15.9k tx/h botty) — FAIL stands (post-grad chase, botty, cabal `5tzFki…`, empty X).
- **ROADSTER** `TB6Q…` — FAIL stands (copycat, creatorBal 0, 26 insiders, whale ~25%; `autopsy-summary-ROADSTER-0311.json`).
- **LULU** (BUNDLE) / **BDOG** (creatorBal 0, band; h1 sells>buys 436/271) — FAILs stand.

## Decision
**NO-TRADE** — stay in SOL (~0.2976). Zero NEW candidates; all in-window names are prior structural FAILs.

## Kraken
Watch-only. Last known USD cash ~$0.81 below min order — no proposal; no orders.
