# GX Stablecoins Overview

## Introduction to the GX Stablecoin Network

The GX Stablecoin network is a sovereign, jurisdiction-specific stablecoin infrastructure designed to support the next generation of fiat-backed digital currencies. Built as a network of independent Layer-1 blockchains, each chain issues a local sovereign stablecoin pegged 1:1 to its respective fiat currency. This architecture enables regulatory compliance, transparency, and operational efficiency tailored to each jurisdiction’s legal and financial frameworks.

At the core of the GX network is a permissioned Proof-of-Authority (PoA) consensus mechanism, where licensed and regulated validators operate the network nodes. This governance model ensures that only authorized entities participate in block validation, reinforcing trust and compliance with jurisdictional requirements. The GX chains leverage the Cosmos SDK and Tendermint BFT technology to provide fast, secure, and interoperable blockchain infrastructure.

The GX Stablecoin network supports multiple fiat currencies, facilitating seamless cross-border payments, FX trading, and DeFi applications with embedded compliance and transparency. Automated minting and burning of stablecoins are anchored directly to bank API events, ensuring that the digital supply always corresponds to real-world fiat reserves.

## Supported Stablecoins

The GX Stablecoin network currently supports four primary fiat-pegged stablecoins, each issued on its own sovereign Layer-1 chain within the network. These stablecoins are fully backed by fiat reserves held in regulated custodial accounts, with live proof-of-reserves available 24/7 to ensure transparency and trust.

| Stablecoin | Pegged Currency | Description                         |
|------------|-----------------|-----------------------------------|
| **USGX**   | United States Dollar (USD) | USD-pegged stablecoin for global use, optimized for cross-border payments and FX trading. |
| **KRGX**   | South Korean Won (KRW)     | KRW-pegged stablecoin tailored for the South Korean market and regional transactions. |
| **JPGX**   | Japanese Yen (JPY)         | JPY-pegged stablecoin designed for Japan’s financial ecosystem and cross-border flows. |
| **PHGX**   | Philippine Peso (PHP)      | PHP-pegged stablecoin supporting the Philippine economy and remittance corridors. |

Each stablecoin operates on its dedicated GX chain, enabling jurisdictional sovereignty, regulatory compliance, and tailored governance.

## Jurisdictional Model

The GX Stablecoin network’s jurisdictional model is a foundational design principle that aligns stablecoin issuance and operation with local regulatory frameworks. Each GX chain is an independent Layer-1 blockchain governed by licensed validators who are regulated entities within the respective jurisdiction. This model ensures that stablecoin issuance, reserve management, and transactional compliance adhere to local laws and supervisory requirements.

By decentralizing issuance across sovereign chains, the GX network mitigates risks associated with centralized stablecoin providers and enhances regulatory transparency. Validators are bound by legal agreements and compliance obligations, and the network enforces wallet-tier compliance, including KYC/AML screening and sanctions checks, at the consensus layer. This architecture supports supervisory-grade observability and auditability, making GX stablecoins suitable for institutional and government use cases.

## Proof-of-Authority (PoA) Consensus

The GX Stablecoin chains utilize a permissioned Proof-of-Authority (PoA) consensus mechanism, implemented via the Cosmos SDK and Tendermint Byzantine Fault Tolerant (BFT) consensus engine. PoA consensus relies on a set of pre-approved, licensed validators who are authorized to produce blocks and validate transactions.

This consensus approach offers several advantages for stablecoin issuance:

- **Regulatory Compliance:** Validators are vetted and licensed entities, ensuring that network operations comply with jurisdictional regulations.
- **High Performance:** PoA enables fast block times (sub-second) and deterministic finality, supporting high throughput and low latency transaction processing.
- **Security and Trust:** Validator identities are known and accountable, reducing the risk of malicious behavior and enhancing network integrity.
- **Governance Control:** The permissioned nature allows for governance policies that reflect local regulatory requirements and operational standards.

The PoA model is complemented by interoperability protocols such as Inter-Blockchain Communication (IBC) and Ethereum Virtual Machine (EVM) compatibility, enabling GX stablecoins to interact seamlessly with other blockchains and DeFi ecosystems.

## Summary

The GX Stablecoin network represents a pioneering approach to stablecoin infrastructure by combining sovereign jurisdictional governance with robust blockchain technology. Its permissioned PoA consensus ensures compliance and security, while the network’s modular design supports multiple fiat-pegged stablecoins tailored to regional markets. Through automated mint/burn mechanisms anchored to bank APIs and continuous proof-of-reserves transparency, GX stablecoins provide a trustworthy and efficient medium for cross-border payments, FX trading, institutional settlement, and DeFi applications.

By integrating regulatory compliance at the consensus layer and leveraging advanced interoperability features, the GX Stablecoin network establishes a neutral, scalable, and transparent foundation for the evolving Web3 economy.

---

*For detailed technical specifications, developer resources, and integration guides, please refer to the subsequent sections of this documentation.*