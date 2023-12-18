# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import cloudmesh
import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = 'cloudmesh-manual'
copyright = '2023, Gregor von Laszewski'
author = 'Gregor von Laszewski'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'autoapi.extension',
    'sphinx.ext.napoleon'
]

# generate autosummary even if no references
autosummary_generate = True
autosummary_imported_members = True

google_show_class_members = True #shows all members of a class in the Methods and Attributes
google_show_inherited_class_members = True #shows all inherited members of a class
google_class_members_toctree = True #creates a Sphinx table of contents for the lists of class methods and attributes.

autoapi_python_use_implicit_namespaces = True

autodoc_default_options = {
    'members': True,
    'imported-members': True,
    'undoc-members': True,
}
autoapi_dirs = [
    '../../../cloudmesh-common/src/cloudmesh',
    '../../../cloudmesh-bar/src/cloudmesh',
    '../../../cloudmesh-bumpversion/src/cloudmesh',
    '../../../cloudmesh-catalog/src/cloudmesh',
    '../../../cloudmesh-cmd5/src/cloudmesh',
    '../../../cloudmesh-configuration/src/cloudmesh',
    '../../../cloudmesh-gpu/src/cloudmesh',
    '../../../cloudmesh-rivanna/src/cloudmesh',
    '../../../cloudmesh-sys/src/cloudmesh',
    '../../../cloudmesh-vpn/src/cloudmesh',
    '../../../cloudmesh-cc/src/cloudmesh',
    '../../../cloudmesh-ee/src/cloudmesh',
]

# autoapi_ignore = [
#     '*/tests/*.py',
#     '*/examples/*.py',
#     '*/gregor-dbtest/*.py'
# ]

html_theme = "sphinx_rtd_theme"

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

# EPUB options
epub_show_urls = 'footnote'