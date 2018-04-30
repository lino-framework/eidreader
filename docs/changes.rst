.. _eidreader.changes: 

====================
Changes in eidreader
====================

Coming version
==============

Version 0.0.8 (2018-04-30)
==========================

Added an `eidreader.doc_trees` attribute.  This change does not change
any functionality, it is just needed to fix a `failure when building
the docs for the Lino Book
<https://travis-ci.org/lino-framework/book/jobs/372900409>`__.

Version 0.0.7 (2018-04-18)
==========================

New command-line option ``--logfile``.


Version 0.0.6 (2018-04-14)
==========================

Fixed encoding problem of the photo file data when posting to a web
server.

Version 0.0.5 (2018-04-14)
==========================

POSTing the data to a web server failed because it was posting a
nested dict. Changed the data format of output so that it is a simple
dict.

Some data fields were missing.

# carddata_serialnumber
Version 0.0.3 (2018-04-14)
==========================

Added an explicit ``include setup_info.py`` to :file:`MANIFEST.in`
file, hoping to fix `#2
<https://github.com/lino-framework/eidreader/issues/2>`__.
(NB: problem was not fixed.


Version 0.0.2 (2018-04-14)
==========================

Added a :file:`MANIFEST.in` file, hoping to fix
`#1 <https://github.com/lino-framework/eidreader/issues/1>`__.



Version 0.0.1 (2018-04-13)
==========================

First implementation. Thanks to Vincent for first ideas, to Yves for
expanding them, to Gerd and Steve for help with further design and
implementation.
