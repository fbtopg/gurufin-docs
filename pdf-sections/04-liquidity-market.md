# Liquidity and Market Structure

## Virtual-Pair Mechanism

GuruDex introduces an innovative Virtual-Pair Mechanism that simplifies multi-currency liquidity provision. Instead of managing separate LP positions for each pair, liquidity providers use a single Virtual LP token that represents stakes in both underlying pools.

### How Virtual-Pair Works

**Traditional LP Model:**
- LP provides liquidity to USGX/KRGX pool
- LP receives USGX-KRGX LP tokens
- LP must manage separate positions for each pair

**Virtual-Pair Model:**
- LP provides liquidity to two single-coin pools simultaneously
- LP receives a single Virtual LP token
- The Virtual LP token represents proportional stake in both pools
- One unified position manages exposure across multiple pairs

### Benefits of Virtual-Pair

**Simplified Management**
One token represents all positions, reducing complexity for liquidity providers.

**Dynamic Rebalancing**
The system automatically rebalances exposure based on pool conditions.

**Reduced Gas Costs**
Single transaction manages multiple pool positions.

**Unified Rewards**
Fees from all represented pools accumulate in one position.

---

## Hybrid Pools: Retail + Institutional Liquidity

GuruDex combines retail and institutional liquidity into hybrid pools, optimizing execution quality for all user types.

### Pool Architecture

**Retail Layer (AMM)**
- Constant-function market maker with stable-swap curve
- Optimized for small to medium trades
- Always-on liquidity
- Dynamic fees based on pool utilization

**Institutional Layer (RFQ)**
- Request-for-Quote execution for large tickets
- Custom pricing from professional market makers
- Minimal slippage for block trades
- Oracle-verified pricing

### Pool Topology

Gurufin organizes liquidity around Cosmos-native Settlement Module (CSM) pools:

**Foundational Pools (CSM Pools)**
- ibc/<hash_uusgx> ↔ GXN
- ibc/<hash_uusdc> ↔ GXN
- gwUSDC ↔ GXN (where enabled)

**Direct Stablecoin Pools**
- ibc/<hash_uusgx> ↔ ibc/<hash_ukrgx>
- ibc/<hash_uusgx> ↔ ibc/<hash_ueurgx>
- Activated when sufficient depth and provenance reliability are confirmed

### Amplification Parameter

Stable-swap pools use an amplification parameter (A) that flattens the invariant around the peg:

- **Range:** 100–500 (governance-set by pair class)
- **Effect:** Higher A values reduce slippage near parity
- **Balance:** Calibration ensures slippage near 1:1 while maintaining resilience to inventory shocks

---

## Fee Structure and Distribution

### Swap Fees by User Type

**Retail Trades:**
- Base fee: 0.3% (dynamic, increases with pool imbalance)
- Protocol fee: 0.05%
- Total: 0.35% base

**Institutional Trades:**
- Fixed fee: 0.1%
- Protocol fee: 0.05%
- Total: 0.15%

### Fee Distribution Model

Fees accumulate continuously and are distributed to LP token holders proportionally via the FeeDistributor contract:

**Distribution Cycle:** 24 hours
**Distribution Method:** Proportional to LP token holdings
**Institutional Cap:** 7% annual return (excess redistributed to retail LPs)

### Fee Flow

```
User Swap → Fee Collection → 24-Hour Accumulation → Distribution
                                    ↓
                            FeeDistributor Contract
                                    ↓
                    Proportional Distribution to LP Holders
```

---

## Reward System

### Incentive Programs

GuruDex incentivizes liquidity provision through multiple reward mechanisms:

**Trading Fee Rewards**
- Continuous accumulation from swap fees
- Distributed every 24 hours
- Proportional to LP token holdings

**Governance-Approved Bonding**
- Time-locked LP positions receive boost multipliers
- Early exit penalties feed safety buffer
- Longer lock periods = higher rewards

**Yield Farming**
- Pool-specific incentive programs
- Governance-approved emission schedules
- Tiered by pair class (stable-stable, stable-GXN, long-tail)

### Reward Calculation

```
User Reward = (User LP Tokens / Total LP Tokens) × Period Rewards

With Boosts:
Boosted Reward = Base Reward × Time Lock Multiplier × Pool Tier Bonus
```

### Institutional LP Cap

To ensure regulatory compliance and revenue fairness:
- Institutional LP returns are capped at 7% annually
- Excess rewards above this cap are redistributed to retail LPs
- This results in higher expected returns for retail participants

---

## Concentrated Liquidity

GuruDex integrates concentrated liquidity AMM models (similar to Uniswap v3), allowing LPs to allocate capital within defined price ranges rather than across the entire curve.

### Benefits of Concentrated Liquidity

**Capital Efficiency**
LPs can concentrate liquidity around the peg (1:1 for stablecoins), earning more fees with less capital.

**Reduced Idle Liquidity**
Capital not allocated outside the prevailing market price range is utilized more effectively.

**Better Execution**
Deeper liquidity at common trading prices means better rates for traders.

### Liquidity Distribution: Uniform vs Concentrated

**Uniform Distribution:**
- Capital spread across entire price range
- Most capital idle (not earning fees)
- Lower capital efficiency

**Concentrated Distribution:**
- Capital focused around peg (e.g., 0.99–1.01)
- Minimal idle capital
- Higher capital efficiency
- Better execution for traders

### Stablecoin Corridor Optimization

For stablecoin-to-stablecoin corridors where prices cluster around parity:
- Concentrated liquidity is particularly effective
- LPs can achieve 10-100x capital efficiency
- Traders experience tighter spreads and better rates
