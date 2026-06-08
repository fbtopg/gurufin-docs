# Retail-to-Institutional Language Audit

**Date:** 2026-06-08
**Researcher:** Researcher Agent
**Scope:** All official docs under `official_docs/`
**Objective:** Identify retail/individual-focused language in documentation for GX stablecoins (GXUSD, GXKRW, etc.), FX, settlement, and cross-border payments — and recommend institutional/corporate alternatives.

---

## Executive Summary

The documentation has an **institutional core intent** (e.g., sections on Institutional DeFi, B2B payments, tokenized FX derivatives, treasury management) but is **riddled with retail/individual-facing language** throughout. Key terms like "user," "retail," "consumer-friendly," "point-of-sale," "migrant workers," and "migrant remittances" appear repeatedly, undermining the institutional positioning.

**Criticality:** HIGH — This language mismatch could confuse enterprise prospects, investors, and compliance partners who evaluate Gurufin as institutional infrastructure.

---

## Findings by File (Sorted by Priority)

### 🔴 CRITICAL — Stablecoin FX Trading (`use_cases/02_stablecoin_fx_trading.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | Title | **"Stablecoin FX Trading on Gurufin"** | **"Institutional FX Settlement & Execution"** | "Trading" implies speculative/retail activity; settlement and execution are B2B terms. |
| 2 | First para | "traders can execute seamless, secure, and efficient FX trading, arbitrage, and derivative strategies." | "Institutions can execute seamless, secure, and efficient FX settlement, arbitrage, and derivative strategies." | "Traders" = retail speculators. Use "Institutions" or "Corporate treasuries." |
| 3 | Header | **"Retail Spot Trading"** | **"Corporate Spot Execution"** | "Retail Spot Trading" is the single most retail-coded term in the entire doc. |
| 4 | Line under #3 | "Users swap sovereign stablecoins..." | "Corporates swap sovereign stablecoins..." | "Users" → "Corporates" / "Institutional counterparties" |
| 5 | Line under #3 | "Dynamic fees adjust based on the utilization of underlying inventory buffers" | (Acceptable, but add corporate context) | Keep mechanism description; add "serving institutional throughput needs." |
| 6 | "Cross-Chain Arbitrage" section | "Traders can exploit price differentials..." | "Institutions can execute cross-chain arbitrage..." | Arbitrage as an institutional risk-mitigation tool, not speculation. |
| 7 | Tokenomics section (below) | "traders" | "Institutional counterparties" | See #6 |

**Confidence:** HIGH — This is the most retail-coded document and needs the most aggressive rewriting.

---

### 🔴 CRITICAL — Mint & Burn Mechanism (`gx_chain/03_mint_and_burn.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | Mint intro | "When a **user** deposits fiat..." | "When an **institutional counterparty** deposits fiat..." | "User" implies individual retail. Mint/burn is a B2B/corporate flow. |
| 2 | Mint intro | "...credited to the **user's wallet**" | "...credited to the **counterparty's custody account**" | "Wallet" is retail terminology. Use "custody account" or "corporate wallet." |
| 3 | Burn intro | "When a **user** redeems stablecoins..." | "When an **institutional counterparty** initiates redemption..." | Same rationale. |
| 4 | Burn flow | "The bank API triggers fiat release to the **user's bank account**..." | "...to the **counterparty's designated bank account**..." | "User's bank account" → "designated beneficiary account." |
| 5 | Burn flow | "completing the **redemption cycle**" | "completing the **settlement cycle**" | "Redemption" is a retail/individual term. "Settlement" is institutional. |

**Confidence:** HIGH — Mint/burn is a pure B2B flow; "user" language is inappropriate.

---

### 🟠 HIGH — GX Chain Overview (`gx_chain/01_overview.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | Fees & Gas | "~**$0.01 per retail transaction**" | "~$0.01 per **standard settlement transaction**" | "Retail transaction" is the word itself. Use "settlement transaction." |
| 2 | Fees & Gas | "**predictable point-of-sale usability**" | "**predictable transaction-level cost for B2B settlement**" | "Point-of-sale" = retail commerce. Irrelevant for institutional use. |
| 3 | Offline Payments | "**low-value flows**" | "**low-frequency B2B flows**" | "Low-value" is a retail concept. Institutional flows are about reliability, not value size. |
| 4 | Offline Payments | "**intermittent-connectivity environments**" | "**disconnected or bandwidth-constrained logistics environments**" | Add corporate context (e.g., shipping, warehousing). |

