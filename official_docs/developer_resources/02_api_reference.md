# API Reference

Gurufin Chain exposes both Cosmos SDK and EVM-compatible APIs for querying chain state, submitting transactions, and integrating with your applications.

---

## Testnet Base URLs

| Endpoint | URL |
|----------|-----|
| RPC (GXN Hub) | https://trpc.gurufin.io |
| WebSocket | wss://trpc.gurufin.io/websocket |
| Block Explorer | https://tscan.gurufin.io/ |

> **Note:** The above endpoints are for the **Season 2 Public Testnet**. Mainnet endpoints will be published before launch.

---

## Cosmos SDK Endpoints

| Service | Port | Description |
|---------|------|-------------|
| Cosmos gRPC | 9090 | Protocol buffer-based RPC for efficient querying |
| Cosmos REST | 9091 | RESTful API for account balances, transactions, staking |
| CometBFT RPC | 26657 | Tendermint consensus and block data |

---

## EVM JSON-RPC Endpoints

| Service | Port | Description |
|---------|------|-------------|
| Ethereum JSON-RPC | 8545 | Standard Ethereum JSON-RPC methods |
| Ethereum WebSocket | 8546 | Real-time event subscriptions |

---

## Common JSON-RPC Methods

| Method | Description |
|--------|-------------|
| `eth_blockNumber` | Get current block number |
| `eth_getBalance` | Query account balance |
| `eth_sendRawTransaction` | Submit signed transaction |
| `eth_call` | Execute read-only contract call |
| `eth_getLogs` | Query event logs |
| `eth_gasPrice` | Get current gas price (Guru-PEG adjusted) |
| `eth_getTransactionByHash` | Query transaction details |

---

## Cosmos SDK Query Examples

**Query validator set:**
```bash
curl https://trpc.gurufin.io:26657/validators?height=latest
```

**Query account balance:**
```bash
curl https://trpc.gurufin.io:1317/cosmos/auth/v1beta1/accounts
```

**Query pending transactions (mempool):**
```bash
curl https://trpc.gurufin.io:26657/unconfirmed_txs?limit=100
```

---

## SDK & Tooling

| Tool | Purpose |
|------|---------|
| `gaiad` / `gurucli` | Cosmos SDK CLI for transaction submission and querying |
| ethers.js / web3.js | EVM-compatible JavaScript libraries for dApp integration |
| Hardhat / Foundry | Smart contract development and testing frameworks |

---

## Rate Limits

Testnet endpoints may enforce rate limits during periods of high traffic. We recommend:

- Using WebSocket subscriptions instead of polling for real-time data
- Implementing exponential backoff on retry attempts
- Caching frequently accessed data on the client side

Contact the developer team on Discord for priority access during beta testing.

---

*This page provides an introductory overview.*
