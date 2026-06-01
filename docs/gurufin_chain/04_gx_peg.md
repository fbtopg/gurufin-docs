# Guru-PEG (Price Equilibrium Governance)

Guru-PEG is the gas pricing mechanism of Gurufin Chain. It decouples user transaction costs from the volatility of the native GXN token, enabling predictable, fiat-indexed fees that remain stable regardless of market conditions.

## Why Guru-PEG Matters

In most blockchain networks, gas fees are denominated in the native token. When the token price surges, a flat token-based fee translates into a much higher fiat cost for users. This volatility creates friction for everyday transactions and makes the chain unsuitable for high-frequency use cases like retail payments or enterprise operations.

Guru-PEG solves this by designing the gas price so that a typical transfer costs approximately **$0.013** — a predictable, consumer-friendly rate — even as the GXN token price fluctuates.

## How It Works

### Core Formula

At its simplest, Guru-PEG applies the following relationship:

```
min_gas_price_GXN = target_gas_fee_USD / current_GXN_price_USD
```

Where:

- **`target_gas_fee_USD`** — the desired fiat-equivalent cost of a standard operation (e.g., a basic transfer)
- **`current_GXN_price_USD`** — the live USD price of GXN as reported by the oracle network
- **`min_gas_price_GXN`** — the resulting minimum gas price in GXN per unit of computation

When GXN's price rises, the required GXN per transaction decreases. When GXN's price falls, the required GXN increases. The user-facing fiat cost stays stable.

### Step-by-Step Mechanism

1. **Oracle Feeds** — A decentralized oracle network continuously collects GXN/USD price data from multiple on-chain and off-chain sources.
2. **Validation & Aggregation** — Reported prices are validated against each other. An outlier filter removes anomalous readings, and the aggregated value is derived using median or quorum-based logic to reduce the impact of any single compromised feed.
3. **Protocol Update** — The protocol contract reads the aggregated price and recalculates the `min_gas_price` in GXN using the formula above. This update occurs each block (or at a configured interval) to keep the fee responsive to market conditions.
4. **Dynamic Inverse Adjustment** — As GXN's price rises, fewer GXN tokens are needed per gas unit, and vice versa. This inverse relationship is what keeps the fiat-equivalent cost stable for users.
5. **User Experience** — Wallets and applications display the estimated fee in both GXN and the user's preferred fiat currency, so the stable cost is transparent at the point of interaction.

## Safeguards & Fault Tolerance

Guru-PEG is designed with multiple layers of protection to handle edge cases and maintain stability even under adverse conditions.

| Safeguard | Purpose |
|-----------|---------|
| **Oracle Quorum** | Price updates require agreement from a minimum number of independent oracle nodes, preventing a single point of manipulation. |
| **Outlier Filtering** | Readings that deviate significantly from the consensus group are excluded from the aggregation calculation. |
| **Price Deviation Checks** | If the reported price change exceeds a configurable threshold within a single interval, the protocol pauses the update until the deviation resolves. |
| **Gas Fee Floor & Ceiling** | A minimum and maximum bound on `min_gas_price_GXN` prevents fees from becoming zero (which would enable spam) or prohibitively high (which would hurt usability). |
| **Peg Buffer** | A reserve mechanism absorbs short-term price shocks, smoothing the fee curve during periods of extreme volatility. |
| **Emergency Fallback / Circuit Breaker** | If the oracle network becomes unresponsive or a critical fault is detected, the protocol falls back to a stale-but-safe price and locks the gas price at a fixed rate until normal operations resume. |

## Known Limitations & Mitigations

### Oracle Latency
Guru-PEG price feeds update on a per-block basis. In rare cases where GXN price moves rapidly between oracle update intervals (typically ~2 seconds), the gas price may briefly diverge from the true market rate. The price deviation checks and gas fee floor/ceiling safeguards mitigate the impact of this divergence.

### MEV Considerations
Because Guru-PEG uses oracle-derived prices rather than on-chain order books, traditional MEV strategies (front-running, sandwich attacks) are not applicable to gas pricing itself. 

**OPRS MEV Protection:** For Oracle Priced Reserve Swaps, the protocol enforces an oracle staleness check (max 5-second delay) and a maximum slippage tolerance per swap. If the oracle update lags market movements beyond configured thresholds, the swap is either repriced conservatively or cancelled, preventing MEV bots from extracting value during latency windows. Applications built on-chain should also implement private transaction relays where appropriate.

### Extreme Market Events
During periods of extreme token price volatility (e.g., >20% single-day moves), the emergency fallback / circuit breaker may activate, temporarily freezing gas price updates. The protocol falls back to the last confirmed price with a conservative buffer until the oracle network stabilizes.

## What This Enables

By keeping transaction costs predictable and consumer-friendly, Guru-PEG makes Gurufin Chain suitable for:

- **Retail payments** — micro-transactions and point-of-sale payments that require stable, low-cost settlement.
- **Enterprise operations** — supply chain tracking, automated invoicing, and recurring on-chain workflows.
- **High-frequency use cases** — any application where volatile gas fees would introduce unacceptable cost uncertainty.
