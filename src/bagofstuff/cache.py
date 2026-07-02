"""Provides a cache manager class."""

##############################################################################
# Python imports.
from hashlib import sha256
from pathlib import Path
from typing import Any, Final


##############################################################################
class CacheManager:
    """A cache manager class."""

    def __init__(
        self, base_path: Path | str, auto_create_directory: bool = True
    ) -> None:
        """Initialise the cache manager.

        Args:
            base_path: The base path for the cache.
            auto_create_directory: If `True`, automatically create the base
                path directory if it doesn't exist.
        """
        self._base_path = Path(base_path)
        """The base path for the cache."""
        self._auto_create_directory = auto_create_directory
        """Whether to automatically create the base path directory if it doesn't exist."""

    @property
    def base_path(self) -> Path:
        """The base path for the cache."""
        return self._base_path

    _PREFIX_SIZE: Final[int] = 2
    """The number of characters to use for the prefix directory."""

    def get(self, **kwargs: Any) -> Path:
        """Get a path from the cache.

        Args:
            **kwargs: The keyword arguments to use to get the path.

        Returns:
            The path from the cache for the given input arguments.
        """
        hash = sha256(
            "".join(f"{k}={v}" for k, v in sorted(kwargs.items())).encode()
        ).hexdigest()
        cache_directory = self._base_path / hash[: self._PREFIX_SIZE]
        if self._auto_create_directory:
            cache_directory.mkdir(parents=True, exist_ok=True)
        return cache_directory / hash[self._PREFIX_SIZE :]


### cache.py ends here
