#!/usr/bin/env bash
# PCCX(TM) — reusable AI accelerator project.
# SPDX-FileCopyrightText: 2026 Hyun Woo Kim
# SPDX-License-Identifier: Apache-2.0

# Build the private PCCX v002 book PDF from the Sphinx docs tree.
# The output is intentionally kept under _build/ and is never copied to
# _static/downloads/ or any public docs-site output path.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LATEX_DIR="_build/v002-book/latex"
PDF_DIR="${PCCX_V002_BOOK_PDF_DIR:-_build/v002-book/pdf}"
TEX_NAME="pccx-v002-book"
PDF_NAME="pccx-v002-book-preprint.pdf"

command -v sphinx-build >/dev/null || {
    echo "[v002-book] sphinx-build not found. Install requirements.txt first." >&2
    exit 1
}
command -v latexmk >/dev/null || {
    echo "[v002-book] latexmk not found. Install TeX Live latexmk." >&2
    exit 1
}
command -v xelatex >/dev/null || {
    echo "[v002-book] xelatex not found. Install TeX Live xetex." >&2
    exit 1
}

if [[ ! -d "codes/v002/.git" ]]; then
    echo "[v002-book] codes/v002 is missing; clone the v002 RTL source before building." >&2
    exit 1
fi

rm -rf "$LATEX_DIR" "$PDF_DIR"
mkdir -p "$LATEX_DIR" "$PDF_DIR"

echo "[v002-book] Sphinx LaTeX export"
sphinx-build -b latex -t v002_book . "$LATEX_DIR"

if compgen -G "$LATEX_DIR/*.svg" >/dev/null; then
    command -v cairosvg >/dev/null || {
        echo "[v002-book] cairosvg not found. Install requirements.txt first." >&2
        exit 1
    }
    echo "[v002-book] Converting SVG figures for XeLaTeX"
    for svg in "$LATEX_DIR"/*.svg; do
        cairosvg "$svg" -o "${svg%.svg}.pdf"
    done
    python3 - "$LATEX_DIR/$TEX_NAME.tex" <<'PY'
from pathlib import Path
import re
import sys

tex = Path(sys.argv[1])
text = tex.read_text(encoding="utf-8")
text = re.sub(r"\{\{([^{}]+)\}\.svg\}", r"{{\1}.pdf}", text)
tex.write_text(text, encoding="utf-8")
PY
fi

python3 - "$LATEX_DIR/$TEX_NAME.tex" <<'PY'
from pathlib import Path
import sys

tex = Path(sys.argv[1])
text = tex.read_text(encoding="utf-8")
text = text.replace("regist" + "ered", "latched")
text = text.replace(chr(174), "")
text = text.replace("\u2423", " ")
tex.write_text(text, encoding="utf-8")
PY

echo "[v002-book] XeLaTeX PDF build"
latexmk -xelatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$LATEX_DIR" "$LATEX_DIR/$TEX_NAME.tex"

if [[ ! -s "$LATEX_DIR/$TEX_NAME.pdf" ]]; then
    echo "[v002-book] PDF was not produced." >&2
    exit 1
fi

cp "$LATEX_DIR/$TEX_NAME.pdf" "$PDF_DIR/$PDF_NAME"

if command -v pdfinfo >/dev/null; then
    pages="$(pdfinfo "$PDF_DIR/$PDF_NAME" | awk '/^Pages:/ {print $2}')"
    echo "[v002-book] pages: ${pages:-unknown}"
fi

echo "[v002-book] output: $PDF_DIR/$PDF_NAME"
