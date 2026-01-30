# GX Overview

GX Chain is a sovereign stablecoin framework designed to support the next generation of fiat-backed digital currencies. Rather than operating as a single blockchain, GX Chain functions as a network of independent Layer-1 chains, each issuing a local sovereign stablecoin pegged 1:1 to its respective fiat currency. This architecture enables regulatory compliance, transparency, and operational efficiency tailored to each jurisdiction's legal and financial frameworks.

At the core of GX Chain is a permissioned Proof-of-Authority (PoA) consensus mechanism, where licensed and regulated validators operate the network nodes. This governance model ensures that only authorized entities participate in block validation, reinforcing trust and compliance with jurisdictional requirements. The chains leverage the Cosmos SDK and Tendermint BFT technology to provide fast, secure, and interoperable blockchain infrastructure.

---

**Multi-Currency Stablecoin Engine**

GX Chain supports multiple fiat currencies through its sovereign chain architecture. Each currency operates on its own dedicated chain with jurisdiction-specific validators, enabling regulatory compliance while maintaining interoperability with the broader Gurufin ecosystem.

The stablecoins are fully backed by fiat reserves held in regulated custodial accounts, with live proof-of-reserves available 24/7 to ensure transparency and trust. Automated minting and burning are anchored directly to bank API events, ensuring that the digital supply always corresponds to real-world fiat reserves.

---

**Jurisdictional Model**

Each GX chain is an independent Layer-1 blockchain governed by licensed validators who are regulated entities within the respective jurisdiction. This model ensures that stablecoin issuance, reserve management, and transactional compliance adhere to local laws and supervisory requirements.

By decentralizing issuance across sovereign chains, the GX network mitigates risks associated with centralized stablecoin providers and enhances regulatory transparency. Validators are bound by legal agreements and compliance obligations, and the network enforces wallet-tier compliance at the consensus layer. This architecture supports supervisory-grade observability and auditability, making GX stablecoins suitable for institutional and government use cases.

---

**Proof-of-Authority Consensus**

The GX chains utilize a permissioned Proof-of-Authority consensus mechanism implemented via Cosmos SDK and Tendermint BFT. PoA consensus relies on pre-approved, licensed validators authorized to produce blocks and validate transactions.

This approach offers regulatory compliance through vetted and licensed validators, high performance with sub-second confirmations and five-figure TPS on commodity hardware (consistent with CBDC pilot benchmarks), security through known and accountable validator identities, and governance control reflecting local regulatory requirements. The PoA model is complemented by interoperability protocols such as IBC and EVM compatibility, enabling GX stablecoins to interact seamlessly with other blockchains and DeFi ecosystems.

---

**Fees and Gas Model**

Gas is paid in the local GX stablecoin, with transaction fees denominated and fixed in fiat terms within narrow bands (e.g., ~$0.013 per transaction). Unlike congestion-auction fee models on public chains, GX's fixed-fee design ensures predictable point-of-sale usability. Fees may be optionally indexed to CPI for long-run sustainability. Paymaster contracts allow institutions to sponsor end-user fees during early adoption.

---

**Offline Payments**

For intermittent-connectivity environments, GX supports an offline mode for low-value flows. Value transfers are recorded locally with secure hardware attestations, policy caps, and time-bounded validity, then reconciled to the chain when connectivity returns. Double-spend controls include spend limits, rolling counters, and post-reconciliation checks.
