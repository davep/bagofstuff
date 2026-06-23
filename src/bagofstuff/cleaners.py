"""Provides functions for cleaning things."""

##############################################################################
type TClampable = int | float
"""A type that can be clamped."""


##############################################################################
def clamp(
    value: TClampable, min_value: TClampable, max_value: TClampable
) -> TClampable:
    """Clamp a value between a minimum and maximum value.

    Args:
        value: The value to clamp.
        min_value: The minimum value.
        max_value: The maximum value.

    Returns:
        The clamped value.
    """
    if min_value > max_value:
        min_value, max_value = max_value, min_value
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value


### cleaners.py ends here
