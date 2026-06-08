# Tokenomics ($GXN)

GXN is the native utility token powering Gurufin Chain. The maximum supply at genesis is 100,000,000,000 GXN.

## Core Utility

GXN serves four primary functions within the Gurufin ecosystem:

* **Staking** — Securing the DPoS network via validator delegation.
* **Governance** — Voting on protocol upgrades and treasury allocations.
* **Fee Payment** — Execution of network settlement activity via GXN-PEG.
* **Liquidity** — Provisioning for the Guruswap OPRS FX execution infrastructure.

## Total Supply

**Maximum Supply (Genesis):**

$$\text{100,000,000,000 GXN}$$

## Allocation Breakdown

The total supply is distributed across nine categories, designed to align incentives among validators, investors, and the broader ecosystem.

### Table 3 — Token Allocation Breakdown

| No. | Category | Allocated Token | Ratio |
| --- | --- | --- | --- |
| 1 | Ecosystem Funds | 27,000,000,000 | 27.00% |
| 2 | Network Operations | 3,000,000,000 | 3.00% |
| 3 | Node Pool | 25,000,000,000 | 25.00% |
| 4 | Team & Developers | 19,500,000,000 | 19.50% |
| 5 | Advisors | 2,000,000,000 | 2.00% |
| 6 | Gurufin Foundation | 5,000,000,000 | 5.00% |
| 7 | Early Ecosystem Investment | 3,000,000,000 | 3.00% |
| 8 | Strategic Investment | 12,500,000,000 | 12.50% |
| 9 | Reserve | 3,000,000,000 | 3.00% |

### Allocation by Group

| Group | Allocated Token | Ratio |
| --- | --- | --- |
| Ecosystem & Operations | 55,000,000,000 | 55.00% |
| Team & Advisors | 21,500,000,000 | 21.50% |
| Investment | 15,500,000,000 | 15.50% |
| Governance & Reserve | 8,000,000,000 | 8.00% |

## Economic Sustainability

A percentage of all collected GXN settlement fees is permanently burned by routing it to the **Gurufin Abyss Ledger (GAL)**, a keyless on-chain address that functions as a provably unspendable "burn address." The GAL is a deterministic, publicly auditable address whose private key is mathematically derivable but computationally infeasible to reconstruct. When GXN is sent to GAL, it is removed from circulation forever, creating deflationary pressure that scales with network utilization.

**How the Burn Works in Practice:** A configurable percentage (set by governance) of each settlement fee is automatically routed to GAL at the protocol level. The remaining fees are distributed to validators and delegators. This means the burn operates transparently and continuously — every settlement on the chain contributes to the deflationary mechanism.

**Why a Burn Address?**
The burn mechanism reduces the circulating supply over time, aligning long-term network utilization with network value accrual. As settlement throughput grows, more GXN is burned, creating a natural feedback loop between network throughput volume and supply dynamics.

> **Note:** The burn rate is dynamically adjustable by governance based on network health. During periods of high inflationary pressure from Node Pool emissions, governance may increase the burn percentage to maintain deflationary balance.

Validators and delegators are compensated via the Node Pool and an increasing share of network settlement fees. Burned fees are separate from validator rewards and do not reduce their earnings.
