# Interoperability

Gurufin Chain is designed to connect multiple blockchain ecosystems, enabling seamless asset transfers and cross-chain communication. The chain uses a three-layer interoperability stack: IBC Protocol for Cosmos ecosystem chains, EVM Gateway for Ethereum-compatible chains, and GatewayGX Module for heterogeneous chains like Solana.

---

**IBC (Inter-Blockchain Communication)**

Gurufin Chain adopts an IBC-first architecture as its foundation for cross-chain communication. IBC is the native Cosmos SDK protocol that enables trust-minimized communication using light client verification. It supports token transfers, cross-chain contract calls, and PvP settlement with any IBC-enabled blockchain including Cosmos Hub, Osmosis, and Celestia.

The IBC-first approach ensures atomic transactions where cross-chain operations either fully succeed or fully revert, eliminates reliance on central bridge operators by using cryptographic proofs, and provides native integration since IBC is built into the Cosmos SDK that Gurufin Chain uses.

---

**EVM Gateway**

The EVM Gateway connects Gurufin Chain to the Ethereum ecosystem and all EVM-compatible chains. ERC-20 tokens can be wrapped and transferred to Gurufin Chain, developers can invoke Ethereum contracts from Gurufin and vice versa, and standard Ethereum tooling like MetaMask and Hardhat is fully supported.

Supported chains include Ethereum, Polygon, Arbitrum, Optimism, BNB Chain, and other EVM-compatible networks.

---

**GatewayGX Module**

For blockchains that don't support IBC or EVM, Gurufin uses the custom GatewayGX module. This includes Solana integration through a custom adapter for its Proof-of-History runtime, with a modular adapter framework designed for future chain integrations.

The module works through custom protocol adapters that translate messages between chain formats, licensed validators that verify and relay cross-chain transactions, and atomic settlement guarantees that prevent double-spending.

---

**Summary**

Gurufin's multi-layer approach ensures connectivity with virtually any blockchain ecosystem. IBC provides the fastest and most trust-minimized path for Cosmos chains, EVM Gateway enables seamless Ethereum integration, and GatewayGX extends reach to non-standard chains—all while maintaining security and efficiency.
