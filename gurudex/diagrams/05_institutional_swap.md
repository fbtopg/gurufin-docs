flowchart TD
    Start([🏦 Institution Initiates Swap])
    
    Start --> PreCheck
    
    PreCheck["🔍 Step 1: Pre-Trade Verification Off-chain<br/>Server checks:<br/>• KYC/AML Status: ACTIVE<br/>• Daily Limit: 1M USGX remaining<br/>• Custom Fee: 0.1%"]
    
    PreCheck --> UpdateOracle
    
    UpdateOracle["📡 Step 2: Oracle Update<br/>Server updates PriceOracle<br/>• Rate: 1 USD = 1,300 KRW<br/>• Time: 14:30:00<br/>• Confidence: 99.5%"]
    
    UpdateOracle --> Submit
    
    Submit["📝 Step 3: Submit Swap<br/>Institution calls swap function<br/>• Amount In: 100,000 USGX<br/>• Oracle Price: 1,300"]
    
    Submit --> CheckStatus
    
    CheckStatus{✅ Step 4:<br/>Status Check<br/>Institution ACTIVE?}
    
    CheckStatus -->|No| Reject1[❌ Rejected:<br/>Not Active]
    CheckStatus -->|Yes| ValidatePrice
    
    ValidatePrice["🔐 Step 5: Triple Validation<br/>Time: ✅ 2 min ago < 5 min<br/>Deviation: ✅ 0.08% < 2%<br/>Confidence: ✅ 99.5% > 95%"]
    
    ValidatePrice --> CheckLimit
    
    CheckLimit{📊 Step 6:<br/>Limit Check<br/>Within limits?}
    
    CheckLimit -->|No| Reject2[❌ Rejected:<br/>Limit Exceeded]
    CheckLimit -->|Yes| CalcOut
    
    CalcOut["🔢 Step 7: Calculate Output<br/>Formula: Out = In × Price × 1-Fee<br/>100,000 × 1,300 × 0.999<br/>= 129,870,000 KRGX"]
    
    CalcOut --> UpdateState
    
    UpdateState["📊 Step 8: Update State<br/>• Update pool reserves<br/>• Record daily volume<br/>• Store compliance logs"]
    
    UpdateState --> TransferFunds
    
    TransferFunds["💸 Step 9: Transfer Funds<br/>Send 129,870,000 KRGX<br/>Fee: 130,000 KRGX to distributor"]
    
    TransferFunds --> EmitEvent
    
    EmitEvent["📢 Step 10: Emit Event<br/>Institutional swap event<br/>for audit trail"]
    
    EmitEvent --> End([✅ Swap Complete<br/>Slippage: ~0%])
    
    Reject1 --> EndFail([❌ Swap Failed])
    Reject2 --> EndFail
    
    style Start fill:#e3f2fd
    style PreCheck fill:#fff3e0
    style UpdateOracle fill:#b3e5fc
    style ValidatePrice fill:#c8e6c9
    style CheckLimit fill:#ffccbc
    style CalcOut fill:#b3e5fc
    style End fill:#81c784
    style Reject1 fill:#ef9a9a
    style Reject2 fill:#ef9a9a
    style EndFail fill:#ef9a9a

