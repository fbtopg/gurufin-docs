# 🇰🇷 한국어

Gurufin Chain은 기관급 기능과 탈중앙화 금융(DeFi)의 효율성을 결합하여 은행, 자산 관리자 및 금융 기관을 위한 규제 준수 환경을 제공합니다. 이 페이지는 Gurufin 생태계 내에서 기관 DeFi 애플리케이션을 가능하게 하는 주요 기능 및 사용 사례를 탐색합니다.

***

## 기관 참여자를 위한 규제 준수 DeFi

Gurufin Chain의 아키텍처는 처음부터 기관 요구 사항을 고려하여 설계되었습니다:

### 주요 기관 기능

* **KYC/AML 통합:** 온체인 및 오프체인 규정 준수 확인이 있는 지갑 계층 규정 준수
* **InstitutionalRegistry:** 기관 온보딩, 권한 및 위험 매개변수를 관리하는 전용 스마트 계약
* **맞춤형 거래 한도:** 거래당 및 일일 거래량 한도를 가진 구성 가능한 위험 매개변수
* **오라클 기반 가격 책정:** 대규모 거래를 위한 최소 슬리피지를 가진 검증된 실시간 FX 비율
* **개인 정보 보호 옵션:** 선택적 zk 증명 모드로 기밀 거래 가능
* **감사 가능성:** 규제 기관을 위한 감독급 관찰 가능성 및 보고

***

## 기관 사용 사례

### 1. 기관 FX 정산

은행 및 금융 기관은 Gurufin을 사용하여 국경 간 FX 거래를 정산할 수 있습니다:

```javascript
const settlement = await gurufin.institutional.settleFX({
  from: 'USGX',
  to: 'JPGX',
  amount: '10000000',
  counterparty: 'institution2',
  settlementDate: '2025-11-05'
});
```

**이점:**

* 원자적 PvP 정산
* 원금 위험 제거
* T+0 정산
* 규제 보고 자동화

### 2. 유동성 제공

기관은 FXSwap 하이브리드 풀에 유동성을 제공하여 보상을 받을 수 있습니다:

```javascript
const liquidity = await fxswap.institutional.addLiquidity({
  pool: 'USGX-KRGX',
  baseAmount: '5000000',
  quoteAmount: '6750000000',
  institution: '0x...'
});
```

**이점:**

* 스왑 수수료에서 보상
* 깊은 유동성 풀
* 위험 관리 도구
* 투명한 보상 분배

### 3. 토큰화된 자산

기관은 Gurufin에서 부동산, 채권 또는 상품과 같은 자산을 토큰화할 수 있습니다:

**이점:**

* 규제 준수 토큰 발행
* 24/7 거래
* 분할 소유권
* 자동화된 규정 준수 확인

***

## InstitutionalRegistry

기관은 플랫폼에 액세스하기 전에 InstitutionalRegistry를 통해 등록해야 합니다:

### 온보딩 프로세스:

1. **초기 등록:** 기관이 등록을 제출합니다
2. **KYC/AML 확인:** 오프체인 검증이 수행됩니다
3. **활성화:** 승인 시 기관이 활성화됩니다
4. **권한 부여:** 특정 풀 및 기능에 대한 액세스가 부여됩니다

```javascript
const registration = await registry.registerInstitution({
  name: 'Global Bank Corp',
  jurisdiction: 'US',
  kycProvider: 'verified-kyc.io',
  limits: {
    perTx: '10000000',
    daily: '100000000'
  }
});
```

***

## 규정 준수 기능

* **Travel Rule 준수:** 국경 간 거래를 위한 FATF Travel Rule 메타데이터
* **제재 스크리닝:** 실시간 제재 목록 확인
* **거래 모니터링:** 의심스러운 활동을 위한 자동 모니터링
* **감사 추적:** 모든 기관 활동의 완전한 온체인 기록

***

Gurufin의 기관 DeFi 기능을 통해 금융 기관은 규제 준수를 유지하면서 블록체인 기술의 효율성과 투명성을 활용할 수 있습니다.
