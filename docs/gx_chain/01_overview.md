# GX Chain Overview

🔗 Sovereign Stablecoin Network — Jurisdiction-Specific PoA Chains

---

## 🚀 Quick Links

- **Introduction**: [`01 Vision & Mission`](/introduction/01_vision_mission.md) | [`02 What is Gurufin?`](/introduction/02_what_is_gurufin.md)
- **GX Stablecoins**: [`02 Reserve & Backing`](/gx_chain/02_reserve_and_backing.md) | [`03 Mint & Burn`](/gx_chain/03_mint_and_burn.md) | [`04 Multi-Currency`](/gx_chain/04_multi_currency_support.md) | [`05 Compliance`](/gx_chain/05_compliance_and_regulation.md)
- **GuruDex**: [`DEX Overview`](/gurudex/01_dex_overview.md) | [`OPRS Architecture`](/gurudex/02_hybrid_pools.md)
- **Gurufin Chain**: [`Whitepaper`](/gurufin_chain/gurufin_chain_whitepaper.md)
- **Use Cases**: [`01 Cross-Border Payments`](/use_cases/01_cross_border_payments.md) | [`02 Stablecoin FX Trading`](/use_cases/02_stablecoin_fx_trading.md)
- **Developer**: [`Testnet Access`](/developer_resources/01_testnet_access.md)

---

## What is GX Chain?

GX Chain is a sovereign stablecoin framework designed to support the next generation of fiat-backed digital currencies. Rather than operating as a single blockchain, GX Chain functions as a network of independent Layer-1 chains, each issuing a local sovereign stablecoin pegged 1:1 to its respective fiat currency. This architecture enables regulatory compliance, transparency, and operational efficiency tailored to each jurisdiction's legal and financial frameworks.

### Key Features

- **Sovereign Chains**: Each currency has its own dedicated PoA blockchain
- **Jurisdictional Compliance**: Licensed validators in each jurisdiction
- **Live Proof-of-Reserves**: 24/7 reserve scanner
- **IBC Interoperability**: Atomic cross-chain transfers
- **EVM Compatibility**: Smart contract support

---

## Architecture

### Jurisdictional Model

Each GX chain is an independent Layer-1 blockchain governed by licensed validators who are regulated entities within the respective jurisdiction. This model ensures that stablecoin issuance, reserve management, and transactional compliance adhere to local laws and supervisory requirements.

**Supported Currencies**:
- **USGX Chain** — USD-pegged, US jurisdiction validators
- **KRGX Chain** — KRW-pegged, Korea jurisdiction validators
- **EURGX Chain** — EUR-pegged, EU jurisdiction validators
- **JPGX Chain** — JPY-pegged, Japan jurisdiction validators

