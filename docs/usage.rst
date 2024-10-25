=====
Usage
=====


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

    Log activity to the specified log file.

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

**Alternative invocation**

The following alternative invocation is no longer supported after version 1.0.7.

When invoking :cmd:`eidreader` from a script, you may prefer to use Python's `-m
<https://docs.python.org/3/using/cmdline.html#command-line>`__ option::

  $ pythonw -m eidreader.main



Config file
===========

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


Environment variable
====================

.. envvar:: PYKCS11LIB

  The name of the PyKCS11 library to load.




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

  F:\Python\bin\eidreader.exe


Don't read
==========


..
  NB The following snippet needs an ellipsis because the text "Details see
  https://eidreader.lino-framework.org/usage.html" sometimes gets wrapped at the
  dash in the link, which causes NORMALIZE_WHITESPACE to not "work as expected"

>>> from atelier.sheller import Sheller
>>> shell = Sheller()
>>> shell("eidreader --help")  #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
usage: eidreader [-h] [-l LOGFILE] [-c CFGFILE] [-d] [url]
<BLANKLINE>
Read the Belgian eID card from smart card reader and either display the data to stdout or post it to a web server. Details see https://eidreader.lino-framework.org/usage.html
<BLANKLINE>
positional arguments:
  url                   Where to POST data to.
<BLANKLINE>
options:
  -h, --help            show this help message and exit
  -l LOGFILE, --logfile LOGFILE
                        Log activity to the specified file.
  -c CFGFILE, --cfgfile CFGFILE
                        Read additional config from the specified file.
  -d, --dryrun          Don't actually do anything.

>>> shell("eidreader")  #doctest: +NORMALIZE_WHITESPACE
{"eidreader_version": "1.0.8", "success": false, "message": "Could not find any reader with a card inserted"}

>>> shell("eidreader -d beid://https//xxxxxx.xxxx/receivedata.php?id=123456")  #doctest: +ELLIPSIS
Invoked as .../eidreader -d beid://https//xxxxxx.xxxx/receivedata.php?id=123456
Got data {"eidreader_version": "1.0.8", "success": false, "message": "Dry run, didn't try to read card data."}
getproxies() returned {}
Load config from ['eidreader.ini', ...]
Using proxies: {}
Would POST data to beid://https//xxxxxx.xxxx/receivedata.php?id=123456

Version 1.0.8 unquotes the specified URL in order to work around `#13
<https://github.com/lino-framework/eidreader/issues/13>`__:

>>> shell("eidreader -d beid%3A//https//xxxxxx.xxxx/receivedata.php%3Fid%3D123456%26date%3D2024-10-24")  #doctest: +ELLIPSIS
Invoked as .../eidreader -d beid%3A//https//xxxxxx.xxxx/receivedata.php%3Fid%3D123456%26date%3D2024-10-24
Got data {"eidreader_version": "1.0.8", "success": false, "message": "Dry run, didn't try to read card data."}
getproxies() returned {}
Load config from ['eidreader.ini', ...]
Using proxies: {}
Would POST data to beid://https//xxxxxx.xxxx/receivedata.php?id=123456&date=2024-10-24
