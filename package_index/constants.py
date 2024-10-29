#!/usr/bin/env python
# -*- coding: utf-8 -*-

## HTML Constants
HTML_PLUS = "%2B"

HTML_BEGIN = '<!DOCTYPE html>\n<html lang="en">\n'
HTML_END = "\n</html>"

HTML_HEAD = """
<head>
  <meta charset="utf-8"/>
  <meta name="pypi:repository-version" content="1.1">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Font -->
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&amp;display=swap" rel="stylesheet" type="text/css"/>

  <!-- CSS Reset -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css">

  <!-- Skeleton CSS -->
  <!-- <link crossorigin="anonymous" href="https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css" rel="stylesheet"/> -->

  <!-- Milligram CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css">

  <!-- JQuery -->
  <script src="https://code.jquery.com/jquery-latest.min.js"></script>

  <title>
    Python Package Index
  </title>
</head>
"""

HTML_BODY_CSS = """
<style>
  body {
    font-family: "Montserrat";
    padding-bottom: 64px;
  }

  code {
    font-size: 100%;
    display: inline-block !important;
    font-size: 1.3rem;
  }

  .header {
    margin-top: 6rem;
    text-align: center;
  }

  .text-header {
    text-transform: uppercase;
    font-size: 1.4rem;
    letter-spacing: .2rem;
    font-weight: 600;
  }

  .card {
    display: inline-block;
    height: auto;
    width: 100%;
    padding: 0.5rem 2rem;
    margin: 0.5rem 0.5rem;
    color: #555;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.5;
    letter-spacing: .05rem;
    text-decoration: none;
    white-space: normal;
    background-color: transparent;
    border-radius: 4px;
    border: 1px solid #bbb;
    cursor: pointer;
    box-sizing: border-box;
  }

  .card:hover {
    border-color: #9b4dca;
    color: #9b4dca;
  }

  .version {
    font-size: 1rem;
    font-style: italic;
  }

  .description {
    font-weight: 300;
  }
</style>
"""

HTML_BODY_BEGIN = '<body>\n<div class="container">'
HTML_BODY_END = "</div>\n</body>"

HTML_BODY_MAIN_PAGE_PREFIX = """
  <section class="header">
    <h2 class="title">
      Python Package Index
    </h2>
  </section>
  You can install packages with :
  <pre><code>pip install &lt;package_name&gt; --extra-index-url https://d-k-ivanov.github.io/packages-py</code></pre>
  Example :
  <pre><code>pip install pytorch3d==0.7.8+pt2.4.1cu124 --extra-index-url https://d-k-ivanov.github.io/packages-py</code></pre>
  </p>
  <hr/>
  <h4 class="text-header">
    Packages
  </h4>
"""
