curl -fsSL -o pypy2.zip https://bitbucket.org/pypy/pypy/downloads/pypy2-v5.8.0-win32.zip
7z x pypy2.zip -oc:\
c:\python34\scripts\virtualenv.exe -p c:\pypy2-v5.8.0-win32\pypy.exe c:\vp\pypy2
pip install cython
pip install -e git+https://github.com/lxml/lxml.git#egg=lxml
