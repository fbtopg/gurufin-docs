GX STABLECOINS
A Regulatory‑Grade Network of Local Sovereign Stablecoin Chains for independent PoA L1s, Bank‑API Mint/Burn,
24/7 Live Proof‑of‑Reserves, Wallet‑Level Compliance, Interoperability with IBC/EVM, and Optional FX Hubs.

Government, Central Bank, FMIs Institutional Edition
GURUFIN Technical Papers Series V. 1 - 2025
August 2025
CONTENTS
Abstract
Hypothesis
Background: Policy Context and Rationale
1.1 Redemption Uncertainty
1.2 Run Amplification Under Stress
1.3 Regulatory Blind Spots
1.4 Fragmented Cross-Border Settlement
1.5 Unpredictable Fees and Poor Retail Suitability
1.6 Weak Operational Governance
System Architecture
3 .1 Jurisdictional PoA ledger with diversified validators
3 .2 Automated mint/burn stack
3 .3 Reserve policy and transparency
3 .5 Retail performance and scale out
3 .6 Integration with existing system
3 .7 Offline payments (bounded risk)
3 .8 Wallet/Application Compliance
3 .9 Redemption and De-Peg Risk in Existing Stablecoins
3 .10 Liquidity and Redemption Dynamic
2.11 Reserve Composition and Risk Policy
Fees and Gas Model
Compliance, Governance, and Supervision
Interoperability and Foreign‑Exchange Connectivity
Tokenized Assets and Programmable Finance
6.1 Scope and Asset Classes
6.2 Legal linkage and registries
6.3 Issuance and transfer controls
6.5 Atomic settlement, DvP and PvP
6.6 Market infrastructure and venues
6.7 Lifecycle automation and corporate actions
6.8 Data protection and privacy
6.9 Interoperability and portability
6.10 Policy stance
Security and Privacy
7.1 Institutional assurance
7.2 Zero-Knowledge Proof
Experiment: Liquidity Risk and Buffers
8.1 Theoretical Framework and Methodological Approach
8.2 Core definitions and notation from GX Liquidity & Risk Methodology.
8.3 Experimental Parameters
8.4 Results and Analysis
Conclusions
9.1 Key Findings and Contributions :
References
Annexes
Liquidity & Risk Methodology: Definitions and notation.
Liquidity & Risk Methodology: NSFR interpretation.
Liquidity & Risk Methodology: Core equations.
Liquidity & Risk Methodology: Arrival calibration.
Liquidity & Risk Methodology: Severity models and tail behavior.
Glossary & Abbreviations
Foreword

This document presents an institutional-grade architecture for fiat-backed stablecoins issued on jurisdiction-specific
Proof-of-Authority (PoA) blockchains.

GX is designed not as a speculative instrument but as financial infrastructure. It draws on lessons from traditional
payment systems and nearly a decade of stablecoin experimentation, together with RTGS finality, prudential concepts
(LCR/NSFR), and supervisory audit frameworks. Its foundations are compliance-first and institutionally auditable:
consensus governed by licensed validators (PoA); bank-API-anchored, automated mint/burn rather than manual
controls; and live proof-of-reserves scanning rather than monthly or quarterly attestations.

Mission : GX aims to provide an unparalleled level of trust for digital settlement for regulators and end users alike:
transparent, fast, and low-cost on-chain payments with predictable finality, observable liquidity, and embedded
regulatory oversight. Whether clearing micropayments at retail scale or supporting high-throughput institutional flows,
GX is engineered to meet the standards of supervisors and real-world usability.

We proceed from first principles: (i) solvency must be continuously observable; (ii) redemption must be honored within
explicit service levels; (iii) transactional privacy must be compatible with supervisory audit; and (iv) cross-border
reach must not subordinate domestic monetary sovereignty.

The design aligns with prudential objectives, solvency, liquidity, governance, auditability, and operational resilience,
while preserving the programmability that makes digital money useful in everyday commerce.

The following pages set out the policy context, architectural model, and supervisory assurances underpinning GX. We
invite central banks, regulators, financial institutions, and market operators to examine the model, participate in pilots,
evaluate its safeguards, and, where policy permits, integrate GX APIs and modules or consider GX as a complementary
component to public-sector payments modernization. GX is not merely a proposal; it is a platform for collaboration.

Gurufin
Blockchain Research Labs
GX STABLECOINS: A Regulatory‑Grade Network of Local
Sovereign Stablecoin Chains
Gurufin Inc, Blockchain Research Labs
August 2025.
Abstract
This paper introduces the GX network, a regulatory-grade architecture for jurisdiction-specific stablecoins designed to
reduce run risk and improve cross-border settlement. Today’s arrangements suffer from fragmented liquidity, USD
concentration, and opacity that can amplify redemptions under stress.

GX employs locally compliant PoA chains, wallet-level KYC/AML, and a Live Reserve Scanner that reconciles bank
balances and circulating supply in near real time. Issuance and redemption are bank events anchored, idempotent, and
auditable. Performance targets are sub-second confirmations on retail lanes and five-figure TPS on commodity
hardware, consistent with CBDC pilot benchmarks.

The Liquidity & Risk Methodology adapts prudential concepts (Basel LCR/NSFR) to a fully reserved token: short-
horizon coverage is calibrated to Expected Shortfall at confidence 𝛼, with observable policy ratios
GX−LCR(H). At launch, reserves are held 100% in cash; where permitted, a capped share may be placed in ultra-short
government bills with pre-arranged repo capacity to raise same-day cash without forced sales. In jurisdictions with
shallow repo markets, GX maintains higher cash floors, shorter ladders, and committed facilities appropriate to local
conditions.

Empirical illustrations show that, under severe but plausible stresses, callable liquidity covers modeled tail redemptions
across multiple horizons when policy floors are met. Fees are fiat-fixed within narrow bands and indexed to CPI on a
defined schedule to ensure long-run sustainability while preserving predictability.

GX aims to deliver transparent, sovereign rails that interoperate with global FX hubs while keeping domestic issuance
and safeguards under local supervision. As jurisdictional Layer-1s, GX chains also provide regulated foundations for
tokenized assets (e.g., RWAs, STOs, and programmatic payments/NFT credentials) under local law, anticipating
scalable participation in the emerging web3 economy.

Keywords: Stablecoin, Central Bank Digital Currency (CBDC), Financial Stability, Liquidity Risk, Expected Shortfall
(ES), Extreme Value Theory (EVT), Operational Governance, Cross-Border Payments, Blockchain.

1. Hypothesis
Stablecoin infrastructures face persistent systemic risks,
including redemption uncertainty, run amplification,
regulatory blind spots, fragmented cross-border
settlement, unpredictable fee structures, and weak
operational governance. This paper hypothesizes that the
GX network, built on jurisdictional Proof of Authority
(PoA), Cosmos-IBC interoperability, and Ethereum
Virtual Machine (EVM) programmability, provides a
framework capable of reducing such vulnerabilities by
embedding compliance and operational resilience
directly into the network architecture.

Stablecoins have emerged as a critical component of
digital finance, yet their architecture exposes users and
regulators to risks that undermine trust and systemic

stability [1], [2]. Existing models suffer from reserve
opacity, weak governance, and limited interoperability.
The GX network proposes a hybrid model that integrates
permissioned PoA consensus with Cosmos SDK,
Tendermint BFT, IBC interoperability, and EVM
execution. We hypothesize that this architecture can
address the aforementioned risks by aligning technical
design with regulatory requirements.
Redemption risk arises from the inability to guarantee
liquidity and transparency of reserves. GX mitigates this
through validator accountability under jurisdictional PoA,
requiring licensed institutions to enforce reporting
standards. Deterministic finality provided by Tendermint
ensures that redemption requests are processed without
backlog, reducing the amplification of runs.
Stablecoins often exploit jurisdictional gaps. In GX ,
every validator is legally bound to a jurisdiction,
embedding AML, CFT, and KYC compliance obligations
into the consensus mechanism. This approach reduces
blind spots by aligning validation authority with
supervisory oversight.

Cross-border settlement in stablecoin systems is often
fragmented and reliant on intermediaries. GX leverages
IBC to enable direct, auditable interoperability across
chains, ensuring that compliance is maintained
throughout transaction flows.

Volatility in transaction costs reduces stablecoin usability.
GX introduces fiat-priced , predictable gas fees governed
by deterministic PoA policy, preventing speculative
congestion pricing.

Governance in stablecoin ecosystems is frequently
opaque. GX governance is anchored to regulated
validators, ensuring transparency, enforceability, and
accountability. This jurisdictional model provides
operational resilience aligned with institutional
expectations.

