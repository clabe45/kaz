# Hold

This cli lets you easily store binary and text items and retrieve them later.

## Installation

```
pip install hold
```

## Usage

Basic usage:
```sh
hold set key value
hold get key # value
```

You can also use stdin and stdout:
```sh
hold set license < license.txt
hold get license > license2.txt
```

and store binary blobs:
```sh
hold set --binary "profile pic" < profile-picture.png
```

## Commands

```sh
$ hold --help
Usage: hold [OPTIONS] COMMAND [ARGS]...

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
wget https://raw.githubusercontent.com/clabe45/hold/master/autocomplete/hold-completion-bash.sh
. hold-completion-bash.sh
```

You may want to add the last command to your ~/.bashrc.

## Contributing

1. [Fork this repo!][fork]
2. Clone: `git clone https://github.com/YOUR-USERNAME/hold.git`
3. [Pick an issue][pick an issue] or [open a new one][open an issue] if you have a feature idea.
4. Preferably check out a new feature branch: `git checkout -b feature/my-feature` (makes the PR process easier)
5. Implement your change.
  - Try to keep your commits [atomic][atomic commits].
6. Push: `git push origin FEATURE-BRANCH`
7. Create a [new pull request][new pull request].

[autocomplete]: https://github.com/clabe45/hold/tree/master/autocomplete
[fork]: https://github.com/clabe45/hold/fork
[pick an issue]: https://github.com/clabe45/hold/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22
[open an issue]: https://github.com/clabe45/hold/issues/new
[atomic commits]: https://www.freshconsulting.com/atomic-commits/
[new pull request]: https://github.com/clabe45/hold/compare

## License

Licensed under GNU GPL v3.
