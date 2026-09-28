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

      KV260 board integration, runtime and board tests using the v002 core.

   .. grid-item-card:: :octicon:`book;1.2em;sd-mr-1` Documentation source
      :link: https://github.com/pccxai/pccx
      :link-type: url

      The English and Korean sources and contribution guidance for this site.

   .. grid-item-card:: :octicon:`beaker;1.2em;sd-mr-1` v003 RTL
      :link: https://github.com/pccxai/pccx-v003
      :link-type: url

      RTL design and testbenches for the v003 architecture.

Contribute and verify
---------------------

.. grid:: 1 1 2 2
   :gutter: 3 4 4 4
   :class-container: pccx-toolchain-grid

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` Getting started
      :link: docs/onboarding/getting-started
      :link-type: doc

      Choose a repository, explore the RTL and prepare your first contribution.

   .. grid-item-card:: :octicon:`project-roadmap;1.2em;sd-mr-1` Contribution roadmap
      :link: docs/roadmap
      :link-type: doc

      Follow the plans for the test environment, first issues and contribution guides.

   .. grid-item-card:: :octicon:`verified;1.2em;sd-mr-1` Verification and evidence
      :link: docs/Evidence/index
      :link-type: doc

      Find simulation and board test records, source versions and logs.

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` Digital Design Studio
      :link: https://docs.altifigence.com/ide/
      :link-type: url

      Explore Altifigence's development tools for digital design.

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