This hypothesis suggests that GX provides a regulatory-
aligned, interoperable, and institutionally governed
settlement infrastructure capable of mitigating key risks
associated with stablecoins.

By embedding compliance into consensus, introducing
deterministic finality, and ensuring predictable
operational parameters, GX reframes stablecoins from
speculative assets into regulated, financial-grade
instruments.

2. Background: Policy Context and Rationale
The prevailing model of global stablecoins is USD-
centric and assurance-light, as many rely on ex-post
attestations and reserve mixes that include marketable
securities subject to price pressure under stress. That
arrangement digitizes legacy frictions rather than
removing them.

High‑volume remittance corridors and domestic retail
payments require predictable, local‑currency finality
with immediate redemption certainty.

GX addresses this constraint by embedding compliance
and transparency at the money layer while remaining
open to cross‑chain settlement hubs, where they improve
user outcomes and supervisory control [1].

2 .1 Redemption Uncertainty : Most existing
stablecoins treat redemption as a best-efforts obligation

rather than a guaranteed, time-bounded right. This
uncertainty manifests as:
i. Contractual ambiguity redemption is subject to
issuer discretion, suspension, or large minimum
thresholds.
ii. Operational opacity redemptions are routed
through manual, slow, or privileged channels[2].
iii. Information lag reserve conditions are disclosed
only monthly or quarterly, leaving markets to
speculate during stress[3].
iv. Run amplification, even rumors of delays or
hidden exposures trigger mass exits, pushing
secondary markets off-par [4].
2. 2 Run Amplification Under Stress : Lack of
granular disclosure forces markets to infer reserve
quality, often pessimistically. Confidence shocks trigger
runs that issuers cannot contain without fire-sales.
Central banks have dedicated significant research and
policy efforts to understanding and mitigating these
amplification mechanisms. The global financial crisis of
2007 - 2009 served as a stark reminder of their destructive
power, prompting a shift from a purely micro-prudential
focus (on the health of individual firms) to a macro-
prudential one (on the stability of the entire system).
Key policy tools and academic frameworks developed in
response include:
i. Macroprudential Stress Testing: Regulators
conduct system-wide stress tests to model how a
shock could propagate through the financial
network, identifying critical choke points and
potential feedback loops.
ii. Liquidity Coverage Ratio (LCR): The LCR, part of
the Basel III framework, requires banks to hold a
sufficient stock of high-quality liquid assets
(HQLA) to withstand a severe liquidity stress
scenario lasting 30 days. This is specifically
designed to absorb the initial shocks and prevent the
need for fire sales [5].
iii. Systemically Important Financial Institutions
(SIFIs): Institutions designated as SIFIs are subject
to enhanced regulatory scrutiny and higher capital
and liquidity requirements because their failure
could pose a significant risk to the entire system.
The "GX Stablecoins" paper alludes to this by
mentioning "Run Amplification Under Stress" and its
potential for a "liquidity mismatch " with existing
stablecoin models. This highlights a key regulatory
concern: whether the stablecoin's reserve assets are
sufficiently liquid and robust to withstand a mass
redemption event without collapsing its peg to the
sovereign currency, thereby amplifying stress in the
broader financial system.

2. 3 Regulatory Blind Spots : Many stablecoins
operate outside domestic legal perimeters, offering
regulators little visibility into flows or compliance. This
undermines trust and risks blanket prohibitions.

A recent Financial Times analysis highlights how global
stablecoin issuers can issue the same fungible tokens both
inside and outside the European Union. Because these
tokens lack jurisdiction-specific backing or unified
governance, the model permits regulatory arbitrage,
exposing domestic authorities to potential contagion and
undermining financial stability. In times of crisis,
domestic redemption obligations may collide with
foreign reserve structures, forcing regulators to intervene
under duress [6].

2. 4 Fragmented Cross-Border Settlement : Current
models either silo liquidity within closed networks or
push everything into USD rails, limiting local-currency
usability and inflating FX costs.

The GX Stablecoins Institutional Paper posits that the
current financial system faces significant systemic

1.2 Run Amplification Under Stress
stress and fragmented cross-border settlement. The
former risk is particularly acute in existing stablecoin
models, where a liquidity mismatch can transform a
localized redemption request into a system-wide run,
forcing fire sales that erode asset values [5].

This is compounded by the latter, as siloed liquidity and
reliance on a single dominant currency for cross-border
transactions inflate costs and introduce a single point of
failure. The GX network is designed as a direct response
to these dual challenges, offering robust, locally
compliant architecture that aims to provide both systemic
stability and efficient, multi-currency interoperability.

2. 5 Unpredictable Fees and Poor Retail Suitability :
Most incumbent stablecoins are deployed on general-
purpose public blockchains (e.g., Ethereum, Tron,
Solana), where congestion-auction fee models determine
transaction costs.

These models introduce several barriers to stablecoin
adoption in everyday retail and point-of-sale (POS)
environments: fee volatility (curved pricing models),
retail, poor user experience, regressive cost structure, and
systemic crowding-out of payments use cases [7].

2. 6 Weak Operational Governance : Issuers often
lack transparent governance, structured incident
response, or supervisory engagement [8].
From a central banking perspective, this concept is
central to ensuring financial stability and consumer
protection. It is a key reason why central banks and
financial regulators are increasingly concerned with the
operational resilience of non-bank financial institutions,
including stablecoin issuers. Weak governance can
manifest in several ways:
i. Lack of Transparent Governance : Issuers may not
have clear lines of authority, decision-making
processes, or accountability. This opacity makes
it difficult for both investors and supervisors to
understand how the stablecoin is managed,
especially during periods of market stress.
ii. Absence of a Structured Incident Response:
Without a pre-defined and tested plan, an
operational failure, such as a cyberattack, a
systems glitch, or an administrative error, could
lead to a chaotic and delayed response. This can
undermine public trust and trigger a run on the
stablecoin.
iii. Lack of Supervisory Engagement: A stablecoin
issuer with weak governance may fail to engage
proactively and transparently with its supervisory
authorities. This hinders regulators' ability to
monitor risks, enforce standards, and intervene
effectively to protect the financial system.
This concept is well-documented in regulatory
frameworks for financial market infrastructures (FMIs),
which emphasize the importance of comprehensive
operational risk management and clear governance
structures to ensure the continuity of critical financial
services, such as PFMI.
3. System Architecture
GX chains utilize a permissioned Proof of Authority
(PoA) ledger-based architecture, where validator roles
are confined to licensed and regulated entities operating
under domestic legal frameworks [9]. This model ensures
that consensus authority is exercised exclusively by
institutions with recognized accountability, thereby
embedding regulatory compliance and systemic
oversight directly into the consensus mechanism.
The architectural foundations of GX are constructed on
the Cosmos SDK framework, providing a modular and
scalable infrastructure that supports custom ledger design
while maintaining compatibility with broader blockchain
ecosystems.

Through the Inter-Blockchain Communication (IBC)
protocol, GX achieves secure cross-chain interoperability,
enabling asset transfers, data exchange, and settlement
finality between heterogeneous networks. This
interoperability is crucial for cross-border financial
services, as it enables GX to integrate seamlessly with
external ledgers while upholding compliance standards,
such as AML/CFT and KYC.

Additionally, GX implements an Ethereum Virtual
Machine (EVM) execution layer, enabling the
deployment of smart contracts and decentralized
applications within a familiar programming environment.
This integration ensures that existing Ethereum-based
financial applications can be ported to GX with minimal
friction, while benefiting from GX’s jurisdictional PoA
governance and compliance framework.

By combining Cosmos modularity, IBC interoperability,
and EVM compatibility, GX establishes a hybrid
architecture that strikes a balance between scalability,
regulatory trust, and developer accessibility.

3 .1 Jurisdictional PoA ledger with diversified validators
validators : The proliferation of consensus mechanisms
such as Proof of Work (PoW) and Proof of Stake (PoS)
has demonstrated the technical feasibility of
decentralized validation, but has not resolved the
question of institutional accountability. For financial
systems where settlement finality, regulatory oversight,
and systemic risk management are paramount,
pseudonymous validation introduces significant
limitations.

As shown in recent peer-reviewed research, PoA
consensus protocols inherently rely on a fixed set of
trusted validators, enabling both improved performance
and transparency, foundational prerequisites for
enforcing operational Service Level Objectives^1 (SLOs)
grounded in law and supervisory oversight [11][12].

GX proposed Jurisdictional Proof of Authority (PoA)
seeks to address this gap by anchoring validation
authority within regulated institutions that operate under
established legal frameworks, thereby embedding
jurisdictional legitimacy into the consensus process.

