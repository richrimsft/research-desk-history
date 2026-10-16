# pump.fun scout 2209 ET — watch-only
Generated: 2026-10-15 22:14 ET

## Wallet (RPC mainnet-beta)
- Address: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF`
- SOL: **0.346122758** (~$36.35 @ $105.01/SOL)
- Tokens with balance>0:
  - SYCAMORE `3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump`: **19,904.206434** tok (~$6.52 @ $0.0003276)
  - USDC dust: 6e-06 (ignore)
- Surprise positions: NONE (Token + Token2022 scanned)
- Est. total portfolio: **~$42.87**

## SYCAMORE
- mc: **$317,754** | liq: **$54,495** | dex: pumpswap
- priceUsd: 0.0003276
- m5: **−3.64%** | h1: **+9.01%** | h6: +7.35% | h24: +546%
- h1 buys/sells: **746/423** | m5 buys/sells: **72/52**
- h1 vol: ~$186k
- age: ~18.4h | entry mcap ~$300k → now ~$318k (**~+5.9%**)
- RugCheck (22:13 ET): score 1 / normalised 1; risks=[]; rugged=false; mint/freeze auth None; lpLockedPct~100%; graphInsidersDetected=0. Top holder LP (~8.7%); top10 ex-LP ~16.6% (under 25%). Creator `4ksbmVvz…` balance ~0.13% supply (not a dump trigger). Prior runs flagged creator-rug history elsewhere — vigilance-only.
- Dump gate: **NOT met** — mc well above $180–200k; m5/h1 buys ≫ sells; h1 still green (+9%).
- **Recommendation: HOLD**

### Devil's advocate (sell case — rejected)
Could argue trimming into a cool-down: h1 momentum faded from ~+41% (22:06 scout) to +9%, m5 is lightly red (−3.6%), bag is only ~$6.52 (~15% of book), age ~18h is past the 0.5–3h narrative window, and creator still holds a token balance (albeit ~0.13%). Counter: dump gate requires breakdown below ~$180–200k **with** sells≥buys on m5/h1 — none of that is present (mc $318k, 746/423 h1, 72/52 m5). On-chain concentration remains healthy (LP-led, 0 graph insiders, mint/freeze revoked, LP ~100% locked). Selling now crystallizes a small paper win and forfeits residual upside while flow is still buy-heavy. **Do not sell.**

## Scout / numeric filter
Universe: DexScreener boosts latest/top + profiles + searches (pump/pumpswap/pumpfun/meme/new solana meme/graduated pump) + frontend-api-v3 currently-live / last_trade / market_cap / created (+ lists.txt merge).
- Unique Solana `*pump` mints: **241**
- Best-pairs resolved: **228**
- Numeric passers (mc $15k–$450k, liq≥$15k, age≥1h, h1≥+20%, buys>sells, not botty; age>3h needs h1≥+40%): **1**
- Autopsy clean: **0**

### Numeric passer → autopsy
- PONK `4jjQjDRYd7xLcFMViRsz4GvtgU6gPZgbVaxN3Rq9pump` — mc~$98k liq~$27k age **25.0h** h1 +62% (801/537) — **REJECT**
  - Holders: top10 ex-curve/LP **36.2%** (FAIL >30%)
  - Insiders: graphInsidersDetected=**61**; 6 transfer nets ~10.8% supply (FAIL)
  - Dev hold: creatorBalance=0 (PASS)
  - Deployer history: no creatorTokens in RugCheck / empty creator coins list (INCONCLUSIVE; prior reject)
  - Bundle (early/block-0): recent swap-api sample only (100 trades ~6m window) — no 8+ identical SOL cluster; residual insider graph used as proxy (FAIL soft)
  - Socials: X @PEPEBONKK joined 2026-10-07, 374 foll / 218 tweets (not empty — soft PASS)
  - Narrative: **25h** ≫ 0.5–3h preferred window (FAIL)
  - Prior scouts (2156/2203/2204): concentration / past-narrative reject — confirmed

### Near rejects (not passers — no autopsy)
- `1` `Gn8Xti76…pump` — mc~$404k liq~$55k age **0.97h** h1 +790% — **YOUNG + botty** (15,662 h1 buys)
- CatTok `A5YQxuXB…pump` — mc~$157k liq~$33k age **0.79h** h1 +245% — **YOUNG + botty** (7,383 h1 buys)
- NVIDIA `Bjr6DbMs…pump` — mc~$450k age **0.12h** h1 +930% — **YOUNG**
- Before GTA `Ewzy4cxD…pump` — mc~$61k age **0.20h** h1 +34% — **YOUNG**
- Holdoween `3UYqfnBm…pump` — mc~$905k (over MC cap) + age 0.69h + botty
- STREAM `Diy4Q5ai…pump` — mc~$180k h1 +5% sells>buys — fails mom + flow
- FTR / EI / DJT — over MC and/or botty

## ACTION
**none** — hold SYCAMORE; keep ~0.35 SOL dry powder. Sole numeric passer (PONK) failed autopsy (holders + insiders + age). Nothing beats parking SOL + SYCAMORE bag this cycle. No BUY, no SELL.

## Key files
- /workspace/pumpfun/wallet-sol-2209.json / wallet-tokens-2209.json / wallet-tokens2022-2209.json
- /workspace/pumpfun/sycamore-2209.json / sycamore-2209-final.json / sol-price-2209.json / sol-price-2209-meta.json
- /workspace/pumpfun/boosts-latest-2209.json / boosts-top-2209.json / profiles-latest-2209.json
- /workspace/pumpfun/dex-search-*-2209.json / pf-2209-*.json
- /workspace/pumpfun/mints-2209.txt / pairs-all-2209.json
- /workspace/pumpfun/cands-filter-2209.json / cands-near-2209.json / cands-meta-2209.json
- /workspace/pumpfun/autopsy-PONK-2209.json / rc-sum-PONK-2209.json / rc-full-PONK-2209.json
- /workspace/pumpfun/rc-sum-3EC7gRDG-2209.json / rc-full-3EC7gRDG-2209.json
- /workspace/pumpfun/scout-2209.md (this file)

---
## Append-ready log block
```
## 2026-10-15 22:14 ET — position watch (no trade)
SOL ~$105.01. Wallet SOL 0.346122758 (~$36.35). Prices via DexScreener + RPC.
- SYCAMORE `3EC7gRDGKgqPHc9ipJxxChoeyseE2xAbQHZUSSTfpump`: 19,904.21 tok @ $0.0003276, mcap $317.8k vs entry ~$300k (**~+5.9%**, ~$6.52). m5 −3.6% (72b/52s) · h1 +9.0% (746b/423s) · liq $54.5k. Buyers ~1.8:1 on h1 — dump gate not met; hold.
- Est. total ~$42.87 (incl. SOL).
Scout: 241 Solana `*pump` mints → 228 pairs → **1** numeric passer (PONK) → **0** autopsy-clean. PONK REJECT: top10 ex-LP 36% + 61 graph-insiders + age 25h.
- Near: `1`/CatTok/NVIDIA (age <1h ± botty); STREAM (sells≥buys); Holdoween over MC.
Nothing beats parking ~0.35 SOL + SYCAMORE bag. Action: none.
```
