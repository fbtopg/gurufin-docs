# Gurufin GitBook QnA — 문서 정확성 검토용

이 문서는 Gurufin GitBook의 정보 정확성을 팀이 빠르게 검토하기 위해 작성되었습니다. 각 질문은 실제 GitBook 문서 내용을 기반으로 하며, 운영/기술적 핵심 사항을 다룹니다.

---

## 1. 비전 및 아키텍처

### Q1. Gurufin의 비전과 미션은 무엇인가?

**A.** Gurufin은 글로벌 금융의 근본적인 비효율성, 즉 송금이 느리고 비싸며 접근하기 어렵다는 문제를 해결합니다.
- **비전:** 가치(자산)가 정보처럼 자유롭게 그리고 즉시 이동하는 세계. 서브초(finality) 최종성, 예측 가능한 파동 기반 수수료, 개방적 접근을 갖춘 중립적 FX/DeFi 허브를 구축합니다.
- **미션:** 스테이블코인 기반 외환 및 크로스보더 결제를 위한 최종 인프라 레이어를 제공하여, 개발자와 기관이 차세대 금융 서비스를 구축할 수 있도록 합니다.

---

### Q2. Gurufin의 시스템 아키텍처는 어떻게 구성되어 있는가?

**A.** Gurufin은 두 개의 상호 연결된 기둥으로 구성됩니다.

1. **Gurufin Chain** — 퍼블릭, 권한 없는(Layer-1) DPoS 블록체인. 서브초 최종성, 최대 10,000 TPS. IBC 퍼스트 아키텍처와 EVM 게이트웨이(Ethereum 호환성)를 제공합니다.
2. **GX Stablecoin Network** — 주권 스테이블코인 체인들의 네트워크. 관할권별 Proof-of-Authority(PoA) 컨센서스로 동작하며, 24/7 증명된 1:1 준비금으로 완전 담보됩니다.

**시스템 흐름:** GX 스테이블코인은 라이선스된 은행 API를 통해 머징되고, IBC로 Gurufin Chain으로 유입되어 트레이딩 및 DeFi 활동에 사용되며, 필요시 언제든지 법정화폐로 리디미션 가능합니다.

---

## 2. Gurufin Chain

### Q3. Gurufin Chain의 기술 스택과 컨센서스 메커니즘은 무엇인가?

**A.** Gurufin Chain은 Cosmos SDK와 CometBFT 위에 구축된 퍼블릭 DPoS Layer-1 블록체인입니다.
- **컨센서스:** Tendermint BFT + DPoS. Validator들이 GXN을 스테이킹하여 블록 생성에 참여하고, 토큰 홀더들은 신뢰하는 Validator에 토큰을 위임합니다.
- **최종성:** 단일 체인 ~500ms의 결정적(final) 최종성.
- **크로스체인 IBC:** 5~30초의 엔드투엔드 최종성 (패킷 릴레이 및 체인 페어에 따라 다름).
- **처리량:** 최적 조건에서 최대 10,000 TPS.

---

### Q4. Gurufin Chain의 노드 유형과 역할은 무엇인가?

**A.**

| 노드 유형 | 역할 |
|-----------|------|
| Validator Node | 컨센서스 참여 및 블록 생성. 스테이킹된 GXN 필요. |
| Full Node | 전체 블록체인 역사 저장 및 트랜잭션 릴레이. |
| Archive Node | 복잡한 쿼리를 위해 모든 역사적 상태 보존. |
| Light Client | 전체 체인 데이터 다운로드 없이 암호학적으로 트랜잭션 검증. |

---

### Q5. Guru-PEG(Gas Price Equilibrium Governance)는 어떻게 동작하는가?

**A.** Guru-PEG는 GXN 토큰의 변동성에서 사용자 거래 비용을 분리하는 가스 가격 메커니즘입니다. Typical transfer 비용이 약 $0.013로 예측 가능하고 안정적으로 유지됩니다.

**핵심 공식:**
```
min_gas_price_GXN = target_gas_fee_USD / current_GXN_price_USD
```

**동작 원리:**
1. **Oracle 피드:** 분산 오라클 네트워크가 GXN/USD 실시간 가격을 수집합니다.
2. **집계:** 이상치 필터링을 통해 중앙값 또는 결재 기반 방식으로 가격 결정.
3. **동적 조정:** GXN 가격이 오르면 필요한 GXN량이 줄고, 내리면 GXN량이 늘어납니다. 사용자-facing 파동 비용은 일정합니다.
4. **안전장치:** Oracle Quorum, Outlier Filtering, Price Deviation Checks, Gas Fee Floor/Ceiling, Peg Buffer, Emergency Fallback.

