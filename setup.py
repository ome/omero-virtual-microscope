#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '1.1.1'


setup(name="omero-virtual-microscope",
      packages=find_packages(exclude=['ez_setup']),
      version=VERSION,
      description="Virtual Microscope OMERO.web extension application",
      long_description=read('README.rst'),
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],  # Get strings from
          # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      author='The Open Microscopy Team',
      author_email='ome-devel@lists.openmicroscopy.org.uk',
      license='AGPL-3.0',
      url="https://github.com/ome/virtual-microscope",
      download_url='https://github.com/ome/virtual-microscope/archive/v{version}.zip'.format(version=VERSION),  # NOQA
      keywords=['OMERO.web', 'plugin'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'omero-web>=5.6.0,<5.14.0',
          'Django>=1.11,<2.0',
      ],
      python_requires='>=3',
      )
