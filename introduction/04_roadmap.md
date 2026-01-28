# Roadmap

Gurufin is committed to transparent, milestone-driven development. This roadmap outlines our technical milestones and strategic objectives as we build the Stablecoin FX Layer for global finance.

## Development Philosophy

Our development follows three core principles:

| Principle | Description |
|---|---|
| **Security First** | Every component undergoes rigorous auditing before mainnet deployment |
| **Incremental Rollout** | Features are released progressively, starting with testnets and limited mainnet access |
| **Community Driven** | Major protocol changes go through governance proposals and community feedback |

## Roadmap Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        GURUFIN ROADMAP                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  PHASE 1          PHASE 2          PHASE 3          PHASE 4         │
│  Foundation       Expansion        Scale            Global           │
│                                                                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐      │
│  │ Mainnet  │    │ GuruDex  │    │ Multi-   │    │ CBDC     │      │
│  │ Launch   │───▶│ + GX     │───▶│ Chain    │───▶│ Bridge   │      │
│  │          │    │ Network  │    │ Expansion│    │          │      │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Foundation

**Status: Completed**

The foundational phase focused on building and launching the core infrastructure of the Gurufin ecosystem.

### Milestones Achieved

| Milestone | Description | Status |
|---|---|---|
| Gurufin Chain Genesis | Launch of the mainnet with initial validator set | ✅ Complete |
| GXN Token Launch | Native token deployment with staking enabled | ✅ Complete |
| Tendermint BFT Consensus | Sub-second finality with up to 10,000 TPS | ✅ Complete |
| CosmWasm Integration | Smart contract runtime deployment | ✅ Complete |
| Basic Governance | On-chain proposal and voting system | ✅ Complete |
| Testnet Program | Public testnet with faucet and documentation | ✅ Complete |

### Technical Specifications Delivered

| Component | Specification |
|---|---|
| Block Time | ~1 second |
| Finality | Instant (single-slot) |
| Initial Validators | 21 active validators |
| Smart Contracts | CosmWasm v1.0+ |
| SDK Version | Cosmos SDK v0.47+ |

---

## Phase 2: Expansion

**Status: In Progress**

The expansion phase focuses on deploying the core financial infrastructure and launching the GX Stablecoin network.

### Current Milestones

| Milestone | Description | Status |
|---|---|---|
| GuruDex v1.0 | Hybrid pool DEX with AMM + RFQ execution | 🔄 In Progress |
| GX Stablecoin Launch | First sovereign stablecoin chains with licensed validators | 🔄 In Progress |
| IBC Connectivity | Inter-Blockchain Communication with Cosmos Hub | 🔄 In Progress |
| Price Oracle Network | Decentralized oracle for FX rates | ✅ Complete |
| Guru-PEG Implementation | Fiat-predictable fee mechanism | ✅ Complete |

### Upcoming Milestones

| Milestone | Description | Target |
|---|---|---|
| GX Network Expansion | Additional sovereign stablecoin chains for new jurisdictions | Q2 |
| EVM Gateway | Ethereum Virtual Machine compatibility layer | Q2 |
| Liquidity Mining Program | Incentive program for GuruDex liquidity providers | Q2 |
| Mobile SDK | Native iOS/Android SDK for wallet integration | Q3 |

### Technical Focus Areas

| Area | Description |
|---|---|
| Hybrid Pool Optimization | Fine-tuning AMM curves and RFQ matching engine |
| Cross-Chain Security | Auditing IBC channels and light client implementations |
| Validator Expansion | Onboarding additional validators across geographies |
| API Standardization | RESTful and WebSocket APIs for institutional integration |

---

## Phase 3: Scale

**Status: Planned**

The scale phase focuses on expanding the GX Stablecoin network to additional currencies and enhancing cross-chain capabilities.

### Planned Milestones

| Milestone | Description | Target |
|---|---|---|
| GX Stablecoin Expansion | Launch of additional sovereign stablecoin chains across new jurisdictions | Q3-Q4 |
| PvP Settlement v2.0 | Enhanced atomic settlement with multi-leg support | Q3 |
| Institutional API Suite | Dedicated APIs for FIX protocol, prime brokerage integration | Q3 |
| Cross-Chain DEX | Direct trading with assets on Ethereum, BSC, Polygon | Q4 |
| Layer-2 Scaling | Optional rollup layer for ultra-high-frequency applications | Q4 |
| Advanced Governance | Quadratic voting, delegation, and treasury management | Q4 |

### Ecosystem Development

| Initiative | Description |
|---|---|
| Developer Grants | Funding for projects building on Gurufin |
| Hackathons | Quarterly hackathons with prizes for innovative applications |
| Integration Partners | Partnerships with wallets, exchanges, and payment providers |
| Educational Content | Comprehensive documentation, tutorials, and certification programs |

---

## Phase 4: Global

**Status: Future**

The global phase represents our long-term vision of becoming the definitive infrastructure for global digital finance.

### Strategic Objectives

| Objective | Description |
|---|---|
| CBDC Bridge | Integration with central bank digital currencies as they launch |
| FMI Partnerships | Collaboration with traditional financial market infrastructures |
| Regulatory Frameworks | Active participation in shaping global stablecoin regulations |
| Full Decentralization | Transition to fully community-governed protocol |

### Long-Term Vision

| Area | Vision |
|---|---|
| Currency Coverage | 50+ sovereign stablecoins covering major and emerging market currencies |
| Daily Volume | Target $10B+ daily trading volume on GuruDex |
| Validator Network | 100+ validators across 30+ jurisdictions |
| Developer Ecosystem | 1,000+ applications built on Gurufin infrastructure |
| User Adoption | 100M+ end users accessing services through Gurufin-powered applications |

---

## Technical Roadmap Details

### Smart Contract Development

| Component | Current | Next |
|---|---|---|
| GuruDex Contracts | v1.0 (Hybrid Pools) | v1.1 (Concentrated Liquidity) |
| GX Token Contracts | v1.0 (Basic ERC-20 compatible) | v1.1 (Hooks for compliance) |
| Governance Contracts | v1.0 (Basic proposals) | v2.0 (Quadratic voting) |
| Oracle Contracts | v1.0 (Price feeds) | v1.1 (Volume-weighted, multi-source) |

### Infrastructure Development

| Component | Current | Next |
|---|---|---|
| Node Software | v1.0.x | v1.1.x (Performance optimizations) |
| RPC Endpoints | Basic JSON-RPC | Enhanced REST + WebSocket + gRPC |
| Indexer | Block explorer only | Full GraphQL indexer |
| SDK | JavaScript/TypeScript | + Python, Go, Rust SDKs |

### Security Roadmap

| Initiative | Status |
|---|---|
| Smart Contract Audits | Ongoing (CertiK, Trail of Bits) |
| Bug Bounty Program | Active on Immunefi |
| Formal Verification | Planned for core contracts |
| Incident Response | 24/7 security monitoring active |

---

## How to Get Involved

| Activity | Description |
|---|---|
| **Testnet Participation** | Deploy contracts and test features on our public testnet |
| **Validator Program** | Apply to become a validator on Gurufin Chain or GX networks |
| **Developer Grants** | Apply for funding to build applications on Gurufin |
| **Community Governance** | Stake GXN and participate in protocol governance |
| **Bug Bounty** | Report security vulnerabilities for rewards |

For the latest updates on our roadmap, follow our official channels and join the community.
