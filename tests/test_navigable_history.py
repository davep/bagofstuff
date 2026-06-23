"""Unit tests for the navigable history class."""

##############################################################################
# Local imports.
from bagofstuff.history import NavigableHistory


##############################################################################
def test_add_removes_forward_history() -> None:
    """Test that adding an item removes forward history."""
    history = NavigableHistory[int]([1, 2, 3])
    assert history.backward() is True
    history.add(4)
    assert history.current_item == 4
    assert history.current_location == 2
    assert history.can_go_backward is True
    assert history.can_go_forward is False
    assert list(history) == [1, 2, 4]


### test_navigable_history.py ends here
