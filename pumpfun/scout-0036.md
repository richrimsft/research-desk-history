# Scout 0036 — 2026-10-16 00:36 ET (America/New_York)

## Decision: **NO_TRADE**

## Wallet snapshot
- Address: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF`
- SOL (RPC getBalance): **0.378250232** (378250232 lamports) — unchanged
- Token-2022 ATAs: all **0** (empty positions: XsCPL…, TTWof…, 31GYU…pump, 3EC7g…pump, EBgMj…pump, cnNgF…pump, BMKd…, pumpCm…, NFLX7…, AKotz…pump, CZ3X9…pump)
- Classic SPL: USDT 0; USDC dust **0.000006** only
- Book: **all SOL**, no meme positions
- Est. total ≈ **$39.86** (SOL ~$105.37)

## Scout counts
- Feeds tagged 0036: DexScreener boosts-latest / boosts-top / profiles-latest OK; pump.fun currently-live OK (50); mcap/last-trade **404**; created **403** Cloudflare
- lists.txt: 4 lines (solana *pump from boosts+profiles+live)
- scan.py: **144 mints** → **79 cands** (`scan-0036.out`, `cands.json`)
- Strict numeric passers: **2** → autopsy-clean: **0**
- Near-misses noted: SXTR (botty 5.3k buys/h), FLOKI (mc $7.5k under floor), ROADSTER/GTA priors dumping

## Strict passers

### 1) GUILD `ABmp7kvhMFXEUvjq9cybBPPbrju8uv8GTQPCDbvLpump` — PRIOR STANDS (REJECT)
- pumpfun curve mc ~$25.5k, age ~0.67h, h1 +684%, 462b/346s
- Prior autopsy 0031: creator sent 52.1M (5.21%) to fresh #2 → dev+linked ~6.6% >5%; top10 ex-curve ~29%; wallet split into fresh bag
- Not drastically improved → **prior stands**. See `autopsy-summary-GUILD-0031.json` / `autopsy-summary-GUILD-0036-prior.json`

### 2) DarkStar / "OG Roadster" `9JYbTj84nzPQrS3zpkNGdwDRmmDA6i6wVaEtu1x5pump` — NEW → **REJECT**
- Numeric PASS: pumpfun curve mc ~$18.4k (was under floor at 0031), age ~2.4h, h1 +154%, m5 +35%, 213b/147s, not botty, mid-curve (~36% on bonding curve)
- Autopsy FAIL (any one enough to skip):
  - **Dev**: creatorBalance **0** (dumped early) — hard fail
  - **Holders**: top10 ex-curve **~30.7%** at/over 25–30% cap
  - **Socials / narrative**: name **OG Roadster**; website = Wikipedia Tesla Roadster; only social = borrowed X status link — ROADSTER copycat clutter (priors already burned this narrative)
  - Bundle: funders mostly aged/diverse — not the kill reason
  - RC score 1, mint/freeze none, graphInsiders 0 — not enough to override dumps/copycat
- Files: `autopsy-raw-DarkStar-0036.json`, `autopsy-summary-DarkStar-0036.json`, `funders-DarkStar-0036.json`

## Other window clutter (not strict / prior)
- SXTR GU3JGZr2… — h1 +458% but **5374 buys/h botty** → reject numeric
- ROADSTER 2B69… — 10k buys/h botty + prior family
- ROADSTER Eizz… / GTA / BANANA / `1` FSJb / VIMP / RDSTR / STARMAN / RUNNER / 123456 — priors stand or failing tape
- FLOKI FTbLCDt9… — h1 +56% but mc ~$7.5k under $15k floor

## Kraken
Watch-only. Last `/workspace/markets` snapshot showed USD cash **~$0.81** below min — no proposal (no fresh markets pull this run).

## Action
**None — stay in SOL.** Parent executes any future buy via browser; this scout does not trade.
