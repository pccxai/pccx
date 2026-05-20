# PCCX(TM) — reusable AI accelerator project.
# SPDX-FileCopyrightText: 2026 Hyun Woo Kim
# SPDX-License-Identifier: Apache-2.0

"""
pccx — English Sphinx configuration.

Thin wrapper: pulls every shared knob from :mod:`conf_common` and only
overrides language-specific values. Keep shared configuration in the
common module so EN and KO builds stay aligned.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make conf_common importable regardless of where sphinx-build is invoked from.
_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

from conf_common import *                          # noqa: F401,F403
from conf_common import (                          # noqa: F401  (explicit re-mutation)
    exclude_patterns,
    html_theme_options,
    sphinx_gallery_conf,
)


# -- Language ----------------------------------------------------------------

language = "en"


# -- Favicon ---------------------------------------------------------------

html_favicon = "_static/pccx_wordmark_favicon.ico"


# -- Exclusions -------------------------------------------------------------

# The English build's srcdir is the repo root. Exclude the Korean source tree
# and anything inside it so Sphinx doesn't double-index it.
exclude_patterns = [
    *exclude_patterns,
    "ko",
    "ko/**",
]


# -- Theme options ----------------------------------------------------------

html_theme_options = {
    **html_theme_options,
    "source_directory": "docs/",
    # Default announcement is empty — the sidebar's EN · 한국어 switch
    # handles language.  `_ext.archive_banner` selectively fills this
    # slot when the reader lands on an archived (non-active) page.
    "announcement": "",
}


# -- sphinx-gallery (paths relative to this conf) ---------------------------

sphinx_gallery_conf = {
    **sphinx_gallery_conf,
    "examples_dirs": "plots",          # <repo>/plots
    "gallery_dirs":  "auto_plots",     # <repo>/auto_plots
}


# -- Referencing & SEO ------------------------------------------------------

bibtex_bibfiles = ["refs.bib"]
sitemap_filename = "sitemap-en.xml"


def _has_sphinx_tag(name: str) -> bool:
    try:
        return tags.has(name)  # type: ignore[name-defined]
    except NameError:
        return False


if not _has_sphinx_tag("v002_book"):
    exclude_patterns = [
        *exclude_patterns,
        "book",
        "book/**",
    ]


if _has_sphinx_tag("v002_book"):
    root_doc = "book/v002/index"

    latex_engine = "xelatex"
    latex_documents = [
        (
            "book/v002/index",
            "pccx-v002-book.tex",
            "PCCX v002 Technical Architecture",
            "Altifigence",
            "manual",
        ),
    ]
    latex_additional_files = [
        "_static/cover.tex",
        "_static/cover/cover-art.jpg",
        "_static/colophon.tex",
    ]
    latex_show_urls = "footnote"
    latex_domain_indices = True
    latex_elements = {
        "papersize": "b5paper",
        "pointsize": "10pt",
        "sphinxsetup": "iconpackage=none",
        "fontpkg": r"""
\usepackage{fontspec}
\usepackage{xeCJK}
\IfFontExistsTF{Noto Serif}{\setmainfont{Noto Serif}}{\setmainfont{Latin Modern Roman}}
\IfFontExistsTF{Noto Sans}{\setsansfont{Noto Sans}}{\setsansfont{Latin Modern Sans}}
\IfFontExistsTF{Noto Sans Mono}{\setmonofont{Noto Sans Mono}}{\setmonofont{Latin Modern Mono}}
\IfFontExistsTF{Noto Sans CJK KR}{\setCJKmainfont{Noto Sans CJK KR}}{%
  \IfFontExistsTF{NanumGothic}{\setCJKmainfont{NanumGothic}}{\setCJKmainfont{UnBatang}}%
}
\IfFontExistsTF{Noto Sans CJK KR}{\setCJKsansfont{Noto Sans CJK KR}}{%
  \IfFontExistsTF{NanumGothic}{\setCJKsansfont{NanumGothic}}{\setCJKsansfont{UnBatang}}%
}
\IfFontExistsTF{Noto Sans CJK KR}{\setCJKmonofont{Noto Sans CJK KR}}{%
  \IfFontExistsTF{NanumGothicCoding}{\setCJKmonofont{NanumGothicCoding}}{\setCJKmonofont{UnBatang}}%
}
""",
        "preamble": r"""
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{3}
\usepackage{bookmark}
\usepackage{makeidx}
\usepackage{newunicodechar}
\usepackage{tikz}
\IfFontExistsTF{Pretendard}{\newfontfamily\pccxcoverfont{Pretendard}}{%
  \IfFontExistsTF{Noto Sans CJK KR}{\newfontfamily\pccxcoverfont{Noto Sans CJK KR}}{%
    \IfFontExistsTF{NanumGothic}{\newfontfamily\pccxcoverfont{NanumGothic}}{\newfontfamily\pccxcoverfont{Latin Modern Sans}}%
  }%
}
\IfFontExistsTF{Courier New}{\newfontfamily\pccxcovermono{Courier New}}{%
  \IfFontExistsTF{Noto Sans Mono}{\newfontfamily\pccxcovermono{Noto Sans Mono}}{\newfontfamily\pccxcovermono{Latin Modern Mono}}%
}
\titleformat{\chapter}[display]
  {\normalfont\pccxcovermono\bfseries\huge}
  {\chaptertitlename\ \thechapter}
  {12pt}
  {\Huge}
\makeindex
\newunicodechar{→}{\ensuremath{\rightarrow}}
\newunicodechar{←}{\ensuremath{\leftarrow}}
\newunicodechar{↔}{\ensuremath{\leftrightarrow}}
\newunicodechar{≈}{\ensuremath{\approx}}
\newunicodechar{≲}{\ensuremath{\lesssim}}
""",
        "maketitle": r"""
\input{_static/cover.tex}
\cleardoublepage
\input{_static/colophon.tex}
\cleardoublepage
\sphinxtableofcontents
\cleardoublepage
""",
        "printindex": r"\printindex",
    }
