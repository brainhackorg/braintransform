# braintransform

[![Build Status](https://github.com/brainhackorg/braintransform/workflows/test,%20package/badge.svg)](https://github.com/brainhackorg/braintransform/actions?query=workflow%3A%22test%2C+package%22+branch%3Amain)

Project issue to website data transformation toolkit .

## Introduction

The purpose of these scripts is to be able to dynamically generate the project
pages used by the Brainhack Global website. Given a GitHub issues URL, the
`scripts/transform_issues_to_pages.py` script obtains the list of issues,
filters those that correspond to projects, and scrapes the relevant data to
generate project Markdown files that are written to an output folder. These
files can then be processed by the Brainhack Global website generator framework
to fill the contents of the project page.

The automation of the project page generation can be seen in the
`.github/workflows/issue-to-page.yml` GitHub workflow of the
[Brainhack Global 2021 repository](Brainhack Global 2021).

This tool was introduced for the Brainhack Global 2020, and was refactored and
moved into a separate repository for the Brainhack Global 2021.
