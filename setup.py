"""A setuptools-based setup module for a Python package.

See:
https://setuptools.readthedocs.io/en/latest/setuptools.html
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

import io
import re
from os import path

from setuptools import setup, find_packages

packages = find_packages()

here = path.abspath(path.dirname(__file__))

with io.open(path.join(here, 'README.rst'), 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open(path.join(here, 'znbpackage/__init__.py'), 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='znbpackage',
    version=version,
    description='A basic Python package.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True
)
