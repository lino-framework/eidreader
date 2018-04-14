from setuptools import setup
fn = 'eidreader/setup_info.py'
# import os
# fn = os.path.join(
#     os.path.abspath(os.path.dirname(__file__)), 'setup_info.py')
exec(compile(open(fn, "rb").read(), fn, 'exec'))

if __name__ == '__main__':
    setup(**SETUP_INFO)
