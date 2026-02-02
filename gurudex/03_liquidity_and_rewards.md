# Liquidity & Rewards

GuruDex incentivizes liquidity provision through a transparent fee distribution system. Liquidity providers deposit stablecoins into pools, earn proportional shares of swap fees, and receive rewards in regular 24-hour cycles.

---

**Virtual-Pair Mechanism**

LPs provide liquidity to two single-coin pools simultaneously and manage their stake through one unified Virtual LP token. This simplifies multi-currency liquidity provision—instead of managing separate LP positions for each pair, a single Virtual LP token represents stakes in both underlying pools.

---

**Fee Structure**

Swap fees vary by user type:

* **Retail trades** — 0.3% base fee (dynamic, increases with pool imbalance) + 0.05% protocol fee
* **Institutional trades** — 0.1% fixed fee + 0.05% protocol fee

Fees accumulate continuously and are distributed to LP token holders proportionally via the FeeDistributor contract.

---

**Reward Distribution**

Rewards are calculated and allocated every 24 hours based on LP token holdings. To ensure regulatory compliance and revenue fairness, institutional LP returns are capped at 7% annually. Excess rewards above this cap are redistributed to retail LPs, resulting in higher expected returns for retail participants.

---

*This page provides an introductory overview.*
