## 01 Dex Overview (Getting Started)

The "01 Dex Overview (Getting Started)" module introduces GuruDex, an FX-specialized decentralized exchange, and guides users through its core concepts and initial access points. This page serves as a foundational entry for understanding how GuruDex operates and where to find more detailed information.

## What is GuruDex?

GuruDex is an FX-specialized decentralized exchange designed for seamless swaps between sovereign stablecoins on the Gurufin Chain. Unlike general-purpose DEXs that rely on Automated Market Makers (AMMs), GuruDex utilizes an **Oracle Priced Reserve Swap (OPRS)** architecture. This architecture is purpose-built for on-chain stablecoin FX trading, emphasizing price stability and accurate FX rates.

## Key Concepts and Relationships

### Gurudex Overview

GuruDex is primarily concerned with stablecoin FX trading, a domain where price discovery and peg maintenance are critical. The `GuruDex Overview` clarifies that its key differentiator is its specialization.

### Why OPRS, Not AMM?

The module highlights the fundamental difference between GuruDex's OPRS mechanism and traditional AMMs. AMMs are often limited in stablecoin FX trading due to challenges with price discovery, slippage, liquidity, and peg maintenance. OPRS addresses these by providing a solution specifically tailored to accurate, low-slippage stablecoin swaps.

### Architecture

The `Architecture` of GuruDex, specifically the OPRS architecture, is a core concept. Further details are explored in the "02 OPRS Architecture" and "04 Smart Contracts" documentation. This architecture is closely related to the `GX Stablecoins` that GuruDex handles, which themselves have a specific `Mint/Burn Mechanism` described in "03 Mint & Burn". The `Developer` concept is supported by further documentation regarding the architecture and smart contracts.

### GX Stablecoins

GuruDex facilitates trading of `GX Stablecoins`. These are sovereign stablecoins, each pegged 1:1 to a respective fiat currency. Examples mentioned in context include `USGX Chain`, `KRGX Chain`, `EURGX Chain`, and `JPGX Chain`, each representing a specific jurisdictional currency. The architecture of GX Chain is described as a network of independent Layer-1 chains.

### Oracle Priced Reserve Swap (OPRS)

The `Oracle Priced Reserve Swap (OPRS)` is the central mechanism of GuruDex. Instead of relying on liquidity pools, OPRS uses `oracle-priced FX rates` to guide a `mint/burn mechanism`. This ensures trades execute at precise market rates with **no slippage**. Related concepts such as `oracle security`, `freshness`, `deviation`, and `confidence` are critical for the reliable functioning of OPRS, with "triple validation" being a key security measure for institutional trades. The `How OPRS Works` section further details this process, including `IBC Settlement` for cross-chain stablecoin movements.

### Getting Started and Testnet Access

For developers and users looking to engage with GuruDex, `Getting Started` is facilitated through readily available `Documentation` and `Testnet Access`. The Testnet provides a sandbox environment with specific network configuration parameters (Chain ID: `guru_631-1`, RPC Endpoint: `https://trpc.gurufin.io`, etc.) and a faucet for obtaining test tokens.

### Compliance Integration

While not a primary focus of this overview, `Compliance Integration` is mentioned, indicating the platform's commitment to regulatory frameworks. This involves aspects like `institutional registry`, `transaction monitoring`, and adherence to `jurisdictional rules`.

### Related Documentation

The module provides convenient quick links to `Related Documentation` for deeper dives into topics like `Settlement Layer` (Gurufin Chain Whitepaper) and `Reserves` (GX Chain Overview).

## Important Details from Source Excerpts

*   GuruDex is specialized for FX trading of sovereign stablecoins on the Gurufin Chain.
*   It utilizes an Oracle Priced Reserve Swap (OPRS) architecture, deliberately avoiding traditional AMMs.
*   OPRS ensures **zero slippage** and relies on real-world oracle rates.
*   The mint-and-burn mechanism for stablecoins is guided by oracle FX rates for swaps.
*   Security for institutional trades includes "triple validation" checks for `freshness` (data < 5 minutes old), `deviation` (< 1% from stored rate), and `confidence` (> 95% oracle score).
*   Testnet access is available with specific network parameters and a faucet for test tokens.
*   GuruDex is part of a larger ecosystem including the Gurufin Chain (a DPoS Layer-1 settlement layer) and GX Chain (a network of sovereign stablecoin PoA chains).