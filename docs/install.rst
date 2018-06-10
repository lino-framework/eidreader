============
Installation
============

Linux
=====

Instructions for Linux users.

#. Install the eidreader script itself::

      $ apt install python3 swig
      $ pip install eidreader


#. The following steps will register ``beid://`` as a custom URL
   scheme on this machine.

#. Edit your :file:`mimeapps.list` file and
   add the following line::

     x-scheme-handler/beid=beid.desktop;

#. create a :file:`/usr/share/applications/beid.desktop` file
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
  

  

Windows
=======

Instructions for Windows users.

#. Download the file
    http://eidreader.lino-framework.org/dl/eidreader-1.0.0.7z
    to a temporary folder on your computer.
  
#. Unpack it to a folder of your choice,
    e.g. :file:`C:\eidreader`.

#. The following steps will register ``beid://`` as a custom URL
   scheme on this machine.


#. save the following text to a file named
   :file:`beid.reg`:

  .. literalinclude:: beid.reg
      :encoding: utf-16


#. Check whether the PATH in the file is the folder you chose

#. Double-click on the :file:`beid.reg` file and confirm modification
   of your registry.



To actually run eidreader, you will need to install the Belgian eID
middleware from https://eid.belgium.be/en

  
