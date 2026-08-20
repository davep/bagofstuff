"""Unit tests for the navigable history class."""

##############################################################################
# Python imports.
from dataclasses import dataclass

##############################################################################
# Pytest imports.
from pytest import raises

##############################################################################
# Local imports.
from bagofstuff.history import NavigableHistory, SimpleHistory


##############################################################################
def test_empty_history() -> None:
    """Test that an empty history has no current item."""
    history = SimpleHistory[None]()
    assert history.current_item is None
    assert history.current_location is None
    assert history.can_go_backward is False


##############################################################################
def test_initialise_with_list() -> None:
    """Test that a history initialised with a list has the last item as current."""
    items = [1, 2, 3]
    history = SimpleHistory[int](items)
    assert history.current_item == 3
    assert history.current_location == 2
    assert history.can_go_backward is True


##############################################################################
def test_initialise_with_tuple() -> None:
    """Test that a history initialised with a tuple has the last item as current."""
    items = (1, 2, 3)
    history = SimpleHistory[int](items)
    assert history.current_item == 3
    assert history.current_location == 2
    assert history.can_go_backward is True


##############################################################################
def test_truncates_on_max_length() -> None:
    """Test that a history truncates when the max length is exceeded."""
    items = [1, 2, 3, 4, 5]
    history = SimpleHistory[int](items, max_length=5)
    history.add(6)
    assert len(history) == 5
    assert list(history) == [2, 3, 4, 5, 6]
    assert history.current_item == 6


##############################################################################
def test_truncates_on_init() -> None:
    """Test that a history truncates when initialised with a list longer than max length."""
    items = [1, 2, 3, 4, 5, 6]
    history = SimpleHistory[int](items, max_length=5)
    assert len(history) == 5
    assert list(history) == [2, 3, 4, 5, 6]
    assert history.current_item == 6


##############################################################################
def test_add_to_empty() -> None:
    """Test that adding an item to an empty history sets it as the current item."""
    history = SimpleHistory[int]()
    assert history.current_item is None
    assert history.current_location is None
    assert history.can_go_backward is False
    assert history.can_go_forward is False
    history.add(1)
    assert history.current_item == 1
    assert history.current_location == 0
    assert history.can_go_backward is False
    assert history.can_go_forward is False


##############################################################################
def test_add_to_non_empty() -> None:
    """Test that adding an item to a non-empty history sets it as the current item."""
    history = SimpleHistory[int]([1, 2, 3])
    assert history.current_item == 3
    assert history.current_location == 2
    assert history.can_go_backward is True
    assert history.can_go_forward is False
    history.add(4)
    assert history.current_item == 4
    assert history.current_location == 3
    assert history.can_go_backward is True
    assert history.can_go_forward is False


##############################################################################
@dataclass
class HistoryItem:
    primary: str
    secondary: int

    def __eq__(self, other: object) -> bool:
        if isinstance(other, HistoryItem):
            return self.primary == other.primary
        return NotImplemented


##############################################################################
def test_add_or_replace_to_empty() -> None:
    """Test that adding an item to an empty history sets it as the current item."""
    history = SimpleHistory[HistoryItem]()
    assert history.current_item is None
    assert history.current_location is None
    assert history.can_go_backward is False
    assert history.can_go_forward is False
    history.add_or_replace(HistoryItem("a", 1))
    assert history.current_item == HistoryItem("a", 1)
    assert history.current_location == 0
    assert history.can_go_backward is False
    assert history.can_go_forward is False


##############################################################################
def test_add_or_replace_to_non_empty() -> None:
    """Test that adding an item to a non-empty history sets it as the current item."""
    history = SimpleHistory[HistoryItem]([HistoryItem("a", 1), HistoryItem("b", 2)])
    assert history.current_item == HistoryItem("b", 2)
    assert history.current_location == 1
    assert history.can_go_backward is True
    assert history.can_go_forward is False
    history.add_or_replace(HistoryItem("c", 3))
    assert history.current_item == HistoryItem("c", 3)
    assert history.current_location == 2
    assert history.can_go_backward is True
    assert history.can_go_forward is False


##############################################################################
def test_add_or_replace_replaces_current() -> None:
    """Test that adding an item to a non-empty history replaces the current item if equal."""
    history = SimpleHistory[HistoryItem]([HistoryItem("a", 1), HistoryItem("b", 2)])
    assert history.current_item is not None
    assert history.current_item.primary == "b"
    assert history.current_item.secondary == 2
    assert history.current_location == 1
    assert history.can_go_backward is True
    assert history.can_go_forward is False
    history.add_or_replace(HistoryItem("b", 3))
    assert history.current_item is not None
    assert history.current_item.primary == "b"
    assert history.current_item.secondary == 3
    assert history.current_location == 1
    assert history.can_go_backward is True
    assert history.can_go_forward is False


