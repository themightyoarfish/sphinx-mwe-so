import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../'))


project = 'test'
copyright = ''
author = ''

version = ''
release = '0'

extensions = [
    'sphinx.ext.autodoc',
]

source_suffix = '.rst'
master_doc = 'index'
