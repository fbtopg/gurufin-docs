# Risk Mitigation: 4-Layer Defense Strategy

GuruDex has established a **multi-layered 4-layer defense strategy** to protect the platform and user assets. Exchange rate volatility is the biggest threat to DEX stability, and each layer of this strategy complements the others to ensure system robustness in effectively managing these risks.

## Defense Strategy Overview

```
┌─────────────────────────────────────────────────────────────────┐
│         Layer 1: Exchange Rate Risk Reserve                      │
│   Exchange Rate Risk Reserve (Insurance Fund)                    │
│   - Compensate for losses from rapid exchange rate fluctuations │
│   - Dual management of retail/institutional reserves            │
└─────────────────────────────────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│         Layer 2: Dynamic Fee Adjustment                          │
│   Dynamic Fee Adjustment (Market Balance Mechanism)              │
│   - Real-time fee adjustment based on pool utilization/volatility│
│   - Suppress excessive trading and induce rebalancing           │
└─────────────────────────────────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│    Layer 3: Swap Size Limits & Price Validation                 │
│   Size Limits & Price Validation (Trade Restriction Mechanism)  │
│   - Limit impact of single transactions                         │
│   - Triple validation of oracle prices (time/deviation/confidence)│
└─────────────────────────────────────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              Layer 4: Circuit Breaker                            │
│   Circuit Breaker (Last Line of Defense)                        │
│   - Automatically halt trading when serious threats detected    │
│   - Protect system and secure response time                     │
└─────────────────────────────────────────────────────────────────┘
```

***

## Layer 1: Exchange Rate Risk Reserve

### Role and Purpose

The Exchange Rate Risk Reserve is an **Insurance Fund** that compensates for pool losses caused by rapid exchange rate fluctuations. This is the first line of defense protecting liquidity providers (LPs) from unpredictable FX market volatility.

### Funding and Management

- **Initial Reserve**: Secure **5-10%** of each pool's liquidity separately
- **Replenishment Mechanism**: 
  - Automatically compensate from reserve when losses occur
  - Shortfalls replenished with a portion of trading fee revenue
  - Automatic alerts triggered when reserve falls below threshold

### Dual Management: Retail vs Institutional Reserves

GuruDex manages reserves in a **dual system** to isolate risks and apply differentiated compensation policies by user type:

| Category | Retail Reserve | Institutional Reserve |
|---|---|---|
| **Purpose** | Compensate retail users' small losses | Compensate institutions' large trade losses |
| **Scale** | 3-5% of pool liquidity | 5-10% of pool liquidity |
| **Risk Characteristics** | High frequency, low unit loss | Low frequency, high unit loss |
| **Replenishment Source** | Retail transaction fees (0.3%) | Institutional transaction fees (0.1%) |
| **Effect** | Minimize retail user risk exposure | Isolate institutional risk and ensure system stability |

### Example Operation

**Scenario**: USD/KRW rate surges from 1,300 to 1,350 (3.8% increase)

1. **Loss Calculation**: USGX-KRGX pool experiences approximately 100,000 USD worth of imbalance
2. **Reserve Activation**: 
   - Retail reserve compensates 30,000 USD
   - Institutional reserve compensates 70,000 USD
3. **LP Protection**: Liquidity providers experience no principal loss despite exchange rate fluctuation
4. **Replenishment**: Over next 30 days, 20% of trading fees allocated to reserve replenishment

***

## Layer 2: Dynamic Fee Adjustment

### Role and Purpose

Dynamic fees are an automated market stabilization mechanism that **adjusts trading costs in real-time** based on market conditions to suppress excessive trading and maintain pool balance.

### Adjustment Logic

Fees are calculated dynamically according to the following formula:

\[
Fee_{adjusted} = Fee_{base} \times (1 + Coefficient_{utilization} + Coefficient_{volatility})
\]

**Components**:
- **Fee_base**: Base fee (e.g., 0.3%)
- **Coefficient_utilization**: Pool utilization coefficient (liquidity shortage level)
- **Coefficient_volatility**: Exchange rate volatility coefficient (market instability level)

### Fee Adjustment Examples by Scenario

| Situation | Base Fee | Utilization | Volatility | Utilization Coef. | Volatility Coef. | Final Adjusted Fee |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Normal (Stable)** | 0.3% | 50% | 0.5% | 0.00 | 0.00 | **0.30%** |
| **High Utilization** | 0.3% | 85% | 0.5% | 0.35 | 0.00 | **0.41%** (+37%) |
| **High Volatility** | 0.3% | 50% | 2.0% | 0.00 | 0.20 | **0.36%** (+20%) |
| **Both High (Crisis)** | 0.3% | 90% | 3.0% | 0.80 | 0.30 | **0.63%** (+110%) |

### Effects

- **When pool utilization is high**: Fee increase → Suppress trading → Prevent liquidity depletion
- **When volatility is high**: Fee increase → Reduce speculative trading → Market stabilization
- **When market is stable**: Maintain low fees → Smooth trading environment

***

