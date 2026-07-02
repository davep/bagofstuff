"""Unit tests for the cache manager class."""

##############################################################################
# Python imports.
from pathlib import Path

##############################################################################
# Local imports.
from bagofstuff.cache import CacheManager


##############################################################################
def test_base_path(tmp_path: Path) -> None:
    """Test that the base path is set correctly."""
    assert CacheManager(tmp_path).base_path == tmp_path


##############################################################################
def test_get_creates_directory(tmp_path: Path) -> None:
    """Test that the get method creates the directory if it doesn't exist."""
    assert CacheManager(tmp_path).get(foo="bar").parent.exists() is True


##############################################################################
def test_get_no_auto_create(tmp_path: Path) -> None:
    """Test that the get method does not create the directory if auto_create_directory is False."""
    assert CacheManager(tmp_path, False).get(foo="bar").parent.exists() is False


##############################################################################
def test_get_is_deterministic(tmp_path: Path) -> None:
    """Test that the get method returns the same path for the same input arguments."""
    cache_manager = CacheManager(tmp_path)
    assert cache_manager.get(foo="bar") == cache_manager.get(foo="bar")
    assert cache_manager.get(foo="baz") != cache_manager.get(foo="wibble")


##############################################################################
def test_get_multiple_types(tmp_path: Path) -> None:
    """Test that the get method works with multiple types of input arguments."""
    cache_manager = CacheManager(tmp_path)
    assert cache_manager.get(foo="bar", baz=42) == cache_manager.get(baz=42, foo="bar")
    assert cache_manager.get(foo="bar", baz=42) != cache_manager.get(foo="bar", baz=43)


### test_cache.py ends here
