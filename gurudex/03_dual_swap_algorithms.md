# Dual Swap Algorithms

The Gurufin Chain’s FXSwap platform employs a sophisticated dual swap algorithm architecture designed to optimally serve both retail users and institutional participants. This hybrid approach leverages the strengths of Automated Market Maker (AMM) models for retail trades and real-time oracle-driven pricing for institutions, ensuring efficient, low-slippage swaps across a global stablecoin ecosystem. This page provides a comprehensive overview of the dual swap algorithms, detailing their mechanisms, routing, execution flows, and comparative characteristics.

---

## Overview of Dual Swap Algorithms

The FXSwap system integrates two distinct swap algorithms within a unified liquidity pool architecture:

- **Retail Swaps:** Utilize a Uniswap v3 style AMM model optimized for smaller, frequent trades by retail users.
- **Institutional Swaps:** Employ real-time oracle pricing with Request-for-Quote (RFQ) style execution tailored for large-volume, low-slippage institutional transactions.

This duality enables the platform to balance liquidity depth, price accuracy, and fee efficiency, while maintaining a single pool per stablecoin pair that consolidates liquidity from both user segments.

---

## Automated Market Maker (AMM) for Retail Users

### Design and Mechanism

Retail swaps on FXSwap are powered by an AMM algorithm inspired by Uniswap v3’s concentrated liquidity model. The AMM operates on the constant product formula:

\[
x \times y = k
\]

where \(x\) and \(y\) represent the reserves of the base and quote stablecoins respectively, and \(k\) is a constant.

Key features include:

- **Dynamic Fee Model:** Fees adjust based on pool imbalance to incentivize rebalancing and protect liquidity providers from adverse selection. The fee increases by 1% for every 1% deviation from the ideal 1:1 reserve ratio.
- **Concentrated Liquidity:** Liquidity providers can allocate capital within specific price ranges, enhancing capital efficiency and reducing slippage.
- **Slippage Protection:** Minimum output amounts (`minAmountOut`) are enforced to protect users from excessive price impact.

### Retail Swap Execution Flow

1. The retail user initiates a swap by calling the `swap` function with parameters indicating direction (`isBaseToQuote`), input amount, and minimum acceptable output.
2. The system verifies the user’s retail status and rate limits.
3. The AMM calculates the output amount using the constant product formula after deducting dynamic fees.
4. Reserves are updated to reflect the swap.
5. The output amount is transferred to the user.
6. Fees are accumulated for liquidity provider rewards.

This process ensures a seamless, permissionless trading experience with predictable fee structures and efficient liquidity utilization.

---

## Real-Time Oracle Pricing for Institutional Users

### Design and Mechanism

Institutional swaps leverage a real-time price oracle network that aggregates vetted exchange rate data from permissioned providers. This oracle-driven model supports RFQ-style swaps characterized by:

- **Price Validation:** Incoming swap requests include an oracle price that is validated against stored rates, ensuring deviation and data freshness constraints (e.g., max 5-minute age, max 5% deviation).
- **Custom Fee Rates:** Institutions benefit from lower, negotiated fees (typically around 0.1%) reflecting their trade volume and risk profile.
- **Transaction and Volume Limits:** Strict per-transaction and daily volume limits are enforced to manage risk and compliance.
- **Pre-Trade Verification:** Institutional users undergo KYC/AML verification and onboarding via a dedicated registry with role-based permissions.

### Institutional Swap Execution Flow

1. The institution submits a swap request including the oracle price.
2. The system confirms institutional status and validates the oracle price within allowed deviation and age parameters.
3. Transaction limits and daily volume caps are checked.
4. The swap amount out is computed by multiplying the input amount by the validated oracle price.
5. Reserves are updated accordingly.
6. The output amount is transferred to the institution.
7. The institution’s trade volume is recorded for limit enforcement.

This approach minimizes slippage and provides institutions with predictable execution aligned with real-world FX rates.

---

## Swap Routing and Execution Architecture

FXSwap’s hybrid liquidity pool architecture supports both algorithms within a single pool per stablecoin pair. Internally, the pool maintains separate accounting for retail and institutional liquidity segments, preserving privacy and operational efficiency.

The routing logic distinguishes user types at swap initiation:

- **Retail users** are routed to the AMM engine, which calculates output based on pool reserves and dynamic fees.
- **Institutional users** are routed to the oracle pricing engine, which applies real-time exchange rates and enforces institutional parameters.

This unified yet segmented design maximizes liquidity utilization, reduces operational overhead, and simplifies pool management.

---

## Comparative Analysis of Retail AMM vs. Institutional Oracle Pricing

| Feature                     | Retail AMM (Uniswap v3 Style)                   | Institutional Oracle Pricing (RFQ)           |
|-----------------------------|------------------------------------------------|----------------------------------------------|
| **User Segment**             | Retail and small traders                        | Institutional and large-volume traders       |
| **Pricing Model**            | Constant product formula \(x \times y = k\)    | Real-time oracle price feed                   |
| **Fee Structure**            | Dynamic fees based on pool imbalance            | Fixed/custom low fees (e.g., 0.1%)            |
| **Slippage**                | Variable, dependent on liquidity and trade size | Minimal, price locked to oracle rate          |
| **Liquidity Pools**          | Single hybrid pool with concentrated liquidity | Same hybrid pool, separate institutional accounting |
| **Trade Limits**             | Rate limits per transaction and hourly volume   | Strict per-transaction and daily volume limits |
| **Price Validation**         | On-chain AMM math, no external price input      | Oracle price validation with deviation and freshness checks |
| **Execution Speed**          | Instantaneous on-chain swap                      | Instantaneous with pre-verified oracle data   |
| **User Onboarding**          | Permissionless                                  | KYC/AML verified via institutional registry  |
| **Risk Management**          | Dynamic fees incentivize pool balance           | Volume and deviation limits enforce risk controls |
| **Use Cases**                | Retail remittances, small FX trades              | Institutional FX trading, large cross-border settlements |

---

## Summary

The dual swap algorithm framework of FXSwap on Gurufin Chain represents a cutting-edge solution for stablecoin FX trading, harmonizing the needs of diverse market participants. Retail users enjoy the flexibility and accessibility of a Uniswap v3 style AMM with dynamic fees and concentrated liquidity, while institutions benefit from real-time, oracle-backed pricing with robust compliance and risk controls.

This hybrid model, supported by a single, integrated liquidity pool per stablecoin pair, delivers deep liquidity, efficient capital utilization, and predictable execution quality. It positions Gurufin Chain as a neutral, scalable FX and DeFi hub for the Web3 economy, bridging retail accessibility with institutional-grade performance.

---

## References

- Gurufin Chain Technical Stack and Features
- FXSwap Architecture Documentation
- GX Stablecoin Chain Overview
- Oracle Network and Hybrid Execution Fabric Details