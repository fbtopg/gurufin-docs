# Hybrid Pools

Hybrid Pools are GuruDex's core innovation—a unified liquidity architecture that combines institutional and retail liquidity within a single pool per stablecoin. This design maximizes depth and capital efficiency while maintaining internal separation for privacy and compliance.

---

**Single Pool per Currency**

GuruDex creates one pool per stablecoin (e.g., USGX pool, KRGX pool) rather than separate pools for each trading pair. For N currencies, this requires only N pools instead of N×(N-1)/2, reducing operational complexity by approximately 66% and concentrating all liquidity for minimal slippage.

---

**Dual Pricing Mechanisms**

Each pool supports two execution algorithms:

* **Retail Segment (AMM)** — Uses a constant product formula (x × y = k) with dynamic fees that increase as the pool becomes imbalanced, incentivizing arbitrageurs to restore equilibrium.
* **Institutional Segment (Oracle)** — Uses real-time FX rates from the PriceOracle with fixed low fees (~0.1%), enabling large trades at precise market prices.

---

**Internal Separation**

While liquidity is shared for maximum depth, institutional and retail balances are tracked separately at the smart contract level. This preserves privacy for institutional trades, enables differentiated fee structures, and supports wallet-tier compliance without exposing sensitive trading data.

---

*This page provides an introductory overview.*