See: [`Sovereign Chain Architecture`](/gurudex/01_dex_overview.md#sovereign-chain-architecture)

### Proof-of-Authority Consensus

The GX chains utilize a permissioned Proof-of-Authority consensus mechanism implemented via Cosmos SDK and Tendermint BFT. PoA consensus relies on pre-approved, licensed validators authorized to produce blocks and validate transactions.

This approach offers:
- **Regulatory compliance** through vetted and licensed validators
- **High performance** with sub-second confirmations and five-figure TPS on commodity hardware (consistent with CBDC pilot benchmarks)
- **Security** through known and accountable validator identities
- **Governance control** reflecting local regulatory requirements

The PoA model is complemented by interoperability protocols such as IBC and EVM compatibility, enabling GX stablecoins to interact seamlessly with other blockchains and DeFi ecosystems.

---

## Multi-Currency Stablecoin Engine

GX Chain supports local fiat currencies through its sovereign chain architecture. Each currency operates on its own dedicated chain with jurisdiction-specific validators, enabling regulatory compliance while maintaining interoperability with the broader Gurufin ecosystem.

### Reserve Backing

The stablecoins are fully backed by fiat reserves held in regulated custodial accounts, with live proof-of-reserves available 24/7 to ensure transparency and trust. Automated minting and burning are anchored directly to bank API events, ensuring that the digital supply always corresponds to real-world fiat reserves.

See: [`Reserve & Backing`](/gx_chain/02_reserve_and_backing.md)

### Mint & Burn Mechanics

When a user requests to mint USGX:
1. User deposits USD into regulated custodial account
2. Bank API confirms receipt
3. USGX is minted on USGX Chain
4. User receives USGX in their wallet

When a user redeems USGX:
1. User burns USGX on USGX Chain
2. Bank API confirms burn
3. USD is withdrawn from custodial account
4. USD is transferred to user's bank account

This process is fully automated and auditable in real-time via the [`Live Reserve Scanner`](https://rescan.gurufin.io/).

See: [`Mint & Burn Process`](/gx_chain/03_mint_and_burn.md)

---

## Fees and Gas Model

Gas is paid in the local GX stablecoin, with transaction fees denominated and fixed in local fiat terms within narrow bands. Unlike congestion-auction fee models on public chains, GX's fixed-fee design ensures predictable point-of-sale usability. Fees may be optionally indexed to CPI for long-run sustainability. Paymaster contracts allow institutions to sponsor end-user fees during early adoption.

### Fee Predictability

| Chain Type | Fee Model | Example |
|------------|-----------|---------|
| Retail Lanes | Fixed fiat fee | $0.01 per transaction |
| Institutional | Negotiated rates | Volume-based discounts |
| Cross-Chain | IBC relay + execution | ~$0.05 per transfer |

See: [`Gurufin Chain Guru-PEG`](/gurufin_chain/gurufin_chain_whitepaper.md#fees-guru-peg)

---

## Offline Payments

For intermittent-connectivity environments, GX supports an offline mode for low-value flows. Value transfers are recorded locally with secure hardware attestations, policy caps, and time-bounded validity, then reconciled to the chain when connectivity returns. Double-spend controls include spend limits, rolling counters, and post-reconciliation checks.

---

## Compliance Framework

Every validator is legally bound to a jurisdiction, embedding AML, CFT, and KYC compliance obligations into the consensus mechanism. This approach reduces regulatory blind spots by aligning validation authority with supervisory oversight.

**Compliance Features**:
- **Wallet Tiers**: Different permission levels based on KYC status
- **Transaction Monitoring**: Real-time AML checks
- **Jurisdictional Rules**: Chain-specific compliance policies
- **Audit Trail**: Complete transaction history for regulators

See: [`GX Compliance & Regulation`](/gx_chain/05_compliance_and_regulation.md)

---

## Interoperability

### IBC-First Design

GX chains use IBC (Inter-Blockchain Communication) for seamless cross-chain transfers:

```
Cross-Chain Transfer Flow:
1. User initiates transfer on source chain
2. Source chain locks tokens
3. IBC packet sent to destination chain
4. Destination chain mints/reveals tokens
5. Recipient receives tokens
```

### Gurufin Chain Integration

GX stablecoins integrate with Gurufin Chain (the neutral settlement layer) for:
- **FX Swaps**: Via GuruDex OPRS
- **DeFi Applications**: EVM-compatible smart contracts
- **Cross-Chain Bridges**: Non-IBC interoperability

See: [`Gurufin Chain Whitepaper`](/gurufin_chain/gurufin_chain_whitepaper.md) | [`GuruDex Overview`](/gurudex/01_dex_overview.md)

---

## Tokenized Assets

GX chains provide regulated foundations for tokenized assets (e.g., RWAs, STOs, and programmatic payments/NFT credentials) under local law, anticipating scalable participation in the emerging web3 economy.

**Supported Asset Classes**:
- **Real World Assets (RWAs)**: Real estate, commodities
- **Securities Token Offerings (STOs)**: Compliant security tokens
- **Programmable Payments**: Automated payroll, subscriptions
- **NFT Credentials**: Digital certificates, licenses

See: [`Institutional DeFi Use Case`](/use_cases/03_institutional_defi.md)

---

## Security

### Institutional Assurance

- **Licensed Validators**: All validators are regulated entities
- **Formal Audits**: Multiple independent security audits
- **Bug Bounty**: Active security reward program
- **Insurance**: Reserve-backed security guarantees

### Zero-Knowledge Privacy

> **Note:** This feature is not yet implemented. Discussion ongoing regarding privacy-preserving ZK protocols to enable confidential transactions while maintaining auditability. ZK-proofs could demonstrate compliance with regulatory requirements without revealing sensitive transaction details, enabling institutional adoption while preserving user privacy.

---

## Performance

### Benchmarks

| Metric | Target | Achieved |
|--------|--------|----------|
| Transaction Finality | <1 second | ~500ms |
| TPS (Commodity Hardware) | 10,000+ | 15,000 |
| Cross-Chain Latency | <5 seconds | ~3 seconds |
| Uptime | 99.9% | 99.97% |

Consistent with CBDC pilot benchmarks and institutional-grade requirements.

---

## Developer Resources

### Getting Started

**Testnet Access**:
- Chain ID: `guru_631-1`
- RPC: `https://trpc.gurufin.io`
- Faucet: [`https://faucet.gurufin.io/`](https://faucet.gurufin.io/)
- Explorer: [`https://tscan.gurufin.io/`](https://tscan.gurufin.io/)

**Documentation**:
- [`API Reference`](/developer_resources/02_api_reference.md)
- [`Full Developer Docs`](/developer_resources/03_full_developer_docs.md)
- [`Ecosystem Grant Program`](/developer_resources/04_ecosystem_grant_program.md)

### SDK Support

```typescript
// Example: Check USGX balance
import { GXChainClient } from '@gurufin/sdk';

const client = new GXChainClient('usgx_631-1');
const balance = await client.getBalance('guru1...');
console.log(`Balance: ${balance.amount} USGX`);
```

See more examples: [`Full Developer Docs`](/developer_resources/03_full_developer_docs.md)

---

## Related Documentation

- **Gurufin Chain**: [`Whitepaper`](/gurufin_chain/gurufin_chain_whitepaper.md)
- **GuruDex**: [`DEX Overview`](/gurudex/01_dex_overview.md) | [`OPRS Architecture`](/gurudex/02_hybrid_pools.md)
- **Reserves**: [`Live Reserve Scanner`](https://rescan.gurufin.io/) | [`Reserve & Backing`](/gx_chain/02_reserve_and_backing.md)
- **Use Cases**: [`Cross-Border Payments`](/use_cases/01_cross_border_payments.md) | [`Stablecoin FX Trading`](/use_cases/02_stablecoin_fx_trading.md)

---

*GX Chain is the foundation of regulated, interoperable stablecoin infrastructure — bridging traditional finance and Web3 with compliance at its core.*

At the core of GX Chain is a permissioned Proof-of-Authority (PoA) consensus mechanism, where licensed and regulated validators operate the network nodes. This governance model ensures that only authorized entities participate in block validation, reinforcing trust and compliance with jurisdictional requirements. The chains leverage the Cosmos SDK and Tendermint BFT technology to provide fast, secure, and interoperable blockchain infrastructure.

---

**Multi-Currency Stablecoin Engine**

GX Chain supports local fiat currencies through its sovereign chain architecture. Each currency operates on its own dedicated chain with jurisdiction-specific validators, enabling regulatory compliance while maintaining interoperability with the broader Gurufin ecosystem.

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

Gas is paid in the local GX stablecoin, with transaction fees denominated and fixed in local fiat terms within narrow bands. Unlike congestion-auction fee models on public chains, GX's fixed-fee design ensures predictable point-of-sale usability. Fees may be optionally indexed to CPI for long-run sustainability. Paymaster contracts allow institutions to sponsor end-user fees during early adoption.

---

**Offline Payments**

For intermittent-connectivity environments, GX supports an offline mode for low-value flows. Value transfers are recorded locally with secure hardware attestations, policy caps, and time-bounded validity, then reconciled to the chain when connectivity returns. Double-spend controls include spend limits, rolling counters, and post-reconciliation checks.
