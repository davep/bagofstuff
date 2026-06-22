"""Tests for the clamp function."""

##############################################################################
# Python imports.

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Local imports.
from bagofstuff.cleaners import TClampable, clamp


##############################################################################
@mark.parametrize(
    "value, min_value, max_value, expected",
    [
        # Test clamping within the range.
        (5, 1, 10, 5),
        # Test clamping below the range.
        (0, 1, 10, 1),
        # Test clamping above the range.
        (11, 1, 10, 10),
        # Test clamping with min_value greater than max_value.
        (5, 10, 1, 5),
        (0, 10, 1, 1),
        (11, 10, 1, 10),
        # Test clamping floats.
        (5.5, 1.0, 10.0, 5.5),
        (0.5, 1.0, 10.0, 1.0),
        (11.5, 1.0, 10.0, 10.0),
    ],
)
def test_clamp(
    value: TClampable,
    min_value: TClampable,
    max_value: TClampable,
    expected: TClampable,
) -> None:
    """Test the clamp function."""
    assert clamp(value, min_value, max_value) == expected


### test_cleaners.py ends here
