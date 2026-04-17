# Compliance & Regulation

GX stablecoins embed compliance directly into the consensus layer via the permissioned Proof-of-Authority model.

**KYC/AML & Wallet Tiers**
GX chains implement wallet-tier compliance. Users and institutions undergo identity verification before transacting. Different wallet tiers dictate transaction permissions, and all wallets are screened against global sanctions lists in real-time.

**FATF Travel Rule**
Transaction messages include encrypted originator and beneficiary details. Validators verify the presence of Travel Rule data before block inclusion, maintaining compliance even during cross-chain IBC transfers.

**Emergency Controls & Security**
* **Hardware Security:** Validator keys are secured in HSMs using multi-party computation (MPC quorum).
* **Circuit Breakers:** An Emergency Procedures Playbook defines supervised circuit breakers (e.g., rate limits, settlement pauses) activated under strict stress conditions with regulator involvement.

**Privacy Roadmap (Future Integration)**
GX plans to integrate Zero-Knowledge Proofs (ZKPs) to allow wallets to demonstrate KYC/sanctions compliance without exposing personal data. Selective-disclosure "view keys" will allow authorized supervisors to inspect provenance without broad data exposure.
