# Dual Swap Algorithms

GuruDex employs a sophisticated dual swap algorithm architecture designed to provide optimal service to both retail users and institutional participants. This hybrid approach leverages the strengths of an Automated Market Maker (AMM) model for retail trades and real-time oracle-based pricing for institutions, ensuring efficient, low-slippage swaps across user types.

***

## Retail Swap: AMM (Automated Market Maker)

Retail swaps are powered by an AMM algorithm inspired by Uniswap v3's concentrated liquidity model. This model is optimized for small, frequent trades with decentralized, permissionless access.

### Mathematical Model

At the core is the constant product formula:

\[ x \times y = k \]

Where \(x\) and \(y\) are the reserves of the base and quote stablecoins respectively, and \(k\) is a constant. When a swap occurs, the amounts of tokens added and removed from the pool are adjusted to maintain \(k\) constant.

**Output Amount Calculation:**

The output amount (\(\Delta y\)) after accounting for fees is calculated as:

\[ \Delta y = \frac{y \times \Delta x_{fee}} {x + \Delta x_{fee}} \]

Where:
* \(\Delta x_{fee}\) = the input amount (\(\Delta x\)) minus the dynamic fee.
* \(x\) and \(y\) = the current pool reserves.

**Dynamic Fee Model:**

Fees are adjusted dynamically based on pool imbalance to encourage rebalancing. For every 1% deviation from an ideal 1:1 reserve ratio, the fee increases by approximately 1%.

\[ Fee_{dynamic} = Fee_{base} + (\frac{|x - y|}{x + y} \times 100) \% \]

### Execution Flow

| Step | Action                      | Description                                                                                         |
| ---- | --------------------------- | --------------------------------------------------------------------------------------------------- |
| 1    | **Initiate Swap**           | User submits swap request via DApp. Calls `swap(isBaseToQuote, amountIn, minAmountOut)` function. |
| 2    | **User Verification**       | System verifies user's retail status and checks rate limits via InstitutionalRegistry.             |
| 3    | **Calculate Dynamic Fee**   | Calls `calculateDynamicFee()` to determine fee based on current pool imbalance. Fee increases as pool ratio deviates from 1:1. |
| 4    | **Calculate Output (AMM)**  | Uses AMM formula \(x \times y = k\) to compute output amount after fee deduction: \(\Delta y = \frac{y \times \Delta x_{fee}}{x + \Delta x_{fee}}\) |
| 5    | **Slippage Check**          | Verifies `amountOut >= minAmountOut` to protect user from excessive price impact. Transaction reverts if condition not met. |
| 6    | **Update State**            | Updates pool reserves and accumulates fees. Pool imbalance state also updated.                     |
| 7    | **Transfer Funds**          | Sends calculated output amount to user. Fees transferred to FeeDistributor.                        |
| 8    | **Emit Event**             | Emits transaction complete event for transparency.                                                 |

### Execution Example: Retail User Swap

**Scenario**: User wants to swap 1,000 USGX for KRGX.

1. **Initial State**: 
   - USGX Pool Reserve: 100,000
   - KRGX Pool Reserve: 130,000,000 (assuming USD/KRW rate of 1:1,300)
   - Pool Imbalance: ~0% (balanced state)
   
2. **Dynamic Fee Calculation**:
   - Base Fee: 0.3%
   - Imbalance Adjustment: 0% (balanced pool)
   - Final Fee: 0.3%

3. **Fee Deduction**: 1,000 USGX × 0.997 = 997 USGX

4. **Output Calculation**: 
   - \(\Delta y = \frac{130,000,000 \times 997}{100,000 + 997} \approx 1,286,710\) KRGX

5. **Final Result**: User deposits 1,000 USGX and receives approximately 1,286,710 KRGX.

***

## Institutional Swap: Oracle-Based Pricing

Institutional swaps leverage real-time price oracle networks to support RFQ (Request-for-Quote) style execution with minimal slippage for large trades.

### Mathematical Model

The model for institutional swaps is straightforward, directly applying validated real-time exchange rates provided by oracles.

**Output Amount Calculation:**

\[ amountOut = amountIn \times Price_{oracle} \times (1 - Fee_{inst}) \]

Where:
* \(amountIn\) = input amount.
* \(Price_{oracle}\) = real-time exchange rate provided and validated by the oracle.
* \(Fee_{inst}\) = fixed fee rate configured for the institution (e.g., 0.1%).

**Price Validation Model:**

Oracle prices must be validated on-chain upon submission.

\[ |\frac{Price_{oracle} - Price_{stored}}{Price_{stored}}| \leq Deviation_{max} \]

Additionally, the data timestamp must be more recent than the maximum allowed age (e.g., 5 minutes).

### Execution Flow

