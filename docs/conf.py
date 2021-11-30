import os
import sys

import commonmark

sys.path.insert(0, os.path.abspath('../'))

project = 'imptools'
copyright = '2021, Danijar Hafner'
author = 'Danijar Hafner'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_mock_imports = ['numpy']
autodoc_inherit_docstrings = False
autodoc_default_options = {
    'member-order': 'bysource',
    'members': True,
    'undoc-members': True,
    'special-members': '__init__',
}

html_theme = 'sphinx_rtd_theme'

def docstring(app, what, name, obj, options, lines):
  wrapped = []
  literal = False
  for line in lines:
    if line.strip().startswith(r'```'):
      literal = not literal
    if not literal:
      line = ' '.join(x.rstrip() for x in line.split('\n'))
    indent = len(line) - len(line.lstrip())
    if indent and not literal:
      wrapped.append(' ' + line.lstrip())
    else:
      wrapped.append('\n' + line.strip())
  ast = commonmark.Parser().parse(''.join(wrapped))
  rst = commonmark.ReStructuredTextRenderer().render(ast)
  lines.clear()
  lines += rst.splitlines()

def setup(app):
  app.connect('autodoc-process-docstring', docstring)
