---
orphan: true
---

# Getting started

Start with {doc}`../quickstart` to select a repository, inspect public RTL
and list the available testbenches. Our first participation goal is a
small SystemVerilog verification PR without requiring an FPGA.

## Current simulation blocker

**pccx-lab, SystemVerilog IDE and PCCX Launcher are discontinued.**
The v002 runner `LLM/sim/run_verification.sh` still invokes
`from_xsim_log` from `PCCX_LAB_DIR`. It attempts to build the converter
before running tests when the executable is missing. This is an execution
dependency, not just an optional trace viewer.

The KV260 wrapper `scripts/v002/use_submodule_sources.sh` delegates to
that runner through `third_party/pccx-v002` and also forwards the old
Lab directory. Removing this dependency and updating the consumer pin
are tracked through
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152).
The replacement public simulation path has not yet been validated.
Do not restore discontinued tools as part of onboarding.

## Inspect board integration when needed

```bash
git clone --recurse-submodules https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260.git
cd pccx-FPGA-NPU-LLM-kv260
git rev-parse HEAD
git submodule status
```

Record both board and core SHAs. A successful clone is not a simulation
result. The existing xsim flow requires Vivado and its simulation
libraries; no simulator-independent replacement is claimed here.
See {doc}`../reference/submodule-pin-policy` for pin review.

## Agree on one test and its result

A contributor issue should identify the target files, interface or
timing behavior, tool version, command, expected assertion or PASS/FAIL
result, raw-log location and reviewer. Check existing coverage before
adding a new testbench. Report blocked execution rather than a synthetic
PASS. Do not infer current-main success from a historical run.

Read {doc}`../v002/Verification/index` and {doc}`../Evidence/index`.
Formal-model checks live with the core under `LLM/formal/sail/`;
their results are distinct from RTL simulation and board execution.
