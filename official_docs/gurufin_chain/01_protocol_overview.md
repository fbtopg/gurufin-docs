# Protocol Overview

Gurufin Chain is a public Delegated Proof-of-Stake (DPoS) Layer-1 blockchain built with Cosmos SDK and CometBFT. It is designed to serve as the settlement and coordination layer for cross-border payments, FX execution, and institutional DeFi activity.

**Key Characteristics**

* **Deterministic finality** - Targets sub-second single-chain finality through CometBFT consensus.
* **High-throughput design** - Designed for up to 10,000 TPS under controlled benchmark conditions. Published benchmark results are expected with mainnet readiness materials.
* **Predictable fee model** - Guru-PEG adjusts GXN-denominated gas fees around fiat-indexed cost targets.
* **Neutral settlement layer** - Connects jurisdiction-specific stablecoin networks, including the GX Stablecoin Network, without requiring Gurufin Chain itself to issue fiat stablecoins.

**Consensus**

Gurufin Chain combines **Tendermint/CometBFT consensus** with **DPoS validator selection**. Validators stake GXN to participate in block production, while delegated stakeholders assign voting power to selected validators. This model provides deterministic finality and Byzantine fault tolerance when validator behavior remains within consensus safety assumptions.

## Settlement Finality

* **Single-chain finality:** Approximately 500ms target finality under controlled conditions.
* **Cross-chain settlement through IBC:** Typically 3-10 seconds end to end, depending on relayer performance and the specific chain pair. Cross-chain settlement can remain deterministic while still including packet relay overhead.

**Protocol Role**

Within the Gurufin ecosystem, Gurufin Chain acts as the central settlement rail. GX stablecoins are minted and managed on dedicated jurisdiction-specific chains, then transferred to Gurufin Chain via IBC for FX execution and DeFi use cases. The protocol focuses on settlement, interoperability, and transparent network rules while specialized issuance, reserve, and compliance logic remain on connected ecosystem chains and applications.
