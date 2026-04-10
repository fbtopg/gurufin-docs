# Network Architecture

This page details the underlying structure and operational mechanisms of the Gurufin Chain, focusing on its consensus engine and the various node types that constitute the network's decentralized infrastructure. Understanding these components is crucial for comprehending how Gurufin Chain achieves its goals of fast, secure, and final transactions, particularly within the context of financial applications.

## Key Concepts

The Gurufin Chain's network architecture is designed for robust performance and security, integrating several core concepts:

### Consensus Engine: Tendermint BFT + DPoS

Gurufin Chain employs a hybrid consensus mechanism that combines the strengths of **Tendermint Byzantine Fault Tolerant (BFT)** and **Delegated Proof-of-Stake (DPoS)**.

*   **Tendermint BFT**: This is the core engine responsible for achieving agreement among network validators. It utilizes a three-phase voting process: Propose, Prevote, and Precommit, culminating in a Block Finalized state. A key advantage of Tendermint BFT is its resilience; the network remains secure even if up to one-third of validators are malicious or offline. Furthermore, once a block is committed, it achieves immediate finality, meaning it cannot be reversed and requires no additional confirmations.
*   **Delegated Proof-of-Stake (DPoS)**: DPoS governs participation in the consensus process. Token holders delegate their native GXN tokens to trusted validators. The validators with the highest amount of delegated stake form the active validator set, and block producers are selected based on their stake weight. This design strikes a balance between decentralization and performance, allowing for efficient block production while still distributing control.

### Node Types

The Gurufin network comprises different types of **nodes**, each fulfilling a specific function:

*   **Validator Node**: These are critical participants in the network. They participate in the consensus process, produce new blocks, and vote on proposals. Validator nodes are typically run by professional operators who have a significant amount of GXN staked, demonstrating their commitment and investment in the network's security.
*   **Full Node**: A full node maintains a complete copy of the entire blockchain history. It plays a vital role in relaying transactions across the network and ensuring data integrity. These nodes are often run by infrastructure providers and developers who need access to the full chain state.
*   **Archive Node**: An archive node stores all historical states of the blockchain. Unlike a full node which may prune older states, an archive node preserves every single state change, making it invaluable for historical queries, analytics services, and auditing purposes.
*   **Light Client**: While not detailed in the provided excerpts, light clients are generally lightweight nodes that do not store the entire blockchain history. Instead, they verify transactions and block headers by relying on information provided by full nodes, making them suitable for resource-constrained environments or applications that only need to verify specific data without the overhead of running a full node.

## Relationship to Performance

The chosen network architecture, particularly the **Tendermint BFT + DPoS** consensus mechanism, directly contributes to the Gurufin Chain's **performance**. The design aims for "sub-second finality and throughput of up to 10,000 TPS," which are crucial metrics for a financial infrastructure. The efficient block finalization provided by Tendermint and the scalable validator set management enabled by DPoS are key enablers of these performance targets.

## Important Details from Source Excerpts

*   Gurufin Chain is a public, permissionless Layer-1 blockchain built on the Cosmos SDK.
*   The native token, GXN, is used for staking, governance, and fee payment.
*   The network is "IBC-first" for interoperability, with an EVM Gateway for Ethereum ecosystem compatibility.
*   The overall Gurufin ecosystem includes the Gurufin Chain and the GX Stablecoin Network, with GX Stablecoins flowing to Gurufin Chain for trading and DeFi activities.