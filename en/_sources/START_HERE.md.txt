---
orphan: true
---

# Start here · PCCX

PCCX (Parallel Compute Core eXecutor) is an open-source semiconductor project
initiated and operated by **Altifigence**. It is currently a company-led project
and community, not an independent nonprofit foundation.

## Choose one entry point

| What you want to do | Start here | First useful result |
| --- | --- | --- |
| Understand the design | [Architecture and ISA](https://docs.pccx.ai/en/docs/v002/) | Explain one instruction or data path and its current limitations |
| Read reusable RTL | [pccx-v002](https://github.com/pccxai/pccx-v002) | Run the repository boundary check, then choose a scoped testbench |
| Reproduce board integration | [KV260 integration](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) | Record the pinned core SHA, tools and a simulation log before board work |
| Improve documentation | [Contribution guide](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md) | A focused EN/KO correction with a passing strict build |
| Explore future implementation | [pccx-v003](https://github.com/pccxai/pccx-v003) | Read the current source and smoke entrypoints; hardware readiness remains unverified |

## A first local check without a board

In Linux, macOS, WSL or a Bash environment with Git and standard Unix tools:

```bash
git clone https://github.com/pccxai/pccx-v002.git
cd pccx-v002
bash scripts/check_repo_boundary.sh
git rev-parse HEAD
```

This checks the reusable core's repository boundary. It does **not** simulate
the NPU or establish hardware correctness. For xsim, use the KV260 repository's
contribution guide; its current flow also requires Vivado and a legacy
`pccx-lab` checkout. That legacy dependency needs a reproducible public replacement
before it can be advertised as a frictionless first-contributor path.

For this documentation checkout, install `requirements.txt` in a virtual
environment, follow the README's RTL-source setup, and run `make strict`.

## What the maintainer should do next

1. **One reproducible baseline.** Start with
   [KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152):
   verify a clean contributor checkout, document required tools and replace or
   explain the legacy lab dependency. Record an exact command and expected result.
2. **Close one runtime blocker.** Continue
   [KV260 #154](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/154):
   deterministic HP0/HP1 INT4 weight packing and tests, then board smoke.
   Do not preload GEMM weights through the ACP feature-map path.
3. **Publish evidence.** Use
   [KV260 #58](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/58):
   source SHA, tool versions, commands, inputs, raw logs, expected/actual results,
   and remaining blockers. Simulation, synthesis, implementation and board
   execution are separate evidence. No model-throughput claim without measurement.
4. **Resolve rights before outreach.** Continue
   [PCCX #71](https://github.com/pccxai/pccx/issues/71): audit notices and obtain
   permission for any documentation license change. Code is Apache-2.0 where
   stated; documentation and marks currently have separate terms.

Track this work in the existing [PCCX Roadmap](https://github.com/orgs/pccxai/projects/1).
Use existing issues, assign one owner per active item and require linked evidence
before moving it to Done. v003 expansion and a future foundation are separate
decisions from this first reproducible v002 milestone.

## Which repository is authoritative?

The public `pccx` repository owns documentation. `pccx-v002` and `pccx-v003`
own reusable core sources. The KV260 repository owns board and model integration.
The private `pccx.ai` repository only publishes the project website.
The dated `v002-kv260-deploy-20260527` repository preserves deployment/debug
history and artifacts. Do not delete it before migrating and verifying unique
sources, logs, rights and provenance. It is not the current contribution entry point.

[Website](https://pccx.ai/) · [Transparency](https://pccx.ai/en/legal/transparency/)
· [Rights](LICENSE) · [Altifigence](https://altifigence.com/)