**Confidence:** HIGH — "Retail transaction" and "point-of-sale" are direct contradictions to institutional positioning.

---

### 🟠 HIGH — Guru-PEG (`gurufin_chain/04_gx_peg.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | "Why Guru-PEG Matters" | "friction for **everyday transactions**" | "friction for **time-critical settlement workflows**" | "Everyday transactions" = consumer use. Use "settlement workflows." |
| 2 | "Why Guru-PEG Matters" | "unsuitable for **retail payments** or enterprise operations" | "unsuitable for **high-frequency B2B settlement** or enterprise operations" | Drop "retail payments." |
| 3 | How It Works | "**consumer-friendly rate**" | "**predictable enterprise-grade rate**" | "Consumer-friendly" → "enterprise-grade." |
| 4 | What This Enables | "**Retail payments** — micro-transactions and point-of-sale payments..." | "**High-Frequency Settlement** — automated B2B payments, recurring corporate transfers..." | Entire bullet is retail-focused. |
| 5 | What This Enables | "**Retail payments**" | "**Automated Corporate Settlements**" | Same. |
| 6 | MEV Protection | "preventing MEV bots from **extracting value**" | "preventing MEV bots from **extracting value during institutional order execution**" | Add context for institutional relevance. |
| 7 | Tokenomics section | "The burn rate is dynamically adjustable by **governance**..." | (Acceptable) | Governance is fine. |

**Confidence:** HIGH — 6 retail-coded terms in a section that should be about enterprise fee predictability.

---

### 🟠 HIGH — Tokenomics (`gurufin_chain/05_tokenomics.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | Economic Sustainability | "every **transaction** contributes" | "every **settlement** contributes" | "Transaction" is neutral; "settlement" is institutional. |
| 2 | Economic Sustainability | "network **adoption** and token **scarcity**" | "**throughput volume** and token **supply dynamics**" | "Adoption" and "scarcity" are crypto-retail buzzwords. |
| 3 | "Token value accrual" | "**token value accrual**" | "**network value accrual**" | "Token value" is retail/speculative language. |

**Confidence:** MEDIUM — Less critical than FX docs but "token value accrual" and "adoption" are retail crypto terminology.

---

### 🟡 MEDIUM — Cross-Border Payments (`use_cases/01_cross_border_payments.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | Intro | "tailored for both **retail remittances** and enterprise-level B2B transactions." | "tailored for **corporate cross-border payments and institutional settlement workflows**." | Drop "retail remittances." It contradicts the institutional thesis. |
| 2 | Cost-Efficiency | "**retail-grade fee stability**" | "**predictable, enterprise-grade fee stability**" | "Retail-grade" is a downgrade signal. |
| 3 | Use Case 1 | "**Retail Remittance Service**" — "A fintech application can enable **migrant workers** to deposit fiat..." | "**Cross-Border B2B Payment Service**" — "An enterprise payment platform can facilitate corporate-to-corporate fiat transfers..." | "Migrant workers" and "remittance" are retail/consumer use cases. Replace with B2B example. |
| 4 | Use Case 1 Benefit | "Near-instant settlement, predictable low fees" | "Guaranteed atomic settlement, predictable B2B fees" | Frame for B2B. |

**Confidence:** HIGH — The "Retail Remittance Service" use case is the most overt retail example in the entire docs and should be replaced.

---

### 🟡 MEDIUM — Protocol Overview (`gurufin_chain/01_protocol_overview.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | Key Characteristics | "Low cost — Minimal gas fees make **micro-transfers** and frequent settlements practical." | "Low cost — Predictable gas fees enable high-frequency B2B settlement workflows." | "Micro-transfers" is retail language. |

**Confidence:** MEDIUM — Single instance, easily fixable.

---

### 🟡 MEDIUM — Compliance & Regulation (`gx_chain/05_compliance_and_regulation.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | KYC/AML | "**Users** and institutions undergo identity verification..." | "**Counterparties** undergo identity verification..." | "Users" lumps individuals and institutions together. In an institutional docs, use "counterparties" or "participants." |
| 2 | KYC/AML | "Different **wallet tiers** dictate transaction permissions" | "**Access tiers** dictate transaction permissions" | "Wallet tiers" is a retail wallet UX concept. Use "access tiers." |

