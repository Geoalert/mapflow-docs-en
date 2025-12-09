# Mapflow Docs — quick agent guide

- Purpose: Sphinx documentation for Geoalert Mapflow; default language is English with Russian translations (see `source/locale`).
- Stack: Sphinx 4.2 with RTD theme, rst2pdf, sphinxemoji, sphinx-favicon, custom `edit_on_github`.
- Setup: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` (activate venv first if it already exists).
- Build EN only: `make -e BUILDDIR="build/docs/en" html` (or `make html`).
- Build EN+RU: `make build-all` (runs gettext + sphinx-intl, then html for both languages).
- Live preview: `sphinx-autobuild source build/autobuild` after installing `sphinx-autobuild`.
- Translations: run `make gettext` then `sphinx-intl update -p build/gettext -l ru`; edit PO files under `source/locale/<lang>/LC_MESSAGES`.
- Key sources: `source/index.rst` entrypoint, user guides in `source/userguides/`, API refs in `source/api/`, config in `source/conf.py`.
- Contribute: keep reST syntax intact, align with documented Sphinx options, avoid breaking links/assets in `_static` and `_templates`.

