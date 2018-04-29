=====
Usage
=====

Installation
============

Instructions for Linux users::

  $ apt install python3 swig
  $ pip install eidreader

Instructions for Windows users:

- Install Python : Go to https://www.python.org/downloads/windows/ and
  select "Latest Python 3 Release".  Choose "Windows x86 executable
  installer" (or -64) and run it as usual with default installation
  options.
  
- Install SWIG : Go to
  http://www.swig.org/download.html
  and follow the instructions.
  
- Open a command prompt and type::
    
    pip install eidreader

  Leave the command prompt open for the following section.

    
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


Integrating eidreader into a web application
============================================

**Alternative invocation** : Instead of invoking the :cmd:`eidreader`
script, you can use Python's `-m
<https://docs.python.org/3/using/cmdline.html#command-line>`__
option::

  $ python -m eidreader.main
  
**Sending data to a web server** : Instead of displaying the data to
``stdout``, you can send it to a web server.  For this you simply
specify the destination URL as first argument::

  $ eidreader https://my.server.com/123

This will send the data to https://my.server.com/123 using a HTTP POST
request.

Of course you are responsible for implementing the server which must
accept the POST request and process the data.  An example of such a
web server is `Lino Avanti <http://avanti.lino-framework.org/>`__
(Hint: `install
<http://avanti.lino-framework.org/install/index.html>`__ and run a
demo server and click on the ``[Read eID card]`` link in the `Quick
links` section).

There is a special case: when URL starts with an additional `schema
<https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax>`__
specification (e.g.  ``beid://https://foo.bar.hjk``), the script
removes the first scheme (here ``beid://``).  So the following
invocation does the same as the previous one::

  $ eidreader beid://https://my.server.com/123

This is to support calling :cmd:`eidreader` directly as a custom URL
schema handler without needing to remove yourself the schema in your
handler definition.


Register a custom URL protocol handler
======================================

Since a web page has no permission to run local programs on a client
machine, you must register a custom URL protocol handler on every client
machine.

**On a Linux machine** you edit your :file:`mimeapps.list` file and add
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
  

**On a Windows machine** you save the following text to a file named
:file:`beid.reg` and then double-click on it:

.. literalinclude:: beid.reg
    :encoding: utf-16

This will register ``beid://`` as a custom URL scheme on this machine.
               

**Use URL with custom protocol in your HTML**

And then your web application can generate HTML code like this:

.. literalinclude:: caller.html

When the user clicks on that link, their browser will shortly open a
popup window on the given URL, which will cause the custom schema
handler to run :cmd:`eidreader`.


Install once, use from many clients
===================================

In a Windows network with several clients and a shared network drive
(e.g. ``F:``) you can install Python, SWIG and eidreader once to this
drive and then run it from any client using something like this::

  F:\Python\python.exe -m eidreader.main
  