## Layer 3: Swap Size Limits & Price Validation

### 3-1. Swap Size Limits

#### Purpose
Limit the impact of single transactions on the pool to prevent **price manipulation by whales or malicious actors**.

#### Limitation Mechanism

- **Per-transaction Limit**: Block swaps exceeding **5%** of total liquidity
- **Daily Cumulative Limit**: 
  - Retail users: No limit (but per-transaction limit applies)
  - Institutional users: Institution-specific daily limits apply

**Example**:
- Pool Liquidity: 10,000,000 USGX
- Maximum per transaction: 500,000 USGX (5%)
- Transaction attempts exceeding limit automatically rejected

### 3-2. Oracle Price Validation (Triple Validation)

Oracle prices used in institutional trading undergo **triple validation** at the contract level to ensure reliability and safety.

#### ① Time Validation (Timestamp Validation)

```solidity
require(
    block.timestamp - oracleData.timestamp <= maxStaleness,
    "Price data is stale"
);
```

- **Purpose**: Prevent application of inaccurate prices due to outdated data
- **Standard**: Only allow data within maximum allowed age (e.g., 5 minutes)
- **Effect**: Ensure real-time market price reflection

#### ② Deviation Validation

```solidity
uint256 deviation = abs(newPrice - storedPrice) / storedPrice;
require(deviation <= maxPriceDeviation, "Price deviation too large");
```

- **Purpose**: Detect rapid price fluctuations or oracle errors
- **Standard**: Only allow fluctuations within 2% of previous price
- **Effect**: Prevent system damage from abnormal price jumps

#### ③ Confidence Validation

```solidity
require(
    oracleData.confidence >= minConfidenceThreshold,
    "Oracle confidence too low"
);
```

- **Purpose**: Reject low-quality or uncertain price data
- **Standard**: Only allow confidence scores of 95% or above
- **Effect**: Ensure transaction accuracy using only high-quality price feeds

### Handling Validation Failures

If oracle price fails any of the triple validations:
1. Transaction immediately rejected
2. Failure reason recorded in event log
3. Automatic alert sent to operations team
4. Temporarily suspend oracle source if necessary

***

## Layer 4: Circuit Breaker

### Role and Purpose

The circuit breaker is the system's **last line of defense**, an automated safety mechanism that temporarily halts related transactions when serious threats are detected. It blocks attackers from exploiting the system and secures time for the operations team to analyze the situation and respond, preventing asset losses.

### Trigger Conditions

The circuit breaker automatically triggers when the following predefined risk scenarios are detected:

#### Condition 1: Excessive Price Fluctuation

```solidity
if (abs(currentPrice - averagePrice) / averagePrice > EXTREME_VOLATILITY_THRESHOLD) {
    triggerCircuitBreaker("Extreme price volatility detected");
}
```

- **Threshold**: Rapid fluctuation of **5% or more** from average price
- **Measurement Period**: Average price over last 10 minutes
- **Example**: Flash crash, oracle manipulation attempt

#### Condition 2: Rapid Liquidity Drain

```solidity
if (currentLiquidity < previousLiquidity * LIQUIDITY_DROP_THRESHOLD) {
    triggerCircuitBreaker("Rapid liquidity drain detected");
}
```

- **Threshold**: Liquidity decrease of **20% or more** from previous
- **Measurement Period**: Last 1 hour
- **Example**: Massive withdrawal panic, bank run

#### Condition 3: Consecutive Large Transactions

```solidity
if (largeTxCount > MAX_LARGE_TX_IN_PERIOD && totalVolume > VOLUME_THRESHOLD) {
    triggerCircuitBreaker("Suspicious large transaction pattern");
}
```

- **Threshold**: **5 or more** maximum limit transactions within 1 hour
- **Volume Threshold**: Trading volume **50% or more** of pool liquidity
- **Example**: Bot attack, flash loan attack

#### Condition 4: Oracle Failure or Discrepancy

```solidity
if (oracleFailureCount > MAX_ORACLE_FAILURES || priceDiscrepancy > MAX_DISCREPANCY) {
    triggerCircuitBreaker("Oracle reliability compromised");
}
```

- **Threshold**: **3 or more** oracle validation failures within 10 minutes
- **Discrepancy Threshold**: **3% or more** price difference between multiple oracle sources
- **Example**: Oracle hacking, data feed interruption

### Circuit Breaker Operation Process

```
┌─────────────────────────────────────────────────────────────┐
│       Step 1: Risk Scenario Detection                       │
│   Automated monitoring system detects anomalies             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│       Step 2: Automatic Circuit Breaker Activation          │
│   Immediately halt trading in affected pool or entire system│
│   - Block new swaps                                         │
│   - Suspend liquidity add/remove                            │
│   - Suspend institutional trading                           │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│       Step 3: Emergency Alert to Operations Team            │
│   - Real-time alerts (Slack, Email, SMS)                    │
│   - Provide detailed risk scenario information              │
│   - Activate current system status dashboard                │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│       Step 4: Situation Analysis & Response                 │
│   Operations team identifies problem cause and develops     │
│   response plan                                             │
│   - Analyze attack vector                                   │
│   - Assess damage scope                                     │
│   - Determine response actions                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│       Step 5: System Recovery & Resumption                  │
│   Gradually resume system functions after resolving issue   │
│   - Perform test transactions                               │
│   - Phased resumption starting with small trades            │
│   - Maintain enhanced monitoring                            │
└─────────────────────────────────────────────────────────────┘
```

