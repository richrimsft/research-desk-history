# Scout 23:46 ET Oct 15 2026 — all-SOL book, hunt for clean buy

Wallet: `BXc3ju3mY68Kx9bM5f7akE2urdsNe7SiSpMmxzsVjyNF` — **0.378250232 SOL** (RPC `getBalance` confirmed).  
Token accounts: dust USDC `0.000006` + USDT 0; all Token-2022 meme ATAs **0** (empty SYCAMORE / prior bags). Book = **all SOL**.  
SOL USD used: **~$105.02** (DexScreener SOL pairs) → book ≈ **$39.72**.

## Scan
- Refreshed `lists.txt` (boosts latest/top + profiles latest) + `pf-live.json` (50 live)
- `python3 scan.py` → **143 mints** → `scan-2346.out` / `cands.json` (83 vol/age rows)
- Broader Dex token fetch + search → `all-scout-pairs-2346.json` / `cands-window-2346.json`
- **Strict numeric passers** (mc $15–450k, age 0.5–3.5h, h1 ≥+20%, buys>sells, not botty, pump mint, not prior-reject): **0**
- **Autopsy-clean buys: 0**

## Autopsies (FAIL any = skip)

### IKE `FZ9jKav6BAEEaBZtq6RPpMnVupQdopvvMiocZMEVpump` (best near-miss)
- Dex: pumpfun bonding, mc ~$15.9k, liq n/a (curve), age **~4.1h** (past 3.5h narrative window), m5 −3%, h1 +27–31%, **47b/39s** (thin), m5 1b/3s
- RC: score 1 / mint+freeze none / graphInsiders **0** / creatorBalance **0** / bonding LP locked 100% on curve reserves
- Holders: #1 unlabeled ~38% (bonding curve) → **top9 ex-curve ~28.2%** (at 25–30% fail band; #2–#6 each ~3.1–3.7%)
- Socials: Dex = X **community** link only (`x.com/i/communities/...`); no own account / no site
- **FAIL:** age past window + thin flow + top10 ex-curve ~28% + weak socials. Not a leader.

### ETERNAL `4XUmT22L7LN2e1us3bLHpPFKtkGUk9cAKQXEr3wXpump` (prior reject — re-check)
- Dex/pf: still bonding, mc ~$14.6–14.7k (**under $15k floor**), age ~1.2h, h1 +133–138%, 122b/43s, m5 +1–2%
- RC: score 1 / 0 insiders / top9 ex-curve ~**18.8%** OK / mint+freeze none
- Creator: balance now **0** (was ~6.6% at 23:22) → **early dump** red flag
- Socials: pf shows `@MinesCryptoZNFT` + minescrypto.space; Dex socials still empty/null
- **FAIL:** prior reject; creator dumped; mc under floor. Do not chase.

### ONE / `1` `FSJbL5UjbZkkMWNeKnUgjG6PHQKdbhhycugDo1LCpump` (new mint, not Gn8)
- Dex: **graduated** pumpswap, mc ~$90–95k, liq ~$24–25k, age **~0.5h**, h1 +93–102%, **~4500–4700b / ~420s** (!), m5 −6 to −14% with 675b/68s
- RC: score 1 / 0 insiders / creatorBalance 0 / LP locked 100%; top10 ~29% (ex-#1 ~16% if #1 is AMM)
- Socials: own X `@inu1coin` + inu1coin.lol (OK on paper)
- **FAIL botty:** ≳4.5k buys/h on modest mc + brand-new graduation spike (expect 30–60% dip). Symbol/`1` adjacency to prior `1` reject. Skip.

### SUPERCYCLE `84AaE16zkQ97UqeRsbZwkkDQJn9L3v4nUqrMMZ3Xpump`
- Dex: pumpswap, mc ~$8.7–9.0k (**under floor**), liq ~$6.7–6.9k (**<$15k**), age ~1.5h, h1 +48%, 110b/83s
- RC: score_norm **18**, risk **Low Liquidity $2.3k**; holder table messy (top10 sum >100%); concentration extreme even ex-#1
- Socials: **borrowed tweet-only** (`x.com/gettindevvy/status/...`) — fail
- **FAIL:** mc/liq floors + borrowed socials + low liq warn.

### UNBUY `2XJTEyYAtrU4K4UBAzJY2cjr4BM29WWaofmPMjPbpump` (optional age-check)
- Age **~11.2h** (far outside window); top9 ex-curve ~**47%**; creator still ~1.6% supply
- **FAIL:** age + concentration. Not a buy.

## Prior rejects still in tape (not re-bought)
BANANA (botty 10k+/h), TESLON (creator rug history), GTA (whale+insiders), ROADSTER/RDSTR (revived/borrowed), DEXTERM, MENTOR (concentration), STARMAN, NINNY (insiders+creator sold+mc floor), BOT, DarkStar, STREAM, PONK, Nihilism, GPU, `1` Gn8, FSD, ETERNAL, Macca.

## Verdict
**HOLD SOL** — no autopsy-clean setup in the preferred 0.5–3.5h / $15–450k / real-flow window.  
Best near-miss IKE fails age + concentration + thin tape; only hot prints are botty graduation (`1` FSJb…) or prior rejects.  
Suggested size: n/a (no buy). Keep ≥0.02 SOL fee buffer; next entry still prefer ~0.08–0.15 SOL when a clean passer appears.
