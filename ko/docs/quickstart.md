---
myst:
  html_meta:
    description lang=ko: |
      PCCX RTL·검증 기여 시작: 공개 소스 확인, 저장소 구조 점검,
      시뮬레이션의 남은 의존성 확인, 작은 PR 준비.
---

# 빠른 시작

PCCX는 SystemVerilog 경험이 있는 RTL·검증 개발자의 참여를 환영합니다.
모듈이나 테스트벤치 하나부터 살펴보세요. {doc}`roadmap`의 우선순위는
독립적인 공개 테스트 경로와 작고 리뷰 가능한 기여를 준비하는 것입니다.

## 1. 작업할 저장소 선택

| 작업 | 저장소 |
| --- | --- |
| 재사용 가능한 v002 RTL·테스트벤치·Sail 모델 | [pccx-v002](https://github.com/pccxai/pccx-v002) |
| KV260 통합·런타임·보드 검증 자료 | [pccx-FPGA-NPU-LLM-kv260](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) |
| 실험 단계의 v003 RTL | [pccx-v003](https://github.com/pccxai/pccx-v003) |
| 아키텍처 문서·프로젝트 안내 | [pccx](https://github.com/pccxai/pccx) |

관심 모듈의 {doc}`v002/ISA/index`와 {doc}`v002/RTL/index`를 읽고,
해당 저장소의 기여 조건과 라이선스를 확인하세요.

## 2. 첫 로컬 점검

Git과 기본 Unix 도구가 있는 Linux·WSL 또는 Bash 환경에서 실행합니다.

```bash
git clone https://github.com/pccxai/pccx-v002.git
cd pccx-v002
bash scripts/check_repo_boundary.sh
git rev-parse HEAD
bash LLM/sim/run_verification.sh --list
```

첫 명령은 저장소 구조를 점검하고, `--list`는 테스트벤치 이름만 출력합니다.
**두 명령 모두 RTL 시뮬레이션이나 하드웨어 동작 검증이 아닙니다.**

**시뮬레이션 독립 실행은 준비 중입니다.** 현재 xsim 실행기는 Vivado를
사용하며, 폐지된 `pccx-lab`의 `from_xsim_log`를 호출합니다.
이 의존성 때문에 테스트 시작 전 실행이 막힐 수 있습니다.
참여를 위해 폐지된 Lab을 설치하지 마세요. 의존성 제거와 지원할 실행
명령은 {doc}`onboarding/getting-started` 및
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152)에서
확인할 수 있습니다.

## 3. 작은 기여 준비

리셋, ready/valid 핸드셰이크, 경계 조건, 명령어 디코드 중 한 동작을
선택합니다. 새 커버리지를 제안하기 전에 기존 테스트벤치를 확인하세요.
소스 SHA·도구 버전·입력·예상 결과·실제 결과·원본 로그를 기록합니다.
실행이 막혔다면 그 결과를 그대로 보고합니다.

해당 저장소의 이슈에서 범위와 리뷰 담당자를 정합니다.
첫 기여 이슈 묶음은 준비할 대상이며, 지금 바로 선택할 수 있는
이슈 5개가 마련됐다는 뜻은 아닙니다.
[기여 가이드](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md)도 확인하세요.

## 4. 문서 변경 빌드

Python·Make·Graphviz가 있는 Linux 또는 WSL에서 실행합니다.

```bash
git clone https://github.com/pccxai/pccx.git
cd pccx
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make strict REQUIRE_RTL=0
```

경고를 오류로 처리하면서 두 언어 문서를 빌드합니다.
`REQUIRE_RTL=0`은 문서만 작업할 때 쓰는 모드이며, 포함된 RTL 소스를
검증하지 않습니다. RTL 참조까지 확인하려면
[README](https://github.com/pccxai/pccx/blob/main/README.md)에 따라 소스를
준비하고 `make strict`를 실행하세요. 관련 안내는 영어·한국어를 함께 수정합니다.

운영 문서는 Cloudflare Pages를 통해
[docs.pccx.ai](https://docs.pccx.ai/)에 게시합니다.
배포 확인은 게시 성공을 뜻하며 RTL 동작 검증을 대신하지 않습니다.

## 도구 상태

**pccx-lab, SystemVerilog IDE, PCCX Launcher는 모두 폐지되었습니다.**
PCCX 참여에 세 제품이나 특정 IDE를 요구하지 않습니다.
[Digital Design Studio](https://docs.altifigence.com/ide/)는 선택적으로
참고할 Altifigence의 도구입니다. 첫 기여 목표에는 FPGA가 필요하지 않습니다.

검증 자료의 범위는 {doc}`Evidence/index`에서 확인하세요.
