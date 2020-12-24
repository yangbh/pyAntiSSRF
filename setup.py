#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

__author__ = 'mody'


with open("requirements.txt", "r") as fr:
    requires = [x.strip() for x in fr.read().splitlines() if x.strip()]

setup(
        name='pyAntiSSRF',
        version='0.0.1',
        packages=['pyAntiSSRF',],
        install_requires=requires,
        url='https://github.com/yangbh/pyAntiSSRF',
        license='',
        author='m0d9',
        author_email='0xyangbh@gmail.com',
        description='python anti ssrf by hijack requests'
)

