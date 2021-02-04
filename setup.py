# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

# with open('README.md') as f:
#     readme = f.read()
#
# with open('LICENSE.md') as f:
#     license = f.read()

setup(
    name='IRS-Form-Scraper-and-PDF-Downloader',
    version='0.1.0',
    description='Coding challenge for Pinwheel',
    long_description='<readme>',
    author='<author>',
    author_email='<email>',
    url='https://github.com/puleri/IRS-Form-Scraper-and-PDF-Downloader',
    license='<license>',
    packages=find_packages(exclude=('tests', 'docs'))
)
