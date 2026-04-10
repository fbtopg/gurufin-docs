# Compliance & Regulation

GX stablecoins are designed with compliance and regulatory adherence embedded directly into their core infrastructure. This approach ensures that the issuance, transfer, and redemption of sovereign stablecoins operate within the legal frameworks of their respective jurisdictions while maintaining the efficiency and transparency of blockchain technology.

---

**Jurisdictional PoA Model**

At the heart of GX compliance architecture is the permissioned Proof-of-Authority consensus mechanism. Unlike public permissionless blockchains, GX chains operate as independent Layer-1 blockchains, each representing a sovereign stablecoin tied to a specific jurisdiction.

Validators on each GX chain are licensed and regulated entities authorized by the relevant financial authorities within their jurisdiction. These validators are responsible for block validation and consensus participation, ensuring that all on-chain activities comply with local regulatory standards. This model enables jurisdictional control with validators operating under local laws, enhanced security through permissioned participation, and regulatory alignment enforced at the consensus level.

---

**KYC/AML Integration**

Know Your Customer (KYC), Know Your Business (KYB), and Anti-Money Laundering (AML) procedures are critical for preventing illicit financial activities. GX chains implement wallet-tier compliance where users and institutions undergo identity verification before engaging in transactions.

Different wallet tiers correspond to varying levels of verification, enabling granular control over transaction permissions. Wallets and transactions are screened against global sanctions lists to prevent prohibited activities. Institutional participants undergo rigorous checks before being authorized to transact or provide liquidity. These measures are enforced both off-chain through integration with identity verification providers and on-chain via validator oversight.

---

**FATF Travel Rule Support**

The Financial Action Task Force (FATF) Travel Rule requires that certain information about the originator and beneficiary of virtual asset transfers be transmitted alongside the transaction. GX stablecoins support this requirement natively.

Transaction messages include encrypted originator and beneficiary details. Licensed validators verify the presence and correctness of Travel Rule data before block inclusion. The Travel Rule metadata is compatible with cross-chain transfers via IBC, ensuring compliance across interconnected chains.

---

**Supervisory Oversight**

To facilitate regulatory supervision, GX chains provide supervisory-grade observability features. Regulators and authorized auditors can monitor transaction flows, proof-of-reserves, and compliance status in real time.

The 24/7 live proof-of-reserves system provides transparent, continuously updated reserve data. Immutable on-chain records create comprehensive audit trails for all transactions and validator actions. Supervisory entities can be granted read-only access to compliance dashboards and analytics tools.

---

---

**Key Security and Governance Controls**

Validator keys are secured in **Hardware Security Modules (HSMs)** with multi-party control mechanisms (MPC quorum) to enforce quorum-based authorization and eliminate single points of failure. Proposed changes follow a formal change-management pipeline: pre-announced release proposals, testing gates, scheduled deployment windows, and rollback mechanisms with immutable audit trails.

---

**Emergency Procedures and Circuit Breakers**

GX includes an Emergency Procedures Playbook defining supervised circuit breakers—rate limits, mint/burn suspension, or settlement pauses—activated only under strictly defined stress conditions with regulator involvement and post-event disclosure. These align with MiFID II-style built-in halt mechanisms.

---

**Zero-Knowledge Proofs and Privacy**

GX integrates Zero-Knowledge Proofs (ZKPs) to balance transparency with privacy. Wallets can demonstrate compliance with sanctions or KYC requirements without exposing personal data. The system can prove full reserve coverage without revealing custodian account details. Selective-disclosure "view keys" allow authorized supervisors to inspect provenance without broad data exposure, consistent with domestic privacy law.

---

By embedding compliance at the consensus layer and leveraging licensed validators, GX stablecoins provide legal certainty, operational transparency, cross-border compliance, and reduced exposure to illicit finance risks—making them suitable for institutional settlement, cross-border payments, and interoperable DeFi applications.
