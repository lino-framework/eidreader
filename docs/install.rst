============
Installation
============

Linux
=====

Instructions for Linux users.

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

#. Download the following file
   to a temporary folder on your computer:
   http://eidreader.lino-framework.org/dl/eidreader-1.0.1.zip
  
#. Unpack it to a folder of your choice,
   e.g. :file:`C:\\eidreader`.

#. Register ``beid://`` as a custom URL scheme on your machine, as
   explained in the following steps.

#. Save the following text to a file named :file:`beid.reg`:

  .. literalinclude:: beid.reg
      :encoding: utf-16

#. Check whether the command in the file is the folder you chose

#. Double-click on the :file:`beid.reg` file and confirm modification
   of your registry.


How to verify whether it works:   

#. To actually run eidreader, you will need to install the Belgian eID
   middleware from https://eid.belgium.be/en

#. Point your browser to http://welfare-demo.lino-framework.org, and
   sign in as robin (or romain or rolf depending on your preferred
   language) and click on the :guilabel:`[Read eID card]` quicklink in
   the main screen.  If you let Lino create a new database record from
   your ID card, you should afterwards delete that client if you don't
   want others to see the stored information.

  
