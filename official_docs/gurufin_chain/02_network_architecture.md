# Network Architecture

Gurufin Chain targets sub-second block times with up to 10,000 TPS using a hybrid consensus mechanism. 

**Consensus Engine: Tendermint BFT + DPoS**
Tendermint Byzantine Fault Tolerant (BFT) achieves agreement through a three-phase voting process: Propose, Prevote, and Precommit. The network tolerates up to one-third of validators being offline or malicious. Block finality is immediate and deterministic. 

Delegated Proof-of-Stake (DPoS) determines consensus participation. Token holders delegate GXN to validators, and block producers are selected based on total stake weight.

**Node Types**
* **Validator Node:** Participates in consensus and block production. Requires staked GXN.
* **Full Node:** Stores complete blockchain history and relays transactions.
* **Archive Node:** Preserves all historical states for complex querying.
* **Light Client:** Verifies transactions cryptographically without downloading full chain data.
