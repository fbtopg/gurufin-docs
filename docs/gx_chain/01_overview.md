# GX Chain Overview

GX Chain is a sovereign stablecoin framework designed for the next generation of fiat-backed digital currencies. Rather than operating as a single blockchain, GX functions as a network of independent Layer-1 chains, each issuing a local sovereign stablecoin pegged 1:1 to its respective fiat currency. 

**Key Features**
* **Sovereign Chains:** Dedicated PoA blockchains for each supported currency (e.g., GXUSD, GXKRW).
* **Jurisdictional Compliance:** Validators are licensed, regulated entities operating within their respective local legal frameworks.
* **Live Proof-of-Reserves:** 24/7 on-chain reserve scanner tied to regulated custodial accounts.
* **IBC Interoperability:** Atomic cross-chain transfers to the Gurufin Chain.

**Fees & Gas**
Gas is paid in the local GX stablecoin, with transaction fees denominated and fixed in local fiat terms within narrow bands (e.g., ~$0.01 per retail transaction). This ensures predictable point-of-sale usability.

**Offline Payments**
For intermittent-connectivity environments, GX supports an offline mode for low-value flows using secure hardware attestations, reconciled to the chain when connectivity returns.

**Performance Benchmarks**
* **Finality:** <1 second (~500ms achieved).
* **Throughput:** 10,000+ TPS on commodity hardware.
* **Uptime:** 99.97%.
