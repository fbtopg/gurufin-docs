# Compliance & Regulation

GX stablecoins are designed for regulated payment and settlement environments. Compliance controls are enforced through the permissioned Proof-of-Authority validator set, counterparty onboarding, transaction screening, and jurisdiction-specific operating rules.

**KYC/AML & Compliance Tiers**

GX chains use compliance-tier access control. Counterparties complete identity verification before transacting, and their tier determines available transaction permissions, limits, and supported workflows. Accounts and counterparties are screened against applicable sanctions and risk lists during onboarding and transaction processing.

**FATF Travel Rule**

Where required, transaction messages include encrypted originator and beneficiary information. Validators verify that required Travel Rule fields are present before block inclusion, including for supported cross-chain IBC transfers.

**Emergency Controls & Security**

* **Hardware security:** Validator keys should be protected with HSMs, MPC quorum controls, or equivalent institutional custody practices.
* **Circuit breakers:** The Emergency Procedures Playbook defines supervised controls, such as rate limits or settlement pauses, that may be activated under predefined stress conditions with appropriate oversight.

**Privacy Roadmap (Future Integration)**

GX plans to integrate zero-knowledge proof tooling so accounts can prove selected compliance attributes, such as KYC completion or sanctions clearance, without exposing unnecessary personal data. Selective-disclosure view keys are expected to support authorized supervisory review while limiting broad data exposure.
