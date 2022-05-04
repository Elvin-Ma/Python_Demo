from distutils.core import setup


setup (name = 'llapi_pytypes',
       version = '0.4',
       author = "Biren Tech",
       packages=[''],
       package_dir={"": "lib/"},
       package_data={'': ['llapi_pytypes*.so']},
       )