# Validator Guide

Validators are the backbone of Gurufin Chain's security and consensus, operating nodes that produce blocks, validate transactions, and participate in governance decisions. Becoming a validator requires meeting hardware specifications to ensure reliable network performance, satisfying staking requirements by bonding GXN tokens as collateral, and adhering to operational standards including high uptime and honest behavior.

Validators are elected through a stake-weighted voting process where token holders delegate their GXN to trusted candidates, and the top validators by total stake form the active validator set responsible for maintaining the network.

---

**Requirements**

* **Hardware** — Enterprise-grade server with specifications published by the network
* **Stake** — Minimum GXN bond required to register as a validator candidate (threshold set by governance)
* **Uptime** — Maintain high availability with sentry node architecture for DDoS protection
* **Security** — Key material held in HSMs or managed via Multi-Party Computation (MPC) with threshold signatures; rotation policies and break-glass procedures required

---

**Slashing & Jailing**

Violations result in slashing penalties where a portion of staked tokens is confiscated. Extended downtime causes partial stake slash and temporary jailing (exclusion from the active set). Double-signing (equivocation) results in severe slash and permanent jailing for signing conflicting blocks. Un-jailing requires liveness proofs; repeat offenders face extended quarantines.

---

**Rewards**

Validators earn rewards from the Node Pool emissions (25% of total supply allocated for staking rewards) plus an increasing share of transaction fee revenue as network usage grows. Delegators share in these rewards proportionally, minus the validator's commission rate.

---

*This page provides an introductory overview. Detailed hardware specifications, setup instructions, and operational best practices will be added in future documentation updates.*
