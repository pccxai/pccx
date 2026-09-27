# PCCX(TM) — reusable AI accelerator project.
# SPDX-FileCopyrightText: 2026 Hyun Woo Kim
# SPDX-License-Identifier: Apache-2.0

"""Factual structured metadata for PCCX documentation; no ranking guarantees."""

from __future__ import annotations

import json
import html
import re
from pathlib import Path
from typing import Any

from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)

_CANONICAL_ROOT = "https://docs.pccx.ai/"


def _website_entry(app: Sphinx) -> dict[str, Any]:
    return {
        "@context": "https://schema.org", "@type": "WebSite",
        "name": "PCCX Docs", "url": app.config.html_baseurl,
        "inLanguage": app.config.language or "en",
        "publisher": {"@type": "Organization", "name": "Altifigence", "url": "https://altifigence.com/"},
        "description": "PCCX NPU architecture, reusable RTL, FPGA integration and verification documentation.",
    }


def _article_entry(app: Sphinx, pagename: str, context: dict[str, Any]) -> dict[str, Any]:
    # Title — prefer the page's own title, fall back to the project name.
    title = html.unescape(re.sub(r"<[^>]+>", "", context.get("title") or "PCCX documentation"))
    # Description — the opengraph extension computes this per-page; reuse
    # its output when present, otherwise compose a stable generic one.
    description = context.get("meta", {}).get("description") if isinstance(context.get("meta"), dict) else None
    if not description:
        description = f"{title}. PCCX architecture, implementation and verification documentation."
    # Canonical URL — conf_common sets html_baseurl; compose from it.
    page_url = f"{_CANONICAL_ROOT}{app.config.language or 'en'}/{pagename}.html"

    article = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": title,
        "name": title,
        "url": page_url,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": page_url,
        },
        "isPartOf": {
            "@type": "WebSite",
            "name": "pccx — Parallel Compute Core eXecutor",
            "url": _CANONICAL_ROOT,
        },
        "publisher": {
            "@type": "Organization",
            "name": "Altifigence",
            "url": "https://altifigence.com/",
        },
        "description": description,
        "inLanguage": app.config.language or "en",
        "license": "https://github.com/pccxai/pccx/blob/main/LICENSE",
    }
    # Build time does not establish a document publication date or authorship.
    meta = context.get("meta") if isinstance(context.get("meta"), dict) else {}
    for source, target in (("schema_date_published", "datePublished"), ("schema_date_modified", "dateModified")):
        value = str(meta.get(source, ""))
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            article[target] = value
    if meta.get("author"):
        article["author"] = {"@type": "Person", "name": meta["author"]}
    return article


def _html_page_context(app: Sphinx, pagename: str, templatename: str,
                        context: dict[str, Any], doctree) -> None:
    # Only inject on actual doc pages, not Sphinx's built-in indices.
    if templatename != "page.html":
        return

    try:
        ld_blocks = [
            _website_entry(app),
            _article_entry(app, pagename, context),
        ]
        script = (
            '<script type="application/ld+json">'
            + json.dumps(ld_blocks, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
            + "</script>"
        )
        source_root = Path(__file__).resolve().parents[1]
        for lang in ("en", "ko"):
            base = source_root if lang == "en" else source_root / "ko"
            if any((base / f"{pagename}{suffix}").is_file() for suffix in (".rst", ".md", ".ipynb")):
                script += f'<link rel="alternate" hreflang="{lang}" href="{_CANONICAL_ROOT}{lang}/{pagename}.html">'
                if lang == "en":
                    script += f'<link rel="alternate" hreflang="x-default" href="{_CANONICAL_ROOT}en/{pagename}.html">'
        # Append to the metatags slot so Furo renders it inside <head>.
        context["metatags"] = (context.get("metatags") or "") + "\n" + script
    except Exception as exc:  # pragma: no cover — extension must never block build
        logger.warning("schema_org: failed to inject JSON-LD for %s: %s",
                        pagename, exc)


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect("html-page-context", _html_page_context)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
