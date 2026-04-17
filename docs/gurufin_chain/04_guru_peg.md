# Guru-PEG

Guru-PEG (Price Equilibrium Governance) is a fee mechanism that provides fiat-indexed, predictable transaction costs, insulating users from native token price volatility and probabilistic gas spikes.

**The Mechanism Formula**
`Fee (GXN) = Fiat Target ÷ GXN Price × Surge Multiplier`

* **Fiat Target:** Base fee target in fiat (e.g., $0.013 for standard transfers).
* **GXN Price:** Current token price delivered via the on-chain oracle.
* **Surge Multiplier:** Congestion factor (1.0 normal load, up to 2.0x during peak demand).

*Example:* If Target = $0.013, GXN = $0.10, and Multiplier = 1.0, the transaction costs exactly 0.13 GXN. 

**Stability Guarantees**
A permissioned oracle network of vetted providers submits real-time FX observations using weighted medians. Automatic circuit breakers enforce price deviation limits and congestion caps to prevent extreme fee manipulation or systemic shocks.
