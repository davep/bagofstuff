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

See [the API documentation](library-contents/cache.md) for details on
the content of the library.

## Hacking

If you want to hack on the code yourself you'll find most of the routine
stuff you'd do when testing and the like in the `Makefile`. Type:

```sh
$ make
```

to get a list of available targets.

[//]: # (index.md ends here)
