from setuptools import setup
fn = 'eidreader/setup_info.py'
exec(compile(open(fn, "rb").read(), fn, 'exec'))

#from cx_Freeze import setup
#from cx_Freeze import Executable
# SETUP_INFO.update()
# options = {'build_exe': {'init_script':'Console'}} 
#includes = []  # ['queue', 'idna.idnadata', 'requests']
#SETUP_INFO.update(executables=[Executable("scripts/eidreader")])
#SETUP_INFO.update(options= {
#    'build_exe': {
#        # 'packages': ['queue', 'idna', 'requests', 'eidreader']
#        'includes': includes
#    }
#})

if __name__ == '__main__':
    setup(**SETUP_INFO)
