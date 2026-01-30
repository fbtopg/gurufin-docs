# Governance

Gurufin Chain employs a robust on-chain governance framework that enables decentralized decision-making through the collective participation of validators and token holders. The governance system leverages the Delegated Proof-of-Stake (DPoS) consensus mechanism, where validators are elected by token holders to represent the network in consensus and voting, while delegators participate indirectly by delegating their stake to trusted validators and sharing in both rewards and responsibilities.

The proposal lifecycle follows a structured process—from submission with deposit requirements, through a voting period where participants can vote Yes, No, Abstain, or No with Veto, to automatic execution upon approval—ensuring all protocol changes are transparently recorded and enacted on-chain.

---

**Governance Participants**

* **Validators** — Elected nodes responsible for block production and governance voting
* **Delegators** — Token holders who delegate stake to validators, gaining indirect voting power

---

**Proposal Types**

* **Parameter Changes** — Fee adjustments, staking requirements, consensus configurations
* **Protocol Upgrades** — New features, module additions, security patches
* **Treasury Allocation** — Development grants, marketing funds, community incentives

---

**Voting & Timelocks**

Standard proposals follow a 7-day voting window with a 72-hour timelock before execution. Parameter changes require a quorum of 10–20% of bonded voting power with >50% yes votes. Economic changes and chain upgrades require higher thresholds (up to 40% quorum and ≥66.7% supermajority for hard forks). A "No with Veto" option allows ≥33.4% to reject proposals outright.

---

**Emergency Controls**

A Security Council (n-of-m multisig with external members) holds narrowly scoped, time-bounded emergency powers for operational safety—such as freezing affected pairs during oracle degradation or pausing specific routes on extreme basis divergence. Emergency actions auto-expire within 72 hours unless ratified by token vote, and all actions are logged with mandatory post-mortem disclosure.

---

*This page provides an introductory overview. Detailed governance procedures and deposit requirements will be added in future documentation updates.*
