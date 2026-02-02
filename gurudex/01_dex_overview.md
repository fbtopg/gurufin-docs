# DEX Overview

GuruDex is an FX-specialized decentralized exchange designed for seamless swaps between sovereign stablecoins on Gurufin Chain. Unlike general-purpose DEXs, GuruDex is purpose-built for foreign exchange use cases, serving both retail users and institutional participants within a unified platform.

---

**Dual-Algorithm Execution**

GuruDex employs two distinct swap algorithms tailored to different user types. Retail users trade via an AMM (Automated Market Maker) with dynamic fees that adjust based on pool conditions. Institutional users access oracle-based pricing with fixed low fees, enabling large trades at precise real-time FX rates with minimal slippage.

---

**Unified Hybrid Pools**

Rather than fragmenting liquidity across multiple pair pools, GuruDex consolidates institutional and retail liquidity into single hybrid pools per stablecoin. This design maximizes capital efficiency, reduces slippage, and simplifies operations—requiring only N pools for N currencies instead of N×(N-1)/2.

---

**Core Smart Contracts**

The platform is powered by four key contracts: **FXSwapMaster** (central orchestration and governance), **HybridStablePool** (liquidity storage and swap execution), **PriceOracle** (real-time FX rate validation), and **InstitutionalRegistry** (KYC/AML and institutional onboarding). Together, they provide regulatory-grade controls and compliance integration.

---

*This page provides an introductory overview.*
