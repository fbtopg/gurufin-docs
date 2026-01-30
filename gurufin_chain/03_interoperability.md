# Interoperability

Gurufin Chain is designed to connect multiple blockchain ecosystems, enabling seamless asset transfers and cross-chain communication. The chain uses a three-layer interoperability stack: IBC Protocol for Cosmos ecosystem chains, EVM Gateway for Ethereum-compatible chains, and GatewayGX Module for heterogeneous chains like Solana.

---

**IBC (Inter-Blockchain Communication)**

Gurufin Chain adopts an IBC-first architecture as its foundation for cross-chain communication. IBC uses escrowed message passing (ICS-20/27 standards) to enforce Payment-versus-Payment (PvP) settlement across ledgers, ensuring assets move only when both sides are securely validated. IBC assets are represented on-chain with full provenance tracking via denom traces.

The IBC-first approach ensures atomic transactions where cross-chain operations either fully succeed or fully revert, eliminates reliance on central bridge operators by using light client verification and cryptographic proofs, and reduces systemic bridge risk compared to custodial wrapped-token bridges.

---

**EVM Gateway**

The EVM Gateway connects Gurufin Chain to the Ethereum ecosystem and all EVM-compatible chains. ERC-20 tokens can be wrapped and transferred to Gurufin Chain, developers can invoke Ethereum contracts from Gurufin and vice versa, and standard Ethereum tooling like MetaMask and Hardhat is fully supported.

Supported chains include Ethereum, Polygon, Arbitrum, Optimism, BNB Chain, and other EVM-compatible networks.

---

**GatewayGX Module**

For blockchains that don't support IBC or EVM, Gurufin uses the custom GatewayGX module. This includes Solana integration through a custom adapter for its Proof-of-History runtime, with a modular adapter framework designed for future chain integrations.

Gateway-wrapped assets are minted via the tokenfactory/CW-20 module and clearly marked with a `gw` prefix (e.g., gwUSDC, gwUSDT) to distinguish them from canonical IBC imports. The module operates under dual control: oracles validate transfer conditions, and timeout safeguards automatically reverse incomplete transactions to prevent bridge risk.

---

**Canonical Asset Registry**

To prevent liquidity fragmentation, governance maintains a Canonical Asset Registry that designates authoritative representations of each currency. IBC-based imports are preferred as canonical, while gateway-wrapped versions are recognized under lower risk weights and transaction limits. Optional parity pools keep narrow-band alignment between canonical and non-canonical representations without forcing users into a single venue.

---

**Summary**

Gurufin's multi-layer approach ensures connectivity with virtually any blockchain ecosystem. IBC provides the most trust-minimized path for Cosmos chains, EVM Gateway enables seamless Ethereum integration, and GatewayGX extends reach to non-standard chains—all governed by the canonical asset registry to concentrate liquidity and maintain security.
