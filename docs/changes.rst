.. _eidreader.changes:

====================
Changes in eidreader
====================

Version 1.0.8 (2024-10-25)
==========================

- eidreader now unquotes the specified URL, so your client can quote the URL in
  order to work around work around `#13
  <https://github.com/lino-framework/eidreader/issues/13>`__ (Chrome  M130 and
  later  `refuse to process
  <https://docs.google.com/document/d/1LjxHl32fE4tCKugrK_PIso7mfXQVEeoD1wSnX2y0ZU8/edit?resourcekey=0-d1gP4X2sG7GPl9mlTeptIA&tab=t.0#heading=h.a67ulu2yrl9p>`__
  custom URLs that contain two occurences of '//:')

- Added a command-line option ``--dryrun`` to make doctests more easy.


Version 1.0.7 (2024-02-11)
==========================

- eidreader should now run OOTB also on MacOS.
  Thanks to Quentin LECLER for reporting the issue and the name of the lib file:
  https://github.com/lino-framework/eidreader/issues/3

- 2022-08-17 Decode using correct charset #9
  Thanks to Bramikke (see https://github.com/lino-framework/eidreader/pull/9)


Version 1.0.6 (2018-10-10)
==========================

- Script was still failing when a config file was found.  Stupid typo
  error.

Version 1.0.5 (2018-10-02)
==========================

- More detailed logging.
- Script failed when no eidreader.ini was found or when there was no
  section "eidreader" in the file.

Version 1.0.4 (2018-10-02)
==========================

It seems that the Windows version of eidreader does not find the proxy
config.  We released this version so users can test witha config file.


- (20181001) eidreader now looks for a file `eidreader.ini` and reads
  two settings `http_proxy` and `https_proxy` from it.  This is just
  another way to specify proxies.  If a config file is found and has
  these settings, then they override what `getproxies()
  <https://docs.python.org/3.7/library/urllib.request.html#urllib.request.getproxies>`__
  gave.  If the proxy requires authentication, you still need to
  specify them (either in the envvar or in the config file).

Version 1.0.3 (2018-09-27)
==========================

- eidreader now works from behind a proxy. It uses the `getproxies()
  <https://docs.python.org/3.7/library/urllib.request.html#urllib.request.getproxies>`__
  standard function for finding out the proxies configured on this
  computer and forwards them to `python-requests
  <http://docs.python-requests.org/en/master/user/advanced/#proxies>`__.

Version 1.0.2 (2018-09-12)
==========================

- eidreader now runs without opening a console window. This is no code
  change, just added the `--noconsole
  <https://pyinstaller.readthedocs.io/en/stable/usage.html#windows-and-mac-os-x-specific-options>`__
  option when building.

Version 1.0.1 (2018-06-11)
==========================

Some internal changes for the binary Windows installer.

Version 1.0.0 (2018-05-21)
==========================

Major version bump because we optimized the format used for sending
the data to an URL: instead of posting every data field as a string,
eidreader now POSTs the card data as single field `card_data` whose
value is a dict with the same fields as before, only that it is JSON
encoded now.

We also added a new field `message`.  Until now there was only one
explanation for having `success` set to False: no card was inserted in
the reader.  But actually there are other possible explanations:
e.g. a card was there, but the user did not permit access to the
reader.  In that latter case, `message` now contains
"CKR_FUNCTION_FAILED (0x00000006)".


Version 0.0.8 (2018-04-30)
==========================

Added an `eidreader.doc_trees` attribute for compliance with Atelier.
This change does not change any functionality, it is just needed to
fix a `failure when building the docs for the Lino Book
<https://travis-ci.org/lino-framework/book/jobs/372900409>`__.


When invoked without any argument :cmd:`eidreader` now uses
:func:`json.dumps` instead of :func:`print`.  Advantage: you can now
redirect the output of :cmd:`eidreader` to a file which serves as
input for tests like those in `lino_book.projects.adg.tests
<http://www.lino-framework.org/api/lino_book.projects.adg.tests.test_beid.html>`__


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
