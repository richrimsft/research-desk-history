# Scout 0231 — 2026-10-16 02:31 ET

## Wallet
- Address: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF`
- SOL: **297605540 lamports = 0.29760554 SOL**
- SPL/Token-2022: dust USDC only + zero-balance meme ATAs (no positions)

## Feeds
- `boosts-latest-0231.json` (30), `boosts-top-0231.json` (30), `profiles-latest-0231.json` (30)
- `pf-live-0231.json` (50)
- `lists.txt` rebuilt → `scan-0231.out` / `cands.json` (**76** mints)

## In-window filter
Criteria: age ≤4h, marketCap ≥10000, priceChange.h1 > 0

| Symbol | Mint (short) | NEW? | dex | mc | age_h | h1 |
|--------|--------------|------|-----|-----|-------|-----|
| CLAUDEMAN | DjrijJNopHhe… | YES | pumpfun | 27739 | 0.61 | +594 |
| RL | DRNqV2V6… | prior | pumpfun | 17018 | 0.84 | +378 |
| ERIC | DuaSA2Yy… | prior | pumpfun | 16333 | 0.98 | +328 |
| Optimus | 5b8F5y5u… | prior | pumpfun | 19597 | 2.87 | +30.6 |
| ELON-SAN | DkKywKTo… | prior | pumpswap | 93008 | 1.90 | +24.1 |

**In-window: 5 | NEW: 1**

## NEW autopsy — CLAUDEMAN
- Mint: `DjrijJNopHheVub1JdtJ7snqHS55kNY6kC5HNViTpump`
- Curve: ~61.0 SOL in pump.fun pool (~72% toward ~85 SOL grad) — phase OK
- RugCheck: score 1, not rugged, creatorBal **0**, 496 holders
- top10 ex-curve/LP: **~22.7%** (OK alone)
- Uniform 1.5–4.5% band: **13** wallets — cabal tell
- Socials: **none** (dex `info` null; empty meta description)
- Funders: no identical multi-wallet SOL bundle; **linked**: AArB9dpo (holder) funded Ayrxby7b (3.07%)
- pump.fun `/coins/<mint>`: 404 this run (used RugCheck + Dex instead)

### Decision: **FAIL**
Reasons: empty socials; creatorBal 0 + uniform cabal band; graph insider link.

## Decision
# **NO-TRADE** — remain in SOL. Prefer SOL over dirty autopsy.

## Key files
- `wallet-sol-0231.json`, `wallet-spl-0231.json`, `wallet-t22-0231.json`
- `boosts-*-0231.json`, `profiles-latest-0231.json`, `pf-live-0231.json`
- `lists.txt`, `scan-0231.out`, `cands.json`, `inwindow-0231.json`
- `autopsy-raw-CLAUDEMAN-0231.json`, `funders-CLAUDEMAN-0231.json`, `autopsy-summary-CLAUDEMAN-0231.json`
- `dex-CLAUDEMAN-0231.json`, `pf-coin-CLAUDEMAN-0231.json` (404)
- `trade-log.md`, `scout-0231.md`
