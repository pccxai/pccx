---
orphan: true
---

# Start here · PCCX

PCCX (Parallel Compute Core eXecutor) is an open-source semiconductor project
initiated and operated by **Altifigence**. Explore the design, work on a
testbench, or help improve the documentation.

## Choose an entry point

| Interest | Start here |
| --- | --- |
| Architecture and instructions | [Architecture and ISA](https://docs.pccx.ai/en/docs/v002/) |
| v002 RTL and testbenches | [pccx-v002](https://github.com/pccxai/pccx-v002) |
| KV260 board integration and runtime | [KV260 integration](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) |
| Documentation | [Contribution guide](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md) |
| v003 RTL design and testbenches | [pccx-v003](https://github.com/pccxai/pccx-v003) |

## Explore the source

In Linux, macOS, WSL or a Bash environment with Git and standard Unix tools:

```bash
git clone https://github.com/pccxai/pccx-v002.git
cd pccx-v002
bash scripts/check_repo_boundary.sh
git rev-parse HEAD
bash LLM/sim/run_verification.sh --list
```

These commands check the repository structure and list the testbenches.
For simulation, the runner currently needs Vivado xsim and an external trace
converter. See the [setup guide](https://docs.pccx.ai/en/docs/onboarding/getting-started.html).

For documentation changes, install `requirements.txt` in a virtual environment,
follow the README's RTL-source setup, and run `make strict`.

## Upcoming work

- [Test environment and contributor setup](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152):
  simplify the simulation dependencies and document a small testbench.
- [KV260 runtime](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/154):
  HP0/HP1 INT4 weight packing and tests, followed by board testing.
- [Verification records](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/58):
  collect source commits, tool versions, commands and logs.
- [Licenses and contribution terms](https://github.com/pccxai/pccx/issues/71):
  review notices and permissions for the project's code, documentation and assets.

See the [roadmap](https://docs.pccx.ai/en/docs/roadmap.html) for priorities and
[PCCX Roadmap](https://github.com/orgs/pccxai/projects/1) for issues and discussion.

## Repository roles

The public `pccx` repository maintains documentation. `pccx-v002` and `pccx-v003`
contain the core sources; the KV260 repository maintains board and model integration.
The private `pccx.ai` repository publishes the project website.
The archived `v002-kv260-deploy-20260527` repository holds earlier deployment
and debugging records.

[Website](https://pccx.ai/) · [Transparency](https://pccx.ai/en/legal/transparency/)
· [Rights](LICENSE) · [Altifigence](https://altifigence.com/)
