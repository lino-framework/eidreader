==================
Build the zip file
==================

How to set up a build environment on a Windows machine:

- Install Python : Go to https://www.python.org/downloads/windows/ and select
  "Latest Python 3 Release".  Choose "Windows x86 executable installer" (or -64)
  and run it as usual with default installation options. We don't recommend to
  use pipenv because it doesn't support -e switch for install.

- Install SWIG : Go to
  https://www.swig.org/download.html
  and follow the instructions.

- Install Git. See `here <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`__
  or `here <https://github.com/git-guides/install-git>`__.

- Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build
  Tools": https://visualstudio.microsoft.com/downloads/?q=build+tools

- Get a clone of the eidreader repository. Open a terminal (:cmd:`cmd.exe`) and
  type::

    c:
    cd \
    git clone https://github.com/lino-framework/eidreader.git
    cd eidreader
    pip install -e .

- Install `PyInstaller <https://pyinstaller.org/>`__. Open a terminal
  (:cmd:`cmd.exe`) and type::

    pip install pyinstaller

When your build environment is set up, here is how to create a distribution
file::

  c:
  cd \eidreader
  git pull  # get the latest version
  pyinstaller --noconsole eidreader.py
  cd dist
  python -m zipfile -c eidreader.zip eidreader

.. 7z a eidreader eidreader

This creates a file :file:`eidreader.zip` in your `dist` folder.

How to test the packaged eidreader::

  c:
  cd \eidreader\dist
  eidreader

This should output something like::

  {"eidreader_version": "1.0.7", "success": false, "message": "Could not find any reader with a card inserted"}

When a Belgian ID card is inserted in your smart card reader, it should output
more detailed information.



.. on my machine I then finish the release by saying::

   $ cd /media/luc/01D0AAA1C6A39410/Users/kasutaja/dist
   $ cp eidreader-1.0.3.zip ~/work/eid/docs/dl/
   $ go eid
   $ inv bd pd



Troubleshooting
===============

Here is a collection of problems reported by Windows users:

- **error: command 'swig.exe' failed: No such file or directory**

  After downloading the :file:`swigwin-3.0.12.zip` file you must
  unpack it.  Did you do that?  Use your Windows Explorer to find the
  file :file:`swig.exe`.  What is the full name of the folder
  containing this file? (for example ``C:\swigwin-3.0.12``).

  Check your :envvar:`PATH` environment variable (somewhere in your
  system settings). The valu of this variable usually contains a long
  text of style ``C:\Windows\;C:\Some\Other``.  It is a list of
  folders where Windows should search for programs.  Got to the end of
  that value and add ``;C:\swigwin-3.0.12`` (don't forget the
  semicolon ";" which is the separator between folders).

  After changing your :envvar:`PATH` variable you must open a new
  command prompt window.
