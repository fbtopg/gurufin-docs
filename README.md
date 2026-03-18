# Gurufin Documentation

Welcome to the official documentation for Gurufin — a specialized financial infrastructure that combines the efficiency of blockchain technology with the stability and regulatory compliance required for institutional adoption.

## Overview

Gurufin is built on two interconnected pillars:

- **Gurufin Chain:** A public, permissionless Layer-1 blockchain built on Cosmos SDK with Tendermint BFT consensus, serving as a neutral FX/DeFi settlement hub for cross-border payments and trading.

- **GX Stablecoin Network:** A federation of sovereign stablecoin chains, each operating under its own jurisdiction with licensed validators, fully backed 1:1 by fiat reserves.

- **GuruDex:** An Oracle Priced Reserve Swap (OPRS) exchange purpose-built for stablecoin FX trading with no slippage and oracle-verified pricing.

## Quick Start

### Connect to Testnet

- **Chain ID:** `guru_631-1`
- **RPC Endpoint:** `https://trpc.gurufin.io`
- **Block Explorer:** `https://tscan.gurufin.io/`
- **Faucet:** `https://faucet.gurufin.io/`

### API Endpoints

- **Cosmos gRPC:** 9090
- **Cosmos REST:** 9091
- **CometBFT RPC:** 26657
- **Ethereum JSON-RPC:** 8545

## Documentation Structure

The documentation is organized into the following sections:

1. **Introduction** — Vision, mission, and roadmap
2. **Gurufin Chain (Layer 1)** — Protocol overview, network architecture, interoperability, Guru-PEG fees, tokenomics, governance, and validator guide
3. **GX Chain (Stablecoin Framework)** — Overview, reserve backing, mint/burn mechanism, multi-currency support, and compliance
4. **GuruDex (OPRS Exchange)** — DEX overview, hybrid pools, liquidity and rewards, smart contract logic, and risk mitigation
5. **Developer Resources** — Testnet access, API reference, full documentation, and ecosystem grants
6. **Use Cases** — Cross-border payments, stablecoin FX trading, institutional DeFi, and government/CBDC applications

## Contributing

We welcome contributions to improve this documentation. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-docs`)
3. Make your changes following the writing guidelines below
4. Commit your changes (`git commit -m 'Improve documentation'`)
5. Push to the branch (`git push origin improve-docs`)
6. Open a Pull Request

### Writing Guidelines

- Use clear, professional language suitable for both technical and non-technical audiences
- Follow the existing structure and formatting conventions
- Include practical examples where applicable
- Use tables for structured data (avoid excessive bullet points)
- Ensure all technical terms are defined on first use
- Maintain consistency with terminology:
  - Use "OPRS" (Oracle Priced Reserve Swap) for the GuruDex execution mechanism
  - Use "local fiat currencies" rather than specific currency codes
  - Refer to "GuruDex" rather than "FXSwap" for the exchange platform

## Additional Resources

- [Gurufin Website](https://gurufin.io)
- [Full Developer Documentation](https://docs.gurufin.com)
- [Gurufin Chain Whitepaper](./gurufin_chain_whitepaper.md)
- [GX Chain Litepaper](./gx_chain_litepaper.md)

## License

This documentation is provided by the Gurufin Foundation. Please refer to the LICENSE file for usage terms.
