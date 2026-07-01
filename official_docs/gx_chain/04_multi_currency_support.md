# Multi-Currency Support

Each GX stablecoin operates on its own dedicated Layer-1 chain, such as GXUSD Chain, GXKRW Chain, or GXEUR Chain. This structure allows issuance, reserve management, validator policy, and compliance controls to be adapted to each jurisdiction.

**FX Settlement and PvP**

Cross-currency flows between jurisdiction-specific chains use Payment-versus-Payment (PvP) settlement with escrowed holds through IBC and HTLC-style coordination. This reduces principal risk by preventing one leg of a transaction from settling unless the corresponding leg also settles.

For stablecoin pairs executed through Guruswap, the Oracle Priced Reserve Swap (OPRS) model uses oracle-guided pricing and managed inventory buffers rather than relying solely on AMM price discovery. Large-value orders can use time-weighted execution to reduce market impact. FX liquidity may be supplied by regulated liquidity providers, banks, and payment service providers.

**Onboarding New Currencies**

The GX framework is extensible. New currency chains require:

1. **Regulatory assessment:** Review the legal and licensing framework of the target jurisdiction.
2. **Validator onboarding:** Recruit and approve regulated local entities that can operate validator infrastructure.
3. **Banking integration:** Establish custodial and payment relationships with licensed local banks.
4. **Technical deployment:** Launch the chain with IBC connectivity to Gurufin Chain, monitoring, and operational runbooks.
