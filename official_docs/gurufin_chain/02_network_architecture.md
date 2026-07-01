# Network Architecture

Gurufin Chain uses a Cosmos-based architecture with deterministic consensus, delegated validator participation, and modular node roles. The network targets sub-second block times and high-throughput settlement workloads, with final benchmark figures subject to public testing and mainnet readiness reviews.

**Consensus Engine: Tendermint BFT + DPoS**

Tendermint Byzantine Fault Tolerant (BFT) consensus reaches agreement through a three-phase voting process: propose, prevote, and precommit. Under standard BFT assumptions, the network can preserve safety if less than one-third of voting power is Byzantine.

Delegated Proof-of-Stake (DPoS) determines consensus participation. Stakeholders delegate GXN to validators, and validator voting power is weighted by total delegated stake. Once a block is committed by the required validator quorum, finality is deterministic under the chain's consensus rules.

**Node Types**

* **Validator node:** Participates in consensus and block production. Validator candidacy requires a GXN bond and compliance with network operating requirements.
* **Full node:** Stores blockchain history, verifies blocks, and relays transactions.
* **Archive node:** Preserves historical state for analytics, compliance review, and complex queries.
* **Light client:** Verifies headers and proofs without downloading the full chain state.

Production deployments should evaluate validator distribution, network latency, monitoring, key management, and recovery procedures alongside raw throughput targets.
