=====
Usage
=====

Installation
============

Install it with :cmd:`pip install eidreader`
    
Simple usage
============

- Run the :cmd:`eidreader` command with an empty card reader::

    $ eidreader
    {'eidreader_version': '0.0.6', 'success': False}
        

- Insert a Belgian eID card into your reader and run the command
  again::
    
    $ eidreader
    {'special_status': '0', 'eidreader_country': 'BE',
    'carddata_soft_mask_version': '\x01', ... 'document_type': '01',
    'carddata_pkcs1_support': '!', 'national_number': '...',
    'nobility': '', 'success': True}    

        
Alternative invocation
======================

Instead of invoking the :cmd:`eidreader` script, you can use Python's
`-m <https://docs.python.org/3/using/cmdline.html#command-line>`__
option::

  $ python -m eidreader.main


Sending data to a web server
============================

Instead of displaying the data to ``stdout``, you can send it to a web
server.  For this you simply specify the destination URL as first
argument::

  $ eidreader https://my.server.com/123

This will send the data to https://my.server.com/123 using a HTTP POST
request.

Of course you are responsible for implementing the server which must
accept the POST request and process the data.

There is a special case: when URL starts with an additional `schema
<https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax>`__
specification (e.g. is a string of type "beid://https://foo.bar.hjk"),
the script removes the first scheme::

  $ eidreader beid://https://my.server.com/123

This is to support calling :cmd:`eidreader` directly as a custom
protocol handler without needing to remove the schema in your handler
definition.


Integrating eidreader into a web application
============================================

Since a web page has no permission to run local programs on a client
machine, you must register a custom URL scheme handler on every client
machine.

On a Linux machine you edit your :file:`mimeapps.list` file and add
the following line::

    x-scheme-handler/beid=beid.desktop;

Then you create a :file:`/usr/share/applications/beid.desktop` file
with this content::

    [Desktop Entry]
    Encoding=UTF-8
    Version=1.0
    Type=Application
    Terminal=true
    Exec=/path/to/python -m eidreader.main %u
    Name=eidreader
    Comment=Run eidreader
    Icon=
    Categories=Application;Network;
    MimeType=x-scheme-handler/beid;
  

On a Windows machine you can save the following text to a file named
:file:`beid.reg` and then double-click on it:

.. literalinclude:: beid.reg
    :encoding: utf-16

This will register ``beid://`` as a custom URL scheme on this machine.
               

And then your web application can generate HTML code like this:

.. literalinclude:: caller.html

When the user clicks on that link, her browser will shortly open a
popup window on the given URL, which will cause the custom schema
handler to run :cmd:`eidreader`.
