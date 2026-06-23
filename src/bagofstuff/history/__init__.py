"""Provides classes for handling different types of history."""

##############################################################################
# Local imports.
from .navigable import NavigableHistory
from .recency import RecencyHistory
from .simple import SimpleHistory

##############################################################################
# Exports.
__all__ = ["NavigableHistory", "RecencyHistory", "SimpleHistory"]

### __init__.py ends here
