# Scout 1003 — 2026-10-16 10:03 ET

## Wallet
- RPC **0.29760554 SOL** (`wallet-sol-1003.json`); SPL dust USDC only (6e-06); Token-2022 12 accounts all zero; **no meme positions**.
- SOL ~$105.58. Est. total ~$31.42.

## Pipeline
- DexScreener boosts latest/top + profiles + CTOs (5 sol) + pf-live 50 → `lists.txt`
- `scan1003.py` → 147 mints / 79 cands (`scan-1003.out` / `cands-1003.json`)
- `expand1003.py` → **657 mints / 578 pairs** (`expand-1003.out`)
- Strict in-window (0.5–4h, mc≥10k, h1>0, pumpfun/pumpswap): **5** (NEW 0 / PRIOR 5)
- Young (<30m): **4**
- Autopsy-clean buys: **0**

## In-window
| tag | symbol | mint | mc | age_h | h1 | m5 | dex |
|-----|--------|------|----|-------|----|----|-----|
| PRIOR | Audaster | `3xmzHi86…` | 1435908 | 0.6 | 2376 | -6.65 | pumpswap |
| PRIOR | ETR | `BALftXRK…` | 240111 | 0.67 | 449 | -26.39 | pumpswap |
| PRIOR | RIBBIT | `78ZBbCJk…` | 99592 | 0.74 | 129 | 12.83 | pumpswap |
| PRIOR | Irene | `6N4BHPN8…` | 52380 | 2.68 | 4.32 | None | pumpswap |
| PRIOR | INU | `5xri1bAx…` | 14978 | 0.75 | 217 | 19.65 | pumpfun |

## Young (<30m)
| symbol | mint | mc | age_h | h1 | m5 |
|--------|------|----|-------|----|----|
| UMBRA | `Axbj7Jdz…` | 37180 | 0.45 | 979 | 60.89 |
| Konasu | `93RFugk8…` | 16388 | 0.47 | 311 | 34.87 |
| BFRG | `FMwuYPDg…` | 13936 | 0.47 | 282 | 53.91 |
| Twin | `7Jain9Ef…` | 147533 | 0.48 | 225 | 27.39 |

## Autopsy verdicts
- **Audaster** [inwindow_recheck] **FAIL**: creatorBal 0 (dev sold out early)
  - `rc-Audaster-1003.json` / `autopsy-summary-Audaster-1003.json` (top10ex=3.48, band_1_5=1, creatorBal=0, rc_score=1)
- **ETR** [inwindow_recheck] **FAIL**: 18× 1–5% holder band; 8× tight 1.8–2.0% sniper band
  - `rc-ETR-1003.json` / `autopsy-summary-ETR-1003.json` (top10ex=19.1, band_1_5=18, creatorBal=14849142185973, rc_score=1)
- **RIBBIT** [inwindow_recheck] **FAIL**: creatorBal 0 (dev sold out early); 16× 1–5% holder band; 6× tight 1.1–1.3% sniper band; 9 graph insiders
  - `rc-RIBBIT-1003.json` / `autopsy-summary-RIBBIT-1003.json` (top10ex=18.91, band_1_5=16, creatorBal=0, rc_score=1)
- **Irene** [inwindow_recheck] **FAIL**: creator 42.2%>5%; top10ex 50.74%>30%; 9× identical ~0.9% holdings; RC Low Liquidity
  - `rc-Irene-1003.json` / `autopsy-summary-Irene-1003.json` (top10ex=50.74, band_1_5=0, creatorBal=422156439268901, rc_score=8228)
- **INU** [inwindow_recheck] **FAIL**: creatorBal 0 (dev sold out early); top10ex 27.51% elevated >25%; 18× 1–5% holder band
  - `rc-INU-1003.json` / `autopsy-summary-INU-1003.json` (top10ex=27.51, band_1_5=18, creatorBal=0, rc_score=1)
- **UMBRA** [too_young] **FAIL**: age 0.45h <30m — no-buy by narrative-age; RC Copycat token; top10ex 27.97% elevated >25%; 18× 1–5% holder band; 7× tight 1.2–1.4% sniper band
  - `rc-UMBRA-1003.json` / `autopsy-summary-UMBRA-1003.json` (top10ex=27.97, band_1_5=18, creatorBal=1, rc_score=2001)
- **Konasu** [too_young] **FAIL**: age 0.47h <30m — no-buy by narrative-age; creatorBal 0 (dev sold out early); 19× 1–5% holder band; 5× tight 1.1–1.3% sniper band
  - `rc-Konasu-1003.json` / `autopsy-summary-Konasu-1003.json` (top10ex=19.88, band_1_5=19, creatorBal=0, rc_score=1)
- **BFRG** [too_young] **FAIL**: age 0.47h <30m — no-buy by narrative-age; creatorBal 0 (dev sold out early); top10ex 25.14% elevated >25%; 19× 1–5% holder band; 7× tight 1.1–1.3% sniper band; RC Low Liquidity
  - `rc-BFRG-1003.json` / `autopsy-summary-BFRG-1003.json` (top10ex=25.14, band_1_5=19, creatorBal=0, rc_score=2811)
- **Twin** [too_young] **FAIL**: age 0.48h <30m — no-buy by narrative-age; creatorBal 0 (dev sold out early); 19× 1–5% holder band; 7× tight 1.0–1.2% sniper band; 5 graph insiders
  - `rc-Twin-1003.json` / `autopsy-summary-Twin-1003.json` (top10ex=19.13, band_1_5=19, creatorBal=0, rc_score=1)

## Devil's advocate
No coin clears structural bars. Audaster/RIBBIT/INU/Konasu/BFRG/Twin creatorBal=0; ETR still shows heavy 1–5% + tight sniper bands; Irene creator ~42% + top10ex~51%; UMBRA Copycat + bands. Momentum (RIBBIT m5 +13, INU +20, young UMBRA/Konasu/BFRG/Twin m5 +27–61) does not fix sold-out creator / sniper bands / copycats / whale creator. Would **not** put most of ~0.30 SOL into any of these.

## Decision
**Stay in SOL.** Zero PASS. Kraken watch-only — no proposal.
