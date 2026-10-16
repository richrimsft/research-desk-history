# Scout 0603 — 2026-10-16 06:03 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0603.json`); SPL: dust USDC only (0.000006) + 1 zero acct; Token-2022: 12 accounts all zero → **no meme positions** (`wallet-spl-0603.json` / `wallet-t22-0603.json`). Unchanged since 01:33 ET.
- SOL ~$105.98 (CoinGecko, `sol-price-0603.json`) → est. total ~$31.54.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0603.json` / `profiles-*-0603.json`
- pump.fun currently-live 48 → `pf-live-0603.json`; pump.fun sorted lists (mcap/last-trade/created) → `pf-sorted-0603.json`
- `lists.txt` rebuilt (4 lines)
- scan.py: **144 mints** → `scan-0603.out` / `cands-0603.json`
- expanded (lists + pf-live + pf-sorted + priors/watch + narrative searches, `expand0603.py`) → **443 mints / 424 pairs** (`expanded-0603.json`)

## In-window (age 0.5–4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| NEW | ElonThrust | ~$816k | 0.60 | +1741 | +2.35 | pumpswap | `pFibPnQk8ekCCtuB…pump` |
| PRIOR | Irene | ~$86k | 0.67 | +114 | -10.3 | pumpswap | `6VdcMnBTCj4tJVwt…pump` |
| PRIOR | CCAT | ~$53k | 3.83 | +1.04 | -9.01 | pumpswap | `D4rzv9WAXJh9QZw1…pump` |
| PRIOR | Deer | ~$34k | 1.57 | +141 | -11.61 | pumpswap | `4tf5GEXU1dt7Vfj2…Deer` |
| PRIOR | ROADSTER | ~$32k | 3.95 | +7.5 | — | pumpswap | `TB6QtGti9j2zadAr…pump` |
| PRIOR | LULU | ~$24k | 2.20 | +1.08 | -0.01 | pumpfun | `8DQzWohFEMWruKUC…pump` |
| PRIOR | TCAT | ~$18k | 3.61 | +45 | -14.78 | pumpfun | `34HExr1pEVFWkx99…pump` |
| NEW | YERN | ~$17k | 0.58 | +414 | -8.03 | pumpfun | `PdtREY9H6Fp9jVMp…yern` |
| PRIOR | SOL | ~$15k | 0.96 | +266 | — | pumpfun | `2ezhap3jauQous1Z…pump` |
| NEW | TCAT (2nd mint) | ~$14k | 1.68 | +188 | +18.39 | pumpfun | `6ZDKgWopksQPMBPQ…pump` |
| NEW | Chase | ~$13k | 0.59 | +229 | -13.98 | pumpfun | `YwCKitMEdf7nagej…pump` |
| PRIOR | Womb | ~$12k | 0.79 | +289 | +16.88 | pumpfun | `BxUHuVGyP9kKRoJZ…pump` |
| PRIOR | GITPAID | ~$11k | 0.83 | +201 | +51.27 | pumpfun | `2MdBA1Yiy3oCFmwy…pump` |

→ **13** in-window, **4** NEW, **0** autopsy-clean PASS (`inwindow-0603.json` / `new-0603.json` / `_prior-rejects-0603.json`)

## NEW autopsies
### ElonThrust `pFibPnQk8ekCCtuBoQFJqeJjHVo92dAME3uH8A4pump` — **FAIL**
- ElonThruster — graduated → PumpSwap (liq ~$76k), ~$815k, 0.60h, h1 +1740 / m5 +2.3.
- FAIL: post-grad blind chase (~$815k after +1740% h1)
- FAIL: single non-pool wallet `CkWRijad…` (system acct, 20.1 SOL) holds **14.06%**
- FAIL: creatorBal 0; deployer `G8thC28H…` is 1.5h-old, 673 tx, now holds 11.6 SOL (dev sold)
- FAIL: RC "High holder correlation" (score 30)
- FAIL: fake volume — ~13.6k tx/h for ~$60k h1 vol (~$4/tx micro-churn)
- FAIL: X @melissa31zb9 created 2026-10-03, 2 followers, 1 tweet; no website
- top10ex ~15.1% (incl. 14.06% whale); band 1; holders 2270.
- `autopsy-raw-ElonThrust-0603.json` / `autopsy-summary-ElonThrust-0603.json` / `funders-ElonThrust-0603.json` / `rc-ElonThrust-0603.json`

### YERN `PdtREY9H6Fp9jVMpG36aywtCgxTtsQZetmehKqgyern` — **FAIL**
- yern.fun — pumpfun curve (Printr-config; curve acct holds 38.65% of supply, SOL reserve not readable via lamports), ~$16.7k, 0.58h, h1 +414 / m5 -8.
- FAIL: creatorBal 0 (creator = fee-share PDA, 0.006 SOL)
- FAIL: **19×** wallets in 1–5% band on only 149 holders
- FAIL: holder `4qFGc44W` (2.03%) funded by known cabal `5tzFki…`
- FAIL: X @yerndotfun created 2026-10-14 (24 foll / 10 tweets) — brand-new
- top10ex ~23.2%; graphInsiders 0; RC score 1.
- `autopsy-raw-YERN-0603.json` / `autopsy-summary-YERN-0603.json` / `funders-YERN-0603.json` / `rc-YERN-0603.json`

### TCAT (2nd mint) `6ZDKgWopksQPMBPQvmdZrP13JEPApbNrSUQLPPbQpump` — **FAIL**
- Tesla Roadster Cat — pumpfun curve (Printr-config; curve acct holds 43.53%), ~$13.7k, 1.68h, h1 +188 / m5 +18.
- FAIL: creatorBal 0; deployer `FB5p7woP…` burner (6 tx, 0 SOL)
- FAIL: **19×** 1–5% band on only 73 holders
- FAIL: top10ex ~27.0% (at limit)
- FAIL: copycat of prior-FAIL TCAT theme; X-community link only; thin ($9.6k h1 vol)
- `autopsy-raw-TCAT2-0603.json` / `autopsy-summary-TCAT2-0603.json` / `funders-TCAT2-0603.json` / `rc-TCAT2-0603.json`

### Chase `YwCKitMEdf7nagejZbvpDvxDui5CdoQ3NuJsE5Tpump` — **FAIL**
- Chase Chadwick — pumpfun curve ~38.9% (~33.066 SOL), ~$13.3k, 0.59h, h1 +229 / m5 -14.
- FAIL: creatorBal 0 (creator fee-share PDA)
- FAIL: fresh wallet `RuYU2iRM…` (1 tx, created at launch) holds **5.64%** — linked/sniper bag
- FAIL: **15×** 1–5% band
- FAIL: botty churn ~1.9k tx/h, ~$78k h1 vol on ~$13k mc; m5 -14 fading
- FAIL: socials = link to third-party tweet (@Humanevolvd, 33k foll.) only; no project X
- top10ex ~23.9%; graphInsiders 0. (Different mint from prior FAIL Chase `9vz5…`.)
- `autopsy-raw-Chase-0603.json` / `autopsy-summary-Chase-0603.json` / `funders-Chase-0603.json` / `rc-Chase-0603.json`

## Young watch (<30m) — `watch-extra-0603.json`
- **CSF** `DDw2yrhhZNCp…` (~$11.3k, 0.08h) / **CSF** `6aNXLr6d9m2g…` (~$18.1k, 0.23h, m5 −31) — twin-mint pair, likely copy war
- **NEBULA** `CaGJEqcDsyUr…` (~$11.3k, 0.11h)
- **Irene** `5j7gTphd94qD…` (~$28.8k, 0.11h, pumpswap) / **Irene** `2xZjZSFkuFvT…` (~$22.5k, 0.48h, pumpswap) — copycats of prior-FAIL Irene
- **BOUNCER** `6X3cMFWWNQSV…` (~$188.6k, 0.47h, pumpswap, h1 +1797) — post-grad chase; do not buy blind

## Prior rechecks (light)
- No prior materially improved: Irene ~$86k (down from ~$102k, m5 −10); Womb ~$12.4k (mc down, m5 bounce only); GITPAID ~$10.9k (down from ~$19k, m5 +51 bounce); TCAT ~$17.7k (down); Deer / CCAT / ROADSTER / LULU / SOL flat-to-down — prior FAILs stand.
- TRELLIS dropped out of in-window (h1/mc filter).

## Decision
**NO-TRADE** — stay in SOL (~0.2976). All 4 NEW autopsies FAIL (post-grad whale/botty ElonThrust; creatorBal 0 + 15–19× sniper bands on YERN/TCAT/Chase, plus cabal funder / fresh 5.6% wallet / brand-new socials). No clean PASS.

## Kraken
Watch-only. Last known USD cash ~$0.81 below min order — no proposal; no orders.
