# Executive Summary

## What is Gurufin?

Gurufin is a specialized financial infrastructure that combines the efficiency of blockchain technology with the stability and regulatory compliance required for institutional adoption. It serves as a neutral, public Layer-1 settlement hub for stablecoins, tokenized assets, and cross-border payments.

The ecosystem is built on two interconnected pillars:

### Gurufin Chain (Layer 1)

- **Public, permissionless blockchain** built on Cosmos SDK with Tendermint BFT consensus
- **Sub-second finality** and throughput of up to 10,000 TPS
- **Neutral FX/DeFi settlement hub** where cross-border payments and trading occur
- **Native token (GXN)** for staking, governance, and fee payment via Guru-PEG
- **IBC-first interoperability** with EVM Gateway for Ethereum ecosystem compatibility

### GX Stablecoin Network

- **Federation of sovereign stablecoin chains**, each operating under its own jurisdiction
- **Licensed validators** bound to jurisdictional Proof-of-Authority (PoA) consensus
- **Fully backed 1:1** by fiat reserves held in regulated custodians
- **Automated minting and burning** via bank API integration
- **24/7 live proof-of-reserves** attestation

---

## The Innovation: Oracle Priced Reserve Swap (OPRS)

Traditional decentralized exchanges (DEXs) use Automated Market Makers (AMMs) that rely on supply/demand dynamics within liquidity pools. While effective for volatile assets, this approach introduces unnecessary slippage and fails to reflect actual foreign exchange rates for stablecoin trading.

Gurufin's **Oracle Priced Reserve Swap (OPRS)** architecture represents a paradigm shift:

- **Oracle-Guided Pricing** — Real-time FX rates from trusted oracles determine swap prices
- **Mint/Burn Mechanism** — Instead of swapping tokens in a pool, OPRS burns input stablecoins and mints output stablecoins
- **No Slippage** — Trades execute at precise market rates, regardless of trade size
- **IBC Settlement** — Cross-chain transfers are atomic, eliminating counterparty risk

This architecture is purpose-built for stablecoin foreign exchange trading, where prices are determined by real-world FX rates rather than on-chain supply/demand dynamics.

---

## Key Benefits

- **Institutional-Grade Settlement** — Payment-versus-Payment (PvP) atomicity eliminates principal risk
- **Predictable Fees** — Guru-PEG mechanism ensures fiat-indexed, stable transaction costs
- **Deep Liquidity** — Hybrid pools combine retail AMM and institutional RFQ liquidity
- **Regulatory Compliance** — Wallet-tier KYC/AML, jurisdictional validators, and supervisory observability
- **Interoperability** — IBC-first design with controlled EVM gateway for maximum connectivity
