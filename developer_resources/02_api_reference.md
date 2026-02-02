# API Reference

Gurufin Chain exposes standard Cosmos SDK and EVM-compatible APIs for querying chain state, submitting transactions, and integrating with your applications.

---

**REST API Endpoints**

| Endpoint | Description |
|----------|-------------|
| `/cosmos/bank/v1beta1/balances/{address}` | Query account balances |
| `/cosmos/tx/v1beta1/txs` | Broadcast and query transactions |
| `/cosmos/staking/v1beta1/validators` | List validators and delegation info |
| `/cosmos/gov/v1beta1/proposals` | Query governance proposals |

---

**EVM JSON-RPC**

Standard Ethereum JSON-RPC methods are supported for EVM compatibility:

| Method | Description |
|--------|-------------|
| `eth_blockNumber` | Get current block number |
| `eth_getBalance` | Query ETH-equivalent balance |
| `eth_sendRawTransaction` | Submit signed transaction |
| `eth_call` | Execute read-only contract call |

---

**WebSocket**

Subscribe to real-time events via WebSocket at `wss://ws-testnet.gurufin.io`.

---

*This page provides an introductory overview.*
