# FPGA synthesis automation guardrails

This page defines the planning boundary for FPGA synthesis automation across
the pccx Lab, Trace, and workflow surfaces. It is a guardrail note for evidence
handling and flow orchestration before hosted execution paths are enabled.

## Product boundary

pccx can prepare synthesis plans, validate evidence, and summarize tool
reports. Commercial FPGA implementation suites and cloud FPGA image flows stay
behind explicit execution boundaries: user-owned environments, approved
isolated workers, or prebuilt accelerator artifacts.

The default product shape is artifact-first:

- generate project scripts, constraints, and review packets
- run open preflight checks where the target is supported
- import simulation, timing, design-rule, waveform, and board-smoke artifacts
- classify blockers before expensive implementation work begins
- keep customer source, commercial tool access material, and raw board captures
  out of shared reference material

## Flow presets

The workflow surface should expose execution modes as separate presets instead
of one generic synthesis action.

| Preset | Purpose | Execution boundary |
| --- | --- | --- |
| Artifact-first | Generate scripts and ingest reports | Planning and artifact review |
| Open preflight | Run parser, lint, and structural checks | Open adapters only |
| Local BYOL | Prepare commands for a user-owned tool install | Explicit preview and opt-in |
| Dedicated worker | Execute in an approved isolated environment | Tenant-isolated path |
| Cloud image handoff | Prepare image-flow artifacts for a user-owned cloud account | User owns account and billing |
| Prebuilt accelerator | Analyze PCCX-owned accelerator artifacts | PCCX-owned build artifacts only |

## Preflight rules

The synthesis request should be blocked before dispatch when a required
precondition is missing.

| Rule | Blocks | Expected output |
| --- | --- | --- |
| `fpga.interface.modport_compat` | Interface names or exposed types that cannot be packaged by the selected flow | failing interface, top, and suggested wrapper action |
| `fpga.top.wrapper_required` | A typed top that cannot be consumed by the selected integration path | plain wrapper requirement |
| `fpga.ooc.final_artifact_gate` | Requesting final hardware output from an out-of-context module run | integration-stage handoff |
| `fpga.axis.single_ready_driver` | Multiple consumers driving one stream-ready signal | mux, demux, or arbitration requirement |
| `fpga.status.polling_semantics` | Host polling status exposed as a lossy event queue | latest or sticky status-register requirement |
| `fpga.timing.evidence_ladder` | Treating synthesis completion as timing closure | stage-specific timing state |
| `fpga.runtime.dma_provider_required` | Runtime test requesting physical DMA without a verified provider | provider fields or sysfs evidence |
| `fpga.artifact.source_of_truth` | Stale status files conflicting with canonical reports | canonical evidence list |
| `fpga.license.execution_boundary` | Unapproved commercial tool execution | blocked license state |
| `fpga.security.customer_artifact_policy` | Customer source or raw captures entering shared material | retention and redaction action |

## Evidence states

Do not collapse FPGA progress into a single pass/fail label. The review packet
should carry separate states for:

- parser and lint status
- simulation status
- out-of-context synthesis status
- integration status
- implementation status
- timing status
- design-rule status
- final artifact status
- runtime smoke status
- throughput evidence status

Use blocked states when evidence is absent. A successful early stage must not
be promoted beyond its own stage until final artifacts and runtime smoke
evidence are present.

## Queue model

Each synthesis request should become a job graph. The first implementation can
be planning-only, but the job shape should already match the future worker pool.

Required job fields:

- `job_id`
- `target_ref`
- `flow_preset`
- `target_part_class`
- `tool_policy`
- `artifact_policy`
- `state`
- `blocking_rules`
- `evidence_refs`

Long-running implementation stages should run only in isolated work directories
with command allowlists, timeouts, cancellation, and log redaction.

## Trace and Evolve integration

Trace should show synthesis automation as an evidence timeline with each
hardware stage labeled separately. Recommended event groups:

- `preflight`
- `simulation`
- `ooc_synthesis`
- `integration`
- `implementation`
- `timing`
- `design_rules`
- `runtime_smoke`
- `blocked`

Evolve may propose RTL or constraint candidates only when the guardrails remain
satisfied. Candidate scoring should reward timing improvement, regression
preservation, single-driver interfaces, stable host-visible status semantics,
and complete evidence. It should heavily penalize missing runtime providers,
multi-driver introductions, incomplete stage evidence, and license-boundary
violations.

## Initial review packet shape

```json
{
  "flow": "fpga_synthesis_preflight.v0",
  "state": "blocked",
  "flowPreset": "artifact-first",
  "blockingRules": [
    "fpga.ooc.final_artifact_gate",
    "fpga.runtime.dma_provider_required"
  ],
  "evidenceRequired": [
    "post_implementation_timing_report",
    "design_rule_report",
    "dma_provider"
  ]
}
```

The packet is deliberately data-only. It records requested actions and evidence
requirements while commercial execution, hardware access, source publication,
and repository mutation remain behind explicit approval boundaries.