---

### Q6. Gurufin Chain의 Governance 구조와 파라미터는 무엇인가?

**A.**

| 파라미터 | 값 |
|----------|------|
| Voting Period | 14일 |
| Quorum Requirement | 33.4% (전체 스테이킹 투표권의 33.4% 이상) |
| Timelock | Phase 1 — 없음 (즉시 실행) |

**Proposal Types:**
- Parameter Change: 네트워크 파라미터 조정
- Software Upgrade: 네트워크 버전 업그레이드 (supermajority >66%)
- Treasury Allocation: Ecosystem/Governance reserve 자금 지출 (supermajority >66%)
- Text Proposal: 비바인딩 커뮤니티 감정 측정

---

## 3. GX Stablecoin Network

### Q7. GX Stablecoin Network는 어떻게 구성되어 있는가?

**A.** 각 법정화폐(GXUSD, GXKRW, GXEUR, etc.)마다 전용 PoA Layer-1 체인이 존재합니다.
- 각 체인은 관할권별 라이선스된 Validator들이 PoA 컨센서스로 운영.
- 1:1 법정화폐 준비금으로 완전 담보.
- Live Proof-of-Reserves (24/7 실시간 준비금 스캐너) 제공.
- Gurufin Chain과의 IBC 상호운용성 지원.

---

### Q8. GX 스테이블코인의 Reserve 구성은 어떤가?

**A.**
- **출시 시점:** 100% 현금 (라이선스된 Custodian Bank에 보유).
- **점진적 diversification:** 규제 허용 시 ultra-short Treasury bills (3개월 미만 maturity)로 부분 분산.
- **유동성 백업:** 2차 시장 매도가 아닌 Pre-arranged Repo Facilities로 유동성 확보.
- **Liquidity Standards:** Basel 기준의 LCR(Liquidity Coverage Ratio)과 NSFR(Net Stable Funding Ratio) 적용.

**GX-LCR 공식:**
```
GX-LCR(H) = (H0 + (1-h) * ρ) / ES_α[R_D^H]
```
- H0 = 당좌 현금
- ρ = repo capacity
- h = haircut
- ES = Expected Shortfall
- 목표: GX-LCR(H) >= 1

---

### Q9. GX 스테이블코인의 Mint & Burn 프로세스는 어떻게 동작하는가?

**A.**

**Minting:**
1. 사용자가 은행 계좌에 법정화폐 입금.
2. Bank API가 입금 이벤트를 GX Chain Gateway Module로 알림.
3. Licensed Validator들이 입금 인증, 규정 준수, 준비금 충분성 검증.
4. Idempotency 체크 (중복 처리 방지).
5. Quorum 승인 후 On-Chain 머징.
6. 서브초 최종성.

**Burning:**
1. 사용자가 GX Chain Gateway로 Burn 요청.
2. Validator들이 규정 준수, 준비금 충분성, 사용자 권한 검증.
3. Stablecoin On-Chain에서 Burn.
4. Bank API가 법정화폐를 사용자 계좌로 이체.

**Key Safeguards:** Idempotency, Quorum Authorization, Deterministic Finality, Live Reserve Scanner (LRS).

---

### Q10. Multi-Currency FX Settlement과 PvP는 어떻게 동작하는가?

**A.**
- **PvP Settlement:** IBC/HTLC를 통해 Escrowed Hold로 양측이 동시에 거래. Herstatt 리스크(한쪽만 결제되는 리스크) 제거.
- **FX Liquidity Pools:** Gurufin Chain에서 OPRS를 통해 교환. Stable-swap Curves로 Slippage 최소화. Large tickets는 TWAP/TWAMM 방식으로 시간 분산.
- **Onboarding:** 신규 통화 추가 시 Regulatory Assessment → Validator Recruitment → Banking Integration → Technical Deployment.

---

## 4. Compliance & Security

### Q11. GX Chains의 KYC/AML 및 Compliance 구조는 어떻게 되어 있는가?

**A.**
- **Wallet-tier Compliance:** 사용자/기관이 KYC 인증 후 Wallet Tier에 따라 거래 권한 부여.
- **Sanctions Screening:** 모든 Wallet이 실시간 글로벌 Sanctions List로 스크리닝.
- **FATF Travel Rule:** 트랜잭션 메시지에 암호화된 Originator/Beneficiary 정보 포함. Validator가 Travel Rule 데이터 존재 확인 후 Block Include.

