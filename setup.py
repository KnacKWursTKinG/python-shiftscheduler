#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="...",
    description="...",

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            '<command> = <module.path:entry_point>'
        ]
    },

    install_requires=[
        '<pip-dep>',
        '<module> @ git+https://github.com/<user>/<repo>@<branch>'
    ],

    version="0.0.1",
    author="...",
    author_email='...',
    maintainer='Udo Bauer',
    maintainer_email='...',
    url='...',
)
