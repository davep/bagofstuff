# bagofstuff - A library of personal Python utility code

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/davep/bagofstuff/style-lint-and-test.yaml)](https://github.com/davep/bagofstuff/actions)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/davep/bagofstuff/latest)](https://github.com/davep/bagofstuff/commits/main/)
[![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/davep/bagofstuff)](https://github.com/davep/bagofstuff/issues)
[![GitHub Release Date](https://img.shields.io/github/release-date/davep/bagofstuff)](https://github.com/davep/bagofstuff/releases)
[![PyPI - License](https://img.shields.io/pypi/l/bagofstuff)](https://github.com/davep/bagofstuff/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bagofstuff)](https://github.com/davep/bagofstuff/blob/main/pyproject.toml)
[![PyPI - Version](https://img.shields.io/pypi/v/bagofstuff)](https://pypi.org/project/bagofstuff/)

## Introduction

This is small library of utility code for [my personal Python
projects](https://github.com/davep?tab=repositories&q=&type=source&language=python&sort=).
It *might* be useful to someone else, but I imagine that's unlikely. It
contains code that is of general utility for how I approach Python, and also
contains code that I just wanted to have fun writing.

It *is* designed and maintained as being production-ready code.

## Installing

In the unlikely even that you find something in this that you wish to use,
`bagofstuff` is [available from pypi](https://pypi.org/project/bagofstuff/)
and can be installed with `pip` or similar Python package tools:

```shell
$ pip install bagofstuff
```

With `uv`:

```shell
uv add bagofstuff
```

## Using

See [the main documentation](https://bagofstuff.davep.dev/) for details on
the content of the library.

## Hacking

If you want to hack on the code yourself you'll find most of the routine
stuff you'd do when testing and the like in the `Makefile`. Type:

```sh
$ make
```

to get a list of available targets.

[//]: # (README.md ends here)
