# Guru-PEG (Price Equilibrium Governance)

Guru-PEG is the gas pricing mechanism of Gurufin Chain. It decouples user transaction costs from the volatility of the native GURU token, enabling predictable, fiat-indexed fees that remain stable regardless of market conditions.

## Why Guru-PEG Matters

In most blockchain networks, gas fees are denominated in the native token. When the token price surges, a flat token-based fee translates into a much higher fiat cost for users. This volatility creates friction for everyday transactions and makes the chain unsuitable for high-frequency use cases like retail payments or enterprise operations.

Guru-PEG solves this by designing the gas price so that a typical transfer costs approximately **$0.013** — a predictable, consumer-friendly rate — even as the GURU token price fluctuates.

## How It Works

### Core Formula

At its simplest, Guru-PEG applies the following relationship:

```
min_gas_price_GURU = target_gas_fee_USD / current_GURU_price_USD
```

Where:

- **`target_gas_fee_USD`** — the desired fiat-equivalent cost of a standard operation (e.g., a basic transfer)
- **`current_GURU_price_USD`** — the live USD price of GURU as reported by the oracle network
- **`min_gas_price_GURU`** — the resulting minimum gas price in GURU per unit of computation

When GURU's price rises, the required GURU per transaction decreases. When GURU's price falls, the required GURU increases. The user-facing fiat cost stays stable.

### Step-by-Step Mechanism

1. **Oracle Feeds** — A decentralized oracle network continuously collects GURU/USD price data from multiple on-chain and off-chain sources.
2. **Validation & Aggregation** — Reported prices are validated against each other. An outlier filter removes anomalous readings, and the aggregated value is derived using median or quorum-based logic to reduce the impact of any single compromised feed.
3. **Protocol Update** — The protocol contract reads the aggregated price and recalculates the `min_gas_price` in GURU using the formula above. This update occurs each block (or at a configured interval) to keep the fee responsive to market conditions.
4. **Dynamic Inverse Adjustment** — As GURU's price rises, fewer GURU tokens are needed per gas unit, and vice versa. This inverse relationship is what keeps the fiat-equivalent cost stable for users.
5. **User Experience** — Wallets and applications display the estimated fee in both GURU and the user's preferred fiat currency, so the stable cost is transparent at the point of interaction.

## Safeguards & Fault Tolerance

GXN-PEG is designed with multiple layers of protection to handle edge cases and maintain stability even under adverse conditions.

| Safeguard | Purpose |
|-----------|---------|
| **Oracle Quorum** | Price updates require agreement from a minimum number of independent oracle nodes, preventing a single point of manipulation. |
| **Outlier Filtering** | Readings that deviate significantly from the consensus group are excluded from the aggregation calculation. |
| **Price Deviation Checks** | If the reported price change exceeds a configurable threshold within a single interval, the protocol pauses the update until the deviation resolves. |
| **Gas Fee Floor & Ceiling** | A minimum and maximum bound on `min_gas_price_GURU` prevents fees from becoming zero (which would enable spam) or prohibitively high (which would hurt usability). |
| **Peg Buffer** | A reserve mechanism absorbs short-term price shocks, smoothing the fee curve during periods of extreme volatility. |
| **Emergency Fallback / Circuit Breaker** | If the oracle network becomes unresponsive or a critical fault is detected, the protocol falls back to a stale-but-safe price and locks the gas price at a fixed rate until normal operations resume. |

## What This Enables

By keeping transaction costs predictable and consumer-friendly, GXN-PEG makes Gurufin Chain suitable for:

- **Retail payments** — micro-transactions and point-of-sale payments that require stable, low-cost settlement.
- **Enterprise operations** — supply chain tracking, automated invoicing, and recurring on-chain workflows.
- **High-frequency use cases** — any application where volatile gas fees would introduce unacceptable cost uncertainty.
