# GX Chain Overview

GX Chain is a sovereign stablecoin framework designed for the next generation of fiat-backed digital currencies. Rather than operating as a single blockchain, GX functions as a network of independent Layer-1 chains, each issuing a local sovereign stablecoin pegged 1:1 to its respective fiat currency. 

**Key Features**
* **Sovereign Chains:** Dedicated PoA blockchains for each supported currency (e.g., GXUSD, GXKRW).
* **Jurisdictional Compliance:** Validators are licensed, regulated entities operating within their respective local legal frameworks.
* **Live Proof-of-Reserves:** 24/7 on-chain reserve scanner tied to regulated custodial accounts.
* **IBC Interoperability:** Atomic cross-chain transfers to the Gurufin Chain.

**Fees & Gas**
Gas is paid in the local GX stablecoin, with transaction fees denominated and fixed in local fiat terms within narrow bands (e.g., ~$0.01 per B2B transaction). This ensures predictable B2B usability.

**Offline Payments**
For intermittent-connectivity environments, GX supports an offline mode for low-frequency B2B flows using secure hardware attestations, reconciled to the chain when connectivity returns. This feature is currently available for internal testing only and is not yet enabled on the public testnet.

**Performance Targets**
* **Finality:** Sub-second consensus on-chain (~500ms target, measured under controlled conditions).
* **Throughput:** 10,000+ TPS target on commodity hardware (designed capacity, subject to mainnet validation).
* **Uptime:** 99.97% uptime target.

> **Note:** The above figures represent design targets achieved during internal testing. Actual mainnet performance may vary based on network load, validator distribution, and hardware configuration.
