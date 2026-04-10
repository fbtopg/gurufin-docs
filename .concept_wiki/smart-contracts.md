## 02 Hybrid Pools (Smart Contracts)

This module focuses on the "02 Hybrid Pools" concept within the GuruDex ecosystem, specifically detailing the **Oracle Priced Reserve Swap (OPRS) architecture** as an alternative to traditional Automated Market Maker (AMM) pools. It elaborates on how **Smart Contracts** facilitate this unique mechanism for stablecoin Foreign Exchange (FX) trading.

### Key Principles of OPRS

The **Key Principle** behind OPRS is that trade prices are determined by real-world oracle rates, rather than by on-chain supply and demand dynamics within liquidity pools. This design ensures trades execute at precise market rates with **zero slippage**, which is particularly well-suited for stablecoin FX trading.

### How Oracle Priced Reserve Swap (OPRS) Works

The **OPRS Architecture** operates on a mint-and-burn mechanism guided by oracle FX rates, rather than maintaining liquidity pools with constant product formulas. The process for a user initiating a swap is as follows:

1.  **User initiates a swap**: A user desires to exchange one stablecoin for another (e.g., USGX for KRGX).
2.  **Oracle provides real-time FX rate**: An oracle fetches and provides the current, accurate exchange rate between the two stablecoins (e.g., 1 USD = 1,300 KRW). This **Oracle Validation** is crucial for the reliability of the system.
3.  **Input stablecoin is burned**: The stablecoin that the user is exchanging (input stablecoin) is burned on its respective sovereign chain (e.g., 1,000 USGX is burned on the USGX Chain).
4.  **Output stablecoin is minted**: A corresponding amount of the desired stablecoin (output stablecoin) is minted on its respective sovereign chain, based on the oracle's real-time FX rate and deducting any fees (e.g., 1,298,700 KRGX is minted on the KRGX Chain).
5.  **IBC atomic settlement**: The entire transaction, including the burning and minting of stablecoins across different chains, is settled atomically using **IBC atomic settlement**, ensuring that the entire operation either succeeds or fails together.

### Why OPRS for Stablecoin FX?

The OPRS architecture is specifically designed for the nuances of stablecoin FX trading. Traditional AMMs are prone to impermanent loss and slippage, which are undesirable for assets pegged to real-world currencies. By leveraging real-time oracle rates, OPRS provides a more stable, efficient, and reliable method for exchanging stablecoins, directly addressing the requirements for institutional adoption.

### Smart Contracts and Sovereign Chain Integration

The entire OPRS process is orchestrated by **Smart Contracts**. These contracts handle the logic for input stablecoin burning, output stablecoin minting, and the integration with oracles to fetch real-time FX rates. The system also relies on **Sovereign Chain Integration**, as each stablecoin (e.g., USGX, KRGX) resides on its own dedicated chain within the GX Stablecoin Network. The Gurufin Chain, built on Cosmos SDK, acts as a neutral FX/DeFi settlement hub, facilitating cross-chain operations via **IBC-first interoperability**.