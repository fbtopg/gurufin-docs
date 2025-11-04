
# Hybrid Execution Model

The Gurufin Chain introduces a sophisticated **Hybrid Execution Model** that combines the strengths of two distinct trading mechanisms: an **Automated Market Maker (AMM)** for retail users and a **Request-for-Quote (RFQ)** system for institutional clients. This dual approach allows Gurufin to serve a wide range of market participants, ensuring deep liquidity, efficient price discovery, and optimal trading experiences for all.

## The Two Sides of the Hybrid Model

| Component | Target Audience | Mechanism | Key Features |
|---|---|---|---|
| **Automated Market Maker (AMM)** | Retail Users & Small Traders | Utilizes a Uniswap v3-style concentrated liquidity model. | - **Dynamic Fees**: Fees adjust based on pool imbalance and volatility.<br>- **Open & Permissionless**: Anyone can provide liquidity and trade.<br>- **High Efficiency**: Concentrated liquidity minimizes slippage for smaller trades. |
| **Request-for-Quote (RFQ)** | Institutional Clients & Large Traders | Allows institutions to request quotes directly from professional market makers. | - **Minimal Slippage**: Large trades are executed at a quoted price, avoiding the price impact of AMMs.<br>- **Custom Pricing**: Institutions can receive tailored pricing from market makers.<br>- **Privacy**: Trade details are not broadcast to the public mempool. |

## How It Works

The Hybrid Execution Model operates within a single, unified liquidity pool for each stablecoin pair. This innovative design, known as the **HybridStablePool**, allows both retail and institutional trades to be settled against the same pool of assets, maximizing liquidity efficiency.

When a user initiates a swap, the system identifies the user type and routes the trade to the appropriate execution path:

- **Retail Trades**: Are routed to the AMM, where the price is determined by the bonding curve.
- **Institutional Trades**: Are routed to the RFQ system, where they are matched with quotes from registered market makers.

This architecture ensures that the Gurufin Chain can handle both a high volume of small retail trades and large institutional block trades without compromising on performance or efficiency.

### Hybrid Execution Flow Diagram

```mermaid
flowchart TD
    A[User Initiates Swap] --> B{Identify User Type}
    
    B -->|Retail User| C[Route to AMM Path]
    B -->|Institutional User| D[Route to RFQ Path]
    
    C --> C1[HybridStablePool<br/>Retail Area]
    C1 --> C2[Uniswap v3 Style<br/>Concentrated Liquidity]
    C2 --> C3[Dynamic Fees<br/>Based on Pool Imbalance]
    C3 --> C4[Price from Bonding Curve<br/>x × y = k]
    C4 --> E[Execute Trade]
    
    D --> D1[HybridStablePool<br/>Institutional Area]
    D1 --> D2[Request Quote from<br/>Market Makers]
    D2 --> D3[Oracle-Based Pricing<br/>Real-time Exchange Rate]
    D3 --> D4[Custom Fee Structure<br/>Minimal Slippage]
    D4 --> E
    
    E --> F[Update Pool Reserves]
    F --> G[Settlement Complete]
    
    style C1 fill:#e1f5ff
    style D1 fill:#ffe1f5
    style E fill:#e1ffe1
```
