# Validator Guide

Validators maintain network consensus, secure the chain, and execute governance decisions. The active set is determined by the total amount of GXN delegated to a node.

**Operational Requirements**
* **Hardware & Uptime:** Enterprise-grade servers configured with sentry node architecture to mitigate DDoS vectors and ensure high availability.
* **Security:** Key materials must be secured via HSMs or Multi-Party Computation (MPC) with strict rotation policies.
* **Stake:** A minimum GXN bond is required to register as a validator candidate (threshold set by governance).

**Slashing & Penalties**
Security is enforced through economic penalties (slashing) and removal from the active set (jailing).
* **Downtime:** Failing to sign blocks results in a partial stake slash and temporary jailing.
* **Double-Signing:** Signing conflicting blocks at the same height results in a severe stake slash and permanent tombstoning from the network.

**Rewards**
Validators earn rewards from the Node Pool emissions (25% of total supply) and an increasing share of transaction fee revenue. Delegators share these rewards proportionally, minus the validator's commission rate.
