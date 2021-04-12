# -*- coding: utf-8 -*-
from lino.sphinxcontrib import configure ; configure(globals())

from atelier.sphinxconf import interproject
interproject.configure(globals(), 'atelier')

from eidreader.setup_info import SETUP_INFO
release = SETUP_INFO['version']
version = '.'.join(release.split('.')[:2])
# language = 'en'

project = "EIDReader"
html_title = "EIDReader"
copyright = '2018-2021 Rumma & Ko Ltd'
# extensions += ['lino.sphinxcontrib.logo']

html_context.update({
    'display_gitlab': True,
    'gitlab_user': 'lino-framework',
    'gitlab_repo': 'eidreader',
    'public_url': 'https://eidreader.lino-framework.org',
})
