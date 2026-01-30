# Interoperability

Gurufin Chain is designed to connect multiple blockchain ecosystems, enabling seamless asset transfers and cross-chain communication. This page explains the three interoperability mechanisms that make this possible.

---

## Three-Layer Interoperability Stack

```
┌─────────────────────────────────────────────────────────┐
│                    GatewayGX Module                     │
│              (Solana, other non-IBC chains)             │
├─────────────────────────────────────────────────────────┤
│                     EVM Gateway                         │
│              (Ethereum, Polygon, BSC, etc.)             │
├─────────────────────────────────────────────────────────┤
│                   IBC Protocol                          │
│              (Cosmos, Osmosis, Terra, etc.)             │
└─────────────────────────────────────────────────────────┘
```

---

## IBC (Inter-Blockchain Communication) — Primary Protocol

Gurufin Chain adopts an **IBC-first architecture** as its foundation for cross-chain communication.

| Feature | Description |
|---------|-------------|
| **Protocol Type** | Native Cosmos SDK protocol |
| **Communication** | Trust-minimized using light client verification |
| **Use Cases** | Token transfers, cross-chain contract calls, PvP settlement |
| **Connected Chains** | Any IBC-enabled blockchain (Cosmos Hub, Osmosis, Celestia, etc.) |

**Why IBC-First?**
- Atomic transactions: Either the entire cross-chain operation succeeds, or it fully reverts
- No central bridge operator: Security relies on cryptographic proofs, not trusted third parties
- Native integration: Built into the Cosmos SDK that Gurufin Chain uses

---

## EVM Gateway — Ethereum Compatibility

The EVM Gateway connects Gurufin Chain to the Ethereum ecosystem and all EVM-compatible chains.

| Capability | How It Works |
|------------|--------------|
| **Asset Bridging** | ERC-20 tokens can be wrapped and transferred to Gurufin Chain |
| **Smart Contract Calls** | Invoke Ethereum contracts from Gurufin and vice versa |
| **Developer Tools** | Supports MetaMask, Hardhat, and standard Ethereum tooling |

**Supported Chains**: Ethereum, Polygon, Arbitrum, Optimism, BNB Chain, and other EVM-compatible networks.

---

## GatewayGX Module — Heterogeneous Chain Support

For blockchains that don't support IBC or EVM, Gurufin uses the custom **GatewayGX module**.

| Target Chain | Integration Method |
|--------------|-------------------|
| **Solana** | Custom adapter for Proof-of-History runtime |
| **Other Chains** | Modular adapter framework for future integrations |

**How It Works:**
1. Custom protocol adapters translate messages between chain formats
2. Licensed validators verify and relay cross-chain transactions
3. Atomic settlement guarantees prevent double-spending

---

## Summary Comparison

| Method | Best For | Trust Model | Speed |
|--------|----------|-------------|-------|
| **IBC** | Cosmos ecosystem | Trust-minimized (light clients) | Fast |
| **EVM Gateway** | Ethereum ecosystem | Multi-signature validation | Moderate |
| **GatewayGX** | Non-standard chains | Validator-orchestrated | Variable |

Gurufin's multi-layer approach ensures connectivity with virtually any blockchain ecosystem while maintaining security and efficiency.
