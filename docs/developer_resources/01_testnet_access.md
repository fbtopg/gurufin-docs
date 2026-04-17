# Testnet Access (Season 2)

Connect to the Gurufin Public Testnet Season 2 to develop and test your applications before mainnet deployment.

**Season 2 Network Architecture**
The Season 2 Testnet introduces the Tier 1 Hub and six Tier 2 sovereign stablecoin chains.

| Chain | Display Name | Chain ID | EVM Chain ID | Native Denom | Prefix | Tier |
|---|---|---|---|---|---|---|
| GURU | GXN | guru_631-1 | 631 | agxn | guru | Tier 1 (Hub) |
| GXUSD | tGXUSD | gxusd_531-1 | 531 | atgxusd | gxusd | Tier 2 |
| GXKRW | tGXKRW | gxkrw_431-1 | 431 | atgxkrw | gxkrw | Tier 2 |
| GXIDR | tGXIDR | gxidr_1331-1 | 1331 | atgxidr | gxidr | Tier 2 |
| GXEUR | tGXEUR | gxeur_931-1 | 931 | atgxeur | gxeur | Tier 2 |
| GXPHP | tGXPHP | gxphp_731-1 | 731 | atgxphp | gxphp | Tier 2 |
| GXJPY | tGXJPY | gxjpy_231-1 | 231 | atgxjpy | gxjpy | Tier 2 |

**Connection Endpoints (GURU Hub)**
* **RPC Endpoint:** https://trpc.gurufin.io
* **WebSocket:** wss://trpc.gurufin.io/websocket
* **Block Explorer:** https://tscan.gurufin.io/

**API Ports**
* **Cosmos gRPC:** 9090
* **Cosmos REST:** 9091
* **CometBFT RPC:** 26657
* **Ethereum JSON-RPC:** 8545
* **Ethereum WebSocket:** 8546
