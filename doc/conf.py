"""Configure the Sphinx documentation builder."""

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess
from pathlib import Path

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'RomiRobot'
copyright = '2024, Sterling Peet'
author = 'Sterling Peet'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'breathe',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Breathe Configuration: Breathe is the bridge between the information extracted
# from the C++ sources by Doxygen and Sphinx.
breathe_projects = {}
breathe_default_project = 'RomiRobot'

# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'

# Implement build logic on RTD servers
if read_the_docs_build:
    cwd = Path.cwd()
    builddir = cwd / 'build-cmake'
    builddir.mkdir(exist_ok=True)
    subprocess.check_call(
        ['cmake', '-DBUILD_DOCS=ON', '-DBUILD_TESTING=OFF', '../..'],  # noqa: S607
        cwd=builddir,
    )
    subprocess.check_call(
        ['cmake', '--build', '.', '--target', 'doxygen'], cwd=builddir  # noqa: S607
    )
    breathe_projects['RomiRobot'] = builddir / 'doc' / 'xml'
