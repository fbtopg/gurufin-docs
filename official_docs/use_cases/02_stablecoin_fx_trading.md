# Institutional FX Settlement & Execution on Gurufin

Gurufin Chain supports institutional FX settlement by connecting jurisdiction-specific GX stablecoin chains with Guruswap, the ecosystem's FX execution layer. The goal is to make cross-currency stablecoin settlement faster, more transparent, and easier to integrate with regulated workflows.

**The OPRS Advantage in FX**

Many DeFi exchanges rely on Automated Market Makers (AMMs), where price discovery comes from pool balances and arbitrage. Gurufin uses the **Oracle Priced Reserve Swap (OPRS)** architecture, where cross-currency stablecoin swaps reference validated oracle prices and managed inventory buffers. This design is intended to reduce execution slippage for standard order sizes while preserving controls for stressed market conditions.

**Execution Workflows**

* **Corporate spot execution:** Institutional counterparties can swap GX stablecoins, such as GXUSD to GXKRW, through OPRS. Dynamic fees adjust based on inventory buffer utilization, helping maintain balanced liquidity. Oracle latency and market volatility may affect execution quality during fast-moving conditions.
* **Institutional execution:** Verified institutions can execute larger FX orders using oracle pricing, custom compliance limits, and defined fee schedules.

### Inventory Buffer Rebalancing Mechanism

When sustained asymmetric flows reduce a local inventory buffer, for example heavy GXKRW to GXUSD demand, the protocol can trigger a rebalancing process:

1. **Dynamic fee adjustment:** Swap fees increase on the depleted side to discourage further one-sided flow and encourage reverse flow.
2. **Cross-chain inventory routing:** Excess stablecoins can be routed through IBC to chains with inventory surplus and exchanged at oracle-guided rates.
3. **Banking API top-up:** If local reserves and banking partner rules permit, licensed partners can replenish inventory through the automated mint/burn API.

**Advanced Settlement Applications**

* **Cross-chain arbitrage:** Qualified participants can capture price differences across jurisdiction-specific stablecoin chains using IBC-based Payment-versus-Payment settlement. Single-chain finality targets are sub-second, while cross-chain IBC settlement typically takes 3-10 seconds depending on relayers and the chain pair.
* **Tokenized FX derivatives:** Developers can build tokenized FX derivatives that settle on-chain and reference OPRS spot rates where appropriate.
* **Enterprise treasury management:** Corporates can automate FX conversions and manage global liquidity with predictable fees, compliance controls, and clearer settlement status.
