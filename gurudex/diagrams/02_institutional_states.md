stateDiagram-v2
    [*] --> NONE: New Institution
    
    NONE --> PENDING: registerInstitution()
    
    PENDING --> ACTIVE: activateInstitution()<br/>(After KYC/AML)
    PENDING --> REVOKED: Verification Failed
    
    ACTIVE --> SUSPENDED: Compliance Issue<br/>or Risk Alert
    ACTIVE --> REVOKED: Serious Violation
    
    SUSPENDED --> ACTIVE: Issue Resolved<br/>reactivateInstitution()
    SUSPENDED --> REVOKED: Permanent Ban
    
    REVOKED --> [*]: End
    
    note right of NONE
        Unregistered
        Can call registerInstitution()
    end note
    
    note right of PENDING
        Awaiting Verification
        Cannot trade
    end note
    
    note right of ACTIVE
        Fully Operational
        Can perform all approved trades
    end note
    
    note right of SUSPENDED
        Temporarily Halted
        Under investigation
    end note
    
    note right of REVOKED
        Permanently Banned
        All operations forbidden
    end note

