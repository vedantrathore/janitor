# Janitor

[![Build Status](https://travis-ci.org/vedantrathore/janitor.svg?branch=master)](https://travis-ci.org/vedantrathore/janitor)
[![Coverage Status](https://coveralls.io/repos/github/vedantrathore/janitor/badge.svg?branch=master)](https://coveralls.io/github/vedantrathore/janitor?branch=master)

The Easiest way to clean and analyse your files!

### Installation

* Install python and pip according to your system with the guide available [here](http://docs.python-guide.org/en/latest/starting/installation/)
* ` git clone https://github.com/vedantrathore/janitor && cd janitor`
* ` pip install -r requirements.txt`
* ` pip install -e .`

### Usage

* open the directory of your choice in a terminal/command prompt
```
Usage: janitor [OPTIONS] COMMAND [ARGS]...

  A simple command line tool to clean and analyse your file system

Options:
  --help  Show this message and exit.

Commands:
  analyse  Analyse the directory
  clean    Clean your unwanted files to a secure location of your choice
```
* add `--help` to check command arguments

### Todo
- [x] ~~Add Travis support~~
- [ ] Package and publish to pip
- [ ] Write more tests and increase coverage
- [ ] Add more features
