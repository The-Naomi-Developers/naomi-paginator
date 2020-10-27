# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2020 Naomi-Dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup


version = '1.3'


with open('README.md') as f:
  readme = f.read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()


setup(name='naomi-paginator',
  author='Naomi-Dev',
  url='https://github.com/Naomi-Dev/naomi-paginator',
  version=version,
  packages=['naomi_paginator'],
  license='MIT',
  description='Simple Embed paginator written in Python for discord.py bots',
  long_description=readme,
  include_package_data=True,
  install_requires=requirements
)
