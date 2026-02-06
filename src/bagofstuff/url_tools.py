"""Utility code for dealing with URLs."""

##############################################################################
# Python imports.
from urllib.parse import urlsplit


##############################################################################
def looks_webish(candidate: str) -> bool:
    """Does a given string look like it might be a web-oriented URL?

    Args:
        candidate: The candidate string to test.

    Returns:
        [`True`][True] if it might be a URL, [`False`][False] if not.

    Note:
        This simply checks if a string looks like the sort of input you'd
        expect if you asked a common user to 'enter a URL'. It won't test if
        it's valid or anything like that; but it might be a good tool for
        looking at some text and going 'that might be a URL'.
    """
    return (url := urlsplit(candidate)).scheme in ("http", "https") and any(url[1:])


### url_tools.py ends here
