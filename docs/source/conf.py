"""Configuration file for Sphinx documentation."""

import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------

# Direct Sphinx to source code in other directories, to enable autodoc.

repository_base_dir = Path(__file__).parents[2]
source_base_dir = Path(repository_base_dir, "python_library_template")

sys.path.insert(0, str(source_base_dir))

from version import __version__  # noqa

# -- Project information -----------------------------------------------------

project = "python_library_template"
copyright = "2021, Kieran Ryan"
author = "Kieran Ryan"

# The short X.Y.Z version:
version = __version__

# The full version, including alpha/beta/rc tags:
release = __version__

# -- General configuration ---------------------------------------------------

# Sphinx extension module names
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
]

# Paths containing templates, relative to this directory.
templates_path = ["_templates"]

# Patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = "alabaster"

# Paths containing custom static files (such as style sheets), relative
# to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: list[str] = []
