# Tokenomics ($GXN)

GXN is the native utility token for Gurufin Chain. The maximum genesis supply is 100,000,000,000 GXN.

## Core Utility

GXN has four primary roles:

* **Staking** - Secures the DPoS network through validator bonding and delegation.
* **Governance** - Supports voting on protocol upgrades, parameters, and treasury allocations.
* **Fee payment** - Pays transaction fees through the Guru-PEG gas pricing mechanism.
* **Liquidity support** - Supports Guruswap OPRS inventory and FX execution infrastructure where configured by governance or ecosystem policy.

## Total Supply

**Maximum Supply (Genesis):**

$$\text{100,000,000,000 GXN}$$

## Allocation Breakdown

The total supply is distributed across nine categories intended to support network operations, ecosystem growth, validator incentives, contributors, investors, and reserves.

### Table 3 — Token Allocation Breakdown

| No. | Category | Allocated Tokens | Ratio |
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

| Group | Allocated Tokens | Ratio |
| --- | --- | --- |
| Ecosystem & Operations | 55,000,000,000 | 55.00% |
| Team & Advisors | 21,500,000,000 | 21.50% |
| Investment | 15,500,000,000 | 15.50% |
| Governance & Reserve | 8,000,000,000 | 8.00% |

## Economic Sustainability

A governance-defined percentage of collected GXN settlement fees can be permanently removed from circulation through a protocol burn route. For EVM-compatible flows, this may use the designated zero address; for native module accounting, it may use a chain-level burn module or another publicly auditable unspendable address defined by governance.

**How the burn works in practice:** A configurable percentage of each settlement fee is routed to the burn mechanism at the protocol level. The remaining fees are distributed according to validator, delegator, and treasury rules. This creates a transparent link between network activity and token supply reduction.

**Why burn fees?**

The burn mechanism reduces circulating supply over time and ties network usage to supply dynamics. As settlement throughput grows, the amount of GXN burned can increase, depending on active governance parameters.

> **Note:** The burn rate is adjustable by governance. It should be evaluated alongside Node Pool emissions, validator economics, network usage, and treasury requirements.

Validators and delegators are compensated through Node Pool emissions and transaction fee revenue. Burned fees are accounted for separately from validator rewards under the active fee distribution policy.

> Tokenomics parameters describe protocol design and governance-controlled mechanics. They are not a forecast of token price or investment performance.
