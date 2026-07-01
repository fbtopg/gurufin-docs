# Technical Action Items & Documentation Gaps

This document tracks technical explanations that need additional architectural detail before broader public or institutional review.

## 1. Inventory Buffer Rebalancing

**Gap:** OPRS uses managed inventory buffers to support fast execution, but sustained one-sided flow can deplete the buffer for a target currency.
* **Action required:** Document the rebalancing process across fees, IBC routing, banking partner top-ups, and corridor-specific limits.

## 2. Cross-Chain Latency vs. Single-Chain Finality

**Gap:** The documentation needs to clearly distinguish sub-second single-chain finality from complete cross-chain execution over IBC.
* **Action required:** Keep all latency claims explicit about whether they describe single-chain confirmation or end-to-end cross-chain settlement.

## 3. Oracle Latency and MEV Controls

**Gap:** OPRS depends on oracle freshness, deviation checks, and confidence thresholds. During fast-moving FX markets, stale prices could expose inventory buffers to adverse execution.
* **Action required:** Define the specific staleness checks, slippage controls, circuit breakers, and transaction-routing protections used to reduce oracle-latency extraction.

## 4. Validator Economics

**Gap:** GX chains rely on regulated PoA validators, and enterprise-grade operations can require HSMs, monitoring, compliance screening, and service-level processes.
* **Action required:** Explain validator incentives, fee revenue, service revenue, and non-financial strategic reasons a licensed institution may operate validator infrastructure.
