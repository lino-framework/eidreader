# -*- coding: utf-8 -*-
from atelier.sphinxconf import configure

configure(globals())
from lino.sphinxcontrib import configure

configure(globals())

# from rstgen.sphinxconf import interproject
# interproject.configure(globals(), 'atelier')

# from eidreader.setup_info import SETUP_INFO
# release = SETUP_INFO['version']
# version = '.'.join(release.split('.')[:2])

project = "eidreader"
html_title = "eidreader"
import datetime

copyright = '2018-{} Rumma & Ko Ltd'.format(datetime.date.today().year)
# extensions += ['lino.sphinxcontrib.logo']

html_context.update({
    'display_github': True,
    'github_user': 'lino-framework',
    'github_repo': 'eidreader',
})