### Circuit Breaker Levels

GuruDex operates a **3-tier circuit breaker** based on threat severity:

| Level | Name | Trigger Condition | Impact Scope | Release Authority |
|---|---|---|---|---|
| **Level 1** | **Warning** | Medium threat detected | - Temporarily limit large trades<br/>- Enhanced monitoring | Auto-release (after 30 minutes) |
| **Level 2** | **Partial Halt** | Serious threat detected | - Halt all swaps in specific pool<br/>- Suspend liquidity changes in that pool<br/>- Other pools operate normally | Operator approval required |
| **Level 3** | **Full Halt** | Systemic crisis | - Halt all swaps<br/>- Halt all liquidity changes<br/>- Complete institutional trading suspension | Owner + Governance approval required |

### Real Operation Example

**Scenario**: Flash loan attack attempt detected

1. **09:30:00** - Attacker borrows massive funds and attempts consecutive large swaps in USGX-KRGX pool
2. **09:30:15** - Automated monitoring system detects abnormal pattern:
   - 5 maximum limit transactions within 15 seconds
   - 30% of pool liquidity moved
3. **09:30:16** - **Level 2 Circuit Breaker Activated**:
   - Immediately halt all transactions in USGX-KRGX pool
   - Block attacker's additional transactions
4. **09:30:20** - Emergency alert sent to operations team
5. **09:45:00** - Operations team completes situation analysis:
   - Flash loan attack confirmed
   - No actual losses (circuit breaker early interception)
6. **10:00:00** - Trading resumed with Operator approval
7. **Result**: **Zero asset loss, system normally recovered**

***

## Additional Risk Management Mechanisms

### Smart Contract Security

| Security Measure | Description |
|---|---|
| **Code Audits** | Regular audits by reputable third-party security firms (e.g., CertiK, OpenZeppelin) |
| **Bug Bounty** | Operate reward program for vulnerability discovery to encourage white hat hacker participation |
| **Upgradeability** | Use proxy pattern to rapidly deploy bug fixes and improvements |
| **Timelock** | Apply 24-48 hour timelock to significant system changes for community review opportunity |

### Institutional Risk Management

| Management Item | Description |
|---|---|
| **KYC/AML Verification** | Thorough identity verification and anti-money laundering verification through InstitutionalRegistry |
| **Trading Limits** | Limit exposure by setting per-institution transaction and daily cumulative limits |
| **Custom Fees** | Apply differential fees based on institution-specific risk profiles |
| **Real-time Monitoring** | Real-time monitoring of institutional trading patterns and automatic detection of abnormal trades |

### Network and System Risks

| Risk | Mitigation |
|---|---|
| **Network Congestion** | Ensure priority transactions through Guru-PEG's dynamic gas fee adjustment |
| **Oracle Centralization** | Eliminate single points of failure using multiple oracle sources and weighted median aggregation |
| **Governance Attacks** | Time-delayed voting, minimum quorum, emergency veto mechanisms |

***

## 4-Layer Defense Strategy Comprehensive Summary

| Defense Layer | Purpose | Key Mechanisms | Effects |
|---|---|---|---|
| **Layer 1: Reserve** | Loss Compensation | Secure 5-10% exchange rate fluctuation reserve | Protect LP principal, system stability |
| **Layer 2: Dynamic Fees** | Suppress Trading | Adjust fees based on utilization/volatility | Maintain pool balance, block speculation |
| **Layer 3: Limits & Validation** | Limit Impact | Transaction size limits + oracle triple validation | Prevent price manipulation, ensure quality |
| **Layer 4: Circuit Breaker** | Emergency Halt | Automatic threat detection and trading halt | Block attacks, secure response time |

### Risk Mitigation Flow Diagram

<figure><img src="../.gitbook/assets/risk_mitigation.png" alt=""><figcaption></figcaption></figure>

***

## Conclusion

GuruDex's 4-layer defense strategy is a powerful safety mechanism that ensures platform **stability and asset safety** even amid the unpredictable volatility of FX markets.

- **Layer 1 (Reserve)** immediately compensates when losses occur
- **Layer 2 (Dynamic Fees)** automatically stabilizes the market
- **Layer 3 (Limits & Validation)** proactively blocks malicious actions
- **Layer 4 (Circuit Breaker)** protects the system as the last line of defense

Through this multi-layered approach, GuruDex positions itself as an **enterprise-grade decentralized FX platform** capable of meeting real financial market requirements beyond mere technical experimentation.

Users can trade in a safe, reliable, and resilient FX swap environment through these comprehensive risk management features.