---

### Q12. GX Chains의 Security 구조는 어떤가?

**A.**
- **HSM (Hardware Security Module):** Validator 키는 Multi-Party Computation(MPC)로 HSM에 보호.
- **Circuit Breakers:** Emergency Procedures Playbook에 정의된 Rate Limits, Settlement Pauses 등. Regulator 개입 하에 Activation.
- **Privacy Roadmap (Future):** ZKP(Zero-Knowledge Proofs)를 통한 KYC/Sanctions 상태 증빙 (개인 데이터 노출 없이).

---

## 5. Use Cases

### Q13. Gurufin의 Cross-Border Payments는 어떤 이점을 제공하는가?

**A.**

| 이점 | 설명 |
|------|------|
| Cost-Efficiency | GXN-PEG로 파동 기반 예측 가능한 수수료 (~$0.013/tx) |
| Atomic PvP | IBC로 Principal 리스크 및 Bridge 리스크 제거 |
| Minimal Slippage FX | OPRS로 Oracle-guided 시장 가격 기반. Typical <0.05% slippage |
| Embedded Compliance | Wallet-tier KYC/AML, Sanctions Screening, FATF Travel Rule |

**Use Cases:** Retail Remittance (이민자 송금), B2B Cross-Border Payments (기업 간 결제), Multinational Treasury Management (다국적 현금 관리).

---

### Q14. OPRS(Oracle Priced Reserve Swap)의 이점은 무엇인가?

**A.** 전통 AMM 기반 DEX와 달리:
- **Slippage 최소화:** Oracle-guided 시장 가격 기반. Stable-swap Curves로 추가 개선.
- **Inventory Buffer Rebalancing:** 비정상적 한쪽 플로우 시 3단계 리밸런싱 (Dynamic Fee Adjustment → Cross-Chain Arbitrage → Banking API Top-Up).
- **Oracle Latency:** Typical <2s. Extreme volatility 시 Slippage 증가 가능.

---

### Q15. Institutional DeFi에서 Gurufin Chain의 주요 가치 제안은 무엇인가?

**A.**

| 가치 | 설명 |
|------|------|
| Tokenized Asset Settlement | 서브초 결정적 On-Chain 최종성 (single chain). Cross-chain은 5-30초. |
| Collateral & Treasury Management | OPRS로 Large-volume rebalancing이 negligible slippage로 실행. |
| Supervisory Observability & Privacy | zkGuru Selective Disclosure로 Compliant 상태만 증명 (거래 내용 노출 없이). |

---

## 6. Developer Resources

### Q16. Season 2 Testnet의 네트워크 아키텍처는 어떻게 구성되어 있는가?

**A.**

| Chain | Display Name | Chain ID | EVM Chain ID | Native Denom | Prefix |
|---|---|---|---|---|---|
| GXN | GXN | guru_631-1 | 631 | agxn | guru |
| GXUSD | tGXUSD | gxusd_531-1 | 531 | atgxusd | gxusd |
| GXKRW | tGXKRW | gxkrw_431-1 | 431 | atgxkrw | gxkrw |
| GXIDR | tGXIDR | gxidr_1331-1 | 1331 | atgxidr | gxidr |
| GXEUR | tGXEUR | gxeur_931-1 | 931 | atgxeur | gxeur |
| GXPHP | tGXPHP | gxphp_731-1 | 731 | atgxphp | gxphp |
| GXJPY | tGXJPY | gxjpy_231-1 | 231 | atgxjpy | gxjpy |

**GXN Hub Endpoints:**
- **RPC:** https://trpc.gurufin.io
- **WebSocket:** wss://trpc.gurufin.io/websocket
- **Block Explorer:** https://tscan.gurufin.io/

**API Ports:** gRPC(9090), REST(9091), CometBFT(26657), Ethereum JSON-RPC(8545), WebSocket(8546).

---

### Q17. Testnet Endpoints의 Lifecycle Policy는 무엇인가?

**A.**
- Endpoints는 rotation, upgrade, decommissioning의 대상이 될 수 있습니다.
- **권장:** Hardcoding 금지, Parameterize URLs.
- **Migration Path:** Mainnet은 동일한 hostname 구조로 전환 (30일 전 공식 채널 발표).
- **Status Page:** Real-time endpoint health는 status.gurufin.io에서 확인.

---

## 7. Tokenomics ($GXN)

