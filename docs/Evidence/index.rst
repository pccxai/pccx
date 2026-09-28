Evidence
========

This page collects simulation, ISA-model and board test records for PCCX.
Include the source commit, tool versions, command and logs when sharing a result.

Where to find records
----------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Area
     - Information to record
     - Location and guidance
   * - Repository structure
     - Source commit and check output
     - ``scripts/check_repo_boundary.sh`` in ``pccx-v002``.
       See :doc:`../quickstart` for the command.
   * - v002 RTL simulation
     - Testbench, tool version, command, expected result and actual logs
     - ``LLM/sim/work/<tb>/``.
       See :doc:`../onboarding/getting-started` for the environment.
   * - Sail ISA model
     - Source commit and type-check result
     - `pccx-v002 Actions <https://github.com/pccxai/pccx-v002/actions>`_.
   * - Documentation
     - EN/KO build logs and deployed revision
     - GitHub Actions in pccx and Cloudflare Pages deployment records.
   * - KV260 board and runtime
     - Source and bitstream hashes, timing reports, inputs and board logs
     - `KV260 #58 <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/58>`_.

Earlier records
----------------

Earlier test and trace-analysis results are kept in the
`previous documentation <https://github.com/pccxai/pccx/blob/6336b16d5fe4ae80721e0bbb9e2cae00f24e8325/docs/Evidence/index.rst>`_.
Each result refers to the source and environment used at the time.

Share a result
---------------

1. Describe the test and target commit in the relevant repository's issue or PR.
2. Include tool versions, inputs and the command.
3. Explain the expected and actual results, with raw logs attached.
4. Add the reviewed result to the documentation.

When comparing throughput, latency, resource use or power, check the
environment and inputs as well. See :doc:`../v002/Verification/index`
for the test structure.
