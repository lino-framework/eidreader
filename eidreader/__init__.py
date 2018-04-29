# Copyright 2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
import os

SETUP_INFO = {}
fn = os.path.join(os.path.dirname(__file__), 'setup_info.py')
exec(compile(open(fn, "rb").read(), fn, 'exec'))

__version__ = SETUP_INFO['version']

doc_trees = ['docs']
intersphinx_urls = dict(docs="http://eidreader.lino-framework.org")
srcref_url = 'https://github.com/lino-framework/eidreader/blob/master/%s'

