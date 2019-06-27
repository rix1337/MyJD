# -*- coding: utf-8 -*-
# MyJD
# Project by https://github.com/rix1337

import setuptools

from myjd_api.version import get_version

try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except:
    import io

    long_description = io.open('README.md', encoding='utf-8').read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="myjd_api",
    version=get_version().replace("v.", ""),
    author="rix1337",
    author_email="",
    description="A simple json interface for the MyJDownloader API to be used with Organizr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rix1337/MyJD-API",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=required,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'myjd_api = myjd_api.web:main',
        ],
    },
)