**Confidence:** MEDIUM — Minor terminology adjustments.

---

### 🟡 MEDIUM — Validator Guide (`gurufin_chain/07_validator_guide.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | Economic Sustainability | "high-frequency enterprise workflows (supply chain tracking, automated invoicing, **micro-settlements**)" | "high-frequency enterprise workflows (supply chain tracking, automated invoicing, **batch settlements**)" | "Micro-settlements" is retail terminology. Use "batch settlements" or "high-frequency settlements." |

**Confidence:** MEDIUM — Single instance.

---

### 🟢 LOW — Reserve & Backing (`gx_chain/02_reserve_and_backing.md`)

| # | Line/Context | Current Language (Retail) | Recommended Language (Institutional) | Rationale |
|---|-------------|--------------------------|--------------------------------------|-----------|
| 1 | First para | "ensuring that **holders** can redeem their tokens" | "ensuring that **counterparties** can redeem their tokens" | "Holders" is a retail investor term. Use "counterparties" or "token holders (institutional counterparties)." |

**Confidence:** LOW — Minor terminology fix.

---

### 🟢 LOW — Governance (`gurufin_chain/06_governance.md`)

No retail-specific language detected. Already institutional in tone.

**Confidence:** HIGH — Clean.

---

### 🟢 LOW — What is Gurufin? (`introduction/02_what_is_gurufin.md`)

No retail-specific language detected. Already institutional.

**Confidence:** HIGH — Clean.

---

### 🟢 LOW — Interoperability (`gurufin_chain/03_interoperability.md`)

No retail-specific language detected.

**Confidence:** HIGH — Clean.

---

### 🟢 LOW — Institutional DeFi (`use_cases/03_institutional_defi.md`)

No retail language detected. Already institutional.

**Confidence:** HIGH — Clean.

---

## Summary Statistics

| Category | Count |
|----------|-------|
| 🔴 CRITICAL (must fix) | 11 instances across 2 files |
| 🟠 HIGH (should fix) | 10 instances across 3 files |
| 🟡 MEDIUM (recommended) | 6 instances across 4 files |
| 🟢 LOW (nice to fix) | 2 instances across 2 files |
| **TOTAL** | **29 instances** |
| Files requiring changes | 8 of 12 |
| Files already institutional | 4 of 12 |

## Files Requiring the Most Aggressive Rewriting

1. **`stablecoin_fx_trading.md`** — Title, section headers, and most body text is retail-coded. Needs wholesale rewrite.
2. **`mint_and_burn.md`** — Every instance of "user" should be "institutional counterparty."
3. **`gx_chain/01_overview.md`** — "Retail transaction" and "point-of-sale" are direct contradictions.
4. **`gx_peg.md`** — 6 retail terms in a single section.
5. **`cross_border_payments.md`** — "Retail Remittance Service" use case should be replaced with a B2B/corporate example.

## Recommended Language Replacement Dictionary

| Retail Term | Institutional Replacement |
|-------------|--------------------------|
| user | institutional counterparty, corporate participant, enterprise client |
| retail | B2B, enterprise-grade, institutional |
| consumer-friendly | enterprise-grade, predictable, SLA-compliant |
| point-of-sale | B2B settlement, corporate payment |
| migrant workers / remittance | corporate entities, cross-border B2B payments |
| micro-transactions / micro-settlements | high-frequency settlements, batch settlements |
| everyday transactions | time-critical settlement workflows |
| holders | counterparties, institutional participants |
| wallet tiers | access tiers, compliance tiers |
| adoption | throughput volume, network utilization |
| token value accrual | network value accrual |
| trading | settlement, execution |
| redemption cycle | settlement cycle |
| low-value flows | low-frequency B2B flows |

## Next Steps

1. **Hand off to Writer** to rewrite the 8 affected documentation files.
2. **Prioritize** by criticality: FX Trading doc first, then Mint & Burn, then GX Overview, then Guru-PEG.
3. **Review** the revised docs with the Architect to ensure technical accuracy is preserved.
4. **Update** the SUMMARY.md if section titles change (e.g., "Stablecoin FX Trading" → "Institutional FX Settlement").

---

*End of audit.*
