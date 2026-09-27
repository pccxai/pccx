# Contributing to PCCX

Thanks for your interest in PCCX.

PCCX currently welcomes contributions in:

- Documentation improvements
- Localization
- Architecture note reviews
- Examples and diagrams

For first-time contributors, please check issues labeled `good first issue` or `help wanted`.

Before opening a pull request:

1. Keep changes focused and small.
2. Explain why the change is useful.
3. Install the repository git hooks once:

   ```bash
   git config core.hooksPath .githooks
   ```

4. Run `make strict` before every commit. The local pre-commit hook runs the
   same command and blocks the commit when Sphinx emits warnings or errors.
5. For documentation updates, verify that the affected page builds correctly.
6. If you are unsure, open an issue first.

PCCX is currently research-oriented and evolves quickly, so design discussions are welcome.


## Operator, rights and tools

PCCX is initiated and operated by Altifigence. See
[Transparency](https://pccx.ai/en/legal/transparency/) for decisions, commercial
interests, funding and the planned developer support program.

Check [LICENSE](LICENSE) and any file-level notice before contributing.
Code and documentation do not share a blanket license. Submit only work
you are authorized to provide, preserve attribution, and identify third-party
material. Inclusion does not itself assign your ownership to Altifigence.

The [DCO](DCO.md) and CLA placeholder remain drafts, not new requirements.
You may contribute using other tools without purchasing Altifigence products,
joining a support program or providing a positive review. The Altifigence
Open Source Program is in preparation; eligibility and limits will be
announced separately when available.
