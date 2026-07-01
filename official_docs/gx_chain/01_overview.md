# GX Stablecoin Network Overview

The GX Stablecoin Network is a framework for fiat-backed digital currencies. Instead of operating as a single blockchain, GX is structured as a network of independent Layer-1 chains, each issuing a local stablecoin intended to maintain a 1:1 peg with its corresponding fiat currency.

**Key Features**

* **Jurisdiction-specific chains:** Dedicated PoA blockchains for each supported currency, such as GXUSD and GXKRW.
* **Jurisdictional compliance:** Validator participation and operating rules are aligned with local licensing and regulatory requirements.
* **Live proof-of-reserves:** Reserve monitoring connects on-chain supply data with regulated custodial account data.
* **IBC interoperability:** Cross-chain transfers connect GX chains with Gurufin Chain for settlement and FX workflows.

**Fees & Gas**

Gas is paid in the local GX stablecoin. Transaction fees are designed to remain within narrow local fiat cost bands, such as approximately $0.01 per standard B2B transaction, depending on network parameters.

**Offline Payments**

For intermittent-connectivity environments, GX is testing an offline mode for low-frequency B2B flows using secure hardware attestations. Transactions are reconciled to the chain when connectivity returns. This feature is currently available for internal testing only and is not enabled on the public testnet.

**Performance Targets**

* **Finality:** Sub-second on-chain consensus target, with approximately 500ms finality measured under controlled conditions.
* **Throughput:** 10,000+ TPS design target on commodity hardware, subject to public testnet and mainnet validation.
* **Uptime:** 99.97% uptime target for production validator operations.

> **Note:** These figures are design and testing targets. Mainnet performance may vary based on network load, validator distribution, hardware configuration, and operational conditions.
