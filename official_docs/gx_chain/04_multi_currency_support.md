# Multi-Currency Support

Each GX stablecoin operates on its own dedicated Layer-1 blockchain (e.g., GXUSD Chain, GXKRW Chain, GXEUR Chain). This model ensures that stablecoin issuance, reserve management, and compliance strictly adhere to local laws while providing operational independence.

**FX Settlement and PvP**
Cross-currency flows between sovereign chains utilize Payment-versus-Payment (PvP) settlement with escrowed holds via IBC/HTLCs. This ensures neither leg of a transaction settles unless both do, eliminating Herstatt (principal) risk.

For correlated stablecoin pairs traded on the Gurufin Chain (Guruswap), pools use low-curvature stable-swap curves to minimize slippage. Large tickets can be time-weighted (TWAP/TWAMM) to reduce market footprint. FX liquidity is supplied by regulated LPs, banks, and Payment Service Providers (PSPs).

**Onboarding New Currencies**
The GX framework is extensible. New sovereign chains require:
1. **Regulatory Assessment:** Evaluating the legal framework of the target jurisdiction.
2. **Validator Recruitment:** Licensing regulated local entities.
3. **Banking Integration:** Establishing custodial relationships with local banks.
4. **Technical Deployment:** Launching the chain with IBC connectivity to the Gurufin Chain.
