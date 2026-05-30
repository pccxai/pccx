# =============================================================================
# pccx — documentation build targets
#
# Convenience wrapper around sphinx-build / sphinx-autobuild for the dual
# English-Korean dual-source site. Run "make help" for the full command list.
# =============================================================================

PY             ?= python
SPHINXBUILD    ?= sphinx-build
SPHINXAUTOBLD  ?= sphinx-autobuild
SPHINXOPTS     ?=

# Source roots (per language).
EN_SRC         := .
KO_SRC         := ko

# Build output roots (kept together for a single deploy upload).
BUILD_ROOT     := _build/html
EN_OUT         := $(BUILD_ROOT)/en
KO_OUT         := $(BUILD_ROOT)/ko

# Dev server ports.
DEV_PORT_EN    := 8000
DEV_PORT_KO    := 8001

# Common flags.
STRICT         := -W --keep-going -n
AUTOBLD_FLAGS  := --re-ignore '_build' --re-ignore 'auto_plots' --open-browser


# -- Phony ------------------------------------------------------------------

.PHONY: help en ko all strict dev-en dev-ko linkcheck lint clean distclean \
        check-codes install install-dev

help:
	@echo "pccx documentation — make targets"
	@echo "  make en          Build English HTML  → $(EN_OUT)/"
	@echo "  make ko          Build Korean  HTML  → $(KO_OUT)/"
	@echo "  make all         Build both languages"
	@echo "  make strict      Build both with -W (CI mode)"
	@echo "                   (use REQUIRE_RTL=0 for docs-only work without RTL)"
	@echo "  make dev-en      Autobuild + serve EN on :$(DEV_PORT_EN)"
	@echo "  make dev-ko      Autobuild + serve KO on :$(DEV_PORT_KO)"
	@echo "  make linkcheck   Run Sphinx linkcheck builder (EN + KO)"
	@echo "  make lint        sphinx-lint + codespell"
	@echo "  make clean       Remove _build/ and auto_plots/"
	@echo "  make distclean   clean + remove codes/v002/"
	@echo "  make install     pip install -r requirements.txt"
	@echo "  make install-dev pip install -r requirements-dev.txt"


# -- Preflight --------------------------------------------------------------
#
# v002 RTL sources live in an external repo (public mirror by default).
#
# For pure documentation work in *this repo only*:
#   make lint
#   make strict REQUIRE_RTL=0
#
# For full verification with real RTL literalincludes:
#   git clone --depth 1 https://github.com/hwkim-dev/pccx-FPGA-NPU-LLM-kv260 codes/v002
#   make strict
#
# REQUIRE_RTL=1 (default) enforces the check for targets that need RTL.
# This policy applies only to the documentation repo.

REQUIRE_RTL ?= 1

check-codes:
ifeq ($(REQUIRE_RTL),1)
	@if [ ! -d "codes/v002/.git" ]; then \
	    echo "\033[33m[pccx] codes/v002 is missing.\033[0m"; \
	    echo "    For docs-only work:  make lint    or    make strict REQUIRE_RTL=0"; \
	    echo "    For full RTL verification:"; \
	    echo "        git clone --depth 1 https://github.com/hwkim-dev/pccx-FPGA-NPU-LLM-kv260 codes/v002"; \
	    exit 1; \
	fi
endif


# -- Build targets ----------------------------------------------------------

en:
ifeq ($(REQUIRE_RTL),1)
	$(MAKE) check-codes
endif
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(EN_SRC) $(EN_OUT)

ko:
ifeq ($(REQUIRE_RTL),1)
	$(MAKE) check-codes
endif
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(KO_SRC) $(KO_OUT)

all: en ko

strict: SPHINXOPTS += $(STRICT)
strict: all


# -- Dev servers ------------------------------------------------------------

dev-en:
ifeq ($(REQUIRE_RTL),1)
	$(MAKE) check-codes
endif
	$(SPHINXAUTOBLD) $(AUTOBLD_FLAGS) --port $(DEV_PORT_EN) $(EN_SRC) $(EN_OUT)

dev-ko:
ifeq ($(REQUIRE_RTL),1)
	$(MAKE) check-codes
endif
	$(SPHINXAUTOBLD) $(AUTOBLD_FLAGS) --port $(DEV_PORT_KO) $(KO_SRC) $(KO_OUT)


# -- Quality gates ----------------------------------------------------------

linkcheck:
ifeq ($(REQUIRE_RTL),1)
	$(MAKE) check-codes
endif
	$(SPHINXBUILD) -b linkcheck $(EN_SRC) _build/linkcheck/en
	$(SPHINXBUILD) -b linkcheck $(KO_SRC) _build/linkcheck/ko

lint:
	@command -v sphinx-lint >/dev/null || (echo "sphinx-lint missing; pip install -r requirements-dev.txt"; exit 1)
	sphinx-lint --enable all --disable line-too-long docs ko/docs
	@command -v codespell >/dev/null || (echo "codespell missing"; exit 1)
	codespell --skip="*.svg,*.png,*.jpg,*.jpeg,*.js,*.css,*.html,_build,auto_plots,.venv,codes,.git" \
	          --ignore-words-list="nd,ot,te,ans,hist,ue,som,sow,lod"


# -- Housekeeping -----------------------------------------------------------

clean:
	rm -rf _build auto_plots ko/auto_plots

distclean: clean
	rm -rf codes/v002


# -- Install shortcuts ------------------------------------------------------

install:
	$(PY) -m pip install -r requirements.txt

install-dev:
	$(PY) -m pip install -r requirements-dev.txt
