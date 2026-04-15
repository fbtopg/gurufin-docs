# Protocol Overview

Gurufin Chain is a purpose-built Layer-1 blockchain designed to serve as a global on-chain FX (foreign exchange) and DeFi hub for the Web3 economy. Unlike general-purpose blockchains, Gurufin Chain is specifically optimized for stablecoins, tokenized assets, and cross-border payments.

The chain addresses three fundamental challenges that have hindered blockchain adoption in traditional finance: unpredictable transaction fees, cross-chain fragmentation, and regulatory uncertainty. Through its innovative Guru-PEG mechanism, IBC-first architecture, and built-in compliance modules, Gurufin Chain provides a foundation where both institutions and retail users can participate in Web3 finance with confidence.

---

**High Performance**

Gurufin Chain delivers sub-second finality and throughput of up to 10,000 transactions per second. Unlike probabilistic consensus mechanisms that require multiple confirmations, transactions on Gurufin Chain are deterministically final once committed—critical for financial applications where settlement certainty matters.

**Interoperability**

The chain connects multiple blockchain ecosystems through a two-layer approach: native Cosmos IBC for trust-minimized cross-chain communication, and an EVM Gateway for Ethereum ecosystem compatibility.

---

**Technology Stack**

Gurufin Chain is built on the Cosmos SDK framework, leveraging **Tendermint BFT (Comet BFT)** consensus for Byzantine fault tolerance and instant finality, Delegated Proof-of-Stake (DPoS) for balancing decentralization with performance, and a modular architecture that enables independent upgrades and feature additions.

**What Makes Gurufin Different**

Gurufin Chain is not just another blockchain—it's a neutral settlement layer designed specifically for financial applications. By combining predictable fees, regulatory compliance, and multi-chain connectivity, it serves as the infrastructure where cross-border payments, FX trading, stablecoin issuance, and compliant DeFi applications can thrive.

---

## Guru-PEG: Predictable Transaction Fees

The Guru-PEG mechanism anchors the chain's transaction fees to real-world fiat currency, delivering predictable costs for users and developers alike.

### How Guru-PEG Works

- **Fiat Indexing**: Each transaction is priced at a fixed amount of USD (or equivalent in major fiat currencies), with automatic conversion based on oracle-published FX rates
- **Deterministic Fees**: Fees are computed on-chain at transaction execution time using verified oracle data—no surprises for users
- **Fee Stability**: During periods of high demand, fees adjust predictably rather than spiking wildly as in probabilistic gas markets
- **Multi-Currency Support**: The mechanism can support multiple fiat indices, enabling localized pricing for different regions

### Benefits

**For Users**: Predictable transaction costs enable accurate budgeting for DeFi operations, remittances, and payments—critical for financial planning.

**For Developers**: Stable fee structures simplify dApp economics and enable reliable revenue models. Smart contract integrations can compute expected fees deterministically.

**For Institutions**: Compliance systems can track and predict fee expenses in fiat terms, simplifying accounting and regulatory reporting.

---

## Architecture at a Glance

### Layer Structure

**Consensus Layer**: Tendermint BFT (Comet BFT) provides Byzantine fault-tolerant consensus with finality guarantees and fast block times. The layer handles validator selection, voting, and block finalization.

**Application Layer**: Cosmos SDK modules provide modular blockchain functionality—accounts, governance, staking, bank transfers, and custom modules for compliance and FX-specific features.

**Execution Layer**: Dual execution engines support both Cosmos SDK native transactions and EVM-compatible smart contracts, enabling interoperability with both Cosmos and Ethereum ecosystems.

**Networking Layer**: IBC protocol handles cross-chain packet transmission and verification, while the EVM Gateway manages bidirectional asset and message bridges with Ethereum.

---

## Key Components

### IBC First Architecture

Gurufin Chain treats inter-blockchain communication as a first-class feature rather than an afterthought. IBC connections enable:

- **Trust-Minimized Bridges**: Assets move between chains using cryptographic proofs rather than custodial intermediaries
- **Packet Relay**: Messages and tokens can be transmitted across connected chains with verifiable delivery guarantees
- **Composable DeFi**: Applications can leverage liquidity and functionality from multiple chains in a single transaction flow

### EVM Gateway

The EVM Gateway provides seamless interoperability with the Ethereum ecosystem:

- **Asset Bridge**: Lock-and-mint mechanism for moving ERC-20 tokens to Gurufin Chain
- **Message Bridge**: Cross-chain messaging for calling functions and triggering events
- **Gas Abstraction**: Bridge operations can be paid with Gurufin Chain native tokens, reducing friction for Ethereum users

---

## Compliance by Design

Gurufin Chain embeds regulatory compliance directly into its protocol layer, enabling institutional participation while preserving the benefits of decentralized infrastructure.

### Built-In Compliance Modules

**Address Screening**: On-chain modules for screening transactions against sanctioned addresses and high-risk entities, configurable per jurisdiction and use case.

