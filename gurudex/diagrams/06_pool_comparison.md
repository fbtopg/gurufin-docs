graph TB
    subgraph Single["Single Pool (Shared)"]
        direction TB
        S1["One Pool for All Users"]
        S2["Retail + Institutional<br/>Liquidity Mixed"]
        S3["Capital Efficiency: Best<br/>Swap Efficiency: Best<br/>Revenue Fairness: Worst<br/>Risk Management: Risky"]
        S4["Overall Score: 72/100"]
        S1 --> S2 --> S3 --> S4
    end
    
    subgraph Separated["Separated Pools (Independent)"]
        direction TB
        P1["Two Separate Pools"]
        P2["Retail Pool | Institutional Pool<br/>Completely Separated"]
        P3["Capital Efficiency: Worst<br/>Swap Efficiency: Worst<br/>Revenue Fairness: Best<br/>Risk Management: Safe"]
        P4["Overall Score: 58/100"]
        P1 --> P2 --> P3 --> P4
    end
    
    subgraph Hybrid["Hybrid Dual-Layer (Optimal)"]
        direction TB
        H1["Core Pool 50%<br/>+ Dedicated Pools 50%"]
        H2["Layer 1: Shared Base Pool<br/>Layer 2: Retail + Inst Dedicated"]
        H3["Capital Efficiency: Excellent<br/>Swap Efficiency: Excellent<br/>Revenue Fairness: Best<br/>Risk Management: Safe"]
        H4["Overall Score: 88/100 ★"]
        H1 --> H2 --> H3 --> H4
    end
    
    Start([Pool Architecture Choice])
    Start --> Single
    Start --> Separated
    Start --> Hybrid
    
    Single --> Compare[Comparison Analysis]
    Separated --> Compare
    Hybrid --> Compare
    
    Compare --> Winner["Winner: Hybrid Model"]

