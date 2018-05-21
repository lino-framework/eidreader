=====
Usage
=====

Simple usage
============

eidreader is a command-line tool. Open a command prompt to try the
following commands.
    
- Run the :cmd:`eidreader` command with an empty card reader::

    $ eidreader
    {"eidreader_version": "1.0.0", "success": false, "message": "Could not find any reader with a card inserted"}

        

- Insert a Belgian eID card into your reader and run the command
  again::
    
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


Receiving data into a web application
=====================================


You are responsible for implementing a server that accepts the POST
request and processes the data.  An example of such a web server is
`Lino Avanti <http://avanti.lino-framework.org/>`__ (Hint: `install
<http://avanti.lino-framework.org/install/index.html>`__ and run a
demo server and click on the ``[Read eID card]`` link in the `Quick
links` section).


Register a custom URL schema handler
====================================

Since a web page has no permission to run local programs on a client
machine, you must register a custom URL protocol handler on every
client machine.

**On a Linux machine** you edit your :file:`mimeapps.list` file and
add the following line::

    x-scheme-handler/beid=beid.desktop;

Then you create a :file:`/usr/share/applications/beid.desktop` file
with this content::

    [Desktop Entry]
    Encoding=UTF-8
    Version=1.0
    Type=Application
    Terminal=true
    Exec=/path/to/python -m eidreader.main -l /path/to/eidreader.log %u
    Name=eidreader
    Comment=Run eidreader
    Icon=
    Categories=Application;Network;
    MimeType=x-scheme-handler/beid;
  

**On a Windows machine** you save the following text to a file named
:file:`beid.reg` and then double-click on it:

.. literalinclude:: beid.reg
    :encoding: utf-16

This will register ``beid://`` as a custom URL scheme on this machine.

**Alternative invocation** : Instead of invoking the :cmd:`eidreader`
script, you can use Python's `-m
<https://docs.python.org/3/using/cmdline.html#command-line>`__
option::

  $ python -m eidreader.main


**Use URL with custom protocol in your HTML**

Your web application should generate HTML code like this:

.. literalinclude:: caller.html

When the user clicks on that link, their browser will shortly open a
popup window on the given URL, which will cause the custom schema
handler to run :cmd:`eidreader`.


Install once, use from many clients
===================================

In a Windows network with several clients and a shared network drive
(e.g. ``F:``) you can install Python, SWIG and eidreader once to this
drive and then run :cmd:`eidreader` from any client using something
like this::

  F:\Python\python.exe -m eidreader.main
  

