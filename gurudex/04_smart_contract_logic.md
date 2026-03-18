# Smart Contract Logic

GuruDex's swap execution is orchestrated by a modular smart contract system. Each contract handles a specific responsibility, enabling clean separation of concerns and independent upgradability.

---

**Swap Routing**

When a swap is initiated, the OPRSProcessor queries the InstitutionalRegistry to determine user type:

* **Retail users** → Routed to the standard OPRS execution path with appropriate fee tiers
* **Institutional users** → Routed to the institutional OPRS path with oracle-verified pricing and custom parameters

All swaps execute through the Oracle Priced Reserve Swap (OPRS) mechanism, ensuring consistent oracle-guided pricing regardless of user type.

---

**Institutional Onboarding**

Institutions follow a multi-step workflow before trading is enabled:

1. **Registration** — Submit basic information via `registerInstitution()`
2. **Verification** — Off-chain KYC/AML review by operations team
3. **Activation** — Operator sets custom limits, fees, and parameters
4. **Authorization** — Approve specific coins and pools for access

---

**Core Contracts**

* **FXSwapMaster** — Central orchestration, governance, and system parameters
* **OPRSProcessor** — Oracle-priced swap execution via mint/burn mechanism
* **PoolFactory** — Deploys new pool instances as currencies are added
* **PriceOracle** — Stores and validates real-time FX rates
* **InstitutionalRegistry** — Manages institutional profiles and permissions
* **FeeDistributor** — Allocates rewards proportionally to LP token holders

---
