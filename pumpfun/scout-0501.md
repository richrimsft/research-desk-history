# Scout 0501 — 2026-10-16 05:01 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0501.json`); SPL: dust USDC only (~6e-06) + Token-2022 all zero → **no meme positions** (`wallet-spl-0501.json` / `wallet-t22-0501.json`). SOL unchanged since OPENSTOCK dump 01:33 ET.
- SOL ~$106.6 (`sol-price-0501.json`) → est. total ~$31.72.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0501.json` / `profiles-*-0501.json`
- pump.fun currently-live 49 → `pf-live-0501.json` (+ `_pf-live-as-list-0501.json`)
- `lists.txt` rebuilt (4 lines from boosts/profiles/CTO)
- scan.py: **146 mints** → 83 cands (`scan-0501.out` / `cands-0501.json`)
- expanded narrative dex searches + pf-live fill → **198** merged pairs (`expanded-0501.json`)

## In-window (age ≤4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| PRIOR | ROADSTER | ~$30k | 2.93 | +9 | −2 | pumpswap | `TB6QtGti9j2z…pump` |
| PRIOR | GULP | ~$16–25k | ~1.1 | +10..203 | −30 | pumpfun | `8BwEQTbuKD6D…pump` |
| PRIOR | SocialFrnk | ~$24–28k | 0.7 | +651..787 | +5..32 | pumpfun | `62tKjqdvzKrN…pump` |
| PRIOR | LULU | ~$23k | 1.2 | +10..15 | ~0 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | BDOG | ~$12–14k | 0.6 | +232..276 | −3..+10 | pumpfun | `G6NnKQTgN7Dm…pump` |
| PRIOR | TCAT | ~$13k | 2.6 | +27..65 | +44 | pumpfun | `34HExr1pEVFW…pump` |
| NEW | MemeTrace | ~$12–17k | 0.05–0.10 | +256..377 | spike | pumpfun | `HUARGQHB7ovb…pump` |
| NEW | MemeTrace | ~$6–12k | 0.06–0.13 | faded | −32 | pumpfun | `Aunf8ZYfEgRo…pump` |

→ **8** in-window at filter time, **2** NEW, **0** autopsy-clean PASS (`inwindow-0501.json` / `new-0501.json`)

## NEW autopsies
### MemeTrace `HUARGQHB7ovbPkUaYUmsqGBCLG4uHpCEr3q8zGcupump` — **FAIL**
- Phase: curve ~$12–17k, age **~6m** (<30m gate).
- Creator `6a29wP5C…` token bal **0** (RPC).
- Holders: **19×1–5% band**; top10 ex-curve ~22%.
- Funders: 2× share Axiom router dust; no clear 8+ same-funder block-0 bundle, but botty ntx=1000 wallets dominate.
- Socials: **none** (PF twitter/tg/web null; `/coins` empty-ish).
- Copycat: second concurrent MemeTrace mint live.
- Artifacts: `autopsy-summary-MemeTraceHUAR-0501.json`, `autopsy-raw-MemeTraceHUAR-0501.json`, `_holders-MemeTraceHUAR-0501.json`, `funders-MemeTraceHUAR-0501.json`, `rugcheck-MemeTraceHUAR-0501.json`, `dex-MemeTraceHUAR-0501.json`

### MemeTrace `Aunf8ZYfEgRozzi3ddBqu6bnAFgTVC882Ab2y4zVpump` — **FAIL**
- Phase: curve; mc **collapsed ~$6.1k** mid-autopsy (below $10k), age **~8m**, m5 **−32%**.
- Creator `G3p92QcW…` token bal **0**.
- Holders: **16×1–5% band**; top10 ex-curve ~22%.
- Funders: cabal hit `u6PJ8D…` (known from GALAX/prior); plus other sniper wallets.
- Socials: **none**. Copycat same symbol.
- Artifacts: `autopsy-summary-MemeTraceAunf-0501.json`, `autopsy-raw-MemeTraceAunf-0501.json`, `_holders-MemeTraceAunf-0501.json`, `funders-MemeTraceAunf-0501.json`, `rugcheck-MemeTraceAunf-0501.json`, `dex-MemeTraceAunf-0501.json`

## Prior rechecks (light)
- **SocialFrnk** (~$28k curve, 0.77h, h1 +787, m5 +32) — prior 0456 FAIL stands (creatorBal 0, 18× band, no socials). Momentum ≠ clean structure; not a post-grad dip hold.
- **GULP** (~$16k, m5 −30, still ~1.9k buys/h) — prior 0433 FAIL stands (creatorBal 0, band, botty); fading.
- **LULU** — prior BUNDLE FAIL stands (~$23k flat).
- **BDOG** (~$12k, sells>buys) — prior 0456 FAIL stands.
- **ROADSTER** / **TCAT** — prior FAILs stand; no post-grad 30–60% dip-and-hold setup.

## Decision
**NO-TRADE** — stay in SOL (~0.2976). No autopsy-clean PASS suitable for 0.15–0.25 SOL size.

## Kraken
Watch-only. Last snapshot (~Oct 15 09:50 ET) USD cash **$0.81** below min order — no proposal; no orders.
