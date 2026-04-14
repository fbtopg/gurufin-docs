# GuruDex Overview

🦙 An FX-Specialized Decentralized Exchange for Stablecoin Trading

---

## 🚀 Quick Links

- **Architecture**: `02 OPRS Architecture` | `04 Smart Contracts`
- **GX Stablecoins**: `01 GX Overview` | `03 Mint & Burn`
- **Use Cases**: `02 Stablecoin FX Trading` | `01 Cross-Border Payments`
- **Developer**: `Testnet Access` | `API Reference`

---

## What is GuruDex?

GuruDex is an FX-specialized decentralized exchange designed for seamless swaps between sovereign stablecoins on Gurufin Chain. Unlike general-purpose DEXs that rely on Automated Market Makers (AMMs), GuruDex uses an **Oracle Priced Reserve Swap (OPRS)** architecture purpose-built for on-chain stablecoin FX trading.

**Key Differentiator**: GuruDex is built specifically for stablecoin FX trading, where price stability and accurate FX rates are critical.

---

## Why OPRS, Not AMM?

AMMs (Automated Market Makers) are designed for volatile asset pairs where price discovery emerges from trading activity. However, stablecoin FX trading is fundamentally different:

| Challenge | AMM Limitation | OPRS Solution |
|-----------|----------------|---------------|
| **Price Discovery** | Emerges from trading activity | Real-time oracle feeds |
| **Slippage** | Increases with trade size | Zero slippage |
| **Liquidity** | Requires deep pools | Minimal liquidity needed |
| **Peg Maintenance** | Relies on arbitrage | Oracle validation |

### Why AMMs Don't Work for Stablecoin FX

- **GX stablecoins are pegged to individual fiat currencies** — USGX (USD), KRGX (KRW), EURGX (EUR), etc.
- **Each fiat-pegged stablecoin has its own GX Chain L1 mainnet** — separate sovereign chains with jurisdiction-specific validators
- **Prices are determined by real-world FX rates**, not on-chain supply/demand dynamics
- **Swaps happen via IBC (Inter-Blockchain Communication)** — cross-chain atomic settlement between sovereign chains

AMM pools would introduce unnecessary slippage and fail to reflect actual FX rates. OPRS uses oracle-guided pricing with mint/burn mechanics, ensuring swaps execute at precise market rates.

See: `OPRS Architecture Details`

---

## Oracle Priced Reserve Swap (OPRS)

GuruDex uses a mint-and-burn mechanism guided by oracle FX rates rather than liquidity pool-based pricing:

### How OPRS Works

1. **Oracle Price Feed** — Real-time FX rates from trusted oracles (with triple validation: freshness, deviation, confidence)
2. **Mint/Burn Mechanism** — Instead of swapping tokens in a pool, the system burns the input stablecoin on its native chain and mints the output stablecoin on its destination chain
3. **IBC Settlement** — Cross-chain transfers are atomic via IBC/HTLCs, eliminating counterparty risk
4. **No Slippage** — Trades execute at oracle-verified rates, not pool-dependent prices

### Step-by-Step Swap Flow

```
Example: User swaps 1,000 USGX → KRGX
1. User initiates swap on GuruDex
2. Oracle provides real-time FX rate (e.g., 1 USD = 1,300 KRW)
3. 1,000 USGX burned on USGX Chain
4. 1,298,700 KRGX minted on KRGX Chain
5. IBC ensures atomic cross-chain settlement
6. User receives KRGX in their wallet
```

See detailed flow: `OPRS Architecture`

---

## Sovereign Chain Architecture

Each GX stablecoin operates on its own dedicated Layer-1 blockchain:

- **USGX Chain** — USD-pegged stablecoin, US jurisdiction validators
- **KRGX Chain** — KRW-pegged stablecoin, Korea jurisdiction validators
- **EURGX Chain** — EUR-pegged stablecoin, EU jurisdiction validators
- **JPGX Chain** — JPY-pegged stablecoin, Japan jurisdiction validators

GuruDex on Gurufin Chain acts as the FX settlement hub, connecting these sovereign chains via IBC for cross-currency swaps.

### Architecture Diagram

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  USGX Chain │    │  KRGX Chain │    │  EURGX Chain│
│   (US PoA)  │    │  (KR PoA)   │    │   (EU PoA)  │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                    ┌─────▼─────┐
                    │ Gurufin   │
                    │ Chain     │
                    │ (DPoS)    │
                    │  IBC Hub  │
                    └───────────┘
                          │
                    ┌─────▼─────┐
                    │  GuruDex  │
                    │   OPRS    │
                    │   DEX     │
                    └───────────┘
```

See: `GX Chain Overview` | `Gurufin Chain Whitepaper`

---

## Core Smart Contracts

The platform is powered by four key contracts:

### 1. FXSwapMaster 🎯
**Central orchestration and governance contract**
- Manages swap routing and execution
- Handles governance parameters
- Coordinates with other contracts

### 2. OPRSProcessor 🔧
**Oracle-priced swap execution via mint/burn**
- Validates oracle price feeds
- Executes mint/burn operations
- Ensures atomic cross-chain settlements

### 3. PriceOracle 📊
**Real-time FX rate validation**
- Triple validation: freshness, deviation, confidence
- Aggregates data from multiple sources
- Price deviation detection

### 4. InstitutionalRegistry 🛡️
**KYC/AML and institutional onboarding**
- Manages institutional wallet permissions
- Enforces compliance requirements
- Tier-based access control

See complete contract details: `Smart Contract Logic`

---

## Security & Compliance

### Oracle Security

All oracle prices undergo **triple validation**:
- **Freshness**: Data must be less than 5 minutes old
- **Deviation**: Price must be within 1% of stored rate
- **Confidence**: Oracle confidence score must exceed 95%

If validation fails, the swap reverts and the user is notified.

### Compliance Integration

- **Institutional Registry**: Pre-verified institutional wallets
- **Transaction Monitoring**: Real-time AML checks
- **Jurisdictional Rules**: Chain-specific compliance policies

See: `GX Compliance Framework`

---

## Use Cases

GuruDex enables several key use cases:

1. **Cross-Border FX Swaps**: Instant currency conversion for individuals and businesses
2. **DeFi Interoperability**: Access liquidity across multiple chains
3. **Institutional Settlement**: FMI-grade settlement for large trades
4. **CBDC Integration**: Bridge fiat and digital currency ecosystems

See detailed use cases: `01 Cross-Border Payments` | `02 Stablecoin FX Trading` | `03 Institutional DeFi`

---

## Developer Resources

### Getting Started

**Testnet Access**:
- Chain ID: `guru_631-1`
- RPC: `https://trpc.gurufin.io`
- Faucet: `https://faucet.gurufin.io/`
- Explorer: `https://tscan.gurufin.io/`

**Documentation**:
- `API Reference`
- `Full Developer Docs`
- `Ecosystem Grant Program`

### SDK Examples

```typescript
// Example: Swap 1000 USGX → KRGX
import { GuruDexClient } from '@gurufin/sdk';

const client = new GuruDexClient('guru_631-1');
const result = await client.swap({
  fromToken: 'USGX',
  toToken: 'KRGX',
  amount: 1000,
  recipient: 'guru1...'
});
```

See more examples: `Full Developer Docs`

---

## Related Documentation

- **Architecture**: `GX Chain Overview`
- **Settlement Layer**: `Gurufin Chain Whitepaper`
- **Reserves**: `GX Reserve & Backing`
- **Liquidity**: `Liquidity & Rewards`

---

*GuruDex is the future of stablecoin FX trading — fast, accurate, and compliant.*

---
