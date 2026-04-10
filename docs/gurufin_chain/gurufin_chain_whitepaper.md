# Gurufin Chain Whitepaper

📡 The Neutral FX/DeFi Settlement Layer

---

## 🚀 Quick Links

- **Architecture**: [`GX Chain Overview`](/gx_chain/01_overview.md) | [`Reserve & Backing`](/gx_chain/02_reserve_and_backing.md)
- **GuruDex**: [`DEX Overview`](/gurudex/01_dex_overview.md) | [`OPRS Architecture`](/gurudex/02_hybrid_pools.md)
- **Use Cases**: [`Cross-Border Payments`](/use_cases/01_cross_border_payments.md) | [`Stablecoin FX Trading`](/use_cases/02_stablecoin_fx_trading.md)
- **Developer**: [`Testnet Access`](/developer_resources/01_testnet_access.md) | [`API Reference`](/developer_resources/02_api_reference.md)

---

## Introduction

Gurufin Chain is a public Delegated Proof-of-Stake (DPoS) Layer-1 blockchain built on the Cosmos SDK with Tendermint BFT consensus. It serves as the neutral settlement layer for the Gurufin ecosystem, enabling frictionless cross-border transactions and DeFi operations.

### Why Gurufin Chain?

- **Neutral FX Settlement**: Acts as an unbiased settlement layer for all GX stablecoin pairs
- **High Performance**: Sub-second finality with Tendermint BFT consensus
- **IBC-First**: Native interoperability with other Cosmos SDK chains
- **Regulatory Compliance**: Built-in compliance hooks for institutional adoption
- **Programmable**: Full EVM compatibility for DeFi applications

---

## Architecture

### Layered Design

```
┌─────────────────────────────────────────┐
│        Gurufin Chain (DPoS L1)          │
│   Neutral FX/DeFi Settlement Layer      │
├─────────────────────────────────────────┤
│        GX Stablecoin Network            │
│   Sovereign PoA L1 Chains (USGX, KRGX,  │
│        EURGX, JPGX, etc.)               │
└─────────────────────────────────────────┘
```

### Key Components

1. **Consensus Layer**: Tendermint BFT with DPoS validator selection
2. **Settlement Layer**: Atomic cross-chain transfers via IBC
3. **Smart Contract Layer**: EVM-compatible for DeFi apps
4. **Compliance Layer**: KYC/AML hooks at consensus level

---

## Consensus Mechanism

### Delegated Proof-of-Stake (DPoS)

Gurufin Chain uses a DPoS consensus model where token holders delegate their voting power to validators who produce blocks.

**Validator Requirements**:
- Minimum stake requirement
- Identity verification (KYC)
- Uptime guarantees (>99%)
- Compliance with jurisdictional regulations

**Security Model**:
- 2/3 + 1 honest validators guarantee safety
- Slashing penalties for malicious behavior
- Economic incentives for honest participation

---

## Interoperability

### IBC-First Design

Gurufin Chain is built with IBC (Inter-Blockchain Communication) as a first-class citizen, enabling:

- **Atomic Swaps**: Cross-chain transfers with finality guarantees
- **Light Client Integration**: Direct communication with other chains
- **Bridge Security**: Non-custodial cross-chain asset transfers

### GX Stablecoin Integration

Each GX stablecoin chain communicates with Gurufin Chain via IBC:

```
User Swap Flow:
1. USGX Chain → Burn 1,000 USGX
2. IBC Transfer → Gurufin Chain (settlement)
3. Gurufin Chain → Trigger KRGX Chain
4. KRGX Chain → Mint 1,298,700 KRGX
5. User receives KRGX
```

See detailed flow in: [`OPRS Architecture`](/gurudex/02_hybrid_pools.md)

---

## Fees: Guru-PEG

### Fiat-Indexed Fee Mechanism

Guru-PEG ensures predictable transaction costs by indexing fees to fiat values rather than cryptocurrency prices.

**Benefits**:
- **Predictability**: Users know exact fees in their local currency
- **Stability**: No fee spikes during network congestion
- **Fairness**: Fees scale with inflation (optional CPI indexation)

**Fee Structure**:
- Standard transfers: Fixed fee in local fiat
- Smart contract execution: Gas priced in GX stablecoins
- Cross-chain transfers: IBC relay fees + execution fees

See more: [`GX Chain Fees & Gas Model`](/gx_chain/01_overview.md#fees-and-gas-model)

---

## Compliance Features

### Built-In Regulatory Hooks

Gurufin Chain includes native compliance features:

1. **Wallet Tier System**: Different permission levels based on KYC status
2. **Transaction Monitoring**: Real-time compliance checks
3. **Jurisdictional Rules**: Chain-specific compliance policies
4. **Audit Trail**: Complete transaction history for regulators

See: [`GX Compliance & Regulation`](/gx_chain/05_compliance_and_regulation.md)

---

## Developer Ecosystem

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

- **TypeScript SDK**: `@gurufin/sdk`
- **Python SDK**: `gurufin-py`
- **Go SDK**: `cosmos-sdk` compatible

---

## Governance

### Proposal Process

1. **Submit Proposal**: Any token holder can submit
2. **Discussion Phase**: Community review and feedback
3. **Voting Period**: 7-day voting window
4. **Execution**: Auto-execution if passed

**Proposal Types**:
- Parameter changes
- Software upgrades
- Treasury allocations
- Governance amendments

See: [`GX Governance Framework`](/gx_chain/01_overview.md)

---

## Security

### Multi-Layer Security

1. **Formal Verification**: Smart contracts undergo rigorous testing
2. **Audit Process**: Multiple independent audits before mainnet
3. **Bug Bounty**: Active bug bounty program
4. **Upgrade Mechanism**: Safe, tested upgrade process

### Incident Response

- 24/7 monitoring team
- Automated incident response protocols
- Transparent communication during incidents

---

## Roadmap

### Phase 1: Foundation ✅
- Mainnet launch
- Initial validator set
- Basic IBC connectivity

### Phase 2: Ecosystem 🚧
- GuruDex launch
- Additional GX chain integrations
- Enhanced compliance features

### Phase 3: Expansion 📈
- Cross-chain bridges (non-IBC)
- Institutional products
- Global regulatory approvals

See full roadmap: [`Introduction → 03 Roadmap`](/introduction/03_roadmap.md)

---

## Resources

- **Live Monitor**: [`Live Reserve Scanner`](https://rescan.gurufin.io/)
- **Block Explorer**: [`TScan`](https://tscan.gurufin.io/)
- **Validator Docs**: [`GX Chain Overview`](/gx_chain/01_overview.md)
- **Community**: [`Discord`](https://discord.gg/gurufin) | [`Telegram`](https://t.me/gurufin)

---

*For technical details and specifications, refer to the linked documentation sections. This whitepaper serves as an overview of Gurufin Chain's architecture and capabilities.*