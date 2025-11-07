flowchart TB
    subgraph Layer1["Frontend Layer"]
        direction LR
        UserDApp["User DApp<br/>(Web3 Interface)"]
        AdminTool["Admin Tool<br/>(Operator Panel)"]
    end
    
    subgraph Layer2["Server Side Layer"]
        direction TB
        KYC["KYC/AML Verification"]
        RateAPI["Real-time Exchange Rate<br/>Query (External API)"]
        TxApproval["Transaction Approval &<br/>Parameter Generation"]
        OracleFeed["Oracle Price Feed<br/>(Reporter Role)"]
    end
    
    subgraph Layer3["Smart Contract Layer"]
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
