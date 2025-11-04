# Connect to Gurufin

Welcome to the comprehensive guide on connecting to the Gurufin blockchain networks. Whether you are a developer, integrator, or user, this document provides all the essential information to configure your wallet and interact with both the Gurufin testnet and mainnet environments. You will find detailed RPC endpoints, chain IDs, and wallet setup instructions to ensure a smooth onboarding experience.

---

## Overview

Gurufin Chain is a high-performance, Layer-1 blockchain designed as a global on-chain FX and DeFi hub. It supports fast, deterministic finality and seamless interoperability through an IBC-first architecture and Ethereum-compatible EVM gateway. The network hosts a suite of fiat-pegged stablecoins and supports advanced DeFi and cross-border payment use cases.

This guide covers connecting to:

- **Gurufin Testnet** — the sandbox environment for development and testing.
- **Gurufin Mainnet** — the production network for live transactions and applications.

---

## Network Details

Below is a summary of the key network parameters for both Gurufin testnet and mainnet.

| Network       | RPC Endpoint                          | Chain ID        | Description                              |
|---------------|-------------------------------------|-----------------|------------------------------------------|
| Gurufin Testnet | `https://rpc.testnet.gurufin.io`   | `gurufin-testnet-1` | Public test network for development and testing. |
| Gurufin Mainnet | `https://rpc.gurufin.io`            | `gurufin-mainnet-1` | Production network supporting live stablecoin and FX operations. |

### Explanation of Parameters

- **RPC Endpoint**: The HTTP(s) URL used by wallets and clients to communicate with the blockchain node.
- **Chain ID**: A unique identifier for the blockchain network, used to prevent replay attacks and ensure transactions are signed for the correct chain.

---

## Connecting Your Wallet

To interact with the Gurufin blockchain, you need to configure your wallet with the appropriate network settings. Most modern wallets, including MetaMask and Cosmos SDK-compatible wallets, support custom network configurations.

### Wallet Configuration Steps

1. **Open your wallet application** (e.g., MetaMask, Keplr).
2. **Navigate to the network settings** or "Add Network" section.
3. **Input the network parameters** as specified in the tables below.
4. **Save the configuration** and switch to the newly added network.
5. **Verify the connection** by checking the network status or querying the chain via the wallet.

---

## Gurufin Testnet Configuration

The testnet environment is ideal for developers to build and test applications without risking real assets.

| Parameter           | Value                              |
|---------------------|----------------------------------|
| Network Name        | Gurufin Testnet                  |
| RPC URL             | `https://rpc.testnet.gurufin.io` |
| Chain ID            | `gurufin-testnet-1`              |
| Currency Symbol     | `GURU` (test token)              |
| Block Explorer URL  | `https://explorer.testnet.gurufin.io` (if available) |

### Notes

- The testnet uses the same Tendermint BFT consensus with delegated proof-of-stake (DPoS) as mainnet.
- Fees are denominated in the test token `GURU`.
- Faucet services may be available to obtain test tokens for transaction fees.

---

## Gurufin Mainnet Configuration

The mainnet hosts the live Gurufin Chain, supporting stablecoins such as USGX, KRGX, JPGX, and PHGX, and enabling cross-border FX and DeFi applications.

| Parameter           | Value                          |
|---------------------|--------------------------------|
| Network Name        | Gurufin Mainnet               |
| RPC URL             | `https://rpc.gurufin.io`       |
| Chain ID            | `gurufin-mainnet-1`            |
| Currency Symbol     | `GURU` (native token)          |
| Block Explorer URL  | `https://explorer.gurufin.io`  |

### Important Considerations

- The mainnet features the Guru-PEG fee equilibrium mechanism, ensuring predictable and retail-grade transaction fees.
- Wallets must support EVM compatibility if interacting with smart contracts via the EVM Gateway.
- Compliance features such as wallet-tier KYC/AML and sanctions screening are embedded at the protocol level.
- For institutional users, additional permissions and configurations may be required.

---

## Adding Gurufin Network to MetaMask

MetaMask users can connect to Gurufin networks by adding a custom RPC network. Follow these steps:

1. Open MetaMask and click on the network dropdown.
2. Select **Add Network**.
3. Enter the network details as per the table below.

| Field               | Testnet Value                     | Mainnet Value                   |
|---------------------|---------------------------------|--------------------------------|
| Network Name        | Gurufin Testnet                 | Gurufin Mainnet                |
| New RPC URL         | `https://rpc.testnet.gurufin.io` | `https://rpc.gurufin.io`        |
| Chain ID            | 12345 (example, confirm actual) | 67890 (example, confirm actual) |
| Currency Symbol     | GURU                           | GURU                          |
| Block Explorer URL  | `https://explorer.testnet.gurufin.io` | `https://explorer.gurufin.io`  |

> **Note:** Replace the Chain ID values with the actual numeric IDs once confirmed from the official Gurufin documentation or network status.

---

## Adding Gurufin Network to Cosmos SDK Wallets (e.g., Keplr)

Since Gurufin Chain is built on Cosmos SDK with Tendermint consensus, Cosmos-compatible wallets can connect using the following configuration:

| Parameter           | Testnet Value                     | Mainnet Value                   |
|---------------------|---------------------------------|--------------------------------|
| Chain ID            | `gurufin-testnet-1`              | `gurufin-mainnet-1`            |
| RPC Endpoint        | `https://rpc.testnet.gurufin.io` | `https://rpc.gurufin.io`        |
| REST Endpoint       | `https://lcd.testnet.gurufin.io` | `https://lcd.gurufin.io`        |
| Stake Currency      | GURU                           | GURU                          |
| Bech32 Prefix       | `guru`                         | `guru`                        |

### Steps to Add Network

1. Open your Cosmos SDK-compatible wallet.
2. Select **Add Custom Network**.
3. Fill in the parameters above for the desired network.
4. Save and switch to the Gurufin network.

---

## Verifying Connection

After configuring your wallet, verify connectivity by:

- Checking the current block height or network status in your wallet.
- Sending a small transaction (testnet) or querying account balances.
- Using the Gurufin block explorer to track transactions and blocks.

---

## Summary Table of Network Parameters

| Parameter           | Gurufin Testnet                         | Gurufin Mainnet                       |
|---------------------|---------------------------------------|-------------------------------------|
| RPC Endpoint        | `https://rpc.testnet.gurufin.io`      | `https://rpc.gurufin.io`             |
| Chain ID            | `gurufin-testnet-1`                    | `gurufin-mainnet-1`                  |
| Currency Symbol     | GURU (test token)                      | GURU (native token)                  |
| Block Explorer URL  | `https://explorer.testnet.gurufin.io` | `https://explorer.gurufin.io`        |
| Consensus           | Tendermint BFT with DPoS               | Tendermint BFT with DPoS             |
| Wallet Prefix       | `guru`                                | `guru`                              |

---

## Additional Resources

- For detailed API references and SDKs, please consult the [Gurufin Developer Portal](https://developer.gurufin.io).
- To explore smart contract deployment and EVM Gateway integration, refer to the [Gurufin EVM Gateway Documentation](https://docs.gurufin.io/evm).
- For stablecoin-specific operations and FX swap functionalities, see the [Gurufin FXSwap Documentation](https://docs.gurufin.io/fxswap).

---

By following this guide, you will be able to seamlessly connect your wallet to the Gurufin blockchain networks, enabling you to participate in a cutting-edge ecosystem for stablecoins, cross-border payments, and decentralized finance.