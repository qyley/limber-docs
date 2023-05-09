# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Limber FPGA Platform'
copyright = '2023, QyLey'
author = 'QyLey'
release = '0.1'

numfig=True
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Listing %s'}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.wavedrom',
    'sphinx.ext.todo',
]

# Wavedrom
wavedrom_html_jsinline = False
render_using_wavedrompy = True

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'style_nav_header_background': '#116699'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'theme_overrides.css', # Fix wide tables in RTD theme
]



