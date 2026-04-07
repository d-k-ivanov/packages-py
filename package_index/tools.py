#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import pathlib

from google import genai


def delete_from_disk(path: pathlib.Path):
    if path.is_file() or path.is_symlink():
        path.unlink()
        return
    for p in path.iterdir():
        delete_from_disk(p)
    path.rmdir()


def _get_api_key():
    return os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")


def get_short_description(term):
    api_key = _get_api_key()
    if not api_key:
        return term
    client = genai.Client(api_key=api_key)
    request = f"Write a one-line but complete description of {term} using 20 words."
    try:
        response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=request)
        return response.text.replace("\n", "") if response else term
    except Exception as e:
        print(e)
        return term


def get_short_description_package(package):
    api_key = _get_api_key()
    if not api_key:
        return package
    client = genai.Client(api_key=api_key)
    request = f"""
        Write a one-line description of {package} using no more than 20 words and versions in the package name.
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
        response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=request)
        return response.text.replace("\n", "") if response else package
    except Exception as e:
        print(e)
        return package


def get_short_description_packages(packages):
    fallback = str({package: package for package in packages})
    api_key = _get_api_key()
    if not api_key:
        return fallback
    client = genai.Client(api_key=api_key)
    request = f"""
        Generate a dictionary of one-line descriptions for each package file name in {packages} using no more than 20 words and versions in the package name.
        Use package names as keys.
        Each package file name starts with the name of a package.
        Follows the environment where the package is intended to be used.
        Pytorch3D and PyTorch are different packages.
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
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=request,
            config={"response_mime_type": "application/json"},
        )
        return response.text if response else fallback
    except Exception as e:
        print(e)
        return fallback
