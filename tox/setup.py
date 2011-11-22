# -*- coding: utf-8 -*-
import ez_setup
ez_setup.use_setuptools()
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
