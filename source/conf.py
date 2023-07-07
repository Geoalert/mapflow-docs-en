# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('_ext'))


# -- Project information -----------------------------------------------------

project = 'Mapflow'
copyright = '2021-2023, Geoalert'
author = 'Geoalert'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'edit_on_github',
  'sphinxemoji.sphinxemoji',
  'sphinx_rtd_theme',
  'rst2pdf.pdfbuilder',
  'sphinxnotes.strike',
  'sphinx_favicon'
]

pdf_documents = [
  ('userguides/get_started', u'get_started', u'Getting Started with Mapflow UI', u'Geoalert'),
  ('userguides/pipelines', u'pipelines', u'Mapping models pipelines', u'Geoalert'),
  ('userguides/prices', u'prices', u'Mapflow tariffs', u'Geoalert')
]


favicons = [
   {
      "sizes": "16x16",
      "href": "https://mapflow.ai/favicon/favicon-16x16.png",
   },
   {
      "sizes": "32x32",
      "href": "https://mapflow.ai/favicon/favicon-32x32.png",
   },
   {
      "rel": "apple-touch-icon",
      "sizes": "180x180",
      "href": "apple-touch-icon.png",  # use a local file in _static
   },
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

version = '0'

html_theme_options = {
    'display_version': False,
    'logo_only': True
}
html_logo = '_static/logo_mapflow.png'

# To show the same sidebar for each page
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['globals.css']

# -- Options for Edit on github ----------------------------------------------
edit_on_gitlab_user = 'geoalert'
edit_on_github_branch = 'main/source'

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.