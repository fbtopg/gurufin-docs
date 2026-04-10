# 04 Multi Currency Support (Cross-Chain Interoperability)

The "04 Multi Currency Support (Cross-Chain Interoperability)" module details how the GX Chain architecture facilitates the management and exchange of stablecoins across various jurisdictions and currencies. Instead of operating a single monolithic chain for all stablecoins, this module outlines a design where each supported currency runs on its own independent Layer-1 blockchain, adhering to specific jurisdictional governance and compliance requirements. This approach positions GX Chain as a global Foreign Exchange (FX) and settlement hub while respecting diverse regulatory landscapes.

## Core Concepts

### Multi-Currency Support
The fundamental principle of this module. GX Chain's design natively supports multiple stablecoins, each representing a different fiat currency. This is achieved through a decentralized model where individual stablecoins are issued and managed on their own sovereign chains.

### Jurisdictional Sovereignty
A cornerstone of the multi-currency support model. Each GX stablecoin chain functions as an independent blockchain, governed by licensed validators that are regulated entities within their respective jurisdictions. This ensures that stablecoin issuance, reserve management, and transactional compliance strictly adhere to local laws and supervisory requirements. This model offers several benefits:
*   **Legal Clarity:** Validators operate under local laws with defined accountability.
*   **Regulatory Alignment:** Each chain can implement jurisdiction-specific compliance rules.
*   **Local Banking Integration:** Facilitated through partnerships with local custodian banks and payment providers.
*   **Operational Independence:** Isolates issues to prevent impacts across stablecoins in different jurisdictions.

### Cross-Chain Interoperability
While stablecoin chains operate independently, they are interconnected through **IBC (Inter-Blockchain Communication)**. This critical technology enables seamless interaction and exchange between different sovereign stablecoin chains, allowing for efficient multi-currency transactions and FX operations without compromising the jurisdictional sovereignty of individual stablecoins.

### FX Settlement and PvP (Payment-versus-Payment)
The multi-currency architecture and cross-chain interoperability are specifically designed to enable robust Foreign Exchange (FX) settlement. The system aims to facilitate **Payment-versus-Payment (PvP)** mechanisms, ensuring that both legs of a currency exchange are settled simultaneously, thereby mitigating settlement risk.

### Onboarding New Currencies
The modular and sovereign chain design provides a clear framework for **Onboarding New Currencies**. As new jurisdictions or currencies are introduced, new dedicated Layer-1 chains can be deployed, each with its own specific governance and regulatory compliance mechanisms.

### Low-Curvature Stable-Swap Curves
While not explicitly detailed in the provided excerpt's direct application, the mention of "low-curvature stable-swap curves" indicates an underlying mechanism for efficient and low-slippage exchange between stablecoins. This is crucial for maintaining tight spreads and providing a good user experience in multi-currency transactions, especially within the context of FX settlement.

## Relationships

The concepts within this module are tightly intertwined:

*   **Multi-Currency Support** is the overarching goal, achieved through the implementation of dedicated chains grounded in **Jurisdictional Sovereignty**.
*   These independent, sovereign chains are tied together by **Cross-Chain Interoperability** (via IBC), which is essential for enabling global **FX Settlement and PvP**.
*   The architecture inherently supports **Onboarding New Currencies** by creating new sovereign chains.
*   Efficient exchange between these different stablecoins will likely leverage mechanisms like **low-curvature stable-swap curves** to optimize trades.