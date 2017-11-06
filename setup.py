# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup
from pkg_resources import load_entry_point    
  
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('colort/colort.py').read(),
    re.M
    ).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name = "colort",
    packages = ["colort"],
    entry_points = {
        "console_scripts": ['colort = colort.colort:main']
        },
    version = version,
    description = "Python command line example package",
    long_description = long_descr,
    author_email = "justin.chernyatevich@gmail.com",
    )
