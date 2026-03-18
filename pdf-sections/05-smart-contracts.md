# Smart Contract Architecture

## Overview

GuruDex's swap execution is orchestrated by a modular smart contract system. Each contract handles a specific responsibility, enabling clean separation of concerns and independent upgradability.

---

## Core Contracts

### FXSwapMaster

The central orchestration contract that coordinates all swap operations and manages system governance.

**Responsibilities:**
- Central routing of all swap requests
- Governance parameter management
- System configuration and upgrades
- Emergency controls and circuit breakers

**Key Functions:**
- `initiateSwap()` — Entry point for all swap operations
- `setGovernanceParams()` — Update system parameters
- `emergencyPause()` — Halt all trading operations
- `resumeTrading()` — Resume operations after pause

---

### OPRSProcessor

The core Oracle Priced Reserve Swap execution engine that handles the mint/burn mechanics.

**Responsibilities:**
- Oracle-priced swap execution via mint/burn mechanism
- Cross-chain settlement coordination via IBC
- Transaction validation and verification
- Burn/mint event logging

**Swap Execution Flow:**

```
1. Receive swap request from FXSwapMaster
2. Query PriceOracle for validated FX rate
3. Calculate output amount (input × rate - fees)
4. Initiate burn on source chain
5. Coordinate mint on destination chain
6. Verify atomic settlement via IBC
7. Emit completion events
```

**Key Functions:**
- `executeOPRS()` — Execute oracle-priced swap
- `validateOraclePrice()` — Verify price freshness and accuracy
- `initiateBurn()` — Burn input tokens on source chain
- `confirmMint()` — Confirm mint on destination chain

---

### PriceOracle

Stores and validates real-time FX rates from the decentralized oracle network.

**Responsibilities:**
- Real-time FX rate storage and validation
- Provider management and quality scoring
- Outlier detection and filtering
- Historical price tracking

**Validation Criteria:**

| Check | Threshold | Purpose |
|-------|-----------|---------|
| Freshness | < 5 minutes | Prevent stale data |
| Deviation | < 1% from stored | Detect manipulation |
| Confidence | > 95% score | Ensure reliability |

**Key Functions:**
- `submitPrice()` — Oracle provider submits price
- `getValidatedPrice()` — Retrieve current validated price
- `addProvider()` — Register new oracle provider
- `removeProvider()` — Remove misbehaving provider

---

### InstitutionalRegistry

Manages institutional profiles, KYC/AML compliance, and custom trading parameters.

**Responsibilities:**
- Institutional onboarding and verification
- KYC/AML status tracking
- Custom fee and limit configuration
- Pool and coin authorization management

**Onboarding Workflow:**

```
1. Registration
   └── Institution calls registerInstitution()
   └── Submit basic company information

2. Verification
   └── Off-chain KYC/AML review by operations team
   └── Document verification and compliance check

3. Activation
   └── Operator sets custom limits and fees
   └── Configure trading parameters

4. Authorization
   └── Approve specific coins and pools
   └── Enable trading access
```

**Key Functions:**
- `registerInstitution()` — Submit registration
- `verifyInstitution()` — Admin verification
- `setInstitutionParams()` — Configure custom parameters
- `isAuthorized()` — Check trading authorization

---

### FeeDistributor

Allocates swap fees proportionally to LP token holders.

**Responsibilities:**
- Fee accumulation and tracking
- Proportional distribution calculation
- 24-hour reward cycles
- Institutional return cap enforcement

**Distribution Algorithm:**

```
For each 24-hour cycle:
1. Calculate total fees accumulated
2. For each LP holder:
   reward = (holder_tokens / total_tokens) × cycle_fees
3. Apply institutional cap (7% annual)
4. Redistribute excess to retail LPs
5. Distribute rewards
```

**Key Functions:**
- `depositFees()` — Add accumulated fees to distributor
- `calculateRewards()` — Compute rewards for all holders
- `claimRewards()` — LP claims accumulated rewards
- `getPendingRewards()` — Check unclaimed rewards

---

### PoolFactory

Deploys new pool instances as currencies are added to the ecosystem.

**Responsibilities:**
- Pool deployment and initialization
- Pool configuration management
- Pool registry maintenance
- Upgrade coordination

**Key Functions:**
- `createPool()` — Deploy new pool
- `configurePool()` — Set pool parameters
- `getPoolInfo()` — Retrieve pool details
- `upgradePool()` — Deploy pool upgrade

---

## Swap Routing Logic

When a swap is initiated, the system determines the optimal execution path:

### Retail User Flow

```
User → FXSwapMaster → InstitutionalRegistry (check type)
                    ↓
              Retail User Confirmed
                    ↓
              OPRSProcessor → PriceOracle (get rate)
                    ↓
              Execute OPRS (mint/burn)
                    ↓
              IBC Settlement
                    ↓
              Completion Event
```

### Institutional User Flow

```
User → FXSwapMaster → InstitutionalRegistry (check type)
                    ↓
              Institutional User Confirmed
                    ↓
              Custom Fee/Limit Lookup
                    ↓
              OPRSProcessor → PriceOracle (get rate)
                    ↓
              Execute OPRS (oracle-verified)
                    ↓
              IBC Settlement
                    ↓
              Completion Event
```

---

## Contract Interaction Diagram

```
                    ┌─────────────────┐
                    │   FXSwapMaster  │
                    │  (Orchestration)│
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Institutional   │ │  OPRSProcessor  │ │  PoolFactory    │
│ Registry        │ │  (Swap Engine)  │ │  (Pool Deploy)  │
└─────────────────┘ └────────┬────────┘ └─────────────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
           ┌─────────────┐   ┌─────────────┐
           │ PriceOracle │   │ FeeDistrib  │
           │ (FX Rates)  │   │ (Rewards)   │
           └─────────────┘   └─────────────┘
```

---

## Security Considerations

### Access Control

- **Role-based permissions** for all administrative functions
- **Multi-signature requirements** for critical operations
- **Timelock delays** for governance changes
- **Emergency pause** capabilities for all contracts

### Upgrade Safety

- **Staged upgrades** with testnet rehearsal
- **Time-locked activation** for production deployment
- **Rollback hooks** for emergency reversion
- **Audit requirements** before any upgrade

### Monitoring

- **Event emission** for all state changes
- **Anomaly detection** for unusual patterns
- **Real-time telemetry** for operational monitoring
- **Incident response** procedures documented
