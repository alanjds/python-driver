# Copyright 2013-2015 DataStax, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from cassandra.cython_deps import HAVE_CYTHON, HAVE_NUMPY

if HAVE_CYTHON:
    import pyximport
    pyximport.install()

try:
    import unittest2 as unittest
except ImportError:
    import unittest  # noqa

def cyimport(import_path):
    """
    Import a Cython module if available, otherwise return None
    (and skip any relevant tests).
    """
    try:
        return __import__(import_path, fromlist=[True])
    except ImportError:
        if HAVE_CYTHON:
            raise
        return None


# @cythontest
# def test_something(self): ...
cythontest = unittest.skipUnless(HAVE_CYTHON, 'Cython is not available')
numpytest  = unittest.skipUnless(HAVE_CYTHON and HAVE_NUMPY, 'NumPy is not available')
