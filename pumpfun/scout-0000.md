# Scout 2026-10-16 00:00 ET

## Wallet
- SOL: **0.378250232** (RPC getBalance; lamports 378250232) @ ~$105.03 → ~$39.72
- Meme holdings: **none** (SYCAMORE/NULLCASH/SPOOKY Token-2022 ATAs uiAmount 0; all 11 T22 zero; SPL dust USDC 0.000006 only)

## Data refresh
- DexScreener: `boosts-latest-0000.json`, `boosts-top-0000.json`, `profiles-latest-0000.json` → `lists.txt` (3 lines)
- pump.fun: `pump-live-0000.json` OK (50); created/last-trade/mcap → Cloudflare challenge pages (skipped)
- `python3 scan.py` → `scan-0000.out` (**142 mints**, 81 vol/age rows)
- Filter dump: `interesting-0000.json`

## Filters
Prefer: mc $15k–450k, liq≥$15k or bonding w/ real buyers, age 0.5–3.5h, h1≥+20%, buys>sells h1, not botty (≪3k buys/h), no crowded copycat.

## Numeric passers → autopsy
| mint | symbol | result | why |
|------|--------|--------|-----|
| `hps4Xy4goXuV9zxdTAuF35tN58Gpks8Ho5zX529pump` | 123456 | **FAIL** | Prior reject; top10 ex-curve ~33.7%; creatorBalance 0 |
| `4XUmT22L7LN2e1us3bLHpPFKtkGUk9cAKQXEr3wXpump` | ETERNAL | **FAIL** | Prior; creatorBalance 0; insider transfer net 4 |
| `BEiJVDNjUYmgMEKeDuLTMqPRDVCW8Pgm5GuLk6Pxpump` | StayDown | **FAIL** | Age 6.5h past window; creator 0; top10 ~32% |

RugCheck raw: `autopsy-raw-hps4Xy4g.json`, `autopsy-raw-4XUmT22L.json`, `autopsy-raw-BEiJVDNj.json`

## Decision
**NO_TRADE** — stay in SOL. No clean autopsy passers.

## Kraken
Watch-only. No fresh `/workspace/markets` data this run; last snapshot (2026-10-15 09:50 ET) USD=$0.81 below min — no proposal.
