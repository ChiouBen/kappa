#!/usr/bin/env python

from setuptools import setup, find_packages

import os

requires = [
    'boto3>=1.2.2',
    'placebo>=0.4.1',
    'click>=5.0',
    'PyYAML>=3.11'
]


setup(
    name='kappa',
    version=open(os.path.join('kappa', '_version')).read().strip(),
    description='A CLI tool for AWS Lambda developers',
    long_description=open('README.md').read(),
    author='Mitch Garnaat',
    author_email='mitch@garnaat.com',
    url='https://github.com/garnaat/kappa',
    packages=find_packages(exclude=['tests*']),
    package_data={'kappa': ['_version']},
    package_dir={'kappa': 'kappa'},
    entry_points="""
        [console_scripts]
        kappa=kappa.scripts.cli:cli
    """,
    install_requires=requires,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ),
)
