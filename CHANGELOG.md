# CHANGELOG

## [0.4.0] - 2020-12-28
### Added
- Wildcard support for `list` and `remove` (\*, ?, [abc]).
- `list` prints keys in alphabetical order.
- Config file support.

### Changed
- Rename project to 'kaz'.
- `list` now prints keys and values.
- Change color scheme.

### Removed
- `clear` subcommand. Use `kaz remove '*'` instead.

## [0.3.0] - 2020-07-20
### Added
- Color in output.
- --version option.

### Changed
- Running with no subcommands now lists the items.

### Removed
- Remove --binary flag; binary items are automatically detected.

### Fixed
- Autocompletion for the --help option now works.
- Help can also be displayed with -h.

## [0.2.0] - 2020-07-20
### Added
- Binary item support.
- Autocompletion support.
- `set` now has an --edit flag for opening the item with the default text editor.
- `set` can now read from stdin when no other options are present.

### Changed
- Rename project to 'hold'.
- Tweak help menu.

### Fixed
- Error messages are now sent to stderr.

## [0.1.0] - 2020-07-20
### Added
- `list` command for viewing all items.
- `get` command for showing the value of an item.
- `set` command for storing a value in an item.
- `remove` command for deleting an item.
- `clear` command for deleting all items.

[Unreleased]: https://github.com/clabe45/kaz/compare/v0.4.0...HEAD
[0.4.0]: https://github.com/clabe45/kaz/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/clabe45/kaz/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/clabe45/kaz/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/clabe45/kaz/releases/tag/v0.1
