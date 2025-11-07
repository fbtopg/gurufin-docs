# GuruDEX System Architecture - 3-Layer Design

## Mermaid Diagram Code

```mermaid
graph TD
    subgraph Frontend["Frontend Layer"]
        A1[User DApp<br/>Web3 Interface]
        A2[Admin Tool<br/>Operator Panel]
    end
    
    subgraph ServerSide["Server Side Layer"]
        B1[KYC/AML Verification]
        B2[Real-time Exchange Rate Query<br/>External API]
        B3[Transaction Approval &<br/>Parameter Generation]
        B4[Oracle Price Feed<br/>Reporter Role]
    end
    
    subgraph SmartContract["Smart Contract Layer"]
        C1[HybridPoolManager<br/>Core]
        C2[Institutional<br/>Registry]
        C3[Oracle<br/>Validator]
        C4[Fee<br/>Distributor]
        C5[PoolFactory]
        C6[USGX Pool]
        C7[KRGX Pool]
        C8[JPGX Pool]
        C9[PHGX Pool]
        C10[... Scalable]
    end
    
    A1 --> ServerSide
    A2 --> ServerSide
    
    ServerSide --> C1
    
    C1 --> C2
    C1 --> C3
    C1 --> C4
    C1 --> C5
    
    C5 --> C6
    C5 --> C7
    C5 --> C8
    C5 --> C9
    C5 --> C10
    
    style Frontend fill:#e1f5ff
    style ServerSide fill:#fff4e1
    style SmartContract fill:#f0f0f0
    style C1 fill:#ffcccc
    style C5 fill:#ccffcc
```

## Alternative: Detailed Component View

```mermaid
flowchart TB
    subgraph Layer1["🖥️ Frontend Layer"]
        direction LR
        UserDApp["User DApp<br/>(Web3 Interface)"]
        AdminTool["Admin Tool<br/>(Operator Panel)"]
    end
    
    subgraph Layer2["⚙️ Server Side Layer"]
        direction TB
        KYC["KYC/AML Verification"]
        RateAPI["Real-time Exchange Rate<br/>Query (External API)"]
        TxApproval["Transaction Approval &<br/>Parameter Generation"]
        OracleFeed["Oracle Price Feed<br/>(Reporter Role)"]
    end
    
    subgraph Layer3["⛓️ Smart Contract Layer"]
        direction TB
        
        subgraph Core["Core Management"]
            HPM["HybridPoolManager"]
        end
        
        subgraph Services["Services"]
            IR["Institutional<br/>Registry"]
            OV["Oracle<br/>Validator"]
            FD["Fee<br/>Distributor"]
        end
        
        subgraph Factory["Pool Factory"]
            PF["PoolFactory"]
        end
        
        subgraph Pools["Liquidity Pools"]
            P1["USGX Pool"]
            P2["KRGX Pool"]
            P3["JPGX Pool"]
            P4["PHGX Pool"]
            P5["..."]
        end
        
        HPM --> IR
        HPM --> OV
        HPM --> FD
        HPM --> PF
        PF --> P1
        PF --> P2
        PF --> P3
        PF --> P4
        PF --> P5
    end
    
    Layer1 ==> Layer2
    Layer2 ==> Layer3
    
    style Layer1 fill:#e3f2fd
    style Layer2 fill:#fff3e0
    style Layer3 fill:#f5f5f5
    style HPM fill:#ffcdd2
    style PF fill:#c8e6c9
```

## Usage Instructions

1. Copy the code block above (including the triple backticks with `mermaid`)
2. Go to https://mermaid.live/
3. Paste the code in the editor
4. The diagram will render automatically
5. You can export as PNG, SVG, or edit further

## Diagram Type

- **Type**: `graph TD` (Top-Down graph) or `flowchart TB` (Top-Bottom flowchart)
- **Best for**: System architecture, layered designs
- **Alternative types**: Use `graph LR` for Left-Right orientation

