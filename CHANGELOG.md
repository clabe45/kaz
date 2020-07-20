# CHANGELOG

## 0.2.0 - 2020-07-20
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

## 0.1.0 - 2020-07-20
### Added
- `list` command for viewing all items.
- `get` command for showing the value of an item.
- `set` command for storing a value in an item.
- `remove` command for deleting an item.
- `clear` command for deleting all items.
