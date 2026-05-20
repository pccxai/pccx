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