**Transaction Limits**: Configurable per-address and per-transaction limits for AML/KYC compliance, with the ability to implement velocity checks and threshold alerts.

**Audit Trail**: Comprehensive transaction logging with metadata capture for regulatory reporting and forensic analysis.

### Jurisdictional Adaptability

The chain supports modular compliance rules that can be adapted to different regulatory requirements:

- **Region-Specific Rules**: Compliance modules can be enabled/disabled per validator set configuration
- **Policy Updates**: Rule changes can be implemented via on-chain governance without requiring network upgrades
- **Transparent Rules**: All compliance policies are codified and visible on-chain, enabling third-party verification

---

## Governance Framework

Gurufin Chain implements a hybrid governance model combining on-chain voting with multi-signature safeguards.

### On-Chain Governance

- **Proposal System**: Token holders can submit and vote on protocol proposals covering technical upgrades, parameter changes, and treasury allocations
- **Voting Power**: Voting weight is proportional to staked $GXN tokens, aligning economic incentives with protocol security
- **Quadratic Safeguards**: Governance mechanisms include checks against plutocratic capture, ensuring diverse participation

### Multi-Sig Administration

Administrative operations require multi-signature approval from a distributed set of trusted signers:

- **Key Distribution**: Signers are selected from diverse validator operators and ecosystem participants
- **Operation Scope**: Multi-sig is required for emergency operations, parameter changes requiring urgent response, and privileged module functions
- **Transparency**: All multi-sig operations are publicly auditable on-chain

---

## Security Architecture

### Consensus Security

Tendermint BFT consensus provides strong safety guarantees under standard assumptions:

- **Byzantine Fault Tolerance**: The network remains safe as long as less than one-third of staked tokens are controlled by malicious actors
- **Finality**: Once a block is committed, it cannot be reverted without compromising the security of the network
- **Economic Security**: Slashing conditions penalize malicious validator behavior, aligning incentives with honest participation

### Module Isolation

The modular architecture isolates different protocol components:

- **Independent Upgrades**: Module updates can be deployed without requiring network-wide restarts
- **Failure Containment**: Issues in one module can be addressed without affecting the entire system
- **Audit Efficiency**: Smaller, focused codebases are easier to audit and verify

### Formal Verification

Critical security components undergo formal verification processes:

- **Consensus Logic**: Tendermint BFT consensus has been extensively verified in production across the Cosmos ecosystem
- **Bridge Protocols**: IBC and EVM Gateway verification ensures cross-chain safety guarantees
- **Compliance Modules**: Transaction filtering logic is validated against specified policies

---

## Network Configuration

### Genesis State

The network launches with a carefully calibrated genesis configuration:

- **Initial Validators**: A set of trusted validators with diverse geographic and operational profiles
- **Staking Parameters**: Conservative initial parameters that can be adjusted through governance
- **Module Configuration**: Compliance and feature modules initialized with sensible defaults

### Validator Requirements

Validator operators must meet operational standards:

- **Infrastructure**: High-availability nodes with redundant networking and storage
- **Geographic Distribution**: Validators are encouraged to operate from diverse jurisdictions
- **Compliance**: Validator operators must adhere to applicable regulatory requirements

---

## Future Roadmap

### Phase 1: Foundation (Current)

- Core protocol launch with basic IBC and EVM connectivity
- Initial compliance modules for address screening and transaction limits
- Governance framework operational

### Phase 2: Expansion

- Enhanced cross-chain bridges to additional ecosystems
- Advanced compliance features including geofencing and transaction scoring
- Developer tooling improvements and SDK enhancements

### Phase 3: Innovation

- Custom module marketplace for specialized use cases
- Layer-2 integration for high-throughput applications
- Advanced DeFi primitives optimized for institutional participants

---

## Glossary

**IBC (Inter-Blockchain Communication)**: Protocol for cross-chain asset and message transfer with cryptographic delivery guarantees.

**EVM Gateway**: Bridge infrastructure for Ethereum-compatible smart contracts and token transfers.

**Guru-PEG**: Fee anchoring mechanism that prices transactions in fiat currency.

**DPoS (Delegated Proof-of-Stake)**: Consensus model where token holders delegate voting power to validators.

**Comet BFT**: Tendermint BFT consensus implementation used as the foundation for Gurufin Chain.

---

## Appendix: Technical Specifications

### Block Parameters

- **Block Time**: 1 second target
- **Max Block Size**: Configurable, typically 10-20 MB
- **Finality Time**: ~3 seconds (3 blocks)
- **Consensus**: Tendermint BFT (Comet BFT)

### Token Economics

- **Native Token**: $GXN
- **Total Supply**: 1,000,000,000 tokens
- **Staking Rewards**: Configurable, currently targeting 8-12% APY
- **Inflation Schedule**: Declining over time, with provisions for governance adjustment

### Gas Parameters

- **Fee Denomination**: $GXN
- **Guru-PEG Price**: 0.0001 USD equivalent per gas unit
- **Gas Limit**: Configurable per block, typically 10-20 million
