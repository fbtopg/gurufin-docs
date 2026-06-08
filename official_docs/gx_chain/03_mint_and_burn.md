# Mint & Burn Mechanism

The Mint & Burn Mechanism enables automated issuance and redemption of sovereign stablecoins anchored to real-world fiat reserves. This process is tightly integrated with licensed banking partners via secure APIs, ensuring that every token minted or burned corresponds to an actual fiat movement in the banking system. This eliminates manual reconciliation delays and mitigates risks associated with double issuance or redemption.

---

**Minting Process**

When an institutional counterparty deposits fiat into a custodian bank account, the banking integration detects the incoming deposit and sends a deposit event to the GX chain gateway module. The gateway reconciles the event against bank settlement data, including the amount, sender, reference ID, and account details, then creates a mint request referencing the bank event ID with a unique idempotency key.

Licensed validators or authorized approval parties verify the deposit authenticity, compliance status, counterparty authorization, and reserve sufficiency. The system also checks that the same bank event or transaction identifier has not already been processed, preventing duplicate issuance from repeated, delayed, or replayed deposit events.

Once the required quorum approves the mint request, the mint transaction is submitted to the GX chain. When the transaction is executed in a block committed by the authorized validator set, the stablecoin contract updates the on-chain state by increasing circulating supply and crediting the counterparty’s custody account. Under GX chain’s PoA implementation of Tendermint BFT consensus, finality is reached when the validator quorum commits the block. At that point, the mint is final under the chain’s consensus rules and cannot be reversed through ordinary chain reorganization. This on-chain finality complements, but does not replace, the off-chain controls that verify fiat settlement, compliance status, idempotency, and reserve sufficiency before minting.

---

**Burning Process**

When an institutional counterparty redeems stablecoins, the burning process is initiated and fiat is released to the designated beneficiary account.

The counterparty submits a burn request via the GX chain gateway with a unique burn request ID. Validators verify compliance, reserve sufficiency, and counterparty authorization. The system confirms the burn request hasn't been processed before. Stablecoins are burned on-chain, reducing circulating supply. The transaction reaches deterministic finality. The bank API triggers fiat release to the designated beneficiary account, completing the settlement cycle.

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
