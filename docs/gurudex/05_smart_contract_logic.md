# Smart Contract Logic

GuruDex's swap execution is orchestrated by a modular smart contract system, enabling clean separation of concerns and independent upgradability.

**Core Contracts**
* **FXSwapMaster:** Central orchestration, managing swap routing, governance, and system parameters.
* **OPRSProcessor:** Executes the Oracle-priced swaps via the cross-chain mint/burn mechanism.
* **PoolFactory:** Deploys new inventory buffer instances as currencies are added.
* **PriceOracle:** Stores and executes the triple-validation logic on real-time FX rates.
* **InstitutionalRegistry:** Manages institutional profiles, custom limits, and KYC/AML permissions.
* **FeeDistributor:** Allocates accumulated rewards to LP token holders.

**Swap Routing**
When a swap initiates, the `OPRSProcessor` queries the `InstitutionalRegistry` to determine the user type. Retail users are routed to the standard execution path with dynamic fees, while verified institutional users are routed to custom parameter paths.
