검증
====

현재 v002 RTL과 테스트벤치의 원본은
`pccx-v002 <https://github.com/pccxai/pccx-v002>`_\ 입니다.
보드 통합 저장소는 고정된 코어를 사용합니다. 검증에 참여하려면
:doc:`/docs/quickstart`\ 에서 구조 점검과 테스트 목록부터 확인하세요.

현재 실행 조건
---------------

**pccx-lab, SystemVerilog IDE, PCCX Launcher는 모두 폐지되었습니다.**
현재 ``LLM/sim/run_verification.sh``\ 는 Vivado xsim을 사용하며,
폐지된 Lab의 ``from_xsim_log``\ 를 테스트 전 빌드하고 실행 후 호출합니다.
독립적인 공개 시뮬레이션 경로는 아직 완료되지 않았습니다.

``--list``\ 로 목록을 확인할 수 있지만 시뮬레이션은 수행하지 않습니다.
폐지 도구를 설치하도록 안내하지 않습니다. 의존성 제거는
`KV260 #152 <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152>`_\ 와
:doc:`/docs/onboarding/getting-started`\ 에서 추적합니다.

테스트벤치 목록과 실제 통과 기록은 구분해야 합니다. 실행 결과에는
코어 SHA·도구 버전·명령·예상 결과·실제 결과·원본 로그를 첨부합니다.
원본 로그의 예정 위치는 ``LLM/sim/work/<tb>/``\ 이며,
보드 wrapper 요약은 ``build/sim_v002_submodule.log``\ 입니다.

첫 검증 기여의 범위
--------------------

* 기존 weight dispatcher, result packer, memory operation queue
  테스트벤치를 읽고 이미 다루는 조건을 확인합니다.
* 리셋·핸드셰이크·경계 조건 중 재현 가능한 작은 범위를 정합니다.
* assertion 또는 PASS/FAIL 기준을 정하고 리뷰 담당자와 합의합니다.
* 도구 오류나 미실행 결과를 성공으로 처리하지 않습니다.

과거 유닛 테스트 기록
----------------------

아래 표는 2026-04-21의 KV260 저장소 커밋 ``773bd82``\ 를 대상으로
이 문서에 기록됐던 결과입니다. 현재 main을 다시 실행한 결과가 아니며,
당시 경로와 실행기를 현재 기여 절차로 사용하지 않습니다.

.. list-table::
   :header-rows: 1
   :widths: 35 50 15

   * - 테스트벤치
     - 범위
     - 상태
   * - ``tb_GEMM_dsp_packer_sign_recovery``
     - 듀얼 채널 W4A8 pack + post-MAC 부호 복원, 1024 사이클
     - PASS
   * - ``tb_mat_result_normalizer``
     - BF16 alignment / exponent delay, 256 사이클
     - PASS
   * - ``tb_GEMM_weight_dispatcher``
     - HP weight stream → INT4 tile dispatch, 128 사이클
     - PASS
   * - ``tb_FROM_mat_result_packer``
     - 32 × 16-bit staggered capture → 128-bit AXIS pack, 4 사이클
     - PASS
   * - ``tb_barrel_shifter_BF16``
     - BF16 mantissa barrel shift, 512 사이클
     - PASS
   * - ``tb_ctrl_npu_decoder``
     - 64-bit VLIW 디코드 → 타입 구조체, 6 사이클
     - PASS


시뮬레이션 이후의 검증
----------------------

형식 모델, 합성·배치배선, 타이밍 리포트, 실제 보드 실행은 각각 별도의
증거가 필요합니다. 모듈 테스트 통과만으로 모델 추론·성능·실리콘 동작을
보장하지 않습니다. :doc:`/docs/Evidence/index`\ 의 기준을 따르세요.

.. seealso::

   :doc:`/docs/v002/Architecture/index`
   :doc:`/docs/v002/ISA/index`
   :doc:`/docs/v002/RTL/index`
