from setuptools import setup, find_packages

setup(
    name="drf_smart_nested_parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "djangorestframework>=3.14",
    ],
    include_package_data=True,
    description="Smart nested parser for DRF (JSON + multipart + files)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AmirHosseinDonyaei/drf_smart_nested_parser",
    author="AmirHosseinDonyaei",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Framework :: Django :: Rest Framework",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)