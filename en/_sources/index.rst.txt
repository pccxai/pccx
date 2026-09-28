========================================
PCCX Documentation
========================================

PCCX (Parallel Compute Core eXecutor) is an open-source semiconductor
project initiated and operated by Altifigence. Explore public RTL,
verification and architecture documentation. SystemVerilog developers
can begin with :doc:`docs/quickstart`.

Project
-------

.. grid:: 1 1 2 2
   :gutter: 3 4 4 4
   :class-container: pccx-ecosystem-grid

   .. grid-item-card:: :octicon:`cpu;1.2em;sd-mr-1` v002 RTL
      :link: https://github.com/pccxai/pccx-v002
      :link-type: url

      Reusable RTL, testbenches and the Sail ISA model. Start with a small verification contribution.

   .. grid-item-card:: :octicon:`cpu;1.2em;sd-mr-1` KV260 integration
      :link: https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260
      :link-type: url

      Board integration and runtime consuming a pinned core. Board results need their own evidence.

   .. grid-item-card:: :octicon:`book;1.2em;sd-mr-1` Documentation source
      :link: https://github.com/pccxai/pccx
      :link-type: url

      The English and Korean sources and contribution guidance for this site.

   .. grid-item-card:: :octicon:`beaker;1.2em;sd-mr-1` Experimental v003
      :link: https://github.com/pccxai/pccx-v003
      :link-type: url

      v003 RTL and verification work. Source availability does not establish hardware readiness.

Contribute and verify
---------------------

.. grid:: 1 1 2 2
   :gutter: 3 4 4 4
   :class-container: pccx-toolchain-grid

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` Getting started
      :link: docs/onboarding/getting-started
      :link-type: doc

      Check what you can run today and the remaining simulation dependency.

   .. grid-item-card:: :octicon:`project-roadmap;1.2em;sd-mr-1` Contribution roadmap
      :link: docs/roadmap
      :link-type: doc

      Backlog cleanup → independent RTL test → scoped verification issues → external PR.

   .. grid-item-card:: :octicon:`verified;1.2em;sd-mr-1` Verification and evidence
      :link: docs/Evidence/index
      :link-type: doc

      Keep simulation, synthesis and execution on a board tied to their own evidence.

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` Digital Design Studio
      :link: https://docs.altifigence.com/ide/
      :link-type: url

      Optional Altifigence tooling documentation. PCCX participation does not require a particular IDE.

.. note::

   pccx-lab, SystemVerilog IDE and PCCX Launcher are discontinued.
   Removing remaining dependencies is part of :doc:`docs/roadmap`.

.. toctree::
   :maxdepth: 2
   :caption: Introduction

   docs/index
   docs/quickstart
   docs/onboarding/getting-started
   docs/Evidence/index
   docs/repo-boundaries
   docs/roadmap

.. toctree::
   :maxdepth: 1
   :caption: v002 Architecture

   docs/v002/index

.. toctree::
   :maxdepth: 1
   :caption: Target Hardware

   docs/Devices/index

.. toctree::
   :maxdepth: 1
   :caption: Archive

   docs/archive/index

.. toctree::
   :maxdepth: 1
   :caption: External links

   Digital Design Studio <https://docs.altifigence.com/ide/>
   Altifigence.com <https://altifigence.com/>
   PCCX Transparency <https://pccx.ai/en/legal/transparency/>
