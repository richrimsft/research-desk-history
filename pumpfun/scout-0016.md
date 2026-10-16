# Scout 0016 — 2026-10-16 00:16 ET

## Decision
**NO_TRADE** — stay in SOL. No autopsy-clean rotate target.

## Wallet
- Address: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF`
- SOL: **0.378250232** (RPC getBalance)
- SPL: dust USDC 0.000006; Token-2022 ATAs (11) all zero
- SOL price ~$105.10 (DexScreener) → est. total ~**$39.75**

## Scout counts
- Feeds: boosts-latest/top + profiles-latest (200) + pf currently-live / mcap / last-trade / created (all 200; not Cloudflare-blocked this run)
- lists.txt: 207 pump-ending addresses → scan.py **250 mints** → `cands.json` 130 vol/age rows
- Strict numeric passers (mc $15–450k, age 0.5–3.5h, h1≥+20%, buys>sells, buys≲3k, mint*pump): **3** — all prior rejects
- Autopsy-clean buys: **0**

## Strict passers (rejected as priors)
| Sym | Mint | Why |
|-----|------|-----|
| 123456 | hps4Xy4…529pump | prior: top10 concentration + creator dumped |
| roadster | CbAeScGT…pump | prior: borrowed tweet, 5 insiders, copycat |
| ROADSTER | Eizz6UJU…pump | prior: revived/borrowed socials, copycat |

## Fresh near-misses
- **WAITIE** `zVXkMzD6…pump` — REJECT (`autopsy-summary-WAITIE-0016.json`): h1 +15.6% misses +20% gate; m5 −16% dumping; borrowed atrupar status link; top10 ex-LP ~27%.
- **EI** `DDaqBWhR…pump` — REJECT (`autopsy-summary-EI-0016.json`): mc ~$10k < $15k; creatorBalance 0; otcdesks + borrowed tweet.
- LUMINOUS / Eloncoin — dump or botty; skip.

## Kraken
Watch-only. Last markets snapshot 2026-10-15 09:50 ET: USD cash **$0.81** below min order — no proposal.
