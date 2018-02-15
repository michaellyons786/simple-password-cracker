# Code borrowed from https://github.com/pypa/sampleproject

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(name='simple password cracker',
      version='1.0',
      description='A toy password cracker/analysis tool',
      py_modules=['foo'],
      author_email='mylonsru@gmail.com',
      author="Michael Lyons",
      packages=['password_cracker'],
      )

