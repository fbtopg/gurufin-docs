# Testnet Access (Season 2)

Use the Gurufin Public Testnet Season 2 to build, integrate, and test applications before mainnet deployment.

**Season 2 Network Architecture**

Season 2 includes one Tier 1 hub chain and six Tier 2 GX stablecoin chains.

| Chain | Display Name | Chain ID | EVM Chain ID | Native Denom | Prefix | Tier |
|---|---|---|---|---|---|---|
| GXN | GXN | guru_631-1 | 631 | agxn | guru | Tier 1 (Hub) |
| GXUSD | tGXUSD | gxusd_531-1 | 531 | atgxusd | gxusd | Tier 2 |
| GXKRW | tGXKRW | gxkrw_431-1 | 431 | atgxkrw | gxkrw | Tier 2 |
| GXIDR | tGXIDR | gxidr_1331-1 | 1331 | atgxidr | gxidr | Tier 2 |
| GXEUR | tGXEUR | gxeur_931-1 | 931 | atgxeur | gxeur | Tier 2 |
| GXPHP | tGXPHP | gxphp_731-1 | 731 | atgxphp | gxphp | Tier 2 |
| GXJPY | tGXJPY | gxjpy_231-1 | 231 | atgxjpy | gxjpy | Tier 2 |

**Connection Endpoints (GXN Hub)**

* **RPC Endpoint:** https://trpc.gurufin.io
* **WebSocket:** wss://trpc.gurufin.io/websocket
* **Block Explorer:** https://tscan.gurufin.io/

**API Ports**

These ports are relevant for direct node access, self-hosted infrastructure, or deployments that expose service-specific ports.

* **Cosmos gRPC:** 9090
* **Cosmos REST:** 9091
* **CometBFT RPC:** 26657
* **Ethereum JSON-RPC:** 8545
* **Ethereum WebSocket:** 8546

## Endpoint Lifecycle & Migration

Testnet endpoints (`trpc.gurufin.io`, `tscan.gurufin.io`) may rotate, upgrade, or be decommissioned as the testnet evolves.

* **Recommended practice:** Parameterize endpoint URLs in integration code instead of hardcoding them.
* **Migration path:** Mainnet endpoints will be announced through official channels before launch.
* **Status page:** Endpoint health and maintenance windows are published at [status.gurufin.io](https://status.gurufin.io).

Testnet assets are for testing only and should not be treated as production assets or representations of mainnet value.
