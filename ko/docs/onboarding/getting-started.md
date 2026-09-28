---
orphan: true
---

# 기여 시작

{doc}`../quickstart`에서 저장소를 선택하고 공개 RTL과 테스트벤치 목록을
확인하세요. 첫 참여 목표는 FPGA 없이 작은 SystemVerilog 검증 PR을
제출할 수 있는 경로를 마련하는 것입니다.

## 현재 시뮬레이션을 막는 의존성

**pccx-lab, SystemVerilog IDE, PCCX Launcher는 모두 폐지되었습니다.**
v002의 `LLM/sim/run_verification.sh`에는 `PCCX_LAB_DIR` 아래의
`from_xsim_log` 호출이 남아 있습니다. 실행 파일이 없으면 테스트 전에
변환기 빌드를 시도합니다. 선택적인 트레이스 뷰어만의 문제가 아니라
실행을 막을 수 있는 의존성입니다.

KV260의 `scripts/v002/use_submodule_sources.sh`는
`third_party/pccx-v002`를 통해 해당 실행기를 호출하며 예전 Lab
디렉터리도 전달합니다. 의존성 제거와 소비 저장소의 고정 버전 갱신은
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152)에서
추적합니다. 대체할 공개 시뮬레이션 경로는 아직 검증되지 않았습니다.
참여를 위해 폐지 도구를 복원하지 마세요.

## 필요할 때 보드 통합 확인

```bash
git clone --recurse-submodules https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260.git
cd pccx-FPGA-NPU-LLM-kv260
git rev-parse HEAD
git submodule status
```

보드와 코어의 SHA를 함께 기록합니다. clone 성공은 시뮬레이션 결과가
아닙니다. 기존 xsim 경로에는 Vivado와 해당 시뮬레이션 라이브러리가
필요하며, 시뮬레이터에 독립적인 대체 경로가 완성됐다고 안내하지 않습니다.
고정 버전 검토는 {doc}`../reference/submodule-pin-policy`를 참고하세요.

## 테스트 하나의 범위와 결과 정하기

기여 이슈에는 대상 파일·인터페이스 또는 타이밍 동작·도구 버전·명령·
예상 assertion 또는 PASS/FAIL 결과·원본 로그 위치·리뷰 담당자를 명시합니다.
기존 커버리지를 먼저 확인하고 테스트벤치를 추가합니다.
실행이 막혔다면 PASS로 바꾸지 말고 그대로 기록합니다.
과거 실행 결과만으로 현재 main이 통과한다고 판단하지 않습니다.

{doc}`../v002/Verification/index`와 {doc}`../Evidence/index`를 읽어보세요.
형식 모델 점검은 코어의 `LLM/formal/sail/`에 있으며, RTL 시뮬레이션 및
실제 보드 실행과 별개의 결과입니다.
