# -*- coding: utf-8 -*-
try:
    import setuptools
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'toxsample',
    version = '0.1',
    description = "ShiningPanda's tox sample",
    url = 'https://www.shiningpanda.com',
    author = 'ShiningPanda',
    author_email = 'developers@shiningpanda.com',
    packages = find_packages(),
)
