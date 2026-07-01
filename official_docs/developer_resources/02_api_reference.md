# API Reference

Gurufin Chain exposes Cosmos SDK and EVM-compatible APIs for querying chain state, submitting transactions, and integrating applications.

## Testnet Base URLs

| Endpoint | URL |
|----------|-----|
| RPC (GXN Hub) | https://trpc.gurufin.io |
| WebSocket | wss://trpc.gurufin.io/websocket |
| Block Explorer | https://tscan.gurufin.io/ |

> **Note:** These endpoints are for the **Season 2 Public Testnet**. Mainnet endpoints will be published before launch.

## Cosmos SDK Endpoints

| Service | Port | Description |
|---------|------|-------------|
| Cosmos gRPC | 9090 | Protocol buffer-based RPC for efficient queries. |
| Cosmos REST | 9091 | REST API for account balances, transactions, and staking. |
| CometBFT RPC | 26657 | Consensus, block, and mempool data. |

## EVM JSON-RPC Endpoints

| Service | Port | Description |
|---------|------|-------------|
| Ethereum JSON-RPC | 8545 | Standard Ethereum JSON-RPC methods. |
| Ethereum WebSocket | 8546 | Real-time event subscriptions. |

## Common JSON-RPC Methods

| Method | Description |
|--------|-------------|
| `eth_blockNumber` | Get the current block number. |
| `eth_getBalance` | Query an account balance. |
| `eth_sendRawTransaction` | Submit a signed transaction. |
| `eth_call` | Execute a read-only contract call. |
| `eth_getLogs` | Query event logs. |
| `eth_gasPrice` | Get the current Guru-PEG-adjusted gas price. |
| `eth_getTransactionByHash` | Query transaction details. |

## Cosmos SDK Query Examples

**Query validator set:**
```bash
curl https://trpc.gurufin.io:26657/validators?height=latest
```

**Query account balance:**
```bash
curl https://trpc.gurufin.io:9091/cosmos/auth/v1beta1/accounts
```

**Query pending transactions (mempool):**
```bash
curl https://trpc.gurufin.io:26657/unconfirmed_txs?limit=100
```

## SDK & Tooling

| Tool | Purpose |
|------|---------|
| `gaiad` / `gurucli` | Cosmos SDK CLI tooling for transaction submission and queries. |
| ethers.js / web3.js | EVM-compatible JavaScript libraries for application integration. |
| Hardhat / Foundry | Smart contract development and testing frameworks. |

## Rate Limits

Testnet endpoints may enforce rate limits during periods of high traffic. Recommended integration practices include:

- Using WebSocket subscriptions instead of polling for real-time data
- Implementing exponential backoff on retry attempts
- Caching frequently accessed data on the client side

Contact the developer team through official community channels for priority access during beta testing.

*This page provides an introductory API overview.*