(^1) Service Level Objectives (SLOs) are formally defined, quantifiable
performance targets used to measure the reliability and effectiveness of
a service within a given timeframe. They typically include metrics such
as availability (uptime), latency (transaction processing time),
Table 1 Consensus Comparative Assessment
In the Jurisdictional PoA model, validators are not
selected through computational competition or economic
stake but through their status as licensed entities, such as
banks, payment service providers, or regulated
custodians operating under the supervision of specific
jurisdictions.
This approach ensures that every validation node is
subject to transparency requirements, auditability
standards, and enforceable accountability mechanisms.
As a result, the system aligns blockchain governance
with regulatory expectations for anti-money laundering
(AML), counter-terrorist financing (CFT), and settlement
oversight, thereby facilitating cross-border
interoperability under a compliance-first paradigm.
The adoption of Jurisdictional PoA has significant
implications for the integration of distributed ledger
systems with mainstream financial infrastructure.
By linking consensus authority to legal jurisdiction, GX
establishes a governance model that can interoperate with
central bank digital currency (CBDC) initiatives, real-
time gross settlement (RTGS) modernization, and
institutional-grade payment systems. The model thus
reframes blockchain validation not as a mechanism of
anonymous trust but as a legally accountable
infrastructure, positioning it as a credible foundation for
regulated digital finance.

3 .2 Automated mint/burn stack
architecture implements an automated, audit-ready
mint/burn framework (Figure 1) designed to meet the
prudential and supervisory standards set out in the Bank
for International Settlements’ Principles for Financial
Market Infrastructures (PFMI) [13]. This framework
ensures that all stablecoin issuance and redemption
processes are transparent, verifiable, and legally
enforceable within regulated jurisdictions.
Minting: Once a fiat deposit is entered into the user’s
wallet environment, the corresponding funds are
transferred directly to the designated custody bank.
Through a secure bank API integration, the confirmation
throughput, error rate, and settlement finality. In financial and
blockchain-based systems, SLOs provide measurable commitments
that connect technical design with institutional accountability, thereby
ensuring trust, regulatory compliance, and systemic stability.
of deposit automatically generates a mint request to the
GX Chain. At this stage, the GX consensus mechanism ,
based on jurisdictional Proof of Authority (PoA),
validates the transaction by requiring approval from
licensed institutional validators operating under domestic
regulatory regimes.

Following consensus, the system executes an escrow
settlement protocol, which ensures that the fiat backing
is legally and operationally locked prior to token creation.
The verified escrow event then triggers the deployment
of a smart contract, governing issuance parameters under
the GX architecture’s regulatory compliance rules.
Finally, the system mints and transfers the equivalent
tokenized representation of the fiat deposit to the user’s
wallet, ensuring one-to-one backing and instant
availability.

This automated lifecycle, from fiat custody to token
issuance, creates a closed, auditable loop that minimizes
redemption uncertainty, mitigates operational risks, and
enhances supervisory oversight. Moreover, the
deterministic nature of PoA consensus combined with
smart contract enforcement ensures that the mint/burn
process remains tamper-resistant, regulatorily compliant,
and institutionally credible.

The GX mint/burn framework comprises a capability-
scoped on-chain module integrated with a bank-API
orchestration layer (Figure 2), which executes token
issuance and redemption exclusively upon receipt of
authenticated banking events [15]. Every operation is
anchored to an append-only reconciliation log, with
segregated module accounts and tamper-evident records
to ensure durability and accountability [16].

Further, issuance and redemption require quorum-based
authorization under separation-of-duties protocols,
eliminating the possibility of unilateral or discretionary
minting[17]. This design guarantees a strict 1:1 mapping
between fiat funds held in custody and tokens in
circulation, while preserving full traceability for
supervisors and external auditors.

Burning: In complement to the minting process, the GX
architecture integrates an automated redemption and burn
framework that guarantees one-to-one fiat. This
framework ensures redemption requests are executed
transparently, with deterministic settlement finality and
continuous supervisory observability.

When a user submits a redemption request, the
transaction is automatically directed to the GX Chain ,
where an Escrow Settlement is initiated to lock the
stablecoins intended for redemption. Once the escrow
event is confirmed, the process invokes the relevant

Smart Contract , which allocates the request into a
Redemption Queue. The queue dispatches a burn request
to the GX Burn Module , which executes consensus
validation under the jurisdictional Proof of Authority
(PoA) mechanism.
Figure 1 GX CHAIN Mint/Burn
Following validation, the Burn Module triggers a real-
time gross settlement (RTGS) sequence, ensuring that
fiat liabilities are settled in finality before token
destruction. A fiat payout instruction is then transmitted
to the designated custodial bank, which performs the
transfer of fiat funds to the user’s external bank account,
thereby completing the redemption cycle (figure 1).
Throughout both minting and burning processes, the Live
Reserves Scanner (LRS) operates transversely,
continuously monitoring custody accounts in real-time.
LRS ensures that every issued token remains fully backed
by reserves and provides on-demand telemetry to
authorized supervisory entities possessing the
appropriate cryptographic keys (Figure 3). This
mechanism establishes continuous, verifiable
transparency, thereby reducing redemption uncertainty
and reinforcing institutional and regulatory confidence.
These GX principles govern critical infrastructures such
as Real-Time Gross Settlement (RTGS) systems (Figure
2), Central Securities Depositories (CSDs), and Central
Counterparties (CCPs), emphasizing segregation of
duties, auditability, operational resilience, and
enforceable settlement finality.
By aligning with PFMI expectations and drawing on
operational practices from RTGS systems like TARGET
(Eurosystem), Fedwire (Federal Reserve), and BOJ-NET
(Bank of Japan), GX ensures that stablecoin issuance and
redemption are managed with controls equivalent to
those applied to systemically important payment
infrastructures [14].

Figure 2 GX CHAIN Bank API Layer

Such an approach aligns with established supervisory
expectations for operational resilience, separation of
duties, and auditability in financial market infrastructures.
By embedding these controls in the money layer, GX
ensures that stablecoin issuance is not merely trust-based
but enforceable in real time [18].

3 .3 Reserve policy and transparency
reserves may be maintained as 100% cash in licensed
domestic custody accounts to ensure immediate liquidity
and eliminate redemption uncertainty according Basel
Committee on Banking Supervision - Basel III [19], [20].

This primary Basel publication explicitly defines the
regulatory haircuts applied to different categories of
High-Quality Liquid Assets (HQLA) to reflect price
volatility and liquidity risk (e.g., 15% for Level 2A
assets, and 25–50% for Level 2B assets when included in
the HQLA buffer) [21].

Over time, and only in accordance with explicit
regulatory guidelines per jurisdiction, a defined (capped)
portion of reserves may be deployed into regulator-
approved, ultra-short, HQLA , such as T-bills^2 or secured
pre-arranged repos facilities (no forced asset sales) while
continuing to disclose holdings in real time [19][22][23].

(^2) Treasury Bills (T-bills) are short-term debt obligations issued by a
national government, typically with maturities ranging from a few days
up to one year. They are considered risk-free instruments as they are
backed by the full faith and credit of the issuing sovereign. T-bills are
generally issued at a discount and redeemed at face value at maturity,
3 .4 Live Reserve Scanner- Real-Time Proof-of-
Reserves and Liquidity Telemetry : The LRS reconciles
banking system balances with on-chain circulation at
minute-level granularity (Figure 3).
It reports total reserves and circulation, cash headroom
𝐻!, the maturity ladder 𝑀" of ultra-short bills, committed
repo capacity ρ with conservative haircuts (ℎ)^3 [ 24 ],
custodian and counterparty concentrations; redemption-
queue depth with an SLA meter (Figure 1) and derived
prudential metrics such as GX-LCR(H) and utilization ρ∗.
[20], [25][26], [27]. These disclosures remove the
informational opacity that has historically triggered panic
during market stress.
A regulator observer API provides read-only supervisory
access to state and telemetry, as shown in Figure 3 (LRS-
Life Reserve Scanner). This usage underscores the
fundamental importance of a robust operational and
regulatory framework.
Figure 3 GX CHAIN LRS
GX aims that a stablecoin's success is not solely
determined by its technical design, but also by its ability
to address and mitigate systemic risks, such as run
amplification, regulatory blind spots, and weak
governance. The LRS module is the mechanism for
achieving reliability and, by extension, ensuring the
stablecoin's trustworthiness.
providing predictable liquidity and minimal credit risk, making them
widely used as reserve assets in financial institutions and payment
infrastructures.
(^3) Haircut is the percentage discount applied to the market value of
collateral when determining its lending or liquidity value.

3 .5 Retail performance and scale out : To support
real-world micropayments (transit gates, tolling, vending,
telco top-ups, in-app purchases), GX is designed to target
sub-second confirmations on retail lanes and five-figure
TPS^4 on commodity infrastructure in PoA settings with
known validators, consistent with CBDC pilot
benchmarks [28][29][30].

