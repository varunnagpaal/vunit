# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2015, Lars Asplund lars.anders.asplund@gmail.com

from setuptools import setup
import os


def find_all_files(directory, endings=None):
    """
    Recursively find all files within directory
    """
    result = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            ending = os.path.splitext(filename)[-1]
            if endings is None or ending in endings:
                result.append(os.path.join(root, filename))
            else:
                print("Ignoring %s" % filename)
    return result

data_files = []
data_files += find_all_files(os.path.join('vunit', 'vhdl'))
data_files += find_all_files(os.path.join('vunit', 'verilog'),
                             endings=[".v", ".sv", ".svh"])
data_files = [os.path.relpath(file_name, 'vunit') for file_name in data_files]

setup(
    name='vunit_hdl',
    version='0.48.1',
    packages=['vunit',
              'vunit.com',
              'vunit.test',
              'vunit.parsing',
              'vunit.parsing.verilog',
              'vunit.test.lint',
              'vunit.test.unit',
              'vunit.test.acceptance'],
    package_data={'vunit': data_files},
    zip_safe=False,
    url='https://github.com/LarsAsplund/vunit',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
                 'Natural Language :: English',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: POSIX :: Linux',
                 'Topic :: Software Development :: Testing'],
    author='Lars Asplund',
    author_email='lars.anders.asplund@gmail.com',
    description="VUnit is an open source unit testing framework for VHDL.",
    long_description=open('README.rst').read())  # nopep8
