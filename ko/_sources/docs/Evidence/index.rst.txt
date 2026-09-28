검증 자료
=========

PCCX의 시뮬레이션, ISA 모델, 보드 테스트 기록을 모읍니다.
결과를 공유할 때는 소스 커밋, 도구 버전, 실행 명령과 로그를 함께 남겨주세요.

자료별 기록 위치
-----------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - 항목
     - 함께 기록할 정보
     - 위치와 안내
   * - 저장소 구조 점검
     - 소스 커밋과 점검 결과
     - ``pccx-v002``\ 의 ``scripts/check_repo_boundary.sh``.
       :doc:`../quickstart`\ 에서 실행 방법을 안내합니다.
   * - v002 RTL 시뮬레이션
     - 테스트벤치, 도구 버전, 실행 명령, 예상 결과와 실제 로그
     - ``LLM/sim/work/<tb>/``.
       실행 환경은 :doc:`../onboarding/getting-started`\ 를 참고하세요.
   * - Sail ISA 모델
     - 소스 커밋과 타입 검사 결과
     - `pccx-v002 Actions <https://github.com/pccxai/pccx-v002/actions>`_.
   * - 문서
     - EN/KO 빌드 로그와 배포 버전
     - pccx 저장소의 GitHub Actions와 Cloudflare Pages 배포 기록.
   * - KV260 보드와 런타임
     - 소스·비트스트림 해시, 타이밍 리포트, 입력 데이터와 보드 로그
     - `KV260 #58 <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/58>`_.

이전 기록
---------

이전 테스트와 트레이스 분석 결과는
`과거 문서 <https://github.com/pccxai/pccx/blob/6336b16d5fe4ae80721e0bbb9e2cae00f24e8325/ko/docs/Evidence/index.rst>`_\ 에 보관되어 있습니다. 각 결과는 당시의 소스와 실행 환경을 기준으로 합니다.

결과 공유하기
--------------

1. 해당 저장소의 이슈나 PR에 테스트 목적과 대상 커밋을 적습니다.
2. 도구 버전, 입력 데이터, 실행 명령을 남깁니다.
3. 예상 결과와 실제 결과를 설명하고 원본 로그를 첨부합니다.
4. 리뷰를 거친 결과를 문서에 추가합니다.

처리량, 지연, 자원 사용량, 전력을 비교할 때는 측정 환경과 입력 조건도
함께 확인하세요. 테스트 구성은 :doc:`../v002/Verification/index`\ 에서
살펴볼 수 있습니다.
