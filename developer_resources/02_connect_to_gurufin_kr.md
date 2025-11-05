# Gurufin에 연결

이 가이드는 다양한 프로토콜 및 인터페이스를 사용하여 애플리케이션을 Gurufin Chain에 연결하는 방법을 설명합니다. IBC, EVM Gateway, GatewayGX 및 REST API를 통한 상호 운용성에 중점을 둡니다.

---

## RPC 및 API 엔드포인트

Gurufin Chain은 개발자가 블록체인과 상호 작용할 수 있는 여러 엔드포인트를 제공합니다:

### 메인넷 엔드포인트

```
RPC: https://rpc.gurufin.io
REST: https://api.gurufin.io
gRPC: grpc.gurufin.io:9090
WebSocket: wss://ws.gurufin.io
```

### 테스트넷 엔드포인트

```
RPC: https://testnet-rpc.gurufin.io
REST: https://testnet-api.gurufin.io
gRPC: testnet-grpc.gurufin.io:9090
```

---

## Web3 지갑 연결

Metamask 또는 기타 Web3 지갑을 Gurufin의 EVM Gateway에 연결:

```javascript
const chainConfig = {
  chainId: '0x47F',  // 1151 10진수
  chainName: 'Gurufin Chain',
  nativeCurrency: {
    name: 'GXN',
    symbol: 'GXN',
    decimals: 18
  },
  rpcUrls: ['https://evm.gurufin.io'],
  blockExplorerUrls: ['https://explorer.gurufin.io']
};

await window.ethereum.request({
  method: 'wallet_addEthereumChain',
  params: [chainConfig]
});
```

---

## IBC를 통한 상호 운용성

Cosmos IBC를 사용하여 다른 체인에 연결:

```bash
# IBC 채널 생성
gurufincli tx ibc channel open-init \
  --channel-id channel-0 \
  --counterparty-channel-id channel-1 \
  --counterparty-port transfer \
  --port transfer

# IBC 전송 실행
gurufincli tx ibc-transfer transfer \
  transfer channel-0 \
  cosmos1recipient... 1000uatom \
  --from mywallet
```

---

## REST API 사용

```javascript
// 계정 잔액 쿼리
const response = await fetch(
  'https://api.gurufin.io/cosmos/bank/v1beta1/balances/gurufin1...'
);
const data = await response.json();
console.log(data.balances);

// 거래 쿼리
const tx = await fetch(
  'https://api.gurufin.io/cosmos/tx/v1beta1/txs/TXHASH'
);
```

---

## GatewayGX를 통한 Solana 통합

Solana와 상호 작용:

```typescript
import { Connection, PublicKey } from '@solana/web3.js';
import { GurufinBridge } from '@gurufin/bridge-sdk';

const bridge = new GurufinBridge({
  gurufin: 'https://rpc.gurufin.io',
  solana: 'https://api.mainnet-beta.solana.com'
});

// Gurufin에서 Solana로 자산 전송
await bridge.transferToSolana({
  from: 'gurufin1...',
  to: new PublicKey('Sol...'),
  amount: '1000',
  asset: 'USGX'
});
```

---

## 스마트 계약 상호 작용

Ethers.js를 사용하여 배포된 계약과 상호 작용:

```javascript
const ethers = require('ethers');

const provider = new ethers.providers.JsonRpcProvider(
  'https://evm.gurufin.io'
);

const contract = new ethers.Contract(
  contractAddress,
  contractABI,
  provider
);

// 계약 호출
const balance = await contract.balanceOf(userAddress);
console.log('Balance:', balance.toString());
```

---

## FXSwap API 통합

FXSwap 유동성 풀과 상호 작용:

```javascript
const { GurufinSDK } = require('@gurufin/sdk');

const sdk = new GurufinSDK({
  rpcUrl: 'https://rpc.gurufin.io',
  privateKey: process.env.PRIVATE_KEY
});

// 스왑 실행
const swap = await sdk.fxswap.swap({
  from: 'USGX',
  to: 'KRGX',
  amount: '1000',
  minOutput: '1350000',
  slippage: 0.5
});

console.log('Swap completed:', swap.txHash);
```

---

이 통합 가이드를 통해 Gurufin Chain의 모든 주요 기능 및 상호 운용성 레이어에 연결할 수 있습니다.

