#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pathlib
import requests

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
        return ""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Write a one-line description of {term} no more than 20 words, not using a term name in the description.")
    return response.text
