# What is Gurufin?

<figure><img src="../.gitbook/assets/Gemini_Generated_Image_iljs2xiljs2xiljs.jpg" alt=""><figcaption></figcaption></figure>



Gurufin is a specialized financial infrastructure that combines the efficiency of blockchain technology with the stability and regulatory compliance required for institutional adoption.

_The ecosystem is built on two interconnected pillars:_

---

**Gurufin Chain**

* Public, permissionless Layer-1 blockchain built on Cosmos SDK with Tendermint BFT consensus
* Sub-second finality and throughput of up to 10,000 TPS
* Serves as a neutral FX/DeFi settlement hub where cross-border payments and trading occur
* Native token (GXN) for staking, governance, and fee payment via Guru-PEG
* IBC-first interoperability with EVM Gateway for Ethereum ecosystem compatibility

---

**GX Stablecoin Network**

* Federation of sovereign stablecoin chains, each operating under its own jurisdiction
* Licensed validators bound to jurisdictional Proof-of-Authority (PoA) consensus
* Fully backed 1:1 by fiat reserves held in regulated custodians
* Automated minting and burning via bank API integration
* 24/7 live proof-of-reserves attestation

---

Together, these components create a complete system: GX Stablecoins are minted when users deposit fiat through licensed partners, flow to Gurufin Chain via IBC for trading and DeFi activities, and can be redeemed back to fiat at any time.

---

## Deep Dive: Gurufin Chain

For detailed technical information about Gurufin Chain:

| Topic | Page |
|-------|------|
| **Protocol Overview** | [Learn about the purpose-built Layer-1 for FX/DeFi](../gurufin_chain/01_protocol_overview.md) |
| **Network Architecture** | [DPoS consensus and Tendermint BFT details](../gurufin_chain/02_network_architecture.md) |
| **Interoperability** | [IBC, EVM Gateway, and cross-chain communication](../gurufin_chain/03_interoperability.md) |
| **Guru-PEG Fees** | [Fiat-indexed transaction fee mechanism](../gurufin_chain/04_guru_peg.md) |
| **Tokenomics** | [$GXN token utility and supply allocation](../gurufin_chain/05_tokenomics.md) |
| **Governance** | [On-chain decision-making framework](../gurufin_chain/06_governance.md) |
| **Validator Setup** | [Requirements and operational standards](../gurufin_chain/07_validator_guide.md) |

---

## Deep Dive: GX Stablecoin Network

For detailed information about the GX stablecoin framework:

| Topic | Page |
|-------|------|
| **GX Overview** | [Sovereign stablecoin network architecture](../gx_chain/01_overview.md) |
| **Reserve & Backing** | [1:1 fiat backing and proof-of-reserves](../gx_chain/02_reserve_and_backing.md) |
| **Mint & Burn** | [Automated bank-API-anchored issuance](../gx_chain/03_mint_and_burn.md) |
| **Multi-Currency** | [Jurisdictional sovereignty and cross-chain FX](../gx_chain/04_multi_currency_support.md) |
| **Compliance** | [PoA consensus and regulatory framework](../gx_chain/05_compliance_and_regulation.md) |

---

## Deep Dive: GuruDex (OPRS)

For detailed information about the exchange:

| Topic | Page |
|-------|------|
| **DEX Overview** | [OPRS architecture for stablecoin FX trading](../gurudex/01_dex_overview.md) |
| **Hybrid Pools** | [Combined institutional and retail liquidity](../gurudex/02_hybrid_pools.md) |
| **Liquidity & Rewards** | [LP mechanics and fee distribution](../gurudex/03_liquidity_and_rewards.md) |
| **Smart Contracts** | [Core contracts and swap routing](../gurudex/04_smart_contract_logic.md) |
| **Risk Mitigation** | [Four-layer defense strategy](../gurudex/05_risk_mitigation.md) |

---

## Quick Start

Looking to build on Gurufin? Start here:

- **[Testnet Access](../developer_resources/01_testnet_access.md)** - Get testnet tokens and network configuration
- **[API Reference](../developer_resources/02_api_reference.md)** - Cosmos SDK and EVM endpoints
- **[Full Developer Docs](../developer_resources/03_full_developer_docs.md)** - Comprehensive documentation portal
- **[Ecosystem Grants](../developer_resources/04_ecosystem_grant_program.md)** - Funding for builders

---

## Explore Use Cases

Real-world applications built on Gurufin:

- **[Cross-Border Payments](../use_cases/01_cross_border_payments.md)** - Remittance and B2B solutions
- **[FX Trading](../use_cases/02_stablecoin_fx_trading.md)** - Stablecoin exchange and arbitrage
- **[Institutional DeFi](../use_cases/03_institutional_defi.md)** - Tokenized assets and custody
- **[Government & CBDC](../use_cases/04_government_and_cbdc.md)** - Central bank applications
