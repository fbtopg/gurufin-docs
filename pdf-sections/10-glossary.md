# Glossary

## Key Terms and Definitions

**AMM (Automated Market Maker)**
A decentralized exchange mechanism where users trade directly against algorithmic liquidity pools, with token prices determined by mathematical invariants rather than order books.

**BFT (Byzantine Fault Tolerant)**
A consensus mechanism that can continue operating correctly even when some nodes fail or act maliciously.

**CFMM (Constant-Function Market Maker)**
A type of AMM where prices are determined by a mathematical function that remains constant during trades.

**Cosmos SDK**
A framework for building blockchain applications in Go, used as the foundation for Gurufin and GX chains.

**CPI (Consumer Price Index)**
A measure of inflation used by Guru-PEG to adjust gas fees over time.

**DPoS (Delegated Proof-of-Stake)**
A consensus algorithm where token holders elect validators to produce blocks, enabling deterministic finality and governance flexibility.

**DvP (Delivery-versus-Payment)**
A settlement mechanism where securities are transferred only if payment is also transferred, eliminating principal risk.

**EVM (Ethereum Virtual Machine)**
The runtime environment for smart contracts on Ethereum, supported by Gurufin via gateway.

**FX (Foreign Exchange)**
The conversion of one currency to another, a primary use case for Gurufin's OPRS architecture.

**GatewayGX**
Gurufin's interoperability module for non-IBC chains like Ethereum and Solana.

**Guru-PEG**
Price Equilibrium Governance — Gurufin's mechanism for maintaining fiat-predictable gas fees.

**Gurufin Chain**
The public, permissionless Layer-1 blockchain serving as Gurufin's neutral FX/DeFi settlement hub.

**GuruDex**
Gurufin's Oracle Priced Reserve Swap exchange for stablecoin FX trading.

**GX Stablecoin Network**
A federation of sovereign stablecoin chains, each operating under its own jurisdiction.

**Hashed Timelock Contract (HTLC)**
A type of smart contract that ensures atomic cross-chain settlement by requiring both parties to confirm within a time window.

**HSM (Hardware Security Module)**
A physical computing device that safeguards digital keys for strong authentication and cryptographic processing.

**IBC (Inter-Blockchain Communication)**
A protocol enabling secure, trust-minimized interoperability between heterogeneous blockchains.

**InstitutionalRegistry**
The smart contract managing institutional profiles, KYC/AML compliance, and custom trading parameters.

**LP (Liquidity Provider)**
An entity that deposits tokens into a pool to enable trading, earning fees in return.

**MEV (Maximal Extractable Value)**
The profit that can be extracted by reordering, inserting, or censoring transactions in a block.

**OPRS (Oracle Priced Reserve Swap)**
Gurufin's exchange architecture using oracle-guided pricing with mint/burn mechanics for stablecoin FX trading.

**Oracle**
A service that provides verified external data (like FX rates) to blockchain smart contracts.

**PvP (Payment-versus-Payment)**
A settlement mechanism ensuring the final transfer of one currency occurs if and only if the final transfer of the counter-currency also occurs.

**RFQ (Request-for-Quote)**
A trade execution model where users solicit binding price quotes from designated liquidity providers.

**SLA (Service Level Agreement)**
A commitment between a service provider and client regarding service quality and performance.

**TEEs (Trusted Execution Environments)**
Secure areas of a processor that isolate code and data from the main operating system.

**Tendermint**
A BFT consensus engine providing deterministic finality and high throughput, used by Gurufin and GX chains.

**TTL (Time-to-Live)**
The maximum duration for which a quoted price or transaction instruction remains valid.

**Virtual-Pair Mechanism**
GuruDex's innovation allowing LPs to manage positions in multiple pools through a single Virtual LP token.

**ZK-Proof (Zero-Knowledge Proof)**
A cryptographic method enabling proof of knowledge without revealing the underlying data.
