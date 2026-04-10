# OPRS Architecture

📊 Oracle Priced Reserve Swap — The Core of GuruDex

---

## 🚀 Quick Links

- **GuruDex Overview**: [`01 DEX Overview`](/gurudex/01_dex_overview.md)
- **Smart Contracts**: [`04 Smart Contract Logic`](/gurudex/04_smart_contract_logic.md)
- **GX Stablecoins**: [`01 GX Overview`](/gx_chain/01_overview.md) | [`03 Mint & Burn`](/gx_chain/03_mint_and_burn.md)
- **Use Cases**: [`02 Stablecoin FX Trading`](/use_cases/02_stablecoin_fx_trading.md)

---

## Overview

GuruDex uses an **Oracle Priced Reserve Swap (OPRS)** architecture instead of traditional AMM pools. This design is purpose-built for stablecoin FX trading, where prices are determined by real-world oracle rates rather than on-chain supply/demand dynamics.

**Key Principle**: Instead of relying on liquidity pool dynamics, OPRS uses oracle-guided mint/burn mechanics to ensure trades execute at precise market rates with zero slippage.

See: [`GuruDex Overview`](/gurudex/01_dex_overview.md#oracle-priced-reserve-swap-oprs)

---

## How OPRS Works

---

**How OPRS Works**

Instead of maintaining liquidity pools with constant product formulas, OPRS uses a mint-and-burn mechanism guided by oracle FX rates:

1. **User initiates a swap** — e.g., 1,000 USGX → KRGX
2. **Oracle provides real-time FX rate** — e.g., 1 USD = 1,300 KRW
3. **Input stablecoin is burned** — 1,000 USGX is burned on the USGX Chain
4. **Output stablecoin is minted** — 1,298,700 KRGX is minted on the KRGX Chain
5. **IBC atomic settlement** — Cross-chain transfer completes atomically via IBC/HTLCs

---

**Why OPRS for Stablecoin FX?**

| Traditional AMM | OPRS (GuruDex) |
|-----------------|----------------|
| Price emerges from trading activity | Price from real-time oracle feeds |
| Slippage increases with trade size | No slippage — oracle-verified rates |
| Requires deep liquidity pools | Minimal liquidity needed (mint/burn) |
| Arbitrageurs maintain peg | Oracle validation maintains accuracy |
| Works for volatile pairs | Purpose-built for stablecoin FX |

---

**Sovereign Chain Integration**

Each GX stablecoin has its own sovereign L1 mainnet:

- **USGX Chain** — USD-pegged, US jurisdiction validators
- **KRGX Chain** — KRW-pegged, Korea jurisdiction validators
- **EURGX Chain** — EUR-pegged, EU jurisdiction validators
- **JPGX Chain** — JPY-pegged, Japan jurisdiction validators

When a user swaps USGX → KRGX on GuruDex:
- USGX is burned on the USGX Chain
- KRGX is minted on the KRGX Chain
- IBC ensures atomic cross-chain settlement

---

**Oracle Validation**

All oracle prices undergo triple validation before execution:

- **Freshness** — Data must be less than 5 minutes old
- **Deviation** — Price must be within 1% of stored rate
- **Confidence** — Oracle confidence score must exceed 95%

If validation fails, the swap reverts and the user is notified.

---
