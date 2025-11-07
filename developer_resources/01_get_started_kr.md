# 시작하기

Gurufin Chain 개발자 빠른 시작 가이드에 오신 것을 환영합니다. 이 페이지는 개발 환경 설정, Gurufin 테스트넷 연결 및 첫 번째 스마트 계약 배포에 대한 단계별 소개를 제공합니다. 국경 간 결제 솔루션, 스테이블코인 FX 거래 플랫폼 또는 상호 운용 가능한 DeFi 애플리케이션을 구축하든 이 가이드는 빠르고 효율적으로 시작하는 데 도움이 됩니다.

---

## 환경 설정

Gurufin Chain과 상호 작용하기 전에 로컬 개발 환경을 준비해야 합니다. Gurufin Chain은 Delegated Proof-of-Stake (DPoS)가 있는 Tendermint 클래스 Byzantine Fault Tolerant (BFT) 합의를 기반으로 구축되었으며 EVM Gateway 모듈을 통해 Ethereum Virtual Machine (EVM) 호환성을 지원합니다. 이를 통해 Ethereum 도구에 익숙한 개발자는 Hardhat 또는 Truffle과 같은 기존 프레임워크를 활용할 수 있습니다.

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

Gurufin Chain은 빠른 블록 시간(1초 미만), 결정적 최종성 및 IBC 상호 운용성을 포함한 메인넷 기능을 미러링하는 공개 테스트넷 환경을 운영합니다.

### 테스트넷용 CLI 구성

테스트넷에 연결하려면 테스트넷 RPC 엔드포인트 및 체인 ID로 CLI를 구성하십시오.

```bash
gurufincli config chain-id gurufin-testnet-1
gurufincli config node https://rpc.testnet.gurufin.io:26657
```

최신 블록을 쿼리하여 연결을 확인하십시오:

```bash
gurufincli status
```

현재 블록 높이 및 네트워크 상태에 대한 정보가 표시되어야 합니다.

### 테스트넷 토큰 획득

테스트넷 토큰은 거래 및 계약 배포에 대한 가스 수수료를 지불하는 데 필요합니다. 공식 Gurufin 포싯에서 테스트 토큰을 요청하십시오:

- 포싯 URL: [https://faucet.testnet.gurufin.io](https://faucet.testnet.gurufin.io)

지갑 주소를 제공하고 거래 비용을 충당할 테스트 USGX 스테이블코인을 받으십시오.

---

## 첫 번째 스마트 계약 배포

Gurufin Chain은 EVM 호환 스마트 계약을 지원하므로 Solidity로 계약을 작성하고 익숙한 도구를 사용하여 배포할 수 있습니다.

### 1단계: 간단한 Solidity 계약 작성

다음 코드로 `SimpleStorage.sol` 파일을 생성하십시오:

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

이 계약은 단일 부호 없는 정수를 저장하고 검색할 수 있습니다.

### 2단계: 계약 컴파일

Hardhat 또는 Remix IDE를 사용하여 계약을 컴파일하십시오. Hardhat의 경우 프로젝트를 초기화하고 컴파일하십시오:

```bash
npm init -y
npm install --save-dev hardhat @nomiclabs/hardhat-ethers ethers

npx hardhat compile
```

Solidity 컴파일러 버전이 계약 pragma(`^0.8.0`)와 일치하는지 확인하십시오.

### 3단계: 배포 스크립트 구성

Hardhat 프로젝트에 배포 스크립트 `deploy.js`를 생성하십시오:

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

### 4단계: 네트워크 설정 구성

Gurufin 테스트넷 네트워크 구성을 Hardhat 구성(`hardhat.config.js`)에 추가하십시오:

```javascript
require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: "0.8.0",
  networks: {
    gurufinTestnet: {
      url: "https://evm.testnet.gurufin.io", // EVM Gateway RPC 엔드포인트
      chainId: 12345, // 실제 테스트넷 체인 ID로 교체
      accounts: ["0xYOUR_PRIVATE_KEY"] // 지갑 개인 키로 교체
    }
  }
};
```

### 5단계: 계약 배포

Gurufin 테스트넷을 대상으로 배포 스크립트를 실행하십시오:

```bash
npx hardhat run scripts/deploy.js --network gurufinTestnet
```

성공하면 콘솔에 배포된 계약 주소가 표시됩니다.

### 6단계: 계약과 상호 작용

ethers.js 또는 Web3.js를 사용하여 배포된 계약과 상호 작용할 수 있습니다. 예를 들어 저장된 데이터를 설정하고 가져오려면:

```javascript
const simpleStorage = await ethers.getContractAt("SimpleStorage", "DEPLOYED_CONTRACT_ADDRESS");

// 값 저장
await simpleStorage.set(42);

// 값 검색
const value = await simpleStorage.get();
console.log("Stored value:", value.toString());
```

---

## 요약 표: 주요 명령 및 엔드포인트

| 작업 | 명령 / 엔드포인트 | 참고 사항 |
|---------------------------|---------------------------------------------------|----------------------------------------|
| CLI 설치 | 복제된 리포지토리에서 `make install` | Go 및 Make 필요 |
| 지갑 생성 | `gurufincli keys add mywallet` | 니모닉을 안전하게 저장 |
| 테스트넷용 CLI 구성 | `gurufincli config chain-id gurufin-testnet-1` | 테스트넷 체인 ID 설정 |
|  | `gurufincli config node https://rpc.testnet.gurufin.io:26657` | 테스트넷 RPC 엔드포인트 설정 |
| 네트워크 상태 확인 | `gurufincli status` | 연결 확인 |
| 테스트 토큰 요청 | [https://faucet.testnet.gurufin.io](https://faucet.testnet.gurufin.io) | 가스 수수료용 |
| Solidity 계약 컴파일 | `npx hardhat compile` | Hardhat 또는 Remix 사용 |
| 계약 배포 | `npx hardhat run scripts/deploy.js --network gurufinTestnet` | EVM Gateway를 통해 배포 |
| 계약과 상호 작용 | ethers.js/Web3.js 계약 호출 | 배포된 계약 주소 사용 |

---

## 다음 단계

첫 번째 계약을 배포한 후 다음과 같은 Gurufin Chain의 고급 기능을 탐색하십시오:

- **IBC 상호 운용성**: 원자적 크로스체인 정산을 활성화합니다.
- **하이브리드 실행 패브릭**: FX 및 DeFi 애플리케이션을 위한 AMM 및 RFQ 메커니즘을 활용합니다.
- **오라클 네트워크 통합**: 동적 수수료 균형을 위한 실시간 가격 피드에 액세스합니다.
- **개인 정보 보호 모드**: zkGuru로 zk-proof 개인 정보 보호를 구현합니다.
- **규정 준수 레이어**: 규제 환경을 위한 지갑 계층 KYC/AML 기능을 활용합니다.

자세한 API 참조, SDK 및 고급 튜토리얼은 [개발자 리소스](../developer-resources) 섹션을 방문하십시오.

---

이 가이드를 따르면 Web3 경제를 위해 맞춤화된 Gurufin Chain의 고성능, 상호 운용 가능하며 규정 준수가 준비된 블록체인 플랫폼에서 구축하기 위한 첫 번째 단계를 밟은 것입니다. 즐거운 코딩하세요!
