# Reserve & Backing

GX stablecoins are designed to be backed 1:1 by fiat reserves held with regulated custodians. The reserve framework is intended to support redemption reliability, price stability, and supervisory transparency for institutional counterparties.

The 1:1 backing model is supported by automated minting and redemption controls integrated with licensed banking partners. Issuance requires verified receipt of fiat funds, and redemption requests are reconciled against both token supply and reserve balances.

## Reserve Composition

Reserve assets are expected to prioritize liquidity, capital preservation, and regulatory eligibility. Composition may differ by jurisdiction based on local rules and banking partner capabilities.

**At launch, reserves are expected to be maintained in cash** at licensed custodian banks, with concentration limits designed to preserve redemption capacity. Over time, and only where permitted by domestic regulation, a capped portion may be allocated to ultra-short Treasury bills, typically with maturities under three months, managed through a roll-down ladder.

Liquidity against eligible securities would be raised through **pre-arranged repo facilities rather than forced secondary-market sales**, helping preserve same-day cash availability under stress.

## 24/7 Live Proof-of-Reserves

GX uses a live proof-of-reserves model to provide continuous visibility into reserve coverage for counterparties, supervisors, and network participants.

The system monitors reserve account balances and compares them with on-chain circulation. Cryptographic verification can use zero-knowledge proofs and Merkle tree structures to confirm reserve coverage without exposing sensitive account details. Proof-of-reserves data is published on-chain and through dashboards where appropriate. Discrepancies or anomalies trigger alerts for governance, operations, and compliance review.

Live proof-of-reserves is intended to complement, not replace, formal audits and supervisory reporting.

## Liquidity Standards

GX reserve management incorporates liquidity metrics adapted from international banking standards, including concepts similar to the Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR). These metrics assess whether reserve assets and backup liquidity are sufficient under stressed redemption scenarios.

The goal is to maintain both full backing and resilience under stress, while allowing jurisdiction-specific supervisors to define exact reserve requirements.

The horizon-specific liquidity coverage formula is:

### Plain-Language Summary

The formula measures whether the network has enough same-day liquidity and committed backup funding to cover a stressed redemption scenario over a defined time horizon. The numerator represents available liquidity: cash on hand plus committed repo capacity after haircuts. The denominator represents expected stressed redemptions. A ratio above 1 means available liquidity is greater than the modeled stress requirement. The utilization ratio \(\rho^*\) should remain below 1 so backup facilities are not expected to be fully consumed during normal operations.

### Technical Formula

For technical reviewers, the calculation is:

$$
\text{GX-LCR}(H) = \frac{H_0 + (1 - h) \cdot \rho}{\text{ES}_\alpha[R_D^H]}
$$

**Notation:**
- \(H_0\) — same-day cash headroom  
- \(\rho\) — committed repo capacity  
- \(h\) — conservative haircut  
- \(\text{ES}_\alpha[R_D^H]\) — Expected Shortfall of redemptions over horizon \(H\) at confidence level \(\alpha\)

The target is GX-LCR(H) ≥ 1 with a supervisory buffer. The utilization ratio \(\rho^* = \lambda/\mu\) should remain below 1 for operational stability, where \(\lambda\) is the redemption arrival rate and \(\mu\) is the service rate.
