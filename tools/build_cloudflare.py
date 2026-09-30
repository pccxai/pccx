"""Build the same bilingual artifact for Cloudflare Workers and local checks."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_build" / "html"
for source, locale in [(".", "en"), ("ko", "ko")]:
    subprocess.run(
        [sys.executable, "-m", "sphinx", "-b", "html", "-d", str(ROOT / "_build" / "doctrees" / locale), source, str(OUTPUT / locale)],
        cwd=ROOT,
        check=True,
    )
OUTPUT.mkdir(parents=True, exist_ok=True)
(OUTPUT / ".assetsignore").write_text("**/.doctrees/**\n**/.buildinfo\n", encoding="utf-8")
(OUTPUT / "_redirects").write_text("/ /en/ 302\n/en /en/ 302\n/ko /ko/ 302\n", encoding="utf-8")
for locale in ["en", "ko"]:
    if not (OUTPUT / locale / "index.html").is_file():
        raise RuntimeError(f"Missing {locale} documentation entrypoint")
