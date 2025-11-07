sequenceDiagram
    actor Institution
    participant Contract as Smart Contract
    participant Team as Operations Team
    participant Operator
    
    Institution->>Contract: 1. registerInstitution()<br/>(name, address, contact)
    Contract-->>Institution: Status: PENDING
    
    Note over Team: 2. Off-chain KYC/AML Verification<br/>• Corporate registration<br/>• Identity verification<br/>• Fund source verification<br/>• Compliance check
    
    alt Verification Passed
        Team->>Operator: Approve institution
        Operator->>Contract: 3. activateInstitution()<br/>(limits, fees, parameters)
        Contract-->>Institution: Status: ACTIVE
        
        Operator->>Contract: 4. allowCoinForInstitution()<br/>(institution, coins)
        Operator->>Contract: 4. authorizePoolForInstitution()<br/>(institution, pools)
        Contract-->>Institution: Access Granted
        
        Note over Institution: 5. Trading Enabled<br/>Can now perform swaps
    else Verification Failed
        Team-->>Institution: Registration Rejected
    end
