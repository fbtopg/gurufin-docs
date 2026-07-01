# What is Gurufin?

Gurufin is a financial infrastructure ecosystem that connects blockchain settlement with institutional compliance requirements. It is organized around two connected layers: Gurufin Chain, the settlement hub, and the GX Stablecoin Network, the set of fiat-backed currency chains.

## 1. Gurufin Chain

Gurufin Chain is a public Layer-1 blockchain built with Cosmos SDK and Tendermint/CometBFT consensus. It is designed to serve as the neutral settlement hub for FX execution, cross-border payments, and institutional DeFi.

Key roles:

* Provides deterministic settlement finality under the chain's consensus rules.
* Uses GXN for staking, governance, and transaction fees through the Guru-PEG gas pricing mechanism.
* Connects compatible chains through IBC and supports Ethereum-compatible application tooling through an EVM gateway.

## 2. GX Stablecoin Network

The GX Stablecoin Network is a set of jurisdiction-specific chains, each aligned with local legal, banking, and reserve requirements. GX stablecoins are intended to be backed 1:1 by fiat reserves held with regulated custodians, with minting and redemption flows integrated through licensed banking partners and reserve verification controls.

## How the Layers Work Together

GX stablecoins are issued after verified fiat deposits, transferred to Gurufin Chain through IBC for FX execution or DeFi activity, and redeemed through the relevant licensed banking partner. This structure separates local issuance and compliance from cross-currency settlement and liquidity routing.
