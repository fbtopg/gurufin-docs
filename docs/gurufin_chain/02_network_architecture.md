# Network Architecture

This page explains the consensus engine and node structure that powers Gurufin Chain. Understanding these fundamentals helps clarify how the network achieves fast, secure, and final transactions.

---

**Consensus Engine: Tendermint BFT + DPoS**

Gurufin Chain uses a hybrid consensus mechanism combining two proven technologies. Tendermint Byzantine Fault Tolerant (BFT) is the engine that achieves agreement among network validators through a three-phase voting process: Propose, Prevote, Precommit, and Block Finalized. The network remains secure even if up to one-third of validators are malicious or offline, and once a block is committed, it cannot be reversed—no confirmations needed.

Delegated Proof-of-Stake (DPoS) determines who can participate in consensus. Token holders delegate their GXN tokens to validators they trust, validators with the most delegated stake form the active validator set, and block producers are selected based on stake weight. This design balances decentralization with performance.

---

**Node Types**

The network consists of different node types, each serving a specific role:

* **Validator Node** — Participates in consensus, produces blocks, and votes on proposals. Run by professional operators with staked GXN.
* **Full Node** — Stores complete blockchain history and relays transactions. Run by infrastructure providers and developers.
* **Archive Node** — Preserves all historical states for queries. Run by analytics services and block explorers.
* **Light Client** — Verifies transactions without full chain data. Used by wallets and mobile apps.

---

**Performance**

Gurufin Chain targets sub-second block times with throughput of up to 10,000 TPS and immediate deterministic finality. The active validator set is configurable, typically ranging from 50 to 150 validators depending on network governance decisions.

---

**Security Model**

Network security is maintained through economic incentives. Validators and delegators earn staking rewards for honest participation, while misbehavior such as downtime or double-signing results in slashing penalties where a portion of staked tokens is confiscated. Repeated violations temporarily or permanently remove validators from the active set through a jail system. This ensures validators have "skin in the game" and are financially motivated to act honestly.
