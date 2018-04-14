SETUP_INFO = dict(
    name='eidreader',
    version='0.0.2',
    install_requires=['requests', 'PyKCS11'],
    scripts=['eidreader.py'],
    description="Read data from Belgian eId card via command-line",
    license='Free BSD',
    author='Luc Saffre',
    author_email='luc@saffre-rumma.net')

SETUP_INFO.update(long_description="""\

eidreader is a command-line script which reads data from Belgian eID
card and writes the data to stdout or posts it to a web server.

- The central project homepage is
  http://eidreader.lino-framework.org
- Please report issues to
  https://github.com/lino-framework/eidreader/issues

""")
SETUP_INFO.update(classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent""".splitlines())

