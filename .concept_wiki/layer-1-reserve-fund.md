# 05 Risk Mitigation: Layer 1 - Reserve Fund

The "05 Risk Mitigation" module of GuruDex outlines a comprehensive, multi-layered strategy designed to protect the system from various risks, including FX volatility, market manipulation, and operational failures. This wiki page focuses specifically on **Layer 1: Reserve Fund**, the foundational element of GuruDex's defense mechanism.

## Overview

Layer 1: Reserve Fund establishes an essential insurance fund that acts as the initial buffer against unexpected losses. Its primary purpose is to compensate for financial discrepancies arising from rapid fluctuations in exchange rates, thereby safeguarding the overall stability and liquidity of GuruDex's trading pools.

## Key Concepts

### Layer 1: Reserve Fund

The Reserve Fund is a dedicated pool of assets maintained to absorb losses. It functions as a first line of defense, providing a direct mechanism to cover shortfalls that might otherwise impact user funds or the operational health of the platform.

### Fund Allocation and Management

The Reserve Fund is designed to hold **5–10% of the total pool liquidity**. This percentage is strategically chosen to provide substantial coverage without overly encumbering the operational liquidity of the pools.

A critical aspect of the Reserve Fund's design is its segregation and targeted management:
*   **Retail Segment:** A portion of the fund, specifically **3–5%**, is allocated to cover potential losses within the retail trading segment.
*   **Institutional Segment:** A larger portion, **5–10%**, is designated for the institutional trading segment, reflecting the potentially higher value and impact of institutional trades.

### Automatic Replenishment

To ensure the Reserve Fund remains robust and effective, an automated mechanism is in place for its replenishment. When the fund's balance falls below predefined thresholds (indicating it has been utilized to cover losses), it is automatically topped up using a portion of the trading fees collected by the platform. This ensures the fund remains adequately capitalized over time without requiring manual intervention.

## Relationship to Other Risk Mitigation Layers

While Layer 1: Reserve Fund is the initial defense, it works in conjunction with the subsequent layers of GuruDex's risk mitigation strategy:

*   **Layer 2: Dynamic Fees** complements the Reserve Fund by actively deterring excessive risk-taking or speculative trading during periods of stress, reducing the likelihood of the Reserve Fund needing to be frequently drawn upon.
*   **Layer 3: Limits & Validation** prevents large-scale manipulations that could quickly deplete the Reserve Fund.
*   **Layer 4: Circuit Breaker** acts as a final safeguard, halting trading entirely in extreme scenarios to prevent catastrophic losses that even a substantial Reserve Fund might struggle to cover.

Together, these layers form a robust and adaptive defense system, with the Reserve Fund providing the financial bedrock for resilience.