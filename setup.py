#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def get_version(package: str) -> str:
    version_file = os.path.join(package, "__init__.py")
    with open(version_file, encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip("\"'")
    raise RuntimeError("Unable to find version string.")


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VERSION = get_version("drf_smart_nested_parser")

with open(os.path.join(BASE_DIR, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="drf_smart_nested_parser",
    version=VERSION,
    url="https://github.com/AmirHosseinDonyaei/drf_smart_nested_parser",
    project_urls={
        "Source": "https://github.com/AmirHosseinDonyaei/drf_smart_nested_parser",
    },
    license="MIT",
    description="Smart nested parser for Django REST Framework (JSON + multipart + form-data)",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Amir Hossein Donyaei",
    author_email="cactuspydon@example.com",
    packages=find_packages(exclude=("tests*",)),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "Django>=4.2",
        "djangorestframework>=3.14",
    ],
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
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "django",
        "djangorestframework",
        "drf",
        "parser",
        "multipart",
        "nested",
        "form-data",
    ],
)
