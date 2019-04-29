#!/usr/bin/env python

from setuptools import setup, find_packages

import rpi

setup(
      name='PyRPi',

      version=rpi.__version__,

      description='Raspberry PI library',

      author=rpi.__author__,

      author_email=rpi.__email__,

      package_dir={'rpi' : 'rpi'},

      packages=find_packages(),

      license=rpi.__license__,

      install_requires=['RPi.GPIO'],
)
