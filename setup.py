# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import find_packages, setup

from pydriller import __doc__, __version__

requirements = Path('requirements.txt').read_text().splitlines()
test_requirements = Path('test-requirements.txt').read_text().splitlines()

setup(
    name='PyDriller',
    description='Framework for MSR',
    long_description=__doc__,
    author='Davide Spadini',
    other_authors=['Daniel Umpierrez'],
    author_email='spadini.davide@gmail.com',
    version=__version__,
    packages=find_packages('.', exclude=['tests*']),
    url='https://github.com/ishepard/pydriller',
    license='Apache License',
    package_dir={'pydriller': 'pydriller'},
    python_requires='>=3.6',
    install_requires=requirements,
    tests_require=requirements + test_requirements,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
    ]
)
