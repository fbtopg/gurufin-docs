# Liquidity & Rewards

While OPRS primarily relies on mint/burn mechanics, GuruDex utilizes liquidity inventory buffers to facilitate instant settlement and manage cross-chain transit times. 

**Virtual-Pair Mechanism**
Liquidity Providers (LPs) deposit stablecoins into these inventory buffers. To simplify multi-currency provision, LPs receive a single Virtual LP token representing their proportional stake across two underlying single-coin reserves.

**Fee Structure**
* **Retail Trades:** 0.3% base fee (dynamic based on reserve imbalance) + 0.05% protocol fee.
* **Institutional Trades:** 0.1% fixed fee + 0.05% protocol fee.

**Reward Distribution**
Fees accumulate continuously and are allocated to LP token holders every 24 hours. To ensure regulatory compliance and revenue fairness, institutional LP returns are capped at 7% annually. Excess rewards generated above this cap are redistributed to retail LPs.
