#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="shiftscheduler",
    description="A flask & webview shiftscheduler app.",

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'shiftscheduler = shiftscheduler:entry_point'
        ]
    },

    data_files=[
        ('share/applications', ['shiftscheduler.desktop']),
        ('share/icons', ['icons/shiftscheduler.png'])
    ],

    install_requires=[
        'flask',
        'pywebview'
    ],

    version="0.10.0",
    #author="...",
    #author_email='...',
    maintainer='Udo Bauer',
    maintainer_email='knackwurstking.tux@gmail.com',
    url='',
)
