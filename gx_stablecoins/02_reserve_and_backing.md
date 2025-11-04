# Reserve & Backing

The integrity and stability of the GX Stablecoin network rest fundamentally on its robust reserve and backing framework. This page provides a comprehensive overview of the 1:1 fiat backing principle, the composition of reserves, and the advanced transparency mechanisms employed, including the 24/7 live proof-of-reserves system. Additionally, it explains the application of Basel regulatory liquidity metrics adapted for the blockchain environment, ensuring both regulatory compliance and operational resilience.

---

## 1:1 Fiat Backing Principle

GX Stablecoins are fully collateralized by fiat currency held in reserve at a 1:1 ratio. This means that for every stablecoin unit issued on the GX Stablecoin chain, an equivalent amount of fiat currency is securely held in reserve. This strict backing model underpins the stablecoin’s price stability and trustworthiness, ensuring that holders can redeem their tokens for fiat currency at any time without risk of shortfall.

The 1:1 fiat backing is enforced through automated minting and burning mechanisms integrated with licensed banking partners via secure APIs. This integration guarantees that token issuance only occurs upon verified receipt of fiat funds, and redemption triggers the corresponding fiat transfer, maintaining a continuous parity between tokens in circulation and fiat reserves.

---

## Reserve Composition

The reserve assets consist primarily of highly liquid and low-risk instruments to maintain capital preservation and immediate liquidity. The composition is designed to optimize safety, regulatory compliance, and operational efficiency.

| Reserve Asset Type              | Description                                                                                   | Characteristics                          |
|--------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------|
| **Cash**                       | Fiat currency held in segregated accounts at licensed financial institutions                  | Immediate liquidity, zero market risk  |
| **Ultra-Short Government Bills** | Short-dated government securities with maturities typically under 3 months, capped by policy | Low credit risk, slightly higher yield than cash, high liquidity |

The inclusion of ultra-short government bills, subject to a predefined cap, allows the reserve to earn modest returns without compromising liquidity or safety. This prudent diversification aligns with best practices for reserve management and regulatory expectations.

---

## 24/7 Live Proof-of-Reserves Mechanism

Transparency is a cornerstone of the GX Stablecoin ecosystem. To provide continuous assurance to users and regulators, the network implements a 24/7 live proof-of-reserves (PoR) system. This mechanism leverages blockchain technology and cryptographic proofs to enable real-time verification of reserve holdings against circulating stablecoin supply.

### Key Features of the Proof-of-Reserves System

- **Real-Time Reserve Scanning:** Automated and continuous scanning of reserve accounts and instruments to verify balances.
- **Cryptographic Verification:** Use of zero-knowledge proofs and Merkle tree structures to confirm reserves without exposing sensitive financial details.
- **Public Accessibility:** Proof-of-reserves data is published on-chain and accessible via public dashboards, enabling independent audits and community scrutiny.
- **Automated Alerts:** Any discrepancies or anomalies trigger immediate alerts to governance and compliance teams for rapid investigation.

This live PoR system surpasses traditional periodic audits by providing ongoing, tamper-evident transparency, reinforcing confidence in the stablecoin’s backing.

---

## Basel LCR/NSFR-Adapted Metrics

To align with international banking regulatory standards, the GX Stablecoin reserve management incorporates liquidity metrics adapted from the Basel Committee on Banking Supervision’s Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR). These metrics are customized to the blockchain context to ensure that reserves maintain sufficient liquidity and stable funding profiles.

| Metric                     | Description                                                                                          | GX Stablecoin Adaptation                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| **Liquidity Coverage Ratio (LCR)** | Measures the ability to cover net cash outflows over a 30-day stress period using high-quality liquid assets (HQLA). | GX-LCR(H) ratio tracks the proportion of cash and ultra-short government bills relative to potential redemption demands within 30 days. |
| **Net Stable Funding Ratio (NSFR)** | Assesses the stability of funding sources over a one-year horizon to ensure long-term resilience. | GX-NSFR metric monitors the stable funding of reserve assets, emphasizing cash and short-term government bills with stable counterparty relationships. |

By applying these Basel-aligned metrics, the GX Stablecoin network ensures that its reserve portfolio is not only fully backed but also resilient under stress scenarios, meeting supervisory-grade liquidity standards.

---

## Summary Table: Reserve & Backing Overview

| Aspect                       | Description                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------|
| **Fiat Backing Ratio**        | 1:1 fiat currency backing for every stablecoin issued                                             |
| **Reserve Composition**       | Cash and capped ultra-short government bills                                                      |
| **Transparency Mechanism**    | 24/7 live proof-of-reserves with cryptographic verification and public dashboards                  |
| **Regulatory Alignment**      | Basel LCR and NSFR adapted metrics (GX-LCR(H) and GX-NSFR) for liquidity and funding stability     |
| **Automated Mint/Burn**       | Bank API integration with multi-party authorization and deterministic finality                     |

---

## Conclusion

The GX Stablecoin chain’s reserve and backing framework exemplifies a rigorous, transparent, and regulatory-compliant approach to stablecoin issuance. By combining strict 1:1 fiat collateralization with a prudent reserve asset mix and continuous proof-of-reserves transparency, the network delivers a stable, trustworthy digital currency suitable for global cross-border payments, institutional settlement, and DeFi applications. The incorporation of Basel liquidity metrics further reinforces the system’s resilience, providing stakeholders with confidence in the stablecoin’s stability and operational soundness.