##############################################################################
def test_backward() -> None:
    """Test that going backward works."""
    history = SimpleHistory[int]([1, 2, 3])
    assert history.backward() is True
    assert history.current_item == 2
    assert history.current_location == 1
    assert history.can_go_backward is True
    assert history.can_go_forward is True
    assert history.backward() is True
    assert history.current_item == 1
    assert history.current_location == 0
    assert history.can_go_backward is False
    assert history.can_go_forward is True
    assert history.backward() is False


##############################################################################
def test_forward() -> None:
    """Test that going forward works."""
    history = SimpleHistory[int]([1, 2, 3])
    history.goto(0)
    assert history.forward() is True
    assert history.current_item == 2
    assert history.current_location == 1
    assert history.can_go_backward is True
    assert history.can_go_forward is True
    assert history.forward() is True
    assert history.current_item == 3
    assert history.current_location == 2
    assert history.can_go_backward is True
    assert history.can_go_forward is False
    assert history.forward() is False


##############################################################################
def test_get_item() -> None:
    """Test that getting an item by index works."""
    history = SimpleHistory[int]([1, 2, 3])
    assert history[0] == 1
    assert history[1] == 2
    assert history[2] == 3
    assert history[-1] == 3
    with raises(IndexError):
        _ = history[3]


##############################################################################
def test_get_slice() -> None:
    """Test that getting a slice of items works."""
    history = SimpleHistory[int]([1, 2, 3, 4, 5])
    assert history[1:4] == [2, 3, 4]
    assert history[:3] == [1, 2, 3]
    assert history[2:] == [3, 4, 5]
    assert history[:] == [1, 2, 3, 4, 5]
    assert history[:999] == [1, 2, 3, 4, 5]


##############################################################################
def test_seed_history_from_history() -> None:
    """Test that a history can be seeded from another history."""
    history1 = SimpleHistory[int]([1, 2, 3])
    history2 = SimpleHistory[int](history1)
    assert list(history2) == [1, 2, 3]
    assert history2.current_item == 3
    assert history2.current_location == 2
    assert history2.can_go_backward is True
    assert history2.can_go_forward is False


##############################################################################
def test_index_of_item_in_history() -> None:
    """Test that the index of an item in the history can be found."""
    history = SimpleHistory[int]([1, 2, 3])
    assert history.index(1) == 0
    assert history.index(2) == 1
    assert history.index(3) == 2
    with raises(ValueError):
        _ = history.index(4)


##############################################################################
def test_count_of_item_in_history() -> None:
    """Test the count of items in a history."""
    history = SimpleHistory[int]([1, 2, 3, 4, 4])
    assert history.count(1) == 1
    assert history.count(4) == 2
    assert history.count(5) == 0


##############################################################################
def test_history_contains() -> None:
    """Test that the in operator works on history."""
    history = SimpleHistory[int]([1, 2])
    assert 1 in history
    assert 3 not in history


##############################################################################
def test_reverse_history() -> None:
    """Test that a reversed history gives a reversed iterator."""
    assert list(reversed(SimpleHistory[int]([1, 2]))) == [2, 1]


##############################################################################
def test_del_history_item() -> None:
    """Test that deleting an item from history works."""
    history = SimpleHistory[int]([1, 2, 3])
    del history[1]
    assert list(history) == [1, 3]
    assert history.current_item == 3
    assert history.current_location == 1
    del history[0]
    assert list(history) == [3]
    assert history.current_item == 3
    assert history.current_location == 0
    del history[0]
    assert list(history) == []
    assert history.current_item is None
    assert history.current_location is None
    with raises(IndexError):
        del history[0]


##############################################################################
def test_clear_history() -> None:
    """Test that clearing the history works."""
    history = SimpleHistory[int]([1, 2, 3])
    history.clear()
    assert list(history) == []
    assert history.current_item is None
    assert history.current_location is None


##############################################################################
def test_truncate_history() -> None:
    """Test that truncating the history works."""
    history = SimpleHistory[int]([1, 2, 3])
    assert list(history.truncate()) == [1, 2, 3]
    assert history.current_item == 3
    history.backward()
    assert history.current_item == 2
    assert list(history.truncate()) == [1, 2]
    assert history.current_item == 2


##############################################################################
def test_navigable_history_add_truncates() -> None:
    """Test that adding to a navigable history truncates the history."""
    history = NavigableHistory[int]([1, 2, 3])
    assert history.backward() is True
    assert history.backward() is True
    assert history.current_item == 1
    history.add(4)
    assert list(history) == [1, 4]
    assert history.current_item == 4


##############################################################################
def test_clone() -> None:
    """Test that cloning a history works."""
    history = SimpleHistory[int]([1, 2, 3])
    history.backward()
    clone = history.clone()
    assert list(clone) == list(history)
    assert clone.current_item == history.current_item
    assert clone.current_location == history.current_location
    clone.truncate()
    assert list(clone) == [1, 2]
    assert list(history) == [1, 2, 3]


### test_history.py ends here
