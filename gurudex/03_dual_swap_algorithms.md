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
| 1    | **Initiate Swap**           | User calls `swap(isBaseToQuote, amountIn, minAmountOut)` function.                                |
| 2    | **User Verification**       | System verifies user's retail status and checks rate limits.                                       |
| 3    | **Calculate Dynamic Fee**   | Calls `calculateDynamicFee()` to determine fee based on current pool imbalance.                    |
| 4    | **Calculate Output**        | Uses AMM formula to compute output amount after fee deduction.                                     |
| 5    | **Slippage Check**          | Verifies `amountOut >= minAmountOut` to protect user from excessive price impact.                 |
| 6    | **Update State**            | Updates pool reserves and accumulates fees.                                                        |
| 7    | **Transfer Funds**          | Sends calculated output amount to user.                                                            |

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
| 1    | **Pre-Trade Verification**    | Server-side pre-verification of institution's KYC/AML status, authorization, and limits.             |
| 2    | **Initiate Swap**             | Institution calls `swap(amountIn, oraclePrice)` function.                                            |
| 3    | **Status Check**              | System verifies institution's active status in `InstitutionalRegistry`.                              |
| 4    | **Validate Oracle Price**     | `PriceOracle` contract validates that submitted `oraclePrice` is within allowed deviation and age.   |
| 5    | **Limit Check**               | Verifies per-transaction and daily volume limits.                                                    |
| 6    | **Calculate Output**          | Computes output amount using validated oracle price and fixed fee.                                   |
| 7    | **Update State**              | Updates pool reserves and records institution's transaction volume.                                  |
| 8    | **Transfer Funds**            | Sends calculated output amount to institution.                                                       |

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
