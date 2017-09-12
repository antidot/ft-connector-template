#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

from setuptools import setup, find_packages

with open('src/{{cookiecutter.project_slug}}/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
    assert version is not None

setup(
    name='{{cookiecutter.project_slug}}',
    description='{{cookiecutter.project_short_description}}',
    version=version,
    author='Antidot',
    author_email='support@antidot.net',
    entry_points={
        'console_scripts': [
            '{{cookiecutter.binary_name}} = {{cookiecutter.project_slug}}.filter:run',
        ]
    },
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fluid-api'
    ],
    zip_safe=True
)
