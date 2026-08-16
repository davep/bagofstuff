"""Provides a simple history class."""

##############################################################################
# Future imports.
from __future__ import annotations

##############################################################################
# Python imports.
from collections import deque
from collections.abc import Iterator, Sequence
from sys import maxsize
from typing import TYPE_CHECKING, Final, Self, overload

##############################################################################
# Local imports.
from ..cleaners import clamp

##############################################################################
_DEFAULT_MAX_LENGTH: Final[int] = 500
"""The default maximum length for the history."""


##############################################################################
class SimpleHistory[T](Sequence[T]):
    """A history class that implements a simple linear history.

    Adding items to the list simple grows the list until the maximum length
    is reached, at which point the oldest items are removed.
    """

    def __init__(
        self, history: Sequence[T] | None = None, max_length: int = _DEFAULT_MAX_LENGTH
    ) -> None:
        """Initialise the history object.

        Args:
            history: Set to the given history.
            max_length: Optional maximum length for the history.
        """
        self._history: deque[T] = deque(history or [], maxlen=max_length)
        """The history."""
        self._current_index: int = max(len(self._history) - 1, 0)
        """The current index in the history."""

    @property
    def current_location(self) -> int | None:
        """The current integer location in the history.

        If there is no valid location the value is `None`.
        """
        try:
            _ = self._history[self._current_index]
        except IndexError:
            return None
        return self._current_index

    @property
    def current_item(self) -> T | None:
        """The current item in the history.

        If there is no current item in the history the value is `None`.
        """
        try:
            return self._history[self._current_index]
        except IndexError:
            return None

    @property
    def can_go_backward(self) -> bool:
        """Can history go backward?"""
        return bool(self._current_index)

    def clone(self) -> Self:
        """Clone the history.

        Returns:
            A clone of the history.

        Note:
            The clone is a new instance of the history with the same items and
            current location.
        """
        return self.__class__(
            list(self._history), max_length=self._history.maxlen or _DEFAULT_MAX_LENGTH
        ).goto(self._current_index)

    def truncate(self) -> Self:
        """Truncate the history at the current location.

        Returns:
            Self.
        """
        self._history = deque(
            list(self._history)[: self._current_index + 1], maxlen=self._history.maxlen
        )
        return self

    def backward(self) -> bool:
        """Go backward through the history.

        Returns:
            `True` if we moved through history, `False` if not.
        """
        if self.can_go_backward:
            self._current_index -= 1
            return True
        return False

    @property
    def can_go_forward(self) -> bool:
        """Can history go forward?"""
        return self._current_index < len(self._history) - 1

    def forward(self) -> bool:
        """Go forward through the history.

        Returns:
            `True` if we moved through history, `False` if not.
        """
        if self.can_go_forward:
            self._current_index += 1
            return True
        return False

    def goto(self, location: int) -> Self:
        """Jump to a specific location within history."""
        self._current_index = int(clamp(location, 0, len(self._history) - 1))
        return self

    def goto_end(self) -> Self:
        """Go to the end of the history."""
        self.goto(len(self) - 1)
        return self

    def add(self, item: T) -> Self:
        """Add an item to the history.

        Args:
            item: The item to add.

        Returns:
            Self.

        Note:
            When adding an item to the history, everything after the current
            location is removed from the history, and the new item is placed
            at the end.
        """
        self._history.append(item)
        return self.goto_end()

    def index(self, item: T, start: int = 0, stop: int = maxsize) -> int:
        """Return the index of the given history item.

        Args:
            item: The item to find in the history.
            start: Optional start location.
            stop: Optional stop location.

        Returns:
            The index of the item in the history.

        Raises:
            ValueError: If the item is not in the history.
        """
        return self._history.index(item, start, stop)

    def count(self, item: T) -> int:
        """Return the number of occurrences of the given value in the history.

        Args:
            item: The value to count in the history.

        Returns:
            The number of occurrences of the value in the history.
        """
        return self._history.count(item)

    def clear(self) -> Self:
        """Clear the history."""
        self._history.clear()
        self._current_index = 0
        return self

    if TYPE_CHECKING:

        @overload
        def __getitem__(self, index: int) -> T: ...

        @overload
        def __getitem__(self, index: slice) -> list[T]: ...

    def __getitem__(self, index: int | slice) -> T | list[T]:
        """Get an item from the history."""
        return (
            list(self._history)[index]
            if isinstance(index, slice)
            else self._history[index]
        )

    def __delitem__(self, index: int) -> None:
        """Delete an item from the history."""
        del self._history[index]
        if self._current_index >= len(self):
            self.goto_end()

    def __len__(self) -> int:
        """The length of the history."""
        return len(self._history)

    def __bool__(self) -> bool:
        """Test if the history is empty."""
        return bool(self._history)

    def __iter__(self) -> Iterator[T]:
        """Support iterating through the history."""
        return iter(self._history)

    def __contains__(self, value: object) -> bool:
        """Test if the given item is in the history."""
        return value in self._history

    def __reversed__(self) -> Iterator[T]:
        """Return a reversed list of the contents of the history."""
        return reversed(self._history)


### simple.py ends here
