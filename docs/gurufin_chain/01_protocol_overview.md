# Protocol Overview

Gurufin Chain is a purpose-built Layer-1 blockchain designed to serve as a global on-chain FX (foreign exchange) and DeFi hub for the Web3 economy. Unlike general-purpose blockchains, Gurufin Chain is specifically optimized for stablecoins, tokenized assets, and cross-border payments.

The chain addresses three fundamental challenges that have hindered blockchain adoption in traditional finance: unpredictable transaction fees, cross-chain fragmentation, and regulatory uncertainty. Through its innovative Guru-PEG mechanism, IBC-first architecture, and built-in compliance modules, Gurufin Chain provides a foundation where both institutions and retail users can participate in Web3 finance with confidence.

---

**High Performance**

Gurufin Chain delivers sub-second finality and throughput of up to 10,000 transactions per second. Unlike probabilistic consensus mechanisms that require multiple confirmations, transactions on Gurufin Chain are deterministically final once committed—critical for financial applications where settlement certainty matters.

**Interoperability**

The chain connects multiple blockchain ecosystems through a three-layer approach: native Cosmos IBC for trust-minimized cross-chain communication, an EVM Gateway for Ethereum ecosystem compatibility, and the GatewayGX module for connecting to non-standard chains like Solana.

**Financial Infrastructure**

Built specifically for financial use cases, Gurufin Chain supports Oracle Priced Reserve Swap (OPRS) execution for optimal pricing, Payment-versus-Payment (PvP) atomic settlement for eliminating counterparty risk, and sovereign stablecoin issuance with transparent reserve backing.

---

**Technology Stack**

Gurufin Chain is built on the Cosmos SDK framework, leveraging Tendermint BFT consensus for Byzantine fault tolerance and instant finality, Delegated Proof-of-Stake (DPoS) for balancing decentralization with performance, and a modular architecture that enables independent upgrades and feature additions.

**What Makes Gurufin Different**

Gurufin Chain is not just another blockchain—it's a neutral settlement layer designed specifically for financial applications. By combining predictable fees, regulatory compliance, and multi-chain connectivity, it serves as the infrastructure where cross-border payments, FX trading, stablecoin issuance, and compliant DeFi applications can thrive.

---

## Related Pages

### Gurufin Chain Architecture

- **[Network Architecture](./02_network_architecture.md)** - DPoS consensus and Tendermint BFT details
- **[Interoperability](./03_interoperability.md)** - IBC, EVM Gateway, and cross-chain communication
- **[Guru-PEG](./04_guru_peg.md)** - Fiat-indexed transaction fee mechanism
- **[Tokenomics](./05_tokenomics.md)** - $GXN token utility and supply allocation
- **[Governance](./06_governance.md)** - On-chain decision-making framework
- **[Validator Guide](./07_validator_guide.md)** - Requirements and operational standards

### GX Stablecoin Integration

Gurufin Chain serves as the settlement hub for GX stablecoins. Learn more:

- **[GX Overview](../gx_chain/01_overview.md)** - Sovereign stablecoin network architecture
- **[Reserve & Backing](../gx_chain/02_reserve_and_backing.md)** - 1:1 fiat backing and proof-of-reserves
- **[Mint & Burn Mechanism](../gx_chain/03_mint_and_burn.md)** - Automated bank-API-anchored issuance

### GuruDex Exchange

GuruDex uses Gurufin Chain for optimal FX trading execution:

- **[GuruDex Overview](../gurudex/01_dex_overview.md)** - OPRS architecture for stablecoin FX
- **[Hybrid Pools](../gurudex/02_hybrid_pools.md)** - Combined institutional and retail liquidity
- **[Risk Mitigation](../gurudex/05_risk_mitigation.md)** - Four-layer defense strategy

### Use Cases

Real-world applications built on Gurufin Chain:

- **[Cross-Border Payments](../use_cases/01_cross_border_payments.md)** - Remittance and B2B solutions
- **[Stablecoin FX Trading](../use_cases/02_stablecoin_fx_trading.md)** - Trading and arbitrage applications
- **[Institutional DeFi](../use_cases/03_institutional_defi.md)** - Tokenized assets and custody management

### Developer Resources

Get started building on Gurufin Chain:

- **[Testnet Access](../developer_resources/01_testnet_access.md)** - Network configuration and endpoints
- **[API Reference](../developer_resources/02_api_reference.md)** - Cosmos SDK and EVM JSON-RPC endpoints
- **[Full Developer Docs](../developer_resources/03_full_developer_docs.md)** - Comprehensive documentation portal