| Step | Action                        | Description                                                                                           |
| ---- | ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1    | **Pre-Trade Verification (Off-chain)** | Server-side pre-verification of institution's KYC/AML status, authorization, and limits. Performed off-chain before on-chain transaction. |
| 2    | **Real-time Rate Update**     | Server updates latest exchange rate to `PriceOracle` contract from external API (`updatePrice` function). |
| 3    | **Initiate Swap**             | Institution submits signed transaction request calling `swap(amountIn, oraclePrice)` function.       |
| 4    | **Status Check**              | System verifies institution's active status in `InstitutionalRegistry`. Transaction rejected if not `ACTIVE`. |
| 5    | **Validate Oracle Price (Triple Validation)** | `PriceOracle` contract validates submitted `oraclePrice` through:<br/>- **Time Validation**: Data within max allowed age (e.g., 5 minutes)<br/>- **Deviation Validation**: Price difference within allowed range from previous price<br/>- **Confidence Validation**: Oracle data confidence above threshold |
| 6    | **Limit Check**               | Verifies institution-specific per-transaction limit and daily cumulative volume limit. Transaction rejected if limits exceeded. |
| 7    | **Calculate Output (Oracle-based)** | Computes output amount using validated oracle price and institution-specific fixed fee:<br/>\(amountOut = amountIn \times Price_{oracle} \times (1 - Fee_{inst})\) |
| 8    | **Update State**              | Updates pool reserves and records institution's daily volume. Compliance transaction logs also stored. |
| 9    | **Transfer Funds**            | Sends calculated output amount to institution. Fees transferred to FeeDistributor.                   |
| 10   | **Emit Event**                | Emits institutional transaction complete event for audit trail.                                      |

### Execution Example: Institutional User Swap

**Scenario**: A bank wants to swap 100,000 USGX for KRGX at scale.

1. **Pre-verification (Off-chain)**:
   - KYC/AML Status: ACTIVE
   - Daily Trading Limit: 1,000,000 USGX
   - Current Daily Usage: 200,000 USGX
   - Custom Fee Rate: 0.1%

2. **Oracle Price Update**:
   - External API Rate: 1 USD = 1,300 KRW
   - Oracle Update Time: 2025-11-07 14:30:00
   - Confidence: 99.5%

3. **Price Validation (Triple Check)**:
   - ✅ Time: 2 minutes difference from current time (within 5 minutes)
   - ✅ Deviation: 0.08% difference from previous price (1,299 KRW) (within 2% allowed range)
   - ✅ Confidence: 99.5% (exceeds 95% threshold)

4. **Limit Check**:
   - Transaction Amount: 100,000 USGX
   - Post-transaction Daily Usage: 300,000 USGX (within limit)
   - ✅ Approved

5. **Output Calculation**:
   - \(amountOut = 100,000 \times 1,300 \times (1 - 0.001) = 129,870,000\) KRGX

6. **Final Result**: 
   - Institution deposits 100,000 USGX and receives 129,870,000 KRGX
   - Fee: 130,000 KRGX (0.1%)
   - Slippage: Nearly 0% (oracle price locked)

***

## Comparative Analysis

| Feature                  | Retail AMM                                      | Institutional Oracle Pricing              |
| ------------------------ | ----------------------------------------------- | ----------------------------------------- |
| **Price Determination**  | On-chain liquidity and constant product formula | External real-time oracle price feeds     |
| **Mathematical Complexity** | High (dynamic curves and fees)               | Low (direct multiplication)               |
| **Slippage**             | Variable (depends on trade size)                | Minimized (price locked)                  |
| **Execution Reliability** | High (relies only on on-chain data)            | High (if oracle validation passes)        |
| **Fee Model**            | Dynamic (varies with pool balance)              | Fixed/Custom (typically lower)            |

***

## Algorithm Selection Logic

The FXSwapMaster contract determines which algorithm to use based on the caller's user type:

```solidity
function determineSwapPath(address user) internal view returns (SwapPath) {
    UserType userType = institutionalRegistry.getUserType(user);
    
    if (userType == UserType.INSTITUTIONAL) {
        return SwapPath.ORACLE_BASED;
    } else {
        return SwapPath.AMM;
    }
}
```

This dual-algorithm architecture ensures that each user type receives an optimized trading experience tailored to their specific needs, while maintaining a unified liquidity pool for maximum capital efficiency.

***

## Conclusion

The dual swap algorithm design within GuruDex represents a sophisticated balance between decentralized permissionless trading and institutional-grade execution. By offering AMM-based swaps for retail users and oracle-based pricing for institutions within a single hybrid pool, GuruDex achieves optimal liquidity utilization, minimized slippage, and compliance-ready infrastructure for a global FX trading platform.

For implementation details and smart contract interfaces, please refer to the [Architecture](01_architecture.md) and [Hybrid Pools](02_hybrid_pools.md) documentation.
