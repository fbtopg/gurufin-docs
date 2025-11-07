sequenceDiagram
    actor User as Retail User
    participant DApp
    participant HybridPool as HybridStablePool
    participant FeeCalc as Fee Calculator
    participant FeeDistributor
    
    User->>DApp: Initiate Swap<br/>1,000 USGX → KRGX<br/>minOut: 1,280,000 KRGX
    DApp->>HybridPool: swap(1000, true, 1280000)
    
    HybridPool->>HybridPool: 1. Verify User<br/>(Check rate limits)
    
    HybridPool->>FeeCalc: 2. calculateDynamicFee()
    FeeCalc-->>HybridPool: 0.3% (balanced pool)
    
    HybridPool->>HybridPool: 3. Fee Deduction<br/>997 USGX after fee
    
    HybridPool->>HybridPool: 4. AMM Calculation<br/>Δy = (y × Δx_fee) / (x + Δx_fee)<br/>Result: 1,286,710 KRGX
    
    HybridPool->>HybridPool: 5. Slippage Check<br/>1,286,710 >= 1,280,000 ✓
    
    HybridPool->>HybridPool: 6. Update Reserves<br/>Update pool state
    
    HybridPool->>FeeDistributor: Transfer 3 USGX fee
    HybridPool->>User: 7. Transfer 1,286,710 KRGX
    
    HybridPool->>HybridPool: 8. Emit SwapComplete Event
    
    HybridPool-->>DApp: Swap Successful
    DApp-->>User: Transaction Complete
