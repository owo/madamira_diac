# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2018 Ossama W. Obeid
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import codecs
from setuptools import setup


VERSION = '0.1.0'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Natural Language :: Arabic',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Science/Research',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering',
    'Topic :: Text Processing',
    'Topic :: Text Processing :: Linguistic',
]

DESCRIPTION = ('A commandline utility for diacritizing Arabic text with'
               'MADAMIRA in server mode.')

LONG_DESCRIPTION = codecs.open('README.md', 'r', encoding='utf-8').read()

INSTALL_REQUIRES = [
    'docopt',
    'Jinja2',
    'lxml',
    'requests',
    'six'
]

setup(
    name='madamira_diac',
    version=VERSION,
    author='Ossama W. Obeid',
    author_email='oobeid@nyu.edu',
    maintainer='Ossama W. Obeid',
    maintainer_email='oobeid@nyu.edu',
    packages=['madamira_diac'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            ('madamira_diac=madamira_diac.madamira_diac:main'),
        ],
    },
    url='https://github.com/owo/CAMeL_Tools',
    license='UNLICENSED',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
)
