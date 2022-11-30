from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("kivyapp1.pyx")
)

