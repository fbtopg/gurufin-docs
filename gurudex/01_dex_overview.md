# DEX Overview

GuruDex is an FX-specialized decentralized exchange designed for seamless swaps between sovereign stablecoins on Gurufin Chain. Unlike general-purpose DEXs that rely on Automated Market Makers (AMMs), GuruDex uses an **Oracle Priced Reserve Swap (OPRS)** architecture purpose-built for on-chain stablecoin FX trading.

---

**Why OPRS, Not AMM?**

AMMs (Automated Market Makers) are designed for volatile asset pairs where price discovery emerges from trading activity. However, stablecoin FX trading is fundamentally different:

- **GX stablecoins are pegged to individual fiat currencies** — USGX (USD), KRGX (KRW), EURGX (EUR), etc.
- **Each fiat-pegged stablecoin has its own GX Chain L1 mainnet** — separate sovereign chains with jurisdiction-specific validators
- **Prices are determined by real-world FX rates**, not on-chain supply/demand dynamics
- **Swaps happen via IBC (Inter-Blockchain Communication)** — cross-chain atomic settlement between sovereign chains

AMM pools would introduce unnecessary slippage and fail to reflect actual FX rates. OPRS uses oracle-guided pricing with mint/burn mechanics, ensuring swaps execute at precise market rates.

---

**Oracle Priced Reserve Swap (OPRS)**

GuruDex uses a mint-and-burn mechanism guided by oracle FX rates rather than liquidity pool-based pricing:

1. **Oracle Price Feed** — Real-time FX rates from trusted oracles (with triple validation: freshness, deviation, confidence)
2. **Mint/Burn Mechanism** — Instead of swapping tokens in a pool, the system burns the input stablecoin on its native chain and mints the output stablecoin on its destination chain
3. **IBC Settlement** — Cross-chain transfers are atomic via IBC/HTLCs, eliminating counterparty risk
4. **No Slippage** — Trades execute at oracle-verified rates, not pool-dependent prices

---

**Sovereign Chain Architecture**

Each GX stablecoin operates on its own dedicated Layer-1 blockchain:

- **USGX Chain** — USD-pegged stablecoin, US jurisdiction validators
- **KRGX Chain** — KRW-pegged stablecoin, Korea jurisdiction validators
- **EURGX Chain** — EUR-pegged stablecoin, EU jurisdiction validators
- **JPGX Chain** — JPY-pegged stablecoin, Japan jurisdiction validators

GuruDex on Gurufin Chain acts as the FX settlement hub, connecting these sovereign chains via IBC for cross-currency swaps.

---

**Core Smart Contracts**

The platform is powered by four key contracts: **FXSwapMaster** (central orchestration and governance), **OPRSProcessor** (oracle-priced swap execution via mint/burn), **PriceOracle** (real-time FX rate validation), and **InstitutionalRegistry** (KYC/AML and institutional onboarding). Together, they provide regulatory-grade controls and compliance integration.

---
