# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 17:03:42 2025

@author: Arjun
"""

from setuptools import setup, find_packages

setup(
    name="SeisPlotPy",
    version="0.2.0",  # Updated version
    py_modules=["seisplotpy"],
    install_requires=[
        "segyio>=1.9.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "seisplotpy=seisplotpy:SeismicViewerApp.main"
        ]
    },
    author="Arjun V H",
    author_email="arjunvelliyidathu@gmail.com",  # Updated email
    description="A GUI tool to view and export SEG-Y seismic data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arjun-vh/SeisPlotPy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    package_data={
        "": ["seisplotpy.ico"]  # Include icon file
    },
)