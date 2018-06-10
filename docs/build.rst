==================
Build the zip file
==================

How to set up a build environment on a Windows machine:


- Install Python : Go to https://www.python.org/downloads/windows/ and
  select "Latest Python 3 Release".  Choose "Windows x86 executable
  installer" (or -64) and run it as usual with default installation
  options.
  
- Install SWIG : Go to
  http://www.swig.org/download.html
  and follow the instructions.
  
- Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
  
- pip install -e eidreader
- pip install pyinstaller

We don't recommend to use pipenv because it doesn't support -e switch
for install.

When your build environment is set up, here is how to create a
distribution file::

  i  
  pyinstaller eidreader\scripts\eidreader
  cd dist
  7z a eidreader eidreader

This creates a file :file:`eidreader.7z` in your `dist` folder.
  
 


Instructions for Windows users:

If there was no error, you can leave the command prompt open and skip
to the :doc:`usage` page.  Otherwise read on!


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
