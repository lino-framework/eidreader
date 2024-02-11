=====
Usage
=====

>>> from atelier.sheller import Sheller
>>> shell = Sheller()
>>> shell("eidreader --help")  #doctest: +NORMALIZE_WHITESPACE
usage: eidreader [-h] [-l LOGFILE] [-c CFGFILE] [url]
<BLANKLINE>
Read the Belgian eID card from smart card reader and either display the data to stdout or post it to a web server. Details see https://eidreader.lino-
framework.org/usage.html
<BLANKLINE>
positional arguments:
  url
<BLANKLINE>
options:
  -h, --help            show this help message and exit
  -l LOGFILE, --logfile LOGFILE
  -c CFGFILE, --cfgfile CFGFILE


>>> shell("eidreader")  #doctest: +NORMALIZE_WHITESPACE
{"eidreader_version": "1.0.7", "success": false, "message": "Could not find any reader with a card inserted"}



Command-line usage
==================

eidreader is a command-line tool. Open a command prompt to try the following
commands.

- Run the :cmd:`eidreader` command with an empty card reader::

    $ eidreader
    {"eidreader_version": "1.0.0", "success": false, "message": "Could not find any reader with a card inserted"}


- Insert a Belgian eID card into your reader and run the command again::

    $ eidreader
    {"special_status": "0", "eidreader_country": "BE",
    "carddata_soft_mask_version": "\x01", ... "document_type": "01",
    "carddata_pkcs1_support": '!', "national_number": '...',
    "nobility": "", "success": true, "message": "OK",}


**Sending data to a web server** : Instead of displaying the data to
``stdout``, you can send it to a web server.  For this you simply
specify the destination URL as first argument::

  $ eidreader https://my.server.com/123

This will send the data to https://my.server.com/123 using a HTTP POST
request.

There is a special case: when URL starts with an additional `schema
<https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax>`__
specification (e.g. ``beid://https://foo.bar.hjk``), then the script
removes the first scheme (here ``beid://``).  So the following
invocation does the same as the previous one::

  $ eidreader beid://https://my.server.com/123

This is to support calling :cmd:`eidreader` directly as a custom URL
schema handler without needing to remove yourself the schema in your
handler definition.

**Command-line options**

-l, --logfile

-c, --cfgfile

    Load the specified config file before looking at the standard
    locations.

**Running from behind a proxy**

eidreader works from behind a proxy. It uses the `getproxies()
<https://docs.python.org/3.7/library/urllib.request.html#urllib.request.getproxies>`__
standard function for finding out the proxies configured on this
computer and forwards them to `python-requests
<http://docs.python-requests.org/en/master/user/advanced/#proxies>`__.

If the proxy requires authentication, you need to specify them in the
URL (either in the envvar or in the config file) using the
``user:pass@`` syntax.

**Config file**

eidreader also looks for a file `eidreader.ini` and reads two settings
`http_proxy` and `https_proxy` from it.  This is just another way to
specify proxies.  If a config file is found and has these settings,
then they override what `getproxies()
<https://docs.python.org/3.7/library/urllib.request.html#urllib.request.getproxies>`__
gave.

The :xfile:`eidreader.ini` file can be (1) in the current
directory, (2) in the user's home directory or (3) in the same
directory as the eidreader script.  It should look something like::

    [eidreader]
    http_proxy = http://user:pass@10.10.1.10:3128
    https_proxy = https://user:pass@10.10.1.10:1080


**Alternative invocation**

The following is no longer supported after version 1.0.7.

When invoking :cmd:`eidreader` from a script, you may prefer to use Python's `-m
<https://docs.python.org/3/using/cmdline.html#command-line>`__ option::

  $ pythonw -m eidreader.main



The web application
===================

You are responsible for implementing a server that accepts the POST requests
issued by eidreader and processes the data.

To **invoke eidreader from a browser**, you must use a ``<a href>`` tag with a
custom URL protocol.

Your web application should generate HTML code like this:

.. literalinclude:: caller.html

When the user clicks on that link, their browser will shortly open a popup
window on the given URL, which will cause the custom schema handler to run
:cmd:`eidreader`.


.. An example of such a web server is `Lino Avanti
  <http://avanti.lino-framework.org/>`__ (Hint: `install
  <http://avanti.lino-framework.org/install/index.html>`__ and run a demo server
  and click on the ``[Read eID card]`` link in the `Quick links` section).


Install once, use from many clients
===================================

In a Windows network with several clients and a shared network drive
(e.g. ``F:``) you can install Python, SWIG and eidreader once to this
drive and then run :cmd:`eidreader` from any client using something
like this::

  F:\Python\python.exe -m eidreader.main
