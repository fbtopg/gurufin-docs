## Prices are Determined by Real-World FX Rates

This module details how GuruDex accurately determines the exchange rates for stablecoin swaps by directly referencing real-world Foreign Exchange (FX) rates. Unlike traditional decentralized exchanges (DEXs) that rely on Automated Market Makers (AMMs) for price discovery, GuruDex employs an Oracle Priced Reserve Swap (OPRS) architecture to ensure stable and precise FX pricing.

### Key Concepts

*   **GX Stablecoins are Pegged to Individual Fiat Currencies**: Each GX stablecoin is designed to maintain a 1:1 peg with a specific fiat currency (e.g., GX_USD for USD, GX_EUR for EUR). This fundamental property makes their exchange rate against other GX stablecoins directly dependent on the underlying fiat FX rates.
*   **Each Fiat-Pegged Stablecoin Has Its Own GX Chain L1 Mainnet**: The architecture of GX stablecoins involves each stablecoin residing on its own dedicated Layer 1 (L1) mainnet within the GX Chain ecosystem. This structure, combined with the fiat peg, means that the intrinsic value of each stablecoin is derived from its corresponding real-world fiat currency.
*   **Why AMMs Don't Work for Stablecoin FX**: Automated Market Makers (AMMs) are primarily designed for volatile asset pairs where liquidity pools and mathematical formulas dictate price discovery based on supply and demand within the pool. However, for stablecoin FX, the price is not an emergent property of trading activity on a DEX. Instead, it is an established, external value determined by global fiat currency markets. Relying on an AMM for stablecoin FX would introduce artificial slippage and price deviations, which is undesirable for assets that are meant to be stable and mirror real-world value.
*   **Swaps Happen Via IBC (Inter-Blockchain Communication)**: Given that each fiat-pegged stablecoin exists on its own GX Chain L1 mainnet, cross-stablecoin swaps necessarily involve the Inter-Blockchain Communication (IBC) protocol. This allows for secure and trustless transfers of value between these sovereign chains. The pricing of these IBC-enabled swaps is then directly guided by external FX rate oracles, rather than an internal AMM.

### How Prices are Determined

GuruDex addresses the unique requirements of stablecoin FX trading by:

1.  **Direct Oracle Integration**: Instead of relying on AMM price discovery, GuruDex’s Oracle Priced Reserve Swap (OPRS) architecture directly integrates with reliable external oracles that fetch real-time, real-world FX rates. These oracles provide the authoritative exchange rates between different fiat currencies.
2.  **Maintaining Fiat Pegs**: The very nature of GX stablecoins, being pegged 1:1 to individual fiat currencies, means their on-chain exchange rates must accurately reflect the real-world FX rates of their underlying fiat counterparts.
3.  **Ensuring Price Stability**: This direct reference to real-world FX rates ensures that users experience minimal slippage and consistent pricing, mirroring what they would find in traditional FX markets. This is a critical differentiator from general-purpose DEXs.

### Important Details from Source Excerpts

The core philosophy of GuruDex, as highlighted in the source, is its specialization in stablecoin FX trading where "price stability and accurate FX rates are critical." The text explicitly states that GuruDex uses an "**Oracle Priced Reserve Swap (OPRS)** architecture purpose-built for on-chain stablecoin FX trading," contrasting it directly with AMMs. It further clarifies that "AMMs (Automated Market Makers) are designed for volatile asset pairs where price discovery emerges from trading activity," which is fundamentally different from stablecoin FX where "price discovery" is not needed, as prices are externally set by real-world markets.