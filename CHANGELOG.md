# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.0.0] - 2025-12-16
### :boom: BREAKING CHANGES
- due to [`c1b33b9`](https://github.com/ietf-tools/rfclint/commit/c1b33b954c52300444759b23746c3a3c37df314b) - Add support for Python 3.1x *(PR [#23](https://github.com/ietf-tools/rfclint/pull/23) by [@kesara](https://github.com/kesara))*:

  Add support for Python 3.1x (#23)


### :sparkles: New Features
- [`c1b33b9`](https://github.com/ietf-tools/rfclint/commit/c1b33b954c52300444759b23746c3a3c37df314b) - Add support for Python 3.1x *(PR [#23](https://github.com/ietf-tools/rfclint/pull/23) by [@kesara](https://github.com/kesara))*
  - :arrow_lower_right: *addresses issue [#17](https://github.com/ietf-tools/rfclint/issues/17) opened by [@moonshiner](https://github.com/moonshiner)*
  - :arrow_lower_right: *addresses issue [#18](https://github.com/ietf-tools/rfclint/issues/18) opened by [@kesara](https://github.com/kesara)*
  - :arrow_lower_right: *addresses issue [#21](https://github.com/ietf-tools/rfclint/issues/21) opened by [@kesara](https://github.com/kesara)*
  - :arrow_lower_right: *addresses issue [#24](https://github.com/ietf-tools/rfclint/issues/24) opened by [@kesara](https://github.com/kesara)*

### :construction_worker: Build System
- [`3b830f7`](https://github.com/ietf-tools/rfclint/commit/3b830f7465d1385b23768a205600546405a73842) - Run tests as GHA *(PR [#26](https://github.com/ietf-tools/rfclint/pull/26) by [@kesara](https://github.com/kesara))*
  - :arrow_lower_right: *addresses issue [#22](https://github.com/ietf-tools/rfclint/issues/22) opened by [@kesara](https://github.com/kesara)*
- [`f202905`](https://github.com/ietf-tools/rfclint/commit/f202905b4a511c49992e21f2391cb16492b5c646) - PyPI trusted publishing *(PR [#28](https://github.com/ietf-tools/rfclint/pull/28) by [@kesara](https://github.com/kesara))*
  - :arrow_lower_right: *addresses issue [#19](https://github.com/ietf-tools/rfclint/issues/19) opened by [@kesara](https://github.com/kesara)*

### :memo: Documentation Changes
- [`5a3fbe7`](https://github.com/ietf-tools/rfclint/commit/5a3fbe768fe493550c15d84c7d6ece57f96c76ed) - reformat CHANGELOG *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`37a76e7`](https://github.com/ietf-tools/rfclint/commit/37a76e7a90ec37beba0f34e9ec439024db4a8a70) - add CODE_OF_CONDUCT.md *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`dfb0dc7`](https://github.com/ietf-tools/rfclint/commit/dfb0dc79ced3e58fe27d5fcac03941ec3897ef18) - add CONTRIBUTING.md *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`a4e05e3`](https://github.com/ietf-tools/rfclint/commit/a4e05e3369a7d9cc04b627c58d34d2ee21981691) - reformat README *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`570e642`](https://github.com/ietf-tools/rfclint/commit/570e642cfe660bba721e173209d63424c0e7a393) - update LICENSE *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`008a6a1`](https://github.com/ietf-tools/rfclint/commit/008a6a19190cbe97623c91ce5ebf480ffdc8ed93) - README typo *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`9531908`](https://github.com/ietf-tools/rfclint/commit/95319081e65208a000e2c0d5823c32567bda295f) - update CONTRIBUTING link *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`210cbea`](https://github.com/ietf-tools/rfclint/commit/210cbea95fb407c9a821d3d599eb84270bb0d0d8) - remove local community files *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`eda253c`](https://github.com/ietf-tools/rfclint/commit/eda253c2e8bc16028d21c3d9134f5b74aaaf00a6) - update README logo *(commit by [@NGPixel](https://github.com/NGPixel))*

### :wrench: Chores
- [`abdd9af`](https://github.com/ietf-tools/rfclint/commit/abdd9afa5f8c0d5a2a46214bf0a5ec26684d705f) - exclude non-rfclint files *(commit by [@NGPixel](https://github.com/NGPixel))*
- [`cd66a3e`](https://github.com/ietf-tools/rfclint/commit/cd66a3e35a42e87840a6c5ad870ee6ede718d7af) - Add .gitignore file *(PR [#25](https://github.com/ietf-tools/rfclint/pull/25) by [@kesara](https://github.com/kesara))*


## [0.6.1] - 2020-01-24

### Changed

- If suggestion if UTF8, then force format template to be UTF8 for Python 2.0

## [0.5.19] - 2019-08-29

### Added

- Add `<xref>` marker when spell checking

### Changed

- Modify BCP14 if needed
- Change the source tree pointer

## [0.5.17] - 2019-08-16

### Added

- Add Copyright messages to source files
- Add first level support for BCP 14 checking - Only reports does not fix
- Add more programming checks for style

### Changed

- Update documentation to match recent work
- Keep the case of the first word to display for dup detection

### Removed

- Remove space padding in display of spelling and dups.
- Remove Python 3.4 from supported list

## [0.5.16] - 2019-07-01

### Changed

- Update version dependency on rfctools_common

## [0.5.15] - 2019-06-01

### Added

- Add svgcheck to rfclint
- Use file names to extract data if they exist

## [0.5.14] - 2019-05-01

### Changed

- Clean up so that pyflakes is happy

## [0.5.11] - 2018-12-19

### Changed

- Aspell does not permit numbers to be part of words while Python does. Change the matching patterns so that numbers are not part of words.
- Change some messages from warnings to info

## [0.5.10] - 2018-09-03

### Added

- Add `--skip-code` and `--skip-artwork` options to not do spell and duplicate checking on these elements.
- Preserve all of the whitespace in the source file when emitting the output file
- Add output comment for ABFN and XML checking not occuring because it was not needed

### Changed

- Fix an issue where some text was not spell and dup checked (tail of a cref)

## [0.5.8] - 2018-07-11

### Changed

- Curses and Python 2.7 does not allow for any character above 128. Remove all characters above that point
- Expand help on some options

## [0.5.8] - 2018-07-09

### Changed

- Deal with curses and sections that are too big
- Center context text when doing spell and duplicate checking
- Fix bug when no spelling suggestions are present
- Change undefined symbol errors for ABNF from error to warnings.

## [0.5.6] - 2018-07-02

### Changed

- Correct code to do checking of XML code fragments

## [0.5.5] - 2018-04-11

### Added

- Separate duplicate detection from spell checking
- Implement interactive duplicate detection both with and without curses
- Implement interactive spell checking both with and without curses

## [0.5.3] - 2018-04-26

### Added

- Display platform name when bap is not installed.

### Changed

- Correct cache clearing code

## [0.5.2] - 2018-03-30

### Added

- Add test case for v2 dtd path searching

## [0.5.1] - 2018-03-01

### Added

- Set up to all for publishing to PyPI

## [0.5.0] - 2018-02-25

### Changed

- If ANBF program not found, then wrong name was printed
- Allow for both hunspell and aspell to be used for spell checking
- On windows, do not require the `.exe` extension to be specified
- Enable characters outside of the ASCII range to be spell checked. This is not supported on all platforms and with all spell programs

## [0.0.3] - 2018-02-11

### Added

- Handle errors when an executable is missing better
- Add the ability for having personal and additional dictionaries.

## [0.0.2] - 2018-01-26

### Added

- Create the initial simple version
- Create python setup program

[0.6.1]: https://github.com/ietf-tools/rfclint/compare/0.5.19...0.6.1
[0.5.19]: https://github.com/ietf-tools/rfclint/compare/0.5.17...0.5.19
[0.5.17]: https://github.com/ietf-tools/rfclint/compare/0.5.16...0.5.17
[0.5.16]: https://github.com/ietf-tools/rfclint/compare/0.5.15...0.5.16
[0.5.15]: https://github.com/ietf-tools/rfclint/compare/0.5.14...0.5.15
[0.5.14]: https://github.com/ietf-tools/rfclint/compare/0.5.11...0.5.14
[0.5.11]: https://github.com/ietf-tools/rfclint/compare/0.5.10...0.5.11
[0.5.10]: https://github.com/ietf-tools/rfclint/compare/0.5.8...0.5.10
[0.5.8]: https://github.com/ietf-tools/rfclint/compare/0.5.8...0.5.8
[0.5.8]: https://github.com/ietf-tools/rfclint/compare/0.5.6...0.5.8
[0.5.6]: https://github.com/ietf-tools/rfclint/compare/0.5.5...0.5.6
[0.5.5]: https://github.com/ietf-tools/rfclint/compare/0.5.3...0.5.5
[0.5.3]: https://github.com/ietf-tools/rfclint/compare/0.5.2...0.5.3
[0.5.2]: https://github.com/ietf-tools/rfclint/compare/0.5.1...0.5.2
[0.5.1]: https://github.com/ietf-tools/rfclint/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/ietf-tools/rfclint/compare/0.0.3...0.5.0
[0.0.3]: https://github.com/ietf-tools/rfclint/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/ietf-tools/rfclint/releases/tag/0.0.2
[v1.0.0]: https://github.com/ietf-tools/rfclint/compare/0.6.1...v1.0.0
