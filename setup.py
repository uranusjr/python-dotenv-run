#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


readme = open('README.rst').read()


setup(
    name='python-dotenv-run',
    version='0.1.3',
    description='Run command with environment populated by the .env file.',
    long_description=readme,
    author='Tzu-ping Chung',
    author_email='uranusjr@gmail.com',
    url='https://github.com/uranusjr/python-dotenv-run',
    py_modules=['dotenv_run'],
    install_requires=['click', 'python-dotenv>=0.7.0'],
    entry_points={
        'console_scripts': [
            'dotenv-run = dotenv_run:main',
        ],
    },
    license='ISC',
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
