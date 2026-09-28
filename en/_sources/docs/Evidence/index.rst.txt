Evidence
========

Verification records must identify the source revision, tools, command,
inputs, expected result, actual result and raw logs. A document or a
successful site deployment is not a simulation or hardware result.

Current evidence requirements
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Area
     - Current interpretation
     - Required evidence
   * - Public repository boundary
     - An available structural check, not RTL execution.
     - Source SHA and output from ``scripts/check_repo_boundary.sh`` in
       ``pccx-v002``. See :doc:`../quickstart`.
   * - v002 RTL simulation
     - Independent public reproduction is pending.
     - Remove the retired Lab converter dependency, then record a clean
       checkout, tool versions and per-testbench logs. See
       :doc:`../onboarding/getting-started`.
   * - Sail ISA model
     - Formal-model results must be tied to a specific run.
     - The source SHA and run from
       `pccx-v002 Actions <https://github.com/pccxai/pccx-v002/actions>`_.
       Type checking does not prove RTL or board correctness.
   * - Documentation
     - Build and publication checks cover the documentation.
     - EN/KO strict build logs, merged SHA, Cloudflare deployment result
       and the published pages.
   * - KV260 implementation and runtime
     - Board claims require their own evidence.
     - Source and bitstream hashes, tool versions, timing reports,
       runtime inputs and captured board logs reviewed through
       `KV260 #58 <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/58>`_.

Retired-tool records
--------------------

**pccx-lab, SystemVerilog IDE and PCCX Launcher are discontinued.**
They are not required products in the current contribution roadmap.
Old Lab tests, trace-format checks and analyzer output cannot establish
that today's public RTL checkout runs independently.

The following statements were recorded in the
`previous evidence page <https://github.com/pccxai/pccx/blob/6336b16d5fe4ae80721e0bbb9e2cae00f24e8325/docs/Evidence/index.rst>`_.
They are retained as historical claims, not revalidated results:

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Historical item
     - Previously recorded result
   * - Lab core tests
     - 7/7 ISA tests and 16 analyzer tests.
   * - Trace-format round trip
     - Bit-exact decode reported for the former format tool.
   * - Self-calibrated golden diff
     - 8/8 and 128/128 steps within ±15%; this was not a model-accuracy
       or hardware-performance result.

Publishing new results
-----------------------

1. Capture raw simulation, synthesis or board logs in the repository
   responsible for the work.
2. Record exact source and tool versions and the reproduction command.
3. Link the immutable artifact or run and state its scope and limitations.
4. Review the result before adding a measured value to the documentation.

Throughput, latency, resource use and power are separate measurements.
Targets and historical reports must not be presented as current measured
results. See :doc:`../v002/Verification/index` and :doc:`../roadmap`.
