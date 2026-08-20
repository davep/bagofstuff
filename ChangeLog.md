# BagOfStuff ChangeLog

## Unreleased

**Released: WiP**

- Added a `add_or_replace` to the history classes.
  ([#27](https://github.com/davep/bagofstuff/pull/27))
- History classes are not based on `MutableSequence` rather than just
  `Sequence`. ([#28](https://github.com/davep/bagofstuff/pull/28))
- BREAKING CHANGE: The `clear` method of the history classes no longer
  returns `self` (to confirm with Python's `MutableSequence` interface).
  ([#28](https://github.com/davep/bagofstuff/pull/28))

## v1.3.0

**Released: 2026-08-16**

- Added a `truncate` method to the history classes.
  ([#24](https://github.com/davep/bagofstuff/pull/24))
- Added a `clone` method to the history classes.
  ([#25](https://github.com/davep/bagofstuff/pull/25))

## v1.2.1

**Released: 2026-07-19**

- Improved the type hint of `Pipe.__or__`.
  ([#23](https://github.com/davep/bagofstuff/pull/23))

## v1.2.0

**Released: 2026-07-03**

- Added a `clear` method to the history classes.
  ([#21](https://github.com/davep/bagofstuff/pull/21))

## v1.1.0

**Released: 2026-07-02**

- Added the ability to `del` from a history object.
  ([#18](https://github.com/davep/bagofstuff/pull/18))
- Added `cache.CacheManager`.
  ([#19](https://github.com/davep/bagofstuff/pull/19))

## v1.0.0

**Released: 2026-06-23**

- Added `cleaners.clamp`.
  ([#12](https://github.com/davep/bagofstuff/pull/12))
- Added `history.SimpleHistory`
  ([#14](https://github.com/davep/bagofstuff/pull/14))
- Added `history.NavigableHistory`
  ([#14](https://github.com/davep/bagofstuff/pull/14))
- Added `history.RecencyHistory`
  ([#14](https://github.com/davep/bagofstuff/pull/14))

## v0.2.0

**Released: 2026-02-06**

- Added `url_tools.looks_webish`.
  ([#9](https://github.com/davep/bagofstuff/pull/9))

## v0.1.0

**Released: 2026-02-01**

- `Pipe` can now start with zero arguments.
  ([#5](https://github.com/davep/bagofstuff/pull/5))
- Added `Pipe.Nullary` as the type to mark a pipe that takes no arguments.
  ([#5](https://github.com/davep/bagofstuff/pull/5))
- An empty `Pipe` when called will now raise a `TypeError`.
  ([#5](https://github.com/davep/bagofstuff/pull/5))

## v0.0.1

**Released: 2026-01-31**

- Initial release to PyPI.

[//]: # (ChangeLog.md ends here)
