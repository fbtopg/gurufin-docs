# 02 Reserve And Backing (24/7 Live Proof-of-Reserves)

This module outlines the fundamental principles and mechanisms ensuring the integrity and stability of GX stablecoins. It details the robust reserve and backing framework designed to maintain a stablecoin's 1:1 peg to fiat currency, guaranteeing holders can redeem their tokens at any time.

## Key Concepts

The stability of GX stablecoins is built upon several critical concepts:

### 24/7 Live Proof-of-Reserves

A core tenet of the GX stablecoin system is **24/7 Live Proof-of-Reserves**. This mechanism ensures continuous, real-time verification that every stablecoin in circulation is fully collateralized by fiat currency held in reserve. This transparency builds trust and provides ongoing assurance of the stablecoin's backing. Automated minting and burning mechanisms, integrated with licensed banking partners via secure APIs, are crucial for enforcing this 1:1 fiat backing. Token issuance only occurs upon verified receipt of fiat funds, and redemption triggers the corresponding fiat transfer, maintaining continuous parity between tokens in circulation and fiat reserves.

### Reserve Composition

The **Reserve Composition** dictates the types of assets held in the reserve to back the stablecoins. The primary objective is to maintain capital preservation and immediate liquidity.

- **At launch, 100% of reserves are maintained in cash:** This is a crucial starting point for GX stablecoins. To ensure immediate redemption capacity, all reserve assets are initially held as cash at licensed custodian banks. Binding concentration limits are applied to these holdings to diversify risk.
- **Capped fraction:** Over time, and only where expressly permitted by domestic regulation, a **capped fraction** of the reserve may be allocated to ultra-short Treasury bills. These are typically under 3 months maturity and are managed on a roll-down ladder strategy, balancing liquidity with modest yield. This diversification is strictly limited and regulated.

### Liquidity Standards

Maintaining high **Liquidity Standards** is paramount to ensuring that stablecoin holders can always redeem their tokens for fiat currency without delay. This includes:

- **Pre-arranged repo facilities—not secondary-market sales:** To ensure immediate liquidity against any securities held in the reserve (such as ultra-short Treasury bills), GX relies on **pre-arranged repo facilities**. This means that agreements are in place beforehand to quickly and efficiently convert these securities into cash if needed, rather than relying on potentially less liquid secondary-market sales which could introduce price volatility or delays.

## Important Details from Source Excerpts

*   Every stablecoin issued is fully collateralized by fiat currency at a 1:1 ratio.
*   The strict backing model underpins price stability and trustworthiness.
*   Redemption for fiat currency is guaranteed at any time without risk of shortfall.
*   Token issuance occurs only upon verified receipt of fiat funds.
*   Redemption triggers the corresponding fiat transfer.
*   Reserve composition may differ by jurisdiction based on local regulatory requirements and banking partner capabilities.