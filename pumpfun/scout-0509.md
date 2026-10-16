# Scout 0509 — 2026-10-16 05:09 ET

## Wallet
- `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` RPC **0.29760554 SOL** (297605540 lamports, `wallet-sol-0509.json`); SPL: dust USDC only (~6e-06) + Token-2022 all zero → **no meme positions** (`wallet-spl-0509.json` / `wallet-t22-0509.json`). SOL unchanged since OPENSTOCK dump 01:33 ET.
- SOL ~$106.59 (`sol-price-0509.json`) → est. total ~$31.72.

## Feeds
- DexScreener boosts latest/top (30+30), profiles latest (30), community-takeovers (8) → `boosts-*-0509.json` / `profiles-*-0509.json`
- pump.fun currently-live 50 → `pf-live-0509.json` (+ `_pf-live-as-list-0509.json`)
- `lists.txt` rebuilt (4 lines from boosts/profiles/CTO)
- scan.py: **145 mints** → cands (`scan-0509.out` / `cands-0509.json`)
- expanded narrative dex searches + pf-live fill → **207** merged pairs (`expanded-0509.json`)

## In-window (age ≤4h, mc ≥$10k, h1>0, dex pump/pumpswap)
| tag | symbol | mc | age_h | h1 | m5 | dex | mint |
|-----|--------|-----|-------|-----|-----|-----|------|
| NEW | GOAT11 | ~$163–175k | 0.61 | +267..292 | −3..+14 | pumpswap | `GjkMsvYmuFR37SyK…pump` |
| NEW | FSR | ~$63–65k | 0.49 | +50..54 | +11..25 | pumpswap | `HiKU8Lsa8aUFkhtC…pump` |
| PRIOR | MemeTrace | ~$24k | 0.20 | +580 | +10 | pumpfun | `HUARGQHB7ovbPkUa…pump` |
| PRIOR | LULU | ~$23k | 1.33 | +1.7 | — | pumpfun | `8DQzWohFEMWruKUC…pump` |
| NEW | Chase | ~$11–16k | 0.07 | +212..379 | spike | pumpfun | `9vz5mXmJnNjmC8on…pump` |
| NEW | SOL | ~$15k | 0.08 | +266 | +266 | pumpfun | `2ezhap3jauQous1Z…pump` |
| PRIOR | GULP | ~$14–16k | 1.17 | +37 | −5 | pumpfun | `8BwEQTbuKD6DyHsr…pump` |
| PRIOR | TCAT | ~$12k | 2.73 | +6 | −10 | pumpfun | `34HExr1pEVFWkx99…pump` |
| PRIOR | BDOG | ~$11k | 0.77 | +194 | −11 | pumpfun | `G6NnKQTgN7Dmo9yr…pump` |

→ **9** in-window at filter time, **4** NEW, **0** autopsy-clean PASS (`inwindow-0509.json` / `new-0509.json`)

## NEW autopsies
### GOAT11 `GjkMsvYmuFR37SyKnJoD8DwccLb3HKMQBnNe5Nqbpump` — **FAIL**
- Phase: **pumpswap post-grad** ~$168–175k; pair created **04:35 ET** (~40m age). Explicit no-chase after graduation spikes.
- Creator `BEWzEmGU…` token bal ~449k (~0.05%) OK; but unlocked LP still held by creator (~22% of LP).
- Holders: band_1_5 **3** OK; top10 ex-pool ~10.6% OK; graphInsiders 0.
- Volume: **~6.4k buys / 5.2k sells / ~$1.5M h1** on ~$170k mc → ~9× churn (botty).
- Funders: **2×** share cabal `5tzFki…` (known GALAX/POKESQUAD/Dragon); 6/12 checked wallets ntx≥1000.
- Socials: X/TG/site present, but X `@GOAT11SOL` **near-empty** (21 followers, 5 tweets; old 2014 handle, dormant/repurposed).
- Artifacts: `autopsy-summary-GOAT11-0509.json`, `autopsy-raw-GOAT11-0509.json`, `_holders-GOAT11-0509.json`, `funders-GOAT11-0509.json`, `rugcheck-GOAT11-0509.json`, `dex-GOAT11-0509.json`

