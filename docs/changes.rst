.. _eidreader.changes: 

====================
Changes in EIDReader
====================

Coming version
==============

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
