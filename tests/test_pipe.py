"""Tests for the Pipe class."""

##############################################################################
# Python imports.
from functools import partial
from operator import add

##############################################################################
# Local imports.
from bagofstuff.pipe import Pipe


##############################################################################
def test_single_function_inline() -> None:
    """We should be able to pass a single function inline."""
    assert Pipe[str, str](str.upper)("test") == "TEST"


##############################################################################
def test_single_function_via_pipe() -> None:
    """We should be able to pass a single function later."""
    assert (Pipe[str, str]() | str.upper)("test") == "TEST"


##############################################################################
def test_multi_function_inline() -> None:
    """We should be able to pass multiple functions inline."""
    assert Pipe[str, str](str.strip, str.upper)("   test   ") == "TEST"


##############################################################################
def test_multi_function_via_piple() -> None:
    """We should be able to pass multiple functions inline."""
    assert (Pipe[str, str]() | str.strip | str.upper)("   test   ") == "TEST"


##############################################################################
def test_pipe_with_pipe() -> None:
    """A pipe should be usable in another pipe's pipeline."""
    child_pipe = Pipe[int, int](partial(add, 1))
    main_pipe = Pipe[int, int](child_pipe, child_pipe) | child_pipe | child_pipe
    assert main_pipe(1) == 5


### test_pipe.py ends here
