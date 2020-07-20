# Hold

> Holds anything you would like

Hold is a minimalistic local storage cli. You can easily store binary and text items and retrieve them later.

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

You can also use stdin:
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

## Contributing

1. Fork this repo!
2. Clone: `git clone https://github.com/YOUR-USERNAME/hold.git`
3. Pick an issue or open a new one if you have a feature idea.
4. Preferably check out a new feature branch: `git checkout -b feature/my-feature` (makes the PR process easier)
5. Implement your change.
  - Try to keep your commits [atomic](https://www.freshconsulting.com/atomic-commits/).
6. Push: `git push origin FEATURE-BRANCH`
7. Create a new pull request.
