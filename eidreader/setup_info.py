SETUP_INFO = dict(
    name='eidreader',
    version='1.0.6',
    install_requires=['requests', 'PyKCS11'],
    scripts=['scripts/eidreader'],
    packages=['eidreader'],
    description="Read data from Belgian eId card via command-line",
    license='BSD-2-Clause',
    author='Rumma & Ko Ltd',
    url="https://github.com/lino-framework/eidreader",
    author_email='info@lino-framework.org')

SETUP_INFO.update(long_description="""\

eidreader is a command-line script that reads data from Belgian eID cards and
writes the data to stdout or posts it to a web server. It is designed to be used
together with a web application that will process the data.

Not to be mixed up with its deprecated Java predecessor `eidreader
<https://github.com/lsaffre/eidreader>`__ (same project name but
another account).

- The central project homepage is https://eidreader.lino-framework.org
- Please report issues to https://github.com/lino-framework/eidreader/issues

This script was written and is maintained by Luc Saffre <luc@saffre-rumma.net>.

Thanks to Vincent Hardy (vincent.hardy.be@gmail.com)



""")
SETUP_INFO.update(classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 5 - Stable
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent""".splitlines())
