# Governance

Gurufin Chain uses on-chain governance for protocol upgrades, parameter changes, treasury decisions, and network policy updates. Validators and delegated stakeholders participate through stake-weighted voting.

**Governance Parameters**

Current governance parameters are designed for the testnet and early network phases. Mainnet parameters may change after additional testing, audits, legal review, and governance review.

* **Voting period:** **14 days**.
* **Quorum requirement:** **33.4%** of total staked voting power must participate for a proposal to be valid.
* **Timelock:** **Phase 1 - none.** If a proposal reaches quorum and passes the voting threshold, it executes at the end of the voting period.

The absence of a timelock is a testnet tradeoff that supports faster iteration. Before mainnet, governance is expected to review whether configurable timelocks should apply to sensitive proposal types so counterparties and protocols have time to respond to material parameter changes.

**Delegated Voting**

Delegators inherit their validator's vote by default. They can override that vote by casting their own vote on any active proposal before the voting period ends.

**Proposal Types**

| Type | Description | Execution |
|------|-------------|-----------|
| **Parameter Change** | Adjusts network parameters, such as gas pricing or validator limits. | Immediate in Phase 1; future timelock settings subject to governance. |
| **Software Upgrade** | Proposes a network-wide software version upgrade. | Requires a supermajority threshold. |
| **Treasury Allocation** | Directs funds from ecosystem or governance reserves. | Requires a supermajority threshold for large allocations. |
| **Text Proposal** | Records non-binding community or stakeholder sentiment. | Informational only. |

**Quorum and Threshold**
* **Standard proposals** require a simple majority of votes cast, subject to the 33.4% quorum floor.
* **Software upgrades** require a supermajority threshold because they can affect consensus behavior.
* **Treasury allocations** exceeding 1% of total reserves require a supermajority threshold and additional review controls.

**Emergency Governance**

In a critical security incident, the validator set may initiate an emergency pause through a fast-track proposal with a shorter voting window. This mechanism requires at least 66% validator agreement and triggers review by the Gurufin Foundation security team.

Emergency governance is intended for security and operational continuity, not routine parameter management.
