"""Tests for the Pipe class."""

##############################################################################
# Python imports.
from functools import partial
from operator import add

##############################################################################
# Pytest imports.
from pytest import raises

##############################################################################
# Local imports.
from bagofstuff.pipe import NoArgument, Pipe


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


##############################################################################
def test_pipe_with_no_initial_argument() -> None:
    """A pipe should work fine without an initial argument."""

    def one() -> int:
        return 1

    def plus_one(value: int) -> int:
        return value + 1

    assert (Pipe[NoArgument, int](one, plus_one) | plus_one)() == 3


##############################################################################
def test_empty_pipeline() -> None:
    """Calling an empty Pipe should result in an error."""
    with raises(TypeError):
        _ = Pipe[None, None]()()


### test_pipe.py ends here
