# The OPRS Architecture: Oracle Priced Reserve Swap

## What is Oracle Priced Reserve Swap (OPRS)?

Oracle Priced Reserve Swap (OPRS) is a revolutionary exchange architecture purpose-built for stablecoin foreign exchange trading. Unlike traditional Automated Market Makers (AMMs) that rely on supply/demand dynamics within liquidity pools, OPRS uses oracle-guided pricing with mint/burn mechanics to execute swaps at precise market rates.

### Core Principle

OPRS recognizes that stablecoin FX trading is fundamentally different from volatile asset trading:

- **GX stablecoins are pegged to individual fiat currencies** — USGX (USD), KRGX (KRW), EURGX (EUR), JPGX (JPY)
- **Each fiat-pegged stablecoin has its own GX Chain L1 mainnet** — separate sovereign chains with jurisdiction-specific validators
- **Prices are determined by real-world FX rates**, not on-chain supply/demand dynamics
- **Swaps happen via IBC (Inter-Blockchain Communication)** — cross-chain atomic settlement between sovereign chains

Traditional AMMs would introduce unnecessary slippage and fail to reflect actual FX rates. OPRS eliminates these inefficiencies by using oracle-verified pricing with mint/burn mechanics.

---

## How OPRS Works: Step-by-Step Process

### Step 1: User Initiates a Swap

A user initiates a foreign exchange transaction on GuruDex. For example:
- **Input:** 1,000 USGX (USD-pegged stablecoin)
- **Desired Output:** KRGX (KRW-pegged stablecoin)

### Step 2: Oracle Provides Real-Time FX Rate

The PriceOracle contract retrieves the current USD/KRW exchange rate from the decentralized oracle network:
- **Example Rate:** 1 USD = 1,300 KRW
- **Validation:** The rate undergoes triple validation (freshness, deviation, confidence)

### Step 3: Input Stablecoin is Burned

On the USGX Chain (the sovereign chain for USD-pegged stablecoins):
- 1,000 USGX is **burned** (permanently removed from circulation)
- This action is verified and recorded on the USGX Chain

### Step 4: Output Stablecoin is Minted

On the KRGX Chain (the sovereign chain for KRW-pegged stablecoins):
- 1,298,700 KRGX is **minted** (created and sent to the recipient)
- This amount reflects the oracle rate minus any applicable fees

### Step 5: IBC Atomic Settlement

The cross-chain transfer completes atomically via IBC/HTLCs (Hashed Timelock Contracts):
- Both legs of the transaction either succeed together or fail together
- No counterparty risk — neither party can lose funds
- Settlement is final and irreversible

---

## Why OPRS for Stablecoin FX?

### Comparison: Traditional AMM vs OPRS

**Traditional AMM Characteristics:**
- Price emerges from trading activity
- Slippage increases with trade size
- Requires deep liquidity pools
- Arbitrageurs maintain peg
- Works for volatile pairs

**OPRS (GuruDex) Characteristics:**
- Price from real-time oracle feeds
- No slippage — oracle-verified rates
- Minimal liquidity needed (mint/burn)
- Oracle validation maintains accuracy
- Purpose-built for stablecoin FX

### Key Advantages of OPRS

**1. Zero Slippage**
Unlike AMMs where larger trades experience greater price impact, OPRS executes all trades at the oracle-verified rate. A $100 swap and a $1,000,000 swap both receive the same rate.

**2. True Market Pricing**
Prices reflect real-world FX rates, not pool dynamics. This eliminates the need for complex arbitrage to maintain peg alignment.

**3. Capital Efficiency**
No need to maintain deep liquidity pools. The mint/burn mechanism creates tokens on demand, reducing capital requirements.

**4. Cross-Chain Native**
Each stablecoin operates on its own sovereign chain, enabling jurisdictional compliance while maintaining seamless interoperability.

**5. Regulatory Alignment**
Oracle-verified pricing provides transparency for regulators, while mint/burn mechanics create clear audit trails.

---

## Oracle Validation System

All oracle prices undergo rigorous triple validation before execution:

### Freshness Check
- Data must be less than 5 minutes old
- Stale data is automatically rejected
- Prevents execution on outdated rates

### Deviation Check
- Price must be within 1% of stored rate
- Protects against flash crashes or manipulation
- Triggers circuit breaker if exceeded

### Confidence Check
- Oracle confidence score must exceed 95%
- Based on provider reputation and historical accuracy
- Weighted by provider quality scores

### Validation Process

```
Input: Oracle submission (value, timestamp, provider_id)
Output: Accept/Reject decision

1. Check timestamp freshness (age < τ_max)
2. Compare to stored rate (deviation < Δ_max)
3. Verify provider confidence score (confidence > 95%)
4. If all pass: Accept and update aggregate
5. If any fail: Reject and emit event
```

If validation fails, the swap reverts and the user is notified with the specific validation failure reason.

---

## Mint/Burn Mechanism

The mint/burn mechanism is the core innovation that enables OPRS to avoid traditional liquidity pool constraints:

### Traditional AMM Flow
1. User deposits Token A into pool
2. Pool calculates output based on constant product formula
3. User receives Token B from pool
4. Pool reserves adjust (causing slippage)

### OPRS Mint/Burn Flow
1. User sends Token A to swap contract
2. Token A is burned on its native chain
3. Token B is minted on its destination chain
4. User receives Token B at oracle-verified rate

### Benefits of Mint/Burn

**No Pool Imbalance**
Since tokens are burned and minted rather than swapped, there is no pool imbalance to manage.

**Infinite Liquidity**
As long as the oracle provides a valid price, any amount can be swapped.

**Clean Audit Trail**
Each swap creates a clear burn record on one chain and a mint record on the other.

**Jurisdictional Compliance**
Minting occurs on the appropriate sovereign chain, maintaining regulatory boundaries.

---

## Sovereign Chain Integration

Each GX stablecoin operates on its own dedicated Layer-1 blockchain:

### USGX Chain (USD)
- **Peg:** 1 USGX = 1 USD
- **Validators:** Licensed US financial institutions
- **Jurisdiction:** United States
- **Reserves:** USD held at US-regulated custodians

### KRGX Chain (KRW)
- **Peg:** 1 KRGX = 1 KRW
- **Validators:** Licensed Korean financial institutions
- **Jurisdiction:** South Korea
- **Reserves:** KRW held at Korean-regulated custodians

### EURGX Chain (EUR)
- **Peg:** 1 EURGX = 1 EUR
- **Validators:** Licensed EU financial institutions
- **Jurisdiction:** European Union
- **Reserves:** EUR held at EU-regulated custodians

### JPGX Chain (JPY)
- **Peg:** 1 JPGX = 1 JPY
- **Validators:** Licensed Japanese financial institutions
- **Jurisdiction:** Japan
- **Reserves:** JPY held at Japanese-regulated custodians

### Cross-Chain Swap Example: USGX → KRGX

When a user swaps USGX → KRGX on GuruDex:

1. **USGX Chain:** USGX is burned (removed from circulation)
2. **Gurufin Chain:** Oracle rate is retrieved and validated
3. **KRGX Chain:** KRGX is minted (created and sent to recipient)
4. **IBC Protocol:** Atomic settlement ensures both legs complete or fail together
