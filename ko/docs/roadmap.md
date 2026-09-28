# 로드맵

갱신일: 2026년 9월 28일.

PCCX는 Altifigence가 시작하고 운영하는 오픈소스 반도체 프로젝트입니다.
지금은 SystemVerilog 개발자가 RTL과 테스트벤치를 살펴보고, 작은 수정부터
기여할 수 있도록 개발 환경과 문서를 정리하고 있습니다.

먼저 FPGA 없이 실행할 수 있는 테스트 환경을 갖추고, 테스트부터 PR 제출까지
따라 할 수 있는 기여 가이드를 만들려 합니다.

## 저장소 안내

| 저장소 | 내용 |
| --- | --- |
| [pccx-v002](https://github.com/pccxai/pccx-v002) | v002 RTL, 테스트벤치, Sail ISA 모델 |
| [KV260 통합](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) | KV260 보드 통합, 런타임, 보드 테스트 |
| [pccx-v003](https://github.com/pccxai/pccx-v003) | v003 아키텍처를 위한 RTL 설계와 테스트벤치 |
| [pccx](https://github.com/pccxai/pccx) | 아키텍처 문서, 기여 가이드, 개발 로드맵 |

## 지금 준비하는 것

| 순서 | 할 일 | 목표 |
| --- | --- | --- |
| 1. 진행할 작업 정리 | 기존 이슈와 PR에서 이어갈 작업을 고릅니다. | 작업 범위와 담당자가 정해진 이슈 목록 |
| 2. 테스트 환경 정비 | 실행기의 외부 도구 의존성을 줄이고 필요한 도구와 실행 방법을 정리합니다. | FPGA 없이 실행하는 테스트벤치와 사용 안내 |
| 3. 첫 기여 이슈 준비 | 리셋, 핸드셰이크, 경계 조건 등 작은 검증 작업을 고릅니다. | 실행 명령과 예상 결과가 적힌 5개 안팎의 이슈 |
| 4. 기여 가이드 다듬기 | 처음 참여한 개발자의 경험을 바탕으로 막히는 부분을 개선합니다. | 테스트부터 PR과 리뷰까지 따라 할 수 있는 가이드 |

구체적인 일정은 담당자와 작업 범위를 정한 뒤 공유합니다.
테스트 환경 정비는 [KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152)에서
논의하고 있습니다. 현재 실행 환경은 {doc}`onboarding/getting-started`에서 확인하세요.

첫 검증 작업으로는 v002의 weight dispatcher, result packer, memory operation
queue를 살펴보고 있습니다. 기존 테스트벤치를 읽고 추가로 다룰 조건을 함께 찾아주세요.

## 보드와 아키텍처 개발

KV260 보드의 런타임 작업은
[KV260 #154](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/154)에서 진행합니다.
보드가 있다면 런타임과 데이터 전송을, 보드가 없다면 RTL과 테스트벤치를 살펴볼 수 있습니다.

v003, 디코딩, 희소성, 새로운 워크로드에 관한 제안도 각 저장소의 이슈에서 논의합니다.
시뮬레이션과 보드 테스트 결과는 소스 버전, 실행 환경, 로그와 함께
{doc}`Evidence/index`에 정리합니다.

## 참여하기

{doc}`quickstart`에서 관심 있는 저장소를 골라보세요.
작업 제안과 진행 상황은 [PCCX Roadmap](https://github.com/orgs/pccxai/projects/1)에서,
PR 작성 방법은 [기여 가이드](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md)에서
확인할 수 있습니다. 프로젝트 보드의 일정과 상태도 이 로드맵에 맞춰 정리할 예정입니다.

Altifigence의 개발 도구는 [Digital Design Studio 문서](https://docs.altifigence.com/ide/)를,
PCCX의 운영 방식은 [Transparency](https://pccx.ai/ko-kr/legal/transparency/)를 참고하세요.
기여할 때는 익숙한 편집기와 개발 도구를 사용해도 됩니다.
