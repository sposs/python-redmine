import os
import sys
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.jquery']

# How to sort documented members
autodoc_member_order = 'bysource'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Python-Redmine'
project_copyright = f'{datetime.date.today().year}, Maxim Tepkeev'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'logo': 'img/logo.png',
    'github_user': 'maxtepkeev',
    'github_repo': 'python-redmine',
    'github_type': 'star',
    'github_banner': 'true',
    'show_powered_by': 'false',
    'page_width': '1008px',
    'analytics_id': 'UA-97216617-1',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Either relative to html_static_path paths or full paths (eg. https://...)
html_css_files = [
    'css/python-redmine.css'
]

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['about.html', 'navigation.html', 'searchbox.html']
}

# If false, no index is generated.
html_use_index = False

# If false, no module index is generated.
html_domain_indices = False

# If true, the reST sources are included in the HTML build as _sources/name.
html_copy_source = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'PythonRedminedoc'

# Ignore all py:class warning in nitpicky mode.
nitpick_ignore_regex = [(r'py:class', r'.*')]
