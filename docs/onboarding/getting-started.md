---
orphan: true
---

# Getting started

Choose a repository and testbench in {doc}`../quickstart`.
If you find a bug or a case worth testing, open an issue in that repository
so we can agree on the scope of a contribution.

## Simulation environment

The v002 runner, `LLM/sim/run_verification.sh`, uses Vivado xsim.
It currently also needs the `from_xsim_log` trace converter in `PCCX_LAB_DIR`,
so checking out the core repository alone may leave simulation blocked.

Work to run tests without the external converter is tracked in
[KV260 #152](https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260/issues/152).
In the meantime, `--list` shows the available testbenches, and you can
explore the module and test sources.

## Explore KV260 board integration

```bash
git clone --recurse-submodules https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260.git
cd pccx-FPGA-NPU-LLM-kv260
git rev-parse HEAD
git submodule status
```

The KV260 repository uses the core revision pinned in `third_party/pccx-v002`.
Its `scripts/v002/use_submodule_sources.sh` wrapper calls the core runner,
so it needs the environment described above. Include both board and core
commits when reporting an issue. See {doc}`../reference/submodule-pin-policy`
for how core revisions are managed.

## Choose a first test

Read an existing testbench and choose a reset, handshake or boundary-condition
case. Include the target files, behavior, command and expected result in
your issue. Share the tool version and logs from your run. If a tool fails,
its error log will help others investigate.

See {doc}`../v002/Verification/index` for the test structure and
{doc}`../Evidence/index` for existing results and log locations.
For the Sail ISA model, explore `LLM/formal/sail/` in the core repository.
