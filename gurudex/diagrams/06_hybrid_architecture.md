graph TB
    subgraph Layer1["Layer 1: Shared Core Pool (50%)"]
        direction LR
        Core["🏊 Core Pool<br/>Accessible to Both<br/>Large trades<br/>Minimize slippage"]
        
        RetailLiq1["Retail<br/>Liquidity"] --> Core
        InstLiq1["Institutional<br/>Liquidity"] --> Core
    end
    
    subgraph Layer2["Layer 2: Dedicated Pools (50%)"]
        direction LR
        
        subgraph RetailDedicated["Retail Dedicated"]
            RetailPool["🏊 Retail Pool<br/>Retail-only trades<br/>High fee revenue"]
            RetailLiq2["Retail<br/>Liquidity"] --> RetailPool
        end
        
        subgraph InstDedicated["Institutional Dedicated"]
            InstPool["🏊 Inst Pool<br/>Inst-only trades<br/>Low fee revenue"]
            InstLiq2["Institutional<br/>Liquidity"] --> InstPool
        end
    end
    
    SmartContract["🤖 Smart Contract<br/>Intelligent Routing"]
    
    SmartContract --> Layer1
    SmartContract --> Layer2
    
    Trader([User/Institution])
    Trader --> SmartContract
    
    Core --> |Fee Distribution| RetailLP[Retail LPs]
    Core --> |Fee Distribution| InstLP[Inst LPs]
    RetailPool --> |Fee Distribution| RetailLP
    InstPool --> |Fee Distribution| InstLP
    
    style Layer1 fill:#b3e5fc
    style Layer2 fill:#fff9c4
    style Core fill:#4fc3f7
    style RetailPool fill:#81c784
    style InstPool fill:#ffb74d
    style SmartContract fill:#e1bee7

