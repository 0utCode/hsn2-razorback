#!/usr/bin/python

# Copyright (c) NASK, NCSC
# 
# This file is part of HoneySpider Network 2.1.
# 
# This is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup
from setuptools import find_packages

setup(
    name='hsn2_nugget_commons',
    version='2.0',
    description='HSN2 Nugget Commons - required for running Razorback Nuggets as HSN2 python services.',
    author='CERT Polska',
    author_email='info@cert.pl',
    packages=find_packages(),
    url='http://www.honeyspider.net/',
    license='GPL-3',
    install_requires=open('requirements.txt').read().splitlines(),
)
