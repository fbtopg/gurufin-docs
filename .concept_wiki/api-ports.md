# Testnet Access (API Ports)

The "Testnet Access (API Ports)" module provides essential information for developers to connect their applications to the Guru Testnet. This includes details on network configuration, the specific API ports available for various services, and how to acquire testnet tokens.

## Key Concepts

This module centers around the following core concepts:

*   **API Ports:** These are the specific network communication endpoints that various blockchain services expose. Developers use these ports to interact with the Guru Testnet programmatically.
*   **Faucet:** A service that dispenses free testnet tokens to developers. These tokens are crucial for testing applications without spending real-world assets.
*   **Network Configuration:** This refers to the fundamental parameters required to identify and connect to the Guru Testnet. It includes the network name, chain ID, and various endpoint URLs.

## Module Overview

The Guru Testnet serves as a vital environment for developers to build, test, and refine their applications before deploying them to the mainnet. This module details the necessary information to establish a connection and interact with the testnet effectively.

### API Ports

To facilitate diverse interactions, the Guru Testnet exposes several API ports for different backend services. These ports are critical for any application requiring programmatic access to the blockchain or its related components.

| Service         | Port  |
| :-------------- | :---- |
| Cosmos gRPC     | 9090  |
| Cosmos REST     | 9091  |
| CometBFT RPC    | 26657 |
| Ethereum JSON-RPC | 8545 |
| Ethereum WebSocket | 8546 |

### Faucet

For development and testing purposes, applications often require tokens to cover transaction fees or interact with smart contracts. The Guru Testnet provides a **Faucet** where developers can request free testnet tokens.

| Resource | URL                 |
| :------- | :------------------ |
| Faucet   | `https://faucet.gurufin.io/` |

### Network Configuration

To connect directly to the Guru Testnet, developers need specific network parameters. These identifiers and endpoints ensure applications can locate and communicate with the correct network.

| Parameter    | Value                |
| :----------- | :------------------- |
| Network Name | Guru Testnet         |
| Chain ID     | `guru_631-1`         |
| RPC Endpoint | `https://trpc.gurufin.io` |
| WebSocket    | `wss://trpc.gurufin.io/websocket` |
| Block Explorer | `https://tscan.gurufin.io/` |

This information provides a comprehensive guide for developers to begin their journey on the Guru Testnet.