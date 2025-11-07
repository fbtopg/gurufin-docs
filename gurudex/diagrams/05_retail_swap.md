flowchart TD
    Start([👤 Retail User Initiates Swap])
    
    Start --> Input["📝 Input Parameters<br/>• Direction: USGX → KRGX<br/>• Amount In: 1,000 USGX<br/>• Min Amount Out: 1,280,000 KRGX"]
    
    Input --> Verify
    
    Verify["✅ Step 1: User Verification<br/>Check user type via InstitutionalRegistry<br/>Verify rate limits"]
    
    Verify --> CalcFee
    
    CalcFee["💰 Step 2: Calculate Dynamic Fee<br/>Check pool imbalance<br/>Formula: Fee = Base × 1 + imbalance%<br/>Result: 0.3% (balanced pool)"]
    
    CalcFee --> Deduct
    
    Deduct["➖ Step 3: Fee Deduction<br/>1,000 USGX × 0.997 = 997 USGX"]
    
    Deduct --> CalcOut
    
    CalcOut["🔢 Step 4: Calculate Output AMM<br/>Formula: Δy = y × Δx_fee / x + Δx_fee<br/>Result: ~1,286,710 KRGX"]
    
    CalcOut --> CheckSlip
    
    CheckSlip{⚠️ Step 5:<br/>Slippage Check<br/>1,286,710 >= 1,280,000?}
    
    CheckSlip -->|Yes| Update
    CheckSlip -->|No| Revert[❌ Transaction Reverted<br/>Slippage too high]
    
    Update["📊 Step 6: Update State<br/>• Update pool reserves<br/>• Accumulate fees<br/>• Update imbalance state"]
    
    Update --> Transfer
    
    Transfer["💸 Step 7: Transfer Funds<br/>Send 1,286,710 KRGX to user<br/>Send 3 USGX fee to FeeDistributor"]
    
    Transfer --> Event
    
    Event["📢 Step 8: Emit Event<br/>Record transaction on-chain<br/>for transparency"]
    
    Event --> End([✅ Swap Complete])
    Revert --> EndFail([❌ Swap Failed])
    
    style Start fill:#e3f2fd
    style CalcFee fill:#fff9c4
    style CalcOut fill:#b3e5fc
    style CheckSlip fill:#ffccbc
    style Update fill:#c8e6c9
    style Transfer fill:#c8e6c9
    style End fill:#81c784
    style Revert fill:#ef9a9a
    style EndFail fill:#ef9a9a

