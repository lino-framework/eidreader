.. _eidreader.install:

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

#. To actually run eidreader, you will need to install the Belgian eID
   middleware from https://eid.belgium.be/en

#. Install the eidreader script itself::

      $ sudo apt install python3 swig
      $ pip install eidreader

#. Register ``beid://`` as a custom URL scheme on your machine, as
   explained in the following steps.

#. Edit your :xfile:`mimeapps.list` file and add the following line::

     x-scheme-handler/beid=beid.desktop;

   The :xfile:`mimeapps.list` file is usually in
   :file:`~/.local/share/applications` or :file:`~/.config`.  (`askubuntu
   <https://askubuntu.com/questions/957608/where-i-find-mimeapps-list>`_,
   `archlinux
   <https://wiki.archlinux.org/index.php/default_applications#MIME_types>`__)
   Run :cmd:`locate mimeapps.list` to see where it occurs.

#. Create a file :file:`/usr/share/applications/beid.desktop`
   with this content::

    [Desktop Entry]
    Encoding=UTF-8
    Version=1.0
    Type=Application
    Terminal=false
    Exec=/path/to/env/bin/eidreader -l /path/to/eidreader.log %u
    Name=eidreader
    Comment=Run eidreader
    Icon=
    Categories=Application;Network;
    MimeType=x-scheme-handler/beid;

Or if you like to play, say ``Exec=/home/joe/bin/beid.sh %u`` in above file and
then create an executable  :file:`beid.sh`::

    #!/bin/bash
    set -e
    LOGFILE=/home/joe/bin/beid.log
    date > $LOGFILE
    echo eidreader $* >> $LOGFILE
    /home/joe/virtualenvs/py3/bin/eidreader -l $LOGFILE $* 2>> $LOGFILE


Install eidreader on Windows
============================

Instructions for Windows users.

1. Download the following file
   to a temporary folder on your computer:
   https://eidreader.lino-framework.org/dl/eidreader-1.0.6.zip

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

#. Point your browser to https://weleup1.mylino.net/, and
   sign in as robin (or romain or rolf depending on your preferred
   language) and click on the :guilabel:`[Read eID card]` quicklink in
   the main screen.  When asked whether to give the site permission to open
   the beid link with eidreader, say yes.  The card reader will start
   reading.  Lino will ask you
   whether you want to create a new client based on the card data.  If
   you let Lino create a new database record, you should afterwards
   delete that client if you don't want others to see the stored
   information.



Troubleshooter
==============

"src/dyn_unix.c:34:SYS_dyn_LoadLibrary() libbeidpkcs11.so.0: cannot open shared
object file: No such file or directory"

or

"LoadLibrary() failed with error 126: The specified module could not be found."

--> you don't have the beid middleware installed.
See https://eid.belgium.be/en/linux-eid-software-installation