Where local conditions call for higher throughput, ultra-
low latency, or specialized device integration,
deployments can introduce use-case–specific scale-out
operated under the same compliance and reconciliation
envelope. Specific proprietary mechanisms will be
selected jointly with operators and supervisors and are
designed to integrate with existing systems.

3 .6 Integration with existing system
to provide adapter modules for enterprise and public-
sector environments, interfacing with existing fare-
collection devices, smart cards, validators , Payment
Service Providers (PSP), merchant systems, and
operational databases. Interfaces support idempotent
posting, defined reconciliation windows, and operational
telemetry.

Idempotent posting is a key feature of the GX network's
integration with existing financial systems. Here's what
that implies from a financial and technical perspective:

i. Reliability : If a payment instruction is sent but the
sending system doesn't receive confirmation, it
can safely resend the request. Because the system
is designed to be idempotent, the payment will
only be processed once. This prevents issues like
double-debiting a user's account or double-
crediting a merchant.
ii. Reconciliation : Idempotency greatly simplifies
the process of reconciling transaction records
between different systems (e.g., between the GX
network, a merchant's system, and a Payment
Service Provider). It ensures that the transaction
history remains consistent and accurate, even if
there were communication issues during the
original transaction.
(^4) In this specific paragraph, it refers to the target performance of the GX
network's retail payment lanes. A "five-figure TPS" (Transactions Per
Second) means the system is designed to handle at least 10,
transactions per second on commodity infrastructure. This metric is
presented as a benchmark consistent with the performance goals of
modern Central Bank Digital Currency (CBDC) pilot programs.
(^5) A Trusted Execution Environment (TEE) is a secure area within a
processor that provides an isolated environment for code execution and
data handling. TEEs ensure that sensitive operations are protected from
the host operating system, applications, and potential attackers, even if
the main system is compromised.
iii. Operational Resilienc e: This feature is crucial for
operational resilience. It allows the system to
recover from a wide range of failures without
human intervention, ensuring the continuous and
reliable operation of the payment infrastructure. It
is a critical component for systems that must be
available 24/7, such as those for retail payments
and central bank digital currency (CBDC) pilots.
Where higher assurance is required, selected components
can run in Trusted Execution Environments^5 (TEEs) with
attestation available to supervisors. Implementation
materials will be provided to operators and supervisors as
needed, and integration is designed to proceed without
rip and rip-and-replace of existing systems [31], [32].

3 .7 Offline payments (bounded risk)
intermittent-connectivity environments, GX can support
an offline mode for low-value flows. Value transfer
would be recorded locally with secure hardware
attestations, policy caps, and time-bounded validity, then
reconciled to the chain when connectivity returns.
Double-spend controls could include spend limits, rolling
counters, and post-reconciliation checks.
3 .8 Wallet/Application Compliance
enforced at the wallet and application tiers by
implementing KYC/AML, PEP sanctions, screening,
travel-rule messaging (as is Financial Action Task Force
(FATF) Recommendation 16), per-wallet remittance
limits, and jurisdiction-specific allow/deny lists, all
versioned and auditable, without requiring invasive
changes to the core chain [33], [34], [35].
3 .9 Redemption and De-Peg Risk in Existing Stablecoins
Stablecoins : In most incumbent stablecoin arrangements,
redemption is framed as a “best-efforts” obligation rather
than a hard, time-bounded right, and visibility into
reserves is limited to periodic attestations (typically
monthly or quarterly). In market stress, that combination
of legal ambiguity plus informational lag creates fertile
conditions for self-reinforcing runs[33].
A confidence shock (a rumor, a custodial exposure, or a
delayed payout) accelerates redemption. Issuers holding
Confidentiality: Data processed within a TEE cannot be accessed or
tampered with by unauthorized parties.
Integrity: Code and data executed inside the TEE cannot be altered by
external software.
Attestation: TEEs generate cryptographic proofs that allow external
parties (e.g., supervisors) to verify that specific code is running in a
secure enclave as intended.
a meaningful share of reserves in longer-dated or less-
liquid instruments must sell into thinning markets. This
creates a secondary-market price gap, which further spurs
redemptions, pushing the peg away from “ pa r”.

Episodes such as USDT’s de-peg in 2022 and USDC’s
de-peg in March 2023 illustrate that even “fully backed”
instruments can experience sharp, short-lived
dislocations when redemption velocity outruns same-day
liquidity. Absent granular, real-time disclosures and clear
liquidity policies, markets are left to infer, often
pessimistically, thereby amplifying the run dynamic [36].

3 .10 Liquidity and Redemption Dynamic s: In
incumbent stablecoin arrangements, liquidity stress can
trigger a self-reinforcing feedback loop. GX is
engineered to break that feedback loop:

i. Confidence Shock – Rumors, custodial exposures,
or delayed redemptions undermine user
confidence.
ii. Accelerated Redemptions – Token holders rush to
redeem, often exceeding same-day liquidity
capacity.
iii. Forced Asset Sales – Issuers holding longer-dated
or less liquid instruments are forced into
distressed sales to meet redemptions.
iv. Market Price Dislocation - Secondary markets gap
away from par^6 , amplifying redemptions as
arbitrageurs and retail holders exit en masse^7.
v. Run Dynamics Entrench - The cycle reinforces
itself (Figure 2)
Uncertainty → Redemptions → Fire sales → Price dislocations →
More redemptions.
Figure 4 Run feedback loop

We model redemption arrivals as a point process with
intensity 𝜆 (redemptions/day) and average redemption
size q (fiat). Same-day liquid capacity is defined as:

𝐶!=𝐻!+ ( 1 −ℎ)∗ 𝜌
Equation 1 Same-day liquid capacity

Where 𝐻! is the same-day cash floor, ρ is, repo capacity
against repo-eligible HQLA , and ℎ is a conservative
haircut [37], [38], [39].

(^6) Maintaining a stablecoin's value "at par" is a key indicator of its
operational and financial stability. A de-pegging event signals a loss of
confidence and highlights a failure in the issuer's ability to maintain
sufficient liquidity to meet redemption demands.
The implied same-day service rate is:
𝜇=𝐶!/𝑞
Equation 2 Same-day service rate
and the utilization ratio is:
𝜌∗=𝜆/𝜇
Equation 3 Utilization ratio
Stability requires 𝜌∗< 1 with margin. Therefore, to
formalize these definitions and the stability condition, let
𝐻!denote same‑day cash headroom ; ρ the committed
repo capacity against repo‑eligible HQLA ; ℎ the
conservative haircut ; 𝓆 the average redemption siz e; λ
the redemption arrival rat e; and 𝑅𝐷$ the fiat redemption
demand over horizon H [22], [40], [41], [42].
Figure 5 GX-LCR(H) across horizons (H = 0, 1, 5, 30 days).
In Figure 3, the chart shows a simulation based on
assumptions that show high coverage at intraday
horizons tapering as H increases, which is what is
expected when stress accumulates across days:

H₀ = $75M,
ρ = $200M,
h = 5%, 𝐸𝑆%(𝑅𝐷$ ) rising with H.
GX-LCR(H) = (H₀ + (1−ℎ)·ρ) /𝐸𝑆%(𝑅𝐷$ )
And, for the Horizon-specific liquidity coverage, =𝐺𝑋−
𝐿𝐶𝑅(𝐻)A, we map Basel LCR to the GX redemption
window H by defining Net Cash Outflows and High-
Quality Assets ratio over horizon H as:
(^7) En masse" is a French expression that means "in a mass," "in a
group," or "all together.

=𝐺𝑋−𝐿𝐶𝑅(𝐻)A=
𝐻𝑄𝐿𝐴$
𝑁𝐶𝑂𝐹$
Equation 4 Horizon-specific liquidity coverage

with:
𝐻𝑄𝐿𝐴$=𝐻!+( 1 −ℎ)∗𝐻𝑄𝐿𝐴&'()-'+,-,.+'
and
𝑁𝐶𝑂𝐹$≡𝐸𝑆%(𝑅𝐷$)
Where the Expected Shortfall (ES) of redemptions over
H at confidence α target GX-LCR(H) ≥ 1 with
supervisory buffer[20], [40].

For the NSFR interpretation, GX publishes an analogue
operational NSFR to evidence structural resilience, even
though token liabilities are fully matched by segregated
reserves[22], [42].

𝐺𝑋−𝑁𝑆𝐹𝑅=
𝐴𝑆𝐹/
𝑅𝑆𝐹/
Equation 5 Analogue operational NSFR

