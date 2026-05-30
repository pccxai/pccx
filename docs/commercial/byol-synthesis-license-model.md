---
orphan: true
---

> Draft operational policy; not legal advice; not a contract.
> Subject to qualified legal review before binding use.

# BYOL synthesis license model

This page defines the PCCX bring-your-own-license model for FPGA
synthesis and implementation tooling. The policy boundary is simple:
PCCX can orchestrate or guide a build, but the customer installs,
activates, and operates vendor FPGA tools under the customer's own
license rights.

PCCX must not own, distribute, resell, share, proxy, or inspect vendor
license secrets for AMD Vivado, Altera Quartus Prime, or other FPGA EDA
tools. Customer license files, authorization codes, portal credentials,
floating-license server addresses, and license environment variables
remain in the customer-controlled environment.

## Supported operating modes

### Local mode

Local mode keeps the toolchain and license state on the customer's
machine.

1. The customer installs Vivado, Quartus Prime, or another supported
   vendor tool on the customer's workstation or build server.
2. The customer accepts the applicable vendor EULA and activates the
   license directly with the vendor.
3. PCCX Desktop or PCCX CLI invokes the local tool through a thin
   adapter.
4. PCCX records only non-secret build state: selected vendor, tool
   version, target device, exit status, sanitized logs, and customer
   selected artifacts.

PCCX does not receive the vendor account login, authorization code,
license file, license server address, or license environment value.

### Isolated VM mode

Isolated VM mode is for customers who want PCCX cloud coordination while
keeping vendor license activation inside a customer-specific execution
environment.

1. PCCX provisions or identifies a VM dedicated to one customer.
2. The customer signs into the VM and installs the vendor toolchain.
3. The customer activates the license directly in that VM or points the
   tool at a customer-controlled floating-license server when the
   customer's vendor terms allow it.
4. PCCX sends build job metadata to the VM-side runner and receives only
   sanitized status, logs, and artifacts.

Required controls:

- one customer per VM;
- no golden image containing activated vendor tools or license files;
- no PCCX access path that copies, displays, or exports license secrets;
- encrypted VM disks and customer-specific teardown policy;
- log redaction for paths, environment values, host IDs, and license
  diagnostics that may reveal customer license data.

### Hybrid mode

Hybrid mode keeps AI planning and account coordination in PCCX cloud
while synthesis runs locally.

1. PCCX cloud manages project state, review workflow, and build
   recommendations.
2. A local PCCX client pulls a build plan and executes the vendor tool on
   the customer's machine.
3. The local client returns sanitized progress and artifacts.
4. License discovery and vendor execution never leave the local
   environment.

Hybrid mode is the default recommendation when the customer wants cloud
workflow support but does not want vendor tooling or license material in
cloud infrastructure.

## Module boundary

The BYOL module should be structured as a narrow policy and adapter
boundary:

```text
modules/byol-license/
  interfaces/
    LicenseProvider
    BitstreamRequest
    BuildResult
  core/
    policy
    orchestration
  adapters/
    xilinx-vivado-local
    xilinx-vivado-vm
    intel-quartus-local
    intel-quartus-vm
    lattice
    microchip
  ui/
    LicenseSetup
    BuildDashboard
```

`interfaces/` contains the stable contract. It must be vendor-neutral and
must not include a field for license keys, license files, authorization
codes, portal passwords, or raw license environment variables.

`core/` is pure policy and orchestration code. It validates mode,
customer consent, artifact policy, and redaction requirements. It must
reject any request that tries to upload or store a vendor license secret.

`adapters/` are the only components that know tool-specific commands,
preflight checks, and report locations. Adapters execute inside the
customer-controlled environment for local and hybrid mode, or inside the
customer-dedicated VM for isolated VM mode.

`ui/` owns user setup and build status. It should guide the customer to
the vendor's own installation and licensing flow, then run a local or VM
preflight. It should never present an upload field for vendor license
files or authorization codes.

## Interface shape

The contract should describe capability, not secrets:

```text
LicenseProvider.check()
  input: vendor, tool, mode, target_device
  output: vendor, tool, detected_version, status, checked_at

BitstreamRequest
  source_ref
  target_device
  vendor_tool
  mode
  build_profile
  artifact_policy
  customer_license_responsibility_ack
  no_vendor_license_secret_ingress_ack

BuildResult
  request_id
  status
  tool_version
  started_at
  completed_at
  sanitized_log_refs
  artifact_refs
  redaction_report
```

`LicenseProvider.check()` may report `ready`, `not_detected`,
`tool_missing`, `license_unavailable`, or `unknown`. It must not return
the content or raw location of a vendor license file or license server.

`BitstreamRequest` must include customer acknowledgements that the
customer is using only licenses they control, that vendor terms remain
the customer's responsibility, and that PCCX is not receiving vendor
license secrets.

`BuildResult` must be safe to store in PCCX systems. If a log contains a
license diagnostic, the raw log stays local and the stored copy must be
redacted first.

## User flow

1. The customer signs up for PCCX and selects a plan.
2. When a synthesis or implementation action is requested, PCCX shows a
   "license activation required" setup step.
3. The customer chooses Local, Isolated VM, or Hybrid mode.
4. PCCX shows vendor-specific setup links and local preflight commands.
5. The customer installs the vendor toolchain and activates the license
   directly with the vendor or with the customer's company license
   server.
