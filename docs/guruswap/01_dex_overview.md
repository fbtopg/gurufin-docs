# Guruswap Overview

Guruswap is an FX-specialized decentralized exchange designed for seamless swaps between sovereign stablecoins on the Gurufin Chain. 

**Why AMMs Fail for Stablecoin FX**
Automated Market Makers (AMMs) are built for volatile asset pairs where price discovery emerges from trading activity. However, stablecoin FX trading relies on real-world FX rates. Using an AMM for cross-currency stablecoins introduces unnecessary slippage and requires deep liquidity pools to function.

**The OPRS Solution**
Instead of AMMs, Guruswap uses an **Oracle Priced Reserve Swap (OPRS)** architecture. Because each GX stablecoin (e.g., GXUSD, GXKRW) is pegged to fiat on its own independent Layer-1 blockchain, Guruswap does not swap tokens inside a pool. Instead, it uses oracle-guided pricing to burn the input stablecoin on its native chain and mint the output stablecoin on its destination chain, ensuring swaps execute at precise market rates with zero slippage.

**Sovereign Chain Architecture**
Guruswap acts as the FX settlement hub, utilizing IBC (Inter-Blockchain Communication) to connect sovereign PoA chains (GXUSD Chain, GXKRW Chain) to the main Gurufin Chain (DPoS) for atomic cross-chain swaps.
