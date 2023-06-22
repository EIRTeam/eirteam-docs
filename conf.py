# -*- coding: utf-8 -*-
#
# EIRTeam documentation build configuration file

import sys
import os

# -- Project information -----------------------------------------------------

project = "EIRTeam Modules"
copyright = "2023-present, Álex Román (EIRTeam) (CC-BY 3.0)"
author = "Álex Román (EIRTeam)"

version = os.getenv("READTHEDOCS_VERSION", "latest")
release = version

godot_version = "latest"
godot_docs_url = "https://docs.godotengine.org/en/%s/" % (godot_version)

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.imgmath",
    "sphinx_tabs.tabs",
]

templates_path = ["_templates"]
source_suffix = [".rst", ".md"]

html_js_files = [
    "js/custom.js?6", # Increment the number at the end when the file changes to bust the cache.
]

master_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", ".github"]

# Syntax highlighting
from sphinx.highlighting import lexers
from pygments.lexers import GDScriptLexer

lexers["gdscript"] = GDScriptLexer()
pygments_style = "sphinx"
highlight_language = "gdscript"

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_logo = "img/logo.png"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    "logo_only": True,
    "display_version": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#4e1537",  # Match sidebar background.
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

# VCS options: https://docs.readthedocs.io/en/latest/vcs.html#github
html_context = {
    "display_github": True,  # Integrate GitHub
    "github_user": "EIRTeam",  # Username
    "github_repo": "eirteam-docs",  # Repo name
    "github_version": version,  # Version
    "conf_py_path": "/",  # Path in the checkout to the docs root
    "godot_is_latest": False,
}

html_static_path = ["_static"]
html_extra_path = ["robots.txt"]
# These paths are either relative to html_static_path
# or fully qualified paths (e.g. https://...)
html_css_files = [
    "css/custom.css?10", # Increment the number at the end when the file changes to bust the cache.
]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Eirteammodules"

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

intersphinx_mapping = {godot_docs_url: None}
