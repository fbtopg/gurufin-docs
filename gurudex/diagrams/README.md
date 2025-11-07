# GuruDEX Mermaid Diagrams

All files contain **pure Mermaid code only** - no markdown, no headers, no instructions.

## 🚀 Usage (Super Simple)

1. Open any `.md` file
2. **Select All** (Ctrl+A)
3. **Copy** (Ctrl+C)
4. Go to **https://mermaid.live/**
5. **Paste** (Ctrl+V)
6. Export as PNG/SVG ✨

## 📁 Available Diagrams

### System Architecture
- `01_system_architecture.md` - Basic 3-layer view (graph TD)
- `01_system_architecture_detailed.md` - Detailed nested view (flowchart TB)

### Institutional Onboarding  
- `02_institutional_onboarding.md` - 5-step workflow (flowchart TD)
- `02_institutional_states.md` - State transitions (stateDiagram-v2)

### Risk Mitigation
- `03_risk_4layer_defense.md` - 4-layer defense strategy (flowchart TD)

### Circuit Breaker
- `04_circuit_breaker.md` - Operation flow (flowchart TD)
- `04_circuit_breaker_timeline.md` - Gantt timeline (gantt)

### Swap Flows
- `05_retail_swap.md` - Retail user 8-step flow (flowchart TD)
- `05_institutional_swap.md` - Institutional 10-step flow (flowchart TD)

### Pool Comparison
- `06_pool_comparison.md` - Single vs Separated vs Hybrid (graph TB)
- `06_hybrid_architecture.md` - Dual-layer structure (graph TB)

## 🎨 Color Scheme

Consistent across all diagrams:
- 🔵 Process/Steps: `#e3f2fd`, `#b3e5fc`
- 🟢 Success: `#c8e6c9`, `#81c784`
- 🟡 Warning: `#fff9c4`, `#ffccbc`
- 🔴 Error/Critical: `#ffcdd2`, `#ef5350`

## 📊 Diagram Types

- `graph TD/LR` - Architecture, components
- `flowchart TB/TD` - Process flows
- `stateDiagram-v2` - State machines
- `gantt` - Timelines
- `sequenceDiagram` - Actor interactions

## ✅ All diagrams work with GitBook Mermaid plugin
