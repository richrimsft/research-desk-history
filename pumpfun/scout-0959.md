# Scout 0959 — 2026-10-16 09:59 ET

Wallet **0.29760554 SOL** (~$31.44 at SOL $105.63). SPL USDC dust only; Token-2022 none. **No meme positions.**

## Pipeline
- Refreshed Dexscreener boosts latest/top + profiles + CTOs → `lists.txt`
- `pf-live-0959.json` (50)
- `scan0959.py` → 145 mints / 79 cands (`scan-0959.out` / `cands-0959.json`)
- `expand0959.py` → 655 mints / 575 pairs → **5** strict in-window, **0** NEW, **7** young

## In-window (0.5–4h, mc≥$10k, h1>0, pumpfun/pumpswap)
- **PRIOR** Audaster `3xmzHi86…` mc~$1,608,001 age 0.51h h1 2672 m5 80.53 pumpswap
- **PRIOR** ETR `BALftXRK…` mc~$257,949 age 0.58h h1 485 m5 -23.8 pumpswap
- **PRIOR** OPTIMA `DdVXE425…` mc~$153,816 age 2.6h h1 33.75 m5 -6.83 pumpswap
- **PRIOR** RIBBIT `78ZBbCJk…` mc~$58,943 age 0.65h h1 35.42 m5 72.17 pumpswap
- **PRIOR** INU `5xri1bAx…` mc~$12,412 age 0.65h h1 162 m5 57.33 pumpfun

## Autopsy (aged-into-window recheck + young pre-screen)
- **Audaster** [inwindow_recheck] **FAIL**: creatorBal 0 (dev sold out early)
- **BFRG** [too_young] **FAIL**: age 0.37h <30m — no-buy by narrative-age; RC Low Liquidity (score 2884); creatorBal 0 (dev sold out early); 19× 1–5% holder band
- **ETR** [inwindow_recheck] **FAIL**: top10ex 26.7% elevated >25%; 9× tight 2.0–2.2% sniper band; 18× 1–5% holder band
- **INU** [inwindow_recheck] **FAIL**: creatorBal 0 (dev sold out early); 19× 1–5% holder band
- **Konasu** [too_young] **FAIL**: age 0.37h <30m — no-buy by narrative-age; creatorBal 0 (dev sold out early); 16× 1–5% holder band
- **OPTIMA** [inwindow_recheck] **FAIL**: top10ex 37.1%>30%; 16× 1–5% holder band
- **RIBBIT** [inwindow_recheck] **FAIL**: creatorBal 0 (dev sold out early); 15× 1–5% holder band
- **SKILL** [too_young] **FAIL**: age 0.2h <30m — no-buy by narrative-age; creatorBal 0 (dev sold out early); 18× 1–5% holder band
- **Scud** [too_young] **FAIL**: age 0.29h <30m — no-buy by narrative-age; RC Low Liquidity (score 2864); creatorBal 0 (dev sold out early)
- **Twin** [too_young] **FAIL**: age 0.39h <30m — no-buy by narrative-age; creatorBal 0 (dev sold out early); top10ex 31.0%>30%; 19× 1–5% holder band
- **UMBRA** [too_young] **FAIL**: age 0.36h <30m — no-buy by narrative-age; RC Copycat; top10ex 28.8% elevated >25%; 18× 1–5% holder band
- **catJAM** [too_young] **FAIL**: age 0.26h <30m — no-buy by narrative-age; RC Low Liquidity (score 2699); creatorBal 0 (dev sold out early); 19× 1–5% holder band

## Devil's advocate
No coin clears structural bars. Audaster/RIBBIT/INU creatorBal=0; ETR still shows ~9× 2.0–2.2% sniper band + top10ex~27%; OPTIMA top10ex~37% + bands. Momentum (Audaster m5 +80, RIBBIT +72, INU +57) does not fix sold-out creator / sniper bands. Would not put most of the SOL into any of these.

## Decision
**Action: none — stay in SOL.** 0 autopsy-clean buys.