6. PCCX runs a preflight through the selected adapter.
7. The build dashboard shows tool readiness, target device, current
   stage, sanitized logs, and artifacts.
8. Any failed license check is reported as a customer-environment action:
   install, activate, select a valid license server, or contact the
   vendor.

## UI requirements

`LicenseSetup` should include:

- mode selector: Local, Isolated VM, Hybrid;
- vendor selector: Vivado, Quartus Prime, Lattice, Microchip;
- setup checklist: install tool, accept vendor EULA, activate license,
  run preflight;
- explicit acknowledgements that the customer owns or is authorized to
  use the vendor license;
- no input for vendor account passwords, authorization codes, license
  files, or raw license server values.

`BuildDashboard` should include:

- selected mode and vendor tool;
- detected tool version;
- target device and build profile;
- build stage and exit status;
- sanitized log viewer;
- artifact list;
- redaction status;
- customer action items when the tool or license is unavailable.

The UI should avoid implying that PCCX supplies Vivado, Quartus Prime,
or vendor IP licenses. It should say that the customer is using the
customer's own vendor license in the customer's environment.

## EULA review notes

This review is a product-design summary, not a legal conclusion. The
model is designed to avoid vendor-tool resale and redistribution by
keeping the vendor relationship between the customer and the vendor.
Qualified counsel should review final customer terms before launch.

AMD's public product licensing page states that the AMD/Xilinx End User
License Agreement applies to Vivado Design Suite tools and to certain
included LogiCORE IP components. The Vivado installation guide also says
the command-line installer requires acceptance of the Xilinx EULA. The
current AMD/Xilinx EULA text states that only software items for which
the licensee has applicable authorization codes are validly licensed,
and it places responsibility for third-party licenses on the licensee.

Altera's current Quartus Prime licensing guide states that Quartus Prime
Lite supports selected devices without license files, while Quartus
Prime Pro and Standard require a paid fixed or floating license. It also
states that subscriptions are set up and managed in the Altera FPGA
Self-Service Licensing Center, where the customer can generate a
`license.dat` file. A fixed license is tied to the NIC ID of the
computer on which the software is installed.

Design conclusion for PCCX:

- Local mode is the cleanest BYOL path because the customer runs the
  vendor tool on the customer's machine.
- Isolated VM mode can be acceptable only if the VM is customer-specific
  and the customer performs activation without exposing license secrets
  to PCCX.
- Hybrid mode is acceptable when PCCX cloud only manages planning and
  status while synthesis executes locally.
- Multi-tenant shared runners, PCCX-managed vendor license pools, and
  uploaded customer license files are out of scope.

Official references:

- AMD Product Licensing:
  <https://www.amd.com/en/products/adaptive-socs-and-fpgas/intellectual-property/license.html>
- AMD Vivado release notes, installation, and licensing guide:
  <https://docs.amd.com/r/en-US/ug973-vivado-release-notes-install-license/Running-the-Installer>
- AMD/Xilinx End User License Agreement:
  <https://download.amd.com/docnav/documents/eula/end-user-license-agreement.pdf>
- Altera FPGA Software Installation and Licensing:
  <https://docs.altera.com/r/docs/683472/current>
- Quartus Prime Software License:
  <https://docs.altera.com/r/docs/683472/25.3/altera-fpga-software-installation-and-licensing/quartus-prime-software-license>
- Altera Self-Service Licensing Center workflow:
  <https://docs.altera.com/r/docs/683472/25.3/altera-fpga-software-installation-and-licensing/requesting-a-license-file-from-the-altera-fpga-self-service-licensing-center>

## Customer terms checklist

Before a commercial launch, PCCX terms should state:

- The customer is responsible for obtaining, maintaining, and complying
  with all vendor FPGA tool licenses.
- PCCX does not sell, sublicense, lease, lend, host, or distribute
  Vivado, Quartus Prime, vendor IP cores, or vendor license rights.
- PCCX does not request or store vendor license files, authorization
  codes, account credentials, or license-server secrets.
- The customer authorizes PCCX only to invoke or coordinate the selected
  toolchain in the customer-controlled environment.
- The customer must not use PCCX to bypass vendor license restrictions,
  seat limits, geographic limits, export controls, or project/IP license
  restrictions.
- Vendor EULAs and IP-license terms control the vendor tools and vendor
  IP. PCCX terms control PCCX software and services only.

## Security controls

The implementation must treat vendor license material as customer
secrets:

- block upload fields and API fields for vendor license files, license
  keys, authorization codes, and portal credentials;
- redact common license environment variables such as `LM_LICENSE_FILE`
  and vendor-specific equivalents before logs leave the build host;
- store only sanitized build logs in PCCX cloud;
- keep raw tool logs local by default;
- prevent cross-customer VM reuse unless storage has been destroyed and
  the VM has been rebuilt from a clean image;
- isolate customer build artifacts from other tenants;
- keep access logs for who initiated builds, without recording license
  values.

## Future implementation gate

No runtime adapter should be enabled until these checks pass:

- documented customer consent flow;
- adapter contract tests proving license-secret fields are rejected;
- log redaction tests for license-like environment variables and common
  vendor diagnostics;
- per-mode threat model review;
- qualified legal review of the customer terms and vendor-EULA posture.
