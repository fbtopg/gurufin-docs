# Validator Guide

Validators maintain consensus, produce blocks, and participate in governance. The active validator set is determined by the amount of GXN bonded directly to a validator and delegated by stakeholders.

**Operational Requirements**

* **Hardware and uptime:** Validators should operate resilient infrastructure with sentry nodes, monitoring, backup procedures, and high-availability networking.
* **Key security:** Validator keys should be protected with hardware security modules (HSMs), multi-party computation (MPC), or equivalent controls, with documented rotation and recovery procedures.
* **Stake:** A minimum GXN bond is required to register as a validator candidate. The threshold is set by governance.
* **Operational process:** Validators should maintain incident response, upgrade, and communication procedures suitable for production network operations.

**Slashing & Penalties**

Consensus accountability is enforced through slashing and jailing:

* **Downtime:** Failure to sign required blocks can result in partial stake slashing and temporary jailing.
* **Double-signing:** Signing conflicting blocks at the same height can result in severe slashing and permanent tombstoning.

**Rewards**

Validators earn rewards from Node Pool emissions and transaction fee revenue. Delegators receive a proportional share of validator rewards after validator commission is applied.

**Economic Sustainability**

Operating enterprise-grade validator infrastructure requires sustainable economics. Validator revenue can come from three sources:

1. **Node Pool emissions:** Block rewards from the Node Pool allocation, distributed to active validators and delegators according to network rules.
2. **Transaction fees:** Predictable, fiat-indexed fees can create recurring revenue as enterprise transaction volume grows.
3. **Institutional services:** Validators may offer uptime reporting, compliance reporting, or service-level agreements to institutional clients where permitted.

Delegation does not remove operational risk. Delegators should evaluate validator performance, commission policy, security practices, and governance behavior before assigning stake.
