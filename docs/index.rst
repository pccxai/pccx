pccx: Parallel Compute Core eXecutor
=====================================

|License| |Architecture| |Target| |Precision|

   **Notice: Active Development in Progress.** pccx is a scalable,
   modular Neural Processing Unit (NPU) architecture designed to
   accelerate Transformer-based large language models (LLMs) on
   resource-constrained edge devices.

--------------

1. Architecture Overview
------------------------

pccx is a hardware-software co-design framework for autoregressive
Transformer-LLM decoding on resource-constrained edge devices. The
core architecture is sized at synthesis time to match the DSP, BRAM,
and URAM budget of each target device. The primary target is the
Xilinx Kria KV260 SoM (Zynq UltraScale+ ZU5EV).

1.1 Ecosystem Structure
~~~~~~~~~~~~~~~~~~~~~~~

The project is structured in three layers so that the same logic
can be resynthesized for a different device or driven by a different
host stack.

-  ``/architecture`` **(Logic Layer)** — core RTL and generate
   parameters.

   -  Defines the logical pipeline, instruction scheduling, and the
      **custom 64-bit ISA**.
   -  Independent of any specific hardware vendor or interface protocol.

-  ``/device`` **(Implementation Layer)** — maps the pccx architecture
   onto a specific hardware target.

   -  Adjusts core count, systolic-array dimensions, and memory port
      widths to the available resource budget (DSP count, local memory
      size, etc.).

-  ``/driver`` **(Software Layer)** — a C/C++ hardware abstraction layer
   (HAL) and high-level API.

   -  Handles instruction dispatch and memory mapping, bridging
      high-level AI models with the pccx hardware.

--------------

2. Key Technical Features
-------------------------

2.1 Decoupled Dataflow & Custom ISA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pccx uses a **custom 64-bit ISA** tuned for matrix and vector
operations. A **decoupled-dataflow** pipeline separates instruction
decode from execution to reduce dispatch-side stalls.

2.2 W4A8 Dynamic Precision Promotion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pccx balances efficiency with accuracy:

-  **Compute**: a parallel 2D systolic array executes dense
   **INT4 (weight) × INT8 (activation)** operations.
-  **Promotion**: during non-linear operations (Softmax, RMSNorm, GELU),
   the CVO core automatically promotes precision to **BF16 / FP32** so
   numerical integrity is preserved.

2.3 Tiered Memory Hierarchy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Matrix core**: dedicated GEMM, with a scalable array size.
-  **Vector core**: GEMV and element-wise operations.
-  **Shared interconnect**: a flexible bus that lets cores and local
   caches access each other concurrently without arbitration overhead.

--------------

3. Documentation
----------------

Detailed technical specifications for the active **v002** line live
under :doc:`v002/index`:

1. :doc:`quickstart` — reader path for release-line claims, evidence,
   local checks, deploy posture, and common v002.1 questions.
2. :doc:`v002/ISA/index` — 64-bit custom instruction set.
3. :doc:`v002/Architecture/index` — hardware architecture and
   floorplan.
4. :doc:`v002/Drivers/index` — driver and SDK documentation.

v003 and the Vision track no longer live on this Sphinx site. They are
maintained at `docs.altifigence.com <https://docs.altifigence.com/>`__,
which is now the canonical hub for every PCCX™ track beyond v002.

The :doc:`roadmap` retains the historical relationship between tracks.

Evidence-gated v002.1 pointers:

.. list-table::
   :header-rows: 1
   :widths: 24 44 32

   * - Item
     - Link
     - Guard
   * - Architecture explainer
     - `docs/spec/v002.1-architecture-explainer.md (PR #48) <https://github.com/pccxai/pccx/blob/docs/v002.1-architecture-explainer/docs/spec/v002.1-architecture-explainer.md>`__
     - Draft explainer; no board-run, closed-timing, deployable-bitstream,
       or measured-throughput claim.
   * - Evidence inventory
     - `pccx-FPGA-NPU-LLM-kv260 evidence inventory (PR #95) <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/blob/docs/v002.1-evidence-inventory/docs/evidence/v002.1-evidence-inventory.md>`__
     - Inventory of landed and pending evidence; release claims remain
       gated by measured artifacts.
   * - Bitstream runbook
     - `pccx-FPGA-NPU-LLM-kv260 bitstream runbook (PR #82) <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/blob/build/v002-kv260-bitstream-runbook/docs/runbooks/v002.1-bitstream-build.md>`__
     - Pre-flight runbook; Vivado and KV260 board execution are not
       claimed by this link.
   * - Project board
     - `PCCX Roadmap project board <https://github.com/orgs/pccxai/projects/1>`__
     - Planning tracker; status must be read with the evidence gates
       above.

The v001 architecture is archived at
:doc:`archive/experimental_v001/index`.

--------------

4. License
----------

This repository uses a mixed rights model. Source code is licensed under
the **Apache License 2.0**. PCCX™ documentation, site copy, diagrams,
logos, trademarks, and brand assets are protected company assets of
Altifigence.

--------------

5. Project and participation
----------------------------------------

Reusable RTL and testbenches live in
`pccx-v002 <https://github.com/pccxai/pccx-v002>`_.
`KV260 integration <https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260>`_
owns board and runtime work.
`pccx-v003 <https://github.com/pccxai/pccx-v003>`_ contains RTL design
and testbenches for the v003 architecture.

Begin a small RTL or verification contribution at :doc:`quickstart`.
Read :doc:`onboarding/getting-started` for current execution prerequisites
and :doc:`roadmap` for upcoming work.

.. |License| image:: https://img.shields.io/badge/License-Apache_2.0-blue.svg
.. |Architecture| image:: https://img.shields.io/badge/Architecture-Scalable_NPU-purple
.. |Target| image:: https://img.shields.io/badge/Target-Edge_AI-orange
.. |Precision| image:: https://img.shields.io/badge/Precision-W4A8_Promotion-green

.. toctree::
   :hidden:

   quickstart
