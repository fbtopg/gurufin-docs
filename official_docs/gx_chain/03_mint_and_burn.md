# Mint & Burn Mechanism

The mint and burn mechanism governs how GX stablecoins are issued and redeemed against fiat reserves. It connects on-chain token supply with verified banking events, compliance checks, and reserve controls.

## Minting Process

When an institutional counterparty deposits fiat into a custodian bank account, the banking integration detects the incoming deposit and sends a deposit event to the GX chain gateway module. The gateway reconciles the event against bank settlement data, including the amount, sender, reference ID, and account details, then creates a mint request referencing the bank event ID with a unique idempotency key.

Licensed validators or authorized approval parties verify deposit authenticity, compliance status, counterparty authorization, and reserve sufficiency. The system also checks that the same bank event or transaction identifier has not already been processed, reducing the risk of duplicate issuance from repeated, delayed, or replayed events.

Once the required quorum approves the mint request, the mint transaction is submitted to the GX chain. When the transaction is committed by the authorized validator set, the stablecoin contract increases circulating supply and credits the counterparty account. Under GX chain's PoA implementation of Tendermint/CometBFT consensus, finality is reached when the validator quorum commits the block. This on-chain finality complements the off-chain controls that verify fiat settlement, compliance status, idempotency, and reserve sufficiency before minting.

## Burning Process

When an institutional counterparty redeems stablecoins, the burn process removes the corresponding tokens from circulation and coordinates fiat release to the designated beneficiary account.

The counterparty submits a burn request through the GX chain gateway with a unique burn request ID. Validators verify compliance, reserve sufficiency, counterparty authorization, and request idempotency. After approval, tokens are burned or locked according to the corridor's redemption policy, and fiat release is initiated through the banking partner. The process is reconciled so token supply and reserve liabilities remain aligned.

## Key Safeguards

**Idempotency** prevents repeated processing of the same request from creating multiple token issuances or redemptions. The GX chain assigns unique identifiers to each bank event and checks if the request ID has already been executed before processing.

**Quorum Authorization** requires multi-party approval from licensed validators operating under Proof-of-Authority consensus. This enforces separation of duties and prevents unilateral issuance or redemption. Only upon reaching the required quorum threshold does the system proceed.

**Deterministic Finality** means that once a transaction is committed by the validator quorum, it is final under the chain's consensus rules. This supports predictable mint and burn settlement timing.

## Live Reserve Scanner (LRS)

Throughout minting and redemption, the Live Reserve Scanner monitors custody accounts and compares reserve balances with circulating supply. LRS provides telemetry to authorized supervisory entities and can report:

- Total reserves vs. circulation
- Cash headroom and maturity ladder
- Committed repo capacity and haircuts
- Redemption-queue depth with SLA meter
- Derived prudential metrics (GX-LCR, utilization ρ*)

This reduces the information gap that can develop during periods of market stress.

## RTGS Settlement Alignment

The redemption process is designed to align token destruction, reserve accounting, and fiat payout in a controlled sequence similar to real-time gross settlement (RTGS) principles. This helps reduce settlement risk and supports PFMI-aligned operational controls.

Together, these mechanisms are intended to keep stablecoin supply aligned with fiat reserves and regulatory obligations.
