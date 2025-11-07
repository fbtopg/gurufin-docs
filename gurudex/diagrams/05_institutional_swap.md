sequenceDiagram
    actor Institution as Bank/Institution
    participant Server
    participant Oracle as PriceOracle
    participant Registry as InstitutionalRegistry
    participant Pool as HybridStablePool
    participant FeeDistributor
    
    Note over Server: Pre-Trade Verification
    Institution->>Server: Request swap approval
    Server->>Server: 1. Verify KYC/AML Status<br/>Daily Limit: 1M USGX<br/>Used: 200K USGX<br/>Custom Fee: 0.1%
    
    Server->>Oracle: 2. updatePrice()<br/>Rate: 1 USD = 1,300 KRW<br/>Confidence: 99.5%
    Oracle-->>Server: Price Updated
    
    Institution->>Pool: 3. swap(100000, oraclePrice)
    
    Pool->>Registry: 4. Check Institution Status
    Registry-->>Pool: Status: ACTIVE ✓
    
    Pool->>Oracle: 5. Validate Oracle Price
    Oracle->>Oracle: Triple Validation:<br/>• Time: 2 min < 5 min ✓<br/>• Deviation: 0.08% < 2% ✓<br/>• Confidence: 99.5% > 95% ✓
    Oracle-->>Pool: Price Valid
    
    Pool->>Registry: 6. Check Limits<br/>perTx: 100K <= 500K ✓<br/>daily: 300K <= 1M ✓
    Registry-->>Pool: Within Limits
    
    Pool->>Pool: 7. Calculate Output<br/>100,000 × 1,300 × 0.999<br/>= 129,870,000 KRGX
    
    Pool->>Pool: 8. Update State<br/>Record volume
    
    Pool->>FeeDistributor: Transfer 130,000 KRGX fee
    Pool->>Institution: 9. Transfer 129,870,000 KRGX
    
    Pool->>Pool: 10. Emit Institutional Swap Event
    
    Pool-->>Institution: Swap Complete<br/>Slippage: ~0%
