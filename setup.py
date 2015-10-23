#!/usr/bin/env python
#-----------------------------------------------------------------------------
#
# Ivy: a lightweight software bus
# Copyright (c) 2005-2013 Sebastien Bigaret <sebastien.bigaret@telecom-bretagne.eu>
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# 3. Neither the name of its copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY  THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS  OR IMPLIED WARRANTIES, INCLUDING, BUT  NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY  AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN  NO EVENT SHALL THE COPYRIGHT  OWNER OR CONTRIBUTORS BE
# LIABLE  FOR  ANY  DIRECT,  INDIRECT,  INCIDENTAL,  SPECIAL,  EXEMPLARY,  OR
# CONSEQUENTIAL  DAMAGES  (INCLUDING,  BUT  NOT LIMITED  TO,  PROCUREMENT  OF
# SUBSTITUTE GOODS  OR SERVICES; LOSS OF  USE, DATA, OR  PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER  CAUSED AND  ON ANY THEORY  OF LIABILITY,  WHETHER IN
# CONTRACT,  STRICT LIABILITY,  OR TORT  (INCLUDING NEGLIGENCE  OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE  USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#-----------------------------------------------------------------------------

"""Ivy: a lightweight software bus

Ivy is a lightweight software bus for quick-prototyping protocols. It allows
applications to broadcast information through text messages, with a
subscription mechanism based on regular expressions.
"""
__version__="3.0"

from distutils.core import setup
#from setuptools import setup
import sys

# Instruction for PyPi found at:
# http://www.python.org/~jeremy/weblog/030924.html
classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python
Natural Language :: English
Natural Language :: French
Topic :: Software Development :: Libraries :: Python Modules
"""

doclines = __doc__.split("\n")
short_description = doclines[0]
long_description = "\n".join(doclines[2:])

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup(name="ivy-python",
      version=__version__,
      license ="BSD License",
      description=short_description,
      author="Sebastien Bigaret",
      author_email="sebastien.bigaret@telecom-bretagne.eu",
      maintainer="Sebastien Bigaret",
      maintainer_email="sebastien.bigaret@telecom-bretagne.eu",
      url="http://www.eei.cena.fr/products/ivy/products/ivy/",
      packages=['ivy', ],
      scripts=['examples/ivyprobe.py',],
      long_description = long_description,
      download_url = "http://www.eei.cena.fr/products/ivy/download/packages/ivy-python-2.2.tar.gz",
      classifiers = filter(None, classifiers.split("\n")),
     )
