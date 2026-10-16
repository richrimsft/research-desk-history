# Pump.fun scout scan — 19:31 ET Oct 15 2026

**Recommendation: HOLD** — no clean rotate target that clearly beats current holdings.

## Holdings snapshot (refreshed ~19:34 ET)

| Coin | MC | vs entry | Value | m5 | h1 | m5 b/s | h1 b/s | Liq |
|------|-----|----------|-------|----|----|--------|--------|-----|
| SPOOKY | $192,126 | -42.6% | $4.50 | -6.5% | +15.4% | 13/17 | 747/448 | $40,267 |
| SYCAMORE | $329,221 | +9.7% | $6.76 | +1.2% | +10.8% | 17/11 | 256/184 | $54,863 |
| NULLCASH | $35,893 | +48.3% | $5.97 | -4.5% | +76.5% | 43/45 | 256/156 | $0 |

- SOL left: ~0.00766 (~$0.81)
- **Est total portfolio: ~$18.04**

### Holdings notes
- **SPOOKY** (~$192k, −43%): softest. m5 sells>buys; h1 still +15% with buys>sells. Dump rule (~$180k + h1 neg + sells≥buys) **not met** — watch only.
- **SYCAMORE** (~$329k, +10%): stable, buys>sells on m5 and h1. Hold.
- **NULLCASH** (~$36k, +48%): still strong h1 (+76%). Liq shows $0 on Dex (bonding-curve / pumpfun pair). Past +20% — would rotate only into a *clean* replacement; none found this scan.

## Scan coverage

- Unique `*pump` mints collected (boosts/profiles/searches/pump.fun API): **219** (+ refresh batch)
- Mints with DexScreener pair data scored: **197**
- Sources: DexScreener token-boosts latest/top, token-profiles latest, searches (solana pump, pump.fun, meme solana, pumpswap, new pump, trending, etc.), frontend-api-v3.pump.fun coin lists

## Numeric passers (all filters)

| Symbol | Mint | MC | Liq | Age | h1 | m5 | h1 b/s | m5 b/s |
|--------|------|----|----|-----|----|----|--------|--------|
| APU | `E7eCZS2cq655qJ7uVx3dSHR2zK31kwNQsWS6P6Hpump` | $105k | $26.6k | 232.0h | +22.0% | +23.5% | 49/31 | 45/27 |
| EGO | `BbJJUTuGV2B7tJ99YeryiCBFLG39Hoc4RTzEwchtpump` | $71k | $29.6k | 270.8h | +65.3% | -5.8% | 348/229 | 0/4 |

## RugCheck results

### EGO (`BbJJUTuGV2B7tJ99YeryiCBFLG39Hoc4RTzEwchtpump`)
- Score: 1 | rugged: False
- Mint revoked: True | Freeze revoked: True
- Top10 ex-LP: **25.4%** (ideal <40%)
- graphInsidersDetected: **64** | insiderNetworks: 9
- totalHolders: 13949 | market liq (RC): $31,945

### APU (`E7eCZS2cq655qJ7uVx3dSHR2zK31kwNQsWS6P6Hpump`)
- Score: 1 | rugged: False
- Mint revoked: True | Freeze revoked: True
- Top10 ex-LP: **30.1%** (ideal <40%)
- graphInsidersDetected: **54** | insiderNetworks: 2
- totalHolders: 2311 | market liq (RC): $25,164

### Chinese (`Tm2iqbxYjKpW8xCMe6q1xUraNMNzcG5xMztAir3pump`)
- Score: 1 | rugged: False
- Mint revoked: True | Freeze revoked: True
- Top10 ex-LP: **25.6%** (ideal <40%)
- graphInsidersDetected: **7** | insiderNetworks: 1
- totalHolders: 4725 | market liq (RC): $43,176

## Qualitative verdict on passers

- **EGO**: numeric OK, but **64 graph insiders / 9 networks** — same “many flagged insiders” failure mode as prior rejects (e.g. DacityCoin ~63). Also m5 buys < sells. **Reject as rotate.**
- **APU**: numeric OK (m5 strong), top10 ex-LP ~30% OK, but **54 graph insiders** (one net size 47). **Reject as rotate.**
- **Chinese** (near): RugCheck cleaner (7 insiders, top10 ex-LP ~26%), but h1 only +14% (< +20% filter). Not a passer.

## Known rejects re-checked (not re-recommended)
- KWIF: botty (4k+ h1 buys) + known reject
- STREAM / DacityCoin / CRS / 250 / BACKED: still fail filters / known rejects
- Age<1h heat (XBAY, Motion, MCP): excluded by age rule

## Clear action recommendation

### **HOLD**

- Do **not** rotate NULLCASH → EGO/APU (insider-network risk; do not clearly beat NULLCASH’s own +76% h1 momentum).
- Do **not** dump SPOOKY yet (mc ~$192k > $180k line; h1 still positive; h1 buys>sells).
- Keep SYCAMORE.
- Any buy still needs a sell first (SOL dust only).

Scout only — no trades executed.