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
