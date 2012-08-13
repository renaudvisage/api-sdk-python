#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = []

setup(
    name="api-sdk-python",
    author="Smartling, Inc.",
    author_email="hi@smartling.com",
    description="A python library for Smartling",
    url="http://www.smartling.com",

    packages=['apisdk'],
    install_requires = install_requires,

    keywords = (
        'translation',
        'localization',
        'internationalization',
    ),
    license='LGPL3',
)