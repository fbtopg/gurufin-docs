# Technical Action Items & Gaps

This document tracks critical technical gaps in the current Gurufin documentation that require deeper architectural clarification prior to public or institutional review.

## 1. The Inventory Buffer Paradox (Asymmetric Flow)
**The Gap:** The OPRS architecture relies on cross-chain minting and burning, supposedly requiring minimal liquidity. However, it also uses LP "inventory buffers" to facilitate instant settlement. If there is sustained asymmetric trading (e.g., massive volume swapping GXKRW to GXUSD), the GXUSD buffer will drain rapidly. 
* **Action Required:** Document the exact rebalancing mechanism. How does the protocol rebalance local reserves across sovereign chains without relying on the arbitrageurs the OPRS system aims to replace?

## 2. Cross-Chain Latency vs. "Instant" Claims
**The Gap:** The documentation repeatedly advertises "sub-second deterministic finality." While Tendermint BFT achieves this on a *single* chain, an OPRS swap requires burning on Chain A, transmitting an IBC packet through the Hub, and minting on Chain B. The physics of cross-chain consensus means this cannot be sub-second. 
* **Action Required:** Clarify the distinction between single-chain settlement finality and complete cross-chain execution times to avoid setting unrealistic technical expectations.

## 3. Oracle Latency and Front-Running Vectors
**The Gap:** OPRS relies entirely on the Oracle Network with triple validation (freshness, deviation, confidence). During extreme real-world macroeconomic volatility, FX markets move in milliseconds. If the on-chain oracle is even seconds behind, MEV bots could execute risk-free arbitrage against the inventory buffers by front-running the oracle updates.
* **Action Required:** Define the specific MEV protection mechanisms and explain how the protocol prevents oracle latency extraction.

## 4. Sovereign Validator Economics
**The Gap:** The GX chains are secured by regulated, licensed PoA validators. Operating enterprise-grade nodes with HSMs, real-time compliance screening, and SLA guarantees is expensive. 
* **Action Required:** Detail the economic incentive and exact business model. If gas fees are pegged to ~$0.01 per transaction, explain what makes running a GX Chain validator profitable or worthwhile for a licensed financial institution.
