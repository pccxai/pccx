# 로드맵

갱신일: 2026년 9월 28일.

PCCX는 Altifigence가 시작하고 운영하는 오픈소스 반도체 프로젝트입니다.
현재 우선순위는 **SystemVerilog 경험이 있는 RTL·검증 개발자**가
실제로 참여할 수 있는 공개 개발 환경을 정비하는 것입니다.

첫 마일스톤은 작은 기여를 재현하는 것입니다. 공개 RTL을 내려받고,
FPGA 없이 테스트벤치를 실행하고, 결과를 분석한 뒤 검증 PR을 제출하는
경로를 마련합니다.

## 현재 범위

| 저장소 | 역할 |
| --- | --- |
| [pccx-v002](https://github.com/pccxai/pccx-v002) | 재사용 가능한 v002 RTL, 테스트벤치, Sail ISA 모델 |
| [KV260 통합](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) | 고정된 v002 코어를 사용하는 보드 통합, 런타임, 하드웨어 검증 자료 |
| [pccx-v003](https://github.com/pccxai/pccx-v003) | 실험 단계의 v003 RTL과 검증 작업. 소스 공개가 하드웨어 동작 검증을 의미하지는 않습니다. |
| [pccx](https://github.com/pccxai/pccx) | 아키텍처 문서, 기여 안내, 공개 로드맵 |

## 폐지된 도구

**pccx-lab, SystemVerilog IDE, PCCX Launcher는 모두 폐지되었습니다.**
세 도구는 현재 로드맵에서 제외합니다. 예전 설치 안내, 제품 링크,
연동 계획은 현재 지원하는 참여 경로가 아닙니다.
SystemVerilog 언어를 사용하는 RTL·테스트벤치 개발은 계속됩니다.

현재 v002 시뮬레이션 실행기에는 폐지된 Lab의 트레이스 변환기
`from_xsim_log` 호출이 남아 있습니다. 의존성 제거는 **미완료 과제**이며,
이전이 끝났다고 안내하지 않습니다. 시작을 위해 폐지 도구를 복원하지
마세요. 지금 가능한 첫 점검과 시뮬레이션의 남은 조건은
{doc}`onboarding/getting-started`에서 확인할 수 있습니다.

## 첫 기여 마일스톤

| 순서 | 작업 | 완료 기준 |
| --- | --- | --- |
| 1. 기존 작업 정리 | 옛 이슈·PR·마일스톤을 검토하고 폐지 작업과 현재 RTL 작업을 구분합니다. | 현재 작업마다 범위·리뷰 담당자·의존성·검증 기준이 있습니다. 폐지 작업은 구현 완료로 계산하지 않습니다. |
| 2. 독립적인 RTL 테스트 경로 | Lab 의존성을 제거하고 지원 도구와 작은 테스트벤치 하나를 안내합니다. | 새 공개 checkout에서 폐지 도구나 FPGA 없이 실행하고 의미 있는 PASS/FAIL 결과와 원본 로그를 얻습니다. |
| 3. 작은 검증 작업 준비 | 기존 커버리지를 확인한 뒤 RTL·TB 이슈 약 5개를 준비합니다. | 대상 파일·인터페이스 또는 타이밍 규약·재현 명령·예상 결과·리뷰 담당자를 명시합니다. |
| 4. 외부 참여 흐름 검증 | 외부 기여자가 checkout → 테스트 → 수정 → PR → 리뷰를 진행합니다. | 같은 경로를 재현하고 막힌 지점을 개선하며 결과를 근거로 변경을 리뷰할 수 있습니다. |

위 항목은 앞으로 충족할 완료 기준입니다. 이미 완료된 작업을 뜻하지 않습니다.
담당자의 투입 시간과 의존성을 정한 뒤 목표일을 배정하며,
새 릴리스의 고정 마감일은 아직 없습니다.

첫 구현 진입점은 기여자 온보딩을 다루는
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152)입니다.
v002 weight dispatcher, result packer, memory operation queue는 작은 검증
작업의 후보입니다. 기존 테스트벤치의 커버리지를 먼저 확인해 중복 작업을 피합니다.

## 보드 검증과 후속 연구

보드 런타임 조사는
[KV260 #154](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/154)에서
별도로 진행합니다. 시뮬레이션·합성·구현·실제 보드 실행에는 각각 다른
완료 기준을 적용합니다. 첫 기여 마일스톤에 보드 보유를 요구하지 않습니다.

고급 디코딩, 희소성, 새로운 워크로드와 v003의 후속 개발은 범위를 정한
기술 제안으로 검토합니다. 예전 달력 일정·학습 예산·처리량 목표를 현재의
약속으로 사용하지 않습니다. 측정 결과는 소스 SHA·도구 버전·실행 명령·
원본 로그와 함께 {doc}`Evidence/index`에 기록합니다.

## 작업 추적과 참여

기존 [PCCX Roadmap 프로젝트](https://github.com/orgs/pccxai/projects/1)와
[기여 가이드](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md)를 사용합니다.
프로젝트 보드는 새 방향에 맞춰 정리할 대상이며, 과거 릴리스 필드와 상태
열이 아직 남아 있을 수 있습니다. 원래 실험일과 릴리스 날짜는 기록으로 보존합니다.

{doc}`quickstart`에서 시작하세요. Altifigence의
[Digital Design Studio 문서](https://docs.altifigence.com/ide/)는 선택적으로
참고할 외부 자료입니다. PCCX 참여의 필수 조건이 아니며, 폐지 도구의
기능이 자동으로 이전됐다는 뜻도 아닙니다. PCCX와 Altifigence의 관계는
[Transparency](https://pccx.ai/ko-kr/legal/transparency/)에서 안내합니다.
