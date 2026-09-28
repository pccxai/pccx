---
orphan: true
---

# Evidence pack index

이 페이지는 기존 검증 기록의 위치를 안내합니다. 과거 통과 기록은 현재
main의 재검증 결과가 아닙니다. pccx-lab은 폐지되었지만 실행기에 변환기
의존성이 남아 있어 새 공개 환경에서의 재현 경로는 정비 중입니다.
{doc}`../onboarding/getting-started`와 {doc}`/docs/Evidence/index`를 먼저 확인하세요.

## 검증 evidence

| 산출물 | 소스 | 위치 |
| --- | --- | --- |
| v002 ISA 모델 Sail typecheck pass | `pccxai/pccx-v002/.github/workflows/sail-typecheck.yml`의 `typecheck` | `pccxai/pccx-v002` GitHub Actions, `main`의 최신 run |
| KV260 sim wrapper PASS 요약(11 testbench) | `pccxai/pccx-FPGA-NPU-LLM-kv260/scripts/v002/use_submodule_sources.sh` | `build/sim_v002_submodule.log` |
| 테스트벤치별 산출물 (`xsim.log`, `.pccx`) | 동일한 wrapper | `third_party/pccx-v002/LLM/sim/work/<tb>/` |

과거 Phase D2 기록에 적힌 PASS는 `11 passed / 0 failed`.

## 통합 evidence

| 산출물 | 소스 | 위치 |
| --- | --- | --- |
| `pccx-v002/main`에서의 submodule pin 도달성 | cross-repo fresh-clone 검증 | [testing protocol](../reference/testing-protocol.md) |
| `repo-validate` 게이트 (`pccx-FPGA-NPU-LLM-kv260`) | `.github/workflows/validate.yml` | GH Actions `repo-validate` |
| EN/KO 정합성, strict Sphinx, sphinx-lint + codespell, repo-validate | `pccxai/pccx/.github/workflows/` | GH Actions |

## 이 페이지에 포함되지 않는 것

- throughput, latency, area, power 등 성능 수치. 아직 검증 수치가 없다.
- KV260 timing closure evidence. 시도는 했으나 완전 폐쇄 완료는 보류.
- application-level model evidence (Gemma 3N E4B end-to-end). 런타임 경로 검증은
  하드웨어 성능이나 정확도 증명을 대체하지 않는다.

부재 항목이 TBD에서 evidence로 전환되면, 그때 행을 추가한다.
