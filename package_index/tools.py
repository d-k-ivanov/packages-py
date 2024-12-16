#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import pathlib

import google.generativeai as genai


def delete_from_disk(path: pathlib.Path):
    if path.is_file() or path.is_symlink():
        path.unlink()
        return
    for p in path.iterdir():
        delete_from_disk(p)
    path.rmdir()


def get_short_description(term):
    if not os.getenv("GOOGLE_API_KEY"):
        return term
    model = genai.GenerativeModel("gemini-1.5-flash")
    request = f"Write a one-line but complete description of {term} no more than 20 words."
    try:
        response = model.generate_content(request)
        return response.text.replace("\n", "") if response else term
    except Exception as e:
        return term


def get_short_description_package(package):
    if not os.getenv("GOOGLE_API_KEY"):
        return package
    model = genai.GenerativeModel("gemini-1.5-flash")
    request = f"""
        Write a one-line description of {package} no more than 20 words using versions in the package name.
        Where:
            'pt' is PyTorch,
            'cpu' is CPU,
            'cu' is CUDA,
            'cp' is CPython,
            'linux' is Linux,
            'macosx' is MacOS,
            'win' is Windows,
            'amd_64' and 'x86_64' is 64-bit.
        Keep the order!
    """
    try:
        response = model.generate_content(request)
        return response.text.replace("\n", "") if response else package
    except Exception as e:
        return package


def get_short_description_packages(packages):
    if not os.getenv("GOOGLE_API_KEY"):
        return str({package: package for package in packages})
    model = genai.GenerativeModel("gemini-1.5-flash")
    request = f"""
        Generate a dictionary of one-line descriptions for each package file name in {packages} no more than 20 words using versions in the package name.
        Use package names as keys.
        Output only the dictionary in curly braces, nothing more.
        Each package file name starts with the name of a package.
        Follows the environment where the package is intended to be used.
        Pytorch3D and PyTorch3 are different packages.
        Where the abbreviations are::
            'pt' is PyTorch,
            'cpu' is CPU,
            'cu' is CUDA,
            'cp' is CPython,
            'linux' is Linux,
            'macosx' is MacOS,
            'win' is Windows,
            'amd_64' and 'x86_64' is 64-bit.
        All available abbreviations should be covered. Keep the order of abbreviation occurrences!

        Examples:
        pytorch3d-0.7.8+pt2.5.1cu118-cp311-cp311-linux_x86_64.whl - PyTorch3D 0.7.8 with PyTorch 2.5.1 and CUDA 11.8 for Python 3.11 on Linux 64-bit.
        pytorch3d-0.7.8+pt2.5.1cpu-cp312-cp312-win_amd64.whl - PyTorch3D 0.7.8 with PyTorch 2.5.1 and CPU for Python 3.12 on Windows 64-bit.
    """
    try:
        response = model.generate_content(request)
        return response.text.replace("\n", "") if response else str({package: package for package in packages})
    except Exception as e:
        return str({package: package for package in packages})
