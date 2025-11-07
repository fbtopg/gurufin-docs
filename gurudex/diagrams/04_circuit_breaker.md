sequenceDiagram
    participant System as Monitoring System
    participant CB as Circuit Breaker
    participant Ops as Operations Team
    participant Pool as Trading Pool
    
    Note over System: Risk Event Detected
    System->>System: 1. Automated Monitoring<br/>• Price volatility > 5%<br/>• Liquidity drop > 20%<br/>• Suspicious patterns<br/>• Oracle failures
    
    System->>CB: Trigger Alert
    
    CB->>Pool: 2. Halt Operations<br/>• Block new swaps<br/>• Suspend liquidity changes<br/>• Halt institutional trading
    Pool-->>CB: Trading Suspended
    
    CB->>Ops: 3. Emergency Alert<br/>• Slack / Email / SMS<br/>• Risk scenario details<br/>• Dashboard activated
    
    Ops->>Ops: 4. Situation Analysis<br/>• Identify attack vector<br/>• Assess damage scope<br/>• Determine response
    
    alt Issue Resolved
        Ops->>CB: Approve Resume
        CB->>Pool: 5. Gradual Recovery<br/>• Test transactions<br/>• Phased resumption<br/>• Enhanced monitoring
        Pool-->>System: System Operational
    else Issue Persists
        Ops->>Ops: Escalate Response<br/>• Engage security team<br/>• Prepare upgrades
    end
