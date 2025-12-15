# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Это позволяет Sphinx найти твой код в корне проекта

project = 'Weather App'
copyright = '2025, Simonenkoa'
author = 'Simonenkoa'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'  # для поддержки Google-style docstrings
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'  # Русский язык для интерфейса документации

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Красивая тема ReadTheDocs
html_static_path = ['_static']
