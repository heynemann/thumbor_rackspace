#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 David Mann codingninja@theiconic.com.au

from distutils.core import setup
from thumbor_hbase import __version__

setup(
    name = "thumbor_rackspace",
    packages = ["thumbor_rackspace"],
    version = __version__,
    description = "Rackspace addons for Thumbor",
    author = "David Mann",
    author_email = "ninja@codingninja.com.au",
    keywords = ["thumbor", "rackspace", "images", "cloud"],
    license = 'MIT',
    url = 'https://github.com/CodingNinja/thumbor_rackspace',
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.6',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                   'Topic :: Multimedia :: Graphics :: Presentation'
    ],
    package_dir = {"thumbor_rackspace": "thumbor_rackspace"},
    install_requires=["thumbor","pymongo", 'pyrax'],
    long_description = """\
Thumbor is a smart imaging service. It enables on-demand crop, resizing and flipping of images.
This module provides a result storage for Rackspace Cloudfiles by using the Pyrax library
"""
)
