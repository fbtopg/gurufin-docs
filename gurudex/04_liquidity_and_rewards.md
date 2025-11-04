# Liquidity & Rewards

This section provides a comprehensive overview of liquidity provision, LP token mechanics, fee accumulation, and reward distribution within the FXSwap platform. Designed to facilitate efficient FX stablecoin swaps for both retail and institutional users, FXSwap leverages a hybrid liquidity pool architecture and dynamic fee mechanisms to optimize trading experience and incentivize liquidity providers.

---

## Providing Liquidity

Liquidity provision in FXSwap is fundamental to enabling seamless swaps between supported sovereign stablecoins such as USGX (USD-pegged), KRGX (KRW-pegged), JPGX (JPY-pegged), and PHGX (PHP-pegged). Each stablecoin pair is served by a **single hybrid liquidity pool**, which integrates both retail and institutional liquidity to maximize depth and efficiency.

### How to Add Liquidity

Liquidity providers (LPs) contribute assets in pairs corresponding to the base and quote stablecoins of the pool. The process differs slightly depending on whether liquidity is being added for the first time or to an existing pool:

- **First Liquidity Addition**: When a pool is initialized, the liquidity amount is calculated as the geometric mean of the base and quote coin amounts provided:

  \[
  \text{liquidity} = \sqrt{\text{baseAmount} \times \text{quoteAmount}}
  \]

- **Subsequent Liquidity Additions**: For existing pools, liquidity is minted proportionally based on the ratio of the amounts added relative to current reserves:

  \[
  \text{liquidity} = \min\left(\frac{\text{baseAmount}}{\text{baseReserve}}, \frac{\text{quoteAmount}}{\text{quoteReserve}}\right) \times \text{totalLiquidity}
  \]

Upon successful liquidity addition, LPs receive **LP tokens** representing their share of the pool.

### Hybrid Pool Design

FXSwap employs a **hybrid pool** model that consolidates institutional and retail liquidity within a single pool per stablecoin pair. This design offers several advantages:

- **Liquidity Maximization**: Combining both user types results in deeper liquidity and reduced slippage.
- **Operational Efficiency**: Single pool management reduces complexity and deployment costs.
- **Internal Separation**: Balances for institutional and retail participants are tracked separately within the pool to maintain privacy and compliance.

---

## LP Token Mechanics

Liquidity providers receive LP tokens proportional to their contribution to the pool. These tokens serve as proof of ownership and entitle holders to a share of the accumulated swap fees and rewards.

### Key Characteristics of LP Tokens

| Feature               | Description                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------|
| **Representation**    | Non-transferable tokens representing proportional ownership of the liquidity pool               |
| **Minting**           | Issued upon liquidity addition based on contribution relative to pool reserves                  |
| **Burning**           | Redeemed when liquidity is withdrawn, reducing the provider’s share accordingly                 |
| **Reward Eligibility**| Holders accumulate a proportional share of swap fees and rewards based on LP token holdings    |

LP tokens are essential for tracking liquidity shares and calculating reward entitlements during distribution cycles.

---

## Fee Accumulation

FXSwap generates fees from every swap transaction executed within the pools. These fees serve multiple purposes: incentivizing liquidity provision, maintaining pool equilibrium, and covering operational costs.

### Fee Structure

- **Retail Users**: Fees are dynamically calculated based on pool imbalance, following a Uniswap v3 style AMM model. The fee rate increases by 1% for every 1% deviation from a balanced 1:1 liquidity ratio between base and quote assets. This dynamic fee mechanism encourages rebalancing and protects against adverse selection.

- **Institutional Users**: Fees are fixed, typically around 0.1%, applied on real-time exchange rate-based swaps. Institutional fees are lower to accommodate large-volume trades with minimal slippage.

### Fee Accumulation Process

Fees collected from swaps are accumulated in the pool’s **accumulatedFees** reserve. This reserve grows continuously as trading activity occurs and forms the basis for subsequent reward distributions to LPs.

---

## Reward Distribution

Reward distribution to liquidity providers occurs in discrete 24-hour cycles, ensuring timely and predictable compensation for liquidity provision.

### Distribution Workflow

1. **Fee Accumulation**: Throughout the 24-hour period, swap fees accumulate in the pool’s fee reserve.
2. **Distribution Execution**: At the end of each cycle, the `distributeRewards()` function is executed to allocate fees proportionally to LP token holders.
3. **Share Calculation**: Each LP’s reward share is calculated based on their LP token balance relative to the total liquidity:

   \[
   \text{share} = \text{accumulatedFees} \times \frac{\text{lpTokens}}{\text{totalLiquidity}}
   \]

4. **Reward Allocation**: The calculated rewards are credited to each LP’s **accumulatedRewards** balance.
5. **Claiming Rewards**: LPs can claim their rewards at any time via the `claimRewards()` function, receiving their share of accumulated fees.

### Reward Distribution Table

| Step                  | Description                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------|
| **1. Accumulate Fees**| Swap fees collected over 24 hours are stored in the pool’s fee reserve                       |
| **2. Calculate Shares**| LP shares computed based on LP token holdings relative to total liquidity                   |
| **3. Allocate Rewards**| Rewards credited to LPs’ accumulated reward balances                                        |
| **4. Claim Rewards**   | LPs withdraw their rewards on-demand                                                        |

---

## Summary Table: Liquidity & Rewards Lifecycle

| Aspect                | Description                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------|
| **Liquidity Provision**| Add base and quote stablecoins to the pool; receive LP tokens proportional to contribution     |
| **LP Tokens**          | Represent ownership share; minted on deposit, burned on withdrawal                             |
| **Fee Generation**     | Swap transactions incur dynamic (retail) or fixed (institutional) fees, accumulating in pool   |
| **Dynamic Fee Model**  | Retail fees increase with pool imbalance to incentivize equilibrium                            |
| **Reward Cycle**       | Fees distributed every 24 hours based on LP token shares                                      |
| **Reward Claiming**    | LPs can claim accumulated rewards anytime after distribution                                  |

---

## Conclusion

The FXSwap liquidity and rewards system is engineered to provide a robust, efficient, and fair environment for liquidity providers. By combining hybrid pools, dynamic fees, and transparent reward cycles, FXSwap ensures deep liquidity, minimized slippage, and consistent incentives aligned with the interests of both retail and institutional participants. This design supports the broader Gurufin Chain vision of a global, interoperable FX and DeFi hub anchored by sovereign stablecoins.