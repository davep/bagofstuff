"""Tests for the contents of itertools."""

##############################################################################
# Python imports.
from typing import Any, Iterable

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Local imports.
from bagofstuff.itertools import Direction, starting_at


##############################################################################
@mark.parametrize(
    "initial, rotate_at, direction, expected",
    (
        # Rotating forward,
        ([], 0, "forward", []),
        ([0], 0, "forward", [0]),
        ([0, 1, 2, 3], 1, "forward", [1, 2, 3, 0]),
        (range(4), 1, "forward", [1, 2, 3, 0]),
        ("ABCD", 1, "forward", ["B", "C", "D", "A"]),
        # Rotating backwards.
        ([], 0, "backward", []),
        ([0], 0, "backward", [0]),
        ([0, 1, 2, 3], 1, "backward", [1, 0, 3, 2]),
        (range(4), 1, "backward", [1, 0, 3, 2]),
        ("ABCD", 1, "backward", ["B", "A", "D", "C"]),
        # Unusual inputs.
        ([], -1, "forward", []),
        ([], 1_000_000, "forward", []),
    ),
)
def test_starting_at(
    initial: Iterable[int],
    rotate_at: Any,
    direction: Direction,
    expected: list[Any],
) -> None:
    """`rotate_around` should work as expected."""
    assert list(starting_at(initial, rotate_at, direction)) == expected


### test_itertools.py ends here
