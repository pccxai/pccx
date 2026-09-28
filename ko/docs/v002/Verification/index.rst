검증
====

현재 v002 RTL과 테스트벤치의 원본은
`pccx-v002 <https://github.com/pccxai/pccx-v002>`_\ 입니다.
보드 통합 저장소는 고정된 코어를 사용합니다. 검증에 참여하려면
:doc:`/docs/quickstart`\ 에서 구조 점검과 테스트 목록부터 확인하세요.

실행 환경
---------

``LLM/sim/run_verification.sh``\ 는 Vivado xsim을 사용합니다.
현재는 외부 트레이스 변환기 ``from_xsim_log``\ 도 필요하며,
이 의존성을 줄이는 작업은
`KV260 #152 <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152>`_\ 에서 진행합니다. 자세한 설정은 :doc:`/docs/onboarding/getting-started`\ 를
참고하세요. ``--list``\ 로 테스트벤치 목록을 확인할 수 있습니다.

실행 결과에는 코어 커밋, 도구 버전, 명령과 로그를 함께 남겨주세요.
테스트별 로그는 ``LLM/sim/work/<tb>/``\ 에,
보드 wrapper의 요약은 ``build/sim_v002_submodule.log``\ 에 기록됩니다.

첫 검증 기여의 범위
--------------------

* 기존 weight dispatcher, result packer, memory operation queue
  테스트벤치를 읽고 이미 다루는 조건을 확인합니다.
* 리셋·핸드셰이크·경계 조건 중 재현 가능한 작은 범위를 정합니다.
* assertion 또는 PASS/FAIL 기준을 정하고 리뷰 담당자와 합의합니다.
* 실행 로그를 첨부하고 예상 결과와 비교합니다.

과거 유닛 테스트 기록
----------------------

아래는 KV260 저장소의 커밋 ``773bd82``\ 에서 기록한
2026년 4월 21일의 테스트 결과입니다.

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

합성·배치배선 이후에는 타이밍과 자원 사용량을 확인하고, 보드에서
데이터 전송과 런타임을 테스트합니다. 결과를 기록하는 방법은
:doc:`/docs/Evidence/index`\ 에 정리되어 있습니다.

.. seealso::

   :doc:`/docs/v002/Architecture/index`
   :doc:`/docs/v002/ISA/index`
   :doc:`/docs/v002/RTL/index`
