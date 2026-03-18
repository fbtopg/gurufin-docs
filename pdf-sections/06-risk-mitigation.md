# Risk Mitigation Strategy

## Overview

Gurufin implements a comprehensive 4-layer defense strategy to protect against FX volatility, market manipulation, and operational risks. Each layer complements the others to ensure system robustness under adverse conditions.

---

## Layer 1: Reserve Fund

An insurance fund holding 5–10% of pool liquidity compensates losses from rapid rate fluctuations.

### Fund Structure

**Retail Segment:**
- Reserve allocation: 3–5% of pool liquidity
- Purpose: Protect retail users from sudden rate movements
- Replenishment: Automatic from trading fees when thresholds are breached

**Institutional Segment:**
- Reserve allocation: 5–10% of pool liquidity
- Purpose: Cover larger institutional exposures
- Replenishment: Automatic from trading fees when thresholds are breached

### Reserve Fund Mechanics

```
Pool Liquidity: $10,000,000
Reserve Allocation: 5% ($500,000)

If loss event occurs:
1. Loss detected via oracle monitoring
2. Reserve fund covers eligible losses
3. Trading fees replenish reserve
4. If reserve below threshold: alerts triggered
```

### Trigger Conditions

- Rapid rate fluctuations (> 5% in 1 hour)
- Oracle disagreement beyond thresholds
- Unusual trading patterns detected
- Circuit breaker activation

---

## Layer 2: Dynamic Fees

Retail fees adjust in real-time based on pool utilization and market volatility.

### Fee Schedule

**Normal Conditions:**
- Base fee: 0.3%
- Protocol fee: 0.05%
- Total: 0.35%

**Stressed Conditions:**
- Fee scales up to 0.63% maximum
- Triggered by high utilization or volatility
- Suppresses speculative trading
- Protects pool equilibrium

### Dynamic Fee Calculation

```
Current Fee = Base Fee × Volatility Multiplier × Utilization Multiplier

Where:
- Base Fee = 0.3%
- Volatility Multiplier = 1.0 - 2.0 (based on recent price swings)
- Utilization Multiplier = 1.0 - 1.5 (based on pool depth)

Example (high stress):
Current Fee = 0.3% × 1.4 × 1.5 = 0.63%
```

### Benefits

- **Automatic Stabilization** — Higher fees during stress discourage excessive trading
- **LP Protection** — Increased fees compensate LPs for additional risk
- **Market Calming** — Higher costs reduce panic selling
- **Revenue Increase** — More fees during volatile periods replenish reserves

---

## Layer 3: Limits and Validation

Individual swaps are capped and undergo rigorous validation to prevent manipulation.

### Swap Limits

**Pool Exposure Limit:**
- Maximum swap: 5% of pool liquidity
- Prevents whale manipulation
- Protects against flash loan attacks
- Applies to both retail and institutional trades

**Daily Volume Limits:**
- Per-user daily cap (governance-set)
- Per-pool daily cap (governance-set)
- Circuit breaker if limits exceeded

### Oracle Triple Validation

All institutional trades and large retail trades undergo oracle validation:

**Freshness Check:**
- Data must be less than 5 minutes old
- Stale data automatically rejected
- Prevents execution on outdated rates

**Deviation Check:**
- Price must be within 1% of stored rate
- Protects against flash crashes
- Triggers circuit breaker if exceeded

**Confidence Check:**
- Oracle confidence score must exceed 95%
- Based on provider reputation
- Weighted by quality scores

### Validation Failure Response

```
If validation fails:
1. Swap reverted (no funds lost)
2. User notified with failure reason
3. Event logged for monitoring
4. If repeated failures: alert operations team
```

---

## Layer 4: Circuit Breaker

Trading halts automatically when critical thresholds are breached, securing response time for operators and preventing cascading losses.

### Automatic Triggers

**Price Swing Trigger:**
- Threshold: > 5% price movement in 5 minutes
- Action: Pause all trading
- Duration: Until manual review and restart

**Liquidity Drain Trigger:**
- Threshold: > 20% liquidity removed in 1 hour
- Action: Pause affected pools
- Duration: Until investigation complete

**Suspicious Pattern Detection:**
- Indicators: Repeated failed transactions, unusual volume spikes
- Action: Temporary pause for review
- Duration: Until cleared by operations

### Circuit Breaker States

**Normal:**
- All trading active
- Standard fee schedule
- Full functionality

**Warning:**
- Enhanced monitoring
- Fee multiplier increased
- Alerts to operations team

**Paused:**
- Trading halted
- No new swaps accepted
- Existing swaps allowed to complete
- Manual restart required

**Emergency:**
- All operations halted
- Only withdrawals allowed
- Governance vote required to restart

### Manual Override

Governance can manually activate circuit breakers:
- Multi-signature requirement (3-of-5)
- Timelock delay (15 minutes for non-emergency)
- Public announcement required
- Audit trail maintained

---

## Risk Monitoring Dashboard

### Real-Time Metrics

**Pool Health:**
- Current liquidity depth
- Utilization rate
- Recent trade volume
- Fee revenue

**Oracle Status:**
- Price freshness
- Provider count
- Deviation from reference
- Confidence scores

**Risk Indicators:**
- Reserve fund balance
- Recent loss events
- Failed validations
- Circuit breaker status

### Alert System

**Level 1 (Information):**
- Fee rate changes
- Pool utilization updates
- Oracle provider status

**Level 2 (Warning):**
- Reserve fund below 75%
- Oracle deviation approaching threshold
- Unusual trading patterns

**Level 3 (Critical):**
- Reserve fund below 50%
- Oracle validation failures
- Circuit breaker triggered
- Potential security incident

---

## Incident Response Procedures

### Detection Phase
1. Automated monitoring detects anomaly
2. Alert generated to operations team
3. Initial assessment within 5 minutes

### Response Phase
1. Circuit breaker activated if needed
2. Operations team investigates
3. Root cause identified
4. Remediation plan developed

### Recovery Phase
1. Fix deployed (if code issue)
2. Parameters adjusted (if parameter issue)
3. Gradual restart with monitoring
4. Post-incident review completed

### Communication
1. Status page updated
2. Users notified of impact
3. Resolution communicated
4. Lessons learned documented
