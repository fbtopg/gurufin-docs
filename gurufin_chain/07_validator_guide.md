# Validator Guide

Validators are the backbone of Gurufin Chain's security and consensus, operating nodes that produce blocks, validate transactions, and participate in governance decisions. Becoming a validator requires meeting **hardware specifications** to ensure reliable network performance, satisfying **staking requirements** by bonding GXN tokens as collateral, and adhering to **operational standards** including high uptime and honest behavior—violations of which result in **slashing penalties** where a portion of staked tokens is confiscated. Validators are elected through a stake-weighted voting process where token holders delegate their GXN to trusted candidates, and the top validators by total stake form the active validator set responsible for maintaining the network.

---

## Requirements Overview

| Requirement | Description |
|-------------|-------------|
| **Hardware** | Enterprise-grade server with high CPU, memory, and storage specifications |
| **Stake** | Minimum GXN bond required to register as a validator candidate |
| **Uptime** | Maintain high availability (99%+ recommended) |
| **Security** | Secure key management and infrastructure practices |

---

## Slashing Conditions

| Violation | Consequence |
|-----------|-------------|
| **Downtime** | Partial stake slash for extended unavailability |
| **Double-Signing** | Severe slash and permanent removal for signing conflicting blocks |
| **Governance Abuse** | Penalties for malicious proposal or voting behavior |

---

## Rewards

Validators earn rewards from:
- Block production rewards (newly minted GXN)
- Transaction fee distribution
- Delegator commission fees

---

*This page provides an introductory overview. Detailed hardware specifications, setup instructions, and operational best practices will be added in future documentation updates.*
