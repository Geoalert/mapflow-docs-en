# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Extract translatable messages
gettext:
	@$(SPHINXBUILD) -b gettext "$(SOURCEDIR)" "$(SOURCEDIR)/locale"
	@echo "Extracting translatable messages complete."

# Update PO files for all languages
update-po: gettext
	sphinx-intl update -p $(SOURCEDIR)/locale -l en
	sphinx-intl update -p $(SOURCEDIR)/locale -l ru
	@echo "PO files updated."

# Build all language versions
build-all: update-po
	@echo "Building English version..."
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/docs/en" $(SPHINXOPTS)
	@echo "Building Russian version..."
	@$(SPHINXBUILD) -b html -D language=ru "$(SOURCEDIR)" "$(BUILDDIR)/docs/ru" $(SPHINXOPTS)
	@echo "All language versions built successfully!"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
