"""Tests for the Pipe class."""

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


### test_pipe.py ends here
