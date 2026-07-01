# Guru-PEG (Price Equilibrium Governance)

Guru-PEG is Gurufin Chain's gas pricing mechanism. It adjusts GXN-denominated gas prices using oracle-fed market data so standard transactions remain close to a fiat-indexed target cost.

## Why Guru-PEG Matters

In many blockchain networks, gas fees are denominated in the native token. If the native token price changes sharply, a fixed token-based fee can become expensive or unpredictable in fiat terms. This volatility creates friction for business workflows that require stable operating costs.

Guru-PEG addresses this by recalculating the minimum GXN gas price against a target fiat cost. For standard transfers, the current design target is approximately **$0.013**, subject to governance parameters, oracle availability, and network safeguards.

## How It Works

### Core Formula

At a high level, Guru-PEG applies the following relationship for a standard operation:

```
target_operation_fee_GXN = target_operation_fee_USD / current_GXN_price_USD
```

Where:

- **`target_operation_fee_USD`** - the target fiat-equivalent cost of a standard operation, such as a basic transfer.
- **`current_GXN_price_USD`** - the current USD price of GXN reported by the oracle network.
- **`target_operation_fee_GXN`** - the resulting GXN-denominated fee target, which is translated into gas pricing through protocol parameters.

When the GXN price rises, the required amount of GXN per transaction decreases. When the GXN price falls, the required amount of GXN increases. The goal is to keep the counterparty-facing fiat cost within a predictable range.

### Step-by-Step Mechanism

1. **Oracle feeds** - A decentralized oracle network collects GXN/USD price data from multiple on-chain and off-chain sources.
2. **Validation and aggregation** - Reported prices are compared against one another. Outlier filters remove anomalous readings, and the aggregated value is calculated through median or quorum-based logic.
3. **Protocol update** - The protocol reads the aggregated price and recalculates the GXN-denominated fee target using the formula above. Updates occur per block or at a configured interval.
4. **Inverse adjustment** - As GXN's price rises, fewer GXN tokens are needed per gas unit. As GXN's price falls, more GXN tokens are needed.
5. **Counterparty display** - Wallets and applications can show estimated fees in both GXN and the counterparty's preferred fiat currency.

## Safeguards & Fault Tolerance

Guru-PEG includes several safeguards to reduce oracle, volatility, and spam risks.

| Safeguard | Purpose |
|-----------|---------|
| **Oracle Quorum** | Price updates require agreement from a minimum number of independent oracle nodes, preventing a single point of manipulation. |
| **Outlier Filtering** | Readings that deviate significantly from the consensus group are excluded from the aggregation calculation. |
| **Price Deviation Checks** | If the reported price change exceeds a configurable threshold within a single interval, the protocol pauses the update until the deviation resolves. |
| **Gas Fee Floor & Ceiling** | A minimum and maximum bound on `min_gas_price_GXN` prevents fees from becoming zero (which would enable spam) or prohibitively high (which would hurt usability). |
| **Peg Buffer** | A reserve mechanism can absorb short-term price shocks, smoothing the fee curve during periods of extreme volatility. |
| **Emergency Fallback / Circuit Breaker** | If the oracle network becomes unresponsive or a critical fault is detected, the protocol can fall back to the last accepted price with conservative bounds until normal operations resume. |

## Known Limitations & Mitigations

### Oracle Latency

Guru-PEG price feeds update on a per-block basis or at a configured interval. If the GXN price moves rapidly between oracle updates, the gas price may briefly diverge from the current market rate. Price deviation checks and gas fee floor/ceiling safeguards reduce the impact of this divergence.

### MEV Considerations

Because Guru-PEG uses oracle-derived prices rather than an on-chain order book, common exchange-related MEV strategies, such as front-running and sandwich attacks, are not directly applicable to gas pricing itself.

**OPRS MEV Protection:** For Oracle Priced Reserve Swaps, the protocol enforces oracle staleness checks and maximum slippage tolerances per swap. If oracle updates lag market movement beyond configured thresholds, the swap can be repriced conservatively or cancelled. Applications should also use private transaction relays or similar protections where appropriate.

### Extreme Market Events

During periods of extreme token price volatility, the emergency fallback or circuit breaker may temporarily freeze gas price updates. The protocol then uses the last accepted price with a conservative buffer until oracle conditions stabilize.

## What This Enables

By making transaction costs more predictable, Guru-PEG supports:

- **Automated corporate settlements** - B2B payments that require predictable settlement costs.
- **Enterprise operations** - supply chain tracking, automated invoicing, and recurring on-chain workflows.
- **High-frequency use cases** - applications where volatile gas fees would create unacceptable cost uncertainty.
