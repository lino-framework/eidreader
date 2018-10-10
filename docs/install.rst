============
Installation
============

This page explains how to install eidreader on your computer.


.. contents::
   :depth: 1
   :local:



Install eidreader on Linux
==========================

Instructions for Linux users.  Windows users please skip to the next
section.

#. Install the eidreader script itself::

      $ apt install python3 swig
      $ pip install eidreader

#. Register ``beid://`` as a custom URL scheme on your machine, as
   explained in the following steps.

#. Edit your :file:`mimeapps.list` file (usually in
   :file:`~/.local/share/applications`) and add the following line::

     x-scheme-handler/beid=beid.desktop;

#. Create a :file:`/usr/share/applications/beid.desktop` file
   with this content::

    [Desktop Entry]
    Encoding=UTF-8
    Version=1.0
    Type=Application
    Terminal=false
    Exec=/path/to/python -m eidreader.main -l /path/to/eidreader.log %u
    Name=eidreader
    Comment=Run eidreader
    Icon=
    Categories=Application;Network;
    MimeType=x-scheme-handler/beid;
  

  

Install eidreader on Windows
============================

Instructions for Windows users.

1. Download the following file
   to a temporary folder on your computer:
   http://eidreader.lino-framework.org/dl/eidreader-1.0.6.zip
  
2. Unpack it to a folder of your choice,
   e.g. :file:`C:\\eidreader`.

3. Register ``beid://`` as a custom URL scheme on your machine, as
   explained in the following steps.

4. Open Notepad or a similar text editor and copy the following text
   to a new file:

  .. literalinclude:: beid.reg
      :encoding: utf-16

5. Check whether the command on the last line in the file is the
   folder you chose in step 2.

6. Save the file in a temporary folder as :file:`beid.reg`.

7. Open Windows Explorer, find the :file:`beid.reg` file, double-click
   on it and confirm modification of your registry.

8. You can now delete the file :file:`beid.reg` or keep it in case you
   want to install eidreader on other computers.
   

Test whether it worked
======================
   
How to verify whether eidreader works:   

#. To actually run eidreader, you need to install the Belgian eID
   middleware from https://eid.belgium.be/en

#. Point your browser to http://welfare-demo.lino-framework.org, and
   sign in as robin (or romain or rolf depending on your preferred
   language) and click on the :guilabel:`[Read eID card]` quicklink in
   the main screen.  The card reader will start reading (possibly
   after a confirmation asked by the middleware).  Lino will ask you
   whether you want to create a new client based on the card data.  If
   you let Lino create a new database record, you should afterwards
   delete that client if you don't want others to see the stored
   information.

  
