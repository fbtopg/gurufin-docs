# Liquidity & Rewards

The "Liquidity & Rewards" module on GuruDex is designed to incentivize users to provide liquidity to its trading pools through a transparent system of fee distribution and additional rewards. This mechanism ensures deep liquidity for seamless trading of stablecoins while fairly compensating liquidity providers (LPs).

## Key Concepts

The system is built upon several interconnected concepts:

### Fee Structure
GuruDex employs a dynamic fee structure tailored to different user types:
*   **Retail trades**: Incur a base fee of 0.3% which can dynamically increase with pool imbalance, plus an additional 0.05% protocol fee.
*   **Institutional trades**: Benefit from a fixed fee of 0.1% plus a 0.05% protocol fee.

These fees accumulate continuously and are proportionally distributed to LP token holders via the `FeeDistributor` contract, acting as a primary incentive for liquidity provision.

### Reward Distribution
Beyond swap fees, LPs also receive additional rewards, calculated and allocated every 24 hours based on their LP token holdings. To ensure regulatory compliance and maintain fairness, a specific cap is applied:
*   **Institutional trades**: Annual returns for institutional LPs are capped at 7%.
*   **Retail trades**: Any excess rewards exceeding the 7% cap for institutional LPs are redistributed to retail LPs, aiming to provide higher expected returns for individual participants.

### Virtual-Pair Mechanism
To simplify the process of providing liquidity, GuruDex introduces a **Virtual-Pair Mechanism**. LPs deposit stablecoins into two single-coin pools simultaneously but manage their stake through a single, unified "Virtual LP token." This abstraction allows LPs to manage multi-currency liquidity provisions without the complexity of handling separate LP positions for each individual trading pair. Instead, one Virtual LP token represents their stakes in both underlying pools.

## Relationship to Other Concepts

*   **Virtual-Pair Mechanism**: Directly informs how LPs interact with the system, simplifying liquidity provision.
*   **Fee Structure**: Defines the primary income stream for LPs, with differentiated rates for retail and institutional traders.
*   **Retail trades & Institutional trades**: These two categories of users are fundamentally linked to the fee structure and reward distribution models, with distinct rates and reward caps.
*   **Reward Distribution**: Is the mechanism through which additional incentives are provided to LPs, distinct from the collected swap fees, and includes specific rules for institutional vs. retail participants.

## Important Details

*   Liquidity providers deposit stablecoins into pools.
*   LPs earn proportional shares of collected swap fees.
*   Rewards are distributed in regular 24-hour cycles.
*   The `FeeDistributor` contract handles fee distribution.
*   Institutional LP returns are capped at 7% annually.
*   Excess institutional rewards are reallocated to retail LPs.