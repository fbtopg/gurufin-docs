gantt
    title Circuit Breaker Response Timeline
    dateFormat HH:mm:ss
    axisFormat %H:%M:%S
    
    section Detection
    Normal Operation           :done, t1, 09:30:00, 15s
    Anomaly Detected          :crit, t2, 09:30:15, 1s
    
    section Activation
    Circuit Breaker Triggered :crit, t3, 09:30:16, 1s
    Trading Halted            :crit, t4, 09:30:16, 4s
    
    section Response
    Alert Sent                :active, t5, 09:30:20, 5s
    Team Notified             :active, t6, 09:30:25, 20m
    
    section Analysis
    Investigation             :t7, 09:30:45, 15m
    Solution Determined       :t8, 09:45:00, 5m
    
    section Recovery
    Test Transactions         :t9, 09:50:00, 5m
    Phased Resumption         :t10, 09:55:00, 5m
    Full Operation            :done, t11, 10:00:00, 5s

