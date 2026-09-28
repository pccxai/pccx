Verification
============

Current v002 RTL and testbenches live in
`pccx-v002 <https://github.com/pccxai/pccx-v002>`_.
The board integration repository consumes a pinned core. Begin with
the structural check and test listing in :doc:`/docs/quickstart`.

Execution environment
----------------------

``LLM/sim/run_verification.sh`` uses Vivado xsim and currently also needs
the external ``from_xsim_log`` trace converter. Work to reduce this
dependency is tracked in
`KV260 #152 <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152>`_.
See :doc:`/docs/onboarding/getting-started` for the setup. Use ``--list``
to view the testbench names.

Include the core commit, tool version, command and logs when sharing a run.
Test logs are written to ``LLM/sim/work/<tb>/``; the board wrapper's
summary is written to ``build/sim_v002_submodule.log``.

Scope a first verification contribution
---------------------------------------

* Read the existing weight dispatcher, result packer or memory operation
  queue testbench before proposing new coverage.
* Choose a small reset, handshake or boundary-condition case.
* Agree on assertions or PASS/FAIL criteria with a reviewer.
* Attach the run log and compare it with the expected result.

Historical unit-test record
---------------------------

The following results were recorded on April 21, 2026, for commit
``773bd82`` in the KV260 repository.

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

After synthesis and implementation, check timing and resource use, then
test data transfers and runtime behavior on the board. See
:doc:`/docs/Evidence/index` for how to record the results.

.. seealso::

   :doc:`/docs/v002/Architecture/index`
   :doc:`/docs/v002/ISA/index`
   :doc:`/docs/v002/RTL/index`
