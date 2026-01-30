# Mint & Burn Mechanism

The Mint & Burn Mechanism enables automated issuance and redemption of sovereign stablecoins anchored to real-world fiat reserves. This process is tightly integrated with licensed banking partners via secure APIs, ensuring that every token minted or burned corresponds to an actual fiat movement in the banking system. This eliminates manual reconciliation delays and mitigates risks associated with double issuance or redemption.

---

**Minting Process**

When a user deposits fiat into a custodian bank account, an automated minting event is initiated on the GX chain. The process follows these steps:

The bank API detects the fiat deposit and sends an event notification to the GX chain gateway module. A mint request is created referencing the bank event ID with a unique transaction identifier. Licensed validators review and verify the deposit authenticity, compliance status, and reserve sufficiency. The system performs an idempotency check to ensure this specific deposit hasn't already been processed. Upon reaching quorum approval, the mint transaction executes on-chain. The transaction reaches deterministic finality within sub-second, and stablecoins are credited to the user's wallet.

---

**Burning Process**

When a user redeems stablecoins, the burning process is initiated and fiat is released to the user. The user submits a burn request via the GX chain gateway with a unique burn request ID. Validators verify compliance, reserve sufficiency, and user authorization. The system confirms the burn request hasn't been processed before. Stablecoins are burned on-chain, reducing circulating supply. The transaction reaches deterministic finality. The bank API triggers fiat release to the user's bank account, completing the redemption cycle.

---

**Key Safeguards**

**Idempotency** ensures that repeated processing of the same request does not result in multiple token issuances or redemptions. The GX chain assigns unique identifiers to each bank event and checks if the request ID has already been executed before processing.

**Quorum Authorization** requires multi-party approval from licensed validators operating under Proof-of-Authority consensus. This enforces separation of duties and prevents unilateral issuance or redemption. Only upon reaching the required quorum threshold does the system proceed.

**Deterministic Finality** guarantees that once a transaction is committed, it becomes irreversible and immediately recognized by all network participants. Leveraging Tendermint BFT consensus, the GX chain achieves sub-second finality, enabling rapid and predictable settlement.

---

**Live Reserve Scanner (LRS)**

Throughout both minting and burning processes, the Live Reserve Scanner operates continuously, monitoring custody accounts in real time. LRS ensures every issued token remains fully backed and provides on-demand telemetry to authorized supervisory entities. The Scanner reports:

- Total reserves vs. circulation
- Cash headroom and maturity ladder
- Committed repo capacity and haircuts
- Redemption-queue depth with SLA meter
- Derived prudential metrics (GX-LCR, utilization ρ*)

This removes the informational opacity that historically triggers panic during market stress.

---

**RTGS Settlement Alignment**

The burning process follows a real-time gross settlement (RTGS) sequence, ensuring fiat liabilities are settled with finality before token destruction. This design aligns with PFMI (Principles for Financial Market Infrastructures) expectations and practices from systems like TARGET (Eurosystem), Fedwire (Federal Reserve), and BOJ-NET.

---

These mechanisms ensure that stablecoin supply is always fully backed and accurately reflects real-world fiat reserves, maintaining the trustworthiness and regulatory alignment of GX stablecoins.
