# python packages and modules install and uninstall steps

1. build the package and modules project;

- we can directly import package name if we use __init__.py
2. the package need to have __init__.py file;

- so that we can access the modules from the package name
- use . is better, because it's a relative path
3. we need use "from . import * " in __init__.py 
4. touch and code the python module mtnModule.py
5. touch and code setup.py

# install the packages and modules
1. sudo python setup.py build
2. sudo python setup.py install

'''
the packages and modules will be packaged to a .egg file
the .egg file will be copy to:
  /usr/local/lib/python3.6/dist-packages
'''

# uninstall the packages
1. sudo python ./setup.py install --record install.txt // reinstall the packages and recode
2. sudo cat install.txt |sudo xargs rm -rf // uninstall the package

# other file
- .rst 文件使得我们可以用PYPI的格式来写具体的描述
- .in 文件使得我们可以包含其他文件




