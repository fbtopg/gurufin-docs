flowchart TD
    Start([🚨 Risk Event Occurs])
    
    Start --> Monitor
    
    Monitor["👁️ Step 1: Automated Monitoring<br/>System detects anomaly:<br/>• Price volatility > 5%<br/>• Liquidity drop > 20%<br/>• Suspicious tx pattern<br/>• Oracle failures"]
    
    Monitor --> Trigger
    
    Trigger["⚡ Step 2: Circuit Breaker Triggered<br/>Immediately halt affected operations:<br/>• Block new swaps<br/>• Suspend liquidity add/remove<br/>• Halt institutional trading"]
    
    Trigger --> Alert
    
    Alert["📢 Step 3: Emergency Alert<br/>Notify operations team:<br/>• Slack / Email / SMS alerts<br/>• Risk scenario details<br/>• System status dashboard"]
    
    Alert --> Analyze
    
    Analyze["🔍 Step 4: Situation Analysis<br/>Team investigates:<br/>• Identify attack vector<br/>• Assess damage scope<br/>• Determine response"]
    
    Analyze --> Decision{Issue<br/>Resolved?}
    
    Decision -->|No| Escalate["⚠️ Escalate Response<br/>• Engage security team<br/>• Consider upgrades<br/>• Prepare recovery plan"]
    
    Escalate --> Analyze
    
    Decision -->|Yes| Resume
    
    Resume["✅ Step 5: System Recovery<br/>Gradually resume functions:<br/>• Perform test transactions<br/>• Phased resumption<br/>• Enhanced monitoring"]
    
    Resume --> End([✅ System Operational])
    
    style Start fill:#ffcdd2
    style Monitor fill:#fff9c4
    style Trigger fill:#ef5350,color:#fff
    style Alert fill:#ff9800,color:#fff
    style Analyze fill:#b3e5fc
    style Decision fill:#ffccbc
    style Escalate fill:#ff9800
    style Resume fill:#c8e6c9
    style End fill:#81c784

