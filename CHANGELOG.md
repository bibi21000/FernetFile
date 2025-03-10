# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Added

### Changed

### Removed


## [0.1.6] - 2025/03/02

### Changed

- Update derivation function


## [0.1.5] - 2025/02/24

### Changed

- Test github publishing


## [0.1.4] - 2025/02/24

### Changed

- Test github publishing


## [0.1.3] - 2025/02/22

### Added

 - Add key derivation function (experimental)


## [0.1.1] - 2025/02/13

### Added

- Add test for small files


## [0.1.0] - 2025/02/11

Important !!!

This release break compatibility with old ones because of the change of the size
of the meta-informations !!! Export all your files before upgrading

### Added

### Changed

- Split for support of other cryptographic tools

### Removed


## [0.0.9] - 2025-02-09

### Added

- Add FernetStore and open method

### Changed

- Fix fileobj propagation


## [0.0.8] - 2025-02-07

### Added

- Test for lzma
- Failing test for gzip : io.UnsupportedOperation: Negative seek in write mode not supported
- Failing tests for tar append ... normal
- Add fast and furious zstd FernetFile class and open function

### Changed

- Change raised exceptions to io.* ones


## [0.0.7] - 2025-02-05

### Added

- Test for encrypting existing file
- Add documentation

### Removed

- Remove unused mtime parameter


## [0.0.6] - 2025-02-05

### Changed

- Update classifiers


## [0.0.5] - 2025-02-05

### Changed

- Fix tests
- Update doc

### Removed

- Support for python 3.8
- Support for python 3.13 (codecov-cli not compatible)


## [0.0.4] - 2025-02-04

### Changed

- Fix packaging


## [0.0.3] - 2025-02-04

### Changed

- Update doc
- Update test


## [0.0.2] - 2025-02-02

### Added

- Initial release
