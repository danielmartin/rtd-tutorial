# Configuration file for the Sphinx documentation builder.

import os

# -- Project information

project = 'Core SourceDocs'
copyright = '2023, Daniel Martín'
author = 'Daniel Martín'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Include the docs/ directory and all docs/ subdirectories, so that
# documentation can be next to source files.
include_patterns = ['index.md', 'docs/**', '**/docs**']

html_context = {
    'conf_py_path': '/core/'
}

def setup(app):
    # Set the source directory to the project directory, as we have
    # subfolders with documentation that we want to include as well
    # (see 'include_patterns').
    app.srcdir = os.path.abspath('..')
