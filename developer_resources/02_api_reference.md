# API Reference

Gurufin Chain exposes both Cosmos SDK and EVM-compatible APIs for querying chain state, submitting transactions, and integrating with your applications.

---

**Cosmos SDK Endpoints**

| Service | Port | Description |
|---------|------|-------------|
| Cosmos gRPC | 9090 | Protocol buffer-based RPC for efficient querying |
| Cosmos REST | 9091 | RESTful API for account balances, transactions, staking |
| CometBFT RPC | 26657 | Tendermint consensus and block data |

---

**EVM JSON-RPC Endpoints**

| Service | Port | Description |
|---------|------|-------------|
| Ethereum JSON-RPC | 8545 | Standard Ethereum JSON-RPC methods |
| Ethereum WebSocket | 8546 | Real-time event subscriptions |

---

**Common JSON-RPC Methods**

| Method | Description |
|--------|-------------|
| `eth_blockNumber` | Get current block number |
| `eth_getBalance` | Query account balance |
| `eth_sendRawTransaction` | Submit signed transaction |
| `eth_call` | Execute read-only contract call |
| `eth_getLogs` | Query event logs |

---

**Testnet Base URL**

All endpoints are accessible via the testnet RPC base: `https://trpc.gurufin.io`

---

*This page provides an introductory overview.*