### Q18. $GXN 토큰의 할당 구조는 어떻게 되어 있는가?

**A.**

| 카테고리 | 할당량 | 비율 |
|----------|--------|------|
| Ecosystem Funds | 27,000,000,000 | 27.00% |
| Node Pool | 25,000,000,000 | 25.00% |
| Team & Developers | 19,500,000,000 | 19.50% |
| Strategic Investment | 12,500,000,000 | 12.50% |
| Early Ecosystem Investment | 3,000,000,000 | 3.00% |
| Network Operations | 3,000,000,000 | 3.00% |
| Reserve | 3,000,000,000 | 3.00% |
| Gurufin Foundation | 5,000,000,000 | 5.00% |
| Advisors | 2,000,000,000 | 2.00% |

**Total Supply (Genesis):** 100,000,000,000 GXN

---

### Q19. $GXN의 주요 용도는 무엇인가?

**A.**

| 용도 | 설명 |
|------|------|
| Staking | DPoS 네트워크 보안 (Validator 위임) |
| Governance | Protocol 업그레이드, Treasury 할당 투표 |
| Fee Payment | Network transaction 수수료 (GXN-PEG 기반) |
| Liquidity | Guruswap OPRS 거래 인프라 |

---

### Q20. GXN의 Burn Mechanism은 어떻게 동작하는가?

**A.**
- **Gurufin Abyss Ledger (GAL):** Keyless on-chain burn address. Private key는 수학적으로 도출 가능하지만 계산상 비현실적으로 복원 불가.
- **동작:** Governance가 설정한 비율의 수수료가 매 TX마다 자동으로 GAL로 라우팅. 영구 소각.
- **Deflationary Pressure:** 네트워크 사용량 증가 → 더 많은 GXN 소각 → 공급 감소.
- **Burn Rate:** Governance가 동적으로 조정. High Node Pool emissions 시 Burn Rate 증가 가능.

---

## 8. Validator Guide

### Q21. Validator의 Operational Requirements는 무엇인가?

**A.**
- **Hardware:** Enterprise-grade servers + Sentry Node Architecture (DDoS 완화).
- **Security:** HSM 또는 Multi-Party Computation(MPC)로 Key Material 보호. Strict rotation policy.
- **Stake:** 최소 GXN Bond (Governance로 설정).

---

### Q22. Slashing 및 Penalties는 어떤가?

**A.**

| 위반 유형 | 페널티 |
|-----------|--------|
| Downtime (블록 서명 실패) | Partial stake slash + temporary jailing |
| Double-Signing (동일 높이에서 conflicting block) | Severe stake slash + permanent tombstoning |

---

### Q23. Validator의 수익 구조는 무엇인가?

**A.**

| 수익원 | 설명 |
|--------|------|
| Node Pool Emissions | 25% Node Pool 할당에서 고정 블록 리워드 (Validator + Delegator 분배) |
| Transaction Fees | ~$0.01/tx. High-frequency enterprise workflows로 consistent base revenue |
| Institutional SLAs | Premium uptime guarantees / compliance reporting (추가 수수료 기반 서비스) |

---

## 9. Roadmap

### Q24. Gurufin의 개발 로드맵은 어떻게 구성되어 있는가?

**A.**

| Phase | 상태 | 주요 Milestone |
|-------|------|----------------|
| Phase 1: Foundation | 완료 | Core infrastructure, Live Reserve Scanner, Mint/Burn, GXN-PEG, Sherlock Audit 완료 |
| Phase 2: Expansion | 진행 중 | Public Testnet, OPRS, Sovereign PoC, IBC connectivity, EVM Gateway, Price Oracle, Ecosystem Fund |
| Phase 3: Scale | 계획 | Mainnet launch, Sovereign stablecoins 확장, Multi-leg PvP settlement, Layer-2 scaling, Quadratic voting |
| Phase 4: Global | 미래 | Sovereign bridge, Traditional finance partnerships, Full community governance. Target: 100M users, 50 sovereign stablecoins |

---

### Q25. Phase 1 Audit의 현재 상태는?

**A.** Sherlock에 의한 독립 보안 Audit이 완료되었습니다. Full Report는 Mainnet Launch 시점과 함께 게시될 예정입니다.

---

*문서 버전: v1.0 | 생성일: 2024-06-04*
*이 문서는 Gurufin GitBook의 내용 정확성을 검토하기 위해 생성되었습니다.*
*모든 Q&A는 실제 GitBook 문서 내용을 기반으로 작성되었습니다.*