### FSR / Flying Solana Roadster `HiKU8Lsa8aUFkhtCMWp3ySCcpZ899zEhRqzvEgnSpump` — **FAIL**
- Phase: pumpswap ~$63k, age **~0.5h** (≤30m gate borderline).
- Creator `7KocpDKH…` token bal **0**.
- Holders: **16×1–5% band**; top10 ex-pool ~24–27%; graphInsiders **4**.
- RugCheck score **13911** (Large LP Unlocked danger + Low Liquidity).
- Funders: cabal `5tzFki…` @ **~19.6 SOL** into a top holder; 8/12 ntx≥1000.
- Socials: **status-tweet only** (`x.com/solana/status/…`) + otcdesks.cash — not project socials.
- Artifacts: `autopsy-summary-FSR-0509.json`, `autopsy-raw-FSR-0509.json`, `_holders-FSR-0509.json`, `funders-FSR-0509.json`, `rugcheck-FSR-0509.json`, `dex-FSR-0509.json`

### Chase / Chase Chadwick `9vz5mXmJnNjmC8onX5tjfrRADuYYZXJ9qLkm1mWJpump` — **FAIL**
- Phase: curve; age **~5m** (<30m); mc faded ~$16k→~$10.5k mid-run.
- Creator `6o23RbWz…` token bal **0**.
- Holders: **11×1–5% band**; top10 ex-curve ~19%.
- Funders: cabal `u6PJ8D…` hit (known GALAX/MemeTrace).
- Socials: **none**.
- Artifacts: `autopsy-summary-Chase-0509.json`, `autopsy-raw-Chase-0509.json`, `_holders-Chase-0509.json`, `funders-Chase-0509.json`, `rugcheck-Chase-0509.json`, `dex-Chase-0509.json`

### SOL / tesla `2ezhap3jauQous1ZxS4LDq6cXv7NrDLQbziVkbSTpump` — **FAIL**
- Phase: curve ~$15k, age **~6m** (<30m); only 9 buys/5 sells h1.
- Creator `9BXEDSb…` token bal **0**; RugCheck **Creator history of rugged tokens** + single-holder ~51% + high concentration (score 30119).
- Copycat: name **tesla** / symbol **SOL**.
- totalHolders **3**; no socials.
- Artifacts: `autopsy-summary-SOL-0509.json`, `autopsy-raw-SOL-0509.json`, `_holders-SOL-0509.json`, `funders-SOL-0509.json`, `rugcheck-SOL-0509.json`, `dex-SOL-0509.json`

## Prior rechecks (light)
- **MemeTrace HUAR** (~$24k, 0.2h) — prior 0501 FAIL stands (age, creatorBal 0, band, no socials, copycat).
- **LULU** (~$23k flat) — prior BUNDLE FAIL stands.
- **GULP** (~$14–16k, m5 −5) — prior 0433 FAIL stands (creatorBal 0, band, botty); fading.
- **TCAT** / **BDOG** — prior FAILs stand; no clean post-grad 30–60% dip-and-hold setup.

## Decision
**NO-TRADE** — stay in SOL (~0.2976). No autopsy-clean PASS suitable for 0.15–0.25 SOL size. Closest structure (GOAT11) still fails hard on post-grad chase + botty churn + cabal funder + empty X.

## Kraken
Watch-only. Last snapshot (~Oct 15 09:50 ET) USD cash **$0.81** below min order — no proposal; no orders.

## Notes
- `frontend-api-v3.pump.fun/coins/{mint}` returned 404 for all NEW (same as 0501 run); creator/balance/socials taken from RugCheck + DexScreener. `currently-live` still works.
