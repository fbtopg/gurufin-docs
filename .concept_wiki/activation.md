# Smart Contract Logic (Activation)

The "Smart Contract Logic (Activation)" module details the process by which institutional users gain full trading capabilities within the GuruDex ecosystem, specifically focusing on the critical **Activation** step. This module is a core component of the broader [Smart Contract Logic] that governs operations, ensuring controlled and permissioned access for institutional participants.

## What is Activation?

**Activation** is the third stage in the multi-step [Institutional Onboarding] workflow on GuruDex. Following successful [Registration] and off-chain [Verification], Activation involves an authorized operator configuring specific trading parameters for an institutional user. This step is crucial for customizing the trading environment to meet the institution's requirements and for enforcing platform policies.

## Key Concepts and Relationships

*   **Activation**: This is the central concept of this module. It refers to the final technical setup of an institutional account on-chain after off-chain verification. During activation, an operator defines key parameters that will govern the institution's interactions with the platform.

*   **Institutional Onboarding**: Activation is an integral part of this broader process. Without successful activation, an institutional user, despite having registered and been verified, cannot proceed to full [Authorization] and begin trading.

*   **Institutional Users**: Activation directly impacts these users. It enables their trading capabilities and customizes their experience based on defined limits, fees, and parameters.

*   **InstitutionalRegistry**: This contract plays a vital role in storing and managing institutional profiles and permissions. After activation, the parameters set during this step are likely recorded and managed within the `InstitutionalRegistry` to enable the platform's contracts, such as the [OPRSProcessor], to properly route and execute trades for these users.

*   **Smart Contract Logic**: Activation is a specific implementation detail within the overall `Smart Contract Logic` of GuruDex. It demonstrates how different contracts, like the `InstitutionalRegistry` and potentially the `OPRSProcessor`, work together to manage user access and trading parameters.

## Activation in the Onboarding Flow

As per the source excerpts, the institutional onboarding process flows sequentially:

1.  **Registration**: Initial submission of basic information via `registerInstitution()`.
2.  **Verification**: Off-chain KYC/AML review by an operations team.
3.  **Activation**: An operator configures custom limits, fees, and other parameters for the institution. This is where the specific trading rules for the institution are set up on-chain.
4.  **Authorization**: The institution approves specific coins and pools they wish to access, giving them the final green light to trade.

## Important Details

*   Activation is performed by an "Operator," implying a privileged role responsible for managing institutional access.
*   The parameters set during activation, such as custom limits, fees, and other user-specific configurations, are fundamental to defining the operational scope for institutional users. These parameters differentiate institutional trading experiences from those of [Retail Users].
*   While not explicitly stated for activation, the **OPRSProcessor** relies on the **InstitutionalRegistry** to determine user type and route swaps accordingly (to the institutional OPRS path with oracle-verified pricing and custom parameters). This implies that the parameters set during activation are crucial for the `OPRSProcessor` to function correctly for institutional trades.