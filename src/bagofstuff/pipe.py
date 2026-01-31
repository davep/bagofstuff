"""Provides a tool for creating a 'pipe' of functions."""

##############################################################################
# Back from the future...
from __future__ import annotations

##############################################################################
# Python imports.
from functools import reduce
from typing import Any, Callable, cast


##############################################################################
class Pipe[TInitial, TResult]:
    """A class that provides a simple function pipeline."""

    def __init__(self, *functions: Callable[[Any], Any]) -> None:
        """Initialise the pipeline.

        Args:
            functions: The initial set of functions.
        """
        self._functions = functions
        """The functions in the pipeline."""

    def __or__(self, function: Callable[[Any], Any], /) -> Pipe[TInitial, TResult]:
        """Add another function to the pipeline."""
        return Pipe[TInitial, TResult](*self._functions, function)

    def __call__(self, initial: TInitial) -> TResult:
        """Execute the pipeline.

        Args:
            initial: The initial value.

        Returns:
            The result of the pipeline.
        """
        return cast(
            TResult,
            reduce(
                lambda value, function: function(value),
                self._functions,
                initial,
            ),
        )


### pipe.py ends here
