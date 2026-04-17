# Interoperability

Gurufin Chain utilizes a multi-layer interoperability stack to connect disparate blockchain ecosystems securely.

**IBC (Inter-Blockchain Communication)**
The primary foundation for cross-chain transfers within the Cosmos ecosystem. It enforces Payment-versus-Payment (PvP) settlement using cryptographic proofs and light client verification, eliminating the need for custodial bridge operators.

**EVM Gateway**
Connects Gurufin Chain to Ethereum, Polygon, Arbitrum, BNB Chain, and other EVM networks. Supports ERC-20 wrapping, bidirectional smart contract invocation, and standard Ethereum tooling (e.g., MetaMask).

**GatewayGX Module (Planned)**
A future adapter framework intended for non-standard, heterogeneous chains like Solana. *(Note: CosmWasm is not supported on Gurufin Chain).*

**Canonical Asset Registry**
To prevent liquidity fragmentation, on-chain governance maintains a registry designating authoritative asset representations. IBC-imported assets are prioritized as canonical over gateway-wrapped versions.
