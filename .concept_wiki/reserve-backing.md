# 02 What Is Gurufin (Reserve & Backing)

This module provides a foundational understanding of Gurufin, focusing specifically on its core components and, most importantly, the robust reserve and backing mechanisms that ensure the stability and trustworthiness of its GX Stablecoins. It outlines how Gurufin combines blockchain efficiency with stringent regulatory compliance to create a specialized financial infrastructure.

## What is Gurufin?
Gurufin is a specialized financial infrastructure that leverages blockchain technology for efficient, stable, and compliant financial operations. It is built upon two interconnected pillars:

*   **Gurufin Chain**: A public, permissionless Layer-1 blockchain built on Cosmos SDK with Tendermint BFT consensus. It acts as a neutral FX/DeFi settlement hub, facilitating cross-border payments and trading. Its native token, GXN, is used for staking, governance, and fee payments via Guru-PEG. It boasts sub-second finality and high throughput (up to 10,000 TPS) with IBC-first interoperability.
*   **GX Stablecoin Network**: A federation of sovereign stablecoin chains, each operating under its own jurisdiction. These chains feature licensed validators governed by Proof-of-Authority (PoA) consensus. GX Stablecoins are fully backed 1:1 by fiat reserves held in regulated custodians, with automated minting and burning facilitated by bank API integration. The system also includes 24/7 live proof-of-reserves attestation to ensure transparency and trust.

Together, these components create a seamless system: GX Stablecoins are minted when users deposit fiat through licensed partners, are then transferred to the Gurufin Chain via IBC for trading and DeFi activities, and can be redeemed back to fiat at any time.

## Reserve & Backing of GX Stablecoins

The integrity and stability of GX Stablecoins are fundamentally underpinned by a rigorous **Reserve & Backing** framework. Each stablecoin issued on a GX chain is fully collateralized by fiat currency held in reserve at a 1:1 ratio. This strict backing model is crucial for maintaining the stablecoin's price stability and ensuring that holders can redeem their tokens for fiat currency without risk of shortfall.

### Key Aspects of Reserve & Backing:
*   **1:1 Fiat Backing**: Every GX stablecoin is backed 1:1 by fiat currency held in reserve.
*   **Automated Minting and Burning**: This 1:1 parity is enforced through automated minting and burning mechanisms. Token issuance occurs only upon the verified receipt of fiat funds via integrations with licensed banking partners' secure APIs. Conversely, redemption triggers the corresponding fiat transfer, ensuring continuous balance between tokens in circulation and fiat reserves.
*   **Reserve Composition**: Reserve assets primarily consist of highly liquid and low-risk instruments to ensure capital preservation and immediate liquidity. While the exact composition may vary by jurisdiction based on local regulatory requirements and banking partnerships, at launch, 100% of reserves are maintained in cash at licensed custodian banks, with binding concentration limits.
*   **Future Reserve Allocation (Capped Fraction)**: In jurisdictions where expressly permitted by domestic regulation, a *capped fraction* of reserves may be allocated to ultra-short Treasury bills (typically under 3 months maturity). These are managed on a roll-down ladder, and liquidity against such securities is raised via pre-arranged repo facilities.
*   **Compliance and Regulation**: The GX Stablecoin Network emphasizes **Compliance**, with each sovereign stablecoin chain operating under its own jurisdiction and adhering to local legal and financial frameworks. Licensed validators enforce a jurisdictional Proof-of-Authority (PoA) consensus.

The **Reserve & Backing** mechanism is a critical component that links directly to the overall definition of **What is Gurufin?** by providing the essential trust and stability for the GX Stablecoin Network, which in turn fuels the Gurufin Chain's DeFi capabilities. This transparent and auditable reserve system is a core differentiator, supporting Gurufin's ambition for institutional adoption.