# Governance

Gurufin Chain utilizes an on-chain governance system where native token holders and validators propose, vote on, and execute network upgrades and parameter changes.

**Governance Parameters**
The protocol enforces strict, hardcoded parameters to ensure rapid but secure decision-making:
* **Voting Period:** Exactly **14 Days**. (This aligns with efficient network agility while allowing sufficient time for stakeholder review).
* **Quorum Requirement:** **33.4%**. (At least 33.4% of the total staked voting power must participate for a proposal to be considered valid).
* **Timelock:** **Phase 1 — None**. (If a proposal achieves quorum and passes the voting threshold, it is executed immediately upon the conclusion of the voting period). This is a deliberate tradeoff for rapid iteration during the testnet phase. Institutional users should note that this does not apply to treasury allocations exceeding 1% of reserves, which require supermajority quorum and can trigger a separate emergency pause mechanism.

**Phase 2 Timelock Upgrade**
For mainnet, the protocol is designed to introduce a configurable timelock (typically 24–72 hours) between proposal passage and execution. This will provide a final window for users to withdraw or hedge against unexpected parameter changes, addressing a key concern of institutional participants. The timelock mechanism and duration will be set by governance before mainnet launch.

**Delegated Voting**
Users who delegate their tokens to a validator inherit that validator's vote by default. However, delegators retain the right to override their validator's decision by casting an individual vote on any active proposal.

**Proposal Types**
| Type | Description | Execution |
|------|-------------|-----------|
| **Parameter Change** | Adjusts network parameters (e.g., gas pricing, validator limits) | Immediate (Phase 1) / Timelocked (Phase 2) |
| **Software Upgrade** | Proposes a network-wide software version upgrade | Requires supermajority quorum |
| **Treasury Allocation** | Directs funds from the Ecosystem or Governance reserve | Requires supermajority quorum |
| **Text Proposal** | Non-binding community sentiment gauge | Informational only |

**Quorum and Threshold**
* **Standard proposals** require a simple majority (>50%) of votes cast, with the 33.4% quorum floor.
* **Software upgrades** require a supermajority (>66%) to account for the critical nature of consensus-level changes.
* **Treasury allocations** exceeding 1% of total reserves require a supermajority (>66%) and a separate emergency pause mechanism.

**Emergency Governance**
In the event of a critical security incident, the validator set may trigger an emergency pause through a simplified fast-track proposal (24-hour voting window). This mechanism is gated by a minimum of 66% validator agreement and is automatically reviewed by the Gurufin Foundation's security team.
