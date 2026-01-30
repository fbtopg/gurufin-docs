# Guru-PEG

Guru-PEG (Price Equilibrium Governance) is Gurufin Chain's innovative fee mechanism that provides fiat-indexed, predictable transaction costs. Unlike traditional blockchains where gas fees fluctuate wildly with token prices and network congestion, Guru-PEG ensures users can reliably forecast their transaction expenses.

Traditional blockchains have unpredictable fees that spike during congestion and fluctuate with token prices. This makes it difficult to budget for transactions and renders micropayments uneconomical. Guru-PEG solves this by maintaining stable, predictable fees regardless of market conditions, with costs indexed to fiat currency.

---

**How Guru-PEG Works**

The fee in GXN is calculated as follows:

```
Fee (GXN) = Fiat Target ÷ GXN Price × Surge Multiplier
```

* **Fiat Target** — The base fee in fiat (e.g. $0.013 for a standard transfer), set by governance.
* **GXN Price** — Current GXN price in fiat from the oracle network (e.g. $0.10).
* **Surge Multiplier** — Congestion factor: 1.0 under normal load, up to ~2× during high demand.

*Example:* With Fiat Target = $0.013, GXN Price = $0.10, and Surge Multiplier = 1.0:

```
Fee (GXN) = 0.013 ÷ 0.10 × 1.0 = 0.13 GXN
```

So the user pays 0.13 GXN and experiences a stable cost of about $0.013.

Standard L1 transfers cost approximately $0.013 and asset/NFT operations around $0.040. These fee targets are adjusted periodically (annually or quarterly) using the Consumer Price Index (CPI) for inflation, with a maximum step cap of 2% per update.

---

**Predictability Guarantees**

Automatic circuit breakers prevent extreme fee changes. Price deviation limits cap fee adjustments if oracle prices move too rapidly, congestion caps prevent fees from exceeding 2-3x normal rates, and governance can override in abnormal market conditions.

A permissioned oracle network ensures accurate, manipulation-resistant price feeds. Vetted providers—exchanges, data firms, and institutional operators—submit signed observations to the on-chain Oracle Module. The module enforces quorum rules, staleness bounds, and outlier filters, then aggregates inputs using weighted median to resist manipulation. Provider bonds and slashing mechanisms incentivize honest reporting.

---

**Benefits**

Retail users know exact transaction costs before confirming. Businesses can build sustainable pricing models on predictable fees. Developers can simplify UX by hiding gas complexity from end users. Institutions can budget accurately for high-volume operations.

Guru-PEG transforms blockchain transaction fees from a volatile, unpredictable expense into a stable, manageable cost—a critical step toward mainstream adoption.
