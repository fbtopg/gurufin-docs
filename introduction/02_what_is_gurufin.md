# What is Gurufin?

Gurufin is the **Stablecoin FX Layer**—a purpose-built blockchain infrastructure designed specifically for foreign exchange and cross-border payments using stablecoins. It is not a general-purpose blockchain, but rather a specialized financial infrastructure that bridges the gap between traditional finance and the decentralized economy.

## Defining the Stablecoin FX Layer

The Stablecoin FX Layer is a new category of blockchain infrastructure that sits at the intersection of three domains:

```
┌─────────────────────────────────────────────────────────────────┐
│                    STABLECOIN FX LAYER                          │
│                                                                 │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐          │
│   │ Traditional │   │   DeFi &    │   │  Stablecoin │          │
│   │   FX/FMI    │ + │ Blockchain  │ + │  Networks   │          │
│   └─────────────┘   └─────────────┘   └─────────────┘          │
│                                                                 │
│   Settlement        Programmability    Digital Fiat             │
│   Standards         & Composability    Currencies               │
└─────────────────────────────────────────────────────────────────┘
```

| Domain | What Gurufin Takes | What Gurufin Improves |
|---|---|---|
| **Traditional FX/FMI** | Settlement standards, compliance frameworks, institutional trust models | Speed, cost, accessibility, transparency |
| **DeFi & Blockchain** | Programmability, composability, atomic transactions, 24/7 availability | Regulatory compliance, institutional-grade risk management |
| **Stablecoin Networks** | Digital fiat representation, blockchain efficiency | Multi-currency support, cross-chain interoperability, sovereign issuance |

## Core Architecture

Gurufin is built on two interconnected pillars that work together to provide a complete infrastructure for stablecoin-based finance.

### Pillar 1: Gurufin Chain (Public Layer-1)

The Gurufin Chain is a public, permissionless DPoS (Delegated Proof-of-Stake) blockchain built on the Cosmos SDK with Tendermint BFT consensus. It serves as the neutral settlement layer for the entire ecosystem.

**Key Characteristics:**

| Feature | Specification |
|---|---|
| Consensus | Tendermint BFT (Delegated Proof-of-Stake) |
| Finality | Sub-second (< 1 second) |
| Throughput | Up to 10,000 TPS |
| Native Token | GXN (staking, governance, fee payment) |
| Execution | CosmWasm smart contracts + EVM Gateway |
| Interoperability | IBC-native with EVM bridge support |

### Pillar 2: GX Stablecoin Network (Sovereign Chains)

The GX Stablecoin Network is a federation of jurisdiction-specific stablecoin chains. Each GX Stablecoin operates on its own sovereign chain with validators licensed in that jurisdiction, supporting any fiat currency.

**Key Characteristics:**

| Feature | Description |
|---|---|
| Backing | 1:1 fiat reserves held in licensed custodians |
| Validators | Jurisdictional Proof-of-Authority (PoA) with licensed entities |
| Minting/Burning | Automated via bank API integration |
| Proof-of-Reserves | 24/7 live attestation via oracles |
| Compliance | Embedded KYC/AML hooks and regulatory reporting |

## How It Works Together

The two pillars create a complete system for global stablecoin FX:

```
┌──────────────────────────────────────────────────────────────────┐
│                        USER APPLICATIONS                          │
│         (Wallets, DEXs, Payment Apps, Institutional APIs)        │
└───────────────────────────────┬──────────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────────┐
│                      GURUFIN CHAIN (L1)                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │   GuruDex    │  │    Price     │  │   PvP        │           │
│  │  (FX Swap)   │  │   Oracles    │  │ Settlement   │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│                          GXN Token                               │
└───────────────────────────────┬──────────────────────────────────┘
                                │ IBC
                                ▼
┌──────────────────────────────────────────────────────────────────┐
│                   GX STABLECOIN NETWORK                          │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐    │
│  │  GX-A  │  │  GX-B  │  │  GX-C  │  │  GX-D  │  │  ...   │    │
│  │ (Fiat) │  │ (Fiat) │  │ (Fiat) │  │ (Fiat) │  │        │    │
│  └────────┘  └────────┘  └────────┘  └────────┘  └────────┘    │
└──────────────────────────────────────────────────────────────────┘
```

1. **GX Stablecoins** are minted on their respective sovereign chains when users deposit fiat through licensed banking partners
2. **Stablecoins flow to Gurufin Chain** via IBC for trading, lending, and other DeFi activities
3. **GuruDex** provides efficient FX swaps between different GX Stablecoins using the Hybrid Execution Model
4. **PvP Settlement** enables atomic cross-chain swaps for secure, risk-free transactions
5. **Users withdraw** by burning stablecoins and receiving fiat through the banking network

## What Makes Gurufin Unique

Gurufin is not just another blockchain or stablecoin project. It is purpose-built infrastructure that combines the best of traditional finance and blockchain technology:

| Aspect | Traditional Finance | Generic Blockchains | Gurufin |
|---|---|---|---|
| Settlement Speed | 2-5 days | Seconds to minutes | Sub-second |
| Transaction Cost | $25-50+ per transfer | Variable (gas fees) | Fixed, fiat-predictable |
| Regulatory Status | Fully regulated | Often unclear | Compliance-embedded |
| FX Efficiency | Fragmented, opaque | Limited pairs, low liquidity | Hybrid execution, deep liquidity |
| Accessibility | Bank account required | Wallet required | Both supported |
| Interoperability | Limited | Chain-specific | IBC + EVM native |

Gurufin is the Stablecoin FX Layer that global finance has been waiting for.
