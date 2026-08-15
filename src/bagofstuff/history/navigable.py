"""Provides a navigable history class."""

##############################################################################
# Python imports.
from typing import Self

##############################################################################
# Local imports.
from .simple import SimpleHistory


##############################################################################
class NavigableHistory[T](SimpleHistory[T]):
    """A history class that implements a linear navigation history.

    When adding an item to the history, everything after the current
    location is removed from the history, and the new item is placed at the
    end.
    """

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
        self.truncate()
        return super().add(item)


### navigable.py ends here
