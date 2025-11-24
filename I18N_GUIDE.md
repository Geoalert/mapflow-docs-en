# Internationalization (i18n) Guide

This document explains how to work with translations in the Mapflow documentation.

## 📁 Structure

```
source/
├── locale/
│   ├── en/               # English (source language)
│   │   └── LC_MESSAGES/
│   │       ├── *.po      # English PO files (source text)
│   │       └── *.mo      # Compiled message catalogs
│   ├── ru/               # Russian
│   │   └── LC_MESSAGES/
│   │       ├── *.po      # Russian translations
│   │       └── *.mo      # Compiled message catalogs
│   └── *.pot             # Template files (auto-generated)
├── _templates/
│   └── language_selector.html  # Language switcher dropdown
└── conf.py               # Sphinx configuration with i18n settings
```

## 🚀 Quick Start

### 1. Extract Messages (When RST files are updated)

Extract translatable strings from RST files to POT template files:

```bash
make gettext
```

Or manually:
```bash
sphinx-build -b gettext source source/locale
```

### 2. Update PO Files

Update PO files for all languages (merges new strings, marks outdated ones):

```bash
make update-po
```

Or manually:
```bash
sphinx-intl update -p source/locale -l en
sphinx-intl update -p source/locale -l ru
```

### 3. Translate

Edit the `.po` files in `source/locale/[LANG]/LC_MESSAGES/` directories:

- **English PO files** (`source/locale/en/LC_MESSAGES/*.po`) contain the source text
- **Translation PO files** (e.g., `source/locale/ru/LC_MESSAGES/*.po`) need to be translated

Example PO file entry:
```po
#: ../../source/userguides/imagery_search.rst:4
msgid "Imagery search"
msgstr "Поиск изображений"
```

### 4. Build Documentation

Build all language versions:

```bash
make build-all
```

Or use the comprehensive build script:
```bash
./build_all_languages.sh
```

Or build specific languages:
```bash
# English
sphinx-build -b html source build/docs/en

# Russian
sphinx-build -b html -D language=ru source build/docs/ru
```

## 🌍 Adding a New Language

To add a new language (e.g., Spanish):

### 1. Update `source/conf.py`

Add the language code to the `languages` list:

```python
languages = ['en', 'ru', 'es']  # Added 'es' for Spanish
```

Add the language name to `html_context`:

```python
html_context = {
    'languages': [
        ('English', 'en'),
        ('Русский', 'ru'),
        ('Español', 'es'), 
    ],
    'current_language': language,
}
```

### 2. Create PO Files for the New Language

```bash
sphinx-intl update -p source/locale -l es
```

### 3. Update Build Scripts

Update `Makefile`:

```makefile
update-po: gettext
	sphinx-intl update -p $(SOURCEDIR)/locale -l en
	sphinx-intl update -p $(SOURCEDIR)/locale -l ru
	sphinx-intl update -p $(SOURCEDIR)/locale -l es  # Add this line
	@echo "PO files updated."

build-all: update-po
	@echo "Building English version..."
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/docs/en" $(SPHINXOPTS)
	@echo "Building Russian version..."
	@$(SPHINXBUILD) -b html -D language=ru "$(SOURCEDIR)" "$(BUILDDIR)/docs/ru" $(SPHINXOPTS)
	@echo "Building Spanish version..."
	@$(SPHINXBUILD) -b html -D language=es "$(SOURCEDIR)" "$(BUILDDIR)/docs/es" $(SPHINXOPTS)  # Add this
	@echo "All language versions built successfully!"
```

Update `build_all_languages.sh`:

```bash
# 3. Update Spanish PO files
echo "Step 3b: Updating Spanish PO files..."
sphinx-intl update -p source/locale -l es

# 4. Build Spanish documentation
echo "Step 6: Building Spanish documentation..."
sphinx-build -b html -D language=es source build/docs/es
```

### 4. Translate

Translate the content in `source/locale/es/LC_MESSAGES/*.po` files.

### 5. Build

```bash
./build_all_languages.sh
```

## 🛠️ Tools & Editors

### Recommended PO File Editors

- **[Poedit](https://poedit.net/)** - Cross-platform, user-friendly GUI
- **[GTranslator](https://wiki.gnome.org/Apps/Gtranslator)** - GNOME translation editor
- **[Lokalize](https://apps.kde.org/lokalize/)** - KDE translation tool
- **VS Code** with extensions:
  - "gettext" extension for .po file syntax highlighting
  - "Translation Helper" for translation assistance

### Online Tools

- **[Weblate](https://weblate.org/)** - Web-based collaborative translation
- **[Crowdin](https://crowdin.com/)** - Translation management platform

## 📝 Translation Workflow

1. **Developer updates RST files**
   ```bash
   # After editing RST files
   make gettext
   make update-po
   ```

2. **Translator receives updated PO files**
   - PO files contain new strings marked as `#, fuzzy`
   - Old strings marked as `#~ msgid` (obsolete)

3. **Translator edits PO files**
   - Translate new strings
   - Review fuzzy strings
   - Remove obsolete entries

4. **Build and test**
   ```bash
   make build-all
   # Preview at build/docs/[LANG]/index.html
   ```

5. **Commit translations**
   ```bash
   git add source/locale/
   git commit -m "Update [LANGUAGE] translations"
   ```

## 🔍 Understanding PO Files

### PO File Structure

```po
# TRANSLATOR COMMENT
#: source/file.rst:line_number
#, flags
msgid "Source text"
msgstr "Translated text"
```

### Common Flags

- `#, fuzzy` - Translation needs review (auto-generated or uncertain)
- `#, python-format` - String contains Python formatting
- `#~` - Obsolete entry (not used anymore)

### Variables and Formatting

Preserve variables and formatting:

```po
msgid "Welcome to {project} version {version}"
msgstr "Bienvenue dans {project} version {version}"
```

## 🐛 Troubleshooting

### Problem: Translations not appearing

**Solution**: Ensure MO files are compiled
```bash
sphinx-intl build
```

### Problem: Missing strings in PO files

**Solution**: Re-extract messages
```bash
make gettext
make update-po
```

### Problem: Build errors with special characters

**Solution**: Ensure UTF-8 encoding in PO files
```po
"Content-Type: text/plain; charset=UTF-8\n"
```

## 📚 Resources

- [Sphinx Internationalization](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl Documentation](https://sphinx-intl.readthedocs.io/)
- [GNU gettext Manual](https://www.gnu.org/software/gettext/manual/)
- [PO File Format Specification](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)

## 🎯 Best Practices

1. **Keep source text clear** - Write clear English in RST files
2. **Use consistent terminology** - Maintain a glossary for technical terms
3. **Preserve formatting** - Keep RST directives and inline markup
4. **Test builds** - Always test after translating
5. **Regular updates** - Update translations when RST files change
6. **Version control** - Commit PO files to track translation history
7. **Translator notes** - Add comments for context: `# Translators: This refers to...`

## 🚨 Important Notes

- **DO NOT** edit `.pot` files manually (they are auto-generated)
- **DO NOT** edit `.mo` files (they are compiled from `.po` files)
- **DO** commit `.po` files to version control
- **DO** exclude `.mo` files from git (add to `.gitignore`)
- **DO** preserve RST markup in translations

## 📊 Current Languages

- 🇬🇧 English (en) - Source language
- 🇷🇺 Russian (ru) - Active translation

To add more languages, follow the "Adding a New Language" section above.
