# Roadmap

Updated September 28, 2026.

PCCX is an open-source semiconductor project initiated and operated by
Altifigence. We are improving the development setup and documentation so
SystemVerilog developers can explore the RTL, work on a testbench, and
make a first contribution.

Our first goal is a test environment that runs without an FPGA, with a
guide that takes contributors from running a test to opening a pull request.

## Repositories

| Repository | Contents |
| --- | --- |
| [pccx-v002](https://github.com/pccxai/pccx-v002) | v002 RTL, testbenches and the Sail ISA model. |
| [KV260 integration](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) | KV260 board integration, runtime and board tests. |
| [pccx-v003](https://github.com/pccxai/pccx-v003) | RTL design and testbenches for the v003 architecture. |
| [pccx](https://github.com/pccxai/pccx) | Architecture documentation, contribution guides and the development roadmap. |

## What we are working toward

| Step | Work | Goal |
| --- | --- | --- |
| 1. Organize upcoming work | Review existing issues and PRs and choose what to carry forward. | An issue list with a scope and owner for each task. |
| 2. Simplify the test setup | Reduce external tool dependencies and document the tools and commands. | A testbench that runs without an FPGA, with setup instructions. |
| 3. Prepare first-contribution issues | Choose small reset, handshake and boundary-condition tests. | Around five issues with a command to run and an expected result. |
| 4. Improve the contribution guide | Use feedback from first-time contributors to fix difficult steps. | A guide covering tests, pull requests and review. |

We will share dates once the scope and owners are agreed.
Test setup work is discussed in
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152).
See {doc}`onboarding/getting-started` for the current environment.

The v002 weight dispatcher, result packer and memory operation queue are
starting points for small verification tasks. Read their existing testbenches
and help identify additional cases to cover.

## Board and architecture development

KV260 runtime work is tracked in
[KV260 #154](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/154).
Contributors with a board can work on runtime and data transfers; RTL and
testbench work can begin by reading the sources without one.

Proposals for v003, decoding, sparsity and new workloads are welcome in
the relevant repository's issues. Simulation and board test results are
collected in {doc}`Evidence/index`, along with source revisions, tools and logs.

## Get involved

Choose a repository in {doc}`quickstart`. Use
[PCCX Roadmap](https://github.com/orgs/pccxai/projects/1) to discuss and follow
work, and the [contribution guide](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md)
to prepare a PR. We will also update the project board's dates and statuses
to match this roadmap.

For Altifigence's development tools, see the
[Digital Design Studio documentation](https://docs.altifigence.com/ide/).
[Transparency](https://pccx.ai/en/legal/transparency/) describes how PCCX
is operated. You are welcome to contribute using your preferred editor and tools.
