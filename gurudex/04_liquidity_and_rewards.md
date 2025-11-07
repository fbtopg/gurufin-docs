# Liquidity & Rewards

This section provides a comprehensive overview of liquidity provision, LP token mechanics, fee accumulation, and reward distribution within the FXSwap platform. Designed to facilitate efficient FX stablecoin swaps for both retail and institutional users, FXSwap is architected to leverage a hybrid liquidity pool architecture and dynamic fee mechanisms to optimize trading experience and incentivize liquidity providers.

---

## Providing Liquidity

Liquidity provision in FXSwap is designed to enable seamless swaps between planned sovereign stablecoins such as USGX (USD-pegged), KRGX (KRW-pegged), JPGX (JPY-pegged), and PHGX (PHP-pegged). Each stablecoin pair will be served by a **single hybrid liquidity pool**, which integrates both retail and institutional liquidity to maximize depth and efficiency.

### Virtual-Pair Mechanism

FXSwap's liquidity is provided through a unique mechanism called **Virtual-Pair**. This is an innovative approach that distinguishes itself from traditional Pair Pool methods:

**Problems with Traditional Pair Pool Approach**:
- Requires separate pools for every currency pair (USGX-KRGX, USGX-JPGX, KRGX-JPGX, etc.)
- For n currencies, requires n×(n-1)/2 pools (e.g., 4 currencies = 6 pools)
- Liquidity fragmentation reduces capital efficiency
- Increased management and deployment costs

**Advantages of Virtual-Pair Approach**:
- Creates only a **single pool** per stablecoin
- Users provide liquidity simultaneously to two different single pools
- Managed through one **Virtual LP Token**
- For n currencies, only n pools needed (e.g., 4 currencies = 4 pools)
- Concentrated liquidity maximizes capital efficiency
- Management complexity reduced by approximately 66%

### How to Add Liquidity (Virtual-Pair Based)

Liquidity addition using the Virtual-Pair mechanism follows this process:

**Example: Providing Liquidity for USGX-KRGX Trading Pair**

1. **Simultaneous Deposit to Two Single Pools**:
   - LP deposits 1,000 USGX to USGX pool
   - Simultaneously deposits 1,300,000 KRGX to KRGX pool

2. **Virtual LP Token Issuance**:
   - Virtual LP tokens issued based on value of both assets
   - First liquidity addition:
     \[
     \text{virtualLP} = \sqrt{\text{amount}_{\text{USGX}} \times \text{amount}_{\text{KRGX}}}
     \]
   - Subsequent liquidity additions:
     \[
     \text{virtualLP} = \min\left(\frac{\text{amount}_{\text{USGX}}}{\text{reserve}_{\text{USGX}}}, \frac{\text{amount}_{\text{KRGX}}}{\text{reserve}_{\text{KRGX}}}\right) \times \text{totalVirtualLP}
     \]

3. **Stake Management**:
   - One Virtual LP token represents stakes in both pools
   - Fee revenue generated from both pools distributed to LP

**Liquidity Removal (`removeLiquidity`)**:
- When LP burns Virtual LP tokens
- Simultaneously withdraws assets from both pools proportional to stake
- Also receives accumulated fee rewards

This approach allows LPs to efficiently provide liquidity to multiple currency pairs without complex management.

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

Reward distribution to liquidity providers is managed through the **FeeDistributor** contract and occurs in discrete 24-hour cycles, ensuring timely and predictable compensation for liquidity provision.

### FeeDistributor Role

**FeeDistributor** is a dedicated contract that collects swap fees generated and distributes them fairly to liquidity providers (LPs) according to their shares:

- **Fee Collection**: Automatically collects fees from all HybridStablePool instances
- **Segregated Accounting**: Separately tracks retail pool fees and institutional pool fees
- **Proportional Distribution**: Calculates rewards precisely proportional to LP token holdings
- **Efficient Claiming**: Gas-efficient batch distribution and claiming mechanism

### Distribution Workflow

1. **Fee Accumulation**: 
   - Swap fees generated from each pool over 24 hours
   - FeeDistributor tracks fees in real-time
   - Retail transaction fees and institutional transaction fees recorded separately

2. **Distribution Execution**: 
   - At end of each cycle, `distributeRewards()` function executed automatically
   - Or manually executed by governance/operator
   - Fees allocated proportionally to LP token holders

3. **Share Calculation**: 
   - Each LP's reward share calculated based on LP token balance relative to total liquidity:
   \[
   \text{reward}_{\text{LP}} = \text{totalFees} \times \frac{\text{lpTokens}_{\text{LP}}}{\text{totalLPTokens}}
   \]

4. **Reward Allocation**: 
   - Calculated rewards credited to each LP's **accumulatedRewards** balance
   - Transparently recorded on-chain for verification

5. **Claiming Rewards**: 
   - LPs can claim rewards anytime via `claimRewards()` function
   - Withdraw accumulated fee share to their wallet
   - Can batch claim rewards from multiple pools to save gas costs

### Fee Distribution Example

**Scenario**: Over 24 hours, USGX-KRGX pool generates 1,000 USGX worth of fees

- **LP A**: Holds 10,000 Virtual LP tokens (40% of total)
  - Reward: 400 USGX worth
  
- **LP B**: Holds 7,500 Virtual LP tokens (30% of total)
  - Reward: 300 USGX worth
  
- **LP C**: Holds 5,000 Virtual LP tokens (20% of total)
  - Reward: 200 USGX worth
  
- **Other LPs**: Hold 2,500 Virtual LP tokens (10% of total)
  - Reward: 100 USGX worth

Each LP receives fees exactly proportional to their stake.

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

The FXSwap liquidity and rewards system is engineered to provide a robust, efficient, and fair environment for liquidity providers. By combining hybrid pools, dynamic fees, and transparent reward cycles, FXSwap is designed to deliver deep liquidity, minimized slippage, and consistent incentives aligned with the interests of both retail and institutional participants. This design supports the broader Gurufin Chain vision of a global, interoperable FX and DeFi hub anchored by sovereign stablecoins.