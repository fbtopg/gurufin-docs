# Protocol Overview

The "Protocol Overview" module provides a foundational understanding of the Gurufin ecosystem, primarily focusing on the Gurufin Chain—a purpose-built Layer-1 blockchain designed for global on-chain foreign exchange (FX) and decentralized finance (DeFi). This overview highlights the core architecture, capabilities, and underlying principles that make Gurufin a specialized financial infrastructure for the Web3 economy.

## What is Gurufin Chain?

Gurufin Chain is a public, permissionless Layer-1 blockchain built on the Cosmos SDK and utilizes Tendermint BFT consensus. Unlike general-purpose blockchains, it is specifically optimized for stablecoins, tokenized assets, and cross-border payments. It acts as a neutral FX/DeFi settlement hub where cross-border payments and trading can occur efficiently and securely.

The chain addresses critical challenges in blockchain adoption for traditional finance, including:
*   Unpredictable transaction fees
*   Cross-chain fragmentation
*   Regulatory uncertainty

Through its innovative Guru-PEG mechanism, IBC-first architecture, and built-in compliance modules, Gurufin Chain aims to provide a reliable foundation for institutions and retail users to engage with Web3 finance.

## Key Features and Concepts

### High Performance
Gurufin Chain is engineered for high performance, boasting sub-second finality and a throughput of up to 10,000 transactions per second (TPS). This deterministic finality, which contrasts with probabilistic consensus mechanisms requiring multiple confirmations, is crucial for financial applications where settlement certainty is paramount.

### Interoperability
Interoperability is a cornerstone of Gurufin Chain's design, achieved through a three-layered approach:
*   **Native Cosmos IBC:** For trust-minimized communication with other Cosmos-based blockchains.
*   **EVM Gateway:** Provides compatibility with the Ethereum ecosystem.
*   **GatewayGX module:** Extends connectivity to non-standard chains, such as Solana.

This comprehensive approach ensures the chain can connect multiple blockchain ecosystems, facilitating a fluid movement of assets and data across diverse environments.

### Financial Infrastructure
Gurufin Chain is explicitly built for financial use cases, supporting features like Oracle Priced Reserves. It forms one of the two interconnected pillars of the Gurufin ecosystem, the other being the GX Stablecoin Network. Together, these components create a complete system where GX Stablecoins are minted from fiat deposits, utilized on Gurufin Chain for trading and DeFi, and can be redeemed back to fiat seamlessly.

### Native Token (GXN)
The Gurufin Chain utilizes GXN as its native token. GXN serves multiple functions within the ecosystem, including:
*   Staking
*   Governance
*   Payment of fees via the Guru-PEG mechanism

## Relationship to Other Concepts

The "Protocol Overview" is intrinsically linked to several other core concepts within the Gurufin documentation:

*   **Financial Infrastructure:** The Gurufin Chain itself is presented as a specialized financial infrastructure, contrasting it with general-purpose blockchains.
*   **Technology Stack:** The overview details core components of the Gurufin Chain's technology stack, such as Cosmos SDK, Tendermint BFT, IBC, and the EVM Gateway.
*   **What Makes Gurufin Different:** The challenges Gurufin Chain aims to solve (unpredictable fees, fragmentation, regulatory uncertainty) directly contribute to its unique value proposition and differentiate it within the blockchain landscape.

For a deeper dive into the technical details of GXN, the Guru-PEG mechanism, or the GX Stablecoin Network, refer to the respective documentation sections.