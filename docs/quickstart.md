---
myst:
  html_meta:
    description lang=en: |
      Start contributing to PCCX RTL and verification: find public sources,
      check repository boundaries, understand the remaining simulation dependency,
      and prepare a focused pull request.
---

# Quickstart

PCCX welcomes developers with SystemVerilog RTL and verification experience.
Start with one module or testbench. The {doc}`roadmap` prioritizes a public,
independent test path and small, reviewable contributions.

## 1. Choose the right repository

| Work | Repository |
| --- | --- |
| Reusable v002 RTL, testbenches and Sail model | [pccx-v002](https://github.com/pccxai/pccx-v002) |
| KV260 integration, runtime and board evidence | [pccx-FPGA-NPU-LLM-kv260](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260) |
| Experimental v003 RTL | [pccx-v003](https://github.com/pccxai/pccx-v003) |
| Architecture documentation and project guidance | [pccx](https://github.com/pccxai/pccx) |

Read {doc}`v002/ISA/index` and {doc}`v002/RTL/index` for the module you
want to work on. Use each repository's contribution and license files.

## 2. Make the first local check

In Linux, WSL, or a Bash environment with Git and standard Unix tools:

```bash
git clone https://github.com/pccxai/pccx-v002.git
cd pccx-v002
bash scripts/check_repo_boundary.sh
git rev-parse HEAD
bash LLM/sim/run_verification.sh --list
```

The boundary check validates repository layout; `--list` only lists
testbench names. **Neither command simulates the RTL or proves hardware
correctness.**

**Simulation is still being made independent.** The current xsim runner
uses Vivado and calls `from_xsim_log` from the discontinued `pccx-lab`
project. This dependency can block execution before a test runs.
Do not install the retired Lab as an onboarding step.
Follow {doc}`onboarding/getting-started` and
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152)
for the removal work and supported test commands as they become available.

## 3. Prepare a focused contribution

Choose one behavior: reset, a ready/valid handshake, a boundary condition,
or an instruction decode. Check the existing testbench before proposing
new coverage. Record the source SHA, tool versions, input, expected result,
actual result and raw log. If the run is blocked, report that outcome.

Use the owning repository's issues to agree on scope and a reviewer.
The proposed first-issue set is being prepared; it is not yet a promise
that five ready-to-pick tasks are available.
See the [contribution guide](https://github.com/pccxai/pccx/blob/main/CONTRIBUTING.md).

## 4. Build a documentation change

In Linux or WSL, with Python, Make and Graphviz available:

```bash
git clone https://github.com/pccxai/pccx.git
cd pccx
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make strict REQUIRE_RTL=0
```

This builds both language trees with warnings as errors. `REQUIRE_RTL=0`
is the documented docs-only mode; it does not verify embedded RTL source.
For that check, follow the
[README](https://github.com/pccxai/pccx/blob/main/README.md) to obtain the
RTL sources and run `make strict`.
Update the corresponding English and Korean guidance together.

The production documentation is published at
[docs.pccx.ai](https://docs.pccx.ai/) through Cloudflare Pages.
A deployment check confirms publication, not RTL correctness.

## Tool status

**pccx-lab, SystemVerilog IDE and PCCX Launcher are discontinued.**
PCCX participation does not require those products or a particular IDE.
[Digital Design Studio](https://docs.altifigence.com/ide/) is an optional
Altifigence resource. The first contribution goal does not require an FPGA.

For evidence boundaries, read {doc}`Evidence/index`.
