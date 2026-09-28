# Roadmap

Updated September 28, 2026.

PCCX is an open-source semiconductor project initiated and operated by
Altifigence. Our immediate priority is to make it practical for developers
with **SystemVerilog RTL and verification experience** to contribute.

The first milestone is a small, reproducible contribution: check out public
RTL, run a testbench without an FPGA, investigate a result, and submit a
reviewable verification PR.

## Current scope

| Repository | Responsibility |
| --- | --- |
| [pccx-v002](https://github.com/pccxai/pccx-v002) | Reusable v002 RTL, testbenches and the Sail ISA model. |
| [KV260 integration](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) | Board integration, runtime and hardware evidence; consumes a pinned v002 core. |
| [pccx-v003](https://github.com/pccxai/pccx-v003) | Experimental v003 RTL and verification work; hardware readiness is not established by source availability. |
| [pccx](https://github.com/pccxai/pccx) | Architecture documentation, contribution guidance and the public roadmap. |

## Retired tools

**pccx-lab, SystemVerilog IDE and PCCX Launcher are discontinued.**
They are outside the active roadmap. Their old installation instructions,
product links and integration plans are not a supported contribution path.
SystemVerilog remains the language used for RTL and testbench development.

The current v002 simulation runner still invokes the retired Lab trace
converter, `from_xsim_log`. Removing that dependency is an **open task**,
not a completed migration. Do not restore the retired tools to get started.
{doc}`onboarding/getting-started` explains the available first check and
the remaining simulation prerequisite.

## First contribution milestone

| Step | Work | Completion criterion |
| --- | --- | --- |
| 1. Align the backlog | Review old issues, PRs and milestones; separate retired work from current RTL work. | Each active task has a scope, reviewer, dependencies and a checkable result. Retired work is recorded as discontinued rather than implemented. |
| 2. Publish an independent RTL test path | Remove the Lab dependency; document supported tools and one small testbench. | A clean public checkout runs without the retired tools or an FPGA, producing a meaningful PASS/FAIL result and raw logs. |
| 3. Prepare small verification tasks | Prepare about five scoped RTL/TB issues after checking existing test coverage. | Each issue identifies files, interface or timing rules, a reproduction command, expected results and a reviewer. |
| 4. Validate external participation | Have an independent contributor follow checkout → test → change → PR → review. | The path is reproduced, obstacles are fixed, and the resulting change can be reviewed using its evidence. |

These are completion goals, not claims that the work has finished. Dates
will be assigned when maintainer availability and dependencies are agreed.
There is no new fixed release deadline.

The first implementation entry is
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152),
covering contributor onboarding. The v002 weight dispatcher, result packer
and memory operation queue are candidate areas for small verification work;
existing testbenches must be reviewed before adding duplicate coverage.

## Hardware and later research

Board runtime investigation continues separately through
[KV260 #154](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/154).
Simulation, synthesis, implementation and execution on a board have
separate completion criteria. Board access is not a prerequisite for the
first contribution milestone.

Advanced decoding, sparsity, new workloads and further v003 development
remain subjects for scoped technical proposals. Earlier calendar plans,
training budgets and throughput targets are not current commitments.
Measured results belong in {doc}`Evidence/index` with source SHAs,
tool versions, commands and raw logs.

## Tracking and participation

Use the existing [PCCX Roadmap project](https://github.com/orgs/pccxai/projects/1)
and [contribution guide](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md).
The board is being reconciled with the new direction; old target-release
fields and status columns may still reflect earlier plans.
Original experiment and release dates remain historical records.

Start with {doc}`quickstart`. Altifigence
[Digital Design Studio documentation](https://docs.altifigence.com/ide/)
is an optional external resource, not a prerequisite or an automatic
replacement for retired PCCX tools. See
[Transparency](https://pccx.ai/en/legal/transparency/) for the relationship
between PCCX and Altifigence.
