from setuptools import setup
fn = 'eidreader/setup_info.py'
exec(compile(open(fn, "rb").read(), fn, 'exec'))

# from cx_Freeze import setup, Executable
# SETUP_INFO.update()
# options = {'build_exe': {'init_script':'Console'}} 
# SETUP_INFO.update(executables=[Executable("scripts/eidreader")])

if __name__ == '__main__':
    setup(**SETUP_INFO)
