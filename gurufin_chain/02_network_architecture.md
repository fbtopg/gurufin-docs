# Network Architecture

This page explains the consensus engine and node structure that powers Gurufin Chain. Understanding these fundamentals helps clarify how the network achieves fast, secure, and final transactions.

---

## Consensus Engine: Tendermint BFT + DPoS

Gurufin Chain uses a **hybrid consensus mechanism** combining two proven technologies:

### Tendermint Byzantine Fault Tolerant (BFT)

Tendermint is the engine that achieves agreement among network validators. It works through a three-phase voting process:

```
Propose → Prevote → Precommit → Block Finalized
```

| Property | Description |
|----------|-------------|
| **Fault Tolerance** | Network remains secure even if up to 1/3 of validators are malicious or offline |
| **Instant Finality** | Once a block is committed, it cannot be reversed (no "confirmations" needed) |
| **Deterministic** | Every validator reaches the same conclusion—no forks or chain reorganizations |

### Delegated Proof-of-Stake (DPoS)

DPoS determines *who* can participate in consensus:

1. **Token Holders** delegate their GXN tokens to validators they trust
2. **Validators** with the most delegated stake form the active validator set
3. **Block Producers** are selected from active validators based on stake weight

This design balances decentralization (anyone can delegate) with performance (limited active validators enable fast consensus).

---

## Node Structure

The network consists of different node types, each serving a specific role:

| Node Type | Role | Who Runs It |
|-----------|------|-------------|
| **Validator Node** | Participates in consensus, produces blocks, votes on proposals | Professional operators with staked GXN |
| **Full Node** | Stores complete blockchain history, relays transactions | Infrastructure providers, developers |
| **Archive Node** | Preserves all historical states for queries | Analytics services, block explorers |
| **Light Client** | Verifies transactions without full chain data | Wallets, mobile apps |

---

## Performance Specifications

| Metric | Specification |
|--------|---------------|
| Block Time | Sub-second (~1 second) |
| Throughput | Up to 10,000 TPS |
| Finality | Immediate (deterministic) |
| Active Validators | Configurable (typically 50-150) |

---

## Security Model

Network security is maintained through economic incentives:

- **Staking Rewards**: Validators and delegators earn rewards for honest participation
- **Slashing Penalties**: Misbehavior (downtime, double-signing) results in stake being "slashed" (partially confiscated)
- **Jail System**: Repeated violations temporarily or permanently remove validators from the active set

This economic model ensures validators have "skin in the game" and are financially motivated to act honestly.
