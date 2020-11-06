#!/usr/env/bin/python3

import setuptools

from mapdump.definitions import VERSION


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "mapdump",
    version = VERSION,
    author = "Ayoub Sabri, Dimitri Kokkonis",
    author_email = "sabriayoub96@gmail.com, kokkonisd@gmail.com",
    description = "A CLI tool that analyzes the memory usage of a binary via its .map file.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/sorjente/mapdump",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires = [ "click" ],
    package_data = {'mapdump': []},
    include_package_data = True,
    entry_points = {'console_scripts': [
        'mapdump = mapdump.__main__:main',
    ], },
)
