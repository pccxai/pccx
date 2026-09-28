Verification
============

Current v002 RTL and testbenches live in
`pccx-v002 <https://github.com/pccxai/pccx-v002>`_.
The board integration repository consumes a pinned core. Begin with
the structural check and test listing in :doc:`/docs/quickstart`.

Current execution prerequisites
--------------------------------

**pccx-lab, SystemVerilog IDE and PCCX Launcher are discontinued.**
The current ``LLM/sim/run_verification.sh`` uses Vivado xsim and still
builds the retired Lab's ``from_xsim_log`` before tests, then invokes it
after simulation. The independent public simulation path is not complete.

``--list`` can enumerate testbenches without running them. Installing
retired tools is not an onboarding step. Dependency removal is tracked
through `KV260 #152 <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152>`_
and :doc:`/docs/onboarding/getting-started`.

A testbench listing is distinct from a passing run. Attach the core SHA,
tool version, command, expected result, actual result and raw logs.
The runner's output location is ``LLM/sim/work/<tb>/``;
the board wrapper summary belongs in ``build/sim_v002_submodule.log``.

Scope a first verification contribution
---------------------------------------

* Read the existing weight dispatcher, result packer or memory operation
  queue testbench before proposing new coverage.
* Choose a small reset, handshake or boundary-condition case.
* Agree on assertions or PASS/FAIL criteria with a reviewer.
* Report tool failures and unexecuted tests as such.

Historical unit-test record
---------------------------

The table below was recorded here for KV260 repository commit
``773bd82`` on April 21, 2026. It is not a fresh result for current main.
The old source paths and runner are not the current contributor runbook.

.. list-table::
   :header-rows: 1
   :widths: 35 50 15

   * - Testbench
     - Scope
     - Status
   * - ``tb_GEMM_dsp_packer_sign_recovery``
     - Dual-channel W4A8 pack + post-MAC sign recovery, 1024 cycles
     - PASS
   * - ``tb_mat_result_normalizer``
     - BF16 alignment / exponent delay, 256 cycles
     - PASS
   * - ``tb_GEMM_weight_dispatcher``
     - HP weight stream → INT4 tile dispatch, 128 cycles
     - PASS
   * - ``tb_FROM_mat_result_packer``
     - 32 × 16-bit staggered capture → 128-bit AXIS pack, 4 cycles
     - PASS
   * - ``tb_barrel_shifter_BF16``
     - BF16 mantissa barrel shift, 512 cycles
     - PASS
   * - ``tb_ctrl_npu_decoder``
     - 64-bit VLIW decode → typed structs, 6 cycles
     - PASS


Verification beyond simulation
-------------------------------

Formal models, synthesis and implementation, timing reports and execution
on a board require separate evidence. Passing a module test does not
establish model inference, performance or silicon readiness.
Follow :doc:`/docs/Evidence/index`.

.. seealso::

   :doc:`/docs/v002/Architecture/index`
   :doc:`/docs/v002/ISA/index`
   :doc:`/docs/v002/RTL/index`
