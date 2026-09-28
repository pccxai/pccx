==========================================
Historical Gemma 3N E4B Integration Plan
==========================================

.. warning::

   Historical integration plan. pccx-lab, SystemVerilog IDE and PCCX
   Launcher are discontinued. The former UI/daemon protocol below is
   retained for provenance, not as a supported product or installation
   guide. For current work, read :doc:`/docs/roadmap` and
   :doc:`/docs/onboarding/getting-started`.

This page preserves the earlier Gemma 3N E4B target-path contract and
candidate bitstream identity. It does not establish current runtime,
timing, model accuracy or throughput.

Shared Daemon Contract
======================

The former integration plan described an aiohttp HTTP+WS daemon on port ``7860``. The
common readiness endpoint is ``GET /api/status``.

.. code-block:: json

   {
     "schemaVersion": "pccx.kv260.status.v0",
     "daemon": {
       "transport": "aiohttp",
       "httpPort": 7860,
       "websocketAvailable": true
     },
     "target": {
       "device": "KV260",
       "model": "Gemma 3N E4B target path"
     },
     "bitstream": {
       "candidate": "v12d",
       "sha256": "59558c5f86968be2cd968212be3519afeb7afd148809079a314af29a50cf0c6c",
       "verified": false
     },
     "backend": {
       "mode": "cpu",
       "allowedModes": ["cpu", "npu_uca", "hybrid"]
     },
     "readiness": {
       "state": "blocked",
       "stage": "Stage 1 of staged release",
       "goldenVectorGate": "pending",
       "evidenceGate": "no measured tok/s claims"
     }
   }

Backend modes are interpreted conservatively:

``cpu``
   Numpy or host-side baseline for command and protocol validation.

``npu_uca``
   v002 NPU target path through the PCCX ISA. This stays experimental
   until bitstream identity and golden-vector gates are reviewed.

``hybrid``
   CPU orchestration with selected NPU offload targets. Each offload
   remains separately gated.

The v12d candidate SHA256 recorded in that plan was
``59558c5f86968be2cd968212be3519afeb7afd148809079a314af29a50cf0c6c``.
A SHA match identifies the candidate bitstream only; it is not a
throughput, timing, or runtime signoff.

Former integration surfaces
============================

The plan referenced pccx-lab Live Run, SystemVerilog IDE Board Health,
PCCX Launcher chat and a trace Live Capture endpoint. These references
do not define a current contribution route. Use raw runtime logs and
source/bitstream identifiers in a scoped KV260 issue.

Release Wording Rules
=====================

The original plan used the following evidence-limited wording:

- "Gemma 3N E4B target path"
- "runtime readiness checks"
- "experimental"
- "golden-vector gated"
- "Stage 1 of staged release"
- "evidence-gated — no measured tok/s claims"

Avoid wording that says or implies:

- measured token rate or latency;
- production readiness;
- completed on-board model execution;
- timing, bitstream, or runtime signoff;
- FPS or application benchmark results.

Where to File Issues
====================

File canonical documentation issues in:
https://github.com/pccxai/pccx/issues

File daemon, board integration, bitstream, and golden-vector evidence
issues in:
https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues

For current issues, include the checked-out source and bitstream hashes,
tool versions, reproduction command, expected/actual behavior and raw logs.
Do not require a retired debug UI to report a board or runtime problem.