Where Available Stable Funding 𝐴𝑆𝐹/0 comprises
permanent capital and committed lines>1y, and the
Required Stable Funding 𝑅𝑆𝐹/0 applies regulatory
factors to cash, central-bank cash, and short-dated bills.

Legal segregation ensures tokens are always covered 1:
by reserves, irrespective of the Net Stable Funding Ratio
(NSFR)[41].

The Live Reserve Scanner publishes real-time estimates
𝝀J (Redemption arrival rate (per day) variation) and 𝜇̂
(Service rate variation) so participants and supervisors
can verify that ρ* remains comfortably below one.

2.11 Reserve Composition and Risk Policy
launch, 100% of reserves are maintained in cash at
licensed custodian bank entities, diversified with binding
concentration limits to ensure immediate redemption
capacity.

Over time, only where expressly permitted by domestic
regulation, a capped fraction of reserves may be allocated
to ultra-short Treasury bills managed on a roll-down
ladder with a weighted-average maturity well under one
quarter.

Liquidity against such securities is raised via pre-
arranged repos, not secondary-market sales. Callable
cash from those facilities is:
( 1 −ℎ) S
Equation 6 Callable cash
Where S is the securities notional and ℎ the disclosed
haircut[37]. Horizon-specific coverage is calibrated to
Expected Shortfall (ES) at confidence level α; we define:
𝐺𝑋−𝐿𝐶𝑅(𝐻)=
𝐻!+( 1 −ℎ)∗𝜌
𝐸𝑆%[𝑅𝐷$]
Where RDH denotes redemptions over horizon H.
𝐶!=𝐻!+( 1 −ℎ)∗𝜌
Equation 7 Same-day liquid capacity without market sales
and,
𝜇=
𝐶!
𝑞
Equation 8 Same day service rate in redemptions/day)
for utilization:
𝜌∗=
𝜆
𝜇
Stability requires ρ* < 1 with margin or policy target ρ*
≤ 0.7 even under stress to keep headroom.)
4. Fees and Gas Model
Gas is paid in the local GX stablecoin , and transaction
fees are denominated and fixed in fiat terms, published
within narrow bands to preserve point-of-sale usability
(e.g., USGX: $0.013 per transaction, or the local-
currency equivalent to other GX chains).
Let 𝑔 denote the fiat fee per transaction:
𝑔
And N as the daily transaction count:
𝑁
then,
𝑅=𝑔∗𝑁
Equation 9 Total operating revenue (in fiat terms)

Then, the Operating revenue from Equation 9, where 𝑔
The fiat-denominated fee per transaction and N is the
daily transaction volume, which provides the economic
foundation for sustaining the GX ecosystem. Unlike
congestion-auction fee models, GX’s fixed-fee design
produces a stable and predictable revenue stream[13].

This revenue is earmarked for three critical functions:

i. Validator Operations – compensation for
licensed validator institutions operating the PoA
consensus layer, covering infrastructure,
security, and compliance monitoring.
ii. Supervision Tooling – funding of real-time
reserve scanners, reporting dashboards, and
compliance messaging infrastructure, ensuring
continuous supervisory visibility.
iii. Business-Continuity Controls – provisioning of
redundancy, disaster-recovery capacity, and
incident-response reserves, in line with
standards for systemically important financial
market infrastructures.
To ensure long-run sustainability while retaining price
predictability, the fee schedule may be optionally
indexed to a governance-set marginal inflation parameter
(e.g., up to 2% per annum, or a CPI-linked cap )^8 , with
any adjustments pre-announced and disclosed on the
Scanner.

Paymaster contracts allow institutions to sponsor all or
part of end-user fees, particularly during early adoption.
Thus, wallets and merchant apps can deliver a fully
abstract experience without undermining transparency.

The Deterministic finality and Capacity management (no
congestion auctions) prevent surge pricing under bursty

(^8) Consumer Price Index. It is a widely used economic indicator that
measures changes in the average price of a basket of consumer goods
and services over time.
(^9) In the GX system, keys are cryptographic credentials that control
access, authorization, and visibility. They include:
Signing Keys: Private keys that authorize critical operations such as
minting, burning, validation, or transfer of regulated instruments. These
are safeguarded in Hardware Security Modules (HSMs) or protected
with multi-party controls.
loads, maintaining a stable, retail point-of-sale–grade
user experience even at peak throughput[11].

5. Compliance, Governance, and Supervision
GX enforces compliance with the wallet/application
layer, independently of the base ledger. Features such as
embedded KYC/AML verification, travel-rule messaging,
sanctions/PEP screening, and jurisdictionally
configurable remittance rules are implemented client-
side for precision and privacy.
This design echoes the blockchain-based decentralized
Travel Rule systems proposed in recent research, where
peer-to-peer authenticated exchange of originator and
beneficiary data (geo-parameters) is secured without
reliance on central intermediaries [43].
Policy logic is versioned and auditable; compliance
events (e.g., threshold breaches, sanctions hits) generate
immutable audit records anchored on-chain with
references to off-chain evidence.
Personally identifiable information remains off-chain;
selective-disclosure “view keys^9 ” allow authorized
supervisors to inspect provenance without broad data
exposure, consistent with domestic privacy law.
Governance is executed by a whitelisted set of PoA
validators operating under published SLOs/SLAs.
Figure 6 GX Validator Key Control and Change Management Flow
GX validators are backed by cryptographic keys secured
in Hardware Security Modules (HSMs)(Figure 6),
View Keys: Read-only keys enabling selective disclosure of transaction
or position data to supervisors and auditors without exposing such
information publicly.
Workflow Keys: Keys integrated into segregation-of-duties
frameworks, ensuring that system changes, releases, and operational
actions require multi-party authorization.
tamper-resistant devices standard in institutional custody
that ensure secure key generation, storage, and
protection, and leverage multi-party control mechanisms
(e.g., HSM + MPC hybrid) to enforce quorum-based
authorization and avoid single points of failure [44].

In Figure 4, the operational safeguards are applied to GX

validator governance. Cryptographic keys are generated
and secured within Hardware Security Modules (HSMs)
(Figure 6), ensuring tamper-resistant key management.

Access to validator signing privileges is governed by

multi-party control (MPC quorum), eliminating single
points of failure. Proposed changes to validator software
follow a formal change-management pipeline:

i. Pre-announced release proposals.
ii. Testing and regression gate.
iii. Deployment only within scheduled release
windows.
All deployments include a rollback mechanism and
immutable audit trail, aligning GX validator operations
with prudential standards for operational resilience,
segregation of duties, and auditability established under
the Principles for Financial Market Infrastructures
(PFMI) [13].

GX includes an Emergency Procedures Playbook^10 that
defines supervised circuit breakers, such as rate limits,
mint/burn suspension, or settlement pauses, activated
only under strictly defined stress conditions[45]. These
measures are designed and coordinated with the
regulator's involvement and are followed by post-event
disclosure.

The theoretical foundation is grounded in welfare-
optimised circuit breaker literature that demonstrates
how such mechanisms can stabilize liquidity runs when
calibrated [46]. Regulatory frameworks, like MiFID II,
mandate that trading venues implement built-in halts and
transparent disclosure regimes for emergencies [45],
[46], [47], [48], [49], [50].

Experimental evidence further shows that circuit
breakers can improve outcomes during runs,
exceptionally when information clarity is maintained
[51].

