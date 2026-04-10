# Reserve & Backing

The integrity and stability of GX stablecoins rest fundamentally on a robust reserve and backing framework. Every stablecoin issued on a GX chain is fully collateralized by fiat currency held in reserve at a 1:1 ratio. This strict backing model underpins the stablecoin's price stability and trustworthiness, ensuring that holders can redeem their tokens for fiat currency at any time without risk of shortfall.

The 1:1 fiat backing is enforced through automated minting and burning mechanisms integrated with licensed banking partners via secure APIs. Token issuance only occurs upon verified receipt of fiat funds, and redemption triggers the corresponding fiat transfer, maintaining continuous parity between tokens in circulation and fiat reserves.

---

**Reserve Composition**

The reserve assets consist primarily of highly liquid and low-risk instruments to maintain capital preservation and immediate liquidity. Reserve composition may differ by jurisdiction based on local regulatory requirements and banking partner capabilities.

**At launch, 100% of reserves are maintained in cash** at licensed custodian banks with binding concentration limits to ensure immediate redemption capacity. Over time, only where expressly permitted by domestic regulation, a **capped fraction** may be allocated to ultra-short Treasury bills (typically under 3 months maturity) managed on a roll-down ladder.

Liquidity against such securities is raised via **pre-arranged repo facilities—not secondary-market sales**—ensuring same-day cash availability without forced asset liquidation. This prudent diversification aligns with best practices for reserve management and regulatory expectations.

---

**24/7 Live Proof-of-Reserves**

Transparency is a cornerstone of the GX ecosystem. To provide continuous assurance to users and regulators, the network implements a 24/7 live proof-of-reserves system leveraging blockchain technology and cryptographic proofs.

The system features real-time reserve scanning that automatically and continuously verifies reserve account balances. Cryptographic verification uses zero-knowledge proofs and Merkle tree structures to confirm reserves without exposing sensitive financial details. Proof-of-reserves data is published on-chain and accessible via public dashboards, enabling independent audits and community scrutiny. Any discrepancies or anomalies trigger immediate alerts to governance and compliance teams for rapid investigation.

This live proof-of-reserves system surpasses traditional periodic audits by providing ongoing, tamper-evident transparency.

---

**Liquidity Standards**

To align with international banking regulatory standards, GX reserve management incorporates liquidity metrics adapted from Basel Committee standards. These include the Liquidity Coverage Ratio (LCR) to measure the ability to cover net cash outflows over a 30-day stress period, and the Net Stable Funding Ratio (NSFR) to assess funding stability over a one-year horizon.

By applying these Basel-aligned metrics, the GX network ensures that its reserve portfolio is not only fully backed but also resilient under stress scenarios, meeting supervisory-grade liquidity standards.

The horizon-specific liquidity coverage formula is:

$$
\text{GX-LCR}(H) = \frac{H_0 + (1 - h) \cdot \rho}{\text{ES}_\alpha[R_D^H]}
$$

**Notation:**
- \(H_0\) — same-day cash headroom  
- \(\rho\) — committed repo capacity  
- \(h\) — conservative haircut  
- \(\text{ES}_\alpha[R_D^H]\) — Expected Shortfall of redemptions over horizon \(H\) at confidence level \(\alpha\)

The target is GX-LCR(H) ≥ 1 with a supervisory buffer. The utilization ratio \(\rho^* = \lambda/\mu\) must remain below 1 for operational stability, where \(\lambda\) is the redemption arrival rate and \(\mu\) is the service rate.
