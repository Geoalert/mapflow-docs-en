# Mapflow Docs

## Install requirements

Before start you need to install the required dependencies

### If this is your first time using this project

Create venv:

    python3 -m venv .venv

Activate the `.venv`:

    source .venv/bin/activate

Install requirements:

    pip3 install -r requirements.txt

### If you have already created `.venv` and installed dependencies

Just activate `.venv`:

    source .venv/bin/activate

**Then you can call to sphinx commands.**

## Build

To build EN docs:

    make -e BUILDDIR="build/docs/en" html

## Internatization

### Translate the docs

Translations are located in the `source/locale/<lang>/LC_MESSAGES` directory. An example of one such file, from Sphinx, index.po, is given below.

```po
#: ../../source/index.rst:6
msgid "Welcome"
msgstr "FILL HERE BY TARGET LANGUAGE"
```

Another case, msgid is multi-line text and contains reStructuredText syntax:

```po
#: ../../source/index.rst:12
msgid ""
"EO data processing and analysis – here `Mapflow <https://mapflow.ai>`_ "
"comes in game |:boom:|"
"FILL HERE BY TARGET LANGUAGE - `Mapflow <https://mapflow.ai>`_ "
"FILL HERE BY TARGET LANGUAGE |:boom:|"
```

**Please be careful not to break reST notation!**

### Update translations

If a document is updated, it is necessary to generate updated pot files and to apply differences to translated po files. In order to apply the updates from a pot file to the po file, use the sphinx-intl update command

```console
make gettext
```

```console
sphinx-intl update -p build/gettext -l ru
```

## Using autobuild

To watch docs changes immediately you can use sphinx-autobuild tool

Install sphinx-autobuild:

    pip3 install sphinx-autobuild

Run the autobuild server

    sphinx-autobuild source build/autobuild

**Only en docs will builded**