(^10) The Emergency Procedures Playbook is a formalized set of
predefined, rules-based controls that can be invoked in the event of
market stress, operational disruption, or systemic risk. It ensures orderly
functioning and supervisory coordination under exceptional conditions.
GX’s Live Reserve Scanner delivers continuous
supervisory transparency, synthesizing on-chain data,
bank/custodian reconciliations, redemption-queue
telemetry, and redemption flows into auto-generated
reports accessible via read-only keys and secure APIs.
Supervisors receive the read-only observer keys and
authenticated APIs for real-time access to:
× Reserves vs. Circulation.
× Cash headroom 𝐻!.
× Maturity ladder 𝑀(").
× Committed repo capacity ρ.
× Haircuts h.
× Utilization ρ*.
× SLA conformance.
This approach parallels innovations in blockchain-
enabled financial reporting: for instance, a blockchain
accounting framework provides real-time, tamper-proof
reconciliation of financial statements and liquidity
metrics [52].
Event-driven alerts (e.g., breaches of concentration
limits, LCR/ES buffers, or unusual flow patterns) are
delivered to designated authorities. Lawful-order
workflows (freeze/unfreeze, address allow/deny lists) are
implemented with explicit role separation and full
auditability.
Operational controls, business-continuity and disaster-
recovery plans, third-party risk management, and
independent audits (security, financial, and compliance)
complete the supervisory perimeter and are summarized
in the Scanner’s (LRS) supervisory dashboard.

6. Interoperability and Foreign‑Exchange Connectivity
GX chains interoperate with Internet Block Chain (IBC)
and Ethereum Virtual Machine (EVM) ecosystems and
include a Foreign Exchange (FX) layer as a core feature
that natively supports regulated FX settlement across
chains, making it function like a real-time on-chain CLS
(Continuous Linked Settlement) system [53].
Data from the BIS Quarterly Review underlines the scale
of FX settlement risk and the urgent need for PvP
mitigation , Bank for International Settlements[53]. On-
chain FX implementations such as those using automated
Key features include: Supervised Circuit Breakers, Regulatory
Participation, Post-Incident Disclosure, Systemic Protection.
market makers have shown the potential to cut remittance
costs by up to 80% while preserving rate fidelity [54].

Atomic settlement protocols utilizing hash-time-locks
(HTLCs) achieve the conditionality required for PvP,
ensuring that one leg of a trade completes only alongside
the other [55].

The design follows a simple principle:

Comply where required, permits where allowed.
Sovereign obligations, including minting, burning,
redemption, custody, and wallet-level KYC/AML , are
handled on the local PoA chain with fully identified
wallets and policy limits. Once funds are lawfully on-
chain in a KYC wallet, users may route FX swaps across
compatible networks, subject to the same wallet-level
controls already in place (e.g., per-wallet limits, travel-
rule metadata, sanctions screening) [43].

GX stablecoins implement standard token interfaces, so
they are natively swappable on exchanges and hub chains
meet the same interoperability expectations as leading
stablecoins (e.g., USDC, USDT, DAI, BUSD, TrueUSD,
FRAX).

Cross-currency flows can clear on venues such as
Partior, Baton Systems’ Core FX, Fnality + Finteum,
Meridian FX, mBridge, Circle’s upcoming Arc
blockchain, and on IBC/EVM venues like Gurufin (via
Guru Station ) using payment-versus-payment (PvP)
settlement with escrowed holds (e.g., IBC/HTL^11 ),
ensuring simultaneous finality; neither leg settles unless
both do.

FX liquidity may be supplied by regulated LPs, banks,
PSPs, and market makers, who post two-sided inventory
to whitelisted currency pools with:

(i) Inventory bands.
(ii) Concentration and counterparty caps.
(iii) Transparent maker–taker fees.
(iv) dynamic fee guards under volatility.
For correlated pairs (stablecoin ↔ stablecoin ), pools use
low-curvature (Figure 5) stable-swap curves to minimize
slippage; large tickets can be time-weighted
(TWAP^12 /TWAMM^13 ) to reduce footprint. Pool

11 Hash Time-Locked Contract: It’s a type of smart contract widely
used in cross-chain and payment-versus-payment (PvP) settlement to
ensure that either both legs of a transaction complete, or neither does.

(^12) TWAP (Time-Weighted Average Price): An execution strategy that
breaks a large order into smaller, evenly sized trades executed over
time, aiming to match the average market price across the chosen
interval. Purpose: minimize slippage and market impact.
telemetry (depth, realized slippage, utilization) is
published in real time to the Scanner [56], [57], [58].
Figure 5 contrasts the constant-product invariant used in
general-purpose AMMs (e.g., Uniswap v2) with a low-
curvature stable-swap invariant (e.g., Curve-style design)
[57].
The constant-product model maintains liquidity across
the full price domain but imposes high marginal slippage
even near parity, making it less suitable for correlated
assets such as stablecoin ↔ stablecoin pairs. In contrast,
the low-curvature stable-swap design produces an almost
linear region around the 1:1 peg, significantly reducing
slippage for trades executed near parity. At larger
imbalances, the curve steepens to restore pool
equilibrium[56], [57].
Figure 7 Comparative Pricing Curves in Automated Market Makers
(AMMs)
GX’s adoption of a low-curvature invariant for
stablecoin-to-stablecoin swaps rests on solid theoretical
and empirical foundations. Recent research by Bergault
et al. (2024) demonstrates that tailored AMMs calibrated
for pegged asset dynamics can deliver efficient pricing
and depth using multi-level OU process models.
Separately, Engel & Herlihy (2021) show that Curve-
style invariants maintain low slippage and minimal
divergence loss around parities, while The AMM Book
(2025) mathematically describes how the stable-swap
(^13) TWAMM (Time-Weighted Automated Market Maker): A smart-
+contract–based mechanism that allows large orders to be natively split
and executed gradually over many blocks within an AMM. Purpose:
achieve continuous TWAP execution on-chain, reducing price footprint
and making large trades more efficient and less disruptive.

curve flattens near peg via a parameterization
mechanism, widening the minimal slippage.

Collectively, these findings justify GX’s design choice,
ensuring cost-effective and deep liquidity for retail-grade
FX settlement under supervisory visibility [59], [60],
[61].

GX incorporates an optional central bank/CBDC
backstop, a narrow-band liquidity provision mechanism,
activated under stress, operating under rules defined by
Memorandum of Understanding (MoUs), and fully
transparent via supervisory reporting. This mirrors the
institutionalization of central bank swap lines into
standing global liquidity backstops and coordinated
central bank systems, such as those providing USD
liquidity during market [62], [63].

These frameworks require operational preparedness and
collateral readiness, aligning with GX’s design of a time-
bounded, conditional backstop, as outlined by the Bank
for International Settlements. In CBDC contexts, too,
central banks are exploring how digital currencies could
support cross-border liquidity and systemic
resilience [64], [65].

The principle of the central bank as a lender of last resort
for digital money systems also aligns with authoritative
proposals for anchoring digital [66]

7. Tokenized Assets and Programmable Finance
GX chains are jurisdiction-specific Layer-1 ledgers that
natively support regulated tokenized instruments
alongside their stablecoins. The purpose is trusted market
infrastructure, not speculation, so issuance, transfer, and
lifecycle events (corporate actions, disclosures,
redemptions) are programmable under local law and
supervised in real time.

GX chains are jurisdiction-specific Layer-1 ledgers,
designed to host regulated tokenized instruments
alongside stablecoins. Their role is to provide trusted
market infrastructure, not speculative assets, with
issuance, transfer, corporate actions, disclosures, and
redemptions encoded in compliance with local law. This

(^14) Real-World Assets (RWAs) are off-chain financial or tangible
assets—such as government bonds, commercial paper, trade
receivables, real estate, or commodities—that are digitally tokenized
and represented on a blockchain. Each token functions as a digital claim
on the underlying asset, enabling on-chain transferability, fractional
ownership, and programmable settlement, while the legal rights and
obligations remain anchored in traditional frameworks (e.g.,
prospectuses, registries, CSDs).
approach is aligned with international research on the
tokenization of assets and financial infrastructures [67].
Furthermore, GX integrates the principle of embedded
supervision, ensuring supervisors can observe lifecycle
events in real time without requiring duplicative
reporting structures. By grounding tokenization and
supervision in the domestic legal framework [68], GX
ensures programmability is consistent with statutory
obligations while delivering institutional-grade
assurance.
7 .1 Scope and Asset Classes : Subject to licensing
and prospectus requirements, GX supports issuance of
tokenized deposits, real-world assets^14 (RWAs) such as
commercial paper and trade receivables, and securities
tokens, including equity, bond, and fund unit
representations, under recognized regulatory
frameworks.
In Ethereum Virtual Machine (EVM) environments, GX
conforms to standards like ERC-20 for fungible assets,
ERC-1400/3643 for regulated and partitioned securities,
and ERC-721/1155 for credential or NFT-style
attestations. Within IBC settings, GX leverages CW- 20
tokens with compliance extensions (e.g., transfer
restrictions, partitions), transmitted via ICS-20 and
coordinated using ICS-27, with ICS-721 facilitating
credential/NFT attestations.
Reflecting broader institutional adoption trends,
tokenization extends beyond speculative use cases to
include deposits and RWAs under compliant
architectures [69], [70]. Standards such as ERC-1400 and
modular IBC token mechanisms are increasingly
recognized in cross-border and regulated contexts [71],
[72].
Programmable credentials and attestations serve identity,
permits, and benefits, not as bearer value, but as
verifiable access claims tied to KYC wallets. Listings and
offers remain within the domestic perimeter or
recognized cross-border regimes.
7 .2 Legal linkage and registries : Each instrument is
anchored to an authoritative register, typically an issuer,
transfer agent, or central securities depository (CSD^15 ),
(^15) A Central Securities Depository (CSD) is a financial market
infrastructure that provides centralized custody, safekeeping, and
settlement of securities. CSDs maintain authoritative records of
ownership, enable transfer of title, and often support corporate actions
(e.g., dividends, voting).

that maps on-chain token units to off-chain legal rights
such as ISIN^16 , CUSIP^17 , or local equivalents.

The register enforces jurisdiction-specific rules
(eligibility, limits, suitability) and reconciles
continuously with the on-chain state. Supervisors are
granted authenticated API access to query both registers
and chain data in real time. This approach reflects
regulatory consensus that tokenized instruments must
preserve legal enforceability, link to authoritative
registries, and support supervisory observability [73],
[74].

6.3 Issuance and transfer controls
issuance targets whitelisted, KYC wallets under offering
documents; secondary transfers are policy-checked at
settlement (suitability, holding limits, lockups, travel-
rule metadata). Instruments embed transfer restrictions
(e.g., partition-leve l rules for retail/professional
investors) and event hooks for disclosures and voting,
preserving finality while ensuring every movement
satisfies jurisdictional constraints without retroactive
ledger edits.

7 .5 Atomic settlement, DvP and PvP : Tokenized
assets on GX settle via Delivery-versus-Payment^18 (DvP )
atomically against the corresponding stablecoins within
the same jurisdiction, while cross-currency legs are
executed using Payment-versus-Payment^19 (PvP)
protocols via recognized FX settlement venues,
mitigating principal risk with atomicity , accelerating
settlement to T+0 or near real-time , and preserving
comprehensive post-trade audit trails [75], [76], [77],
[78].

6.6 Market infrastructure and venues
RFQ^20 venues, and AMM^21 pools are policy-scoped.

(^16) A Central Securities Depository (CSD) is a financial market
infrastructure that provides centralized custody, safekeeping, and
settlement of securities. CSDs maintain authoritative records of
ownership, enable transfer of title, and often support corporate actions
(e.g., dividends, voting). Examples include DTCC (US), Clearstream
(Luxembourg), and Euroclear (Belgium).
(^17) A CUSIP is a 9-character alphanumeric identifier assigned to
securities in the United States and Canada. Managed by the CUSIP
Global Services (CGS) system, it identifies issuers and instruments
(stocks, bonds, derivatives) for clearing, settlement, and regulatory
purposes. CUSIPs are functionally similar to ISINs but are region-
specific.
(^18) DvP is a settlement mechanism in which the delivery of a security
occurs if and only if the corresponding payment is made. It removes
principal risk by linking asset transfer (e.g., bond, equity, tokenized
RWA) directly to the associated cash leg.
(^19) PvP is a settlement mechanism used in foreign exchange (FX)
transactions, where the payment in one currency occurs if and only if
Order flow can be segmented by investor class and
instrument type, with circuit breakers, price bands, and
maker–taker schedules published ex ante. Venue
telemetry (depth, turnover, slippage, circuit triggers) is
made available by the venue and mirrored in near-real
time to the GX Scanner LRS for supervisory
visibility[78], [79].

6.7 Lifecycle automation and corporate actions
Dividends, coupons, and redemptions follow smart-
contract timetables with configurable record dates and
withholding rules. Proxy voting and consent solicitations
use verifiable ballots tied to partitioned holdings;
outcomes and quorums are posted on-chain with required
off-chain attestations [75], [80].
7. 8 Data protection and privacy : Personally
Identifiable Information^22 (PII) remains off-chain ; on-
chain records carry only the minimum necessary
metadata.
Where policy allows, selective-disclosure view keys or
privacy-preserving proofs conceal commercial amounts
from the public while preserving full supervisory
auditability.
Keys and signing workflows are certified hardware
security module HSM)- guarded ; selected adapters may
run in Trusted Execution Environments (TEEs) with
attestation available to supervisors.
7 .9 Interoperability and portability : Because GX is
IBC/EVM- compatible, approved representations of
regulated instruments can bridge to recognized venues
with policy-enforced gateways.
the payment in the other currency occurs simultaneously. PvP
eliminates settlement (Herstatt) risk in cross-currency trades.
(^20) An RFQ (Request-for-Quote) is a trading protocol where a buyer or
seller requests executable price quotes from one or more market
makers. RFQs are widely used in fixed income, FX, and OTC markets,
allowing for segmentation by investor class, instrument type, and trade
size, and are increasingly implemented on electronic and DLT-based
venues for regulatory visibility.
(^21) An AMM (Automated Market Maker) is a decentralized trading
mechanism where assets are priced and traded against liquidity pools
governed by algorithmic pricing functions, rather than traditional order
books. AMMs enable continuous liquidity provision, with slippage and
execution quality determined by the pool’s invariant function and
depth. They are widely studied in the context of DeFi and tokenized
asset markets.
(^22) Personally Identifiable Information (PII) refers to any data that can
be used to identify a specific individual, either directly or when
combined with other information. Examples include names, addresses,
ID numbers, account details, biometrics, or combinations like date of
birth plus postal code.

