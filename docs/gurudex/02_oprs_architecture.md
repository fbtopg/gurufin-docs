# OPRS Architecture

The Oracle Priced Reserve Swap (OPRS) is the core engine of GuruDex, replacing liquidity pool dynamics with oracle-guided mint/burn mechanics.

**Step-by-Step Swap Flow**
*Example: User swaps 1,000 GXUSD → GXKRW*
1. User initiates a swap on GuruDex.
2. The Oracle provides a real-time FX rate (e.g., 1 USD = 1,300 KRW).
3. 1,000 GXUSD is burned on the GXUSD Sovereign Chain.
4. 1,298,700 GXKRW is minted on the GXKRW Sovereign Chain.
5. IBC ensures atomic cross-chain settlement.

**Oracle Validation**
To prevent manipulation, all oracle prices undergo triple validation before execution:
* **Freshness:** Data must be less than 5 minutes old.
* **Deviation:** Price must be within 1% of the previously stored rate.
* **Confidence:** The oracle confidence score must exceed 95%.
If validation fails, the swap safely reverts.
