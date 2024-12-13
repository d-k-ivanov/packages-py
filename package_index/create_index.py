#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import time
import pathlib
import requests

from constants import *
from tools import delete_from_disk, get_short_description, get_short_description_package


def normalize_pep_503(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def get_packages_dict(links_wheels):
    packages = {}
    for link_wheel in links_wheels:
        file_name = link_wheel.split("/")[-1]
        package_and_version = file_name.split(HTML_PLUS)[0]
        package, _version = package_and_version.rsplit("-", 1)

        try:
            packages[package].append(link_wheel)
        except KeyError:
            packages[package] = [link_wheel]

    return packages


def get_links(releases):
    links = []
    for release in releases.json():
        release_links = (x["browser_download_url"] for x in release["assets"])
        links.extend(release_links)

    return links


def create_main_index(packages, output_file):
    with open(output_file, "w") as f:
        f.write(HTML_BEGIN)
        f.write(HTML_HEAD)
        f.write(HTML_BODY_CSS)
        f.write(HTML_BODY_BEGIN)
        f.write(HTML_BODY_MAIN_PAGE_PREFIX)

        print("Packages in Index:")
        for package in packages:
            print(f"\t{package}")
            f.write(f'<a class="card" href="{normalize_pep_503(package)}/">{package}<br/><span class="description">{get_short_description(package)}</span></a><br>\n')
            time.sleep(2)

        f.write(HTML_BODY_END)
        f.write(HTML_END)


def create_package_index(package, links_wheels, output_file):
    with open(output_file, "w") as f:
        f.write(HTML_BEGIN)
        f.write(HTML_HEAD)
        f.write(HTML_BODY_CSS)
        f.write(HTML_BODY_BEGIN)

        print(f"Wheels in {package}:")
        file_names = set()
        for link_wheel in links_wheels:
            file_name = link_wheel.rsplit("/", 1)[1].replace(HTML_PLUS, "+")
            if file_name not in file_names:
                print(f"\t{file_name}")
                file_names.add(file_name)
                f.write(f'<a class="card" href="{link_wheel}">{file_name}<br/><span class="description">{get_short_description_package(file_name)}</span></a><br>\n')
                time.sleep(2)

        f.write(HTML_BODY_END)
        f.write(HTML_END)


def create_pep_503_index(packages_dict, output_dir: pathlib.Path):
    packages = sorted(packages_dict.keys(), key=str.lower)

    create_main_index(packages, output_dir / "index.html")

    for package in packages:
        package_dir = output_dir / normalize_pep_503(package)
        package_dir.mkdir()
        create_package_index(package, packages_dict[package], package_dir / "index.html")


def main():
    github_token = os.environ["GITHUB_TOKEN"]
    repository = os.environ["REPO_NAME"]
    output_dir = pathlib.Path("_site")

    headers = {"Authorization": "token " + github_token}
    releases = requests.get(f"https://api.github.com/repos/{repository}/releases", headers=headers)

    links = get_links(releases)
    links_wheels = [x for x in links if x.endswith(".whl")]
    packages_dict = get_packages_dict(links_wheels)

    if os.path.isdir(output_dir):
        delete_from_disk(output_dir)

    output_dir.mkdir()
    create_pep_503_index(packages_dict, output_dir)


if __name__ == "__main__":
    main()