Price formation may occur on an external hub, while final
delivery remains DvP/PvP back to the home chain under
local oversight.

7 .10 Policy stance : Tokenization on GX is
compliance-first by design: rule sets are explicit,
machine-checked at transfer, and continuously
observable via the Scanner LRS.

The result is a natural extension of GX’s sovereign rails:
trusted stablecoin settlement coupled with regulated
token markets, enabling instant DvP , programmable
lifecycle events, and lower operational “ risk-ready ” for
activation as jurisdictions and market participants
engage.

8. Security and Privacy
8 .1 Institutional assurance : GX’s architecture
incorporates components such as consensus modules,
mint/burn flows, bank-API connectors, and the
supervisory LRS , which undergo independent security
reviews and continuous auditing, aligned with Federal
Reserve recommendations for CBDC [81].

Transparency is enforced through tamper-proof logging
akin to BlockAudit^23 ensuring any issuance or redemption
event is permanently auditable [82].

Release protocols strictly embed separation of duties and
regression gating, reflecting core PFMI principles
(Separation of Duties). Smart contract configuration
mechanisms further anchor changes and configuration
traceability via permissioned blockchain enhancements
[83], [84].

GX’s secure development lifecycle is informed by
modern Secure Development Lifecycle (SDL) paradigms,
ensuring operational monitoring, incident response, and
audit lessons are fed back directly into development [85].

Key material is protected in certified hardware security
modules (HSMs^24 ) and governed by multi-party controls
(threshold authorization, dual control, rotation policies,
and break-glass procedures). Validator (Figure 6) and
treasury actions require quorum approvals; keys are

(^23) BlockAudit is a blockchain-based audit logging framework that
records system events on an immutable, cryptographically linked
ledger. It provides tamper-proof, verifiable, and transparent audit trails,
enabling regulators and auditors to independently confirm the integrity
of critical operations such as financial transactions or system changes.
(^24) A Hardware Security Module (HSM) is a dedicated, tamper-resistant
hardware device designed to securely generate, store, and manage
cryptographic keys and perform sensitive operations such as signing,
encryption, and authentication.
rotated on a fixed schedule and on demand after any
control change.
8 .2 Zero-Knowledge Proof : GX integrates Zero-
Knowledge Proofs (ZKPs) within its compliance and
reserve-reporting architecture to balance transparency
with privacy. ZKPs allow wallets to demonstrate
compliance with sanctions or KYC requirements without
exposing personal data and enable GX to prove full
reserve coverage without revealing custodian account
details.
This aligns with supervisory research on CBDCs, where
ZKPs are recognized as tools to reconcile user privacy
with regulatory compliance. The underlying
cryptographic assurances are grounded in well-
established proofs and applied in modern confidential
transaction protocols such as Bulletproofs.
Privacy follows a data-minimization approach:
personally identifiable information remains off-chain,
while on-chain records carry only the metadata necessary
for settlement and compliance.
Figure 8 GX Security Tree Distribution
Key Management: HSMs provide secure key lifecycle management
(generation, storage, rotation, and destruction) in compliance with
international standards (e.g., FIPS 140-3).
Tamper Resistance: Physical and logical protections prevent extraction
or alteration of keys, even in the event of an attempted breach.
Assurance: HSMs enforce separation of duties and produce
cryptographic attestations, ensuring that critical operations (e.g.,
mint/burn, validator signatures) are provably authorized.

Confidential amounts and selective disclosure (“view-
keys”) enable commercial privacy for counterparties
while preserving full supervisory auditability. A
cryptography roadmap is maintained for trusted
execution environments and succinct zero-knowledge
proofs, with adoption paced

9. Experiment: Liquidity Risk and Buffers
8.1 Theoretical Framework and Methodological Approach
Approach : This section outlines a quantitative
experiment to assess the adequacy of the GX network's
liquidity buffers under both normal and stressed market
conditions.

GX methodology is grounded in financial risk

