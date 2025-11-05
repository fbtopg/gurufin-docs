# 시작하기

Gurufin Chain 개발자 빠른 시작 가이드에 오신 것을 환영합니다. 이 페이지는 개발 환경 설정, Gurufin 테스트넷 연결 및 첫 번째 스마트 계약 배포에 대한 단계별 소개를 제공합니다. 국경 간 결제 솔루션, 스테이블코인 FX 거래 플랫폼 또는 상호 운용 가능한 DeFi 애플리케이션을 구축하든 이 가이드는 빠르고 효율적으로 시작하는 데 도움이 됩니다.

---

## 환경 설정

Gurufin Chain과 상호 작용하기 전에 로컬 개발 환경을 준비해야 합니다. Gurufin Chain은 Delegated Proof-of-Stake (DPoS)가 있는 Tendermint 클래스 Byzantine Fault Tolerant (BFT) 합의를 기반으로 구축되었으며 EVM Gateway 모듈을 통해 Ethereum Virtual Machine (EVM) 호환성을 지원합니다.

### 사전 요구 사항

- **Node.js** (v14 이상): JavaScript 기반 개발 도구 실행에 필요합니다.
- **Yarn** 또는 **npm**: 종속성 설치를 위한 패키지 관리자.
- **Gurufin Chain CLI**: 블록체인과 상호 작용하기 위한 명령줄 인터페이스.
- **Metamask** 또는 호환 Web3 지갑: 계정 관리 및 거래 서명용.
- **Solidity 컴파일러**: 스마트 계약 컴파일용.

### Gurufin Chain CLI 설치

Gurufin Chain CLI는 노드 운영, 블록체인 쿼리 및 계약 배포에 필수적입니다.

```bash
# Gurufin Chain 저장소 복제
git clone https://github.com/gurufin/gurufin-chain.git
cd gurufin-chain

# CLI 바이너리 빌드
make install

# 설치 확인
gurufincli version
```

CLI는 연결 구성, 키 관리 및 거래 제출 명령을 제공합니다.

### 지갑 설정

CLI를 사용하여 새 지갑을 생성하거나 기존 개인 키를 가져올 수 있습니다.

```bash
# 새 지갑 생성
gurufincli keys add mywallet

# 지갑 목록 표시
gurufincli keys list
```

니모닉을 안전하게 저장하십시오. 이 지갑을 사용하여 테스트넷에서 계약을 배포하고 거래에 서명합니다.

---

## 테스트넷에 연결

Gurufin 테스트넷은 개발자가 메인넷에 배포하기 전에 애플리케이션을 테스트할 수 있는 공개 테스트 환경을 제공합니다.

### 테스트넷 구성

```bash
# 테스트넷 엔드포인트 구성
gurufincli config chain-id gurufin-testnet-1
gurufincli config node https://testnet-rpc.gurufin.io:443
gurufincli config trust-node true
```

### 테스트 토큰 획득

Gurufin 테스트넷 포싯을 사용하여 무료 테스트 GXN 토큰을 받으십시오:

```bash
# 포싯에서 테스트 토큰 요청
curl -X POST https://faucet.gurufin.io/request \
  -H "Content-Type: application/json" \
  -d '{"address":"YOUR_WALLET_ADDRESS"}'
```

---

## 첫 번째 스마트 계약 배포

간단한 ERC-20 스타일 토큰 계약을 배포하여 Gurufin Chain을 시작해 보겠습니다.

### 1. 계약 작성

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyToken {
    string public name = "My Gurufin Token";
    string public symbol = "MGT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1000000 * 10**18;
    
    mapping(address => uint256) public balanceOf;
    
    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }
    
    function transfer(address to, uint256 amount) public returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
```

### 2. 계약 컴파일 및 배포

```bash
# Hardhat 사용
npx hardhat compile
npx hardhat run scripts/deploy.js --network gurufin-testnet

# 배포 주소 기록
# Contract deployed to: 0x...
```

---

## 다음 단계

- [Gurufin에 연결](02_connect_to_gurufin.md)에서 상호 운용성에 대해 자세히 알아보기
- FXSwap API를 탐색하여 스테이블코인 거래 통합
- GX Stablecoins로 국경 간 결제 애플리케이션 구축

Gurufin 생태계에 오신 것을 환영합니다! 🚀

