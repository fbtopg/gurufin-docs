# Developer Resources

## Testnet Access

Developers can connect to the Gurufin testnet to build and test applications before mainnet deployment.

### Network Configuration

**Chain ID:** `guru_631-1`

**RPC Endpoints:**
- **RPC Endpoint:** https://trpc.gurufin.io
- **Cosmos gRPC:** Port 9090
- **Cosmos REST:** Port 9091
- **CometBFT RPC:** Port 26657
- **Ethereum JSON-RPC:** Port 8545

**Block Explorer:** https://tscan.gurufin.io/

**Faucet:** https://faucet.gurufin.io/

### Quick Start

1. **Install Dependencies**
   - Cosmos SDK CLI tools
   - Ethereum wallet (MetaMask compatible)
   - Development environment (Node.js, Python, or Go)

2. **Configure Wallet**
   - Add testnet chain to wallet
   - Request testnet tokens from faucet
   - Verify balance

3. **Deploy Contracts**
   - Compile smart contracts
   - Deploy to testnet
   - Verify deployment

4. **Test Integration**
   - Execute test swaps
   - Verify oracle prices
   - Test error handling

---

## API Reference

### Cosmos SDK APIs

**Cosmos gRPC (Port 9090)**
- Query account balances
- Submit transactions
- Query governance proposals
- Validator information

**Cosmos REST (Port 9091)**
- RESTful interface for all Cosmos operations
- JSON responses
- Standard HTTP methods

**CometBFT RPC (Port 26657)**
- Block queries
- Transaction broadcast
- Validator set queries
- Network status

### Ethereum JSON-RPC (Port 8545)

Compatible with standard Ethereum tools:
- `eth_call` — Execute contract read calls
- `eth_sendTransaction` — Submit transactions
- `eth_getBalance` — Query account balance
- `eth_getTransactionReceipt` — Get transaction status

### GuruDex Specific APIs

**Swap API**
```
POST /api/v1/swap
{
  "from_token": "USGX",
  "to_token": "KRGX",
  "amount": "1000",
  "user_type": "retail"
}
```

**Price API**
```
GET /api/v1/price/{pair}
Response: {
  "pair": "USGX/KRGX",
  "price": "1300.50",
  "timestamp": "2026-03-18T12:00:00Z"
}
```

**Pool Info API**
```
GET /api/v1/pools/{pool_id}
Response: {
  "pool_id": "usgx_krgx",
  "liquidity": "10000000",
  "volume_24h": "5000000",
  "fee_rate": "0.003"
}
```

---

## Integration Guide

### Step 1: Environment Setup

```bash
# Install Cosmos CLI
curl -sSf https://get.starport.network | sh

# Install dependencies
npm install @cosmjs/stargate
npm install ethers
```

### Step 2: Connect to Network

```javascript
import { StargateClient } from "@cosmjs/stargate";

const client = await StargateClient.connect(
  "https://trpc.gurufin.io"
);
```

### Step 3: Query Account

```javascript
const balance = await client.getAllBalances(
  "guru1..."
);
console.log(balance);
```

### Step 4: Execute Swap

```javascript
const result = await client.signAndBroadcast(
  senderAddress,
  [{
    typeUrl: "/gurufin.dex.MsgSwap",
    value: {
      fromToken: "USGX",
      toToken: "KRGX",
      amount: "1000000",
      minReceive: "1290000000"
    }
  }],
  fee
);
```

---

## Ecosystem Grant Program

Gurufin offers grants for developers building on the platform:

### Grant Categories

**Infrastructure Grants**
- Bridge development
- Wallet integrations
- Developer tools
- Documentation

**Application Grants**
- DeFi applications
- Payment solutions
- Trading platforms
- Analytics tools

**Research Grants**
- Oracle improvements
- Privacy enhancements
- Scalability research
- Security audits

### Application Process

1. Submit proposal via governance portal
2. Community review and feedback
3. Technical evaluation
4. Grant approval and funding
5. Milestone-based disbursement

### Support Resources

- Developer documentation: https://docs.gurufin.com
- Community Discord: Active developer community
- Technical support: Dedicated support team
- Office hours: Weekly developer calls
