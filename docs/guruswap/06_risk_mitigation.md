# Risk Mitigation

Guruswap implements a 4-layer defense strategy to protect against FX volatility and market manipulation.

**Layer 1: Reserve Fund**
An insurance fund holding 5–10% of total liquidity compensates for losses from rapid rate fluctuations. Reserves are segmented by user type (Retail: 3–5%, Institutional: 5–10%) and automatically replenish via trading fees.

**Layer 2: Dynamic Fees**
Retail fees adjust in real-time based on reserve utilization. During market stress, the standard 0.3% base fee can scale up to 0.63% to suppress speculative trading and protect equilibrium.

**Layer 3: Limits & Validation**
Individual retail swaps are capped at 5% of available liquidity to prevent whale manipulation. All trades are subject to strict Oracle Triple Validation (Freshness, Deviation, Confidence).

**Layer 4: Circuit Breakers**
Trading halts automatically when critical thresholds are breached (e.g., >5% price swing, >20% liquidity drain, or suspicious transaction velocity). This secures response time for operators and prevents cascading losses.
