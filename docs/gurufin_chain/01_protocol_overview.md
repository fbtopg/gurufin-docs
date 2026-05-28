# Protocol Overview

Gurufin Chain is a public Delegated Proof-of-Stake (DPoS) Layer-1 blockchain built on Cosmos SDK and CometBFT. It serves as a high-performance, neutral settlement hub for cross-border payments and DeFi activities.

**Key Characteristics**

* **Fast finality** — Sub-second block times with deterministic consensus, ensuring transactions are confirmed almost instantly.
* **High throughput** — Up to 10,000 TPS capacity, designed for enterprise-grade transaction volumes.
* **Low cost** — Minimal gas fees make micro-transfers and frequent settlements practical.
* **Neutral routing layer** — Connects sovereign stablecoin networks (like the GX Stablecoin network) and external liquidity hubs without requiring protocol-level AMMs or native stablecoin issuance.

**Consensus**

Gurufin Chain uses **Tendermint BFT** combined with **DPoS**. Validators stake GXN to participate in block production, and token holders delegate their tokens to vote for trusted validators. This model guarantees immediate, deterministic finality while remaining resistant to Byzantine faults.

**Protocol Role**

Within the Gurufin ecosystem, Gurufin Chain acts as the central settlement rail. Stablecoins are minted and managed on dedicated sovereign chains (GX Stablecoin network) and settle across Gurufin Chain via IBC for trading, FX, and DeFi use cases. The protocol focuses on fast, secure, and compliant value transfer — leaving complex financial logic to the ecosystem chains that plug into it.
