"""Tests for the URL tools."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Local imports.
from bagofstuff.url_tools import looks_webish


##############################################################################
@mark.parametrize(
    "candidate, expected_result",
    (
        ("https://example.com", True),
        ("http://example.com", True),
        ("  https://example.com  ", True),
        ("  http://example.com  ", True),
        ("ftp://example.com", False),
        ("http", False),
        ("https", False),
        ("http:", False),
        ("https:", False),
        ("http:example.com", True),
        ("https:example.com", True),
        ("https:80", True),
        ("", False),
    ),
)
def test_looks_webish(candidate: str, expected_result: bool) -> None:
    """Does looks_webish perform as expected?"""
    assert looks_webish(candidate) is expected_result


### test_url_tools.py ends here
