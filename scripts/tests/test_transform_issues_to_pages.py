#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tempfile

tmp_dir = tempfile.TemporaryDirectory()


def test_help_option(script_runner):

    ret = script_runner.run("transform_issues_to_pages.py", "--help")
    assert ret.success


def test_execution(script_runner):

    url = "https://api.github.com/repos/brainhackorg/global2021/issues?per_page=100"  # noqa: E501
    path = os.path.expanduser(tmp_dir.name)

    ret = script_runner.run("transform_issues_to_pages.py", url, path)
    assert ret.success
