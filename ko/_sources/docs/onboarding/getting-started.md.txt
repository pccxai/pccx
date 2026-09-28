---
orphan: true
---

# 기여 시작

{doc}`../quickstart`에서 관심 있는 저장소와 테스트벤치를 골라보세요.
RTL이나 문서를 읽다가 발견한 오류, 추가하고 싶은 테스트를 해당 저장소의
이슈로 남겨주시면 작업 범위를 함께 정할 수 있습니다.

## 시뮬레이션 환경

v002 실행기 `LLM/sim/run_verification.sh`는 Vivado xsim을 사용합니다.
현재는 `PCCX_LAB_DIR`에 있는 트레이스 변환기 `from_xsim_log`에도 의존하므로,
코어 저장소만 내려받으면 시뮬레이션 실행 단계에서 막힐 수 있습니다.

외부 변환기 없이 실행할 수 있도록 환경을 정리하는 작업은
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152)에서
진행합니다. 그동안 `--list`로 테스트벤치 목록을 확인하고,
관심 모듈과 테스트 코드를 살펴볼 수 있습니다.

## KV260 보드 통합 살펴보기

```bash
git clone --recurse-submodules https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260.git
cd pccx-FPGA-NPU-LLM-kv260
git rev-parse HEAD
git submodule status
```

KV260 저장소는 `third_party/pccx-v002`에 지정된 코어 버전을 사용합니다.
`scripts/v002/use_submodule_sources.sh`가 코어의 시뮬레이션 실행기를
호출하므로 위의 실행 환경이 필요합니다. 문제를 공유할 때는 보드와 코어의
커밋을 함께 적어주세요. 버전 관리 방법은 {doc}`../reference/submodule-pin-policy`에 있습니다.

## 첫 테스트 고르기

기존 테스트벤치를 읽고 리셋, 핸드셰이크, 경계 조건 중 하나를 골라보세요.
이슈에는 대상 파일, 확인하려는 동작, 실행 명령과 예상 결과를 적으면 좋습니다.
실행 로그와 도구 버전도 함께 남겨주세요. 실행 중 오류가 났다면 오류 로그를
첨부하면 원인을 찾는 데 도움이 됩니다.

테스트 구성은 {doc}`../v002/Verification/index`에서,
기존 결과와 로그 위치는 {doc}`../Evidence/index`에서 확인할 수 있습니다.
Sail ISA 모델에 관심이 있다면 코어 저장소의 `LLM/formal/sail/`을 살펴보세요.
