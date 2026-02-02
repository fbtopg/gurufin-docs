# Risk Mitigation

GuruDex implements a 4-layer defense strategy to protect against FX volatility, market manipulation, and operational risks. Each layer complements the others to ensure system robustness under adverse conditions.

---

**Layer 1: Reserve Fund**

An insurance fund holding 5–10% of pool liquidity compensates losses from rapid rate fluctuations. Reserves are managed separately for retail (3–5%) and institutional (5–10%) segments, with automatic replenishment from trading fees when thresholds are breached.

---

**Layer 2: Dynamic Fees**

Retail fees adjust in real-time based on pool utilization and market volatility. During normal conditions, fees remain at the 0.3% base. Under stress, fees can scale up to 0.63%, suppressing speculative trading and protecting pool equilibrium.

---

**Layer 3: Limits & Validation**

Individual swaps are capped at 5% of pool liquidity to prevent whale manipulation. Institutional trades undergo oracle triple validation:

* **Freshness** — Data must be less than 5 minutes old
* **Deviation** — Price must be within 1% of stored rate
* **Confidence** — Oracle confidence score must exceed 95%

---

**Layer 4: Circuit Breaker**

Trading halts automatically when critical thresholds are breached—such as >5% price swing, >20% liquidity drain, or suspicious transaction patterns. This secures response time for operators and prevents cascading losses during attacks or market crises.

---

*This page provides an introductory overview.*
