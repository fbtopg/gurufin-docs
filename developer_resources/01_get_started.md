# Get Started

Welcome to the Gurufin Chain developer quick-start guide. This page provides a step-by-step introduction to setting up your development environment, connecting to the Gurufin testnet, and deploying your first smart contract. Whether you are building cross-border payment solutions, stablecoin FX trading platforms, or interoperable DeFi applications, this guide will help you get started quickly and efficiently.

---

## Environment Setup

Before interacting with Gurufin Chain, you need to prepare your local development environment. Gurufin Chain is built on a Tendermint-class Byzantine Fault Tolerant (BFT) consensus with Delegated Proof-of-Stake (DPoS), and supports Ethereum Virtual Machine (EVM) compatibility through its EVM Gateway module. This allows developers familiar with Ethereum tooling to leverage existing frameworks such as Hardhat or Truffle.

### Prerequisites

- **Node.js** (v14 or higher): Required for running JavaScript-based development tools.
- **Yarn** or **npm**: Package managers for installing dependencies.
- **Gurufin Chain CLI**: Command-line interface for interacting with the blockchain.
- **Metamask** or compatible Web3 wallet: For managing accounts and signing transactions.
- **Solidity Compiler**: For compiling smart contracts.

### Installing Gurufin Chain CLI

The Gurufin Chain CLI is essential for node operations, querying the blockchain, and deploying contracts.

```bash
# Clone the Gurufin Chain repository
git clone https://github.com/gurufin/gurufin-chain.git
cd gurufin-chain

# Build the CLI binary
make install

# Verify installation
gurufincli version
```

The CLI provides commands to configure your connection, manage keys, and submit transactions.

### Setting Up Your Wallet

You can create a new wallet using the CLI or import an existing private key.

```bash
# Create a new wallet
gurufincli keys add mywallet

# List wallets
gurufincli keys list
```

Store your mnemonic securely. You will use this wallet to deploy contracts and sign transactions on the testnet.

---

## Connecting to the Testnet

Gurufin Chain operates a public testnet environment that mirrors mainnet features including fast block times (1-3 seconds), deterministic finality, and IBC interoperability.

### Configuring the CLI for Testnet

To connect to the testnet, configure the CLI with the testnet RPC endpoint and chain ID.

```bash
gurufincli config chain-id gurufin-testnet-1
gurufincli config node https://rpc.testnet.gurufin.io:26657
```

Verify connectivity by querying the latest block:

```bash
gurufincli status
```

You should see information about the current block height and network status.

### Obtaining Testnet Tokens

Testnet tokens are required to pay gas fees for transactions and contract deployments. Request test tokens from the official Gurufin faucet:

- Faucet URL: [https://faucet.testnet.gurufin.io](https://faucet.testnet.gurufin.io)

Provide your wallet address and receive test USGX stablecoins to cover transaction costs.

---

## Deploying Your First Smart Contract

Gurufin Chain supports EVM-compatible smart contracts, enabling you to write contracts in Solidity and deploy them using familiar tools.

### Step 1: Write a Simple Solidity Contract

Create a file `SimpleStorage.sol` with the following code:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedData;

    event DataStored(uint256 data);

    function set(uint256 data) public {
        storedData = data;
        emit DataStored(data);
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
```

This contract allows storing and retrieving a single unsigned integer.

### Step 2: Compile the Contract

Use Hardhat or Remix IDE to compile the contract. For Hardhat, initialize a project and compile:

```bash
npm init -y
npm install --save-dev hardhat @nomiclabs/hardhat-ethers ethers

npx hardhat compile
```

Ensure the Solidity compiler version matches the contract pragma (`^0.8.0`).

### Step 3: Configure Deployment Script

Create a deployment script `deploy.js` in your Hardhat project:

```javascript
async function main() {
    const [deployer] = await ethers.getSigners();

    console.log("Deploying contracts with the account:", deployer.address);

    const SimpleStorage = await ethers.getContractFactory("SimpleStorage");
    const simpleStorage = await SimpleStorage.deploy();

    await simpleStorage.deployed();

    console.log("SimpleStorage deployed to:", simpleStorage.address);
}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.error(error);
        process.exit(1);
    });
```

### Step 4: Configure Network Settings

Add the Gurufin testnet network configuration to your Hardhat config (`hardhat.config.js`):

```javascript
require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: "0.8.0",
  networks: {
    gurufinTestnet: {
      url: "https://evm.testnet.gurufin.io", // EVM Gateway RPC endpoint
      chainId: 12345, // Replace with actual testnet chain ID
      accounts: ["0xYOUR_PRIVATE_KEY"] // Replace with your wallet private key
    }
  }
};
```

### Step 5: Deploy the Contract

Run the deployment script targeting the Gurufin testnet:

```bash
npx hardhat run scripts/deploy.js --network gurufinTestnet
```

Upon success, the console will display the deployed contract address.

### Step 6: Interact with the Contract

You can interact with the deployed contract using ethers.js or Web3.js. For example, to set and get the stored data:

```javascript
const simpleStorage = await ethers.getContractAt("SimpleStorage", "DEPLOYED_CONTRACT_ADDRESS");

// Store a value
await simpleStorage.set(42);

// Retrieve the value
const value = await simpleStorage.get();
console.log("Stored value:", value.toString());
```

---

## Summary Table: Key Commands and Endpoints

| Task                      | Command / Endpoint                                   | Notes                                  |
|---------------------------|----------------------------------------------------|----------------------------------------|
| Install CLI               | `make install` in cloned repo                      | Requires Go and Make                   |
| Create wallet             | `gurufincli keys add mywallet`                      | Save mnemonic securely                 |
| Configure CLI for testnet | `gurufincli config chain-id gurufin-testnet-1`     | Set testnet chain ID                   |
|                           | `gurufincli config node https://rpc.testnet.gurufin.io:26657` | Set testnet RPC endpoint               |
| Check network status      | `gurufincli status`                                 | Verify connection                     |
| Request test tokens       | [https://faucet.testnet.gurufin.io](https://faucet.testnet.gurufin.io) | For gas fees                          |
| Compile Solidity contract | `npx hardhat compile`                               | Use Hardhat or Remix                   |
| Deploy contract           | `npx hardhat run scripts/deploy.js --network gurufinTestnet` | Deploy via EVM Gateway                |
| Interact with contract    | ethers.js/Web3.js contract calls                    | Use deployed contract address          |

---

## Next Steps

After deploying your first contract, explore Gurufin Chain’s advanced features such as:

- **IBC Interoperability**: Enable atomic cross-chain settlements.
- **Hybrid Execution Fabric**: Utilize AMM and RFQ mechanisms for FX and DeFi applications.
- **Oracle Network Integration**: Access real-time price feeds for dynamic fee equilibrium.
- **Privacy Modes**: Implement zk-proof privacy with zkGuru.
- **Compliance Layers**: Leverage wallet-tier KYC/AML features for regulated environments.

For detailed API references, SDKs, and advanced tutorials, visit the [Developer Resources](../developer-resources) section.

---

By following this guide, you have taken the first step toward building on Gurufin Chain’s high-performance, interoperable, and compliance-ready blockchain platform tailored for the Web3 economy. Happy coding!