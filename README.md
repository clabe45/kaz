# Pallet

This cli lets you easily store binary and text items and retrieve them later.

## Installation

```
pip install pallet
```

## Usage

Basic usage:
```sh
pallet set key value
pallet get key # value
```

You can also use stdin and stdout:
```sh
pallet set license < license.txt
pallet get license > license2.txt
```

which also works with binary blobs:
```sh
pallet set "profile pic" < profile-picture.png
```

## Commands

```sh
$ pallet --help
Usage: pallet [OPTIONS] COMMAND [ARGS]...

  Simple local storage cli

Options:
  --help  Show this message and exit.

Commands:
  clear   Remove all items
  get     Print the value of an item
  list    Show all stashed items
  remove  Remove an item
  set     Store a value in an item
```

## Autocompletion

To enable autocompletion, source the script in the [autocomplete][autocomplete] directory that corresponds to your shell. Currently bash, fish and zsh are supported.

For bash, this would look like:

```sh
wget https://raw.githubusercontent.com/clabe45/pallet/master/autocomplete/pallet-completion-bash.sh
. pallet-completion-bash.sh
```

You may want to add the last command to your ~/.bashrc.

## Contributing

1. [Fork this repo!][fork]
2. Clone: `git clone https://github.com/YOUR-USERNAME/pallet.git`
3. [Pick an issue][pick an issue] or [open a new one][open an issue] if you have a feature idea.
4. Preferably check out a new feature branch: `git checkout -b feature/my-feature` (makes the PR process easier)
5. Implement your change.
  - Try to keep your commits [atomic][atomic commits].
6. Push: `git push origin FEATURE-BRANCH`
7. Create a [new pull request][new pull request].

[autocomplete]: https://github.com/clabe45/pallet/tree/master/autocomplete
[fork]: https://github.com/clabe45/pallet/fork
[pick an issue]: https://github.com/clabe45/pallet/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22
[open an issue]: https://github.com/clabe45/pallet/issues/new
[atomic commits]: https://www.freshconsulting.com/atomic-commits/
[new pull request]: https://github.com/clabe45/pallet/compare

## License

Licensed under GNU GPL v3.
