#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
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
    request = f"Write a one-line description of {term} no more than 20 words."
    try:
        response = model.generate_content(request)
        return response.text.replace("\n", "") if response else "Sorry, I couldn't generate a response."
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
        return response.text.replace("\n", "") if response else "Sorry, I couldn't generate a response."
    except Exception as e:
        return package
