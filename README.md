<div align="center">
    
<img src="https://raw.githubusercontent.com/ietf-tools/common/main/assets/logos/rfclint.svg" alt="RFCLINT" height="125" />
    
[![Release](https://img.shields.io/github/release/ietf-tools/rfclint.svg?style=flat&maxAge=360)](https://github.com/ietf-tools/rfclint/releases)
[![License](https://img.shields.io/github/license/ietf-tools/rfclint)](https://github.com/ietf-tools/rfclint/blob/main/LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/rfclint)](https://pypi.org/project/rfclint/)
[![PyPI - Status](https://img.shields.io/pypi/status/rfclint)](https://pypi.org/project/rfclint/)
[![PyPI - Format](https://img.shields.io/pypi/format/rfclint)](https://pypi.org/project/rfclint/)

##### Perform Validation checks on Internet-Drafts

</div>

- [Changelog](https://github.com/ietf-tools/rfclint/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/ietf-tools/.github/blob/main/CONTRIBUTING.md)

---

There are a number of tasks that need to be performed when an [Internet-Draft](https://en.wikipedia.org/wiki/Internet_Draft) is begin process to create an [RFC](https://en.wikipedia.org/wiki/Request_for_Comments). This tool performs a subset of those actions.

The actions performed are:

- Validate the file is well formed XML and that it conforms to the XML2RFC Version 3 schema as defined in [RFC 7991](https://tools.ietf.org/html/rfc7991).
- Verify that embedded XML stanzas are well formed.
- Verify that embedded ABNF is complete and well formed.
- Identify misspelled words.
- Detect duplicate words.

The tool can be used either in an interactive mode or in batch mode.

## Usage

`rfclint` accepts a single XML document as input and optionally outputs a modified version
of the document.

### Basic Usage

```sh
rfclint [options] SOURCE
```

### General Options

|      Short     |           Long          |                   Description                   |
|----------------|-------------------------|-------------------------------------------------|
| `-C`           | `--clear-cache`         | purge the cache and exit                        |
| `-N`           | `--no-network`          | don't use the network to resolve references     |
| `-n`           | `--no-rng`              | don't check against the RNG schema              |
| `-q`           | `--quiet`               | don't print anything                            |
| `. `           | `--save-config`         | save configuration back to config file          |
| `-v`           | `--verbose`             | print extra information                         |
| `-V`           | `--version`             | display the version number and exit             |
| `.`            | `--no-xml`              | don't check xml examples for well-formness      |
| `.`            | `--bcp14`               | do checking for bcp14 keywords                  |
| `.`            | `--no-svgcheck`         | skip check svg for limited vocabulary           |
| `-c DIRECTORY` | `--cache=DIRECTORY`     | specify the primary cache directory to write to |
| `.`            | `--configfile=FILENAME` | specify the configuration file to use           |
| `-o FILENAME`  | `--out=FILENAME`        | specify an output filename                      |
| `.`            | `--extract=TYPE`        | extract all source code for the given type      |

### Spelling Options

The following options affect how the spell checking is performed.

|  Short  |            Long            |                    Description                   |
|---------|----------------------------|--------------------------------------------------|
| `.`     | `--no-dup-detection`       | don't perform duplicate detection                |
| `.`     | `--no-spell`               | don't perform spell checking on the source       |
| `.`     | `--no-suggest`             | don't provide suggestions for misspelled words   |
| `.`     | `--skip-code`              | skip code elements when checking                 |
| `.`     | `--skip-artwork`           | skip artwork elements check checking             |
| `.`     | `--no-curses`              | don't do window based                            |
| `.`     | `--color=TEXT`             | specify the color to use for word highlighting   |
| `.`     | `--dictionary=FILENAME`    | specify an additional dictionary to use          |
| `.`     | `--personal=FILENAME`      | specify the personal dictionary to use           |
| `.`     | `--spell-program=FILENAME` | program to use for spell checking                |
| `.`     | `--spell-window=NUM`       | how many words to display as part of the context |

It is assumed that the spell checking program is aspell and that aspell is on the path.  
For Windows systems, it additionally look in `C:\Program Files (x86)\Aspell\bin` for the program.  
If a different program is given, then it should be either an absolute path or on the path so that it can be located.

When a misspelled word is located, a certain amount of context will be provided along with the file and line number of the word. The spell-window parameter controls how many words are displayed with up to that number of words being displayed before and after the misspelled word. The context window is also restricted to the current paragraph.

The `color` option allows for the misspelled word to be highlighted, but it requires VT100 terminal emulation and thus may not always work well on Windows systems. The color defaults to `bright` on non-Windows systems and `none` on Windows systems.

If the value of `spell-window` is `0`, then no context will be displayed.
    
### ABNF Checking Options
    
| Short | Long                      | Description                               |
|-------|---------------------------|-------------------------------------------|
| `.`   | `--no-abnf`               | don't perform abnf checking on the source |
| `.`   | `--abnf-add-rules`        | ABNF file to include when checking        |
| `.`   | `--abnf-program=FILENAME` | specify program to use for ABNF checking  |

### Configuration File

`rfclint` keeps configuration information in a configuration file. By default the file is stored at

- On Windows: `C:\Users\USER\AppData\Local\rfclint\IETF\rfclint.cfg`
- Otherwise: `/home/USER/.local/share/rfclint/rfclint.cfg`

The format of the configuration file is the standard INI file format.

### Spell Configuration

- `program` - name of the spelling program to use - defaults to `aspell`
- `window` - number of words to display on each side of a misspelled word
- `color` - color to use to highlight the misspelled word
- `suggest` - Should suggested values be displayed? value is `0` or `1`
- `dictionaries` - a comma separated list of dictionaries to include

### ABNF Configuration

- `program` - name of the ABNF program to use - defaults to bap provided w/ `rfclint` *(bap is only installed for systems identified as nt, darwin or linux\*)*
- `addRules` - name of file to be processed along with rules in the source

## Windows and Curses

The version of python that ships on windows does not include a copy of the curses module as part of it.
If interactive spell checking or duplicate detection is desired on a windows system then a curses module will need to be installed independent of this package.
One place to locate a curses Python extension an be found at https://www.lfd.uci.edu/~gohlke/pythonlibs/.
If no curses library is detected, rfclint will automatically turn on the `--no-curses` option.

## Dependencies

Various features on `rfclint` depends on the following external packages:
 * [Bill's ABNF Parser (BAP)](https://github.com/ietf-tools/bap)
 * [aspell](http://aspell.net)

 ## Running `rfclint` tests for development

 ```
 tox
 ```
