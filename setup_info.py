SETUP_INFO = dict(
    name='eidreader',
    version='0.0.1',
    install_requires=['requests', 'PyKCS11'],
    scripts=['eidreader.py'],
    description="Read data from Belgian eId card via command-line",
    license='Free BSD',
    author='Luc Saffre',
    author_email='luc@saffre-rumma.net')

SETUP_INFO.update(long_description="""\

Read data from Belgian eId card via command-line.

Write the data as a JSON dict to stdout or post it to a web server.

""")
SETUP_INFO.update(classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Natural Language :: English
Operating System :: OS Independent""".splitlines())

