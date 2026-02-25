#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup, find_packages


def get_version(package):
    init_py = open(os.path.join(package, "__init__.py"), encoding="utf-8").read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version("drf_smart_nested_parser")

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="drf_smart_nested_parser",
    version=version,
    url="https://github.com/AmirHosseinDonyaei/drf_smart_nested_parser",
    license="MIT",
    description="Smart nested parser for DRF (JSON + multipart/form-data + files)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "drf",
        "django",
        "rest framework",
        "nested parser",
        "multipart",
        "form-data",
        "json",
    ],
    author="Amir Hossein Donyaei",
    author_email="cactuspydon@example.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=4.2",
        "djangorestframework>=3.14",
    ],
)
