# API Reference

The **API Reference** module provides a comprehensive guide to interacting with the Gurufin Chain programmatically. It details the various endpoints and methods available for querying chain state, submitting transactions, and integrating Gurufin Chain functionalities into your applications. Gurufin Chain offers a dual interface, supporting both the familiar Cosmos SDK for blockchain-specific operations and an EVM-compatible API for seamless integration with existing Ethereum tooling and smart contracts.

## Key Concepts

*   **Cosmos SDK Endpoints**: These provide access to the core functionalities of the Gurufin Chain, built on the Cosmos SDK framework. They are essential for operations related to accounts, staking, governance, and general blockchain data.
*   **EVM JSON-RPC Endpoints**: These endpoints offer compatibility with the Ethereum Virtual Machine (EVM), allowing developers to interact with smart contracts and utilize standard Ethereum JSON-RPC methods, making it easy to port existing dApps or develop new ones using familiar Ethereum tools.
*   **Common JSON-RPC Methods**: A curated list of frequently used JSON-RPC methods, particularly for EVM interactions, that enable common tasks such as checking balances, sending transactions, and querying contract data.
*   **Testnet Base URL**: This specifies the base URL for accessing all API endpoints on the Gurufin Chain's testnet environment, crucial for development and testing purposes.

## Cosmos SDK Endpoints

The Gurufin Chain exposes the following Cosmos SDK-based services:

*   **Cosmos gRPC**: Accessible on port `9090`, this is a Protocol Buffer-based RPC for highly efficient querying of blockchain data.
*   **Cosmos REST**: Available on port `9091`, this provides a RESTful API for common operations such as retrieving account balances, transaction details, and staking information.
*   **CometBFT RPC**: Found on port `26657`, this endpoint offers access to the Tendermint consensus engine and raw block data.

## EVM JSON-RPC Endpoints

For Ethereum compatibility, the following endpoints are provided:

*   **Ethereum JSON-RPC**: Located on port `8545`, this endpoint supports standard Ethereum JSON-RPC methods, enabling interactions with EVM-compatible smart contracts.
*   **Ethereum WebSocket**: Available on port `8546`, this provides real-time event subscriptions, useful for dApps that require immediate updates on blockchain events.

## Common JSON-RPC Methods

Developers will frequently use the following EVM JSON-RPC methods:

*   `eth_blockNumber`: Retrieves the current block number of the chain.
*   `eth_getBalance`: Queries the balance of a specific account.
*   `eth_sendRawTransaction`: Submits a signed transaction to the network.
*   `eth_call`: Executes a read-only contract call without broadcasting a transaction.
*   `eth_getLogs`: Allows querying of event logs emitted by smart contracts.

## Testnet Base URL

All of the aforementioned API endpoints, for both Cosmos SDK and EVM, are accessible through the following testnet RPC base URL:

`https://trpc.gurufin.io`

When making API requests, you would prepend this base URL to the specific endpoint path.