#!/usr/bin/env python
"""PyAMG: Algebraic Multigrid Solvers in Python

PyAMG is a library of Algebraic Multigrid (AMG) solvers
with a convenient Python interface.
"""

import sys
from setuptools import setup

# if sys.version_info[:2] < (2, 6) or (3, 0) <= sys.version_info[0:2]:
#     raise RuntimeError("Python version 2.6, 2.7 required.")
if sys.version_info[0] >= 3:
    import builtins
else:
    import __builtin__ as builtins

classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: X11 Applications
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: C++
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Education
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Mathematics
Topic :: Software Development :: Libraries :: Python Modules
"""

name = 'pyamg'
author = 'Nathan Bell, Luke OLson, and Jacob Schroder'
author_email = 'luke.olson@gmail.com'
maintainer = 'Luke Olson'
maintainer_email = 'luke.olson@gmail.com'
url = 'https://github.com/pyamg/pyamg'
download_url = 'https://github.com/pyamg/pyamg/releases'
doclines = __doc__.split('\n')
description = doclines[0]
long_description = '\n'.join(doclines[2:])
classifiers = [_f for _f in classifiers.split('\n') if _f]
platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix']
license = 'MIT'
major = 3
minor = 0
micro = 2
isreleased = False
version = '%d.%d.%d' % (major, minor, micro)
install_requires = ['nose', 'numpy', 'scipy']

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    classifiers=classifiers,
    #
    keywords=keywords,  #
    packages=packages,  #
    install_requires=install_requires,  #
    package_data=package_data,  #
    #
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    download_url=download_url,
    platforms=platforms,
    configuration=configuration,
    )
