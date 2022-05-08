"""Configuration file for Sphinx documentation."""

import pathlib
import sys

# -- Path setup --------------------------------------------------------------

repository_base_dir = pathlib.Path(__file__).parents[2]
source_base_dir = repository_base_dir / "pysamplelib"

# -- Project information -----------------------------------------------------

sys.path.insert(0, str(source_base_dir))

import __version__  # noqa

project = __version__.__title__
copyright = __version__.__copyright__
author = __version__.__author__

# The short X.Y.Z version:
version = __version__.__version__

# The full version, including alpha/beta/rc tags:
release = __version__.__version__

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
    ".DS_Store",
    "Thumbs.db",
    "_build",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = "alabaster"

# Paths containing custom static files (such as style sheets), relative
# to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: list[str] = []
