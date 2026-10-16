# Scout 0442 — 2026-10-16 04:42 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0442.json`); SPL: dust USDC only (~6e-06) + zero USDT → **no meme positions** (`wallet-spl-0442.json`). SOL unchanged since OPENSTOCK dump 01:33 ET.
- SOL ~$106.56 (`sol-price-0442.json`) → est. total ~$31.71.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0442.json` / `profiles-*-0442.json`
- pump.fun currently-live 50 → `pf-live-0442.json` (+ `_pf-live-as-list-0442.json`)
- `lists.txt` rebuilt (5 lines, ~74 unique + pf-live)
- scan.py: **146 mints** → 88 cands (`scan-0442.out` / `cands-0442.json`)
- expanded narrative dex searches → **292** merged pairs (`expanded-0442.json`)

## In-window (age ≤4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| NEW | SpaceX | ~$392k | 0.05 | +784 | +784 | pumpswap | `vHRVLH6RDNee…pump` |
| PRIOR | LOOM | ~$204k | 1.85 | +26 | −19 | pumpswap | `7GCMYJcykHZ3…pump` |
| PRIOR | GULP | ~$25k | 0.73 | +327 | +46 | pumpfun | `8BwEQTbuKD6D…pump` |
| PRIOR | LULU | ~$23k | 0.88 | +670 | +2 | pumpfun | `8DQzWohFEMWr…pump` |
| PRIOR | Dragon | ~$12k | 0.96 | +118 | +32 | pumpfun | `9gG2evdn4HgP…pump` |

→ **5** in-window, **1** NEW, **0** autopsy-clean PASS (`inwindow-0442.json` / `new-0442.json`)

## NEW autopsy
### SpaceX `vHRVLH6RDNeeMhcAsyNifSBvSRFFv1PD5RwVTempump` — **FAIL**
- Phase: already **PumpSwap** ~$392k, pair age ~3m (post-grad spike).
- Age gate: **FAIL** (<30m).
- Creator `AANH2…` token bal **0** (RPC); deployer wallet ~602 SOL.
- RugCheck: score_norm 40; risks = High holder correlation (17) + **Copycat** (verified SpaceX symbol).
- Holders: **17** wallets with identical ~464072.557 amounts (bot/bundle dust). Funders ambiguous (many oldest-tx None / tiny 0.01 SOL) but identical amounts enough.
- Socials: none (PF `/coins/<mint>` 404).
- Artifacts: `autopsy-summary-SpaceX-0442.json`, `autopsy-raw-SpaceX-0442.json`, `_holders-SpaceX-0442.json`, `funders-SpaceX-0442.json`, `rugcheck-SpaceX-0442.json`, `dex-SpaceX-0442.json`

## Prior rechecks (light)
- **LOOM** (~$204k, botty ~8.2k buys/h) — prior FAIL stands (creatorBal 0 / churn / band).
- **GULP** (~$25k curve, 0.73h, h1 +327) — prior 0433 FAIL stands (creatorBal 0, band, botty).
- **LULU** — prior BUNDLE FAIL stands.
- **Dragon** — prior 0417 FAIL stands (creatorBal 0, band, no socials).

## Decision
**NO-TRADE** — stay in SOL (~0.2976). No autopsy-clean PASS suitable for 0.15–0.25 SOL size.

## Kraken
Watch-only. No material change assumed (~$0.81 USD below min from prior) — no proposal; no orders.