management principles, specifically the use of Value at
Risk (VaR) and Expected Shortfall (ES) to model
potential liquidity outflows. We interpret these metrics as
the minimum required cash reserves to cover a given
level of redemption risk over a specified time horizon

(H). The analysis uses a combination of two statistical
models for event arrival and severity:

i. Arrival Rate (λ): We model the arrival of
redemption requests as a Poisson or Hawkes
process. A Hawkes process is particularly relevant
for stress scenarios, as it captures the self-exciting
nature of financial crises where one event (a large
redemption) increases the probability of subsequent
events (a run). The stress multiplier of 1.6 on λ
formalizes this entrenchment of run dynamics.
ii. Severity Distribution : We model the size of
individual redemption requests (severities) using a
lognormal distribution for everyday conditions and
an Extreme Value Theory (EVT) mix for tail risk.
EVT, specifically the Generalized Pareto
Distribution (GPD), is a powerful tool for modeling
the behavior of extreme events that fall outside the
typical range of historical data.
iii. EVT: The EVT-mix alternative with a 5%
exceedance threshold (u) accounts for the
possibility of very large, but rare, redemption events
that would not be captured by a standard lognormal
distribution 25.
(^25) A standard lognormal distribution is a continuous probability
distribution of a random variable whose logarithm is normally
distributed. It is commonly used to model variables that are always

8.2 Core definitions and notation from GX Liquidity & Risk Methodology.
Liquidity & Risk Methodology.
Same-Day Liquid Capacity ( 𝐶! ): This is the total
liquidity available for same-day redemptions. It is
defined as the sum of the same-day cash headroom (𝐻! )
and the usable committed repo capacity, calculated after
applying a conservative haircut (h) to the repo-eligible
High-Quality Liquid Assets (ρ).
𝐶!=𝐻!+( 1 −ℎ)∗𝜌
Horizon-Specific Liquidity Coverage (GX-LCR(H)):
This metric, analogous to the Basel LCR, measures the
adequacy of liquid assets to cover expected net cash
outflows over a given time horizon (H). The numerator,
HQLA    4 , represents the total available high-quality liquid
assets.
The denominator, NCO (^) $, represents the Expected
Shortfall (ES) of redemptions over that horizon, which is
the average loss from a portfolio of extreme events. The
target is a ratio greater than or equal to 1 with a
supervisory buffer.

𝐺𝑋−𝐿𝐶𝑅(𝐻)=
𝐻!+( 1 −ℎ)∗𝜌
𝐸𝑆%[𝑅𝐷$]
Utilization ($\rho$)*: This is an operational metric that
indicates the stability of the system's service rate. It is the
ratio of the redemption arrival rate (λ) to the same-day
service rate μ=^56 !, where q is the average size of
redemption)+. For operational stability, this ratio must
remain below 1.
𝑝∗=
𝜆
𝜇
Arrival Calibration: The arrival of redemption requests
is modeled using a Poisson process for baseline
conditions. For stress scenarios, a Hawkes process is
employed to capture self-exciting or clustering behavior,
where an initial redemption event increases the
probability of subsequent redemptions, mimicking a
"run."
Severity Models and Tail Behavior : The size of
individual redemptions (severities) is modeled using a
lognormal distribution for common events. For extreme,
low-probability events, the model switches to an Extreme
Value Theory (EVT) framework, specifically the
positive and are skewed, meaning they have a long right tail. In finance,
it is a very common distribution for modeling asset prices, as they
cannot go below zero and their percentage changes tend to be
lognormally distributed.
Generalized Pareto Distribution (GPD), which is better
suited for modeling "tail behavior" beyond a certain
threshold (u).

Expected Shortfall (ES (^) %) is used as the primary risk
metric, as it accounts for the magnitude of extreme
losses, unlike Value at Risk (VaR)^26 , which only
measures the maximum loss at a given confidence level.
9 .3 Experimental Parameters : The following
parameters are used in our illustrative experiment.
Confidence Level (α): 99.5%
Normal Condition Parameters:

Redemption arrival rate (λ): 5,000 requests per
day.
Lognormal severity mean: $2,000.
Lognormal severity standard deviation: $3,000.
Stress Condition Parameters:

Hawkes stress multiplier: 1.6 on λ.
EVT-mix: 5% of events exceed a threshold (u)
of $10,000
GPD parameters ξ=0.4
β=$7,000.
Liquidity Buffers:

Repo capacity (ρ): $200M.
Haircut (h): 5%.
Usable repo capacity=( 1 −ℎ)∗𝑝A=190M
Time Horizons (H): 1 day and 5 days.

9 .4 Results and Analysis : The experiment calculates
the required cash floor (𝐻!∗) based on the formula:

𝐻!∗=𝑚𝑎𝑥( 0 ,𝐸𝑆−( 1 −ℎ)∗𝑝)
Where ES is the Expected Shortfall of redemptions over
the time horizon, and (1−h)⋅ρ is the usable repo capacity.

Table 2 Liquidity Risk Metrics

(^26) Value at Risk (VaR) is a widely used risk metric that estimates the
maximum potential loss of a portfolio or position over a specified time
The results of the experiment demonstrate the robustness
of the GX network's liquidity framework.
The highest calculated Expected Shortfall, under the
most severe stress conditions over a 5-day horizon, is
$51.64M. This value is significantly lower than the
$190M in usable repo capacity. This leads to two key
conclusions:
9 .4.1 Sufficient Liquidity Coverage : The calculated
GX-LCR(H) for all scenarios is well above the target of

For example, in the most stressed 5-day scenario, the
ratio is $89.;<=
$9>!=
≈ 3. 68. This shows that the network's
liquid assets are more than sufficient to meet extreme
redemption demands.
9 .4.2 Required Cash Floor : The core equation for the
required cash floor 𝐻!∗=𝑚𝑎𝑥( 0 ,𝐸𝑆%( 1 −ℎ)∗𝑝),
consistently yields a value of zero in our illustrations.
This mathematically confirms that the committed repo
capacity alone is sufficient to cover extreme shortfalls
without the need for additional same-day cash.
The paper notes that despite this, GX maintains a positive
𝐻!as a prudential and operational buffer to account for
real-world factors not captured in the model, such as
time-of-day frictions and unforeseen operational needs.
This reflects a conservative and responsible approach to
managing liquidity, going beyond a purely theoretical
minimum.
The real-time disclosure of metrics like GX-LCR(H) and
utilization (ρ∗) via the Scanner (LRS) ensures that market
participants and supervisors have constant, transparent
access to the network's liquidity status, mitigating the
informational opacity that has historically triggered
stablecoin runs.
10. Conclusions
The GX network presents a novel and robust framework
for sovereign stablecoins by directly addressing the
fundamental weaknesses of existing financial systems
and stablecoin arrangements. The conclusion reinforces
the core arguments of the paper and outlines the strategic
path for deployment.
9.1 Key Findings and Contributions :
From Assurances to Measurements: The paper's central
thesis is the transition from opaque, trust-based
horizon (H) at a given confidence level (α), under normal market
conditions.
assurances to continuous, real-time measurements. The
Scanner platform is the lynchpin of this approach,
providing a transparent, observable, and testable system
for crucial metrics like 1:1 reserve reconciliation,
liquidity coverage, and operational capacity. This moves
the system beyond mere attestations and into a verifiable,
data-driven framework.

A Hybrid and Pragmatic Model : GX is not a purely
decentralized system but rather a hybrid, a "sovereign,
programmable money" that is locally compliant while
remaining globally interoperable. It fuses established
financial principles, such as LCR/NSFR-informed
liquidity policy and Expected Shortfall-based tail-risk
calibration, with modern blockchain technology. This
pragmatic approach is designed to satisfy supervisory
requirements and regulatory standards.

Operational and Liquidity Resilience : The quantitative
experiment's results are a critical finding. They
demonstrate that the network's liquidity buffers,
composed of committed repo capacity, are more than
sufficient to cover even extreme redemption events. This
effectively means the theoretical cash floor required is
zero, showing the system's structural resilience without
the need for large, inefficient balance-sheet cash
reserves. This makes the model capital-efficient and
operationally sound.

Phased, Strategic Rollout: The deployment roadmap is
deliberately phased to align with regulatory approvals
and partner readiness. Starting with Asia-Pacific pilots
and extending to other regions, the network is designed
to be flexible and adaptable, adding corridor-specific FX
connectivity and deepening supervisory tooling with
automated stress tests and regulator dashboards in
subsequent phases. This phased approach mitigates risk
and ensures scalability.

In sum, the GX network offers a solution for sovereign
money in a digital age, a system that is secure, compliant,
capital-efficient, and globally interoperable, delivering
predictable costs and instant settlement for a wide range
of users while fundamentally enhancing financial
stability.