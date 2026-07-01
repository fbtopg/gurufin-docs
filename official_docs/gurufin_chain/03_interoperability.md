# Interoperability

Gurufin Chain is built with an IBC-first architecture for standards-based cross-chain asset transfers and messaging across compatible blockchain networks.

**Inter-Blockchain Communication (IBC)**

IBC is the primary interoperability layer. It enables cross-chain messaging and token transfers between Gurufin Chain and other Cosmos SDK-based networks, including GX stablecoin chains. This allows Payment-versus-Payment (PvP) settlement flows to be coordinated without relying on centrally operated bridge custody.

Cross-chain settlement depends on relayer availability, counterparty chain health, and the finality rules of each connected chain. Applications should treat single-chain finality and end-to-end IBC settlement time as separate operational metrics.

**EVM Compatibility**

To support existing application tooling, Gurufin includes EVM compatibility through an EVM gateway. Developers can deploy Solidity smart contracts while using Gurufin's settlement layer, IBC connectivity, and fee model.

EVM compatibility is intended to reduce integration friction for existing teams, not to replace Cosmos-native modules where native functionality is more appropriate.
