"""Unit tests for the recency history class."""

##############################################################################
# Local imports.
from bagofstuff.history import RecencyHistory


##############################################################################
def test_add_duplicate_item() -> None:
    """Test that adding a duplicate item moves it to the end of the history."""
    history = RecencyHistory[int]([1, 2, 3])
    history.add(2)
    assert len(history) == 3
    assert list(history) == [1, 3, 2]


### test_recency_history.py ends here
